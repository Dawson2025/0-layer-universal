---
resource_id: "12e98370-a924-464a-ab67-e955493aee46"
resource_type: "output"
resource_name: "cli_speak_command"
---
# Design: CLI `speak` Command

**Purpose**: Speak text from the terminal — arguments, stdin, or pipe.
**Priority**: Secondary — convenience for terminal workflows and scripting.

<!-- section_id: "aa4e8977-f7c2-48ec-ba12-aec1740866ae" -->
## User Flow

```bash
speak "Hello world"              # from arguments
echo "Read this" | speak         # from stdin/pipe
cat article.txt | speak          # read a file
speak -s                         # stop current speech
```

<!-- section_id: "b2c9c1b4-44c4-4016-9afe-0cf9e8ebd815" -->
## Current Implementation (Working)

```
speak "text" or echo "text" | speak
  → /home/dawson/.local/bin/speak
  → piper --model en_US-amy-medium --output-raw
  → paplay --raw --rate=22050 --channels=1 --format=s16le
  → speakers
```

<!-- section_id: "5fba33da-cbd4-46c1-8da4-f49a8d71a0dd" -->
### Script Logic

1. `-s`/`--stop` flag: kill PID from `/tmp/speak.pid`, exit
2. Kill any existing speak process (auto-cancel previous)
3. Get text from `$*` (args) or `cat` (stdin)
4. Write PID, pipe text through Piper → paplay, clean up

<!-- section_id: "01358283-d8a9-4a82-9377-3d79c0ddaf64" -->
### Components

| Component | Location | Role |
|-----------|----------|------|
| speak | `~/.local/bin/speak` | Orchestration script |
| Piper | `~/.local/bin/piper` | Neural TTS engine |
| paplay | `/usr/bin/paplay` | Audio playback |

<!-- section_id: "4f73f42e-2153-43f5-a766-1934a685d120" -->
## Target Implementation (Kokoro Upgrade)

```bash
speak "Hello world"
  → curl -s http://localhost:8880/v1/audio/speech \
      -H "Content-Type: application/json" \
      -d '{"input":"Hello world","voice":"af_heart","model":"kokoro"}' \
      --output -
  → paplay --raw --rate=24000 --channels=1 --format=s16le
```

<!-- section_id: "ea739252-230e-4318-b0d3-f29bd4aa4a0a" -->
### Fallback

If Kokoro server is not running, fall back to Piper:
```bash
if ! curl -sf http://localhost:8880/v1/models > /dev/null 2>&1; then
    # Piper fallback
    echo "$TEXT" | piper --model "$VOICE" --output-raw | paplay ...
else
    # Kokoro primary
    curl ... | paplay ...
fi
```

<!-- section_id: "0c32a526-c7fd-480d-97ae-5dfb462f2d5e" -->
## Design Notes

- `speak` and `speak-selection` share the same TTS backend — changing one changes both
- PID-based stop mechanism works for both Piper (process) and Kokoro (curl + paplay process group)
- No network dependency — Kokoro server runs locally on localhost:8880
