# Speech-to-Text / Dictation Tools for Linux

**Last Updated**: January 12, 2026
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
| Easiest setup | [Vibe Typer](platform_options/vibe_typer.md) |
| Privacy / offline | [Whisper-Dictation](platform_options/whisper_dictation.md) |
| Voice commands | [Linux-Dictation-Project](platform_options/linux_dictation_project.md) |
| Open source | [OpenWhispr](platform_options/openwhispr.md) |

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

- [Reddit: Linux alternatives to Wispr Flow](https://www.reddit.com/r/linux4noobs/comments/1n6zvpr/any_good_linux_alternatives_to_wispr_flow_or/)
- [Vibe Typer - WisprFlow Alternative for Linux](https://vibetyper.com/blog/wisprflow-alternative-linux-guide)
- [OpenWhispr vs WisprFlow](https://openwhispr.com/compare/wisprflow)
- [Whisper-Dictation GitHub](https://github.com/LumenYoung/Whisper-Dictation)
- [Linux-Dictation-Project GitHub](https://github.com/wheeler01/Linux-Dictation-Project)
- [BlabbyAI Linux Speech-to-Text](https://www.blabby.ai/linux-speech-to-text)
