# Design: Kokoro Migration (Piper → Kokoro)

**Purpose**: Upgrade the TTS engine from Piper (CPU, good quality) to Kokoro (GPU, best quality).
**Priority**: Next action — the main improvement to make.

## Why Kokoro

| Metric | Piper (current) | Kokoro (target) |
|--------|-----------------|-----------------|
| Quality | High (VITS, 60MB model) | Highest (#1 HuggingFace TTS Arena, 82M params) |
| Speed | ~1s (CPU cold start + generation) | Sub-0.1s (GPU-accelerated, warm server) |
| Voices | 1 (Amy medium, US female) | 40+ built-in (multiple accents, genders) |
| Architecture | CLI process per invocation | FastAPI server (persistent, OpenAI-compatible) |
| GPU | Not used | RTX 4060, ~200-300MB VRAM |
| API | None | OpenAI-compatible `/v1/audio/speech` |

## Architecture

```
                    ┌─────────────────────────────────┐
                    │  Kokoro FastAPI Server           │
                    │  (systemd user service)          │
                    │                                  │
                    │  localhost:8880                   │
                    │  GPU: RTX 4060 (CUDA)            │
                    │  Model: kokoro-82M               │
                    │  VRAM: ~200-300MB                │
                    │  API: /v1/audio/speech            │
                    └──────────┬──────────────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    speak-selection       speak CLI      Speech Dispatcher
    (Ctrl+Alt+S)         (terminal)      (spd-say, apps)
              │                │                │
              └────────────────┼────────────────┘
                               │
                         curl → paplay
                               │
                           speakers
```

All three consumers (highlight-and-speak, CLI, Speech Dispatcher) call the same Kokoro server. Single point of TTS, single voice config.

## Installation Plan

### Step 1: Install Kokoro FastAPI (GPU)

```bash
# Install with GPU support
pip install kokoro-fastapi[gpu]

# OR via uvx (isolated)
uvx kokoro-fastapi[gpu] serve
```

### Step 2: Create Systemd User Service

```ini
# ~/.config/systemd/user/kokoro-tts.service
[Unit]
Description=Kokoro TTS FastAPI Server (GPU)
After=network.target

[Service]
Type=simple
ExecStart=%h/.local/bin/kokoro-fastapi serve --host 127.0.0.1 --port 8880
Restart=on-failure
RestartSec=5
Environment=CUDA_VISIBLE_DEVICES=0

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now kokoro-tts.service
```

### Step 3: Verify Server

```bash
# Check it's running
curl -s http://localhost:8880/v1/models | jq .

# Test speech
curl -s http://localhost:8880/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"input":"Hello from Kokoro","voice":"af_heart","model":"kokoro"}' \
  --output /tmp/test.wav && paplay /tmp/test.wav
```

### Step 4: Update speak-selection

Replace Piper pipe with Kokoro curl in `~/.local/bin/speak-selection`:

```bash
# Old (Piper):
echo "$TEXT" | piper --model "$VOICE" --output-raw | paplay --raw --rate=22050 ...

# New (Kokoro with Piper fallback):
if curl -sf http://localhost:8880/v1/models > /dev/null 2>&1; then
    curl -s http://localhost:8880/v1/audio/speech \
      -H "Content-Type: application/json" \
      -d "{\"input\":$(echo "$TEXT" | jq -Rs .),\"voice\":\"af_heart\",\"model\":\"kokoro\",\"response_format\":\"pcm\"}" \
      --output - | paplay --raw --rate=24000 --channels=1 --format=s16le
else
    # Piper fallback
    echo "$TEXT" | piper --model "$VOICE" --output-raw | paplay --raw --rate=22050 --channels=1 --format=s16le
fi
```

### Step 5: Update speak

Same change as speak-selection — swap TTS backend.

### Step 6: Update Speech Dispatcher Module

Create `~/.config/speech-dispatcher/modules/kokoro-generic.conf` and set as default in `speechd.conf`.

### Step 7: Test

```bash
# Highlight text, Ctrl+Alt+S — should use Kokoro (near-instant)
# speak "test" — should use Kokoro
# spd-say "test" — should use Kokoro via Speech Dispatcher
# Stop Kokoro service → verify Piper fallback works
```

## Rollback

If Kokoro causes issues:
1. `systemctl --user stop kokoro-tts.service`
2. Scripts auto-fall back to Piper (fallback built into design)
3. No need to revert any files

## Future: VoiceMode MCP

After Kokoro is working standalone, VoiceMode MCP server can manage the Kokoro lifecycle and add Claude Code voice integration. That's the agentic_tts feature, separate from system TTS.
