---
resource_id: "85d44162-c206-4488-b40c-64ec6df959d4"
resource_type: "output"
resource_name: "agentic_tts_plan"
---
# Agentic TTS Implementation Plan

**Date**: 2026-02-23

## Completed Steps

1. [x] Research Claude Code hooks API (Stop event, JSON format)
2. [x] Create tts-response.sh hook script
3. [x] Implement markdown stripping for speech-friendly text
4. [x] Implement truncation at word boundary
5. [x] Add background execution (non-blocking)
6. [x] Add PID-based kill-existing-speech
7. [x] Add hook to ~/.claude/settings.json
8. [x] Test with simulated JSON input

## Remaining Steps

9. [ ] Live test (next Claude Code response will auto-test)
10. [ ] Tune truncation length based on real responses
11. [ ] Add PostToolUse hook for long-running tool announcements
12. [ ] Implement split-output pattern (spoken_summary field)
13. [ ] Add SubagentStop hook for team workflow announcements
14. [ ] Consider voice differentiation (different voice for errors vs success)
