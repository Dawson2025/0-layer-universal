# Gemini Context

## Identity
You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: System TTS.
- **Role**: System-wide text-to-speech — Orca screen reader, Piper engine, highlight-and-speak scripts
- **Scope**: Linux/Ubuntu desktop + terminal TTS integration, voice engine setup, GNOME accessibility
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_audio)
- **Children**: None (leaf entity)

## Triggers
Load this context when:
- User mentions: Orca, Piper, system TTS, highlight-and-speak, screen reader, Speech Dispatcher
- Working on: System-wide TTS setup, voice engine installation, GNOME keyboard shortcuts for speech
- Entering: `layer_2_subx2_feature_system_tts/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_2_group/layer_2_99_stages/` for stage progress
3. Read parent overview: `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Sibling (Agentic TTS) | `../layer_2_subx2_feature_agentic_tts/` |
| Stages | `layer_2_group/layer_2_99_stages/` |
| Parent research | `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

## Resources Available

### Key References
- Parent architecture overview: `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`
- Parent design doc: `../../../layer_1_group/layer_1_99_stages/stage_1_04_design/outputs/audio_system_design.md`
- TTS research extraction: `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`

### Key Components
- **Orca**: GNOME screen reader, toggle with `Super+Alt+S`
- **Piper**: Neural TTS engine (offline, natural-sounding)
- **Speech Dispatcher**: Middleware routing text to TTS engines
- **Highlight-and-speak**: Custom script: `xsel | piper | aplay`, bound to GNOME shortcut

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
