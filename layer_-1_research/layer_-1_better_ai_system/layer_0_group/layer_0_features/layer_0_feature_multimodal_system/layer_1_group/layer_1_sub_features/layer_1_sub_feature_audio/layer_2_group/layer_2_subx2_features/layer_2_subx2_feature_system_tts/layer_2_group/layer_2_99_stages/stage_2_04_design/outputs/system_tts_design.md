# System TTS Design

**Date**: 2026-02-23

## Architecture

```
┌──────────────────────────────────────────────────┐
│                  User Interface                    │
│                                                    │
│  [Hotkey: Super+S]     [Terminal]                  │
│       │                    │                       │
│       v                    v                       │
│  speak-selection        speak                      │
│       │                    │                       │
│       v                    v                       │
│  xclip (selection)    args or stdin                │
│       │                    │                       │
│       └────────┬───────────┘                       │
│                v                                   │
│         PID check (kill existing)                  │
│                │                                   │
│                v                                   │
│    echo "$TEXT" | piper --model $VOICE             │
│         --output-raw                               │
│                │                                   │
│                v                                   │
│    aplay -r 22050 -f S16_LE -t raw -c 1           │
│                │                                   │
│                v                                   │
│         PulseAudio → Speakers                      │
└──────────────────────────────────────────────────┘
```

## Components

| Component | Script | Purpose |
|-----------|--------|---------|
| speak | `~/.local/bin/speak` | General TTS: args, stdin, or stop |
| speak-selection | `~/.local/bin/speak-selection` | X11 highlight-and-speak |
| Piper | `~/.local/bin/piper` (pipx) | Neural TTS engine |
| Voice model | `~/.local/share/piper-voices/en_US-amy-medium.onnx` | Amy medium voice |

## Stop/Toggle Behavior

Both scripts use PID files for stop control:
1. On invocation, check if PID file exists
2. If exists → kill that process, remove PID file, exit (toggle off)
3. If not → write own PID, speak text, remove PID file on completion

## Future Extensions

- Multiple voice models selectable via `speak -v male "text"`
- Speed control via Piper `--length-scale`
- Volume control via Piper `--volume`
- Wayland support via wl-paste (when session switches)
