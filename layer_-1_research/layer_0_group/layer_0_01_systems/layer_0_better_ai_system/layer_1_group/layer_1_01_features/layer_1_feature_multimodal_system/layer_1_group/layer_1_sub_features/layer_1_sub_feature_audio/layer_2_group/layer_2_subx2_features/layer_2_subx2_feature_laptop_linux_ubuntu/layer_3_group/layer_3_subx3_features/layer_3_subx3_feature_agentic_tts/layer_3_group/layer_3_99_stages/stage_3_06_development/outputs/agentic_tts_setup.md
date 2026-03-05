---
resource_id: "a4bc20c0-2259-41fc-aedf-7159ef98c9b2"
resource_type: "output"
resource_name: "agentic_tts_setup"
---
# Agentic TTS Setup — Development Log

**Date**: 2026-02-23
**Status**: Working (basic Stop hook)

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

## Implementation

### Hook Script: `~/.claude/hooks/tts-response.sh`

Features:
- Reads `last_assistant_message` from Stop hook JSON via `jq`
- Cleans markdown for speech (removes code blocks, inline code, headers, bold/italic, URLs, file paths, table pipes)
- Truncates to 600 chars at word boundary for spoken summary
- Kills any existing speech before starting new
- Runs speech in background (doesn't block Claude)
- Uses Piper with Amy voice model

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

## Test Results

| Test | Method | Result |
|------|--------|--------|
| Simulated JSON input | `echo '{"last_assistant_message": "..."}' \| tts-response.sh` | Works — speaks the message |
| Live Claude Code | Pending next response | Will auto-test on this response |

## Available Hook Events for Future Use

| Event | Use Case |
|-------|----------|
| Stop | Speak response summary (current) |
| PostToolUse | Announce tool completion |
| SubagentStop | Announce subagent results |
| Notification | Speak notifications |
| TaskCompleted | Announce team task completion |

## Future Enhancements

- [ ] Split-output pattern: Claude emits `spoken_summary` field for TTS-optimized text
- [ ] PostToolUse hook for long-running tool completion announcements
- [ ] Voice selection based on context (different voices for errors vs success)
- [ ] Speech queue instead of kill-and-replace
- [ ] Configurable max length and verbosity
- [ ] Integration with Kokoro for more voices
