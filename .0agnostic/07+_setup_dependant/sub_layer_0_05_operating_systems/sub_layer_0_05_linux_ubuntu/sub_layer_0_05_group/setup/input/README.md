---
resource_id: "17c4cb5d-d8a4-4279-9877-d1b8c3a04d55"
resource_type: "readme
document"
resource_name: "README"
---
# Input Device Setup

**Last Updated**: January 13, 2026
**System**: Ubuntu/Linux

<!-- section_id: "3f819566-2480-4d32-8e2d-39606bdb0f73" -->
## Overview

Configuration and setup documentation for input devices and methods on Linux.

<!-- section_id: "e8bb0cbf-b5fd-4776-a704-3361fc105bc9" -->
## Available Input Setup Guides

| Input Type | Description | Status |
|------------|-------------|--------|
| [Speech-to-Text](speech_to_text/) | System-wide voice dictation (WisprFlow alternatives) | Documented |
| [Trackpad](trackpad/) | Cursor speed, acceleration, scroll settings | Documented |

<!-- section_id: "77a0fed7-1799-4ae8-8049-05d970ba2284" -->
## Quick Setup

<!-- section_id: "a7bc3338-b897-4799-a5ff-9d71f4462d66" -->
### Speech-to-Text (Recommended: VibeTyper)

For system-wide dictation on Linux, use **VibeTyper**:

```bash
# Install dependencies (Ubuntu 24+ / Wayland)
sudo apt install -y libfuse2 wl-clipboard
sudo usermod -aG input $USER

# Download and run
# Get AppImage from https://vibetyper.com/downloads
chmod +x ~/Downloads/VibeTyper.AppImage
~/Downloads/VibeTyper.AppImage

# Add to autostart
mkdir -p ~/.config/autostart
cp ~/.local/share/applications/com.vibetyper.app.desktop ~/.config/autostart/

# IMPORTANT: Log out and back in for input group to take effect
```

**Default hotkey**: `Ctrl + Space` (hold to dictate)

See [speech_to_text/platform_options/vibe_typer.md](speech_to_text/platform_options/vibe_typer.md) for full details.

<!-- section_id: "896b4bd0-d881-455c-9401-bef74b262db0" -->
### Trackpad

See [trackpad/](trackpad/) for cursor speed, acceleration, and scroll configuration on Wayland and X11.

<!-- section_id: "29a44163-8b86-4f1e-a124-635ab4a0ba59" -->
## Directory Structure

```
input/
├── README.md                 # This file
├── speech_to_text/           # Voice dictation tools
│   ├── README.md
│   ├── decision_guide/       # Help choosing tools
│   ├── platform_options/     # Individual tool docs
│   │   ├── vibe_typer.md     # Recommended for functionality
│   │   ├── whisper_dictation.md
│   │   ├── linux_dictation_project.md
│   │   ├── openwhispr.md
│   │   ├── blabby_ai.md
│   │   └── cloud_apis.md
│   └── environment/          # Wayland/X11 compatibility
└── trackpad/                 # Trackpad configuration
    └── ...
```

<!-- section_id: "0bd5c84c-7de4-4985-bf4c-81f19288a93e" -->
## Related Documentation

- Parent: [../README.md](../README.md) - OS Setup overview
- Speech-to-Text details: [speech_to_text/README.md](speech_to_text/README.md)
- Trackpad details: [trackpad/README.md](trackpad/README.md)
