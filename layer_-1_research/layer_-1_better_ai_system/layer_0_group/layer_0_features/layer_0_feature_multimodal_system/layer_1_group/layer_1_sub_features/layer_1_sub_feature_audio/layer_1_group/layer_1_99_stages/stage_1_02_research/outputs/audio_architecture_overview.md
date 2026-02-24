# Audio Architecture Overview

## Two Domains, One Engine Layer

The audio sub-feature spans two distinct but related domains:

### System-Wide TTS
- **What it is**: OS-level text-to-speech, always available, reads any text on screen
- **Key tool**: Orca (GNOME screen reader) + highlight-and-speak hotkey scripts
- **How it works**: Orca reads focused UI elements; custom script grabs selection via `xsel` and pipes to TTS engine
- **Voice engine**: Speech Dispatcher → Piper (neural, natural) or eSpeak NG (lightweight, robotic)
- **Scope**: Desktop apps, browser, terminal windows — everything on the Ubuntu desktop

### Agentic TTS
- **What it is**: AI-controlled, selective speech — Claude Code decides what to speak
- **Key tool**: Claude Code hooks (PostToolUse) or MCP TTS plugin
- **How it works**: Hook intercepts response, extracts/generates short spoken summary, sends to TTS engine while full output stays in terminal
- **Voice engine**: Same Piper/eSpeak underneath, called from Python (pyttsx3) or shell
- **Scope**: Claude Code CLI responses, future AI agent outputs

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

## Recommended Engine: Piper

Piper provides the best balance:
- Neural TTS — natural-sounding voices, not robotic
- Fully offline — no cloud dependency
- Multiple voice models available (en_US-lessac, en_US-amy, etc.)
- Fast enough for real-time use
- Works as both a command-line tool and a library

## Children Features
- **System TTS** (`layer_2_subx2_feature_system_tts/`): Orca setup, Piper installation, highlight-and-speak script
- **Agentic TTS** (`layer_2_subx2_feature_agentic_tts/`): Claude Code hooks, MCP plugin evaluation, split-output pattern

## Sources
- Perplexity extraction: `perplexity_extraction_2026-02-22_tts-research.md` (same directory)
