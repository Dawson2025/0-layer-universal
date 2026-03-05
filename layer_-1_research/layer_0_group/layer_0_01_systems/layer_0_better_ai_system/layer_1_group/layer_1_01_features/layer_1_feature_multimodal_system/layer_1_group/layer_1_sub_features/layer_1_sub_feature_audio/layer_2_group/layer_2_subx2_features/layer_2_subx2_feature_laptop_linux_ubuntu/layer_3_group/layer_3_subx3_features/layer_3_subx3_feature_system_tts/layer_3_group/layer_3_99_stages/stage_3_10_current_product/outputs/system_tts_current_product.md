---
resource_id: "53dce2fa-ba50-4f97-a2d0-d5dcb4483b6b"
resource_type: "output"
resource_name: "system_tts_current_product"
---
# System TTS — Current Product

**Date**: 2026-02-25
**Status**: Working (Kokoro GPU upgrade complete)

## Design Philosophy

**Selective, on-demand TTS** — the user chooses exactly what gets read aloud. No automatic reading of UI elements, keystrokes, or focus changes. This is NOT a screen reader setup.

## What's Delivered

### Primary: Highlight-and-Speak (Ctrl+Alt+S)

The main interaction: highlight any text in any app, press **Ctrl+Alt+S** to hear it.
- Toggle: press again while speaking to stop
- Falls back to clipboard if no selection
- Uses **Kokoro** GPU-accelerated neural voice (0.17s generation for 6s audio)
- Falls back to Piper if Kokoro server is down

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
| **Kokoro TTS** | **0.9.4 (82M)** | **`~/.local/share/kokoro-tts/venv/` (GPU, primary)** |
| **Kokoro server** | **custom** | **`~/.local/share/kokoro-tts/server.py` (systemd: kokoro-tts.service, port 8880)** |
| Piper TTS | 1.4.1 | `~/.local/bin/piper` (CPU, fallback) |
| Amy voice | medium | `~/.local/share/piper-voices/en_US-amy-medium.onnx` |
| eSpeak NG | 1.51 | `/usr/bin/espeak-ng` (phonemizer for Kokoro) |
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

## Kokoro Upgrade (Completed 2026-02-25)

Piper replaced by **Kokoro** as primary TTS engine:

| Aspect | Before (Piper) | After (Kokoro) |
|--------|----------------|----------------|
| Engine | Piper 1.4.1 (CPU, VITS) | Kokoro 0.9.4 (GPU, 82M params) |
| Quality | High | Highest (#1 HF TTS Arena) |
| Generation | ~1s | 0.17s for 6s audio (35x realtime) |
| Voices | 1 (Amy) | 40+ (af_heart default) |
| Architecture | Process per invocation | Persistent server (systemd, port 8880) |
| VRAM | None | ~1.1GB on RTX 4060 |

**Server**: `~/.local/share/kokoro-tts/server.py` — custom HTTP server, model warm in GPU memory
**Service**: `systemctl --user status kokoro-tts.service`
**Fallback**: Piper auto-activates if Kokoro server is unreachable

## Limitations

- Speech Dispatcher module not yet updated (still uses Piper via piper-generic)
- X11 only for speak-selection (no Wayland yet)
- Single Kokoro voice configured (af_heart) — 40+ available

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
