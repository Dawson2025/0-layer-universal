# System TTS Setup — Development Log

**Date**: 2026-02-23
**Status**: Working

## Components Installed

| Component | Version | Status |
|-----------|---------|--------|
| Orca | 46.1 | Pre-installed (GNOME screen reader) |
| eSpeak NG | 1.51 | Pre-installed |
| Speech Dispatcher | 0.12.0-rc2 | Pre-installed with espeak-ng module |
| Piper TTS | 1.4.1 | Installed via `pipx install piper-tts` |
| Voice Model | en_US-amy-medium | Downloaded from HuggingFace |
| xclip | system | Pre-installed (X11 clipboard) |
| aplay | 1.2.9 | Pre-installed (ALSA utils) |

## Installation Steps

### Piper TTS
```bash
pipx install piper-tts
pipx inject piper-tts pathvalidate  # missing dependency fix
```

### Voice Model
```bash
mkdir -p ~/.local/share/piper-voices
curl -L -o ~/.local/share/piper-voices/en_US-amy-medium.onnx \
  "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx?download=true"
curl -L -o ~/.local/share/piper-voices/en_US-amy-medium.onnx.json \
  "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx.json?download=true"
```

## Scripts Created

### `~/.local/bin/speak`
General-purpose TTS command:
- `speak "Hello world"` — speak text from arguments
- `echo "Hello" | speak` — speak from stdin
- `speak -s` — stop current speech

### `~/.local/bin/speak-selection`
Highlight-and-speak for X11:
- Reads X primary selection (highlighted text)
- Falls back to clipboard if no selection
- Toggle behavior: run again to stop
- Bind to keyboard shortcut (e.g., Super+S)

## Test Results

| Test | Command | Result |
|------|---------|--------|
| Speech Dispatcher | `spd-say "test"` | Works (espeak-ng, robotic) |
| eSpeak NG direct | `espeak-ng "test"` | Works (robotic) |
| Piper direct | `echo "test" \| piper --model amy ... \| aplay ...` | Works (natural) |
| speak script (args) | `speak "Hello world"` | Works |
| speak script (pipe) | `echo "test" \| speak` | Works |

## Audio Stack

```
Session: X11
Audio: PulseAudio (server protocol v35)
Output: aplay → ALSA → PulseAudio → hardware
```

## Keyboard Shortcut Setup

To bind speak-selection to a hotkey (GNOME):
```bash
# Settings → Keyboard → Keyboard Shortcuts → Custom Shortcuts
# Name: Speak Selection
# Command: /home/dawson/.local/bin/speak-selection
# Shortcut: Super+S (or your preference)
```

## Known Issues

- Piper 1.4.1 missing `pathvalidate` dependency — fixed with `pipx inject`
- eSpeak NG voice is robotic — Piper provides much better quality
- No Wayland clipboard support yet (currently X11, would need wl-paste)

## Next Steps

- [ ] Configure keyboard shortcut in GNOME settings
- [ ] Add more voice models (male voice, different accents)
- [ ] Integrate with Speech Dispatcher as Piper module
- [ ] Test with longer documents
