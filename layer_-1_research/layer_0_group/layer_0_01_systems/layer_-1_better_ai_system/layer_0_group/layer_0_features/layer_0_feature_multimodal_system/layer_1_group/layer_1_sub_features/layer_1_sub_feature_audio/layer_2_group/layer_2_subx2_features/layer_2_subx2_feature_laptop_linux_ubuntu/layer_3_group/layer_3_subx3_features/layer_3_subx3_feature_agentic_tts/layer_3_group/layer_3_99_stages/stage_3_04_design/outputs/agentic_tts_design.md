# Agentic TTS Design

**Date**: 2026-02-23

## Architecture

```
Claude Code finishes responding
         │
         v
    Stop event fires
         │
         v
    ┌─────────────────────┐
    │ Hook 1: Sound        │  paplay complete.oga
    └─────────────────────┘
         │
         v
    ┌─────────────────────┐
    │ Hook 2: TTS          │  tts-response.sh
    │                      │
    │  1. Read JSON stdin   │
    │  2. jq extract msg    │
    │  3. sed strip markdown│
    │  4. cut truncate      │
    │  5. (piper | aplay)& │  ← background subshell
    └─────────────────────┘
         │
         v
    Hook exits 0 immediately
    Speech continues in background
```

## Text Processing Pipeline

```
last_assistant_message
    │
    ├─ Remove code blocks (``` ... ```)
    ├─ Remove inline code (`...`)
    ├─ Remove markdown headers (#)
    ├─ Remove bold/italic (** *)
    ├─ Remove URLs (https://...)
    ├─ Remove long file paths (/path/with/20+chars)
    ├─ Remove table pipes (|...|)
    ├─ Collapse whitespace
    └─ Truncate to 600 chars at word boundary
         │
         v
    Clean text → Piper → aplay
```

## Configuration (settings.json)

```json
{
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [
        {"type": "command", "command": "paplay ... || aplay ..."},
        {"type": "command", "command": "/home/dawson/.claude/hooks/tts-response.sh", "timeout": 60}
      ]
    }]
  }
}
```

## Future: Split-Output Pattern

Claude could emit structured output:
```json
{
  "spoken_summary": "I fixed the bug in the login function.",
  "visual_output": "## Changes\n- Modified `auth.py:42`\n- Updated test..."
}
```

The hook would prefer `spoken_summary` when present, falling back to `last_assistant_message` cleanup.
