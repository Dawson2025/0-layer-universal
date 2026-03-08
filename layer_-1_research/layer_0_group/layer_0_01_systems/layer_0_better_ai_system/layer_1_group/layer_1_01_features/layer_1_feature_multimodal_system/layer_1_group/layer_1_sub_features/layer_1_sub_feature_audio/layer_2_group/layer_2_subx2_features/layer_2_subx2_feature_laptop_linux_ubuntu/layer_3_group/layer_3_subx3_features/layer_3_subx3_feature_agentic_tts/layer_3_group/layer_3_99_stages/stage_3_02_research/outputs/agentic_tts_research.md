---
resource_id: "2b48f39b-15fb-4568-afcc-dcddfb04e8be"
resource_type: "output"
resource_name: "agentic_tts_research"
---
# Agentic TTS Research

**Date**: 2026-02-23 (initial), 2026-03-07 (updated)

<!-- section_id: "2397f0a0-0e34-496b-8aae-1bc767a167a1" -->
## Claude Code Hooks System

Claude Code provides 18 hook events. For TTS, the key ones are:

| Event | Data Available | TTS Use Case |
|-------|---------------|--------------|
| **Stop** | `last_assistant_message` (full text) | Speak response summary |
| PostToolUse | Tool name, result summary | Announce tool completion |
| SubagentStop | Agent type, last message | Announce subagent results |
| Notification | Notification content | Speak notifications |
| TaskCompleted | Task details | Announce team task completion |

**Decision**: Start with Stop hook — highest impact, simplest implementation.

<!-- section_id: "f8e80ed6-53cc-4dc8-9673-23c50686fc52" -->
## Hook Input Format

Hooks receive JSON on stdin:
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/directory",
  "hook_event_name": "Stop",
  "last_assistant_message": "I've completed the task. Here's what I did..."
}
```

<!-- section_id: "65318f88-6f20-4cfb-a3d2-e13c6c23b39d" -->
## Community Projects Evaluated

| Project | Approach | Status |
|---------|----------|--------|
| Kokoro hook (sourcehut) | PostToolUse hook with Kokoro TTS | Not evaluated (Kokoro not installed) |
| MCP TTS plugin (GitHub) | MCP server wrapping TTS | Not evaluated (heavyweight) |
| Custom Stop hook | Direct Piper integration | **Implemented** |

**Decision**: Custom Stop hook with Piper — simplest, reuses existing system TTS infrastructure.

<!-- section_id: "288aaf8c-2792-4f42-98b3-5dd4a3475392" -->
## Text Cleanup for Speech

Markdown elements that must be stripped:
- Code blocks (``` ... ```)
- Inline code (`...`)
- Headers (# ## ###)
- Bold/italic (** _ __)
- URLs (https://...)
- File paths (/long/path/to/file)
- Table pipes (| col | col |)
- Multiple whitespace

---

<!-- section_id: "a1b2c3d4-voice-mode-landscape-2026-03-07" -->
## Voice Mode Landscape (2026-03-07 Update)

Research from Perplexity conversation covering voice mode ecosystem, prosody quality, hybrid architectures, and integration patterns.

<!-- section_id: "b2c3d4e5-claude-code-voice-mode" -->
### Claude Code Native Voice Mode

- Claude Code is rolling out `/voice` command — push-to-talk (hold spacebar, speak, release to send)
- **STT only** (speech-to-text) — no native TTS for reading responses aloud
- Gradual rollout across Pro, Max, Team, Enterprise plans (feature-flag gated, not plan-gated)
- Voice quality for conversational coding: good but not at ChatGPT's prosody level yet
- Strengths: thoughtful step-by-step explanation style integrated into coding UX

<!-- section_id: "c3d4e5f6-voice-mode-comparison" -->
### Voice Mode Quality Ranking (Prosody/Naturalness)

| Rank | System | Strengths | Weaknesses |
|------|--------|-----------|------------|
| 1 | ChatGPT Advanced Voice | Most natural prosody, emotional expressiveness, actor-grade delivery | Memory/tools limited to OpenAI ecosystem |
| 2 | Claude Code Voice | Thoughtful coding explanations, integrated with coding UX | Voice not as expressive as ChatGPT; STT only (no TTS) |
| 3 | Gemini Live | Low latency, best multimodal (camera + voice), Google ecosystem | More robotic feel, frequent disconnections |
| 4 | Perplexity Voice | Best for cited research answers via voice | Not optimized for deep free-form conversation |

<!-- section_id: "d4e5f6a7-why-chatgpt-sounds-better" -->
### Why ChatGPT Voice Sounds More Human Than Local TTS

Six architectural reasons ChatGPT voice exceeds Kokoro and other local setups:

1. **Model size and training data** — Very large neural TTS models trained on massive, prosody-rich, multi-speaker datasets. Local models (Kokoro 82M params) are much smaller with less diverse data.
2. **End-to-end prosody planning** — Predicts phrase breaks, emphasis, pitch contours, timing/pauses tied to semantics. Local setups do simpler text-to-mel-spectrogram-to-vocoder with minimal prosody control.
3. **Tight LLM-TTS coupling** — LLM emits tokens that TTS is trained to interpret (punctuation, subtle markup aligned with expressive speech). Local setups glue generic LLM to generic TTS via plain text.
4. **Streaming and overlap** — TTS voices while LLM is still generating; can adjust prosody as more context arrives. Local pipelines often chunk: wait for full sentences, then synthesize (choppy/monotonous).
5. **Inference scale** — Huge models with custom kernels on GPU clusters. Local hardware constrains to smaller models, lower sampling rates, more aggressive quantization.
6. **Voice design and post-processing** — Voice actors + model engineers curate style tokens and fine-tune emotional range. Local models trained on generic datasets lack this "acting" layer.

<!-- section_id: "e5f6a7b8-improving-kokoro-prosody" -->
### How to Improve Kokoro Prosody Locally

- **Write for speech, not text** — shorter sentences, clear commas, parentheses for asides, ellipses for pauses
- **Chunk at phrase boundaries** — don't send giant paragraphs; split on sentence/phrase boundaries for better "breathing points"
- **Add simple markup mapped to styles** — e.g., `[excited]...[/excited]` mapped to higher pitch/faster rate in pre/post-processing
- **Post-process audio** — gentle dynamics compression + EQ makes voice feel "closer" and more "present"
- **Prefer larger non-quantized TTS models** — many gains come from going tiny to medium-sized TTS
- **Stream smaller chunks** — phrase-level rather than full paragraphs, but keep context for look-ahead intonation

<!-- section_id: "f6a7b8c9-tts-engine-tier-list" -->
### TTS Engine Tier List

| Tier | Systems | Notes |
|------|---------|-------|
| **Top (commercial)** | ChatGPT voice, ElevenLabs, Fish Audio, Inworld TTS | Actor-grade prosody, emotional range |
| **High (freemium)** | ElevenLabs free tier, Speechify API, Google Cloud TTS free tier | Strong naturalness, metered usage |
| **Good (open/local)** | Kokoro 82M (current best open), F5-TTS, Bark-like models, VITS/Coqui | Kokoro leads for local; others more expressive but noisier |
| **Baseline (open/local)** | Piper, eSpeak NG | Reliable, fast, less natural |

<!-- section_id: "a7b8c9d0-speechify-api-integration" -->
### Speechify API Integration Research

- Speechify consumer subscription and API are **separate products** with separate quotas
- API pricing: free tier with limited characters, then ~$10/1M characters pay-as-you-go
- Can be wired system-wide: terminal, editors, GUI via shell functions piping text to API
- **Recommended pattern**: Keep Kokoro/local TTS as default engine; use Speechify selectively for high-quality voice (long reading sessions, published content)
- SDK available: Python/TypeScript at [github.com/SpeechifyInc/speechify-api-sdks](https://github.com/SpeechifyInc/speechify-api-sdks)

<!-- section_id: "b8c9d0e1-mcp-integration-patterns" -->
### MCP Integration Patterns for Voice

**Perplexity as MCP server** (working today):
- Perplexity exposes official MCP server for Sonar models and Search API
- Any MCP-compatible client can call Perplexity via MCP (Claude Code, OpenAI API, custom agents)
- Tools available: `perplexity_search`, `perplexity_reason`

**ChatGPT as MCP client** (evolving):
- ChatGPT supports connecting remote MCP servers to a chat/app
- Voice mode in a chat with MCP tools attached = speech -> STT -> text -> tool calls for context -> model answer -> TTS
- Gives Codex-like deep context while maintaining ChatGPT's voice quality

**VoiceMode MCP** (local, privacy-focused):
- v8.3.0, 1,601 commits, 143 releases (very actively maintained)
- Local Kokoro (GPU-accelerated) + Whisper.cpp (offline STT)
- Cloud fallback to OpenAI TTS/STT API if API key set
- Install: `uvx voice-mode-install` then `claude mcp add --scope user voicemode -- uvx --refresh voice-mode`
- See: `../../.0agnostic/01_knowledge/gpu_tts/docs/voicemode_mcp.md`

<!-- section_id: "c9d0e1f2-screen-sharing-capabilities" -->
### Screen Sharing + Voice Capabilities

| System | Image/Screenshot Input | Continuous Screen Share |
|--------|----------------------|------------------------|
| ChatGPT | Yes (send screenshots, reason about them in voice) | Limited/experimental |
| Claude Code | Yes (paste/upload screenshots, discuss in voice) | Not available |
| Gemini | Strongest (camera + uploaded images + video clips while talking) | Closest to real-time on mobile |

<!-- section_id: "d0e1f2a3-hybrid-architecture-design" -->
### Hybrid Architecture: Human Voice + Custom Memory/Context

The key insight: no single product does top-tier voice + deep custom memory/context. Solution is a three-layer hybrid:

**Layer 1 — Voice Shell (front-end)**:
- Best available voice (ChatGPT Realtime, ElevenLabs, Speechify)
- Handles: mic -> STT -> text, and text -> TTS -> audio
- Does NOT own memory; forwards text to brain layer

**Layer 2 — Brain + Memory (existing infra)**:
- Reuses existing Claude Code CLI, Codex CLI, MCP servers
- Maintains conversational memory (short-term buffer + long-term embeddings/DB)
- Calls tools: repo search, file ops, shell commands
- Returns final text response

**Layer 3 — Router**:
- Small local daemon/CLI connecting voice shell to brain
- Streams user text to brain, brain response to TTS
- Allows swapping LLM (Claude/ChatGPT/Gemini/Perplexity) without changing UX

**Net effect**: Voice quality from best commercial provider + memory/context from custom infra. Each component independently swappable.

<!-- section_id: "59d038de-ea47-4af6-8bb9-9d95e2ee23be" -->
## Sources

### Original (2026-02-23)
- [Claude Code Hooks Documentation](https://code.claude.com/docs/en/hooks)
- [Piper TTS](https://github.com/rhasspy/piper)

### Voice Mode Landscape (2026-03-07)
- [Perplexity MCP Server Docs](https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server)
- [Perplexity MCP GitHub](https://github.com/perplexityai/modelcontextprotocol)
- [OpenAI MCP Docs](https://developers.openai.com/api/docs/mcp/)
- [VoiceMode MCP](https://getvoicemode.com)
- [VoiceMode GitHub](https://github.com/mbailey/voicemode)
- [Claude Code Voice Mode — TechCrunch](https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/)
- [Claude Code Voice Mode — Reddit](https://www.reddit.com/r/ClaudeAI/comments/1rjkwqk/new_voice_mode_is_rolling_out_now_in_claude_code/)
- [Claude Voice Mode — Support](https://support.claude.com/en/articles/11101966-using-voice-mode)
- [Speechify API Pricing](https://speechify.com/pricing-api/)
- [Speechify API SDKs](https://github.com/SpeechifyInc/speechify-api-sdks)
- [ElevenLabs](https://elevenlabs.io)
- [Kokoro TTS](https://kokorottsai.com)
- [Fish Audio TTS](https://fish.audio/blog/best-ai-speech-synthesis-tools/)
- [Inworld Voice AI](https://inworld.ai/resources/best-ai-voice-generators)
- [ChatGPT vs Gemini Voice Comparison](https://www.tomsguide.com/ai/google-gemini/google-gemini-live-vs-chatgpt-4o-voice-which-ai-assistant-could-win)
- [Best AI Voice Assistants 2026](https://www.krater.ai/blog/best-ai-voice-assistants-2026)
- [claude-code-tts (sourcehut)](https://git.sr.ht/~cg/claude-code-tts)
- [claude-code-tts MCP Plugin (GitHub)](https://github.com/ybouhjira/claude-code-tts)
- [Local Voice Pipeline for Claude Code](https://crunchtools.com/local-voice-pipeline-claude-code-rhel10-intel-gpu/)
- [Perplexity Changelog — March 6, 2026](https://www.perplexity.ai/changelog/what-we-shipped---march-6-2026)
