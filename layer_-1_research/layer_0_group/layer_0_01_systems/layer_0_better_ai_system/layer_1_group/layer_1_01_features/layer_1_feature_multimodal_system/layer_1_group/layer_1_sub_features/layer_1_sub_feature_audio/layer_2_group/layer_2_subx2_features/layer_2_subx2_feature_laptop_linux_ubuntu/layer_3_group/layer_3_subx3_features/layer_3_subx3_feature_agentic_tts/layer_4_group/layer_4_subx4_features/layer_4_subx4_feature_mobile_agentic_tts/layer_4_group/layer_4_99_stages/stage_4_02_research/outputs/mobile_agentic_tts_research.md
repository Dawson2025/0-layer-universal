---
resource_id: "1a2b3c4d-5e6f-4a7b-8c9d-0e1f2a3b4c5d"
resource_type: "output"
resource_name: "mobile_agentic_tts_research"
---
# Mobile Agentic TTS Research

**Date**: 2026-03-07
**Source**: Perplexity voice conversation (extracted from `/home/dawson/Downloads/And I would like to know.md`)

<!-- section_id: "2a3b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d" -->
## Problem Statement

How to set up a voice-driven interaction with AI coding agents (Claude Code, Codex, etc.) running on a remote machine, controlled entirely from a phone — enabling natural conversational voice mode for CLI tools.

<!-- section_id: "3b4c5d6e-7f8a-9b0c-1d2e-3f4a5b6c7d8e" -->
## SSH via Termius Approach

**Current capability**: Termius (iPhone SSH client) can connect to remote machines where Claude Code is installed. Voice dictation on the phone types commands into the terminal.

**Limitations**:
- Voice dictation is one-way (type commands) — no conversational back-and-forth
- No natural conversation flow like ChatGPT or Perplexity voice modes
- Response reading requires manual scrolling, no TTS for responses
- No context awareness between commands

**Assessment**: Good for basic command execution but insufficient for the target experience of natural voice conversation with an AI agent.

<!-- section_id: "4c5d6e7f-8a9b-0c1d-2e3f-4a5b6c7d8e9f" -->
## Voice Agent Platform Integration

Three main approaches identified for connecting voice to remote AI agents:

### Retell AI + n8n Workflow
- Build a workflow where Claude Code provides the logic
- Voice AI platform handles call audio (STT/TTS)
- n8n orchestrates the connection between platforms

### FreJun Integration
- Provision a phone number via FreJun API
- Route live call audio through API to backend
- Claude Code processes text and generates responses on the backend

### ElevenLabs Terminal Agent
- Set up a terminal-based agent that initiates phone calls
- Conversational voice using ElevenLabs high-quality TTS
- Can be configured to converse automatically

<!-- section_id: "5d6e7f8a-9b0c-1d2e-3f4a-5b6c7d8e9f0a" -->
## Three-Component Architecture

A complete mobile voice agent requires three components:

1. **Telephony / Voice Service** (Twilio, SIP provider, or web app)
   - Handle incoming/outgoing calls or web audio
   - Convert audio to text (STT) and text to audio (TTS)

2. **Speech Engine** (STT + TTS)
   - Understand spoken commands
   - Generate natural language audio responses

3. **AI Agent Backend** (Claude Code, Codex, OpenClaw)
   - Running on remote machine with file system access
   - Full context of projects, files, and tasks
   - Execute commands and return structured responses

**Integration flow**: Voice service → Speech engine → AI agent → Speech engine → Voice service

<!-- section_id: "6e7f8a9b-0c1d-2e3f-4a5b-6c7d8e9f0a1b" -->
## OpenClaw (Open-Source Personal Agent)

- Open-source AI project recently acquired by OpenAI
- Designed as a personal agent connecting to apps (Google Sheets, email, Slack, calendar)
- Grew extremely fast before acquisition
- Early indications suggest OpenAI will keep it open-source (possibly via a foundation)
- **Current limitation**: No built-in voice interface — text-based integrations only
- **Opportunity**: Could integrate voice input on top since it's open-source
- **No phone call support found**: No examples of OpenClaw being set up for voice calls

<!-- section_id: "7f8a9b0c-1d2e-3f4a-5b6c-7d8e9f0a1b2c" -->
## Custom Wake Sound (Tongue Click Trigger)

**Concept**: Use a tongue click as a wake word / trigger to start voice input.

**Implementation approach**:
- Audio processing library to detect specific sound signature (tongue click pattern)
- Treat detection as wake word → start recording speech
- Pass subsequent audio to STT → AI agent
- On-device wake-word engines (Picovoice) can be trained for custom sounds

**Assessment**: Definitely possible but requires custom development for sound detection accuracy.

<!-- section_id: "8a9b0c1d-2e3f-4a5b-6c7d-8e9f0a1b2c3d" -->
## Web App vs Phone Call Comparison

| Factor | Web App | Phone Call |
|--------|---------|------------|
| **Speed** | Faster data transmission via internet | Limited by phone network audio quality |
| **Data richness** | Can send context, files, rich responses | Audio-only, limited information exchange |
| **Integration** | Easy to connect with tools, calendars, file systems | Requires telephony middleware |
| **Flexibility** | Interactive UI possible alongside voice | Voice-only interface |
| **Accessibility** | Requires internet + browser | Works with traditional phone line |
| **Latency** | Lower (direct WebSocket/HTTP) | Higher (phone network + STT/TTS chain) |

**Recommendation**: Web app is generally superior for performance and functionality. Phone call is simpler for basic accessibility but trades off speed, richness, and integration ease.

<!-- section_id: "9b0c1d2e-3f4a-5b6c-7d8e-9f0a1b2c3d4e" -->
## Perplexity Voice Mode Observations

During the source conversation, the following was observed about Perplexity's voice mode capabilities:
- **Sound recognition**: Correctly identified a tongue click sound during voice conversation
- **Multi-language support**: Handled inputs in English, Korean (네), Arabic (نعم), Japanese (一、, いない), Russian (Присаживайтесь)
- **Contextual understanding**: Maintained conversation context across language switches and topic pivots

<!-- section_id: "0c1d2e3f-4a5b-6c7d-8e9f-0a1b2c3d4e5f" -->
## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Primary approach | Web app over phone call | Better performance, richer data, easier integration |
| Backend | Remote machine running Claude Code | Full file system access, existing infrastructure |
| Frontend | Mobile web app with voice I/O | Cross-platform, no app store dependency |
| Architecture | Three-layer (voice shell + brain + router) | Each component independently swappable |

<!-- section_id: "1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a" -->
## Next Steps

1. **Research web app voice frameworks** — identify best mobile-friendly voice SDK for browser
2. **Design the router component** — how voice shell connects to Claude Code backend
3. **Prototype basic flow** — browser mic → STT → text to remote Claude Code → response → TTS → audio
4. **Evaluate latency** — measure round-trip time for voice-to-response cycle
5. **Investigate wake word** — Picovoice or custom audio detection for tongue-click trigger

<!-- section_id: "2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b" -->
## Sources

- [Perplexity conversation](/home/dawson/Downloads/And I would like to know.md) — Primary source (voice conversation, 2026-03-07)
- [OpenClaw / OpenAI acquisition](https://openai.com) — Referenced in conversation
- [Retell AI](https://retellai.com) — Voice AI platform for phone calls
- [FreJun](https://frejun.com) — Phone number provisioning and call routing
- [ElevenLabs](https://elevenlabs.io) — High-quality TTS and voice agent
- [Picovoice](https://picovoice.ai) — On-device wake word engine
- [Termius](https://termius.com) — SSH client for mobile
