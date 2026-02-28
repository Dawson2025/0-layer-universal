# Agentic TTS — Current Product

**Date**: 2026-02-23
**Status**: Working (basic Stop hook, pending live test)

## What's Delivered

### Hook Script

| File | Location | Purpose |
|------|----------|---------|
| tts-response.sh | `~/.claude/hooks/tts-response.sh` | Stop hook — speaks Claude response summary |

### Configuration

In `~/.claude/settings.json`, Stop hook array:
1. Completion sound (paplay/aplay)
2. TTS response (tts-response.sh, 60s timeout)

### Behavior

When Claude finishes responding:
1. Completion chime plays
2. Hook extracts `last_assistant_message` from JSON
3. Strips markdown formatting for speech
4. Truncates to ~600 chars at word boundary
5. Speaks via Piper Amy voice in background

### Shared Infrastructure

Uses the same Piper TTS + Amy voice model as system TTS. No additional installation needed.

## Limitations

- Only speaks on Stop event (not PostToolUse or SubagentStop)
- No split-output pattern (no spoken_summary field from Claude)
- Crude markdown stripping via sed
- Fixed 600-char truncation
- No per-response disable option
