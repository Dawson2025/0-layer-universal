---
resource_id: "6e2eda19-92e0-46c1-9fbb-d4c1a06afe37"
resource_type: "readme_document"
resource_name: "README"
---
# Speech-to-Text / Dictation Tools for Linux

**Last Updated**: January 13, 2026
**System**: Ubuntu/Linux
**Use Case**: System-wide dictation (WisprFlow-style)

<!-- section_id: "1a4b81f8-e84b-472e-a722-cb5eb0e2dae7" -->
## Overview

WisprFlow is **NOT available for Linux** - it only supports macOS, Windows, and iOS. This directory covers Linux alternatives for system-wide voice dictation with hotkey activation.

<!-- section_id: "cf4f3187-a370-4d4c-b001-a8b0f3332f0c" -->
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

<!-- section_id: "d202b83f-b4b6-4235-8da0-e2a79692592d" -->
## Quick Start

<!-- section_id: "06bd778a-3897-4403-8ede-b4f1e8415b96" -->
### Don't know what to pick?
→ [Decision Guide](decision_guide/README.md)

<!-- section_id: "d6834d5c-e477-4ef5-9da6-04d1163fb18c" -->
### Know what you want?
→ [Platform Options](platform_options/README.md)

<!-- section_id: "32d3daf2-251f-4dc3-b6ce-253025fbd9b1" -->
### Need to check compatibility?
→ [Environment Guide](environment/README.md)

<!-- section_id: "073a938e-0d2d-4d28-9d01-fa7fb51a26b1" -->
## TL;DR

| You Want | Use This |
|----------|----------|
| Easiest setup + best functionality | [Vibe Typer](platform_options/vibe_typer.md) **(Recommended)** |
| Privacy / offline | [Whisper-Dictation](platform_options/whisper_dictation.md) |
| Voice commands | [Linux-Dictation-Project](platform_options/linux_dictation_project.md) |
| Open source | [OpenWhispr](platform_options/openwhispr.md) |

<!-- section_id: "2c0ec94b-0d14-4efe-a967-2a99df62d89e" -->
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

<!-- section_id: "1a90a838-898c-4828-b8bd-d0e018839c1b" -->
## Available Tools

| Tool | Type | Privacy | Doc |
|------|------|---------|-----|
| Vibe Typer | Cloud | Low | [Link](platform_options/vibe_typer.md) |
| OpenWhispr | Cross-platform | High | [Link](platform_options/openwhispr.md) |
| Whisper-Dictation | Local | Full | [Link](platform_options/whisper_dictation.md) |
| Linux-Dictation-Project | Local + Commands | Full | [Link](platform_options/linux_dictation_project.md) |
| BlabbyAI | Native (upcoming) | TBD | [Link](platform_options/blabby_ai.md) |

<!-- section_id: "b0de71ea-1de5-460e-a458-d06863b5bd45" -->
## Check Your Environment

```bash
# Display server
echo $XDG_SESSION_TYPE

# Desktop environment
echo $XDG_CURRENT_DESKTOP
```

See [environment/](environment/) for compatibility details.

<!-- section_id: "063dc33d-4524-449f-bb35-e6f7a6230182" -->
## Related Documentation

- [Trackpad Configuration](../trackpad/) - Input device setup
- Main setup README: `../../README.md`

<!-- section_id: "3a2c0240-f07a-48fa-8a84-a4a8aca01e9a" -->
## Sources

<!-- section_id: "1899485e-ad24-4a84-8acd-307e231c6d91" -->
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

<!-- section_id: "278041a6-ea8d-4ca6-8249-903d3d3c5686" -->
### WisprFlow Platform Confirmation
- [WisprFlow Official](https://wisprflow.ai) - Confirms macOS/Windows/iOS only, no Linux
- [WisprFlow Review (Zack Proser)](https://zackproser.com/blog/wisprflow-review) - Independent review confirming no Linux support

<!-- section_id: "277173d1-559f-4ca6-9109-4a64bc2e09f0" -->
### Community Discussions
- [Reddit r/linux4noobs: Linux alternatives to Wispr Flow](https://www.reddit.com/r/linux4noobs/comments/1n6zvpr/any_good_linux_alternatives_to_wispr_flow_or/)
- [Reddit r/linuxquestions: Easy to use speech-to-text apps](https://www.reddit.com/r/linuxquestions/comments/1jzbyv9/recommendations_on_easy_to_use_speechtotext_apps/)
- [LinkedIn: Open Source WisprFlow for Linux](https://www.linkedin.com/posts/imsidharthj_i-made-open-source-wisprflow-for-linux-recently-activity-7361421809130307585-jsZq)

<!-- section_id: "9a643e73-ed7a-49b5-9988-b8ced30cc682" -->
### General STT Comparisons
- [DevOps School: Top 10 Speech to Text Tools 2025](https://www.devopsschool.com/blog/top-10-speech-to-text-tools-in-2025-features-pros-cons-comparison/)
- [Slashdot: Speech to Text for Linux](https://slashdot.org/software/speech-to-text/linux/)
- [Zapier: Best Dictation Software](https://zapier.com/blog/best-text-dictation-software/)
- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text)
