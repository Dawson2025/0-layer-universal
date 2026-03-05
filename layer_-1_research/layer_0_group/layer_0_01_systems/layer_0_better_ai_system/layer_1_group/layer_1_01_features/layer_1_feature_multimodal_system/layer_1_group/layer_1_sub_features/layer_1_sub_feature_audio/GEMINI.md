<!-- derived_from: "1bcfc63a-46b2-4d46-9b1e-ad1da3ed2607" -->
# Gemini Context

## Identity
You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Audio.
- **Role**: Audio capabilities research — text-to-speech (TTS), speech synthesis, audio I/O for the AI system
- **Scope**: Platform-agnostic TTS research, speech output workflows, audio modality research. Platform-specific implementations live in children.
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_multimodal_system)
- **Children**: `layer_2_group/layer_2_subx2_features/` contains 1 platform entity (laptop_linux_ubuntu)

## Triggers
Load this context when:
- User mentions: audio, TTS, text-to-speech, speech synthesis, voice output
- Working on: Audio integration, TTS pipelines, speech output for CLI or desktop
- Entering: `layer_1_sub_feature_audio/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_1_group/layer_1_99_stages/` for stage progress

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| Laptop Linux Ubuntu | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Platform-agnostic research | Appropriate stage `outputs/` directory |
| Platform-specific work | Navigate to child entity (laptop_linux_ubuntu) |
| Session notes | `.0agnostic/04_episodic_memory/` |

## Resources Available

### Knowledge
| Topic | Location | Description |
|-------|----------|-------------|
| TTS Research | `.0agnostic/01_knowledge/` | TTS options, tools, integration patterns (platform-agnostic) |

### Key References
- Perplexity extraction (TTS research): `layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`
- TTS engines (general): Kokoro, Piper, eSpeak NG, Coqui, OpenAI TTS API
- Claude Code TTS patterns: Hooks (PostToolUse/Stop), MCP plugins, split-output (spoken_summary)
- Platform implementations: See child entity `layer_2_subx2_feature_laptop_linux_ubuntu/`

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
