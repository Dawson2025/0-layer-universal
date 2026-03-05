---
resource_id: "43b28579-a52c-40ed-8944-863bdd11b501"
resource_type: "document"
resource_name: "linux_dictation_project"
---
# Linux-Dictation-Project

**Last Updated**: January 12, 2026
**Repository**: [github.com/wheeler01/Linux-Dictation-Project](https://github.com/wheeler01/Linux-Dictation-Project)
**Category**: Full desktop control with voice commands

<!-- section_id: "8c685ef7-ad19-4750-afbf-5f86165eecac" -->
## Overview

Linux-Dictation-Project is an open-source tool that goes beyond simple dictation. It provides Whisper-based speech-to-text plus voice commands for full desktop control, including copy/paste, key chords, and system commands.

**Key Strength**: Full desktop control as well as text input - aimed at complete hands-free operation for accessibility and productivity use cases.

<!-- section_id: "2b4e81f9-e557-4bd1-8cc8-4c4cf5914f39" -->
## Platform Support

| Platform | Supported |
|----------|-----------|
| Linux | Yes |
| Windows | No |
| macOS | No |

<!-- section_id: "37a67ff5-d9ac-4c8a-9a28-ad4b957ef73a" -->
## Key Features

| Feature | Details |
|---------|---------|
| Dictation | Whisper-based speech-to-text |
| Voice commands | Copy, paste, key chords, navigation |
| Sleep mode | "Go to sleep" / "Wake up" commands |
| Desktop control | Control any focused window |
| Local processing | Whisper runs on your machine |
| Open source | Fully customizable |

<!-- section_id: "3cc06f0c-75a2-4b1d-be92-0f9c6391bdb0" -->
## Voice Commands

| Command | Action |
|---------|--------|
| "Copy" | Copies selected text |
| "Paste" | Pastes clipboard content |
| "Go to sleep" | Pauses listening |
| "Wake up" | Resumes listening |
| Custom key chords | Configurable shortcuts |

<!-- section_id: "c0f6e031-ec34-4154-9348-c2f80636bf4a" -->
## How It Works

1. Listens for voice input via hotkey or continuous mode
2. Processes audio locally with Whisper
3. Recognizes commands vs dictation text
4. Executes commands or types text into focused window

<!-- section_id: "8e8a0a00-239b-486e-96c1-ddc71beae748" -->
## Privacy

| Aspect | Details |
|--------|---------|
| Processing | 100% local |
| Audio | Never sent to cloud |
| Network | Not required after setup |

<!-- section_id: "4e93ebff-916a-4e3b-9913-79ddbe2600bb" -->
## Requirements

- Python 3.x
- Whisper model
- Sufficient RAM/GPU for Whisper
- Linux with X11 or Wayland

<!-- section_id: "b015efdf-a607-487a-bd73-eca73e747592" -->
## Installation

```bash
# Clone the repository
git clone https://github.com/wheeler01/Linux-Dictation-Project.git
cd Linux-Dictation-Project

# Follow the repo's README for complete setup instructions
# Typically involves:
# - Python virtual environment
# - Installing dependencies
# - Downloading Whisper model
# - Configuring voice commands
```

<!-- section_id: "0c66fa0c-bb6f-4ce4-87d7-89740251241f" -->
## Use Cases

| Use Case | How It Helps |
|----------|--------------|
| Hands-free coding | Dictate code, use voice for copy/paste |
| Accessibility | Full desktop control without keyboard |
| Productivity | Faster than typing for long text |
| RSI prevention | Reduce keyboard/mouse strain |

<!-- section_id: "1af744aa-e86a-42ba-80b3-5719da02f150" -->
## Comparison to Simple Dictation

| Feature | Linux-Dictation-Project | Simple Dictation Tools |
|---------|-------------------------|------------------------|
| Voice commands | Yes | No |
| Desktop control | Yes | No |
| Sleep/wake | Yes | No |
| Complexity | Higher | Lower |
| Learning curve | Steeper | Gentle |

<!-- section_id: "51f16cdb-b72d-4c0f-8825-3a19b523ca8a" -->
## Troubleshooting

| Issue | Solution |
|-------|----------|
| Commands not recognized | Check command configuration |
| Wrong text typed | Adjust Whisper model or settings |
| Desktop control not working | Verify X11/Wayland compatibility |
| High CPU usage | Use smaller Whisper model |

<!-- section_id: "9e0882c1-bd8a-4594-af42-405b3636e8d5" -->
## Sources

- [Linux-Dictation-Project GitHub](https://github.com/wheeler01/Linux-Dictation-Project)
