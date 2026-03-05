---
resource_id: "6a583f7b-e0f9-4f9f-862b-1fd7de5a128e"
resource_type: "output"
resource_name: "highlight_and_speak"
---
# Design: Highlight-and-Speak (Ctrl+Alt+S)

**Purpose**: Read any highlighted text aloud with a single keyboard shortcut.
**Priority**: Primary use case — this is the main reason system TTS exists.

<!-- section_id: "9836f09c-c204-4344-bc6d-aa1eee061569" -->
## User Flow

```
1. User highlights text in any application
2. Presses Ctrl+Alt+S
3. Text is spoken aloud in a natural voice
4. Press Ctrl+Alt+S again to stop (toggle)
```

<!-- section_id: "72f9d2cf-c37f-434d-9ade-8daa4a31a6f2" -->
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

<!-- section_id: "5ce2ca4b-19d9-4367-867e-2066b933624b" -->
### Components

| Component | Location | Role |
|-----------|----------|------|
| speak-selection | `~/.local/bin/speak-selection` | Orchestration script |
| xclip | `/usr/bin/xclip` | X11 selection/clipboard access |
| Piper | `~/.local/bin/piper` (pipx venv) | Neural TTS engine (CPU) |
| Amy voice | `~/.local/share/piper-voices/en_US-amy-medium.onnx` | Voice model |
| paplay | `/usr/bin/paplay` | PulseAudio playback |
| gsd-media-keys | GNOME daemon | Custom keybinding dispatch |

<!-- section_id: "3874988a-a45a-415d-a1bf-138faaf54c3b" -->
### Keybinding Config

```
dconf path: /org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/
binding: <Ctrl><Alt>s
command: /home/dawson/.local/bin/speak-selection
```

<!-- section_id: "b702c0ca-b1c1-4ae7-bd0e-3707c4b069a3" -->
### Toggle Behavior

- PID file at `/tmp/speak-selection.pid`
- If PID file exists: kill process, remove PID file, exit (stop speech)
- If PID file absent: get text, speak, write PID, clean up on finish

<!-- section_id: "2536cfa9-e3ab-411a-bd2e-3fbc55a96ea9" -->
### Fallback Chain

1. Primary X selection (highlighted text)
2. Clipboard (if no selection)
3. `notify-send` error if both empty

<!-- section_id: "40ebe805-4642-4f9c-9c45-d52d8bb91ced" -->
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

<!-- section_id: "026f826f-7bb6-424b-a52c-982a69ee927f" -->
### What Changes

| Aspect | Piper (current) | Kokoro (target) |
|--------|----------------|-----------------|
| TTS engine | Piper CLI (process per invocation) | Kokoro FastAPI (persistent server) |
| Voice | Amy (1 voice) | 40+ voices (af_heart default) |
| Latency | ~1s startup + generation | Sub-0.1s (GPU, server warm) |
| Quality | High | Highest (#1 HF TTS Arena) |
| Sample rate | 22050 Hz | 24000 Hz |
| Dependencies | piper binary + model file | kokoro-fastapi server (systemd) |

<!-- section_id: "19a4a50d-a0ac-4f45-9a03-86900f04c035" -->
### Migration Steps

1. Install Kokoro: `uvx kokoro-fastapi[gpu] serve`
2. Create systemd user service for Kokoro server
3. Update speak-selection: replace Piper pipe with curl to localhost:8880
4. Test with Ctrl+Alt+S
5. Keep Piper as fallback (if Kokoro server is down)

<!-- section_id: "f4523e3e-ad6b-4e37-8417-142c93c4fa1d" -->
## Known Dependencies

- `gsd-media-keys` must be running for Ctrl+Alt+S to work
- `gsd-keepalive.timer` auto-restarts if it dies
- X11 session (xclip doesn't work on Wayland — need wl-paste for future)
- PipeWire audio stack must be functional
