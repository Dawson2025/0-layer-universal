# System TTS — Current Product

**Date**: 2026-02-24
**Status**: Working (Phase 2 complete)

## Design Philosophy

**Selective, on-demand TTS** — the user chooses exactly what gets read aloud. No automatic reading of UI elements, keystrokes, or focus changes. This is NOT a screen reader setup.

## What's Delivered

### Primary: Highlight-and-Speak (Ctrl+Alt+S)

The main interaction: highlight any text in any app, press **Ctrl+Alt+S** to hear it.
- Toggle: press again while speaking to stop
- Falls back to clipboard if no selection
- Uses Piper neural voice (natural-sounding)

### CLI: `speak` Command

```bash
speak "Hello, this is a test"       # from arguments
echo "Read this aloud" | speak      # from stdin/pipe
cat article.txt | speak             # read a file
speak -s                            # stop current speech
```

### Speech Dispatcher Integration

Any app or script that uses Speech Dispatcher now gets Piper's natural voice:

```bash
spd-say "Hello from Speech Dispatcher"         # Piper (default)
spd-say -o espeak-ng "Hello from eSpeak"       # eSpeak fallback (robotic)
```

### Components

| Component | Version | Location |
|-----------|---------|----------|
| Piper TTS | 1.4.1 | `~/.local/bin/piper` (pipx venv) |
| Amy voice | medium | `~/.local/share/piper-voices/en_US-amy-medium.onnx` |
| eSpeak NG | 1.51 | `/usr/bin/espeak-ng` (fallback) |
| Speech Dispatcher | 0.12.0 | User config at `~/.config/speech-dispatcher/` |
| paplay | system | PulseAudio playback |

### Configuration Files

| File | Purpose |
|------|---------|
| `~/.config/speech-dispatcher/speechd.conf` | Speech Dispatcher user config (Piper as default module) |
| `~/.config/speech-dispatcher/modules/piper-generic.conf` | Piper sd_generic module config |

### Test Suite

```bash
bash .../stage_2_07_testing/outputs/test-system-tts.sh
# 29/29 tests: components, config, modules, audio pipeline, scripts, keepalive
```

## NOT Included (by design)

- **Orca screen reader is NOT enabled** — Orca reads every UI element, keystroke, and focus change. That's designed for visually impaired users, not selective TTS. Orca is installed (v46.1) and configured to use Piper via Speech Dispatcher, but is disabled by default.
- No automatic speech on any event — all TTS is user-initiated

## Limitations

- No runtime rate/pitch control via Speech Dispatcher (Piper CLI limitation)
- Single voice model (Amy medium) — more can be added
- X11 only for speak-selection (no Wayland yet)

## Architecture

```
User action (highlight + Ctrl+Alt+S, or CLI)
  → speak / speak-selection script
  → Piper (neural TTS)
  → paplay (PulseAudio)
  → speakers

Apps using Speech Dispatcher (spd-say, etc.)
  → speechd daemon
  → piper-generic module (sd_generic)
  → Piper → paplay → speakers
```
