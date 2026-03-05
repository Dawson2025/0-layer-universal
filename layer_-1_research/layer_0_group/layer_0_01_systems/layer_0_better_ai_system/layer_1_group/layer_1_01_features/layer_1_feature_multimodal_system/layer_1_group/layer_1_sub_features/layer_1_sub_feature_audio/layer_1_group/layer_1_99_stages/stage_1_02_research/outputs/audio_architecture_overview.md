---
resource_id: "e53d02d2-ae1a-4a71-a1fa-74b5057e9023"
resource_type: "output"
resource_name: "audio_architecture_overview"
---
# Audio Architecture Overview

<!-- section_id: "2a9dfda1-59ea-4e26-b7b5-a57bb142237c" -->
## Two Domains, One Engine Layer

The audio sub-feature spans two distinct but related domains:

<!-- section_id: "43a62602-18ba-432e-b341-c3c52512c42e" -->
### System-Wide TTS
- **What it is**: OS-level text-to-speech, always available, reads any text on screen
- **Key tool**: Orca (GNOME screen reader) + highlight-and-speak hotkey scripts
- **How it works**: Orca reads focused UI elements; custom script grabs selection via `xsel` and pipes to TTS engine
- **Voice engine**: Speech Dispatcher → Piper (neural, natural) or eSpeak NG (lightweight, robotic)
- **Scope**: Desktop apps, browser, terminal windows — everything on the Ubuntu desktop

<!-- section_id: "6f47aa7d-a8e6-4261-8308-4e3d6bd6645b" -->
### Agentic TTS
- **What it is**: AI-controlled, selective speech — Claude Code decides what to speak
- **Key tool**: Claude Code hooks (PostToolUse) or MCP TTS plugin
- **How it works**: Hook intercepts response, extracts/generates short spoken summary, sends to TTS engine while full output stays in terminal
- **Voice engine**: Same Piper/eSpeak underneath, called from Python (pyttsx3) or shell
- **Scope**: Claude Code CLI responses, future AI agent outputs

<!-- section_id: "4e3e0c3d-6476-48a8-9404-19c827bc75ac" -->
### How They Relate

```
┌─────────────────────────────────────────┐
│           User's Ubuntu Desktop          │
├──────────────────┬──────────────────────┤
│  System-Wide TTS │    Agentic TTS       │
│  (Orca + hotkey) │  (Claude Code hooks) │
├──────────────────┴──────────────────────┤
│         Speech Dispatcher               │
├─────────────────────────────────────────┤
│    TTS Engine (Piper / eSpeak / Festival)│
├─────────────────────────────────────────┤
│         Audio Output (PulseAudio)        │
└─────────────────────────────────────────┘
```

**Shared**: Both use the same TTS engine layer (Piper recommended for voice quality). Speech Dispatcher acts as the middleware that routes text to the engine.

**Independent**: System TTS fires from user action (hotkey, Orca navigation). Agentic TTS fires from AI events (Claude Code hook). They don't interfere because they're triggered by different things.

**Potential conflict**: If Orca is actively speaking and a Claude Code hook also tries to speak simultaneously, Speech Dispatcher queues or interrupts. This is manageable but worth testing.

<!-- section_id: "350b7db5-7e84-4a1f-a945-1d2c6721dd6a" -->
## Recommended Engine: Piper

Piper provides the best balance:
- Neural TTS — natural-sounding voices, not robotic
- Fully offline — no cloud dependency
- Multiple voice models available (en_US-lessac, en_US-amy, etc.)
- Fast enough for real-time use
- Works as both a command-line tool and a library

<!-- section_id: "59f16376-1a5d-4e7e-8c39-8344bacb72ff" -->
## Children — Detailed Research

This document covers the **overall audio architecture** at the parent level. Each child has its own research outputs:

<!-- section_id: "7ab48c5a-ca35-40fe-833c-9ac91e328220" -->
### System TTS Research (Summary)
- Compared TTS engines: Piper (neural, best quality), eSpeak (robotic, lightweight), Festival (medium), Mimic 3 (neural, heavy)
- Evaluated voice models: Amy medium (chosen), Lessac medium, Alan medium
- Chose xclip for X11 clipboard, aplay for audio output
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_system_tts/layer_3_group/layer_3_99_stages/stage_3_02_research/outputs/system_tts_research.md`

<!-- section_id: "d61b693c-3880-4b0f-ab86-06bacc9c5198" -->
### Agentic TTS Research (Summary)
- Mapped Claude Code hooks API: 18 events, Stop hook provides `last_assistant_message` directly
- Evaluated community projects: Kokoro hook, MCP TTS plugin — chose custom Stop hook for simplicity
- Defined text cleanup requirements: code blocks, markdown, URLs, paths must be stripped
- **Full details**: `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_laptop_linux_ubuntu/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_agentic_tts/layer_3_group/layer_3_99_stages/stage_3_02_research/outputs/agentic_tts_research.md`

<!-- section_id: "684cf957-f3e2-454e-b5c2-a9df5473a0ea" -->
## Sources
- Perplexity extraction: `perplexity_extraction_2026-02-22_tts-research.md` (same directory)
