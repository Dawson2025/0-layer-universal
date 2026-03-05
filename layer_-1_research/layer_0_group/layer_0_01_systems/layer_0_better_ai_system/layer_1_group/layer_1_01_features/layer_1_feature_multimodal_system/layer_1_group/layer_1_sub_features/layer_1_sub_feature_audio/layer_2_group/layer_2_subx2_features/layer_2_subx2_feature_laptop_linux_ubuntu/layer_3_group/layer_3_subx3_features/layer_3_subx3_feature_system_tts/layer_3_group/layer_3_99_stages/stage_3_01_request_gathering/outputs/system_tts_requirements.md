---
resource_id: "7870ecff-d58b-4726-856e-e93649160644"
resource_type: "output"
resource_name: "system_tts_requirements"
---
# System TTS Requirements

**Date**: 2026-02-23

## Core Requirements

1. **Highlight-and-speak**: Select any text on screen, press a hotkey, hear it spoken aloud
2. **CLI speak command**: Pipe text or pass arguments to a `speak` command for terminal use
3. **Natural-sounding voice**: Not robotic — neural TTS (Piper) over basic synthesizers (eSpeak)
4. **Offline operation**: No cloud APIs required, all processing local
5. **Low latency**: Speech should begin within ~1 second of request
6. **Toggle/stop**: Ability to stop speech mid-utterance

## User Stories

- As a user, I want to highlight a paragraph in my browser and hear it read aloud so I can multitask
- As a developer, I want to pipe command output through TTS so I can hear results while looking away
- As a user, I want to press the same hotkey again to stop speech if it's too long

## Constraints

- Linux/Ubuntu desktop (X11 session, PulseAudio)
- No paid API dependencies
- Must coexist with Orca screen reader (if active)
- Must not conflict with agentic TTS (different PID files for stop control)

## Acceptance Criteria

- [ ] `speak "Hello"` produces audible natural speech
- [ ] `echo "text" | speak` works via pipe
- [ ] `speak -s` stops current speech
- [ ] `speak-selection` reads X primary selection
- [ ] Hotkey (Super+S) triggers speak-selection
- [ ] Speech uses Piper Amy voice (not eSpeak)
