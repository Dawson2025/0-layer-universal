---
resource_id: "fff32592-583c-474c-934c-57eb12ae06da"
resource_type: "output"
resource_name: "NATIVE_FEATURES"
---
# Codex CLI — Native Features

**Date**: 2026-02-27
**Focus**: What Codex provides natively (the mechanisms)

---

## Overview

Codex CLI's native context system provides these built-in mechanisms:

1. **Three-level AGENTS.md hierarchy** (global → project → directory)
2. **config.toml shared configuration** (workspace settings)
3. **Session persistence** (conversation history resumption)
4. **IDE extensions** (VS Code, Cursor, Windsurf integration)
5. **Context window management** (token budgeting with awareness)
6. **Model selection** (choice of Codex models with reasoning effort)
7. **Model Context Protocol (MCP)** (external tool/API integration)
8. **GitHub integration** (repo-based initialization and workspace setup)
9. **Cloud workspace platform** (synchronized project state)

---

## 1. Three-Level AGENTS.md Hierarchy

### The Mechanism

Codex automatically loads AGENTS.md files in three-level cascade:

```
~/.codex/AGENTS.md (global, highest priority)
  ↓
/project/AGENTS.md (project-specific)
  ↓
/workspace/subdir/AGENTS.md (workspace/directory-specific, lowest priority)
```

### What Codex Does

- **Reads** all AGENTS.md files found in hierarchy
- **Merges** them (later entries override earlier)
- **Injects** into system context at session start
- **Reloads** on directory change
- **No user action required** — automatic discovery and cascade

### What Codex Does NOT Do

- Doesn't create AGENTS.md files (you must create them)
- Doesn't validate structure (any markdown is acceptable)
- Doesn't enforce naming conventions (you decide)
- Doesn't manage content (you decide what to include)
- Doesn't auto-backup AGENTS.md (you manage versioning)

---

## 2. Config.toml Shared Configuration

### The Mechanism

Codex reads workspace-wide settings from `config.toml`:

**Global**: `~/.codex/config.toml` (applies to all workspaces)
**Project**: `/project/config.toml` (applies to this project only)

### What Codex Does

- **Discovers** config.toml in project root
- **Parses** TOML format (validated structure)
- **Applies** settings: model, temperature, max_tokens, reasoning_effort, context_window
- **Merges** with global config (project overrides global)
- **Reloads** on config file change

### Settings Available

| Setting | Type | Default | Purpose |
|---------|------|---------|---------|
| `model` | string | "codex-opus" | Which Codex model to use |
| `temperature` | float (0.0-2.0) | 0.7 | Sampling temperature (creativity) |
| `max_tokens` | int | 4096 | Max response length |
| `reasoning_effort` | string | "medium" | Reasoning depth (low/medium/high) |
| `context_window` | string | "128k" | Input context limit (128k/256k/1m) |
| `session_persistence` | bool | true | Save/resume conversations |
| `github_integration` | bool | true | Link to GitHub repos |

### What Codex Does NOT Do

- Doesn't validate config values (accepts invalid settings)
- Doesn't enforce limits (respects but doesn't block overages)
- Doesn't auto-update config (manual edits required)
- Doesn't manage secrets (you store API keys separately)

---

## 3. Session Persistence

### The Mechanism

Codex automatically saves and restores conversation state:

**Save Location**: `~/.codex/sessions/[project-id]/` (JSONL format)

**Each Session**:
- Conversation history (all turns)
- Model state (last model used)
- Settings snapshot (config at time of session)
- Timestamps (created, last accessed)

**On Resumption**:
- Codex loads session history
- Restores context
- Allows continuing previous conversation

### What Codex Does

- **Creates** new session directory on project init
- **Appends** turn records (never overwrites)
- **Persists** full conversation (JSONL format)
- **Enables** resumption via `codex resume [session-id]`
- **Maintains** session metadata (duration, turn count)
- **Indexes** sessions for quick lookup

### What Codex Does NOT Do

- Doesn't auto-cleanup old sessions (manual deletion required)
- Doesn't compress old conversations (raw JSONL stored)
- Doesn't encrypt session files (plain text, handle carefully)
- Doesn't share sessions across users (per-user ~/.codex/)
- Doesn't limit session size (no automatic archival)

---

## 4. IDE Extensions

### The Mechanism

Codex integrates with three major IDEs via native extensions:

```
VS Code Extension (marketplace: codex-vscode)
  ↓
Reads: AGENTS.md + config.toml
↓
Shows inline completions, chat sidebar, command palette

Cursor IDE (built-in Codex integration)
  ↓
Reads: .cursor/rules (native Cursor format) + config.toml
↓
Enhanced with semantic search, embeddings, Memory Bank

Windsurf IDE (emerging Codex integration)
  ↓
Reads: AGENTS.md + config.toml
↓
Agent-first interface, Flow mode (agentic execution)
```

### What Codex Does

- **Discovers** IDE environment (VS Code, Cursor, Windsurf)
- **Loads** appropriate config/rules for IDE
- **Provides** IDE-specific UX (inline completions, sidebars, command palette)
- **Syncs** state between CLI and IDE
- **Respects** IDE-specific context (currently open file, selection, line number)

### What Codex Does NOT Do

- Doesn't modify IDE keyboard shortcuts (IDE manages keybindings)
- Doesn't install extensions (user manages extension marketplace)
- Doesn't update IDE versions (user manages IDE updates)
- Doesn't control IDE theme/appearance (IDE manages UI)

---

## 5. Context Window Management

### The Mechanism

Codex tracks token usage and manages context windows:

**Default Context Window**: 128,000 input tokens
**Expandable**: Up to 1,000,000 tokens (with `context_window: "1m"` in config)

**What Fills Context**:
- AGENTS.md (all three levels)
- config.toml settings
- Conversation history (turns in session)
- File contents (if user references files)
- IDE context (current file, selection)
- Tool outputs (from MCP calls)
- System prompt overhead

### What Codex Does

- **Counts** tokens as context fills
- **Monitors** approaching limit (warns at 80%)
- **Truncates** old conversation turns when full
- **Reports** usage via `/context` command
- **Adjusts** model behavior based on window size

### What Codex Does NOT Do

- Doesn't have auto-compaction (manually manages via truncation)
- Doesn't prioritize content (FIFO truncation from oldest)
- Doesn't predict future usage (reacts to current state)
- Doesn't control model choice based on window (user decides)

---

## 6. Model Selection

### The Mechanism

Codex provides multiple models with different capabilities:

**Available Models** (as of 2026-02):

| Model | Context | Reasoning | Speed | Cost | Use Case |
|-------|---------|-----------|-------|------|----------|
| codex-opus | 200K | Very High | Slow | $$$ | Complex analysis, research |
| codex-sonnet | 128K | High | Fast | $$ | General coding, chat |
| codex-haiku | 128K | Medium | Very Fast | $ | Quick questions, lightweight tasks |

**Reasoning Effort Levels** (for Opus/Sonnet):

| Level | Depth | Time | Cost | When to Use |
|-------|-------|------|------|-------------|
| low | Surface analysis | <5s | Standard | Quick questions |
| medium | Standard reasoning | 10-30s | 2x | Most tasks |
| high | Deep chain-of-thought | 30-120s | 4x | Complex problems, math, logic |

### What Codex Does

- **Accepts** model selection via CLI flag (`--model codex-opus`)
- **Applies** reasoning_effort from config.toml
- **Enforces** context window limits per model
- **Routes** requests to correct backend (API endpoint)
- **Reports** token usage and cost estimates

### What Codex Does NOT Do

- Doesn't auto-select models (user decides)
- Doesn't manage billing (you track costs separately)
- Doesn't limit model changes mid-session (allowed)
- Doesn't validate reasoning_effort for model (assumes valid)

---

## 7. Model Context Protocol (MCP)

### The Mechanism

MCP servers extend Codex with external tools:

```
Codex CLI
  ↓ (calls)
MCP Server
  ├─ Tool 1 (e.g., read_file)
  ├─ Tool 2 (e.g., execute_bash)
  └─ Tool 3 (e.g., api_call)
  ↓ (returns results)
Codex receives tool outputs in context
```

### What Codex Does

- **Discovers** available MCP servers (from config)
- **Lists** tools provided by each server
- **Invokes** tools when user/model requests them
- **Streams** results back into context
- **Manages** tool failures and timeouts (30s default)

### What Codex Does NOT Do

- Doesn't create MCP servers (requires separate setup)
- Doesn't manage server installation (you install separately)
- Doesn't validate tool safety (relies on MCP spec)
- Doesn't cache tool results (fresh call each time)

---

## 8. GitHub Integration

### The Mechanism

Codex can initialize and sync with GitHub repositories:

**Initialization**:
```bash
codex init https://github.com/user/repo
  ↓
Creates project structure
Creates config.toml
Links to GitHub workspace
```

**Synchronization**:
- Codex can read git status, branches, commits
- Can analyze pull requests
- Can integrate commit history
- Syncs workspace state to GitHub (optional)

### What Codex Does

- **Accepts** GitHub URLs for project init
- **Clones** repo to local workspace
- **Creates** `.codex/` directory structure
- **Links** local state to GitHub project
- **Enables** git-aware context (branch info, recent commits)

### What Codex Does NOT Do

- Doesn't manage git commands (user runs `git` directly)
- Doesn't auto-commit changes (manual commit required)
- Doesn't create pull requests (user creates via GitHub)
- Doesn't handle authentication (assumes git auth configured)

---

## 9. Cloud Workspace Platform

### The Mechanism

Codex's cloud platform synchronizes project state:

**Web Dashboard**: `https://cloud.codex.ai/workspaces`

**Synchronization**:
- Project metadata synced to cloud
- Session history available on cloud (with permission)
- Conversation history persistent across devices
- Workspace settings synced (config.toml)

### What Codex Does

- **Maintains** cloud workspace account
- **Syncs** metadata to cloud infrastructure
- **Enables** cross-device resumption (login elsewhere, resume session)
- **Provides** web dashboard for workspace management
- **Stores** conversation history on cloud (encrypted)

### What Codex Does NOT Do

- Doesn't sync local files automatically (CLI only)
- Doesn't store code on cloud (only metadata/settings)
- Doesn't require cloud (CLI works fully offline)
- Doesn't manage cloud authentication (user manages login)

---

## 10. Commands (Native to Codex)

| Command | What Codex Does |
|---------|-----------------|
| `codex init [url]` | Initialize new project (with optional GitHub repo) |
| `codex resume [session-id]` | Resume previous conversation |
| `codex list-sessions` | Show available sessions |
| `codex config` | View/edit config.toml |
| `codex context` | Show token usage breakdown |
| `codex status` | Show workspace status, model, reasoning_effort |
| `codex model [name]` | Switch model for current session |
| `codex reasoning [low\|medium\|high]` | Set reasoning effort for this session |

---

## Summary: Native = Mechanisms Provided

Codex provides **mechanisms** (how things work), not **policies** (what to do with them):

✅ **Native**: Three-level AGENTS.md cascade loads automatically
❌ **Not native**: You decide what content goes in AGENTS.md

✅ **Native**: config.toml settings are parsed and applied
❌ **Not native**: You decide what settings to configure

✅ **Native**: Session history persists automatically
❌ **Not native**: You decide when to resume or start new sessions

✅ **Native**: IDE extensions integrate with Codex
❌ **Not native**: You install/update extensions

✅ **Native**: Models and reasoning_effort available
❌ **Not native**: You choose which model and reasoning level

✅ **Native**: MCP servers connect and provide tools
❌ **Not native**: You install/configure MCP servers

✅ **Native**: GitHub integration available
❌ **Not native**: You link your repositories and manage git

---

## Key Differences from Claude Code CLI

| Feature | Claude Code CLI | Codex CLI |
|---------|-----------------|-----------|
| Config file | CLAUDE.md (markdown) | config.toml (TOML) |
| Context hierarchy | CLAUDE.md cascade | AGENTS.md three-level |
| Session persistence | Built-in, automatic | Built-in, automatic |
| IDE integration | MCP-based | Native extensions |
| Model selection | Via CLI, system prompt | Via config.toml, setting |
| Token limits | 200K default, expandable | 128K default, up to 1M |
| Auto-compaction | Yes (at 90%) | No (FIFO truncation) |
| Cloud platform | None | Built-in workspace sync |

