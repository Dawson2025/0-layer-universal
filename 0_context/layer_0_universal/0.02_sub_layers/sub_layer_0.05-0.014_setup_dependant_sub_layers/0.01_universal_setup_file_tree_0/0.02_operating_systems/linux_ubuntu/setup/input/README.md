# Input Device Setup

**Last Updated**: January 13, 2026
**System**: Ubuntu/Linux

## Overview

Configuration and setup documentation for input devices and methods on Linux.

## Available Input Setup Guides

| Input Type | Description | Status |
|------------|-------------|--------|
| [Speech-to-Text](speech_to_text/) | System-wide voice dictation (WisprFlow alternatives) | Documented |
| [Trackpad](trackpad/) | Cursor speed, acceleration, scroll settings | Documented |

## Quick Setup

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

### Trackpad

See [trackpad/](trackpad/) for cursor speed, acceleration, and scroll configuration on Wayland and X11.

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

## Related Documentation

- Parent: [../README.md](../README.md) - OS Setup overview
- Speech-to-Text details: [speech_to_text/README.md](speech_to_text/README.md)
- Trackpad details: [trackpad/README.md](trackpad/README.md)
