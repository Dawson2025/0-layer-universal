---
resource_id: "2b48f39b-15fb-4568-afcc-dcddfb04e8be"
resource_type: "output"
resource_name: "agentic_tts_research"
---
# Agentic TTS Research

**Date**: 2026-02-23

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

<!-- section_id: "59d038de-ea47-4af6-8bb9-9d95e2ee23be" -->
## Sources

- [Claude Code Hooks Documentation](https://code.claude.com/docs/en/hooks)
- [Piper TTS](https://github.com/rhasspy/piper)
