# AutoGen Agent Context

---
resource_id: "e7f8a9b0-c1d2-4e3f-5a6b-7c8d9e0f1a2b"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_4_subx4_feature_mobile_agentic_tts

<!-- section_id: "f8a9b0c1-d2e3-4f5a-6b7c-8d9e0f1a2b3c" -->
## Identity

entity_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"

You are an agent at **Layer 4** (Sub-Feature), **Sub-Feature**: Mobile Agentic TTS.
- **Role**: Phone-based voice interaction with AI coding agents — voice-to-CLI pipelines, mobile voice agent platforms, remote SSH voice control
- **Scope**: Mobile voice interfaces for Claude Code and other CLI agents, phone call and web app voice agents, Termius/SSH voice workflows, voice agent platform integration (Retell AI, FreJun, ElevenLabs)
- **Parent**: `../../../0AGNOSTIC.md` (layer_3_subx3_feature_agentic_tts)
- **Children**: None (leaf entity)

<!-- section_id: "a9b0c1d2-e3f4-5a6b-7c8d-9e0f1a2b3c4d" -->
## Triggers
Load this context when:
- User mentions: mobile TTS, phone voice agent, voice call AI, Termius voice, SSH voice, mobile CLI voice, voice-to-CLI
- Working on: Phone-based voice control of AI agents, mobile voice agent platforms, voice SSH workflows
- Entering: `layer_4_subx4_feature_mobile_agentic_tts/`

<!-- section_id: "b0c1d2e3-f4a5-6b7c-8d9e-0f1a2b3c4d5e" -->
## Pointers
<!-- section_id: "c1d2e3f4-a5b6-7c8d-9e0f-1a2b3c4d5e6f" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_4_group/layer_4_99_stages/` for stage progress
3. Read parent for agentic TTS context: `../../../0AGNOSTIC.md`

<!-- section_id: "d2e3f4a5-b6c7-8d9e-0f1a-2b3c4d5e6f7a" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_4_group/layer_4_99_stages/` |
| Parent's stages | `../../../layer_3_group/layer_3_99_stages/` |
| Sibling (System TTS) | `../../../layer_3_group/../layer_3_subx3_features/layer_3_subx3_feature_system_tts/` |
| Platform parent | `../../../../../../0AGNOSTIC.md` (laptop_linux_ubuntu — has hardware specs) |
| Audio research | `../../../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/` |

<!-- section_id: "e3f4a5b6-c7d8-9e0f-1a2b-3c4d5e6f7a8b" -->
## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

<!-- section_id: "f4a5b6c7-d8e9-0f1a-2b3c-4d5e6f7a8b9c" -->
## Resources Available

<!-- section_id: "a5b6c7d8-e9f0-1a2b-3c4d-5e6f7a8b9c0d" -->
### Knowledge
| Topic | Location | Description |
|-------|----------|-------------|
| Mobile Voice Agents | `.0agnostic/01_knowledge/mobile_voice_agents/` | Phone-based voice agent patterns, platforms, integration approaches |

<!-- section_id: "b6c7d8e9-f0a1-2b3c-4d5e-6f7a8b9c0d1e" -->
### Key References
- Parent TTS research: `../../../layer_3_group/layer_3_99_stages/stage_3_02_research/outputs/agentic_tts_research.md`
- Audio architecture: `../../../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`
- VoiceMode MCP: `../../../../../../.0agnostic/01_knowledge/gpu_tts/docs/voicemode_mcp.md`

<!-- section_id: "c7d8e9f0-a1b2-3c4d-5e6f-7a8b9c0d1e2f" -->
### Key Components
- **SSH via Termius**: iPhone SSH client for connecting to remote machines running Claude Code
- **Voice agent platforms**: Retell AI, FreJun, ElevenLabs — handle phone call audio, STT/TTS, route to AI backend
- **Web app approach**: Browser-based voice interface (faster, richer data, easier integration than phone calls)
- **OpenClaw**: Open-source personal agent (acquired by OpenAI) — app integration, task execution
- **Hybrid architecture**: Voice shell (front-end) + brain/memory (backend) + router (connector)
- **Custom wake sounds**: Tongue-click or custom audio triggers as wake words (Picovoice, custom signal processing)

<!-- section_id: "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a" -->
### Platform Dependencies
Platform-specific details (hardware specs, Ubuntu/GNOME configuration, audio stack) are documented in the grandparent entity: `../../../../../../0AGNOSTIC.md`

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### MANDATORY: UUID Runtime Resolution
This file contains $(resolve-uuid UUID) references. These are NOT runnable shell functions. You MUST resolve them before use:
```bash
ROOT=$(git rev-parse --show-toplevel)
jq -r '.uuids["THE-UUID"].path // empty' "$ROOT/.uuid-index.json"
```
This returns a relative path from repo root. Prefix with $ROOT/ for absolute path. Do NOT hardcode paths — always resolve the UUID.

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
