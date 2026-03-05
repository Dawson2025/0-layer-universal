---
resource_id: "a4bc20c0-2259-41fc-aedf-7159ef98c9b2"
resource_type: "output"
resource_name: "agentic_tts_setup"
---
# Agentic TTS Setup — Development Log

**Date**: 2026-02-23
**Status**: Working (basic Stop hook)

<!-- section_id: "30c4d29b-9aa1-4af6-9b96-5447d4fc504e" -->
## Architecture

```
Claude Code responds
    ↓
Stop hook fires → JSON stdin with last_assistant_message
    ↓
tts-response.sh extracts text
    ↓
Strips markdown, code blocks, URLs, long paths
    ↓
Truncates to ~600 chars (spoken summary)
    ↓
Piper TTS → aplay (background)
```

<!-- section_id: "31671fc3-3bc8-4d61-9c87-8a32431782b7" -->
## Implementation

<!-- section_id: "20d95d68-128f-4801-bce2-54c88a62ce7b" -->
### Hook Script: `~/.claude/hooks/tts-response.sh`

Features:
- Reads `last_assistant_message` from Stop hook JSON via `jq`
- Cleans markdown for speech (removes code blocks, inline code, headers, bold/italic, URLs, file paths, table pipes)
- Truncates to 600 chars at word boundary for spoken summary
- Kills any existing speech before starting new
- Runs speech in background (doesn't block Claude)
- Uses Piper with Amy voice model

<!-- section_id: "5ca87c9b-5aa8-4503-b298-c2c4f9c8452c" -->
### Hook Configuration: `~/.claude/settings.json`

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "paplay /usr/share/sounds/freedesktop/stereo/complete.oga || aplay /usr/share/sounds/alsa/Front_Center.wav"
          },
          {
            "type": "command",
            "command": "/home/dawson/.claude/hooks/tts-response.sh",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

<!-- section_id: "8759ce6a-30f4-4fbd-b234-0687072f4d3e" -->
## Test Results

| Test | Method | Result |
|------|--------|--------|
| Simulated JSON input | `echo '{"last_assistant_message": "..."}' \| tts-response.sh` | Works — speaks the message |
| Live Claude Code | Pending next response | Will auto-test on this response |

<!-- section_id: "d2012d0c-c0ad-48f2-afe0-50b7d6f24db9" -->
## Available Hook Events for Future Use

| Event | Use Case |
|-------|----------|
| Stop | Speak response summary (current) |
| PostToolUse | Announce tool completion |
| SubagentStop | Announce subagent results |
| Notification | Speak notifications |
| TaskCompleted | Announce team task completion |

<!-- section_id: "e8dcc962-4184-41cc-a611-a6069888ed4d" -->
## Future Enhancements

- [ ] Split-output pattern: Claude emits `spoken_summary` field for TTS-optimized text
- [ ] PostToolUse hook for long-running tool completion announcements
- [ ] Voice selection based on context (different voices for errors vs success)
- [ ] Speech queue instead of kill-and-replace
- [ ] Configurable max length and verbosity
- [ ] Integration with Kokoro for more voices
