---
resource_id: "2a9f07ba-695c-4a5e-800d-8a371d4f24ad"
resource_type: "output"
resource_name: "REQUEST_001_TTS_STT_SYSTEM"
---
# Request 001: System-Wide Text-to-Speech & AI CLI Audio Feedback

## Summary
Implement system-wide text-to-speech (TTS) on Ubuntu Linux with integration for AI CLI tools to provide auditory feedback during interactions.

## Current State

### Already Have (Speech-to-Text)
| Platform | Tool | Scope |
|----------|------|-------|
| Linux Ubuntu | Vibetyper | System-wide STT |
| Windows | Whisperflow | System-wide STT |
| iOS | Whisperflow | System-wide STT |

### Missing (Text-to-Speech)
| Platform | Need | Priority |
|----------|------|----------|
| Linux Ubuntu | System-wide TTS | **Primary** |
| Windows | System-wide TTS | Secondary |

## Requirements

### 1. System-Wide TTS on Ubuntu
- Works across all applications
- Can be triggered system-wide (hotkey, pipe, etc.)
- Quality voice output (not robotic)
- Low latency for interactive use

### 2. AI CLI Tool Integration
Provide auditory feedback when using:
- Claude Code CLI
- Gemini CLI
- Codex CLI
- OpenCode CLI

**Use Case**: Instead of reading long CLI outputs, hear them spoken while doing other tasks or resting eyes.

### 3. Platform Progression
1. **Phase 1**: Ubuntu Linux (primary development machine)
2. **Phase 2**: Windows (dual-boot compatibility)

## Open Questions
- [ ] Which TTS engine? (espeak, piper, coqui, cloud-based?)
- [ ] How to pipe CLI output to TTS? (wrapper script, shell function, dedicated tool?)
- [ ] Hotkey activation vs automatic reading?
- [ ] Voice selection preferences?
- [ ] Should it read everything or be selective (errors, summaries, final output)?

## Success Criteria
- [ ] Can speak any selected text system-wide on Ubuntu
- [ ] Can get audio output from Claude Code CLI responses
- [ ] Works offline (no cloud dependency for basic use)
- [ ] Responsive enough for conversational AI interaction
