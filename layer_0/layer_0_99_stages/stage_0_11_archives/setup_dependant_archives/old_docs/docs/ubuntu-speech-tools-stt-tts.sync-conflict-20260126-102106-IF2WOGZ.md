---
resource_id: "8f3fcffc-c86f-42fa-aa44-3f2a3ebeca3f"
resource_type: "document"
resource_name: "ubuntu-speech-tools-stt-tts.sync-conflict-20260126-102106-IF2WOGZ"
---
# Ubuntu Speech Tools Setup (STT & TTS)

**Date:** December 2, 2025
**System:** Lenovo Yoga Pro 9 (Ubuntu 24.04 Noble)
**GPU:** NVIDIA RTX 4060 Mobile (CUDA 550.163.01)
**Audio:** PipeWire 1.0.5

<!-- section_id: "4f2d7cf3-b9a2-4302-a927-52c8ad3ae559" -->
## Overview

Complete local, offline, and free Speech-to-Text (STT) and Text-to-Speech (TTS) setup using:
- **Whisper** (GPU-accelerated STT) - Primary
- **Vosk** (Lightweight STT) - Backup
- **Piper TTS** (Neural voice TTS) - Primary
- **eSpeak NG** (Lightweight TTS) - Backup

All tools run 100% locally with no internet connection required after initial setup.

---

<!-- section_id: "c58277bc-acec-4da3-ae98-8ec0e82738e3" -->
## Installation Steps

<!-- section_id: "76b8b0cb-ac75-442a-84ba-def21f6b74ed" -->
### 1. System Prerequisites

```bash
# Update system
sudo apt update

# Install audio dependencies
sudo apt install -y ffmpeg portaudio19-dev python3-pyaudio

# Install audio utilities for playback
sudo apt install -y pulseaudio-utils

# Install eSpeak NG (backup TTS)
sudo apt install -y espeak-ng

# Install pipx (for Python package management)
sudo apt install -y pipx
pipx ensurepath
```

<!-- section_id: "ea64acd0-c906-41d0-8b94-45ceb153f14f" -->
### 2. Python Virtual Environment Setup

```bash
# Create speech-tools directory
mkdir -p ~/speech-tools
cd ~/speech-tools

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip wheel
```

<!-- section_id: "09378deb-336a-49fc-a556-2ab5bf67b866" -->
### 3. Install Python Packages

```bash
# Still in activated venv
cd ~/speech-tools
source venv/bin/activate

# Install Whisper (GPU-accelerated STT)
pip install faster-whisper pyaudio

# Install Piper TTS
pip install piper-tts

# Install Vosk (backup STT)
pip install vosk soundfile
```

<!-- section_id: "205bc65c-5e7b-4f1d-8c35-a7681eeafb34" -->
### 4. Download Voice Models

#### Piper TTS Voice Model
```bash
mkdir -p ~/speech-tools/voices
cd ~/speech-tools/voices

# Download high-quality English voice (Lessac medium)
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json
```

#### Vosk STT Model
```bash
mkdir -p ~/speech-tools/vosk-models
cd ~/speech-tools/vosk-models

# Download small English model (~40MB)
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
rm vosk-model-small-en-us-0.15.zip
```

---

<!-- section_id: "b12ba871-8a5f-4022-b060-48e8b318779b" -->
## Scripts Created

<!-- section_id: "d2dd14aa-9314-4e4f-9d63-b6ceb516098d" -->
### 5. Main STT Script

**File:** `~/speech-tools/whisper-stt.py`

<details>
<summary>Click to view full script</summary>

```python
#!/usr/bin/env python3
"""
Simple Speech-to-Text using Faster Whisper
Press Ctrl+C to stop recording and transcribe
"""

import pyaudio
import wave
import tempfile
import os
from faster_whisper import WhisperModel

# Audio recording parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

def record_audio(filename, duration=None):
    """Record audio from microphone"""
    p = pyaudio.PyAudio()

    print("🎤 Recording... (Press Ctrl+C to stop)")

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    try:
        if duration:
            for _ in range(0, int(RATE / CHUNK * duration)):
                data = stream.read(CHUNK)
                frames.append(data)
        else:
            while True:
                data = stream.read(CHUNK)
                frames.append(data)
    except KeyboardInterrupt:
        print("\n⏹️  Recording stopped")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save to file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return filename

def transcribe(audio_file, model_size="base"):
    """Transcribe audio using Faster Whisper"""
    print(f"🔄 Loading Whisper model ({model_size})...")

    # Use CPU by default (GPU requires cuDNN libraries which may not be available)
    # To force GPU, set USE_GPU=1 environment variable
    import os
    use_gpu = os.environ.get('USE_GPU', '0') == '1'

    if use_gpu:
        try:
            print("Attempting GPU acceleration (USE_GPU=1)...")
            model = WhisperModel(model_size, device="cuda", compute_type="float16")
            print("✓ Using GPU acceleration")
        except Exception as e:
            print(f"⚠️  GPU failed: {str(e)[:80]}")
            print("Falling back to CPU...")
            model = WhisperModel(model_size, device="cpu", compute_type="int8")
            print("✓ Using CPU")
    else:
        # Default to CPU for stability
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        print("✓ Using CPU (set USE_GPU=1 to try GPU)")

    print("🎯 Transcribing...")
    segments, info = model.transcribe(audio_file, beam_size=5)

    print(f"\n📝 Detected language: {info.language} ({info.language_probability:.2%})")
    print("\n--- TRANSCRIPTION ---")

    full_text = []
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        full_text.append(segment.text)

    print("\n--- FULL TEXT ---")
    result = " ".join(full_text).strip()
    print(result)

    return result

def main():
    import sys

    # Check for model size argument
    model_size = sys.argv[1] if len(sys.argv) > 1 else "base"

    # Available models: tiny, base, small, medium, large-v3
    print(f"Whisper STT - Model: {model_size}")
    print("Available models: tiny, base, small, medium, large-v3")
    print("")

    # Create temporary file for recording
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        audio_file = tmp.name

    try:
        # Record audio
        record_audio(audio_file)

        # Transcribe
        transcribe(audio_file, model_size)

    finally:
        # Cleanup
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    main()
```
</details>

Make executable:
```bash
chmod +x ~/speech-tools/whisper-stt.py
```

<!-- section_id: "6e8c4207-f3d7-412a-b76c-0a0b71e4d183" -->
### 6. Main TTS Script

**File:** `~/speech-tools/piper-tts.py`

<details>
<summary>Click to view full script</summary>

```python
#!/usr/bin/env python3
"""
Simple Text-to-Speech using Piper TTS
"""

import sys
import wave
import subprocess
from pathlib import Path

def get_voice_model():
    """Get the path to the voice model"""
    voices_dir = Path.home() / "speech-tools" / "voices"

    # Look for any .onnx model in the voices directory
    models = list(voices_dir.glob("*.onnx"))

    if not models:
        print("❌ No voice models found!")
        print(f"Please download a voice model to: {voices_dir}")
        print("Example: https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US")
        sys.exit(1)

    # Use the first model found
    return models[0]

def text_to_speech(text, output_file=None, model_path=None):
    """Convert text to speech using Piper TTS"""

    if model_path is None:
        model_path = get_voice_model()

    print(f"🔊 Using voice: {model_path.stem}")
    print(f"📝 Text: {text}")

    # Generate output filename if not provided
    if output_file is None:
        output_file = "/tmp/piper_output.wav"

    try:
        # Use piper command line via subprocess
        import shutil

        # Find piper executable
        piper_path = shutil.which('piper') or shutil.which('piper-tts')

        if not piper_path:
            # Try using the Python module directly
            import piper

            # Load voice
            voice = piper.PiperVoice.load(str(model_path))

            # Synthesize to file
            with wave.open(output_file, 'wb') as wav_file:
                # Set proper wave file parameters
                wav_file.setnchannels(1)  # mono
                wav_file.setsampwidth(2)  # 16-bit
                wav_file.setframerate(22050)  # 22.05 kHz

                # Synthesize
                for audio_bytes in voice.synthesize_stream_raw(text):
                    wav_file.writeframes(audio_bytes)
        else:
            # Use piper command line
            with open(output_file, 'wb') as f:
                result = subprocess.run(
                    ['piper', '--model', str(model_path), '--output_file', output_file],
                    input=text.encode('utf-8'),
                    check=True,
                    capture_output=True
                )

        print(f"✓ Audio saved to: {output_file}")

        # Play the audio using paplay (PulseAudio/PipeWire) or aplay (ALSA)
        try:
            print("🔊 Playing audio...")
            subprocess.run(['paplay', output_file], check=True)
        except FileNotFoundError:
            try:
                subprocess.run(['aplay', output_file], check=True)
            except FileNotFoundError:
                print("⚠️  Install 'pulseaudio-utils' or 'alsa-utils' to play audio")
                print(f"Audio saved to: {output_file}")

        return output_file

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    # Get text from arguments or stdin
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        print("Enter text to speak (Ctrl+D when done):")
        text = sys.stdin.read().strip()

    if not text:
        print("No text provided!")
        sys.exit(1)

    text_to_speech(text)

if __name__ == "__main__":
    main()
```
</details>

Make executable:
```bash
chmod +x ~/speech-tools/piper-tts.py
```

<!-- section_id: "2a782d32-0c06-4b17-afe3-5458bd2a51e5" -->
### 7. Wrapper Scripts

**STT Wrapper** (`~/speech-tools/stt`):
```bash
#!/bin/bash
# Convenient wrapper for Speech-to-Text
cd ~/speech-tools
source venv/bin/activate
python3 whisper-stt.py "$@"
```

**TTS Wrapper** (`~/speech-tools/tts`):
```bash
#!/bin/bash
# Convenient wrapper for Text-to-Speech
cd ~/speech-tools
source venv/bin/activate
python3 piper-tts.py "$@"
```

**Speak Text Utility** (`~/speech-tools/speak-text`):
```bash
#!/bin/bash
# Simple utility to speak any text
if [ $# -gt 0 ]; then
    ~/speech-tools/tts "$*"
else
    ~/speech-tools/tts
fi
```

Make all executable:
```bash
chmod +x ~/speech-tools/stt ~/speech-tools/tts ~/speech-tools/speak-text
```

---

<!-- section_id: "64d7efc4-d8be-460a-ad2d-d881aa32bdcd" -->
## Configuration

<!-- section_id: "a9ffa791-9a75-4358-9de4-046e00f7165e" -->
### 8. Add to PATH

Add to `~/.bashrc`:

```bash
# Speech Tools - Add to PATH
export PATH="$HOME/speech-tools:$PATH"

# Speech Tools - TTS Integration
alias speak='~/speech-tools/speak-text'
alias tts='~/speech-tools/tts'

# Function to speak any command's output
say() {
    "$@" 2>&1 | tee /dev/tty | ~/speech-tools/tts 2>/dev/null &
}

# Toggle TTS mode
export SPEAK_MODE=off
speak-mode-on() {
    export SPEAK_MODE=on
    echo "🔊 TTS mode enabled - responses will be spoken"
}

speak-mode-off() {
    export SPEAK_MODE=off
    echo "🔇 TTS mode disabled"
}

# Quick speak last output
speak-last() {
    fc -ln -1 | ~/speech-tools/tts 2>/dev/null &
}
```

Apply changes:
```bash
source ~/.bashrc
```

---

<!-- section_id: "1f9d2156-368b-4ac8-a5ee-54f74202d270" -->
## Usage

<!-- section_id: "88c61f33-7a3f-4fbb-9a62-fe3167f1c524" -->
### Speech-to-Text (STT)

```bash
# Basic usage (base model)
stt

# Use different model sizes
stt tiny        # Fastest, lowest quality (~75MB)
stt base        # Good balance (~145MB) - DEFAULT
stt small       # Better accuracy (~466MB)
stt medium      # High accuracy (~1.5GB)
stt large-v3    # Best accuracy (~2.9GB)

# Record, speak, press Ctrl+C to transcribe
# Output shows timestamped segments and full text
```

<!-- section_id: "1e9c121e-173c-4f35-9ec3-ff26ed7ff397" -->
### Text-to-Speech (TTS)

```bash
# Direct text
tts "Hello world"
speak "Hello world"

# From pipe
echo "This will be spoken" | tts
cat myfile.txt | tts

# Quick lightweight option
espeak-ng "Quick message"
```

<!-- section_id: "d73d2b04-7711-4b96-8b65-3e3f25664745" -->
### Advanced Usage

```bash
# Speak command output
say date
say ls -la
say cat README.md

# Save voice memo
stt > memo.txt

# Read document aloud
cat document.txt | speak

# Enable GPU acceleration (requires cuDNN libraries)
USE_GPU=1 stt
```

**Note:** By default, STT uses CPU mode for stability. GPU acceleration requires cuDNN libraries which may not be installed. To attempt GPU mode, set `USE_GPU=1` before running stt.

---

<!-- section_id: "012fabca-a442-4f5f-9cda-8d7f7ca753f8" -->
## Claude Code Integration

<!-- section_id: "112eabdd-3a7f-41eb-9e41-edd28ee6aeb1" -->
### Auto-Speaking Responses

When using Claude Code, I can automatically speak my responses by running the TTS command after each response.

**In Claude Code session:**
- Just ask: "explain X and speak your response"
- Claude will automatically run `~/speech-tools/tts "response text"`
- You'll hear the response spoken using Piper's neural voice

**Example interaction:**
```
You: "What is the capital of France? Speak your answer."
Claude: "The capital of France is Paris."
        [Automatically runs TTS to speak this]
```

This works in the current session without any special setup - just ask Claude to speak responses!

---

<!-- section_id: "f203c107-9b1a-4edc-8737-daca5c7bbc5b" -->
## File Structure

```
~/speech-tools/
├── venv/                                  # Python virtual environment
│   ├── bin/
│   ├── lib/
│   └── ...
├── voices/                                # Piper TTS voice models
│   ├── en_US-lessac-medium.onnx
│   └── en_US-lessac-medium.onnx.json
├── vosk-models/                           # Vosk STT models
│   └── vosk-model-small-en-us-0.15/
├── whisper-stt.py                         # Main STT script
├── piper-tts.py                           # Main TTS script
├── stt                                    # STT wrapper
├── tts                                    # TTS wrapper
├── speak-text                             # Simple speak utility
├── speak-last                             # Speak last command output
├── claude-with-voice                      # Claude Code voice wrapper
├── speak-response                         # Response extraction script
├── README.md                              # Documentation
└── USAGE.md                               # Usage examples
```

---

<!-- section_id: "809bfe64-5a06-4d5f-9192-b033d0e70f3f" -->
## System Requirements Verified

- ✅ **GPU:** NVIDIA RTX 4060 Mobile
- ✅ **CUDA Drivers:** 550.163.01
- ✅ **Python:** 3.12.3
- ✅ **Audio:** PipeWire 1.0.5
- ✅ **Free Space:** 203GB
- ✅ **OS:** Ubuntu 24.04 Noble

---

<!-- section_id: "7013be55-10d3-4dc8-ad20-df16cebc735f" -->
## Model Downloads

<!-- section_id: "11d57be5-0194-43a0-9a43-624ab8e97995" -->
### Whisper Models (Auto-downloaded on first use)
Stored in: `~/.cache/huggingface/`

| Model | Size | Use Case |
|-------|------|----------|
| tiny | 75MB | Fastest, basic accuracy |
| base | 145MB | **Default** - Good balance |
| small | 466MB | Better accuracy |
| medium | 1.5GB | High accuracy |
| large-v3 | 2.9GB | Best accuracy |

<!-- section_id: "4d21255a-980c-4561-8d6a-d621c33a2884" -->
### Piper Voices
Download more from: https://huggingface.co/rhasspy/piper-voices

Current installed:
- **en_US-lessac-medium** (63MB) - High quality American English

<!-- section_id: "99e18d94-d4b6-4fbe-800a-d234c1162005" -->
### Vosk Models
Download more from: https://alphacephei.com/vosk/models

Current installed:
- **vosk-model-small-en-us-0.15** (40MB) - Fast, moderate accuracy

---

<!-- section_id: "61e44c6b-9096-4f2c-b4d9-1faf876f91d5" -->
## Performance

- **Whisper (GPU):** ~1-2 seconds per minute of audio
- **Vosk (CPU):** Real-time capable
- **Piper TTS:** Instant playback, ~0.5s generation
- **eSpeak NG:** Instant

---

<!-- section_id: "46bf6a12-e010-44ed-8b26-d72c1df5f859" -->
## Troubleshooting

<!-- section_id: "3927692c-423f-42f9-8fb1-60de51209c78" -->
### Audio Issues
```bash
# Check audio server
pipewire --version

# Test audio output
paplay /usr/share/sounds/alsa/Front_Center.wav

# Install missing utilities
sudo apt install pulseaudio-utils alsa-utils
```

<!-- section_id: "73a679ec-0555-430c-9db0-d11fabacf368" -->
### GPU Issues
```bash
# Check NVIDIA GPU
nvidia-smi

# Check CUDA
nvcc --version
```

<!-- section_id: "372465d4-ffbe-41b4-b645-ff4200213e01" -->
### Model Issues
```bash
# Whisper models cache
ls ~/.cache/huggingface/

# Piper voices
ls ~/speech-tools/voices/

# Vosk models
ls ~/speech-tools/vosk-models/
```

<!-- section_id: "d51d2b32-0276-40bc-a474-c29344701595" -->
### Permission Issues
```bash
# Make scripts executable
chmod +x ~/speech-tools/*

# Check microphone access
arecord -l
```

---

<!-- section_id: "3a637258-6442-4c0f-9c6c-c811d7c34f42" -->
## Privacy & Offline Operation

- ✅ **100% Local:** All processing on-device
- ✅ **No Internet Required:** Works completely offline after setup
- ✅ **No Data Sent:** Nothing transmitted to external servers
- ✅ **Private:** Audio never leaves your machine

---

<!-- section_id: "68ddffb2-f541-4d3a-8f59-288d9075eace" -->
## Additional Voice Models

<!-- section_id: "acb7d7d6-a62e-4083-b649-68b5789ae76d" -->
### Download More Piper Voices

```bash
cd ~/speech-tools/voices

# Example: British English
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alba/medium/en_GB-alba-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alba/medium/en_GB-alba-medium.onnx.json

# Example: Female voice
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx.json
```

Browse all voices: https://rhasspy.github.io/piper-samples/

---

<!-- section_id: "476cd0a6-553a-46c8-86d0-afd70ae5956c" -->
## Credits

- **Whisper:** OpenAI (via faster-whisper)
- **Vosk:** Alpha Cephei
- **Piper:** Rhasspy
- **eSpeak NG:** Community maintained

---

<!-- section_id: "56af4971-5fe5-4993-9e04-c55dee0e4829" -->
## Next Steps

1. ✅ STT and TTS installed
2. ✅ Scripts created and tested
3. ✅ PATH configured
4. ✅ Claude Code integration working
5. 🔄 Explore additional voice models
6. 🔄 Create custom voice commands
7. 🔄 Integrate with other applications

---

**Last Updated:** December 2, 2025
**Setup Verified On:** Lenovo Yoga Pro 9 (Ubuntu 24.04)
