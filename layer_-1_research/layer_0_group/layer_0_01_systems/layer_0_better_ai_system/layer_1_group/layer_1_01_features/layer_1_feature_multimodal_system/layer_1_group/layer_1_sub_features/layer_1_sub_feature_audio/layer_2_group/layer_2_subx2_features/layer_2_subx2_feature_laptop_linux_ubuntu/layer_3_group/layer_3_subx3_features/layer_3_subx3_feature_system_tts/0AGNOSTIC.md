---
resource_id: "c40dec3f-7a09-4f6c-981c-8201fe38cda7"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_3_subx3_feature_system_tts

<!-- section_id: "1fc681eb-1565-4f4a-a5c6-c5cc0a62e742" -->
## Identity

entity_id: "7cab7cdd-b645-40d0-8350-3f3ad1a26705"

You are an agent at **Layer 3** (Sub-Feature), **Sub-Feature**: System TTS.
- **Role**: System-wide text-to-speech — highlight-and-speak scripts, desktop TTS integration
- **Scope**: Desktop TTS setup, voice engine configuration, keyboard shortcut integration
- **Parent**: `../../../0AGNOSTIC.md` (layer_2_subx2_feature_laptop_linux_ubuntu)
- **Children**: None (leaf entity)

<!-- section_id: "02c3319c-cc92-4ec1-ab6d-3fe226b68f46" -->
## Triggers
Load this context when:
- User mentions: system TTS, highlight-and-speak, speak-selection, Ctrl+Alt+S, Speech Dispatcher
- Working on: System-wide TTS setup, voice engine installation, keyboard shortcuts for speech
- Entering: `layer_3_subx3_feature_system_tts/`
- Ctrl+Alt+S not working after reboot → traverse to GSD Session Startup entity (see Platform Dependencies below)

<!-- section_id: "349d1f81-c7a9-41dd-9bc3-9e56acb19d0a" -->
## Pointers
<!-- section_id: "82feb39b-c18c-41f9-a804-7695ad0eb6f5" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_3_group/layer_3_99_stages/` for stage progress
3. Read parent for platform context: `../../../0AGNOSTIC.md`

<!-- section_id: "19231c9b-dbf4-49ca-9f99-7018a114393f" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Sibling (Agentic TTS) | `../layer_3_subx3_feature_agentic_tts/` |
| Stages | `layer_3_group/layer_3_99_stages/` |
| Platform parent | `../../../0AGNOSTIC.md` (has hardware specs, platform deps) |
| Audio research | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/` |

<!-- section_id: "9e3e6fa6-cd2a-4270-9ddc-5b21998967ae" -->
## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |

<!-- section_id: "859ed446-2571-46b9-909a-60c84d89baf1" -->
## Resources Available

<!-- section_id: "e359e320-1575-48dd-a66f-121d72c5570c" -->
### Key References
- Audio architecture: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/audio_architecture_overview.md`
- Audio design: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/outputs/audio_system_design.md`
- TTS research: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/perplexity_extraction_2026-02-22_tts-research.md`

<!-- section_id: "e61cdd65-a5df-440e-b328-ab50dc3c2d7f" -->
### Key Components
- **Kokoro** (target): GPU-accelerated neural TTS, 40+ voices — see parent knowledge at `../../../.0agnostic/01_knowledge/gpu_tts/`
- **Piper** (current): Neural TTS engine (offline, CPU), `~/.local/bin/piper`, Amy voice
- **Speech Dispatcher**: Middleware routing text to TTS engines
- **Highlight-and-speak**: `~/.local/bin/speak-selection` (xclip -> TTS -> paplay), bound to Ctrl+Alt+S

<!-- section_id: "71474be6-aaa8-485b-80d1-6060e6671869" -->
### Platform Dependencies
Platform-specific details (hardware specs, Ubuntu/GNOME configuration, audio stack, gsd-* daemons) are documented in the parent entity: `../../../0AGNOSTIC.md`

### GSD Session Startup (Setup Dependency)
The Ctrl+Alt+S keybinding depends on `gsd-media-keys` running. After reboot, Unity's DISPLAY race condition and the systemd user `GDK_BACKEND=wayland` mismatch can keep gsd daemons from starting. The fix is tracked in a dedicated setup entity:

**Entity**: `.0agnostic/07+_setup_dependant/.../sub_layer_0_06_local/sub_layer_0_06_group/setup/gsd_session_startup/`
(from repo root)

Key files:
- Current status and root causes: `0INDEX.md`
- Solution design: `stages/stage_04_design/outputs/cycle_1/chosen_solution.md`
- Current fix: `stages/stage_10_current_product/outputs/current_fix.md`
