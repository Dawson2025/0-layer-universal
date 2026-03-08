---
resource_id: "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b"
resource_type: "output"
resource_name: "voicemode_mcp_plan"
---
# VoiceMode MCP Implementation Plan

**Date**: 2026-03-07
**Status**: Approved, ready for implementation
**Design basis**: `stage_3_04_design/outputs/voicemode_mcp_design.md`
**Requirements**: `stage_3_01_request_gathering/outputs/agentic_tts_requirements.md` (REQ-1 through REQ-16)
**Replaces**: `agentic_tts_plan.md` (v1 Piper plan — steps 1-8 completed, steps 9-14 superseded)

---

<!-- section_id: "01-current-state" -->
## 1. Current System State

| Component | Status | Details |
|-----------|--------|---------|
| Kokoro TTS service | ✅ Running | Custom server at port 8880, `af_heart` voice, GPU-accelerated |
| Kokoro API format | ⚠️ Custom | `/tts` + `/health` only — NOT OpenAI-compatible (`/v1/audio/speech`) |
| speak-selection | ✅ Uses Kokoro | `~/.local/bin/speak-selection` calls `http://127.0.0.1:8880/tts` |
| Piper Stop hook | ✅ Active | `~/.claude/hooks/tts-response.sh` — CPU Piper, 600-char truncation |
| Whisper STT | ❌ Not installed | No service, no port 2022 |
| VoiceMode | ❌ Not installed | No `voicemode` command, no `~/.voicemode/`, no MCP entry |
| Audio dev libs | ✅ Installed | libasound2-dev, portaudio19-dev, python3-dev |
| GPU | ✅ Ready | RTX 4060, 6.2GB VRAM free, Kokoro using ~300MB |

### Key Compatibility Issue

VoiceMode expects an OpenAI-compatible TTS API at `http://127.0.0.1:8880/v1/audio/speech`.
Our custom Kokoro server only provides `/tts` (custom format) and `/health`.
The system TTS (`speak-selection`) depends on our custom `/tts` endpoint.

**This incompatibility is the primary risk and must be resolved first.**

<!-- section_id: "02-implementation-steps" -->
## 2. Implementation Steps

### Step 1: Install VoiceMode

```bash
uvx voice-mode-install
```

- Creates `~/.voicemode/` directory
- Installs the `voicemode` CLI tool
- **Verify**: `ls ~/.voicemode/` and `which voicemode`

### Step 2: Investigate VoiceMode's Kokoro Service

Before installing VoiceMode's own Kokoro, determine what it provides:

```bash
voicemode service install kokoro --help
```

**Questions to answer**:
- Does it install `kokoro-fastapi` (OpenAI-compatible)?
- Does it detect the existing Kokoro service?
- What port does it use?
- Can it be configured to use our existing server?

**Decision point**: Based on findings, choose Option A or Option B below.

### Step 3: Handle Kokoro Service Transition

#### Option A (Preferred): Let VoiceMode Manage Kokoro

If VoiceMode installs a proper OpenAI-compatible Kokoro server:

1. Stop custom service: `systemctl --user stop kokoro-tts`
2. Disable custom service: `systemctl --user disable kokoro-tts`
3. Install VoiceMode Kokoro: `voicemode service install kokoro`
4. Enable + start: `voicemode service enable kokoro && voicemode service start kokoro`
5. Verify port 8880 responds to `/v1/audio/speech`
6. Update `~/.local/bin/speak-selection` to use new API format
7. Test Ctrl+Alt+S shortcut

**Pros**: Clean, single source of truth for Kokoro, VoiceMode manages everything
**Cons**: Must update speak-selection, temporary service disruption

#### Option B (Fallback): Keep Custom Kokoro, Add Compatibility

If VoiceMode can be configured to use a custom endpoint, or if we add OpenAI-compatible routes:

1. Modify `/home/dawson/.local/share/kokoro-tts/server.py`:
   - Add `/v1/audio/speech` endpoint (OpenAI-compatible format)
   - Keep existing `/tts` endpoint (speak-selection unchanged)
2. Restart custom service: `systemctl --user restart kokoro-tts`
3. Point VoiceMode at `http://127.0.0.1:8880/v1`

**Pros**: No disruption to speak-selection, minimal changes
**Cons**: Custom server maintenance, two API formats in one server

### Step 4: Install Whisper STT

```bash
voicemode service install whisper
voicemode service enable whisper
voicemode service start whisper
```

- **Verify**: `systemctl --user status whisper` → active
- **Verify**: `curl http://127.0.0.1:2022/v1/models` responds

### Step 5: Configure VoiceMode

Create `~/.voicemode/voicemode.env`:

```bash
# Fully local — no cloud APIs
export VOICEMODE_TTS_BASE_URLS=http://127.0.0.1:8880/v1
export VOICEMODE_STT_BASE_URLS=http://127.0.0.1:2022/v1
export VOICEMODE_VOICES=af_sky
export VOICEMODE_TTS_SPEED=1.0
export VOICEMODE_VAD_AGGRESSIVENESS=3
```

### Step 6: Register MCP with Claude Code

```bash
claude mcp add --scope user voicemode -- uvx --refresh voice-mode
```

- **Verify**: `grep voicemode ~/.claude.json`

### Step 7: Add Permissions

Add to `~/.claude/settings.json` permissions.allow array:

```json
"mcp__voicemode__converse",
"mcp__voicemode__service"
```

### Step 8: Test VoiceMode

1. Restart Claude Code (new session to pick up MCP server)
2. Verify: `claude mcp list` shows `voicemode`
3. Test voice conversation via `mcp__voicemode__converse`
4. Test TTS quality (should be Kokoro GPU, natural voice)
5. Test STT quality (Whisper, accurate transcription)
6. Test silence detection (VAD, no phantom triggers)

### Step 9: Migrate from Piper Stop Hook

Once VoiceMode is confirmed working:

1. Edit `~/.claude/settings.json` — remove `tts-response.sh` from Stop hook array
2. Keep the completion chime (`paplay`) in the Stop hook
3. Keep `~/.claude/hooks/tts-response.sh` on disk as fallback
4. Test: Claude response → chime plays, no Piper speech

### Step 10: Update speak-selection (if Option A)

If the custom Kokoro server was replaced:

1. Edit `~/.local/bin/speak-selection`:
   - Change API call from `/tts` → `/v1/audio/speech`
   - Adjust request format (JSON body) and response handling (audio format)
2. Test: Select text → Ctrl+Alt+S → speech plays

### Step 11: Document & Commit

1. Update `stage_3_10_current_product/outputs/agentic_tts_current_product.md` to reflect VoiceMode
2. Git add all changed files
3. `git commit -m "[AI Context] Implement VoiceMode MCP for Claude Code TTS"`
4. `git push`

<!-- section_id: "03-verification" -->
## 3. Verification Checklist

| # | Check | Command / Action |
|---|-------|-----------------|
| 1 | Kokoro TTS service running | `systemctl --user status kokoro` (or `kokoro-tts`) |
| 2 | Whisper STT service running | `systemctl --user status whisper` |
| 3 | VoiceMode MCP registered | `claude mcp list` shows `voicemode` |
| 4 | Voice conversation works | Test `converse` tool in Claude Code |
| 5 | TTS quality acceptable | Listen for natural Kokoro voice |
| 6 | STT accuracy acceptable | Speak clearly, check transcription |
| 7 | speak-selection works | Select text → Ctrl+Alt+S |
| 8 | Completion chime works | Claude response → chime plays |
| 9 | Piper hook disabled | No Piper speech after Claude response |
| 10 | No cloud APIs | Confirm no OpenAI key in `~/.voicemode/voicemode.env` |
| 11 | GPU VRAM reasonable | `nvidia-smi` shows < 2GB for TTS+STT |

<!-- section_id: "04-rollback" -->
## 4. Rollback Plan

If VoiceMode doesn't work or causes issues:

1. Remove MCP: `claude mcp remove voicemode`
2. Remove permissions from `~/.claude/settings.json`
3. Re-enable Piper hook in Stop hook array
4. If custom Kokoro was stopped: `systemctl --user start kokoro-tts`
5. Verify speak-selection still works with original Kokoro

Everything is reversible. The Piper hook and custom Kokoro server remain on disk.

<!-- section_id: "05-files" -->
## 5. Files to Create / Modify

| File | Action | Step |
|------|--------|------|
| `~/.voicemode/voicemode.env` | Create | 5 |
| `~/.claude/settings.json` | Edit (permissions + hook removal) | 7, 9 |
| `~/.claude.json` | Auto-modified by `claude mcp add` | 6 |
| `~/.local/bin/speak-selection` | Edit (if API changes) | 10 |
| `stage_3_10_current_product/outputs/agentic_tts_current_product.md` | Update | 11 |

<!-- section_id: "06-traceability" -->
## 6. Traceability

| Requirement | Step(s) | Verification |
|-------------|---------|-------------|
| REQ-1: Auto-speak responses | 8 (VoiceMode converse) | Check #4 |
| REQ-6: Offline | 5 (no API keys) | Check #10 |
| REQ-7: GPU-accelerated TTS | 3 (Kokoro GPU) | Check #11 |
| REQ-8: Local STT | 4 (Whisper install) | Check #2, #6 |
| REQ-10: Bidirectional voice | 8 (converse tool) | Check #4 |
| REQ-11: Auto-start services | 3, 4 (systemd enable) | Check #1, #2 |
| REQ-13: Coexist with system TTS | 10 (speak-selection) | Check #7 |
| REQ-14: MCP integration | 6, 7 (MCP add + perms) | Check #3 |
| REQ-15: Completion chime | 9 (keep in Stop hook) | Check #8 |
| REQ-16: Graceful migration | 9 (disable, don't delete) | Check #9 |
