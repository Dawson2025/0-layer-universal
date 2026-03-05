---
resource_id: "3c31bd35-b8a8-4d53-90a3-bd6a80fc6aed"
resource_type: "output"
resource_name: "audio_fixes"
---
# Audio Fixes Log (Parent Overview)

**Date**: 2026-02-23

<!-- section_id: "4bb46bbf-bdc6-41c3-b940-cac87ad23ceb" -->
## Cross-Cutting Fixes

<!-- section_id: "83dc21bb-648b-4f25-b03f-6e4aa77a6d53" -->
### Fix 1: Piper pathvalidate Dependency
- **Affects**: Both system TTS and agentic TTS (shared engine)
- **Problem**: Piper 1.4.1 pip package missing pathvalidate dependency
- **Fix**: `pipx inject piper-tts pathvalidate`

<!-- section_id: "753193ef-5f56-4f6f-9834-790d3d05d8d4" -->
## Children — Detailed Fixes

<!-- section_id: "3d9d28d1-4339-4955-a242-62917cec74a1" -->
### System TTS Fixes (Summary)
- Only fix needed: pathvalidate injection (above)
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_09_fixing/outputs/system_tts_fixes.md`

<!-- section_id: "eeb3adbb-9554-449e-b366-704ddc5d87d4" -->
### Agentic TTS Fixes (Summary)
- No fixes required yet — pending live testing
- Anticipated: markdown stripping edge cases, truncation length tuning
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_09_fixing/outputs/agentic_tts_fixes.md`
