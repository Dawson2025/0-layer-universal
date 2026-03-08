---
resource_id: "3e3169c4-ec21-4e4e-add4-95a5c6429a66"
resource_type: "output"
resource_name: "agentic_tts_requirements"
---
# Agentic TTS Requirements

**Date**: 2026-02-23 (initial), 2026-03-07 (updated)

---

<!-- section_id: "a1b2c3d4-tree-of-needs" -->
## Tree of Needs

```
GOAL: Voice interaction with Claude Code CLI on Ubuntu laptop
├── NEED-1: Claude speaks its responses aloud (TTS output)
│   ├── REQ-1: Auto-speak Claude responses [CORE]
│   ├── REQ-2: Markdown cleanup — strip code, URLs, paths, tables [CORE]
│   ├── REQ-3: Length control — summarize/truncate for speech [CORE]
│   ├── REQ-6: Offline — no cloud API dependency [CORE]
│   └── REQ-7: GPU-accelerated TTS — sub-0.1s latency [UPGRADE]
│       └── RESEARCH → TTS Engine Tier List (Kokoro > Piper)
│
├── NEED-2: Speech does not block CLI interaction
│   ├── REQ-4: Non-blocking — speech runs in background [CORE]
│   └── REQ-5: Kill switch — new speech replaces old [CORE]
│
├── NEED-3: User speaks to Claude (STT input) [NEW]
│   ├── REQ-8: Local speech-to-text via Whisper.cpp [NEW]
│   ├── REQ-9: Smart silence detection (VAD) [NEW]
│   └── REQ-10: Bidirectional voice conversation mode [NEW]
│       └── RESEARCH → VoiceMode MCP, Claude /voice command
│
├── NEED-4: Service reliability & management
│   ├── REQ-11: Auto-start TTS/STT on login (systemd) [NEW]
│   ├── REQ-12: Auto-restart on failure [NEW]
│   └── REQ-13: Coexist with system TTS (speak-selection) [CORE]
│
└── NEED-5: Integration with Claude Code ecosystem
    ├── REQ-14: MCP protocol integration (native Claude tools) [NEW]
    ├── REQ-15: Completion chime preserved [CORE]
    └── REQ-16: Migrate from Piper Stop hook gracefully [UPGRADE]
        └── DESIGN → voicemode_mcp_design.md Section 6
```

### Requirement Classification

| ID | Requirement | Type | Priority | Stage Trace |
|----|-------------|------|----------|-------------|
| REQ-1 | Auto-speak Claude responses | Core | P0 | Design §11, Research §Hook System |
| REQ-2 | Markdown cleanup for speech | Core | P0 | Design §11, Research §Text Cleanup |
| REQ-3 | Length control / truncation | Core | P1 | Design §11 |
| REQ-4 | Non-blocking speech | Core | P0 | Design §11 |
| REQ-5 | Kill switch (no overlap) | Core | P1 | Design §11 |
| REQ-6 | Offline / local only | Core | P0 | Design §5 (no API key), Research §VoiceMode |
| REQ-7 | GPU-accelerated TTS | Upgrade | P1 | Design §8, Research §TTS Tier List |
| REQ-8 | Local STT via Whisper | New | P1 | Design §4 Phase 4, Research §VoiceMode |
| REQ-9 | Smart silence detection (VAD) | New | P2 | Design §5 (VAD_AGGRESSIVENESS) |
| REQ-10 | Bidirectional voice conversation | New | P1 | Design §7, Research §Claude /voice |
| REQ-11 | Auto-start services on login | New | P1 | Design §4 Phase 3-4 |
| REQ-12 | Auto-restart on failure | New | P2 | Design §9 |
| REQ-13 | Coexist with system TTS | Core | P1 | Design §2 (What Stays) |
| REQ-14 | MCP protocol integration | New | P0 | Design §4 Phase 5-6 |
| REQ-15 | Completion chime preserved | Core | P1 | Design §6 Step 3 |
| REQ-16 | Migrate from Piper gracefully | Upgrade | P1 | Design §6 (Migration Plan) |

---

<!-- section_id: "db933a0f-4803-4c0e-8d4c-134bd3a60542" -->
## Core Requirements (Original — v1 Piper)

1. **Auto-speak Claude responses** (REQ-1): When Claude finishes responding, automatically speak a summary
2. **Markdown cleanup** (REQ-2): Strip code blocks, URLs, file paths, tables before speaking
3. **Length control** (REQ-3): Truncate long responses to a spoken summary (~600 chars)
4. **Non-blocking** (REQ-4): Speech runs in background — Claude remains interactive
5. **Kill switch** (REQ-5): New speech replaces old (no overlapping speech)
6. **Offline** (REQ-6): Uses local TTS, no cloud APIs

## Upgrade Requirements (v2 VoiceMode MCP)

7. **GPU-accelerated TTS** (REQ-7): Kokoro on RTX 4060 — sub-0.1s latency, natural voice quality
8. **Local STT** (REQ-8): Whisper.cpp for offline speech-to-text input
9. **Smart silence detection** (REQ-9): VAD prevents background noise from triggering STT
10. **Bidirectional voice conversation** (REQ-10): Full voice chat with Claude Code
11. **Auto-start services** (REQ-11): Kokoro + Whisper start automatically on login via systemd
12. **Auto-restart on failure** (REQ-12): systemd restart policy for crashed services
13. **Coexist with system TTS** (REQ-13): VoiceMode does not conflict with speak-selection
14. **MCP protocol integration** (REQ-14): VoiceMode registered as Claude Code MCP server
15. **Completion chime preserved** (REQ-15): Keep existing paplay chime in Stop hook
16. **Graceful migration** (REQ-16): Transition from Piper hook to VoiceMode without downtime

<!-- section_id: "98a4f30c-7068-4218-bdd3-039bc1496420" -->
## User Stories

### Original (v1)
- As a developer, I want Claude to speak its response summary so I can look away from the screen while it works
- As a user, I want long responses truncated to a brief spoken overview
- As a developer, I want to hear a completion sound AND a spoken summary when Claude finishes

### New (v2 VoiceMode)
- As a developer, I want to speak to Claude instead of typing, so I can work hands-free
- As a user, I want high-quality natural voice (not robotic Piper) when Claude speaks
- As a developer, I want TTS/STT services that start automatically and recover from crashes
- As a user, I want voice conversation mode where I speak and Claude responds by voice in real-time

<!-- section_id: "7d0f24d3-80e1-4271-a80e-5b2bb4ffcc86" -->
## Constraints

- ~~Must use Claude Code hooks system (Stop event)~~ → Replaced by MCP protocol
- ~~Hook receives JSON on stdin with `last_assistant_message` field~~ → VoiceMode handles internally
- Must coexist with existing completion sound hook (paplay — kept in Stop hook)
- Must not conflict with system TTS (separate from speak-selection, different entity)
- RTX 4060 GPU (8GB VRAM) — must fit Kokoro + Whisper simultaneously (~800MB VRAM)
- Ubuntu Linux with PipeWire audio stack
- No cloud API keys — fully local operation
- Privacy-focused — no data leaves the machine

<!-- section_id: "6989218b-ae02-4cc1-9abb-c547c7ca3d03" -->
## Acceptance Criteria

### v1 (Piper Stop Hook) — DELIVERED ✅
- [x] Claude's Stop hook triggers TTS of response summary
- [x] Code blocks and markdown are stripped from speech
- [x] Long responses are truncated at word boundary
- [x] Completion sound plays before/alongside TTS
- [x] Can manually kill speech via `kill $(cat /tmp/claude-tts.pid)`

### v2 (VoiceMode MCP) — IN DESIGN
- [ ] VoiceMode MCP server registered with Claude Code (`claude mcp add`)
- [ ] Kokoro TTS running as systemd user service on port 8880
- [ ] Whisper STT running as systemd user service on port 2022
- [ ] `mcp__voicemode__converse` tool available in Claude Code
- [ ] Voice conversation works bidirectionally (speak + hear)
- [ ] GPU-accelerated TTS with sub-0.1s latency
- [ ] Completion chime still plays on Stop event
- [ ] Piper Stop hook disabled (kept as fallback on disk)
- [ ] System TTS (speak-selection) unaffected
- [ ] No cloud API keys configured — fully local

<!-- section_id: "e5f6a7b8-traceability" -->
## Traceability

| Stage | Document | Connection |
|-------|----------|------------|
| 01 Request Gathering | THIS DOCUMENT | Tree of Needs, Requirements, User Stories |
| 02 Research | `agentic_tts_research.md` | Hook system, TTS tier list, VoiceMode MCP, prosody |
| 04 Design | `agentic_tts_design.md` | v1 Piper architecture (legacy) |
| 04 Design | `voicemode_mcp_design.md` | v2 VoiceMode architecture, installation, migration |
| 04 Design | `voicemode_architecture.svg` | Architecture diagram (current → target) |
| 10 Current Product | `agentic_tts_current_product.md` | v1 Piper delivery status |
