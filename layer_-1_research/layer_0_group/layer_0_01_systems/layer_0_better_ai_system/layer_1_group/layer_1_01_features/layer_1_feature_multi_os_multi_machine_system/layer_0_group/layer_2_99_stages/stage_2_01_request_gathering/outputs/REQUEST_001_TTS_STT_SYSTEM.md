---
resource_id: "2a9f07ba-695c-4a5e-800d-8a371d4f24ad"
resource_type: "output"
resource_name: "REQUEST_001_TTS_STT_SYSTEM"
---
# Request 001: System-Wide Text-to-Speech & AI CLI Audio Feedback

<!-- section_id: "84ae27a2-5c70-4ec9-8799-eb2f947d2ed5" -->
## Summary
Implement system-wide text-to-speech (TTS) on Ubuntu Linux with integration for AI CLI tools to provide auditory feedback during interactions.

<!-- section_id: "1bbeecad-169d-4cb2-9c17-d5d41db579cd" -->
## Current State

<!-- section_id: "6e7d5a53-c63f-4c68-b2c9-20c0a918eecd" -->
### Already Have (Speech-to-Text)
| Platform | Tool | Scope |
|----------|------|-------|
| Linux Ubuntu | Vibetyper | System-wide STT |
| Windows | Whisperflow | System-wide STT |
| iOS | Whisperflow | System-wide STT |

<!-- section_id: "a5184168-8ac5-4925-94b3-67d60a32f3dc" -->
### Missing (Text-to-Speech)
| Platform | Need | Priority |
|----------|------|----------|
| Linux Ubuntu | System-wide TTS | **Primary** |
| Windows | System-wide TTS | Secondary |

<!-- section_id: "34cc1db5-1b16-4c4c-9360-0239698e0793" -->
## Requirements

<!-- section_id: "23654cae-6b9f-46a1-a76b-829074294820" -->
### 1. System-Wide TTS on Ubuntu
- Works across all applications
- Can be triggered system-wide (hotkey, pipe, etc.)
- Quality voice output (not robotic)
- Low latency for interactive use

<!-- section_id: "1158f6f6-124f-41e6-869a-5ad5ad8c0f73" -->
### 2. AI CLI Tool Integration
Provide auditory feedback when using:
- Claude Code CLI
- Gemini CLI
- Codex CLI
- OpenCode CLI

**Use Case**: Instead of reading long CLI outputs, hear them spoken while doing other tasks or resting eyes.

<!-- section_id: "7ce65fca-0a12-4e3f-8855-26600e0eda49" -->
### 3. Platform Progression
1. **Phase 1**: Ubuntu Linux (primary development machine)
2. **Phase 2**: Windows (dual-boot compatibility)

<!-- section_id: "898d9793-ef9f-4836-8c51-3bd45c056a86" -->
## Open Questions
- [ ] Which TTS engine? (espeak, piper, coqui, cloud-based?)
- [ ] How to pipe CLI output to TTS? (wrapper script, shell function, dedicated tool?)
- [ ] Hotkey activation vs automatic reading?
- [ ] Voice selection preferences?
- [ ] Should it read everything or be selective (errors, summaries, final output)?

<!-- section_id: "7416e25e-6e89-4f7f-92c6-bc4fdb8cc316" -->
## Success Criteria
- [ ] Can speak any selected text system-wide on Ubuntu
- [ ] Can get audio output from Claude Code CLI responses
- [ ] Works offline (no cloud dependency for basic use)
- [ ] Responsive enough for conversational AI interaction
