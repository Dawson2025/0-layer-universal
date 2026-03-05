---
resource_id: "9cd506d9-8b73-4aab-b8c5-227be3dc4d38"
resource_type: "output"
resource_name: "NATIVE_FEATURES"
---
# Cursor IDE — Native Features

**Date**: 2026-02-27
**Focus**: What Cursor provides natively (the mechanisms)

---

<!-- section_id: "a42eaa17-aad3-4522-aefc-2f35263445e4" -->
## Overview

Cursor IDE provides these built-in mechanisms for AI-powered development:

1. **Built-in AI Assistant** (Claude, GPT-4, other models)
2. **.cursor/rules Configuration System** (YAML-based context rules)
3. **Semantic Search** (proprietary embeddings + code search)
4. **Memory Bank** (persistent persistent multi-turn state)
5. **Tab Context** (automatic current file/selection inclusion)
6. **MCP Integration** (Model Context Protocol for external tools)
7. **Agent CLI** (Command-line agentic execution)
8. **Hooks System** (Lifecycle events: pre-save, post-save, etc.)
9. **IDE Extensions** (VS Code fork with integrated AI)
10. **Cloud Agents** (Remote execution, state persistence)

---

<!-- section_id: "9025e320-d249-4dbf-b0ee-524dbb9fd489" -->
## 1. Built-in AI Assistant

<!-- section_id: "8f5eb029-d7b4-49b9-a72c-97b8bbcde934" -->
### The Mechanism

Cursor comes with integrated AI assistant (Claude by default, with options for other models):

**Model Options**:
- Claude (default)
- GPT-4
- Claude Pro
- Custom API endpoints

**Access Points**:
- Chat sidebar (persistent conversation)
- Inline suggestions (inline code completion)
- Command palette (quick access to AI features)

<!-- section_id: "331bd940-7941-43f4-b240-8eac8c4d629c" -->
### What Cursor Does

- **Initializes** the AI model in the IDE
- **Routes** requests to the specified model endpoint
- **Maintains** chat history within a session
- **Applies** IDE context (current file, selection) automatically
- **Streams** responses token-by-token in real-time

<!-- section_id: "217fdb32-62c6-459a-b59b-1b6bf8f582bc" -->
### What Cursor Does NOT Do

- Doesn't persist conversations across IDE restarts (sessions are ephemeral unless using Memory Bank)
- Doesn't provide token counting before requests
- Doesn't expose model selection in UI (must edit config)
- Doesn't offer built-in cost tracking
- Doesn't support custom system prompts via UI (use .cursor/rules)

---

<!-- section_id: "538dd417-f015-49f9-b66d-6c773f20a6a1" -->
## 2. .cursor/rules Configuration System

<!-- section_id: "aa9b742f-2279-4f96-a799-671a6129de5c" -->
### The Mechanism

Cursor reads rules from `project/.cursor/rules/` (YAML files) or `~/.cursor/rules/` (global):

**Format**: YAML with frontmatter options

```yaml
---
mode: "Always Apply"  # Always Apply | Intelligently | Specific Files | Manual
description: "Code style guide"
---

# Guidelines
- Use camelCase for variables
- Import order: third-party, local
- Prefer const over let
```

**Rule Application**:
- **Always Apply**: Loaded for every request
- **Intelligently**: Loaded when Cursor detects relevance
- **Specific Files**: Loaded only for matching file paths
- **Manual**: Loaded only when user explicitly invokes

<!-- section_id: "b81d38d9-b2dd-4d97-9d37-82e63a700314" -->
### What Cursor Does

- **Loads** all applicable rules from directories
- **Merges** rules (later files override earlier)
- **Applies** to every AI request in the IDE
- **Supports** glob patterns for file matching
- **Provides** rule precedence (user > project > global)

<!-- section_id: "0fdd4ca5-6942-4e74-9ad9-302fb429a0a3" -->
### What Cursor Does NOT Do

- Doesn't validate rule syntax (malformed YAML can cause silent failures)
- Doesn't expose rule loading order in UI
- Doesn't support rule versioning
- Doesn't warn about conflicting rules
- Doesn't support conditional rule loading (except via file paths)

---

<!-- section_id: "76f3fab6-210e-495e-826d-b554060c8823" -->
## 3. Semantic Search

<!-- section_id: "d5927ef3-c0a6-443d-87a6-077f136d5011" -->
### The Mechanism

Cursor implements semantic search with proprietary embeddings:

**How It Works**:
1. Generate embeddings for all code in project
2. Index embeddings in local vector database
3. User provides natural language query
4. System finds semantically related code
5. Return ranked results

**Features**:
- Understand code intent (not just keyword matching)
- Find similar patterns across codebase
- Cross-file search
- Fast (<1 second on typical projects)

<!-- section_id: "ea7fc652-b4c6-407b-ae69-c11f68a8744b" -->
### What Cursor Does

- **Generates** embeddings for all project files
- **Maintains** local vector index
- **Processes** natural language queries
- **Returns** ranked semantic matches
- **Updates** index when files change

<!-- section_id: "e6d53022-ab81-44ed-8472-8da1678b55f4" -->
### What Cursor Does NOT Do

- Doesn't expose embedding model name
- Doesn't allow custom embeddings
- Doesn't provide relevance scores
- Doesn't support semantic search API from code
- Doesn't search across multiple projects

---

<!-- section_id: "b3017360-0761-4ac4-ac1e-1c525537c88a" -->
## 4. Memory Bank

<!-- section_id: "d48339f6-072a-433c-99d3-65830202e374" -->
### The Mechanism

Persistent multi-turn conversation state:

**Storage**: `~/.cursor/memory_bank/` (local file storage)

**How It Works**:
1. Each conversation is a "memory"
2. User can create/edit/delete memories
3. Cursor includes relevant memories in chat context
4. Memories persist across sessions

<!-- section_id: "320fdc83-5a60-4189-b8c2-2cb9b0e7418f" -->
### What Cursor Does

- **Stores** conversation summaries and important notes
- **Retrieves** memories when relevant to current context
- **Maintains** persistent state across IDE restarts
- **Allows** manual memory creation and editing
- **Supports** memory organization (folders, tags)

<!-- section_id: "198d985b-20d4-4b59-8f9c-b2bf2a62f1da" -->
### What Cursor Does NOT Do

- Doesn't auto-summarize long conversations (you must create memories manually)
- Doesn't provide memory search API
- Doesn't support memory versioning
- Doesn't offer collaborative memory (single-user only)
- Doesn't encrypt memories

---

<!-- section_id: "75ad2dc6-e542-4e22-b9d5-2a2e6f284da9" -->
## 5. Tab Context

<!-- section_id: "e0659d06-d6b0-46ce-b467-e155a88d9092" -->
### The Mechanism

Cursor automatically includes IDE context in AI requests:

**What's Included**:
- Current file content
- Current cursor position/selection
- Open tabs (file list)
- Recent files
- Current git branch

**Automatic Inclusion**:
- Every chat request includes current file
- Every inline suggestion includes surrounding code
- File path provides folder context

<!-- section_id: "14d5c89e-77b0-4bf7-b231-164192616f7d" -->
### What Cursor Does

- **Monitors** current file and selection
- **Injects** context into every AI request
- **Updates** context as user switches files
- **Provides** file path information (for rules matching)
- **Handles** large files (truncation if needed)

<!-- section_id: "d0ec8a4c-0f1f-4e93-b647-80ad4dc53dad" -->
### What Cursor Does NOT Do

- Doesn't expose context size in tokens
- Doesn't allow disabling context inclusion
- Doesn't support context filtering
- Doesn't include file history or git information
- Doesn't support custom context sources

---

<!-- section_id: "87597395-9cd8-4e6c-a4c8-f90340206eff" -->
## 6. MCP Integration

<!-- section_id: "813f0e82-d9c0-477d-8160-b1d775146aac" -->
### The Mechanism

Model Context Protocol support for external tools:

**Configuration**: `.cursor/mcp.json` or `~/.cursor/mcp.json`

```json
{
  "mcpServers": {
    "canvas": {
      "command": "python",
      "args": ["-m", "mcp_canvas"],
      "env": {"CANVAS_TOKEN": "..."}
    },
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {"GITHUB_TOKEN": "..."}
    }
  }
}
```

<!-- section_id: "463be19e-4aa8-43b4-b7e5-d5468077dd7e" -->
### What Cursor Does

- **Launches** MCP servers from config
- **Manages** server lifecycle (start/stop/restart)
- **Routes** tool calls to appropriate servers
- **Returns** tool results to AI context
- **Handles** errors and timeouts

<!-- section_id: "d6aa2d7c-84c5-4ed6-adfc-709d2ae10ecc" -->
### What Cursor Does NOT Do

- Doesn't validate MCP server configuration
- Doesn't provide MCP server management UI
- Doesn't support server discovery
- Doesn't offer built-in server implementations
- Doesn't expose MCP logs in IDE

---

<!-- section_id: "78e88c37-2ab2-460f-8431-e5db46a0996e" -->
## 7. Agent CLI

<!-- section_id: "d601d097-457c-4531-bfda-7a1065e948eb" -->
### The Mechanism

Command-line tool for agentic execution:

```bash
cursor agent --workspace ~/my-project
cursor agent resume [session-id]
cursor agent ls
cursor agent mcp ls
```

**Capabilities**:
- Autonomous task execution
- Session persistence
- Shell command execution (with approval)
- MCP tool integration
- State management

<!-- section_id: "ad96a2bf-8d5d-4539-9b89-62a2da5306d9" -->
### What Cursor Does

- **Accepts** tasks from CLI
- **Executes** tasks autonomously with human approval
- **Persists** session state
- **Manages** shell commands (user approval required)
- **Integrates** with MCP servers

<!-- section_id: "ba5161f4-9681-4d7f-9de6-5603cd163d08" -->
### What Cursor Does NOT Do

- Doesn't auto-execute shell commands (requires approval)
- Doesn't provide output streaming to CLI
- Doesn't support collaborative sessions
- Doesn't offer built-in task scheduling
- Doesn't provide cloud execution (runs locally)

---

<!-- section_id: "a6b3b19e-5fa8-47a6-9299-6616f2c9a07a" -->
## 8. Hooks System

<!-- section_id: "6dcb0f7a-da6d-420e-bf6d-c023d09a98e4" -->
### The Mechanism

Lifecycle event hooks for custom automation:

**Configuration**: `~/.cursor/hooks.json` or `.cursor/hooks.json`

```json
{
  "hooks": {
    "pre-save": [
      {
        "event": "file.save",
        "command": "eslint --fix",
        "glob": "src/**/*.js"
      }
    ],
    "post-save": [
      {
        "event": "file.save",
        "command": "npm run test",
        "glob": "**/*.test.js"
      }
    ]
  }
}
```

**Available Events**:
- `file.save`
- `file.create`
- `file.delete`
- `project.open`
- `project.close`
- `debug.start`
- `debug.stop`

<!-- section_id: "50691dc0-9e16-407f-8957-d08009a9f4ee" -->
### What Cursor Does

- **Monitors** specified file events
- **Executes** configured commands on event
- **Applies** glob patterns for file matching
- **Passes** file path to command
- **Handles** command output and errors

<!-- section_id: "cc4609cb-b18a-4ddc-801d-7ddcef08afdd" -->
### What Cursor Does NOT Do

- Doesn't validate hook commands before execution
- Doesn't provide hook output in UI
- Doesn't support conditional hooks
- Doesn't offer hook debugging
- Doesn't support async hook execution

---

<!-- section_id: "912a6b9b-7284-4da0-a9a3-608709aead74" -->
## 9. IDE Extensions

<!-- section_id: "bd5b4d18-da0f-4370-be33-17fb4d614704" -->
### The Mechanism

Cursor is built on VS Code with extensions for AI features:

**Built-in Extensions**:
- AI Chat Sidebar
- Inline Suggestions
- Command Palette Integration
- Semantic Search
- Memory Bank UI

**Extensibility**:
- Can install VS Code extensions
- Can use VS Code settings
- Can leverage VS Code API (limited)

<!-- section_id: "24b11214-1546-4706-a04d-37e7e55605ee" -->
### What Cursor Does

- **Provides** AI-powered extensions out-of-box
- **Supports** VS Code extension ecosystem
- **Applies** extension settings from settings.json
- **Manages** extension lifecycle
- **Integrates** extensions with AI context

<!-- section_id: "d0d89084-60bc-4f0a-bbd2-31a26224450f" -->
### What Cursor Does NOT Do

- Doesn't allow custom AI extension development (limited API)
- Doesn't expose extension configuration in UI
- Doesn't support extension marketplace integration
- Doesn't provide extension API documentation (VS Code API only)

---

<!-- section_id: "6dc16157-5e1a-4c92-bc94-0528e7392425" -->
## 10. Cloud Agents

<!-- section_id: "12dd059d-90f3-41b7-95ba-41faca9eb105" -->
### The Mechanism

Remote execution with persistent state:

**How It Works**:
1. Submit task to Cursor Cloud
2. Cloud agent executes autonomously
3. State persists between turns
4. Results streamed back to local IDE
5. Can resume interrupted tasks

<!-- section_id: "bf207e3a-147f-4a41-9681-60c2183b26c4" -->
### What Cursor Does

- **Submits** tasks to remote agents
- **Maintains** session state in cloud
- **Streams** results to local IDE
- **Handles** resource constraints
- **Provides** resumption tokens

<!-- section_id: "564c3f74-2662-46b7-8232-1049d88787bb" -->
### What Cursor Does NOT Do

- Doesn't offer free cloud agent quotas
- Doesn't provide observability into cloud execution
- Doesn't support custom cloud environment setup
- Doesn't expose cloud agent logs
- Doesn't support collaborative cloud agents

---

<!-- section_id: "2181ba43-e545-4d58-91d7-f93ec5fc7066" -->
## Summary: Native = Mechanisms Provided

Cursor provides **mechanisms** (how things work), not **policies** (what to do with them):

✅ **Native**: Reads .cursor/rules and applies them to every AI request
❌ **Not native**: You decide what rules to create

✅ **Native**: Automatically includes current file context in chat
❌ **Not native**: You decide what context is relevant

✅ **Native**: Supports MCP servers (launches, manages, routes tools)
❌ **Not native**: You choose which servers to configure

✅ **Native**: Provides Memory Bank storage
❌ **Not native**: You decide what to remember

✅ **Native**: Implements semantic search
❌ **Not native**: You decide when to use it

✅ **Native**: Executes shell commands via hooks
❌ **Not native**: You define the hooks and commands

✅ **Native**: Supports Agent CLI
❌ **Not native**: You decide what tasks to delegate to agents

