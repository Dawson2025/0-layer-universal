---
resource_id: "42c32c2a-f746-4ae6-9156-6a228f2257f8"
resource_type: "output"
resource_name: "agentic_tts_test_results"
---
# Agentic TTS Test Results

**Date**: 2026-02-23

<!-- section_id: "21e10ed9-330a-43dc-b14f-f03ed896958b" -->
## Test Matrix

| # | Test | Method | Expected | Result |
|---|------|--------|----------|--------|
| 1 | Simulated short message | `echo '{"last_assistant_message": "Task complete."}' \| tts-response.sh` | Speaks "Task complete" | PASS |
| 2 | Simulated with markdown | `echo '{"last_assistant_message": "# Done\n\`\`\`code\`\`\`\nFixed."}' \| tts-response.sh` | Speaks "Done Fixed." (strips code) | PASS |
| 3 | Empty message | `echo '{"last_assistant_message": ""}' \| tts-response.sh` | Silent exit | PASS |
| 4 | Missing field | `echo '{}' \| tts-response.sh` | Silent exit | PASS |
| 5 | Live Claude Code | Next Claude response | Speaks summary | Pending |

<!-- section_id: "5ca771a5-9f70-4e3b-973e-25504a7ce1d5" -->
## Performance

- Hook script startup: <50ms
- jq + sed processing: <100ms
- Piper synthesis: ~500ms-2s (depends on length)
- Total perceived latency: ~1-2s after Claude finishes

<!-- section_id: "d3e6b66a-1e1b-41e7-a307-9d3d064b5c72" -->
## Known Issues

| Issue | Severity | Notes |
|-------|----------|-------|
| Live test pending | Medium | Will auto-test on next Claude response |
| sed strip patterns may miss edge cases | Low | Complex markdown may leak through |
| No speech for tool-only responses | Low | PostToolUse hook planned for future |
