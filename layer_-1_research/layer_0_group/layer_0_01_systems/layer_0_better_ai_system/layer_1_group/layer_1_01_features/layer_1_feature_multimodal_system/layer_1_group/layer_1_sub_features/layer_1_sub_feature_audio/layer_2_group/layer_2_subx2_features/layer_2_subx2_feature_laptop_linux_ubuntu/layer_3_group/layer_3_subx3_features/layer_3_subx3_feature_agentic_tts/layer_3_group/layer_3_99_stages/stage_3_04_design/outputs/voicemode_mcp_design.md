---
resource_id: "d4a5b6c7-e8f9-4a0b-1c2d-3e4f5a6b7c8d"
resource_type: "output"
resource_name: "voicemode_mcp_design"
---
# VoiceMode MCP Design — Claude Code CLI Integration

**Date**: 2026-03-07
**Status**: Design phase
**Traces to**: `stage_3_01_request_gathering/outputs/agentic_tts_requirements.md` (Req 1-6)
**Research basis**: `stage_3_02_research/outputs/agentic_tts_research.md` (VoiceMode MCP section)
**Replaces**: `agentic_tts_design.md` (Piper Stop hook — becomes legacy)

---

<!-- section_id: "01-system-overview" -->
## 1. System Overview

VoiceMode is an MCP server that gives Claude Code bidirectional voice conversation:
- **TTS**: Claude's responses spoken aloud via local Kokoro (GPU-accelerated)
- **STT**: User speaks into microphone, Whisper.cpp transcribes to text
- **MCP protocol**: Claude Code calls VoiceMode tools (`converse`, `service`) natively

This replaces the current Piper-based Stop hook with a richer, GPU-accelerated, conversational voice system.

<!-- section_id: "02-architecture" -->
## 2. Architecture

### Current State (Piper Stop Hook)

```
Claude Code finishes → Stop event → tts-response.sh
                                        │
                                        ├─ jq: extract last_assistant_message
                                        ├─ sed: strip markdown
                                        ├─ cut: truncate 600 chars
                                        └─ piper (CPU) → aplay (background)
```

**Limitations**: One-directional (TTS only), CPU-based (Piper), crude text processing, 600-char truncation, no voice input.

### Target State (VoiceMode MCP)

```
                    ┌──────────────────────────────────┐
                    │      Claude Code CLI              │
                    │                                    │
                    │  ┌────────────────────────────┐   │
                    │  │ VoiceMode MCP Server        │   │
                    │  │ (uvx voice-mode)            │   │
                    │  │                              │   │
                    │  │  Tools:                      │   │
                    │  │   • converse (voice chat)    │   │
                    │  │   • service (manage engines) │   │
                    │  └────────┬──────────┬──────────┘   │
                    └───────────┼──────────┼──────────────┘
                                │          │
                    ┌───────────▼──┐  ┌────▼────────────┐
                    │ Kokoro TTS   │  │ Whisper STT      │
                    │ (systemd)    │  │ (systemd)        │
                    │ Port 8880    │  │ Port 2022        │
                    │ GPU (RTX4060)│  │ CPU/GPU          │
                    └──────┬───────┘  └───────┬──────────┘
                           │                  │
                    ┌──────▼──────┐    ┌──────▼──────┐
                    │ PipeWire    │    │ Microphone   │
                    │ → Speakers  │    │ (PipeWire)   │
                    └─────────────┘    └──────────────┘
```

### What Changes

| Component | Current | Target | Action |
|-----------|---------|--------|--------|
| TTS engine | Piper (CPU, Amy voice) | Kokoro (GPU, af_sky voice) | Replace |
| STT engine | None | Whisper.cpp (local) | Add new |
| Integration | Stop hook (bash script) | MCP server (native) | Replace |
| Text processing | sed/jq in bash | VoiceMode handles internally | Remove |
| Voice conversation | Not possible | Bidirectional via `converse` | Add new |
| Service management | Manual | `voicemode service` commands | Add new |

### What Stays

| Component | Reason |
|-----------|--------|
| Completion chime (paplay) | Independent of TTS — keep in Stop hook |
| System TTS (speak-selection) | Separate entity (system_tts) — unaffected |
| PipeWire audio stack | Underlying audio — unchanged |
| Piper binary at ~/.local/bin/piper | Keep as fallback; system TTS still uses it |

<!-- section_id: "03-prerequisites" -->
## 3. Prerequisites

### Already Satisfied

| Requirement | Status | Evidence |
|-------------|--------|----------|
| NVIDIA GPU with CUDA | ✅ | RTX 4060, 8GB VRAM, driver 580.126.09 |
| PipeWire audio | ✅ | Running (PipeWire → ALSA/SOF → hardware) |
| ffmpeg | ✅ | Installed via apt |
| Python 3 + pip | ✅ | System Python available |
| Claude Code CLI | ✅ | Installed and configured |

### Need to Install

| Requirement | Command | Notes |
|-------------|---------|-------|
| System audio dev libs | `sudo apt install -y gcc libasound2-dev libasound2-plugins libportaudio2 portaudio19-dev python3-dev` | Some may already be present |
| PulseAudio utils | `sudo apt install -y pulseaudio pulseaudio-utils` | PipeWire provides PA compat layer — may need explicitly |
| uv package manager | Already installed (used for uvx) | Verify with `which uvx` |

<!-- section_id: "04-installation-sequence" -->
## 4. Installation Sequence

### Phase 1: System Dependencies

```bash
# Install audio development libraries
sudo apt install -y gcc libasound2-dev libasound2-plugins \
    libportaudio2 portaudio19-dev pulseaudio pulseaudio-utils python3-dev
```

### Phase 2: VoiceMode Installation

```bash
# Install VoiceMode via uvx
uvx voice-mode-install
```

This creates `~/.voicemode/` directory and installs the voicemode CLI.

### Phase 3: Local TTS Service (Kokoro)

```bash
# Install Kokoro as systemd user service
voicemode service install kokoro

# Enable auto-start on login
voicemode service enable kokoro

# Start now
voicemode service start kokoro
```

Kokoro runs as `kokoro.service` under systemd user scope on port 8880. Uses GPU automatically when CUDA is available.

### Phase 4: Local STT Service (Whisper)

```bash
# Install Whisper.cpp as systemd user service
voicemode service install whisper

# Enable auto-start on login
voicemode service enable whisper

# Start now
voicemode service start whisper
```

Whisper runs as `whisper.service` under systemd user scope on port 2022.

### Phase 5: Claude Code MCP Registration

```bash
# Register VoiceMode as MCP server (user scope = all projects)
claude mcp add --scope user voicemode -- uvx --refresh voice-mode
```

This adds the MCP server entry to `~/.claude.json`.

### Phase 6: Permissions

Add VoiceMode tool permissions to `~/.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "mcp__voicemode__converse",
      "mcp__voicemode__service"
    ]
  }
}
```

<!-- section_id: "05-configuration" -->
## 5. Configuration

### VoiceMode Environment (`~/.voicemode/voicemode.env`)

```bash
# === Local-only configuration (no cloud APIs) ===

# TTS: Point to local Kokoro GPU service
export VOICEMODE_TTS_BASE_URLS=http://127.0.0.1:8880/v1

# STT: Point to local Whisper service
export VOICEMODE_STT_BASE_URLS=http://127.0.0.1:2022/v1

# Voice selection (Kokoro voices)
export VOICEMODE_VOICES=af_sky

# Speech speed (1.0 = normal, range 0.25-4.0)
export VOICEMODE_TTS_SPEED=1.0

# Voice activity detection sensitivity (0-3, higher = more aggressive)
export VOICEMODE_VAD_AGGRESSIVENESS=3

# Kokoro service port (default)
export VOICEMODE_KOKORO_PORT=8880
```

### Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| No OpenAI API key | Local only | Privacy-focused, no cloud dependency, no cost |
| Voice: af_sky | Kokoro default | Natural-sounding, well-tested with Kokoro |
| VAD aggressiveness: 3 | Maximum | Prevent background noise from triggering STT |
| TTS speed: 1.0 | Normal | Adjustable per preference later |

<!-- section_id: "06-migration-plan" -->
## 6. Migration Plan

### Step 1: Install VoiceMode (Phases 1-6 above)

Keep the current Piper hook active during installation. Both can coexist temporarily.

### Step 2: Verify VoiceMode Works

```bash
# Check services are running
systemctl --user status kokoro
systemctl --user status whisper

# Test VoiceMode from Claude Code
# In Claude Code: use /voicemode:converse to test voice
```

### Step 3: Disable Piper Stop Hook

Once VoiceMode is confirmed working, remove the TTS hook from `~/.claude/settings.json`:

**Before** (current Stop hook array):
```json
{
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [
        {"type": "command", "command": "paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || aplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || true"},
        {"type": "command", "command": "/home/dawson/.claude/hooks/tts-response.sh", "timeout": 60}
      ]
    }]
  }
}
```

**After** (keep only the completion chime):
```json
{
  "hooks": {
    "Stop": [{
      "matcher": "",
      "hooks": [
        {"type": "command", "command": "paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || aplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || true"}
      ]
    }]
  }
}
```

The `tts-response.sh` script stays on disk as fallback but is not triggered.

### Step 4: Archive Piper Hook Design

Move `agentic_tts_design.md` (Piper architecture) to `stage_3_11_archives/` — it becomes historical reference.

<!-- section_id: "07-voicemode-usage" -->
## 7. Usage Patterns

### Voice Conversation Mode

```
# In Claude Code CLI
> /voicemode:converse
# Hold spacebar to speak, release to send
# Claude responds with voice (Kokoro TTS)
# Say "stop" or press Escape to exit voice mode
```

### Service Management

```bash
# Check service status
voicemode service status kokoro
voicemode service status whisper

# Restart if needed
voicemode service restart kokoro

# View logs
journalctl --user -u kokoro -f
journalctl --user -u whisper -f
```

### Coexistence with Claude Code /voice

Claude Code's native `/voice` command (rolling out) is **STT-only** — it transcribes your speech to text input. VoiceMode provides **full bidirectional** voice (STT + TTS). They complement each other:

| Feature | Claude /voice | VoiceMode |
|---------|--------------|-----------|
| Speech-to-text input | ✅ | ✅ |
| Text-to-speech output | ❌ | ✅ |
| Local processing | Unknown | ✅ (Kokoro + Whisper) |
| GPU acceleration | Unknown | ✅ (Kokoro on RTX 4060) |

<!-- section_id: "08-resource-usage" -->
## 8. Resource Usage Estimates

| Resource | Kokoro TTS | Whisper STT | Total |
|----------|-----------|-------------|-------|
| VRAM | ~300 MB | ~500 MB | ~800 MB / 8192 MB |
| RAM | ~200 MB | ~300 MB | ~500 MB |
| GPU utilization | Burst (during synthesis) | Burst (during transcription) | Low average |
| Disk | ~500 MB (model) | ~1 GB (model) | ~1.5 GB |
| Network | None (local) | None (local) | Zero |

The RTX 4060's 8GB VRAM comfortably accommodates both services simultaneously, with ~7GB free for other GPU tasks.

<!-- section_id: "09-error-handling" -->
## 9. Error Handling & Fallbacks

| Failure Mode | Detection | Fallback |
|-------------|-----------|----------|
| Kokoro service down | VoiceMode auto-detects | Re-enable Piper Stop hook temporarily |
| Whisper service down | VoiceMode auto-detects | Text input still works normally |
| GPU driver crash | systemd restart policy | Services auto-restart; manual nvidia-smi check |
| PipeWire audio failure | No audio output | `systemctl --user restart pipewire` |
| VoiceMode MCP disconnected | Claude Code shows MCP error | `claude mcp` to check status, restart |

### Monitoring Commands

```bash
# Quick health check
voicemode service status kokoro && voicemode service status whisper

# GPU status
nvidia-smi --query-gpu=memory.used,memory.total,gpu-util --format=csv

# Audio pipeline
pw-cli list-objects | grep -i node
```

<!-- section_id: "10-future-enhancements" -->
## 10. Future Enhancements (Out of Scope)

These are documented for future design iterations but NOT part of this implementation:

1. **Split-output pattern** — Claude emits `spoken_summary` + `visual_output` (requires Claude model cooperation)
2. **Multiple hook events** — Add PostToolUse, SubagentStop, Notification TTS hooks
3. **Voice selection UI** — Switch Kokoro voices dynamically
4. **Kokoro prosody improvements** — Phrase-level chunking, simple markup for emphasis
5. **Speechify API integration** — High-quality cloud TTS for long reading sessions
6. **Hybrid architecture** — Voice shell + brain + router pattern (from research)

<!-- section_id: "11-acceptance-criteria" -->
## 11. Acceptance Criteria

Traces to: `stage_3_01_request_gathering/outputs/agentic_tts_requirements.md`

| Req ID | Requirement | How VoiceMode Satisfies |
|--------|-------------|------------------------|
| 1 | Auto-speak Claude responses | VoiceMode TTS speaks responses via MCP `converse` tool |
| 2 | Markdown cleanup | VoiceMode handles text processing internally |
| 3 | Length control | VoiceMode manages output length; Kokoro handles streaming |
| 4 | Non-blocking | MCP server runs asynchronously from CLI |
| 5 | Kill switch | VoiceMode handles speech interruption natively |
| 6 | Offline | Fully local — Kokoro (GPU) + Whisper (local), no cloud APIs |

### New Capabilities Beyond Original Requirements

| Capability | Description |
|-----------|-------------|
| Voice input (STT) | Speak to Claude instead of typing |
| GPU-accelerated TTS | Sub-0.1s latency vs Piper's ~1-2s |
| Natural voice quality | Kokoro top of HuggingFace TTS Arena vs Piper baseline |
| Service management | systemd auto-start, restart, logging |
| Bidirectional conversation | Full voice chat flow |

<!-- section_id: "12-traceability" -->
## 12. Traceability Matrix

| Stage | Document | Connection |
|-------|----------|------------|
| 01 Request Gathering | `agentic_tts_requirements.md` | Core requirements 1-6 → Section 11 acceptance criteria |
| 02 Research | `agentic_tts_research.md` | VoiceMode MCP section → Section 2 architecture |
| 02 Research | `agentic_tts_research.md` | TTS Engine Tier List → Section 5 voice selection |
| 02 Research | `agentic_tts_research.md` | Kokoro prosody → Section 10 future enhancements |
| 04 Design | `agentic_tts_design.md` | Piper architecture → Section 6 migration (legacy) |
| 04 Design | THIS DOCUMENT | VoiceMode MCP target architecture |
| Knowledge | `gpu_tts/docs/voicemode_mcp.md` | Installation commands → Section 4 |

## Sources

- [VoiceMode GitHub](https://github.com/mbailey/voicemode)
- [VoiceMode Documentation](https://voice-mode.readthedocs.io)
- [Kokoro TTS](https://kokorottsai.com)
- [Whisper.cpp](https://github.com/ggerganov/whisper.cpp)
- Knowledge doc: `../../.0agnostic/01_knowledge/gpu_tts/docs/voicemode_mcp.md`
