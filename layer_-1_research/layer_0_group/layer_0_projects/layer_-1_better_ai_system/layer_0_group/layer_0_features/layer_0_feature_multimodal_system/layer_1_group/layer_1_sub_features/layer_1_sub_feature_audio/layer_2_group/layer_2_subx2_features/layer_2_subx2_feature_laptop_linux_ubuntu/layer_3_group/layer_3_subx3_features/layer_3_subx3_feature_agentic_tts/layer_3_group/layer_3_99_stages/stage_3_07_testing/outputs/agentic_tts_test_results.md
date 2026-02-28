# Agentic TTS Test Results

**Date**: 2026-02-23

## Test Matrix

| # | Test | Method | Expected | Result |
|---|------|--------|----------|--------|
| 1 | Simulated short message | `echo '{"last_assistant_message": "Task complete."}' \| tts-response.sh` | Speaks "Task complete" | PASS |
| 2 | Simulated with markdown | `echo '{"last_assistant_message": "# Done\n\`\`\`code\`\`\`\nFixed."}' \| tts-response.sh` | Speaks "Done Fixed." (strips code) | PASS |
| 3 | Empty message | `echo '{"last_assistant_message": ""}' \| tts-response.sh` | Silent exit | PASS |
| 4 | Missing field | `echo '{}' \| tts-response.sh` | Silent exit | PASS |
| 5 | Live Claude Code | Next Claude response | Speaks summary | Pending |

## Performance

- Hook script startup: <50ms
- jq + sed processing: <100ms
- Piper synthesis: ~500ms-2s (depends on length)
- Total perceived latency: ~1-2s after Claude finishes

## Known Issues

| Issue | Severity | Notes |
|-------|----------|-------|
| Live test pending | Medium | Will auto-test on next Claude response |
| sed strip patterns may miss edge cases | Low | Complex markdown may leak through |
| No speech for tool-only responses | Low | PostToolUse hook planned for future |
