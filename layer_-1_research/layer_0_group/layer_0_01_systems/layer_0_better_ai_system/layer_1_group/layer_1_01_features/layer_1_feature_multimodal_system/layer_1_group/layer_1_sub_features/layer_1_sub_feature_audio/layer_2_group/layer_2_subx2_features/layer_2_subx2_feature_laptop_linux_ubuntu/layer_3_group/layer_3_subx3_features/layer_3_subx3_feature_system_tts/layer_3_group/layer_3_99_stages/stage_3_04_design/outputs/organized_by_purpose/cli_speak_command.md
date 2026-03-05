---
resource_id: "12e98370-a924-464a-ab67-e955493aee46"
resource_type: "output"
resource_name: "cli_speak_command"
---
# Design: CLI `speak` Command

**Purpose**: Speak text from the terminal — arguments, stdin, or pipe.
**Priority**: Secondary — convenience for terminal workflows and scripting.

## User Flow

```bash
speak "Hello world"              # from arguments
echo "Read this" | speak         # from stdin/pipe
cat article.txt | speak          # read a file
speak -s                         # stop current speech
```

## Current Implementation (Working)

```
speak "text" or echo "text" | speak
  → /home/dawson/.local/bin/speak
  → piper --model en_US-amy-medium --output-raw
  → paplay --raw --rate=22050 --channels=1 --format=s16le
  → speakers
```

### Script Logic

1. `-s`/`--stop` flag: kill PID from `/tmp/speak.pid`, exit
2. Kill any existing speak process (auto-cancel previous)
3. Get text from `$*` (args) or `cat` (stdin)
4. Write PID, pipe text through Piper → paplay, clean up

### Components

| Component | Location | Role |
|-----------|----------|------|
| speak | `~/.local/bin/speak` | Orchestration script |
| Piper | `~/.local/bin/piper` | Neural TTS engine |
| paplay | `/usr/bin/paplay` | Audio playback |

## Target Implementation (Kokoro Upgrade)

```bash
speak "Hello world"
  → curl -s http://localhost:8880/v1/audio/speech \
      -H "Content-Type: application/json" \
      -d '{"input":"Hello world","voice":"af_heart","model":"kokoro"}' \
      --output -
  → paplay --raw --rate=24000 --channels=1 --format=s16le
```

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

## Design Notes

- `speak` and `speak-selection` share the same TTS backend — changing one changes both
- PID-based stop mechanism works for both Piper (process) and Kokoro (curl + paplay process group)
- No network dependency — Kokoro server runs locally on localhost:8880
