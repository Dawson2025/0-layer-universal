# Linux-Dictation-Project

**Last Updated**: January 12, 2026
**Repository**: [github.com/wheeler01/Linux-Dictation-Project](https://github.com/wheeler01/Linux-Dictation-Project)
**Category**: Full desktop control with voice commands

## Overview

Linux-Dictation-Project is an open-source tool that goes beyond simple dictation. It provides Whisper-based speech-to-text plus voice commands for full desktop control, including copy/paste, key chords, and system commands.

**Key Strength**: Full desktop control as well as text input - aimed at complete hands-free operation for accessibility and productivity use cases.

## Platform Support

| Platform | Supported |
|----------|-----------|
| Linux | Yes |
| Windows | No |
| macOS | No |

## Key Features

| Feature | Details |
|---------|---------|
| Dictation | Whisper-based speech-to-text |
| Voice commands | Copy, paste, key chords, navigation |
| Sleep mode | "Go to sleep" / "Wake up" commands |
| Desktop control | Control any focused window |
| Local processing | Whisper runs on your machine |
| Open source | Fully customizable |

## Voice Commands

| Command | Action |
|---------|--------|
| "Copy" | Copies selected text |
| "Paste" | Pastes clipboard content |
| "Go to sleep" | Pauses listening |
| "Wake up" | Resumes listening |
| Custom key chords | Configurable shortcuts |

## How It Works

1. Listens for voice input via hotkey or continuous mode
2. Processes audio locally with Whisper
3. Recognizes commands vs dictation text
4. Executes commands or types text into focused window

## Privacy

| Aspect | Details |
|--------|---------|
| Processing | 100% local |
| Audio | Never sent to cloud |
| Network | Not required after setup |

## Requirements

- Python 3.x
- Whisper model
- Sufficient RAM/GPU for Whisper
- Linux with X11 or Wayland

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

## Use Cases

| Use Case | How It Helps |
|----------|--------------|
| Hands-free coding | Dictate code, use voice for copy/paste |
| Accessibility | Full desktop control without keyboard |
| Productivity | Faster than typing for long text |
| RSI prevention | Reduce keyboard/mouse strain |

## Comparison to Simple Dictation

| Feature | Linux-Dictation-Project | Simple Dictation Tools |
|---------|-------------------------|------------------------|
| Voice commands | Yes | No |
| Desktop control | Yes | No |
| Sleep/wake | Yes | No |
| Complexity | Higher | Lower |
| Learning curve | Steeper | Gentle |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Commands not recognized | Check command configuration |
| Wrong text typed | Adjust Whisper model or settings |
| Desktop control not working | Verify X11/Wayland compatibility |
| High CPU usage | Use smaller Whisper model |

## Sources

- [Linux-Dictation-Project GitHub](https://github.com/wheeler01/Linux-Dictation-Project)
