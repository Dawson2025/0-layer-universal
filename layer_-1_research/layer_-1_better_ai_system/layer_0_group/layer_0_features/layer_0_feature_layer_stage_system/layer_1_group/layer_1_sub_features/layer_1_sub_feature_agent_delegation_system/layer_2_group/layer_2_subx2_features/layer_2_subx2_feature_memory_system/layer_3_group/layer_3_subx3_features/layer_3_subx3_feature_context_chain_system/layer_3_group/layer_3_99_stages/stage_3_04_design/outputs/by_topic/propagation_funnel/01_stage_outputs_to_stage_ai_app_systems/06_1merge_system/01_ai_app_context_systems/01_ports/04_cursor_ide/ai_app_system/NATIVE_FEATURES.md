# Cursor IDE — Native Features

**Date**: 2026-02-27
**Focus**: What Cursor provides natively (the mechanisms)

---

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

## 1. Built-in AI Assistant

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

### What Cursor Does

- **Initializes** the AI model in the IDE
- **Routes** requests to the specified model endpoint
- **Maintains** chat history within a session
- **Applies** IDE context (current file, selection) automatically
- **Streams** responses token-by-token in real-time

### What Cursor Does NOT Do

- Doesn't persist conversations across IDE restarts (sessions are ephemeral unless using Memory Bank)
- Doesn't provide token counting before requests
- Doesn't expose model selection in UI (must edit config)
- Doesn't offer built-in cost tracking
- Doesn't support custom system prompts via UI (use .cursor/rules)

---

## 2. .cursor/rules Configuration System

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

### What Cursor Does

- **Loads** all applicable rules from directories
- **Merges** rules (later files override earlier)
- **Applies** to every AI request in the IDE
- **Supports** glob patterns for file matching
- **Provides** rule precedence (user > project > global)

### What Cursor Does NOT Do

- Doesn't validate rule syntax (malformed YAML can cause silent failures)
- Doesn't expose rule loading order in UI
- Doesn't support rule versioning
- Doesn't warn about conflicting rules
- Doesn't support conditional rule loading (except via file paths)

---

## 3. Semantic Search

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

### What Cursor Does

- **Generates** embeddings for all project files
- **Maintains** local vector index
- **Processes** natural language queries
- **Returns** ranked semantic matches
- **Updates** index when files change

### What Cursor Does NOT Do

- Doesn't expose embedding model name
- Doesn't allow custom embeddings
- Doesn't provide relevance scores
- Doesn't support semantic search API from code
- Doesn't search across multiple projects

---

## 4. Memory Bank

### The Mechanism

Persistent multi-turn conversation state:

**Storage**: `~/.cursor/memory_bank/` (local file storage)

**How It Works**:
1. Each conversation is a "memory"
2. User can create/edit/delete memories
3. Cursor includes relevant memories in chat context
4. Memories persist across sessions

### What Cursor Does

- **Stores** conversation summaries and important notes
- **Retrieves** memories when relevant to current context
- **Maintains** persistent state across IDE restarts
- **Allows** manual memory creation and editing
- **Supports** memory organization (folders, tags)

### What Cursor Does NOT Do

- Doesn't auto-summarize long conversations (you must create memories manually)
- Doesn't provide memory search API
- Doesn't support memory versioning
- Doesn't offer collaborative memory (single-user only)
- Doesn't encrypt memories

---

## 5. Tab Context

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

### What Cursor Does

- **Monitors** current file and selection
- **Injects** context into every AI request
- **Updates** context as user switches files
- **Provides** file path information (for rules matching)
- **Handles** large files (truncation if needed)

### What Cursor Does NOT Do

- Doesn't expose context size in tokens
- Doesn't allow disabling context inclusion
- Doesn't support context filtering
- Doesn't include file history or git information
- Doesn't support custom context sources

---

## 6. MCP Integration

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

### What Cursor Does

- **Launches** MCP servers from config
- **Manages** server lifecycle (start/stop/restart)
- **Routes** tool calls to appropriate servers
- **Returns** tool results to AI context
- **Handles** errors and timeouts

### What Cursor Does NOT Do

- Doesn't validate MCP server configuration
- Doesn't provide MCP server management UI
- Doesn't support server discovery
- Doesn't offer built-in server implementations
- Doesn't expose MCP logs in IDE

---

## 7. Agent CLI

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

### What Cursor Does

- **Accepts** tasks from CLI
- **Executes** tasks autonomously with human approval
- **Persists** session state
- **Manages** shell commands (user approval required)
- **Integrates** with MCP servers

### What Cursor Does NOT Do

- Doesn't auto-execute shell commands (requires approval)
- Doesn't provide output streaming to CLI
- Doesn't support collaborative sessions
- Doesn't offer built-in task scheduling
- Doesn't provide cloud execution (runs locally)

---

## 8. Hooks System

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

### What Cursor Does

- **Monitors** specified file events
- **Executes** configured commands on event
- **Applies** glob patterns for file matching
- **Passes** file path to command
- **Handles** command output and errors

### What Cursor Does NOT Do

- Doesn't validate hook commands before execution
- Doesn't provide hook output in UI
- Doesn't support conditional hooks
- Doesn't offer hook debugging
- Doesn't support async hook execution

---

## 9. IDE Extensions

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

### What Cursor Does

- **Provides** AI-powered extensions out-of-box
- **Supports** VS Code extension ecosystem
- **Applies** extension settings from settings.json
- **Manages** extension lifecycle
- **Integrates** extensions with AI context

### What Cursor Does NOT Do

- Doesn't allow custom AI extension development (limited API)
- Doesn't expose extension configuration in UI
- Doesn't support extension marketplace integration
- Doesn't provide extension API documentation (VS Code API only)

---

## 10. Cloud Agents

### The Mechanism

Remote execution with persistent state:

**How It Works**:
1. Submit task to Cursor Cloud
2. Cloud agent executes autonomously
3. State persists between turns
4. Results streamed back to local IDE
5. Can resume interrupted tasks

### What Cursor Does

- **Submits** tasks to remote agents
- **Maintains** session state in cloud
- **Streams** results to local IDE
- **Handles** resource constraints
- **Provides** resumption tokens

### What Cursor Does NOT Do

- Doesn't offer free cloud agent quotas
- Doesn't provide observability into cloud execution
- Doesn't support custom cloud environment setup
- Doesn't expose cloud agent logs
- Doesn't support collaborative cloud agents

---

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

