---
resource_id: "37f33c76-68b0-4755-9bac-fe804c403b14"
resource_type: "output"
resource_name: "audio_plan"
---
# Audio Implementation Plan (Parent Overview)

**Date**: 2026-02-23

<!-- section_id: "febc6167-dc9b-4111-a9e7-0086604c9ffd" -->
## Overall Plan

| Phase | Description | Status |
|-------|-------------|--------|
| 1. Engine Setup | Install Piper, download voice model | Done |
| 2. System TTS | Scripts, hotkey, testing | Done (MVP) |
| 3. Agentic TTS | Stop hook, markdown cleanup, testing | Done (MVP) |
| 4. Polish | Additional voices, Wayland support, PostToolUse hook | Pending |

<!-- section_id: "0dc2c300-b0fa-44c9-a86b-9eed164bbe29" -->
## Children — Detailed Plans

<!-- section_id: "cfee664c-bd92-475e-92ce-669c1d78a6f3" -->
### System TTS Plan (Summary)
- 8 of 13 steps completed: installed Piper, fixed pathvalidate, downloaded Amy voice, created scripts, tested
- Remaining: GNOME hotkey config, additional voices, Speech Dispatcher Piper module, Wayland support
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_05_planning/outputs/system_tts_plan.md`

<!-- section_id: "e8b00ab5-92d3-4a3e-9d06-ae630bdfefa4" -->
### Agentic TTS Plan (Summary)
- 8 of 14 steps completed: researched hooks API, created hook script, tested with simulated input
- Remaining: live test, tune truncation, PostToolUse hook, split-output pattern, SubagentStop hook
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_05_planning/outputs/agentic_tts_plan.md`
