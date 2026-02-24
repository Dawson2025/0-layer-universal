# Agentic TTS Requirements

**Date**: 2026-02-23

## Core Requirements

1. **Auto-speak Claude responses**: When Claude finishes responding, automatically speak a summary
2. **Markdown cleanup**: Strip code blocks, URLs, file paths, tables before speaking
3. **Length control**: Truncate long responses to a spoken summary (~600 chars)
4. **Non-blocking**: Speech runs in background — Claude remains interactive
5. **Kill switch**: New speech replaces old (no overlapping speech)
6. **Offline**: Uses local Piper TTS, no cloud APIs

## User Stories

- As a developer, I want Claude to speak its response summary so I can look away from the screen while it works
- As a user, I want long responses truncated to a brief spoken overview
- As a developer, I want to hear a completion sound AND a spoken summary when Claude finishes

## Constraints

- Must use Claude Code hooks system (Stop event)
- Hook receives JSON on stdin with `last_assistant_message` field
- Must coexist with existing completion sound hook
- Must not conflict with system TTS (separate PID file: `/tmp/claude-tts.pid`)
- Timeout: 60 seconds max for speech

## Acceptance Criteria

- [ ] Claude's Stop hook triggers TTS of response summary
- [ ] Code blocks and markdown are stripped from speech
- [ ] Long responses are truncated at word boundary
- [ ] Completion sound plays before/alongside TTS
- [ ] Can manually kill speech via `kill $(cat /tmp/claude-tts.pid)`
