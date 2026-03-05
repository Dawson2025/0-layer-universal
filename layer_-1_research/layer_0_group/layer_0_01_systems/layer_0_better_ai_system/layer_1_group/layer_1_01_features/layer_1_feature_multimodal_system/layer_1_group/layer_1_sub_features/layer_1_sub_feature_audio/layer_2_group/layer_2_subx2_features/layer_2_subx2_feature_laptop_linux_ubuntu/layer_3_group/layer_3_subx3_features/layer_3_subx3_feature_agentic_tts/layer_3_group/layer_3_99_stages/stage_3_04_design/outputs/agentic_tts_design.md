---
resource_id: "eaf64a0c-e57f-404b-9b1b-c956c03756ed"
resource_type: "output"
resource_name: "agentic_tts_design"
---
# Agentic TTS Design

**Date**: 2026-02-23

<!-- section_id: "24021c8a-e063-49f3-a684-0c294851398e" -->
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

<!-- section_id: "e6b75cea-686b-4ed3-b18c-afe6f4c13883" -->
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

<!-- section_id: "e84cc9d7-f02d-4201-b1ed-691365522989" -->
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

<!-- section_id: "c3393009-c12b-4466-b80d-7cf3bc19448f" -->
## Future: Split-Output Pattern

Claude could emit structured output:
```json
{
  "spoken_summary": "I fixed the bug in the login function.",
  "visual_output": "## Changes\n- Modified `auth.py:42`\n- Updated test..."
}
```

The hook would prefer `spoken_summary` when present, falling back to `last_assistant_message` cleanup.
