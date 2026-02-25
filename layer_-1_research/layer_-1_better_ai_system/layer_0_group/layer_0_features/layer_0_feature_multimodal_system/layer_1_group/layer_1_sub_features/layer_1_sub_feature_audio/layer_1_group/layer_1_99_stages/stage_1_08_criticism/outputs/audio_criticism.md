# Audio Criticism / Review (Parent Overview)

**Date**: 2026-02-23

## Cross-Cutting Concerns

1. **No unified speech manager**: System TTS and agentic TTS have independent PID files and kill logic. A single speech manager could coordinate them.
2. **Single voice**: Both domains use Amy medium. No voice variety yet.
3. **No speech queue**: Both domains use kill-and-replace. A proper queue would be better for long content.
4. **X11 only**: Wayland support not implemented for system TTS clipboard.

## Children — Detailed Criticism

### System TTS Criticism (Summary)
- Strengths: Natural Piper voice, simple pipeline, PID toggle, self-contained scripts
- Gaps: No speech queue, no visual feedback, fixed voice, ~0.5s model loading latency, X11 only, no text preprocessing
- Priorities: hotkey setup, voice/speed flags, piper daemon for warm model
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_08_criticism/outputs/system_tts_criticism.md`

### Agentic TTS Criticism (Summary)
- Strengths: Simple hook, reuses Piper, background execution, coexists with sound
- Gaps: No spoken_summary field from Claude, crude sed-based markdown stripping, fixed truncation, no context awareness, single hook event, no per-response disable
- Priorities: live test tuning, PostToolUse hooks, split-output pattern, proper markdown-to-text tool
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_08_criticism/outputs/agentic_tts_criticism.md`
