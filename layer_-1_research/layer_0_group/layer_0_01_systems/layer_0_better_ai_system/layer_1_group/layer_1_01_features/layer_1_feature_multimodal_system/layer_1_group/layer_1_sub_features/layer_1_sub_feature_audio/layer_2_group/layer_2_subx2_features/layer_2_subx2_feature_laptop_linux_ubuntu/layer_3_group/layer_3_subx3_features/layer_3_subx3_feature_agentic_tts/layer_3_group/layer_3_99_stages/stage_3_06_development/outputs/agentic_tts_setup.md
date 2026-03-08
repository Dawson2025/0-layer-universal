---
resource_id: "a4bc20c0-2259-41fc-aedf-7159ef98c9b2"
resource_type: "output"
resource_name: "agentic_tts_setup"
---
# Agentic TTS Setup — Development Log

**Date**: 2026-02-23 (updated 2026-03-08)
**Status**: Working — Piper Stop hook + VoiceMode MCP integration

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
## VoiceMode MCP Integration

- Installed VoiceMode via `uvx voice-mode-install` and added the `voicemode` MCP server to Codex with `codex mcp add voicemode -- /home/dawson/.local/bin/voicemode --tools-enabled converse,service` so the agent can call `/voicemode:converse` without additional credentials.
- Confirmed `codex mcp list` shows `voicemode` enabled and `~/.codex/config.toml` contains the new `[mcp_servers.voicemode]` block that points at the local binary.
- Enabled and started VoiceMode services, installing Whisper with `voicemode service install whisper`, enabling `voicemode-whisper.service`, and letting Kokoro manage GPU-backed `/v1` endpoints through `voicemode-kokoro.service`. This ensured HTTP endpoints `/v1/test` and the streaming TTS path are reachable.

## Codex Verification Notes

- `voicemode status` reports Kokoro (`port 8880`, voice `af_sky`) and Whisper (`port 2022`, model `base`) both running with healthy status.
- Local systemd services `voicemode-kokoro.service` and `voicemode-whisper.service` are enabled so they survive login restarts.
- `ss -ltnp` confirms UDP 2022 and TCP 8880 listeners bound to the local loopback address for the new MCP flow.

<!-- section_id: "b7c8d9e0-f1a2-4b3c-5d6e-7f8a9b0c1d2e" -->
## Claude Code CLI MCP Integration (2026-03-08)

### Registration
```bash
claude mcp add-json -s user voicemode '{
  "type": "stdio",
  "command": "/home/dawson/.local/bin/voicemode",
  "args": ["--tools-enabled", "converse,service"],
  "env": {
    "OPENAI_API_KEY": "dummy-local-only",
    "VOICEMODE_TTS_PROVIDER": "kokoro",
    "VOICEMODE_STT_PROVIDER": "whisper",
    "VOICEMODE_PREFER_LOCAL": "true",
    "VOICEMODE_ALWAYS_TRY_LOCAL": "true"
  }
}'
```

### Permissions
Added to `~/.claude/settings.json` allowlist:
- `mcp__voicemode__converse`
- `mcp__voicemode__service`

### Key Blocker Fix
The VoiceMode MCP client validates `OPENAI_API_KEY` exists in the process environment before allowing tool calls, even when all providers are local. Setting `OPENAI_API_KEY=dummy-local-only` in the MCP server env config satisfies this validation. No external API calls are made.

### Verified Working
- `mcp__voicemode__service`: Reports Kokoro and Whisper status (GPU-accelerated, CUDA)
- `mcp__voicemode__converse` (speak only): Kokoro TTS generation ~1.0s, playback ~8.8s
- `mcp__voicemode__converse` (full round-trip): Speak + listen + transcribe ~10.9s
- All processing local — Kokoro on port 8880 (RTX 4060), Whisper on port 2022 (CUDA)

## Future Enhancements

- [ ] Split-output pattern: Claude emits `spoken_summary` field for TTS-optimized text
- [ ] PostToolUse hook for long-running tool completion announcements
- [ ] Voice selection based on context (different voices for errors vs success)
- [ ] Speech queue instead of kill-and-replace
- [ ] Configurable max length and verbosity
- [ ] Continuing VoiceMode tuning (tool blacklist/whitelist controls)
