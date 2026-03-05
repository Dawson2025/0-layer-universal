---
resource_id: "e4931636-4df5-4afb-a42a-8f85ee9ed7be"
resource_type: "document"
resource_name: "whisper_dictation"
---
# Whisper-Dictation

**Last Updated**: January 12, 2026
**Repository**: [github.com/LumenYoung/Whisper-Dictation](https://github.com/LumenYoung/Whisper-Dictation)
**Category**: Local/offline processing, privacy-focused

<!-- section_id: "7e955b7b-bbff-4a5f-8d11-be9d78c32359" -->
## Overview

Whisper-Dictation is an open-source dictation tool that runs OpenAI's Whisper model locally on your machine. It's designed for KDE/Wayland environments and provides system-wide dictation without sending audio to the cloud.

**Key Strength**: Highly customizable for developers, with clipboard or direct input into focused fields via hotkeys. Ideal for users who prioritize privacy and want full control over their dictation setup.

<!-- section_id: "d1480edd-bb11-44c1-b02c-7b944c5e17a1" -->
## Platform Support

| Platform | Supported |
|----------|-----------|
| Linux | Yes |
| Windows | No |
| macOS | No |

<!-- section_id: "8c8dc81e-b21c-4858-ba8a-e53260f703ff" -->
## Key Features

| Feature | Details |
|---------|---------|
| Local processing | Whisper runs on your machine |
| Privacy | Audio never leaves your computer |
| Hotkey activation | Configurable keyboard shortcuts |
| Output options | Clipboard or direct cursor injection |
| Customizable | Scriptable Python codebase |
| Open source | MIT license |

<!-- section_id: "e2299464-a24d-483a-bda9-e6db28f60798" -->
## How It Works

1. Runs a local Whisper server
2. Press hotkey to start recording
3. Audio is processed locally by Whisper
4. Text is output to clipboard or cursor position

<!-- section_id: "dba48e15-a0ff-49e1-86d2-72c15110657a" -->
## Privacy

| Aspect | Details |
|--------|---------|
| Processing | 100% local |
| Audio | Never sent to cloud |
| Model | Downloaded once, runs offline |
| Network | Not required after setup |

<!-- section_id: "6a9d2e7c-12b3-4fe3-934f-8da502bc27ac" -->
## Requirements

- Python 3.x
- Whisper model (downloaded during setup)
- Sufficient RAM/GPU for Whisper model
- KDE/Wayland (optimized for this environment)

<!-- section_id: "dbb4156d-b6f3-4f64-82f2-4be579c8fa69" -->
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

<!-- section_id: "9f959288-9327-4638-af9e-e754d4643f09" -->
## Whisper Model Sizes

| Model | Size | RAM Required | Speed | Accuracy |
|-------|------|--------------|-------|----------|
| tiny | 39M | ~1GB | Fastest | Lower |
| base | 74M | ~1GB | Fast | Good |
| small | 244M | ~2GB | Medium | Better |
| medium | 769M | ~5GB | Slower | High |
| large | 1550M | ~10GB | Slowest | Highest |

**Recommendation**: Start with `base` or `small` for balance of speed and accuracy.

<!-- section_id: "d0dbdb87-cad4-451d-a53c-22e2cd380df4" -->
## Desktop Environment Compatibility

| Environment | Status |
|-------------|--------|
| KDE Plasma | Optimized |
| Wayland | Primary target |
| GNOME | May work (less tested) |
| X11 | May work (less tested) |

<!-- section_id: "f4f90372-2ee0-4063-b3fd-17d00967785a" -->
## Troubleshooting

| Issue | Solution |
|-------|----------|
| Slow transcription | Use smaller Whisper model |
| Out of memory | Use smaller model or add swap |
| Text not appearing | Check clipboard manager compatibility |
| Hotkey not working | Verify KDE shortcut configuration |
| Model download fails | Check internet connection, try manual download |

<!-- section_id: "85ca3bff-2ce1-49c5-8628-55c3876867e4" -->
## Comparison to Cloud Solutions

| Feature | Whisper-Dictation | Cloud (Vibe Typer, etc.) |
|---------|-------------------|--------------------------|
| Privacy | Full (local) | Limited (cloud processed) |
| Speed | Depends on hardware | Usually faster |
| Offline | Yes | No |
| Setup complexity | Higher | Lower |
| Cost | Free | May have usage limits |

<!-- section_id: "74595f06-4a4d-4763-b1b3-db222a39e4df" -->
## Sources

- [Whisper-Dictation GitHub](https://github.com/LumenYoung/Whisper-Dictation)
- [OpenAI Whisper](https://openai.com/index/whisper/)
