---
resource_id: "7eb56a68-6d19-41d5-92f9-84197e256d49"
resource_type: "output"
resource_name: "audio_requirements"
---
# Audio Requirements

<!-- section_id: "38eeaf78-0264-40dd-81f0-9e9ad279f07c" -->
## Core Need

Hands-free, selective text-to-speech across two domains:
1. **System-wide TTS** — read any text on the Ubuntu desktop, browser, or terminal on demand
2. **Agentic TTS** — AI-controlled speech where Claude Code decides what to speak vs what to show visually

<!-- section_id: "5e167720-a592-4946-b461-008fc552455a" -->
## User Needs

<!-- section_id: "7499d98a-e1a7-4090-9b79-d1b3e4157765" -->
### System-Wide TTS
- Highlight any text anywhere on screen and have it read aloud via hotkey
- Screen reader for navigating GUI apps, browser, and terminal
- Natural-sounding voice (not robotic eSpeak default)
- Fully offline — no cloud dependency
- Works in both GNOME desktop apps and terminal windows

<!-- section_id: "e2eb2ab3-da62-46c2-97b0-9dad67c8c592" -->
### Agentic TTS (Claude Code)
- Claude Code speaks short conversational summaries while showing full output visually
- What you hear is NOT what you see — split output pattern
- Automatic (hook-based) rather than requiring manual piping
- Works with the existing Claude Code hook system
- Local TTS engine (no cloud API calls per response)

<!-- section_id: "3e8fdd3c-c80c-4aff-9c50-c2a5440a6211" -->
## Shared Requirements
- Single TTS engine layer (Piper, eSpeak, or Festival) used by both domains
- No conflicts between system screen reader and agentic TTS
- Ability to interrupt/stop speech

<!-- section_id: "0426781b-8dfb-4383-a0cd-780b5ae86ccd" -->
## Children — Detailed Requirements

This document covers the **overall audio requirements** at the parent level. Each child sub-feature has its own detailed requirements:

<!-- section_id: "9385512c-77b1-4f8e-8eba-e4c86b219388" -->
### System TTS Requirements (Summary)
- Highlight-and-speak via hotkey, CLI `speak` command, offline Piper TTS, toggle/stop control
- Acceptance criteria: `speak "text"`, pipe input, hotkey selection, natural Amy voice
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_01_request_gathering/outputs/system_tts_requirements.md`

<!-- section_id: "4b2dde3e-046a-47bb-ac95-5b90c560527d" -->
### Agentic TTS Requirements (Summary)
- Auto-speak Claude responses via Stop hook, markdown cleanup, length truncation, background execution
- Acceptance criteria: Hook triggers TTS, code blocks stripped, long responses truncated, coexists with sound
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_01_request_gathering/outputs/agentic_tts_requirements.md`
