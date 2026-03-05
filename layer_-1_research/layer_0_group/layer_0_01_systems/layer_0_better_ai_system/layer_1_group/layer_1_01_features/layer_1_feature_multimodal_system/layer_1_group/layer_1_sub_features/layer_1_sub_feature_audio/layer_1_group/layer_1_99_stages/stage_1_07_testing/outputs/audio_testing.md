---
resource_id: "830d734a-aa12-46ce-a7a9-55c4134b6f81"
resource_type: "output"
resource_name: "audio_testing"
---
# Audio Testing (Parent Overview)

**Date**: 2026-02-23

<!-- section_id: "61fead29-8db1-4107-8df8-8390ea706847" -->
## Overall Test Summary

| Domain | Tests Run | Passing | Pending |
|--------|-----------|---------|---------|
| System TTS | 6 | 6 | 1 (hotkey) |
| Agentic TTS | 4 | 4 | 1 (live test) |

All core functionality verified. Two items pending manual/live testing.

<!-- section_id: "59ce5948-8db1-45eb-9579-c8a0cfdda42b" -->
## Children — Detailed Test Results

<!-- section_id: "b4bcacd7-d5fb-4900-be95-98e0a99974a0" -->
### System TTS Testing (Summary)
- 6 tests passing: spd-say, espeak-ng direct, Piper raw pipeline, speak (args), speak (pipe), speak (stop)
- 1 pending: speak-selection with GNOME hotkey (requires manual hotkey setup)
- Performance: ~1.5s for short sentence, ~4s for paragraph
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_07_testing/outputs/system_tts_test_results.md`

<!-- section_id: "3edad554-216c-4cb3-81ef-135dc7ca32b6" -->
### Agentic TTS Testing (Summary)
- 4 simulated tests passing: short message, markdown stripping, empty message, missing field
- 1 pending: live Claude Code response (will auto-test on next response)
- Perceived latency: ~1-2s after Claude finishes
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_07_testing/outputs/agentic_tts_test_results.md`
