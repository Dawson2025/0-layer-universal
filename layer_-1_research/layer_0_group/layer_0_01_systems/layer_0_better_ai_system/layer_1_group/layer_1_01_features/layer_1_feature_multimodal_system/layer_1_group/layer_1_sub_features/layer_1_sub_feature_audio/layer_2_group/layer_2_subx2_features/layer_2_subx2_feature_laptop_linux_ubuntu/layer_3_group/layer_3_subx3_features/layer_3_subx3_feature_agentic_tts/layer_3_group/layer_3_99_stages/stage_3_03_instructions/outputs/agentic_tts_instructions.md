---
resource_id: "e135aa73-ef6f-4667-863c-9fd298d9d88f"
resource_type: "output"
resource_name: "agentic_tts_instructions"
---
# Agentic TTS Instructions / Constraints

**Date**: 2026-02-23

<!-- section_id: "838aff75-021e-4479-aae7-cb0c529d4ce1" -->
## Technical Constraints

1. **Hook script must exit 0**: Non-zero exit codes may be reported as hook failures
2. **PID file isolation**: Agentic TTS uses `/tmp/claude-tts.pid`, separate from system TTS
3. **Background execution**: Speech MUST run in background subshell `( ... ) &` — blocking the hook blocks Claude
4. **Timeout**: Hook has 60s timeout configured in settings.json
5. **jq required**: Hook parses JSON stdin with jq to extract `last_assistant_message`
6. **Truncation**: Max 600 chars spoken to keep summaries brief

<!-- section_id: "de78af0d-b7f8-4d0d-9098-a4adca5a4c98" -->
## Dependencies

- `jq` (JSON parsing from hook stdin)
- `piper` (via pipx — shared with system TTS)
- `aplay` (audio playback)
- Voice model at `~/.local/share/piper-voices/en_US-amy-medium.onnx`

<!-- section_id: "86206e02-1285-4796-a17a-270e4f812b20" -->
## Hook Configuration Rules

- Hooks are defined in `~/.claude/settings.json` under `hooks.Stop`
- Multiple hooks in same event array run sequentially
- Completion sound hook runs first, TTS hook runs second
- `timeout: 60` prevents runaway speech from blocking session

<!-- section_id: "5357b19a-9372-4434-9c44-49c1aa64f4cd" -->
## Do NOT

- Do not use synchronous speech in the hook (will block Claude)
- Do not parse the transcript JSONL file (use `last_assistant_message` field instead)
- Do not use `async: true` in settings — the background subshell handles async
