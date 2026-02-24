# Audio — Current Product (Parent Overview)

**Date**: 2026-02-23
**Status**: Working MVP — both domains functional

## What's Delivered

| Domain | Status | Key Deliverable |
|--------|--------|-----------------|
| System TTS | Working | `speak` + `speak-selection` scripts with Piper Amy |
| Agentic TTS | Working (basic) | Claude Code Stop hook with TTS summary |
| Shared Engine | Installed | Piper 1.4.1 + Amy medium voice model |

## Quick Start

```bash
# System TTS
speak "Hello world"                    # speak from args
echo "Read this" | speak               # speak from pipe
speak -s                               # stop speech
# (Bind speak-selection to Super+S for highlight-and-speak)

# Agentic TTS
# Automatic — Claude Code speaks response summaries after every response
# Kill: kill $(cat /tmp/claude-tts.pid)
```

## Children — Detailed Current Product

### System TTS Current Product (Summary)
- Scripts: `~/.local/bin/speak` (args/stdin/stop) + `~/.local/bin/speak-selection` (X11 hotkey)
- Components: Piper 1.4.1 (pipx), Amy medium voice, eSpeak NG fallback
- Limitations: Amy only, no speed control, X11 only, no visual feedback, no queue
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_system_tts/layer_2_group/layer_2_99_stages/stage_2_10_current_product/outputs/system_tts_current_product.md`

### Agentic TTS Current Product (Summary)
- Hook: `~/.claude/hooks/tts-response.sh` — speaks Claude response summaries
- Config: `~/.claude/settings.json` Stop hook with 60s timeout
- Behavior: strips markdown, truncates to 600 chars, speaks via Piper in background
- Limitations: Stop event only, no split-output pattern, crude markdown stripping, fixed truncation
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agentic_tts/layer_2_group/layer_2_99_stages/stage_2_10_current_product/outputs/agentic_tts_current_product.md`
