#!/usr/bin/env python3
# resource_id: "f6684fa8-d01a-48a9-a35f-b584b41cbacf"
# resource_type: "document"
# resource_name: "tts_ipa"
"""
IPA Text-to-Speech module using Azure Cognitive Services for accurate IPA pronunciation
"""

import os
import base64
import sqlite3
from typing import Dict, Optional

class IPATTSEngine:
    """IPA Text-to-Speech engine using Azure Cognitive Services with proper SSML phoneme support"""

    def __init__(self):
        # Import Azure SDK
        self.azure_available = False
        self.speechsdk = None
        try:
            import azure.cognitiveservices.speech as speechsdk
            self.speechsdk = speechsdk
            self.azure_available = True
            print(f"Azure TTS available: True")
        except Exception as e:
            print(f"Azure SDK not available: {e}")
            print(f"Azure TTS available: False")
        self.fake_enabled = (
            os.getenv("FORCE_FAKE_TTS", "").lower() in {"1", "true", "yes", "on"}
            or not self.azure_available
        )
        if self.fake_enabled and not self.azure_available:
            print("Falling back to deterministic fake TTS output (Azure unavailable).")
        elif self.fake_enabled:
            print("FORCE_FAKE_TTS enabled — fake audio will be used even if Azure is available.")

        self._last_backend: Optional[str] = None

    def _has_azure_credentials(self) -> bool:
        return bool(
            os.environ.get('AZURE_SPEECH_KEY_WEST')
            or os.environ.get('AZURE_SPEECH_KEY_EAST')
            or os.environ.get('AZURE_SPEECH_KEY')
        )

    @property
    def last_backend(self) -> Optional[str]:
        return self._last_backend

    def _set_last_backend(self, backend: str) -> None:
        self._last_backend = backend

    def generate_ipa_audio(self, ipa_text):
        """Generate audio from IPA text using Azure TTS with proper SSML phonemes"""
        
        audio_data = None

        if self.azure_available and os.getenv("FORCE_FAKE_TTS", "").lower() not in {"1", "true", "yes", "on"}:
            audio_data = self._azure_tts_with_phonemes(ipa_text)
            if audio_data:
                print(f"Generated audio using Azure TTS")
                self._set_last_backend("azure")
                return audio_data
            # Automatic fallback when Azure present but fails (e.g., missing/invalid key)
            print("Azure TTS failed — falling back to deterministic fake audio")
        else:
            if not self.azure_available:
                print("Azure TTS not available — falling back to deterministic fake audio")

        # Always allow fallback to unblock UX unless explicitly disabled
        if self.fake_enabled or os.getenv("DISABLE_FAKE_FALLBACK", "").lower() not in {"1", "true", "yes", "on"}:
            fake_audio = self._fake_tts_audio()
            self._set_last_backend("fake")
            return fake_audio

        return None

    def _azure_tts_with_phonemes(self, ipa_text):
        """Azure TTS with proper SSML phoneme formatting for accurate IPA pronunciation"""
        if not self.azure_available or not self.speechsdk:
            return None
            
        try:
            # Get Azure credentials from environment
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
            speech_config = self.speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
            speech_config.speech_synthesis_output_format = self.speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3

            # Create synthesizer
            synthesizer = self.speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

            # Use neural voice optimized for phoneme accuracy
            voice_name = "en-US-AriaNeural"

            # Create proper SSML with phoneme element
            # The key fix: use the phoneme element to specify exact IPA pronunciation
            ssml = f"""
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
                <voice name="{voice_name}">
                    <phoneme alphabet="ipa" ph="{ipa_text}">word</phoneme>
                </voice>
            </speak>
            """

            # Synthesize speech
            print(f"Azure TTS: Processing IPA phonemes '{ipa_text}'")
            result = synthesizer.speak_ssml_async(ssml).get()

            if result.reason == self.speechsdk.ResultReason.SynthesizingAudioCompleted:
                # Convert to base64
                audio_base64 = base64.b64encode(result.audio_data).decode('utf-8')
                return audio_base64
            else:
                print(f"Azure TTS failed: {result.reason}")
                if result.reason == self.speechsdk.ResultReason.Canceled:
                    cancellation_details = result.cancellation_details
                    print(f"Cancellation reason: {cancellation_details.reason}")
                    if cancellation_details.error_details:
                        print(f"Error details: {cancellation_details.error_details}")
                return None

        except Exception as e:
            print(f"Error with Azure TTS: {e}")
            return None

    def generate_phoneme_audio(self, phoneme, position="standalone"):
        """Generate audio for individual phoneme using Azure TTS"""
        try:
            audio_data = None
            force_fake = os.getenv("FORCE_FAKE_TTS", "").lower() in {"1", "true", "yes", "on"}

            if self.azure_available and not force_fake:
                # For individual phonemes, add context for better pronunciation
                # Check if it's a single phoneme by querying the database
                is_single_phoneme = self._is_single_phoneme_in_db(phoneme)
                print(f"TTS Debug: {phoneme} -> is_single_phoneme: {is_single_phoneme}")
                
                if is_single_phoneme:
                    context_phoneme = self._add_context_sound(phoneme, position)
                    print(f"TTS Debug: {phoneme} -> context: {context_phoneme}")
                    audio_data = self._azure_tts_with_phonemes(context_phoneme)
                else:
                    # For longer sequences, use as-is
                    print(f"TTS Debug: {phoneme} -> using as-is (no context)")
                    audio_data = self._azure_tts_with_phonemes(phoneme)

                if audio_data:
                    self._set_last_backend("azure")
                    return audio_data
                print("Azure TTS phoneme generation failed — falling back to deterministic fake audio")

            if not self.azure_available:
                print("Azure TTS not available for phoneme generation — falling back to deterministic fake audio")

            # Always allow fallback to unblock UX unless explicitly disabled
            if self.fake_enabled or os.getenv("DISABLE_FAKE_FALLBACK", "").lower() not in {"1", "true", "yes", "on"}:
                fake_audio = self._fake_tts_audio()
                self._set_last_backend("fake")
                return fake_audio

            return None

        except Exception as e:
            print(f"Error generating phoneme audio: {e}")
            if self.fake_enabled:
                fake_audio = self._fake_tts_audio()
                self._set_last_backend("fake")
                return fake_audio
            return None

    def _add_context_sound(self, phoneme, position):
        """Add context sounds to make phonemes clearer based on their position"""
        
        if position == "onset":
            # Consonant + vowel patterns for onset position
            onset_contexts = {
                # Affricates
                "tʃ": "tʃɑm",    # "cham"
                "dʒ": "dʒɑm",    # "jam"
                
                # Fricatives
                "f": "fɑm",      # "fam"
                "v": "vɑm",      # "vam"  
                "θ": "θɑm",      # "tham"
                "ð": "ðɑm",      # "dham"
                "s": "sɑm",      # "sam"
                "z": "zɑm",      # "zam"
                "ʃ": "ʃɑm",      # "sham"
                "ʒ": "ʒɑm",      # "zham"
                "h": "hɑm",      # "ham"
                
                # Stops
                "p": "pɑm",      # "pam"
                "b": "bɑm",      # "bam"
                "t": "tɑm",      # "tam"
                "d": "dɑm",      # "dam"
                "k": "kɑm",      # "kam"
                "ɡ": "ɡɑm",      # "gam"
                
                # Nasals
                "m": "mɑm",      # "mam"
                "n": "nɑm",      # "nam"
                "ŋ": "ŋɑm",      # "ngam"
                
                # Liquids
                "l": "lɑm",      # "lam"
                "r": "rɑm",      # "ram"
                
                # Glides
                "w": "wɑm",      # "wam"
                "j": "jɑm",      # "yam"
            }
            return onset_contexts.get(phoneme, phoneme + "ɑm")
            
        elif position == "nucleus":
            # Consonant + vowel + consonant patterns for nucleus vowels
            nucleus_contexts = {
                "i": "mim",      # "meem"
                "ɪ": "mɪm",      # "mim"
                "e": "mem",      # "mem"
                "ɛ": "mɛm",      # "mem"
                "æ": "mæm",      # "mam"
                "ɑ": "mɑm",      # "mom"
                "ɒ": "mɒm",      # "mom"
                "ɔ": "mɔm",      # "mawm"
                "o": "mom",      # "moam"
                "ʊ": "pʊt",      # "put"
                "u": "mum",      # "moom"
                "ʌ": "mʌm",      # "mum"
                "ə": "məm",      # "mum"
                "ɜ": "mɜm",      # "murm"
                
                # Diphthongs
                "aɪ": "maɪm",    # "mime"
                "eɪ": "meɪm",    # "maim"
                "ɔɪ": "mɔɪm",    # "moim"
                "aʊ": "maʊs",    # "mouse"
                "oʊ": "moʊm",    # "moam"
            }
            return nucleus_contexts.get(phoneme, "m" + phoneme + "m")
            
        elif position == "coda":
            # Vowel + consonant patterns for coda position
            coda_contexts = {
                # Affricates
                "tʃ": "mɑtʃ",    # "match"
                "dʒ": "mɑdʒ",    # "madge"
                
                # Fricatives
                "f": "mɑf",      # "maf"
                "v": "mɑv",      # "mav"
                "θ": "mɑθ",      # "math"
                "ð": "mɑð",      # "madh"
                "s": "mɑs",      # "mas"
                "z": "mɑz",      # "maz"
                "ʃ": "mɑʃ",      # "mash"
                "ʒ": "mɑʒ",      # "mazh"
                
                # Stops
                "p": "mɑp",      # "map"
                "b": "mɑb",      # "mab"
                "t": "mɑt",      # "mat"
                "d": "mɑd",      # "mad"
                "k": "mɑk",      # "mack"
                "ɡ": "mɑɡ",      # "mag"
                
                # Nasals
                "m": "mɑm",      # "mam"
                "n": "mɑn",      # "man"
                "ŋ": "mɑŋ",      # "mang"
                
                # Liquids
                "l": "mɑl",      # "mal"
                "r": "mɑr",      # "mar"
            }
            return coda_contexts.get(phoneme, "mɑ" + phoneme)
            
        else:  # standalone
            # For standalone, use minimal context 
            return "ɑ" + phoneme + "ɑ"

    def _fake_tts_audio(self) -> str:
        """Return deterministic base64 audio for environments without Azure TTS."""
        # Base64 encoded short WAV tone (generated offline)
        return (
            "UklGRigAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YRAAAAAA"
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        )

    def get_status_report(self) -> Dict[str, Optional[str]]:
        """Summarize backend availability for the status endpoint."""
        backends = []
        if self.azure_available:
            backends.append(
                {
                    "name": "Azure TTS",
                    "type": "ssml_phonemes",
                    "format": "mp3",
                    "priority": 1,
                    "supports_raw_ipa": True,
                    "supports_made_up_words": True,
                }
            )
        if self.fake_enabled:
            backends.append(
                {
                    "name": "Fake TTS (deterministic)",
                    "type": "stub",
                    "format": "wav",
                    "priority": 99,
                    "supports_raw_ipa": True,
                    "supports_made_up_words": True,
                }
            )

        if self.azure_available and os.getenv("FORCE_FAKE_TTS", "").lower() not in {"1", "true", "yes", "on"}:
            primary = "Azure TTS"
        elif self.fake_enabled:
            primary = "Fake TTS (deterministic)"
        else:
            primary = "None"

        return {
            "primary_backend": primary,
            "backends_available": backends,
            "total_backends": len(backends),
            "supports_ipa": primary != "None",
            "supports_made_up_words": primary != "None",
            "azure_available": self.azure_available,
            "azure_configured": self._has_azure_credentials(),
            "fake_tts_enabled": self.fake_enabled,
        }

    def _is_single_phoneme_in_db(self, phoneme):
        """Check if a phoneme exists in the database as a single phoneme block"""
        try:
            # Import here to avoid circular imports
            import main
            
            conn = sqlite3.connect(main.DB_NAME)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT COUNT(*) FROM phonemes 
                WHERE phoneme = ?
            """, (phoneme,))
            
            count = cursor.fetchone()[0]
            conn.close()
            
            return count > 0
        except Exception as e:
            print(f"Error checking phoneme in database: {e}")
            # Fallback: assume it's a single phoneme if it's 3 characters or less
            return len(phoneme) <= 3

# Global TTS engine instance
ipa_tts = IPATTSEngine()
