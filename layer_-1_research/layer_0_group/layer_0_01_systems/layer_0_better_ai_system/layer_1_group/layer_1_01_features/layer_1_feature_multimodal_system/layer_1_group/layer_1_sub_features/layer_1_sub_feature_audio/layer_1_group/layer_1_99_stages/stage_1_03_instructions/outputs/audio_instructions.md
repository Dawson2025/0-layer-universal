---
resource_id: "ef62b7c6-dd15-4673-8d39-db9505bd467e"
resource_type: "output"
resource_name: "audio_instructions"
---
# Audio Instructions / Constraints (Parent Overview)

**Date**: 2026-02-23

<!-- section_id: "c287700d-9643-4bdc-8800-4b12b12995ee" -->
## Overall Constraints

1. **Shared engine**: Both system TTS and agentic TTS use Piper as the primary engine
2. **PID isolation**: Each domain uses separate PID files to avoid kill conflicts
3. **Offline only**: No cloud TTS APIs — all processing local
4. **X11 session**: Current clipboard tools assume X11 (xclip), not Wayland

<!-- section_id: "d71cf497-ff10-4717-bdad-0bf96b890e7d" -->
## Children — Detailed Instructions

<!-- section_id: "52f0958f-2c27-438e-a077-4f0371572b81" -->
### System TTS Instructions (Summary)
- Piper raw PCM at 22050 Hz S16_LE mono — aplay must match exactly
- PID files: `/tmp/speak-selection.pid`, `/tmp/speak.pid`
- Dependencies: piper (pipx), pathvalidate (injected), xclip, aplay
- Install order: pipx → inject → voice model → scripts → hotkey
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_03_instructions/outputs/system_tts_instructions.md`

<!-- section_id: "c341fd3c-c195-4006-97fd-7e52dc68eda0" -->
### Agentic TTS Instructions (Summary)
- Hook must exit 0 and run speech in background subshell
- PID file: `/tmp/claude-tts.pid`
- Dependencies: jq (JSON parsing), piper, aplay
- 60s timeout in settings.json, max 600 chars spoken
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_03_instructions/outputs/agentic_tts_instructions.md`
