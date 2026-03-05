---
resource_id: "a681bfd2-e7cd-492e-b2d4-df18e32aad03"
resource_type: "output"
resource_name: "07_commercial_ai_memory"
---
# Memory Features in Commercial AI Platforms

## Overview

How major AI providers implement memory in their consumer and API products (as of early 2026).

---

## 1. OpenAI

### Assistants API / Threads (Deprecated → Conversations API)
- **Architecture**: Thread-based conversation persistence
- **How it works**: Each thread is a continuous chat session; every message appended chronologically
- **Storage**: Server-side, managed by OpenAI
- **Persistence**: Threads persist until deleted
- **Migration**: Assistants API deprecated, shutting down August 26, 2026; replaced by Conversations API

### Conversations API (Replacement)
- Manages long-running threads for multi-turn conversations
- Sustained interaction contexts for complex conversations
- Integration with Responses API

### ChatGPT Memory (Consumer)
- **Architecture**: Persistent user preferences and facts across conversations
- **How it works**: Model extracts and stores key facts about user; user can view/edit/delete
- **Scope**: Per-user, cross-conversation
- **User control**: Memory entries viewable, editable, and deletable
- **Custom Instructions**: Separate persistent context for behavioral preferences

### Key Characteristics
- Centralized, server-managed
- Opaque memory management (user sees entries but not internals)
- Thread-based conversation isolation

---

## 2. Anthropic Claude

### Claude Memory (Consumer - claude.ai)
- **Architecture**: Markdown-based memory files
- **How it works**: Claude automatically remembers conversation details; stored in CLAUDE.md files
- **Storage**: Simple Markdown files; model uses large context window to find relevant information
- **Capacity**: Up to 500,000 tokens (~1,000 pages) for Enterprise/Team/Max subscribers
- **Availability**: Expanded to all paid users (Max, Pro, Team, Enterprise) in late 2025

### Claude Code Memory (Developer Tool)
- **Architecture**: Auto-memory directory at `~/.claude/projects/<project>/memory/`
- **Files**: `MEMORY.md` (entrypoint, first 200 lines loaded into system prompt) + topic files
- **How it works**: Persistent across conversations; Claude records operational learnings
- **User control**: Users can tell Claude "remember X" for explicit storage; `/memory` command for file access
- **Scope**: Per-project, local to machine

### Project Knowledge (claude.ai)
- **Architecture**: Uploaded files and instructions attached to a Claude Project
- **How it works**: Files added via GitHub integration, text content, or file upload
- **Persistence**: Project-scoped, available to all conversations within that project
- **Capacity**: Multiple files, extensive context

### Key Characteristics
- File-based, transparent memory (human-readable Markdown)
- User has full control over memory content
- Per-project scoping for developer tools
- No parametric memory modification

---

## 3. Google Gemini

### Gemini Memory (Consumer)
- **Architecture**: User preference and detail learning across conversations
- **How it works**: Remembers key details and preferences from past conversations when enabled
- **Scope**: Per-user, cross-conversation
- **User control**: Setting can be toggled on/off; users control what is remembered

### Context Window
- Up to 1 million tokens (Gemini 1.5+)
- Industry-leading context scale
- Reduces need for explicit memory by fitting more in context

### Gemini Code Assist Memory
- **Architecture**: Dynamic evolving memory for team coding standards
- **How it works**: Learns from direct interactions and feedback within pull requests
- **Scope**: Team-wide coding standards, style, and best practices
- **Source**: Derived from PR interactions and feedback

### Key Characteristics
- Largest context window reduces memory pressure
- Privacy controls and temporary chat options
- Team-level memory for code review standards

---

## 4. Comparison Matrix

| Feature | OpenAI (ChatGPT) | Anthropic (Claude) | Google (Gemini) |
|---------|-------------------|-------------------|-----------------|
| **Memory type** | Extracted facts | Markdown files | Preference learning |
| **User visibility** | Memory entries list | Full file contents | Limited visibility |
| **User control** | View/edit/delete entries | Edit files directly | Toggle on/off |
| **Capacity** | Not publicly stated | 500K tokens (paid) | Not publicly stated |
| **Context window** | 128K tokens | 200K tokens | 1M+ tokens |
| **Cross-conversation** | Yes | Yes | Yes |
| **Developer API memory** | Threads/Conversations API | CLAUDE.md files | Code Assist memory |
| **Transparency** | Low (opaque extraction) | High (readable files) | Low |
| **Scope** | Per-user | Per-project or per-user | Per-user |

---

## 5. Emerging Patterns Across Platforms

### Common Approaches
- All three now offer cross-conversation memory for paid users
- Automatic extraction of preferences and facts from conversations
- User controls for privacy (view, edit, delete, disable)

### Differentiators
- **OpenAI**: Most opaque; fact-extraction based; API shifting from Assistants to Conversations
- **Anthropic**: Most transparent; file-based memory humans can read/edit; project-scoped developer memory
- **Google**: Largest context window; team-level memory for code; privacy-first with temporary chats

### Trends
- Memory as a premium feature (paid tier differentiator)
- Growing emphasis on user control and transparency
- Developer-facing memory becoming distinct from consumer memory
- Context window size partially substituting for explicit memory management

---

## Sources

- [OpenAI Assistants API Deprecation (Eesel)](https://www.eesel.ai/blog/openai-assistants-api)
- [OpenAI Threads API Guide (Eesel)](https://www.eesel.ai/blog/openai-threads-api)
- [Anthropic Claude Memory for Pro and Max Users (MacRumors)](https://www.macrumors.com/2025/10/23/anthropic-automatic-memory-claude/)
- [Claude Memory Deep Dive (Skywork)](https://skywork.ai/blog/claude-memory-a-deep-dive-into-anthropics-persistent-context-solution/)
- [Google Gemini Context Window and Memory (DataStudios)](https://www.datastudios.org/post/google-gemini-context-window-token-limits-and-memory-in-2025)
- [Gemini Code Assist Memory (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/memory-for-ai-code-reviews-using-gemini-code-assist)
