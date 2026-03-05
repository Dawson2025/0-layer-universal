---
resource_id: "aacb9ed6-beed-495a-9b65-71a87e41a5fc"
resource_type: "output"
resource_name: "kokoro_migration"
---
# Design: Kokoro Migration (Piper → Kokoro)

**Purpose**: Upgrade the TTS engine from Piper (CPU, good quality) to Kokoro (GPU, best quality).
**Priority**: Next action — the main improvement to make.

<!-- section_id: "8ca7329f-7e52-4da4-a21b-8a2c2234a557" -->
## Why Kokoro

| Metric | Piper (current) | Kokoro (target) |
|--------|-----------------|-----------------|
| Quality | High (VITS, 60MB model) | Highest (#1 HuggingFace TTS Arena, 82M params) |
| Speed | ~1s (CPU cold start + generation) | Sub-0.1s (GPU-accelerated, warm server) |
| Voices | 1 (Amy medium, US female) | 40+ built-in (multiple accents, genders) |
| Architecture | CLI process per invocation | FastAPI server (persistent, OpenAI-compatible) |
| GPU | Not used | RTX 4060, ~200-300MB VRAM |
| API | None | OpenAI-compatible `/v1/audio/speech` |

<!-- section_id: "b02d56fa-346f-4972-8ca0-c7c9e6a406aa" -->
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

<!-- section_id: "371690df-a100-4124-b0f1-48d0fc2a6129" -->
## Installation Plan

<!-- section_id: "ff8d238c-d3ec-4980-bb98-6ab9c5b9de3d" -->
### Step 1: Install Kokoro FastAPI (GPU)

```bash
# Install with GPU support
pip install kokoro-fastapi[gpu]

# OR via uvx (isolated)
uvx kokoro-fastapi[gpu] serve
```

<!-- section_id: "cf48ccb6-6316-4fda-a088-4675b8f05c1b" -->
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

<!-- section_id: "05766c50-c32a-4400-b0b6-06314f81abbd" -->
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

<!-- section_id: "abf8dfb2-125e-4279-aa8f-4c79ed36e2f0" -->
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

<!-- section_id: "98b5b984-4734-4d26-8e84-b22250471275" -->
### Step 5: Update speak

Same change as speak-selection — swap TTS backend.

<!-- section_id: "7072d431-d786-44aa-9101-c66f8b1e140e" -->
### Step 6: Update Speech Dispatcher Module

Create `~/.config/speech-dispatcher/modules/kokoro-generic.conf` and set as default in `speechd.conf`.

<!-- section_id: "c48dd09e-0b1d-4e97-bc25-5766b7b7d802" -->
### Step 7: Test

```bash
# Highlight text, Ctrl+Alt+S — should use Kokoro (near-instant)
# speak "test" — should use Kokoro
# spd-say "test" — should use Kokoro via Speech Dispatcher
# Stop Kokoro service → verify Piper fallback works
```

<!-- section_id: "1291489b-6f42-4f27-beef-171c50e4ecd2" -->
## Rollback

If Kokoro causes issues:
1. `systemctl --user stop kokoro-tts.service`
2. Scripts auto-fall back to Piper (fallback built into design)
3. No need to revert any files

<!-- section_id: "48608b00-b0b3-4823-9825-b10b4c5bf848" -->
## Future: VoiceMode MCP

After Kokoro is working standalone, VoiceMode MCP server can manage the Kokoro lifecycle and add Claude Code voice integration. That's the agentic_tts feature, separate from system TTS.
