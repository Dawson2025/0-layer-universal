---
resource_id: "44241c8d-85ce-4186-ab53-9d85249d0a62"
resource_type: "output"
resource_name: "agentic_tts_current_product"
---
# Agentic TTS — Current Product

**Date**: 2026-02-23
**Status**: Working (basic Stop hook, pending live test)

<!-- section_id: "d43dca09-0179-4dd1-8590-a48baaaca695" -->
## What's Delivered

<!-- section_id: "e479332f-cc5e-4c97-bb84-c73ba9a285c2" -->
### Hook Script

| File | Location | Purpose |
|------|----------|---------|
| tts-response.sh | `~/.claude/hooks/tts-response.sh` | Stop hook — speaks Claude response summary |

<!-- section_id: "3640c630-f21e-4172-8558-4ee8e28a82a4" -->
### Configuration

In `~/.claude/settings.json`, Stop hook array:
1. Completion sound (paplay/aplay)
2. TTS response (tts-response.sh, 60s timeout)

<!-- section_id: "22a3084e-84c0-445c-8bd0-34f206de848b" -->
### Behavior

When Claude finishes responding:
1. Completion chime plays
2. Hook extracts `last_assistant_message` from JSON
3. Strips markdown formatting for speech
4. Truncates to ~600 chars at word boundary
5. Speaks via Piper Amy voice in background

<!-- section_id: "4237ea3a-c5fa-43e9-be1b-5b7aacc02820" -->
### Shared Infrastructure

Uses the same Piper TTS + Amy voice model as system TTS. No additional installation needed.

<!-- section_id: "96614705-ba49-4898-b33e-bb293e1567c5" -->
## Limitations

- Only speaks on Stop event (not PostToolUse or SubagentStop)
- No split-output pattern (no spoken_summary field from Claude)
- Crude markdown stripping via sed
- Fixed 600-char truncation
- No per-response disable option
