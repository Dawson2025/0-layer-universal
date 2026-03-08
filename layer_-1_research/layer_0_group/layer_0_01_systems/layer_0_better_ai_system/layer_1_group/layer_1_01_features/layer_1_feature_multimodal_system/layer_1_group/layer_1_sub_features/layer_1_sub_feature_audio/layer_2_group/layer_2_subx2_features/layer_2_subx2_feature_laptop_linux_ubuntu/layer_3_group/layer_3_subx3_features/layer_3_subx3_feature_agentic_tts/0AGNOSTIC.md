---
resource_id: "7d564027-e3f0-4cc8-99fa-493fef25d6fd"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_3_subx3_feature_agentic_tts

<!-- section_id: "d566ed29-f9b8-4ff2-946d-7e7e308a88d0" -->
## Identity

entity_id: "027d94d7-1b15-4950-977a-d2f30f8772fa"

You are an agent at **Layer 3** (Sub-Feature), **Sub-Feature**: Agentic TTS.
- **Role**: Claude Code agentic text-to-speech — hooks, MCP plugins, split-output patterns
- **Scope**: AI-driven speech for CLI tools, PostToolUse hooks, spoken summary extraction
- **Parent**: `../../../0AGNOSTIC.md` (layer_2_subx2_feature_laptop_linux_ubuntu)
- **Children**: `layer_4_group/layer_4_subx4_features/` contains 1 sub-feature (mobile_agentic_tts)

<!-- section_id: "6d5a3368-9ea5-43e7-9122-d268500bc90a" -->
## Triggers
Load this context when:
- User mentions: Claude Code TTS, agentic TTS, speech hooks, Kokoro hook, MCP TTS, spoken summary
- Working on: Claude Code speech integration, hook-based TTS, split visual/spoken output
- Entering: `layer_3_subx3_feature_agentic_tts/`

<!-- section_id: "cb33c4c7-a7c6-4d46-9934-8d982fae79bc" -->
## Pointers
<!-- section_id: "7f8b6f84-cd79-4b3b-9b89-37a29d6b71e4" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_3_group/layer_3_99_stages/` for stage progress
3. Read parent for platform context: `../../../0AGNOSTIC.md`

<!-- section_id: "c9664430-2a81-45b8-93fe-6aa64994d11c" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Sibling (System TTS) | `../layer_3_subx3_feature_system_tts/` |
| Stages | `layer_3_group/layer_3_99_stages/` |
| Mobile Agentic TTS | `layer_4_group/layer_4_subx4_features/layer_4_subx4_feature_mobile_agentic_tts/` |
| Platform parent | `../../../0AGNOSTIC.md` (has hardware specs, platform deps) |
| Audio research | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/` |

<!-- section_id: "716d4136-92f3-435e-8c98-65c521fd57bc" -->
## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

<!-- section_id: "429499c8-f661-4838-8022-a3add5753b8b" -->
## Resources Available

<!-- section_id: "83c92ddd-d637-45ce-9a8e-90bf6603f83f" -->
### Key References
- Audio architecture: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`
- Audio design: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/outputs/audio_system_design.md`
- TTS research: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`

<!-- section_id: "a8ed15d4-2da2-43c8-a9d5-74289593a585" -->
### Key Components
- **VoiceMode** (target): MCP server managing local Kokoro + Whisper, Claude Code plugin — see parent knowledge at `../../../.0agnostic/01_knowledge/gpu_tts/`
- **Kokoro hook** (sourcehut): Claude Code hook using local Kokoro TTS model
- **MCP TTS plugin** (GitHub): Exposes TTS as MCP tool for Claude Code
- **PostToolUse hook**: Claude Code event that fires after responses — attach TTS here
- **Split-output pattern**: `spoken_summary` (short, conversational) vs `visual_output` (full text, code, diagrams)
- **pyttsx3**: Python TTS wrapper for offline eSpeak/Festival integration

<!-- section_id: "c5c9ed02-51e8-423f-9cbc-109573c0b7c0" -->
### Community Projects
- [claude-code-tts (sourcehut)](https://git.sr.ht/~cg/claude-code-tts) — Hook-based TTS
- [claude-code-tts (GitHub)](https://github.com/ybouhjira/claude-code-tts) — MCP plugin
- [Local Voice Pipeline for Claude Code](https://crunchtools.com/local-voice-pipeline-claude-code-rhel10-intel-gpu/) — Full setup guide

<!-- section_id: "16543355-2fdf-430a-9fa7-43305661e9df" -->
### Platform Dependencies
Platform-specific details (hardware specs, Ubuntu/GNOME configuration, audio stack, gsd-* daemons) are documented in the parent entity: `../../../0AGNOSTIC.md`
