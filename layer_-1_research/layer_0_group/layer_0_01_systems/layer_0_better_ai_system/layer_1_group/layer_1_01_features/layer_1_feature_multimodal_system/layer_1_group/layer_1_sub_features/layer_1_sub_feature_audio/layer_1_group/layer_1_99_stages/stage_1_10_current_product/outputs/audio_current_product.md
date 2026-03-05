---
resource_id: "28d0d1e1-d8b7-4dd8-aa0f-5a3e8ba12355"
resource_type: "output"
resource_name: "audio_current_product"
---
# Audio — Current Product (Parent Overview)

**Date**: 2026-02-23
**Status**: Working MVP — both domains functional

<!-- section_id: "f30ae215-d1d4-4ee4-8da8-151efdfb8142" -->
## What's Delivered

| Domain | Status | Key Deliverable |
|--------|--------|-----------------|
| System TTS | Working | `speak` + `speak-selection` scripts with Piper Amy |
| Agentic TTS | Working (basic) | Claude Code Stop hook with TTS summary |
| Shared Engine | Installed | Piper 1.4.1 + Amy medium voice model |

<!-- section_id: "2f32b3a4-95aa-446d-894c-c4d0ed204a2b" -->
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

<!-- section_id: "8406b41a-b80e-4b9a-98c1-2c3c64679d3f" -->
## Children — Detailed Current Product

<!-- section_id: "e68104e1-5cd2-4d1b-9039-b46154898f7f" -->
### System TTS Current Product (Summary)
- Scripts: `~/.local/bin/speak` (args/stdin/stop) + `~/.local/bin/speak-selection` (X11 hotkey)
- Components: Piper 1.4.1 (pipx), Amy medium voice, eSpeak NG fallback
- Limitations: Amy only, no speed control, X11 only, no visual feedback, no queue
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_10_current_product/outputs/system_tts_current_product.md`

<!-- section_id: "5fa2f728-a88e-419a-844a-76253c0f6287" -->
### Agentic TTS Current Product (Summary)
- Hook: `~/.claude/hooks/tts-response.sh` — speaks Claude response summaries
- Config: `~/.claude/settings.json` Stop hook with 60s timeout
- Behavior: strips markdown, truncates to 600 chars, speaks via Piper in background
- Limitations: Stop event only, no split-output pattern, crude markdown stripping, fixed truncation
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_10_current_product/outputs/agentic_tts_current_product.md`
