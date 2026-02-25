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

## Planned Upgrade: Kokoro TTS

The next step is replacing Piper with **Kokoro** for GPU-accelerated, higher-quality speech:

| Aspect | Current | After Upgrade |
|--------|---------|---------------|
| Engine | Piper (CPU, VITS) | Kokoro (GPU, 82M params) |
| Quality | High | Highest (#1 HF TTS Arena) |
| Latency | ~1s | Sub-0.1s (RTX 4060) |
| Voices | 1 (Amy) | 40+ |

**Install**: `uvx kokoro-fastapi[gpu] serve` — runs as FastAPI on port 8880.
**Migration**: Update `speak`/`speak-selection` to `curl` Kokoro API instead of piping to Piper.

See parent entity knowledge: `../../../.0agnostic/01_knowledge/gpu_tts/` for full Kokoro docs.

## Limitations

- No runtime rate/pitch control via Speech Dispatcher (Piper CLI limitation — resolved by Kokoro upgrade)
- Single voice model (Amy medium) — Kokoro upgrade provides 40+ voices
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
