#!/usr/bin/env python3
# resource_id: "1bea4ae4-df91-4c82-acb3-6e050ca8f8e0"
# resource_type: "document"
# resource_name: "tts_ipa_old"
"""
IPA Text-to-Speech module with multiple backends for high-quality pronunciation
Supports eSpeak-NG (primary) and Azure Cognitive Services (fallback)
"""

import os
import base64
import subprocess
import tempfile

# Try to import Azure SDK, but make it optional
try:
    import azure.cognitiveservices.speech as speechsdk
    AZURE_AVAILABLE = True
except ImportError as e:
    print(f"Azure SDK not available: {e}")
    speechsdk = None
    AZURE_AVAILABLE = False

class IPATTSEngine:
    """IPA Text-to-Speech engine with multiple backends for optimal IPA pronunciation"""

    def __init__(self):
        # Check for eSpeak-NG availability
        self.espeak_available = self._check_espeak_available()
        self.azure_available = AZURE_AVAILABLE
        print(f"eSpeak-NG available: {self.espeak_available}")
        print(f"Azure TTS available: {self.azure_available}")

    def _check_espeak_available(self):
        """Check if eSpeak-NG is available on the system"""
        try:
            result = subprocess.run(['espeak-ng', '--version'], 
                                    capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False

    def generate_ipa_audio(self, ipa_text):
        """Generate audio from IPA text using the best available backend"""
        
        # Try eSpeak-NG first for better IPA accuracy
        if self.espeak_available:
            audio_data = self._try_espeak_ng(ipa_text)
            if audio_data:
                print(f"Generated audio using eSpeak-NG")
                return audio_data
        
        # Fallback to Azure TTS if available
        if self.azure_available:
            audio_data = self._try_azure_tts(ipa_text)
            if audio_data:
                print(f"Generated audio using Azure TTS")
                return audio_data
        
        print("All TTS backends failed")
        return None

    def _try_espeak_ng(self, ipa_text):
        """Try eSpeak-NG for direct IPA pronunciation"""
        try:
            # Create temporary file for audio output
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
                temp_path = temp_file.name

            # Use eSpeak-NG with IPA input
            cmd = [
                'espeak-ng',
                '--ipa',  # Input is IPA
                '-s', '150',  # Speed (words per minute)
                '-a', '100',  # Amplitude (0-200)
                '-g', '10',   # Gap between words (10ms units)
                '-w', temp_path,  # Write to file
                ipa_text
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                # Read the generated audio file
                with open(temp_path, 'rb') as f:
                    audio_bytes = f.read()
                
                # Clean up temporary file
                os.unlink(temp_path)
                
                if len(audio_bytes) > 0:
                    # Convert to base64 for consistency with Azure TTS
                    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
                    return audio_base64
                else:
                    print("eSpeak-NG generated empty audio")
                    return None
            else:
                print(f"eSpeak-NG error: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"Error with eSpeak-NG: {e}")
            return None
        finally:
            # Ensure cleanup
            if 'temp_path' in locals() and os.path.exists(temp_path):
                try:
                    os.unlink(temp_path)
                except:
                    pass

    def _try_azure_tts(self, ipa_text):
        """Try Azure Cognitive Services Speech with raw IPA."""
        if not self.azure_available:
            return None
            
        try:
            # Get Azure credentials from environment - try new dual-region setup first
            speech_key_west = os.environ.get('AZURE_SPEECH_KEY_WEST')
            speech_key_east = os.environ.get('AZURE_SPEECH_KEY_EAST')
            speech_region_west = os.environ.get('AZURE_SPEECH_REGION_WEST', 'westus')
            speech_region_east = os.environ.get('AZURE_SPEECH_REGION_EAST', 'eastus')

            # Use West US by default, fallback to East US if West fails
            speech_key = speech_key_west
            speech_region = speech_region_west

            # Fallback to legacy single key setup if new keys not available
            if not speech_key:
                speech_key = os.environ.get('AZURE_SPEECH_KEY')
                speech_region = os.environ.get('AZURE_SPEECH_REGION', 'westus2')

            if not speech_key:
                print("No Azure Speech key found in environment variables")
                return None

            # Set up speech config
            speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config.speech_synthesis_output_format = speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3

            # Create synthesizer
            synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

            # Use raw IPA directly with SSML phoneme tags
            voice_name = "en-US-AriaNeural"

            ssml = f"""
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
                <voice name="{voice_name}">
                    <phoneme alphabet="ipa" ph="{ipa_text}">{ipa_text}</phoneme>
                </voice>
            </speak>
            """

            # Synthesize speech
            print(f"Azure TTS: Processing raw IPA '{ipa_text}'")
            result = synthesizer.speak_ssml_async(ssml).get()

            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                # Convert to base64
                audio_base64 = base64.b64encode(result.audio_data).decode('utf-8')
                return audio_base64
            else:
                print(f"Azure TTS failed: {result.reason}")
                if result.reason == speechsdk.ResultReason.Canceled:
                    cancellation_details = result.cancellation_details
                    print(f"Cancellation reason: {cancellation_details.reason}")
                    if cancellation_details.error_details:
                        print(f"Error details: {cancellation_details.error_details}")
                return None

        except Exception as e:
            print(f"Error with Azure TTS: {e}")
            return None

    def generate_phoneme_audio(self, phoneme, position="standalone"):
        """Generate audio for individual phoneme with context sounds"""
        try:
            # For eSpeak-NG, we can often use raw phonemes without context
            # Try raw phoneme first with eSpeak-NG
            if self.espeak_available:
                raw_audio = self._try_espeak_ng(phoneme)
                if raw_audio:
                    print(f"Generated raw phoneme audio using eSpeak-NG")
                    return raw_audio
            
            # Fallback to context-based approach for Azure TTS
            context_phoneme = self._add_context_sound(phoneme, position)
            return self.generate_ipa_audio(context_phoneme)

        except Exception as e:
            print(f"Error generating phoneme audio: {e}")
            return None

    def _add_context_sound(self, phoneme, position):
        """Add context sounds to make phonemes clearer based on their position"""
        
        # Use safe, family-friendly context words to help Azure TTS distinguish similar sounds
        
        if position == "onset":
            # Use safe consonant + vowel patterns for onset consonants
            # Avoid potentially offensive combinations
            safe_endings = {
                # Use 'ɑ' (ah) as it's clear and unlikely to create profanity
                'default': phoneme + "ɑ"  # e.g., pɑ, tɑ, kɑ
            }
            return safe_endings.get(phoneme, safe_endings['default'])
            
        elif position == "nucleus":
            # Use safe consonant frames for nucleus vowels
            safe_contexts = {
                "i": "m" + phoneme,      # mi (like "me")
                "ɪ": "m" + phoneme,      # mɪ (like "mitt" without t)  
                "u": "m" + phoneme,      # mu (like "moo" without second o)
                "ʊ": "w" + phoneme + "d", # wʊd (like "wood")
                "ɛ": "m" + phoneme,      # mɛ (like "met" without t)
                "æ": "m" + phoneme,      # mæ (like "mat" without t)
                "ɑ": "m" + phoneme,      # mɑ (like "ma")
                "ɔ": "m" + phoneme,      # mɔ (like "more" without re)
                "ə": "m" + phoneme,      # mə (like "mud" without d)
                "ʌ": "m" + phoneme,      # mʌ (like "mud" without d)
                # Default: use safe 'm' + vowel pattern
                'default': "m" + phoneme
            }
            return safe_contexts.get(phoneme, safe_contexts['default'])
            
        elif position == "coda":
            # Use safe vowel + consonant patterns for coda consonants
            # Use 'ɑ' (ah) as the vowel - clear and safe
            return "ɑ" + phoneme  # e.g., ɑt, ɑn, ɑk
            
        else:  # standalone
            # For standalone, add minimal safe context with 'ɑ'
            return "ɑ" + phoneme + "ɑ"  # e.g., ɑtɑ for isolated t

# Global TTS engine instance
ipa_tts = IPATTSEngine()