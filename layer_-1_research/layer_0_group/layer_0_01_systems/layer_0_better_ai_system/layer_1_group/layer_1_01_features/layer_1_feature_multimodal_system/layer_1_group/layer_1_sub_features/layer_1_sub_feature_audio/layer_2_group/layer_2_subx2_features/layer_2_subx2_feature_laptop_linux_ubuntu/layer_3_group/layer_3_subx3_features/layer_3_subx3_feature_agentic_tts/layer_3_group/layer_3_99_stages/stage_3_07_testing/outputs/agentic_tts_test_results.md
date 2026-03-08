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
| 6 | VoiceMode MCP stream | `voicemode converse -m "VoiceMode test ..." --tts-provider kokoro --voice af_sky --no-wait` | Vital voice stream works via `/v1` | PASS |
| 7 | Claude Code MCP TTS (speak only) | `mcp__voicemode__converse` with `wait_for_response: false` | Speaks message via Kokoro | **PASS** |
| 8 | Claude Code MCP full round-trip | `mcp__voicemode__converse` with `wait_for_response: true` | Speaks + listens via Whisper + transcribes | **PASS** |

<!-- section_id: "5ca771a5-9f70-4e3b-973e-25504a7ce1d5" -->
## Performance

### Piper Hook (legacy)
- Hook script startup: <50ms
- jq + sed processing: <100ms
- Piper synthesis: ~500ms-2s (depends on length)
- Total perceived latency: ~1-2s after Claude finishes

### VoiceMode MCP (current — 2026-03-08)
- Kokoro TTS generation: ~0.4-1.0s
- Audio playback: ~3.8-8.8s (depends on message length)
- Whisper STT recording: ~6.0s
- Whisper transcription: ~0.6s
- Full round-trip (speak + listen + transcribe): ~10.9s

<!-- section_id: "d3e6b66a-1e1b-41e7-a307-9d3d064b5c72" -->
## Integration Verification

- `curl -i http://127.0.0.1:8880/v1/test` now returns HTTP 200 `{"status":"ok"}` after restarting `voicemode-kokoro.service`, proving the FastAPI `/v1` routes are accessible instead of the old 404 BaseHTTP server.
- `voicemode converse ...` produced a streamed Kokoro response (TTFA ~0.43s, total ~3.7s) and completed without falling back to OpenAI, confirming the Codex MCP entry can trigger local TTS output.

### Claude Code CLI MCP Integration (2026-03-08)

**Setup**:
- Registered VoiceMode as MCP server in `~/.claude.json` via `claude mcp add-json -s user voicemode '{...}'`
- Command: `/home/dawson/.local/bin/voicemode --tools-enabled converse,service`
- Environment variables: `OPENAI_API_KEY=dummy-local-only`, `VOICEMODE_TTS_PROVIDER=kokoro`, `VOICEMODE_STT_PROVIDER=whisper`, `VOICEMODE_PREFER_LOCAL=true`, `VOICEMODE_ALWAYS_TRY_LOCAL=true`
- Added `mcp__voicemode__converse` and `mcp__voicemode__service` to allowlist in `~/.claude/settings.json`

**Key fix**: The `OPENAI_API_KEY=dummy-local-only` env var is required in the MCP server process environment. The VoiceMode MCP client layer validates this key exists before allowing tool calls, even when all providers are configured as local (Kokoro/Whisper). The dummy value satisfies validation without making any external API calls.

**Test results**:
- `mcp__voicemode__service` status checks: Kokoro and Whisper both report healthy
- `mcp__voicemode__converse` speak-only (`wait_for_response: false`): 1.0s generation, 8.8s playback — **PASS**
- `mcp__voicemode__converse` full round-trip (`wait_for_response: true`): speak + listen + transcribe in 10.9s — **PASS**
- All audio processed locally via GPU-accelerated Kokoro (port 8880) and Whisper CUDA (port 2022)

## Known Issues

| Issue | Severity | Notes |
|-------|----------|-------|
| ~~Live test pending~~ | ~~Medium~~ | **Resolved** — MCP integration tested and passing (2026-03-08) |
| sed strip patterns may miss edge cases | Low | Complex markdown may leak through (Piper hook only) |
| No speech for tool-only responses | Low | PostToolUse hook planned for future |
| Piper Stop hook still active alongside MCP | Low | Can disable after confirming MCP is stable |
