# Design: Highlight-and-Speak (Ctrl+Alt+S)

**Purpose**: Read any highlighted text aloud with a single keyboard shortcut.
**Priority**: Primary use case — this is the main reason system TTS exists.

## User Flow

```
1. User highlights text in any application
2. Presses Ctrl+Alt+S
3. Text is spoken aloud in a natural voice
4. Press Ctrl+Alt+S again to stop (toggle)
```

## Current Implementation (Working)

```
Ctrl+Alt+S (GNOME custom keybinding)
  → gsd-media-keys (must be running)
  → /home/dawson/.local/bin/speak-selection
  → xclip -selection primary -o (get highlighted text)
  → piper --model en_US-amy-medium --output-raw
  → paplay --raw --rate=22050 --channels=1 --format=s16le
  → speakers (via PipeWire)
```

### Components

| Component | Location | Role |
|-----------|----------|------|
| speak-selection | `~/.local/bin/speak-selection` | Orchestration script |
| xclip | `/usr/bin/xclip` | X11 selection/clipboard access |
| Piper | `~/.local/bin/piper` (pipx venv) | Neural TTS engine (CPU) |
| Amy voice | `~/.local/share/piper-voices/en_US-amy-medium.onnx` | Voice model |
| paplay | `/usr/bin/paplay` | PulseAudio playback |
| gsd-media-keys | GNOME daemon | Custom keybinding dispatch |

### Keybinding Config

```
dconf path: /org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/
binding: <Ctrl><Alt>s
command: /home/dawson/.local/bin/speak-selection
```

### Toggle Behavior

- PID file at `/tmp/speak-selection.pid`
- If PID file exists: kill process, remove PID file, exit (stop speech)
- If PID file absent: get text, speak, write PID, clean up on finish

### Fallback Chain

1. Primary X selection (highlighted text)
2. Clipboard (if no selection)
3. `notify-send` error if both empty

## Target Implementation (Kokoro Upgrade)

```
Ctrl+Alt+S (same keybinding)
  → speak-selection
  → xclip -selection primary -o
  → curl -s http://localhost:8880/v1/audio/speech \
      -H "Content-Type: application/json" \
      -d '{"input":"$TEXT","voice":"af_heart","model":"kokoro"}' \
      --output -
  → paplay --raw --rate=24000 --channels=1 --format=s16le
  → speakers
```

### What Changes

| Aspect | Piper (current) | Kokoro (target) |
|--------|----------------|-----------------|
| TTS engine | Piper CLI (process per invocation) | Kokoro FastAPI (persistent server) |
| Voice | Amy (1 voice) | 40+ voices (af_heart default) |
| Latency | ~1s startup + generation | Sub-0.1s (GPU, server warm) |
| Quality | High | Highest (#1 HF TTS Arena) |
| Sample rate | 22050 Hz | 24000 Hz |
| Dependencies | piper binary + model file | kokoro-fastapi server (systemd) |

### Migration Steps

1. Install Kokoro: `uvx kokoro-fastapi[gpu] serve`
2. Create systemd user service for Kokoro server
3. Update speak-selection: replace Piper pipe with curl to localhost:8880
4. Test with Ctrl+Alt+S
5. Keep Piper as fallback (if Kokoro server is down)

## Known Dependencies

- `gsd-media-keys` must be running for Ctrl+Alt+S to work
- `gsd-keepalive.timer` auto-restarts if it dies
- X11 session (xclip doesn't work on Wayland — need wl-paste for future)
- PipeWire audio stack must be functional
