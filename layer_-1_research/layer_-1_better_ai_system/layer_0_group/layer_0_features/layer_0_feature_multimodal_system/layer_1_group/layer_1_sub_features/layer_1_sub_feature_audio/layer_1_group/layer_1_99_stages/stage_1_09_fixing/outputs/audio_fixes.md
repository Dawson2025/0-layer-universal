# Audio Fixes Log (Parent Overview)

**Date**: 2026-02-23

## Cross-Cutting Fixes

### Fix 1: Piper pathvalidate Dependency
- **Affects**: Both system TTS and agentic TTS (shared engine)
- **Problem**: Piper 1.4.1 pip package missing pathvalidate dependency
- **Fix**: `pipx inject piper-tts pathvalidate`

## Children — Detailed Fixes

### System TTS Fixes (Summary)
- Only fix needed: pathvalidate injection (above)
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_system_tts/layer_2_group/layer_2_99_stages/stage_2_09_fixing/outputs/system_tts_fixes.md`

### Agentic TTS Fixes (Summary)
- No fixes required yet — pending live testing
- Anticipated: markdown stripping edge cases, truncation length tuning
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agentic_tts/layer_2_group/layer_2_99_stages/stage_2_09_fixing/outputs/agentic_tts_fixes.md`
