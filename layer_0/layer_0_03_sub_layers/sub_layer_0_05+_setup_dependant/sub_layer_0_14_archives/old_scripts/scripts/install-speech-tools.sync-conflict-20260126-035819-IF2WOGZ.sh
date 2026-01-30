#!/bin/bash
# Automated Speech Tools Installation Script
# Ubuntu 24.04+ with NVIDIA GPU support
# See: docs/ubuntu-speech-tools-stt-tts.md

set -e

echo "=================================="
echo "Speech Tools Installation Script"
echo "STT (Whisper, Vosk) + TTS (Piper, eSpeak)"
echo "=================================="
echo ""

# Check if running on Ubuntu
if ! grep -q "Ubuntu" /etc/os-release; then
    echo "⚠️  Warning: This script is designed for Ubuntu"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# 1. Install system dependencies
echo "📦 Installing system dependencies..."
sudo apt update
sudo apt install -y ffmpeg portaudio19-dev python3-pyaudio pulseaudio-utils espeak-ng pipx
pipx ensurepath

# 2. Create directory structure
echo "📁 Creating directory structure..."
mkdir -p ~/speech-tools/voices
mkdir -p ~/speech-tools/vosk-models

# 3. Create Python virtual environment
echo "🐍 Setting up Python virtual environment..."
cd ~/speech-tools
python3 -m venv venv
source venv/bin/activate

# 4. Install Python packages
echo "📦 Installing Python packages..."
pip install --upgrade pip wheel
pip install faster-whisper pyaudio piper-tts vosk soundfile

# 5. Download Piper voice model
echo "🎙️  Downloading Piper TTS voice model..."
cd ~/speech-tools/voices
if [ ! -f "en_US-lessac-medium.onnx" ]; then
    wget -q --show-progress https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx
    wget -q https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json
    echo "✓ Voice model downloaded"
else
    echo "✓ Voice model already exists"
fi

# 6. Download Vosk model
echo "🎤 Downloading Vosk STT model..."
cd ~/speech-tools/vosk-models
if [ ! -d "vosk-model-small-en-us-0.15" ]; then
    wget -q --show-progress https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
    unzip -q vosk-model-small-en-us-0.15.zip
    rm vosk-model-small-en-us-0.15.zip
    echo "✓ Vosk model downloaded"
else
    echo "✓ Vosk model already exists"
fi

# 7. Create main scripts (download from setup-hub or create inline)
echo "📝 Creating scripts..."

# This would ideally download from the setup-hub repo
# For now, inform user to check the documentation
echo "⚠️  Note: Main Python scripts need to be created manually"
echo "   See: ~/code/setup-hub/docs/ubuntu-speech-tools-stt-tts.md"
echo "   Sections 5 & 6 for full script content"

# 8. Create wrapper scripts
cat > ~/speech-tools/stt << 'EOF'
#!/bin/bash
cd ~/speech-tools
source venv/bin/activate
python3 whisper-stt.py "$@"
EOF

cat > ~/speech-tools/tts << 'EOF'
#!/bin/bash
cd ~/speech-tools
source venv/bin/activate
python3 piper-tts.py "$@"
EOF

cat > ~/speech-tools/speak-text << 'EOF'
#!/bin/bash
if [ $# -gt 0 ]; then
    ~/speech-tools/tts "$*"
else
    ~/speech-tools/tts
fi
EOF

chmod +x ~/speech-tools/stt ~/speech-tools/tts ~/speech-tools/speak-text

# 9. Add to .bashrc if not already present
echo "⚙️  Configuring shell..."
if ! grep -q "speech-tools" ~/.bashrc; then
    cat >> ~/.bashrc << 'EOF'

# Speech Tools - Add to PATH
export PATH="$HOME/speech-tools:$PATH"

# Speech Tools - TTS Integration
alias speak='~/speech-tools/speak-text'
alias tts='~/speech-tools/tts'

# Function to speak any command's output
say() {
    "$@" 2>&1 | tee /dev/tty | ~/speech-tools/tts 2>/dev/null &
}
EOF
    echo "✓ Added to .bashrc"
else
    echo "✓ Already in .bashrc"
fi

echo ""
echo "=================================="
echo "✅ Installation Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Create the main Python scripts (see documentation)"
echo "2. Run: source ~/.bashrc"
echo "3. Test TTS: tts 'Hello world'"
echo "4. Test STT: stt (then speak and press Ctrl+C)"
echo ""
echo "Full documentation:"
echo "  ~/code/setup-hub/docs/ubuntu-speech-tools-stt-tts.md"
echo ""
