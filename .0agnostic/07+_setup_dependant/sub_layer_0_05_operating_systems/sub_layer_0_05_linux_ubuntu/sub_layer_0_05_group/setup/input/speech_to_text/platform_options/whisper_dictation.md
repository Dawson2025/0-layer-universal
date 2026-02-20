# Whisper-Dictation

**Last Updated**: January 12, 2026
**Repository**: [github.com/LumenYoung/Whisper-Dictation](https://github.com/LumenYoung/Whisper-Dictation)
**Category**: Local/offline processing, privacy-focused

## Overview

Whisper-Dictation is an open-source dictation tool that runs OpenAI's Whisper model locally on your machine. It's designed for KDE/Wayland environments and provides system-wide dictation without sending audio to the cloud.

**Key Strength**: Highly customizable for developers, with clipboard or direct input into focused fields via hotkeys. Ideal for users who prioritize privacy and want full control over their dictation setup.

## Platform Support

| Platform | Supported |
|----------|-----------|
| Linux | Yes |
| Windows | No |
| macOS | No |

## Key Features

| Feature | Details |
|---------|---------|
| Local processing | Whisper runs on your machine |
| Privacy | Audio never leaves your computer |
| Hotkey activation | Configurable keyboard shortcuts |
| Output options | Clipboard or direct cursor injection |
| Customizable | Scriptable Python codebase |
| Open source | MIT license |

## How It Works

1. Runs a local Whisper server
2. Press hotkey to start recording
3. Audio is processed locally by Whisper
4. Text is output to clipboard or cursor position

## Privacy

| Aspect | Details |
|--------|---------|
| Processing | 100% local |
| Audio | Never sent to cloud |
| Model | Downloaded once, runs offline |
| Network | Not required after setup |

## Requirements

- Python 3.x
- Whisper model (downloaded during setup)
- Sufficient RAM/GPU for Whisper model
- KDE/Wayland (optimized for this environment)

## Installation

```bash
# Clone the repository
git clone https://github.com/LumenYoung/Whisper-Dictation.git
cd Whisper-Dictation

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download Whisper model (choose size based on your hardware)
# See repo README for model options
```

## Whisper Model Sizes

| Model | Size | RAM Required | Speed | Accuracy |
|-------|------|--------------|-------|----------|
| tiny | 39M | ~1GB | Fastest | Lower |
| base | 74M | ~1GB | Fast | Good |
| small | 244M | ~2GB | Medium | Better |
| medium | 769M | ~5GB | Slower | High |
| large | 1550M | ~10GB | Slowest | Highest |

**Recommendation**: Start with `base` or `small` for balance of speed and accuracy.

## Desktop Environment Compatibility

| Environment | Status |
|-------------|--------|
| KDE Plasma | Optimized |
| Wayland | Primary target |
| GNOME | May work (less tested) |
| X11 | May work (less tested) |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Slow transcription | Use smaller Whisper model |
| Out of memory | Use smaller model or add swap |
| Text not appearing | Check clipboard manager compatibility |
| Hotkey not working | Verify KDE shortcut configuration |
| Model download fails | Check internet connection, try manual download |

## Comparison to Cloud Solutions

| Feature | Whisper-Dictation | Cloud (Vibe Typer, etc.) |
|---------|-------------------|--------------------------|
| Privacy | Full (local) | Limited (cloud processed) |
| Speed | Depends on hardware | Usually faster |
| Offline | Yes | No |
| Setup complexity | Higher | Lower |
| Cost | Free | May have usage limits |

## Sources

- [Whisper-Dictation GitHub](https://github.com/LumenYoung/Whisper-Dictation)
- [OpenAI Whisper](https://openai.com/index/whisper/)
