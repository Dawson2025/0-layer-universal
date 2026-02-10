# Speech-to-Text / Dictation Tools for Linux

**Last Updated**: January 13, 2026
**System**: Ubuntu/Linux
**Use Case**: System-wide dictation (WisprFlow-style)

## Overview

WisprFlow is **NOT available for Linux** - it only supports macOS, Windows, and iOS. This directory covers Linux alternatives for system-wide voice dictation with hotkey activation.

## Directory Structure

```
speech_to_text/
├── README.md                        # This file
├── decision_guide/                  # Help choosing the right tool
│   ├── README.md
│   ├── quick_decision.md           # Priority-based recommendations
│   ├── comparison_matrix.md        # Full feature comparison
│   └── use_cases.md                # Scenario-based recommendations
├── platform_options/                # Individual tool documentation
│   ├── README.md
│   ├── vibe_typer.md               # Cloud-based, easiest setup
│   ├── whisper_dictation.md        # Local Whisper, KDE/Wayland
│   ├── linux_dictation_project.md  # Local Whisper + voice commands
│   ├── openwhispr.md               # Cross-platform, open source
│   ├── blabby_ai.md                # Upcoming native Linux app
│   └── cloud_apis.md               # Developer APIs
└── environment/                     # Compatibility considerations
    ├── README.md
    ├── wayland_vs_x11.md           # Display server differences
    └── desktop_environments.md     # DE-specific notes
```

## Quick Start

### Don't know what to pick?
→ [Decision Guide](decision_guide/README.md)

### Know what you want?
→ [Platform Options](platform_options/README.md)

### Need to check compatibility?
→ [Environment Guide](environment/README.md)

## TL;DR

| You Want | Use This |
|----------|----------|
| Easiest setup + best functionality | [Vibe Typer](platform_options/vibe_typer.md) **(Recommended)** |
| Privacy / offline | [Whisper-Dictation](platform_options/whisper_dictation.md) |
| Voice commands | [Linux-Dictation-Project](platform_options/linux_dictation_project.md) |
| Open source | [OpenWhispr](platform_options/openwhispr.md) |

## Quick Install: VibeTyper (Recommended)

For system-wide dictation with best accuracy and minimal setup:

```bash
# 1. Install dependencies (Ubuntu 24+ / Wayland)
sudo apt install -y libfuse2 wl-clipboard

# 2. Add to input group (required for global hotkeys on Wayland)
sudo usermod -aG input $USER

# 3. Download AppImage from https://vibetyper.com/downloads
# Then make executable and run:
chmod +x ~/Downloads/VibeTyper.AppImage
~/Downloads/VibeTyper.AppImage

# 4. Add to autostart (optional)
mkdir -p ~/.config/autostart
cp ~/.local/share/applications/com.vibetyper.app.desktop ~/.config/autostart/

# 5. IMPORTANT: Log out and back in for input group to take effect
```

**Default hotkey**: `Ctrl + Space` (hold to dictate, release to insert)

See [platform_options/vibe_typer.md](platform_options/vibe_typer.md) for detailed setup and troubleshooting.

## Available Tools

| Tool | Type | Privacy | Doc |
|------|------|---------|-----|
| Vibe Typer | Cloud | Low | [Link](platform_options/vibe_typer.md) |
| OpenWhispr | Cross-platform | High | [Link](platform_options/openwhispr.md) |
| Whisper-Dictation | Local | Full | [Link](platform_options/whisper_dictation.md) |
| Linux-Dictation-Project | Local + Commands | Full | [Link](platform_options/linux_dictation_project.md) |
| BlabbyAI | Native (upcoming) | TBD | [Link](platform_options/blabby_ai.md) |

## Check Your Environment

```bash
# Display server
echo $XDG_SESSION_TYPE

# Desktop environment
echo $XDG_CURRENT_DESKTOP
```

See [environment/](environment/) for compatibility details.

## Related Documentation

- [Trackpad Configuration](../trackpad/) - Input device setup
- Main setup README: `../../README.md`

## Sources

### Primary Tool Documentation
- [Vibe Typer Website](https://vibetyper.com)
- [Vibe Typer Downloads](https://vibetyper.com/downloads)
- [Vibe Typer - WisprFlow Alternative for Linux](https://vibetyper.com/blog/wisprflow-alternative-linux-guide)
- [Vibe Typer - Wispr Flow Linux Alternative 2025](https://vibetyper.com/blog/wispr-flow-linux-alternative-2025)
- [OpenWhispr Website](https://openwhispr.com)
- [OpenWhispr vs WisprFlow](https://openwhispr.com/compare/wisprflow)
- [Whisper-Dictation GitHub](https://github.com/LumenYoung/Whisper-Dictation)
- [Linux-Dictation-Project GitHub](https://github.com/wheeler01/Linux-Dictation-Project)
- [BlabbyAI Website](https://www.blabby.ai)
- [BlabbyAI Linux Speech-to-Text](https://www.blabby.ai/linux-speech-to-text)
- [WhisperDictation Website](https://www.whisperdictation.com)
- [OpenAI Whisper](https://openai.com/index/whisper/)

### WisprFlow Platform Confirmation
- [WisprFlow Official](https://wisprflow.ai) - Confirms macOS/Windows/iOS only, no Linux
- [WisprFlow Review (Zack Proser)](https://zackproser.com/blog/wisprflow-review) - Independent review confirming no Linux support

### Community Discussions
- [Reddit r/linux4noobs: Linux alternatives to Wispr Flow](https://www.reddit.com/r/linux4noobs/comments/1n6zvpr/any_good_linux_alternatives_to_wispr_flow_or/)
- [Reddit r/linuxquestions: Easy to use speech-to-text apps](https://www.reddit.com/r/linuxquestions/comments/1jzbyv9/recommendations_on_easy_to_use_speechtotext_apps/)
- [LinkedIn: Open Source WisprFlow for Linux](https://www.linkedin.com/posts/imsidharthj_i-made-open-source-wisprflow-for-linux-recently-activity-7361421809130307585-jsZq)

### General STT Comparisons
- [DevOps School: Top 10 Speech to Text Tools 2025](https://www.devopsschool.com/blog/top-10-speech-to-text-tools-in-2025-features-pros-cons-comparison/)
- [Slashdot: Speech to Text for Linux](https://slashdot.org/software/speech-to-text/linux/)
- [Zapier: Best Dictation Software](https://zapier.com/blog/best-text-dictation-software/)
- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text)
