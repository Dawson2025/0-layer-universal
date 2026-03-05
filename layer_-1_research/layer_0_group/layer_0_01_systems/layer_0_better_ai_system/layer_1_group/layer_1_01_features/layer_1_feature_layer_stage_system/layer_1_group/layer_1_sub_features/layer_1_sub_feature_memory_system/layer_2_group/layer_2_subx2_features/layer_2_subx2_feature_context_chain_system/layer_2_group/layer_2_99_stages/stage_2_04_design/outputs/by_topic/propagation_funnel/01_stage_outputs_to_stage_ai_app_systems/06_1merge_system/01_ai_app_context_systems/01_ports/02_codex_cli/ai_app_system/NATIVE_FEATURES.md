---
resource_id: "fff32592-583c-474c-934c-57eb12ae06da"
resource_type: "output"
resource_name: "NATIVE_FEATURES"
---
# Codex CLI — Native Features

**Date**: 2026-02-27
**Focus**: What Codex provides natively (the mechanisms)

---

<!-- section_id: "eb0db669-c4c8-47ad-bb37-05343e6d1a70" -->
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

<!-- section_id: "589d6a85-13de-43de-bd80-3a334c2e10af" -->
## 1. Three-Level AGENTS.md Hierarchy

<!-- section_id: "0ed54035-30b3-4838-8f1c-a2e09980d734" -->
### The Mechanism

Codex automatically loads AGENTS.md files in three-level cascade:

```
~/.codex/AGENTS.md (global, highest priority)
  ↓
/project/AGENTS.md (project-specific)
  ↓
/workspace/subdir/AGENTS.md (workspace/directory-specific, lowest priority)
```

<!-- section_id: "cd40ade7-6037-48fc-b5b2-98ce7403ff6e" -->
### What Codex Does

- **Reads** all AGENTS.md files found in hierarchy
- **Merges** them (later entries override earlier)
- **Injects** into system context at session start
- **Reloads** on directory change
- **No user action required** — automatic discovery and cascade

<!-- section_id: "8670864d-6ea6-40f6-9c04-0f36b015fdd7" -->
### What Codex Does NOT Do

- Doesn't create AGENTS.md files (you must create them)
- Doesn't validate structure (any markdown is acceptable)
- Doesn't enforce naming conventions (you decide)
- Doesn't manage content (you decide what to include)
- Doesn't auto-backup AGENTS.md (you manage versioning)

---

<!-- section_id: "9cbae3a7-e5e2-4573-a1c6-1a38c4bde036" -->
## 2. Config.toml Shared Configuration

<!-- section_id: "82428f1f-2007-4e8c-b8aa-9276e0d263c4" -->
### The Mechanism

Codex reads workspace-wide settings from `config.toml`:

**Global**: `~/.codex/config.toml` (applies to all workspaces)
**Project**: `/project/config.toml` (applies to this project only)

<!-- section_id: "18710fdb-2cd6-4799-a7af-25c7d262a5db" -->
### What Codex Does

- **Discovers** config.toml in project root
- **Parses** TOML format (validated structure)
- **Applies** settings: model, temperature, max_tokens, reasoning_effort, context_window
- **Merges** with global config (project overrides global)
- **Reloads** on config file change

<!-- section_id: "5f3357a7-9600-485c-b2c6-5ea1dbffc3bc" -->
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

<!-- section_id: "14f1e3a1-9332-4531-8b93-c472b64fb6ef" -->
### What Codex Does NOT Do

- Doesn't validate config values (accepts invalid settings)
- Doesn't enforce limits (respects but doesn't block overages)
- Doesn't auto-update config (manual edits required)
- Doesn't manage secrets (you store API keys separately)

---

<!-- section_id: "66a523df-6ee9-43de-b8a8-5fb333173737" -->
## 3. Session Persistence

<!-- section_id: "fd5d53c2-6395-4af9-be48-d3ae7d7b53d8" -->
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

<!-- section_id: "cb91a0b3-fbf6-4f02-bb6e-6a64af7f8c5c" -->
### What Codex Does

- **Creates** new session directory on project init
- **Appends** turn records (never overwrites)
- **Persists** full conversation (JSONL format)
- **Enables** resumption via `codex resume [session-id]`
- **Maintains** session metadata (duration, turn count)
- **Indexes** sessions for quick lookup

<!-- section_id: "4c5fcdb1-d5c0-43d8-8fa2-f7bc957ef039" -->
### What Codex Does NOT Do

- Doesn't auto-cleanup old sessions (manual deletion required)
- Doesn't compress old conversations (raw JSONL stored)
- Doesn't encrypt session files (plain text, handle carefully)
- Doesn't share sessions across users (per-user ~/.codex/)
- Doesn't limit session size (no automatic archival)

---

<!-- section_id: "fec6694b-b344-4dea-911d-64b83a0a7783" -->
## 4. IDE Extensions

<!-- section_id: "96ce04fb-59f9-4f06-adbf-886d363d13dc" -->
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

<!-- section_id: "0b66d950-3527-42f2-bd6c-b193e73b51d1" -->
### What Codex Does

- **Discovers** IDE environment (VS Code, Cursor, Windsurf)
- **Loads** appropriate config/rules for IDE
- **Provides** IDE-specific UX (inline completions, sidebars, command palette)
- **Syncs** state between CLI and IDE
- **Respects** IDE-specific context (currently open file, selection, line number)

<!-- section_id: "78d5dd06-20cb-4cce-8a08-5108544a631c" -->
### What Codex Does NOT Do

- Doesn't modify IDE keyboard shortcuts (IDE manages keybindings)
- Doesn't install extensions (user manages extension marketplace)
- Doesn't update IDE versions (user manages IDE updates)
- Doesn't control IDE theme/appearance (IDE manages UI)

---

<!-- section_id: "041c6601-955b-42bc-a9b3-963698a3fa55" -->
## 5. Context Window Management

<!-- section_id: "06daadea-9a51-404b-b22e-da7ed6e80e32" -->
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

<!-- section_id: "c183eefb-a81b-4179-93da-fbf1fb3e3feb" -->
### What Codex Does

- **Counts** tokens as context fills
- **Monitors** approaching limit (warns at 80%)
- **Truncates** old conversation turns when full
- **Reports** usage via `/context` command
- **Adjusts** model behavior based on window size

<!-- section_id: "d1abcf45-f671-44f1-8c80-b4eb610a07e4" -->
### What Codex Does NOT Do

- Doesn't have auto-compaction (manually manages via truncation)
- Doesn't prioritize content (FIFO truncation from oldest)
- Doesn't predict future usage (reacts to current state)
- Doesn't control model choice based on window (user decides)

---

<!-- section_id: "15de6ba5-863c-4cf7-8655-ad5589ddb9fa" -->
## 6. Model Selection

<!-- section_id: "6d43c055-fe43-4bdb-aff6-4c1d5f29edeb" -->
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

<!-- section_id: "201f8086-4b35-45e5-aefe-f3259061afd6" -->
### What Codex Does

- **Accepts** model selection via CLI flag (`--model codex-opus`)
- **Applies** reasoning_effort from config.toml
- **Enforces** context window limits per model
- **Routes** requests to correct backend (API endpoint)
- **Reports** token usage and cost estimates

<!-- section_id: "dae17d5c-9dbe-4a0a-ac33-e93c26660d82" -->
### What Codex Does NOT Do

- Doesn't auto-select models (user decides)
- Doesn't manage billing (you track costs separately)
- Doesn't limit model changes mid-session (allowed)
- Doesn't validate reasoning_effort for model (assumes valid)

---

<!-- section_id: "44d62e13-3138-4a68-9bd3-abf179d8ae77" -->
## 7. Model Context Protocol (MCP)

<!-- section_id: "6175a5f7-2704-4b08-a728-a22f40d18f09" -->
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

<!-- section_id: "5bcc491c-1bfa-4464-a20a-80fd9e79fdf3" -->
### What Codex Does

- **Discovers** available MCP servers (from config)
- **Lists** tools provided by each server
- **Invokes** tools when user/model requests them
- **Streams** results back into context
- **Manages** tool failures and timeouts (30s default)

<!-- section_id: "77871025-0c1e-4e96-96e0-3f746f2b1926" -->
### What Codex Does NOT Do

- Doesn't create MCP servers (requires separate setup)
- Doesn't manage server installation (you install separately)
- Doesn't validate tool safety (relies on MCP spec)
- Doesn't cache tool results (fresh call each time)

---

<!-- section_id: "fd83e3b6-fafe-4e33-9c49-be291154f49e" -->
## 8. GitHub Integration

<!-- section_id: "d794526a-dccd-4b30-8c19-32fa2b298180" -->
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

<!-- section_id: "0a25a15c-0b0f-4c50-b91f-56f9a2039956" -->
### What Codex Does

- **Accepts** GitHub URLs for project init
- **Clones** repo to local workspace
- **Creates** `.codex/` directory structure
- **Links** local state to GitHub project
- **Enables** git-aware context (branch info, recent commits)

<!-- section_id: "dbd18925-7043-4645-97ca-65f60ceb43d0" -->
### What Codex Does NOT Do

- Doesn't manage git commands (user runs `git` directly)
- Doesn't auto-commit changes (manual commit required)
- Doesn't create pull requests (user creates via GitHub)
- Doesn't handle authentication (assumes git auth configured)

---

<!-- section_id: "88d99a2b-2e56-4da7-9337-dd317b9b4636" -->
## 9. Cloud Workspace Platform

<!-- section_id: "949da718-7657-4c8a-84ef-5e0fdeb32c6c" -->
### The Mechanism

Codex's cloud platform synchronizes project state:

**Web Dashboard**: `https://cloud.codex.ai/workspaces`

**Synchronization**:
- Project metadata synced to cloud
- Session history available on cloud (with permission)
- Conversation history persistent across devices
- Workspace settings synced (config.toml)

<!-- section_id: "be26a435-c8c5-43ac-b4c3-4eceab3d6eab" -->
### What Codex Does

- **Maintains** cloud workspace account
- **Syncs** metadata to cloud infrastructure
- **Enables** cross-device resumption (login elsewhere, resume session)
- **Provides** web dashboard for workspace management
- **Stores** conversation history on cloud (encrypted)

<!-- section_id: "d4d5f8ea-a18a-4abb-ab21-df17709e5d36" -->
### What Codex Does NOT Do

- Doesn't sync local files automatically (CLI only)
- Doesn't store code on cloud (only metadata/settings)
- Doesn't require cloud (CLI works fully offline)
- Doesn't manage cloud authentication (user manages login)

---

<!-- section_id: "6116f086-a6f0-43c1-86ba-381de9a130ca" -->
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

<!-- section_id: "fc3a9eb1-664a-4975-8c3a-cb0fda57e6c5" -->
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

<!-- section_id: "c770d2b7-bb73-4b72-8bc5-89218d47907b" -->
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

