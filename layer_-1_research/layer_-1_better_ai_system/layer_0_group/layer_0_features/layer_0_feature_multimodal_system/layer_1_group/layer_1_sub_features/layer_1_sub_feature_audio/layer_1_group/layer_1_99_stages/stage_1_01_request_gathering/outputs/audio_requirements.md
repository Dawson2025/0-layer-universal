# Audio Requirements

## Core Need

Hands-free, selective text-to-speech across two domains:
1. **System-wide TTS** — read any text on the Ubuntu desktop, browser, or terminal on demand
2. **Agentic TTS** — AI-controlled speech where Claude Code decides what to speak vs what to show visually

## User Needs

### System-Wide TTS
- Highlight any text anywhere on screen and have it read aloud via hotkey
- Screen reader for navigating GUI apps, browser, and terminal
- Natural-sounding voice (not robotic eSpeak default)
- Fully offline — no cloud dependency
- Works in both GNOME desktop apps and terminal windows

### Agentic TTS (Claude Code)
- Claude Code speaks short conversational summaries while showing full output visually
- What you hear is NOT what you see — split output pattern
- Automatic (hook-based) rather than requiring manual piping
- Works with the existing Claude Code hook system
- Local TTS engine (no cloud API calls per response)

## Shared Requirements
- Single TTS engine layer (Piper, eSpeak, or Festival) used by both domains
- No conflicts between system screen reader and agentic TTS
- Ability to interrupt/stop speech

## Children — Detailed Requirements

This document covers the **overall audio requirements** at the parent level. Each child sub-feature has its own detailed requirements:

### System TTS Requirements (Summary)
- Highlight-and-speak via hotkey, CLI `speak` command, offline Piper TTS, toggle/stop control
- Acceptance criteria: `speak "text"`, pipe input, hotkey selection, natural Amy voice
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_system_tts/layer_2_group/layer_2_99_stages/stage_2_01_request_gathering/outputs/system_tts_requirements.md`

### Agentic TTS Requirements (Summary)
- Auto-speak Claude responses via Stop hook, markdown cleanup, length truncation, background execution
- Acceptance criteria: Hook triggers TTS, code blocks stripped, long responses truncated, coexists with sound
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agentic_tts/layer_2_group/layer_2_99_stages/stage_2_01_request_gathering/outputs/agentic_tts_requirements.md`
