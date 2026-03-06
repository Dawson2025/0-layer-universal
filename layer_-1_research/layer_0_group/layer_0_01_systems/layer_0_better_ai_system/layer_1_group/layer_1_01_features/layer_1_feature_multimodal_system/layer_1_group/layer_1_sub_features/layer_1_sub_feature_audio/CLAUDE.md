# Claude Code Context

---
resource_id: "c42d8cf4-12a5-4421-878a-93a60ae29392"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_1_sub_feature_audio

<!-- section_id: "a8eed417-e247-4d2d-ab65-e79d403c8ae9" -->
## Identity

entity_id: "1bcfc63a-46b2-4d46-9b1e-ad1da3ed2607"

You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Audio.
- **Role**: Audio capabilities research — text-to-speech (TTS), speech synthesis, audio I/O for the AI system
- **Scope**: Platform-agnostic TTS research, speech output workflows, audio modality research. Platform-specific implementations live in children.
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_multimodal_system)
- **Children**: `layer_2_group/layer_2_subx2_features/` contains 1 platform entity (laptop_linux_ubuntu)

<!-- section_id: "819a8558-1b26-4aca-b3cb-1ac21c89740e" -->
## Triggers
Load this context when:
- User mentions: audio, TTS, text-to-speech, speech synthesis, voice output
- Working on: Audio integration, TTS pipelines, speech output for CLI or desktop
- Entering: `layer_1_sub_feature_audio/`

<!-- section_id: "d556e4ab-2b29-4367-843e-8a1748f10a0a" -->
## Pointers
<!-- section_id: "6e9bfa2e-3bc0-477d-9830-f059a995d537" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_1_group/layer_1_99_stages/` for stage progress

<!-- section_id: "7fad7b89-ab90-4258-8b05-f463485a2e08" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| Laptop Linux Ubuntu | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/` |

<!-- section_id: "c5c744c4-c339-4141-b4bf-d127b246f3e9" -->
## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Platform-agnostic research | Appropriate stage `outputs/` directory |
| Platform-specific work | Navigate to child entity (laptop_linux_ubuntu) |
| Session notes | `.0agnostic/04_episodic_memory/` |

<!-- section_id: "7166c5c1-8bd9-4a5a-b834-8020823b6708" -->
## Resources Available

<!-- section_id: "f3d9877b-3e11-42d5-8837-fdc6ace618ad" -->
### Knowledge
| Topic | Location | Description |
|-------|----------|-------------|
| TTS Research | `.0agnostic/01_knowledge/` | TTS options, tools, integration patterns (platform-agnostic) |

<!-- section_id: "44aaa017-95cb-4231-b85c-6b34fcd55615" -->
### Key References
- Perplexity extraction (TTS research): `layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`
- TTS engines (general): Kokoro, Piper, eSpeak NG, Coqui, OpenAI TTS API
- Claude Code TTS patterns: Hooks (PostToolUse/Stop), MCP plugins, split-output (spoken_summary)
- Platform implementations: See child entity `layer_2_subx2_feature_laptop_linux_ubuntu/`

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

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
