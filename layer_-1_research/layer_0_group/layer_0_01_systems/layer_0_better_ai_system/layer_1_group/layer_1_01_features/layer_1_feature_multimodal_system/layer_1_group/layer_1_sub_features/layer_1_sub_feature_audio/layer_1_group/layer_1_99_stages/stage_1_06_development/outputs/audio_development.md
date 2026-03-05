---
resource_id: "cd642b1c-ecfd-4c0f-9fc0-9c9c72979c00"
resource_type: "output"
resource_name: "audio_development"
---
# Audio Development (Parent Overview)

**Date**: 2026-02-23

## Overall Development Summary

Both TTS domains have working MVPs:
- **System TTS**: Piper installed, `speak` and `speak-selection` scripts working
- **Agentic TTS**: Stop hook installed, speaks Claude response summaries via Piper

Shared infrastructure: Piper 1.4.1 (pipx) + Amy medium voice at `~/.local/share/piper-voices/`

## Children — Detailed Development

### System TTS Development (Summary)
- Installed Piper 1.4.1 via pipx, fixed pathvalidate dependency
- Downloaded en_US-amy-medium voice model (60MB)
- Created `~/.local/bin/speak` (args, stdin, stop) and `~/.local/bin/speak-selection` (X11 hotkey)
- All tests passing: spd-say, espeak-ng, Piper direct, speak (args), speak (pipe)
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_06_development/outputs/system_tts_setup.md`

### Agentic TTS Development (Summary)
- Created `~/.claude/hooks/tts-response.sh` — extracts `last_assistant_message`, strips markdown, truncates, speaks via Piper in background
- Added to `~/.claude/settings.json` Stop hook array (after completion sound)
- Simulated test passing, live test pending
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_06_development/outputs/agentic_tts_setup.md`
