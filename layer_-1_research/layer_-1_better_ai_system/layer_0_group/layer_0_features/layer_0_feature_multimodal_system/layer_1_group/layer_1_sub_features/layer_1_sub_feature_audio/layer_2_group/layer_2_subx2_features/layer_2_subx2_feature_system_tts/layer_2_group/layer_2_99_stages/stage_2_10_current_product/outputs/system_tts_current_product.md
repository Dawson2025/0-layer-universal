# System TTS — Current Product

**Date**: 2026-02-24
**Status**: Working (Phase 2 complete)

## What's Delivered

### Direct TTS Scripts

| Script | Location | Usage |
|--------|----------|-------|
| `speak` | `~/.local/bin/speak` | `speak "text"`, `echo "text" \| speak`, `speak -s` |
| `speak-selection` | `~/.local/bin/speak-selection` | Highlight text → Ctrl+Alt+S (toggle) |

### Speech Dispatcher Integration

| Command | What It Does |
|---------|--------------|
| `spd-say "text"` | Speak via Speech Dispatcher using Piper (natural voice) |
| `spd-say -o espeak-ng "text"` | Speak via eSpeak NG fallback (robotic) |
| `spd-say -O` | List available modules (espeak-ng, piper-generic) |

### Orca Screen Reader

| Action | How |
|--------|-----|
| Enable | `gsettings set org.gnome.desktop.a11y.applications screen-reader-enabled true` |
| Start | `orca` or `DISPLAY=:0 orca &` |
| Toggle speech | Caps Lock + S |
| Where Am I | Caps Lock + Enter |
| Preferences | Caps Lock + Space |
| Stop Orca | `orca -q` or Super+Alt+S |

Orca uses Piper via Speech Dispatcher — same natural voice as all other TTS.

### Components

| Component | Version | Location |
|-----------|---------|----------|
| Piper TTS | 1.4.1 | `~/.local/bin/piper` (pipx venv) |
| Amy voice | medium | `~/.local/share/piper-voices/en_US-amy-medium.onnx` |
| eSpeak NG | 1.51 | `/usr/bin/espeak-ng` (fallback) |
| Speech Dispatcher | 0.12.0 | System package, user config at `~/.config/speech-dispatcher/` |
| Orca | 46.1 | `/usr/bin/orca` (GNOME screen reader) |
| paplay | system | PulseAudio playback |

### Quick Start

```bash
# Direct speech
speak "Hello, this is a test"
echo "Read this aloud" | speak
speak -s  # stop

# Highlight text in any app, then press Ctrl+Alt+S

# Via Speech Dispatcher
spd-say "Hello from Speech Dispatcher"

# Screen reader
orca  # starts reading focused UI elements
```

### Configuration Files

| File | Purpose |
|------|---------|
| `~/.config/speech-dispatcher/speechd.conf` | Speech Dispatcher user config |
| `~/.config/speech-dispatcher/modules/piper-generic.conf` | Piper module for sd_generic |
| `~/.local/share/orca/user-settings.conf` | Orca preferences |

### Test Suite

```bash
bash .../stage_2_07_testing/outputs/test-system-tts.sh
# 29/29 tests: components, config, modules, audio pipeline, scripts, Orca, keepalive
```

## Limitations

- No runtime rate/pitch control via Speech Dispatcher (Piper CLI limitation)
- Single voice model (Amy medium) — more can be added
- X11 only for speak-selection (no Wayland yet)
- Orca configuration is manual (GUI preferences dialog)

## Architecture

Two independent audio paths, both using PulseAudio:
1. **Direct**: speak/speak-selection → Piper → paplay
2. **Speech Dispatcher**: Orca/spd-say → speechd → sd_generic → Piper → paplay

No audio conflicts — PulseAudio handles mixing.
