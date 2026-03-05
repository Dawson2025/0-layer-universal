<!-- derived_from: "7cab7cdd-b645-40d0-8350-3f3ad1a26705" -->
# OpenAI Context

## Identity
You are an agent at **Layer 3** (Sub-Feature), **Sub-Feature**: System TTS.
- **Role**: System-wide text-to-speech — highlight-and-speak scripts, desktop TTS integration
- **Scope**: Desktop TTS setup, voice engine configuration, keyboard shortcut integration
- **Parent**: `../../../0AGNOSTIC.md` (layer_2_subx2_feature_laptop_linux_ubuntu)
- **Children**: None (leaf entity)

## Triggers
Load this context when:
- User mentions: system TTS, highlight-and-speak, speak-selection, Ctrl+Alt+S, Speech Dispatcher
- Working on: System-wide TTS setup, voice engine installation, keyboard shortcuts for speech
- Entering: `layer_3_subx3_feature_system_tts/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_3_group/layer_3_99_stages/` for stage progress
3. Read parent for platform context: `../../../0AGNOSTIC.md`

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Sibling (Agentic TTS) | `../layer_3_subx3_feature_agentic_tts/` |
| Stages | `layer_3_group/layer_3_99_stages/` |
| Platform parent | `../../../0AGNOSTIC.md` (has hardware specs, platform deps) |
| Audio research | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

## Resources Available

### Key References
- Audio architecture: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`
- Audio design: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/outputs/audio_system_design.md`
- TTS research: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`

### Key Components
- **Kokoro** (target): GPU-accelerated neural TTS, 40+ voices — see parent knowledge at `../../../.0agnostic/01_knowledge/gpu_tts/`
- **Piper** (current): Neural TTS engine (offline, CPU), `~/.local/bin/piper`, Amy voice
- **Speech Dispatcher**: Middleware routing text to TTS engines
- **Highlight-and-speak**: `~/.local/bin/speak-selection` (xclip -> TTS -> paplay), bound to Ctrl+Alt+S

### Platform Dependencies
Platform-specific details (hardware specs, Ubuntu/GNOME configuration, audio stack, gsd-* daemons) are documented in the parent entity: `../../../0AGNOSTIC.md`

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
