---
resource_id: "dbc8b271-7b7f-4315-9a5f-03bd245a77d2"
resource_type: "document"
resource_name: "ubuntu-speech-tools-stt-tts"
---
# Ubuntu Speech Tools Setup (STT & TTS)

**Date:** December 2, 2025
**System:** Lenovo Yoga Pro 9 (Ubuntu 24.04 Noble)
**GPU:** NVIDIA RTX 4060 Mobile (CUDA 550.163.01)
**Audio:** PipeWire 1.0.5

<!-- section_id: "5330b101-50a0-4bf6-97bd-ddd5c76884f7" -->
## Overview

Complete local, offline, and free Speech-to-Text (STT) and Text-to-Speech (TTS) setup using:
- **Whisper** (GPU-accelerated STT) - Primary
- **Vosk** (Lightweight STT) - Backup
- **Piper TTS** (Neural voice TTS) - Primary
- **eSpeak NG** (Lightweight TTS) - Backup

All tools run 100% locally with no internet connection required after initial setup.

---

<!-- section_id: "34595b31-c1f4-407a-9f5e-9b2f8d3462b4" -->
## Installation Steps

<!-- section_id: "2f225c72-0916-4654-8b74-d358696798ca" -->
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

<!-- section_id: "4e108c8d-9589-4032-ab9e-867bc0bcc193" -->
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

<!-- section_id: "3d0cc9eb-9796-49f9-87f1-f5ade7438847" -->
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

<!-- section_id: "f2d1c2d4-dd44-48a2-bd63-a80ee2d52d32" -->
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

<!-- section_id: "c1e478a6-053b-4971-9e7e-4aa559f3e3a1" -->
## Scripts Created

<!-- section_id: "2048ff6a-48cb-43d1-bbbe-d4d87ffdb9d6" -->
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

<!-- section_id: "7df13174-f09b-46c5-8423-93622a006fd4" -->
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

<!-- section_id: "a4cb600c-0d25-4c2b-92bb-d22c82b17271" -->
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

<!-- section_id: "74acfd2f-9a38-4802-90c1-2dcf26434b61" -->
## Configuration

<!-- section_id: "2da3f936-f7a3-43ce-8cf8-1c4b1f4558d1" -->
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

<!-- section_id: "d146adac-b222-4d44-b05a-10bd4e0a574e" -->
## Usage

<!-- section_id: "9cf4ecd4-1301-4e06-97bb-b0937e10d90f" -->
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

<!-- section_id: "e3e5bb9e-2dd4-4bf0-824b-591b334154f3" -->
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

<!-- section_id: "39bd2ab2-7bce-42aa-8b0a-e20e0fcd9323" -->
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

<!-- section_id: "5ee00a8d-e495-4e06-9514-611484f61a1b" -->
## Claude Code Integration

<!-- section_id: "748b3992-dec4-4276-9d02-2b92ac1b47cf" -->
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

<!-- section_id: "5a3c139c-dd5b-46c3-b943-f52a75028e19" -->
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

<!-- section_id: "757c6695-4a5a-40af-908e-75b2eb768e44" -->
## System Requirements Verified

- ✅ **GPU:** NVIDIA RTX 4060 Mobile
- ✅ **CUDA Drivers:** 550.163.01
- ✅ **Python:** 3.12.3
- ✅ **Audio:** PipeWire 1.0.5
- ✅ **Free Space:** 203GB
- ✅ **OS:** Ubuntu 24.04 Noble

---

<!-- section_id: "887e4bf0-850b-4332-b477-52f2e09fab2f" -->
## Model Downloads

<!-- section_id: "63566665-41a8-4fdc-8b5f-62419766ecb1" -->
### Whisper Models (Auto-downloaded on first use)
Stored in: `~/.cache/huggingface/`

| Model | Size | Use Case |
|-------|------|----------|
| tiny | 75MB | Fastest, basic accuracy |
| base | 145MB | **Default** - Good balance |
| small | 466MB | Better accuracy |
| medium | 1.5GB | High accuracy |
| large-v3 | 2.9GB | Best accuracy |

<!-- section_id: "8292196d-359f-40f2-8fa6-59679817a267" -->
### Piper Voices
Download more from: https://huggingface.co/rhasspy/piper-voices

Current installed:
- **en_US-lessac-medium** (63MB) - High quality American English

<!-- section_id: "07fa25bf-fe6a-4011-bf65-421b18b5ea98" -->
### Vosk Models
Download more from: https://alphacephei.com/vosk/models

Current installed:
- **vosk-model-small-en-us-0.15** (40MB) - Fast, moderate accuracy

---

<!-- section_id: "d21a755d-a913-49a9-b604-dbb64c069831" -->
## Performance

- **Whisper (GPU):** ~1-2 seconds per minute of audio
- **Vosk (CPU):** Real-time capable
- **Piper TTS:** Instant playback, ~0.5s generation
- **eSpeak NG:** Instant

---

<!-- section_id: "dee36324-dd9b-4731-a2e0-4df0ebf33178" -->
## Troubleshooting

<!-- section_id: "d6c1546f-c575-43e9-a8a8-4450f63cbdec" -->
### Audio Issues
```bash
# Check audio server
pipewire --version

# Test audio output
paplay /usr/share/sounds/alsa/Front_Center.wav

# Install missing utilities
sudo apt install pulseaudio-utils alsa-utils
```

<!-- section_id: "4f12599d-ef81-41b7-8798-5aef7464caf7" -->
### GPU Issues
```bash
# Check NVIDIA GPU
nvidia-smi

# Check CUDA
nvcc --version
```

<!-- section_id: "7e72e085-edb7-4913-933d-77c6bf7f87fe" -->
### Model Issues
```bash
# Whisper models cache
ls ~/.cache/huggingface/

# Piper voices
ls ~/speech-tools/voices/

# Vosk models
ls ~/speech-tools/vosk-models/
```

<!-- section_id: "d642d9c5-9d1f-4532-bfaf-c2d9d5aee055" -->
### Permission Issues
```bash
# Make scripts executable
chmod +x ~/speech-tools/*

# Check microphone access
arecord -l
```

---

<!-- section_id: "de6e225e-00de-431b-a67f-5a0bb934ccbf" -->
## Privacy & Offline Operation

- ✅ **100% Local:** All processing on-device
- ✅ **No Internet Required:** Works completely offline after setup
- ✅ **No Data Sent:** Nothing transmitted to external servers
- ✅ **Private:** Audio never leaves your machine

---

<!-- section_id: "20ea2313-11c6-4a53-9f62-3d8a401b495f" -->
## Additional Voice Models

<!-- section_id: "df7a5fcc-3d20-4a16-8901-14e5dfb9c374" -->
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

<!-- section_id: "91b17d8f-1be7-4a5c-90a4-128d4c3cd589" -->
## Credits

- **Whisper:** OpenAI (via faster-whisper)
- **Vosk:** Alpha Cephei
- **Piper:** Rhasspy
- **eSpeak NG:** Community maintained

---

<!-- section_id: "f0c22147-5b69-4a32-b940-09c64433f386" -->
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
