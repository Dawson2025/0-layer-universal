# System TTS — Current Product

**Date**: 2026-02-23
**Status**: Working (MVP)

## What's Delivered

### Scripts

| Script | Location | Usage |
|--------|----------|-------|
| `speak` | `~/.local/bin/speak` | `speak "text"`, `echo "text" \| speak`, `speak -s` |
| `speak-selection` | `~/.local/bin/speak-selection` | Highlight text → run script (bind to hotkey) |

### Components

| Component | Version | Location |
|-----------|---------|----------|
| Piper TTS | 1.4.1 | `~/.local/bin/piper` (pipx venv) |
| Amy voice | medium | `~/.local/share/piper-voices/en_US-amy-medium.onnx` |
| eSpeak NG | 1.51 | `/usr/bin/espeak-ng` (fallback) |

### Quick Start

```bash
# Speak text
speak "Hello, this is a test"

# Pipe text
echo "Read this aloud" | speak

# Stop speech
speak -s

# Highlight text in any app, then:
speak-selection
```

### Hotkey Setup (Manual)

GNOME Settings → Keyboard → Custom Shortcuts:
- **Name**: Speak Selection
- **Command**: `/home/dawson/.local/bin/speak-selection`
- **Shortcut**: Super+S

## Limitations

- No voice switching (Amy only)
- No speed/pitch control
- X11 only (no Wayland)
- No visual feedback
- No speech queue (new speech replaces old)
