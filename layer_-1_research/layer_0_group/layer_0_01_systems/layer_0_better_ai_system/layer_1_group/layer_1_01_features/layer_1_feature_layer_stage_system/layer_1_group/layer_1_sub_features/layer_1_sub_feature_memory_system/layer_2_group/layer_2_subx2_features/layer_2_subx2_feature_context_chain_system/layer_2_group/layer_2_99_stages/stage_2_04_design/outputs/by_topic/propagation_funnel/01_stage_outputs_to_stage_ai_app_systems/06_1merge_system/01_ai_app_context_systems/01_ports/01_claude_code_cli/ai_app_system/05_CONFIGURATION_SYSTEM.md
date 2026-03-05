---
resource_id: "ebd0310b-8bdb-4267-a38f-775d26fbce11"
resource_type: "output"
resource_name: "05_CONFIGURATION_SYSTEM"
---
# Claude Code CLI — Configuration System and Files

**Date**: 2026-02-28
**Focus**: All configuration files, settings, and how they work together

---

<!-- section_id: "34cb1528-766d-4f4a-8f25-7c81c10dfb8f" -->
## Configuration Files Overview

Claude Code CLI uses several configuration files across different levels. Here's the complete system:

```
~/.claude/
├── CLAUDE.md                    ← Context/rules (loaded first)
├── settings.json                ← Global settings (applied globally)
├── keybindings.json            ← Keyboard shortcuts (applies to CLI)
│
└── projects/
    └── [PROJECT_HASH]/
        ├── CLAUDE.md            ← Project context (overrides global)
        ├── 0INDEX.md            ← Current state tracking
        └── status.json          ← Project metadata
```

---

<!-- section_id: "4f45200c-2b0a-4e31-a8ed-4121de89dc93" -->
## 1. CLAUDE.md (Context Configuration)

**Location**: `~/.claude/CLAUDE.md` + `~/.claude/projects/[HASH]/CLAUDE.md` + `[DIR]/CLAUDE.md`

**What It Is**: Markdown file containing rules, triggers, resources, skills

**What It Does**:
- Defines what Claude should do and when
- Lists available skills and triggers for invoking them
- Specifies resources (where to find files, knowledge, protocols)
- Provides current status and context

**Format**: Markdown (no strict schema, but conventional sections):

```markdown
# [Project] Claude Code Configuration

## [CRITICAL] Rules
- Rule 1
- Rule 2

## Triggers
| Situation | Action |
|-----------|--------|
| User says X | Load Y file |

## Skills
| Skill | When to Use |
|-------|------------|
| /skill-name | Use when... |

## Resources
| Resource | Location |
|----------|----------|
| Docs | path/to/docs |

## Current Status
[Brief summary of project state]
```

**Loaded**: Automatically, via cascade (see `04_CLAUDE_FILE_PATH_RULES.md`)

---

<!-- section_id: "80017cf8-9c00-4f1c-a9e1-0e0718dc6b88" -->
## 2. settings.json (Global Settings)

**Location**: `~/.claude/settings.json`

**What It Is**: JSON configuration file for Claude Code CLI

**What It Does**: Controls global behavior, models, context windows, MCP servers

**Format**:

```json
{
  "version": "1.0",
  "context_window": "200k",
  "default_model": "claude-opus-4-6",
  "auto_memory_enabled": true,
  "auto_memory_disable_env": "CLAUDE_CODE_DISABLE_AUTO_MEMORY",
  "memory_lines_loaded": 200,
  "compaction_threshold": 0.9,
  "history_format": "jsonl",
  "mcp_servers": [
    {
      "name": "canvas",
      "type": "python",
      "command": "python -m mcp_servers.canvas",
      "env": {
        "CANVAS_API_KEY": "${env:CANVAS_API_KEY}",
        "CANVAS_DOMAIN": "canvas.instructure.com"
      }
    }
  ],
  "keybindings": {
    "submit": "enter",
    "split_line": "shift+enter",
    "context": "ctrl+shift+c",
    "memory": "ctrl+shift+m"
  }
}
```

**Key Settings**:

| Setting | Type | Default | Purpose |
|---------|------|---------|---------|
| `context_window` | string | "200k" | Input context limit (128k, 200k, 1m) |
| `default_model` | string | "claude-opus-4-6" | Model to use by default |
| `auto_memory_enabled` | bool | true | Auto-load MEMORY.md first 200 lines |
| `memory_lines_loaded` | int | 200 | How many lines of MEMORY.md to auto-load |
| `compaction_threshold` | float | 0.9 | When to trigger auto-compaction (90%) |
| `history_format` | string | "jsonl" | Conversation history format |
| `mcp_servers` | array | [] | MCP servers to connect |

**Loaded**: Once at session start

**Edited**: Manually (or via `/settings` command if available)

---

<!-- section_id: "1c8e6308-bf5f-4da0-bd1e-6c4ebe59f61a" -->
## 3. keybindings.json (Keyboard Shortcuts)

**Location**: `~/.claude/keybindings.json`

**What It Is**: JSON mapping of keyboard shortcuts to commands

**What It Does**: Defines how to invoke commands via keyboard in Claude Code CLI

**Format**:

```json
{
  "keybindings": [
    {
      "key": "enter",
      "command": "submit-message",
      "when": "terminal_focused"
    },
    {
      "key": "shift+enter",
      "command": "new-line",
      "when": "terminal_focused"
    },
    {
      "key": "ctrl+shift+c",
      "command": "show-context",
      "when": "terminal_focused"
    },
    {
      "key": "ctrl+shift+m",
      "command": "show-memory",
      "when": "terminal_focused"
    },
    {
      "key": "ctrl+k",
      "command": "clear-screen",
      "when": "terminal_focused"
    }
  ]
}
```

**Common Keybindings**:

| Key | Command | Purpose |
|-----|---------|---------|
| `enter` | submit-message | Send message to Claude |
| `shift+enter` | new-line | Break message into multiple lines |
| `ctrl+shift+c` | show-context | Display context window breakdown |
| `ctrl+shift+m` | show-memory | Show MEMORY.md (with file selector) |
| `ctrl+k` | clear-screen | Clear terminal |
| `ctrl+c` | cancel | Cancel current operation |

**Loaded**: At session start

**Edited**: Via `/keybindings-help` command or manually in JSON file

---

<!-- section_id: "ba1b18d8-afb9-4819-b7c0-7d5deb33f19a" -->
## 4. status.json (Project Metadata)

**Location**: `~/.claude/projects/[HASH]/status.json`

**What It Is**: JSON file tracking project state

**What It Does**: Records project metadata for session resumption and tracking

**Format**:

```json
{
  "project_hash": "a1b2c3d4e5f6",
  "working_directory": "/home/user/project",
  "created_at": "2026-02-28T10:30:00Z",
  "last_accessed": "2026-02-28T14:45:00Z",
  "last_session_id": "session-001",
  "model_last_used": "claude-opus-4-6",
  "context_window_last_used": "200k",
  "total_turns": 42,
  "total_tokens_used": 185000,
  "memory_version": "1.0",
  "git_status": {
    "repo": "git@github.com:user/project.git",
    "branch": "main",
    "commit": "abc123def456"
  }
}
```

**Updated**: Automatically after each session

**Used**: For session resumption, project history, statistics

---

<!-- section_id: "053f9eca-0508-43bc-afb1-69934e588460" -->
## 5. 0INDEX.md (Current State Tracking)

**Location**: `~/.claude/projects/[HASH]/0INDEX.md`

**What It Is**: Markdown file for tracking project state

**What It Does**: Provides human-readable project status and quick navigation

**Format**:

```markdown
# Project State Index

**Project**: Example Project
**Hash**: a1b2c3d4e5f6
**Last Updated**: 2026-02-28 14:45 UTC
**Status**: In Progress

## Current Focus
- Working on feature X
- Debugging issue Y

## Session History
- Session 001 (2026-02-26): Initial setup
- Session 002 (2026-02-27): Implementation
- Session 003 (2026-02-28): Bug fixes

## Quick Links
- CLAUDE.md: ~/.claude/projects/[HASH]/CLAUDE.md
- MEMORY.md: ~/.claude/projects/[HASH]/memory/MEMORY.md
- History: ~/.claude/projects/[HASH]/history.jsonl

## Recent Changes
- Updated MEMORY.md (2026-02-28)
- Fixed bug in feature X (2026-02-27)
```

**Updated**: Manually (not automatic)

**Purpose**: Quick reference for project state across sessions

---

<!-- section_id: "a3833123-b62f-411f-9086-2ea1a645a16e" -->
## 6. history.jsonl (Conversation History)

**Location**: `~/.claude/projects/[HASH]/history.jsonl`

**What It Is**: JSON Lines file (one JSON object per line)

**What It Does**: Persists all conversation turns, enabling session resumption

**Format** (one line per turn):

```json
{"turn": 1, "timestamp": "2026-02-28T10:30:00Z", "role": "user", "content": "Hello", "tokens": 10}
{"turn": 1, "timestamp": "2026-02-28T10:30:05Z", "role": "assistant", "content": "Hi! How can I help?", "tokens": 15}
{"turn": 2, "timestamp": "2026-02-28T10:30:30Z", "role": "user", "content": "Show me /context", "tokens": 12}
{"turn": 2, "timestamp": "2026-02-28T10:30:35Z", "role": "assistant", "content": "Current context: ...", "tokens": 200}
```

**Appended**: After each turn (never overwritten)

**Size**: Can grow large over time (archive periodically)

**Privacy**: Stored locally, never uploaded to Anthropic

---

<!-- section_id: "558f21ca-bfc5-404b-a291-8059ce6f365b" -->
## 7. MCP Server Configuration

MCP (Model Context Protocol) servers are configured in `settings.json`:

**What MCP Servers Do**: Provide external tools (Canvas API, GitHub, databases, etc.)

**Configuration**:

```json
{
  "mcp_servers": [
    {
      "name": "canvas",
      "type": "python",
      "command": "python -m mcp_servers.canvas",
      "env": {
        "CANVAS_API_KEY": "${env:CANVAS_API_KEY}",
        "CANVAS_DOMAIN": "canvas.instructure.com"
      },
      "enabled": true
    },
    {
      "name": "github",
      "type": "node",
      "command": "npx @github/mcp-server-github",
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
      },
      "enabled": true
    }
  ]
}
```

**Environment Variables**: Use `${env:VARIABLE_NAME}` syntax

**Tool Discovery**: Claude Code automatically lists available tools from each MCP server

**Usage**: Tools are available within conversations (Claude Code calls them automatically when needed)

---

<!-- section_id: "69277923-f113-4da1-be5a-1ef7c2207d3d" -->
## Configuration Hierarchy and Override

Settings follow a hierarchy with later values overriding earlier:

```
Defaults (built-in)
  ↓ (overridden by)
~/.claude/settings.json (global)
  ↓ (overridden by)
~/.claude/projects/[HASH]/settings.json (project-specific, if exists)
  ↓ (overridden by)
CLI flags (command-line arguments)

Result: Final effective settings
```

**Example**:
- Global: `context_window: 128k`
- Project override: `context_window: 200k`
- CLI flag: `--context-window 1m`
- **Result**: 1M context window used

---

<!-- section_id: "5c41c503-1431-43a1-9fd6-89b07e6eade7" -->
## How to Modify Configuration

<!-- section_id: "587d84fa-30e7-4bf7-913d-15046d9f8837" -->
### Method 1: Edit JSON Files Directly

```bash
# Edit global settings
nano ~/.claude/settings.json

# Edit project-specific status
nano ~/.claude/projects/[HASH]/status.json
```

<!-- section_id: "20b3f916-556b-4833-b415-d69506f41707" -->
### Method 2: Use CLI Commands

```bash
# View context breakdown
claude /context

# View project memory (with file selector)
claude /memory

# View/edit keybindings
claude /keybindings-help

# View current settings
claude /settings
```

<!-- section_id: "6978bed6-98b5-4e2b-a1da-70ddc0fbfe8a" -->
### Method 3: Update via MEMORY.md

```bash
# Use /remember to update MEMORY.md
/remember: Add important note about project state
```

---

<!-- section_id: "ad7cdb02-35b4-42b3-bdcf-6de643f4d9cd" -->
## Best Practices

<!-- section_id: "ebba09cc-65b5-44db-a668-d8def39bf8cf" -->
### 1. Keep Global settings.json Lean

```json
{
  "context_window": "200k",
  "default_model": "claude-opus-4-6",
  "mcp_servers": [...]
}
```

Only include universal settings. Project-specific overrides go in project CLAUDE.md.

<!-- section_id: "a3349772-f674-4035-902e-c15955d4c044" -->
### 2. Document Configuration in CLAUDE.md

```markdown
## Configuration

- Context Window: 200K tokens
- Default Model: Claude Opus 4.6
- MCP Servers: Canvas, GitHub
- Auto-Memory: Enabled (200 lines)
```

<!-- section_id: "ffe35d72-d311-4738-acf3-49162c50e4bf" -->
### 3. Use Environment Variables for Secrets

```json
{
  "mcp_servers": [
    {
      "env": {
        "API_KEY": "${env:MY_API_KEY}"
      }
    }
  ]
}
```

Never hardcode API keys in configuration files.

<!-- section_id: "c002d887-19e1-480e-aa9e-e5410d1f83c7" -->
### 4. Archive Old history.jsonl Files

```bash
# After a project reaches 1M tokens, archive history
mv ~/.claude/projects/[HASH]/history.jsonl history.jsonl.2026-02

# Start fresh for new session
```

<!-- section_id: "b4390d5b-1803-4825-9aa8-4e0c0af559da" -->
### 5. Update status.json Manually

After significant work, update `status.json` to reflect progress:

```json
{
  "last_accessed": "2026-02-28T16:00:00Z",
  "total_turns": 50,
  "total_tokens_used": 245000
}
```

---

<!-- section_id: "2cd23df4-1e0c-4501-951e-493fbd39e909" -->
## Summary: Configuration System

✅ **CLAUDE.md**: Context, rules, triggers, skills (per level: global → project → directory)
✅ **settings.json**: Global settings, models, context windows, MCP servers
✅ **keybindings.json**: Keyboard shortcuts for CLI commands
✅ **status.json**: Project metadata, statistics, state
✅ **0INDEX.md**: Human-readable project state tracking
✅ **history.jsonl**: Complete conversation history (auto-appended)

All files work together to provide a complete, flexible configuration system for Claude Code CLI.
