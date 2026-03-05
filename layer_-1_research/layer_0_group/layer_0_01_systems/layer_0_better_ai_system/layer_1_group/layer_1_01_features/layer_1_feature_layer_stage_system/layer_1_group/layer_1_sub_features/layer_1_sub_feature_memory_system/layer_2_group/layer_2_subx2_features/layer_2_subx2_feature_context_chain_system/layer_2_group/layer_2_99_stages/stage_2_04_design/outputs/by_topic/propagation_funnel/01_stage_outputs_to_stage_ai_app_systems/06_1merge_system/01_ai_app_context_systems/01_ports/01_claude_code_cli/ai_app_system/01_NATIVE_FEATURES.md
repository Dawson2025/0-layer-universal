---
resource_id: "1abf5025-e648-49e6-80ce-448b3c724ec0"
resource_type: "output"
resource_name: "01_NATIVE_FEATURES"
---
# Codex CLI — Native Features

**Date**: 2026-02-27
**Focus**: What Codex provides natively (the mechanisms)

---

<!-- section_id: "5d142bcf-5c95-46f7-90b6-01f09800326d" -->
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

<!-- section_id: "4d70ff5d-518b-48c1-beee-a4f14900bd8b" -->
## 1. Three-Level AGENTS.md Hierarchy

<!-- section_id: "039b8cfe-5d00-4f9a-85ef-06a756b93586" -->
### The Mechanism

Codex automatically loads AGENTS.md files in three-level cascade:

```
~/.codex/AGENTS.md (global, highest priority)
  ↓
/project/AGENTS.md (project-specific)
  ↓
/workspace/subdir/AGENTS.md (workspace/directory-specific, lowest priority)
```

<!-- section_id: "8c37aa18-e976-44a2-afc4-5ac8dfcc1c47" -->
### What Codex Does

- **Reads** all AGENTS.md files found in hierarchy
- **Merges** them (later entries override earlier)
- **Injects** into system context at session start
- **Reloads** on directory change
- **No user action required** — automatic discovery and cascade

<!-- section_id: "cc915633-3926-4bcb-b5e8-33ebe592ad52" -->
### What Codex Does NOT Do

- Doesn't create AGENTS.md files (you must create them)
- Doesn't validate structure (any markdown is acceptable)
- Doesn't enforce naming conventions (you decide)
- Doesn't manage content (you decide what to include)
- Doesn't auto-backup AGENTS.md (you manage versioning)

---

<!-- section_id: "de5d8724-5b2c-4aec-ad0d-b9457f5df29d" -->
## 2. Config.toml Shared Configuration

<!-- section_id: "d4d34105-90da-4308-92c2-5267f1905381" -->
### The Mechanism

Codex reads workspace-wide settings from `config.toml`:

**Global**: `~/.codex/config.toml` (applies to all workspaces)
**Project**: `/project/config.toml` (applies to this project only)

<!-- section_id: "685dcc37-d9bc-4508-a43f-b1ca21661119" -->
### What Codex Does

- **Discovers** config.toml in project root
- **Parses** TOML format (validated structure)
- **Applies** settings: model, temperature, max_tokens, reasoning_effort, context_window
- **Merges** with global config (project overrides global)
- **Reloads** on config file change

<!-- section_id: "6964b463-b485-4c31-b91a-c3d0b611af9d" -->
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

<!-- section_id: "ed49698c-09f6-453b-b6d0-a5f379feda00" -->
### What Codex Does NOT Do

- Doesn't validate config values (accepts invalid settings)
- Doesn't enforce limits (respects but doesn't block overages)
- Doesn't auto-update config (manual edits required)
- Doesn't manage secrets (you store API keys separately)

---

<!-- section_id: "391c23ad-d335-441f-b0a6-054cf0df8728" -->
## 3. Session Persistence

<!-- section_id: "40019f73-6fc4-4ca3-b5f9-f014c311d93d" -->
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

<!-- section_id: "c94d15e3-29a9-42bf-a872-1868f228833b" -->
### What Codex Does

- **Creates** new session directory on project init
- **Appends** turn records (never overwrites)
- **Persists** full conversation (JSONL format)
- **Enables** resumption via `codex resume [session-id]`
- **Maintains** session metadata (duration, turn count)
- **Indexes** sessions for quick lookup

<!-- section_id: "affcba6f-97ec-422f-b51d-084594b96df9" -->
### What Codex Does NOT Do

- Doesn't auto-cleanup old sessions (manual deletion required)
- Doesn't compress old conversations (raw JSONL stored)
- Doesn't encrypt session files (plain text, handle carefully)
- Doesn't share sessions across users (per-user ~/.codex/)
- Doesn't limit session size (no automatic archival)

---

<!-- section_id: "f9f59175-df65-4138-95cd-fa654cec5952" -->
## 4. IDE Extensions

<!-- section_id: "f88a5cad-bd62-40d7-bdd1-97a99aeee4d7" -->
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

<!-- section_id: "eedb6041-3bfc-40a6-bf07-21c99f98548e" -->
### What Codex Does

- **Discovers** IDE environment (VS Code, Cursor, Windsurf)
- **Loads** appropriate config/rules for IDE
- **Provides** IDE-specific UX (inline completions, sidebars, command palette)
- **Syncs** state between CLI and IDE
- **Respects** IDE-specific context (currently open file, selection, line number)

<!-- section_id: "21069982-2f6f-4f64-952c-30cf110fde9a" -->
### What Codex Does NOT Do

- Doesn't modify IDE keyboard shortcuts (IDE manages keybindings)
- Doesn't install extensions (user manages extension marketplace)
- Doesn't update IDE versions (user manages IDE updates)
- Doesn't control IDE theme/appearance (IDE manages UI)

---

<!-- section_id: "5fbcea65-43c7-4893-9fb1-50c80a529bf6" -->
## 5. Context Window Management

<!-- section_id: "2c5dee12-a71a-46f0-b103-e618f71861e1" -->
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

<!-- section_id: "670b2a62-5da1-449f-8b1d-a75f73dee958" -->
### What Codex Does

- **Counts** tokens as context fills
- **Monitors** approaching limit (warns at 80%)
- **Truncates** old conversation turns when full
- **Reports** usage via `/context` command
- **Adjusts** model behavior based on window size

<!-- section_id: "bb1f26ef-dd2e-4b13-9c03-f1808920c79c" -->
### What Codex Does NOT Do

- Doesn't have auto-compaction (manually manages via truncation)
- Doesn't prioritize content (FIFO truncation from oldest)
- Doesn't predict future usage (reacts to current state)
- Doesn't control model choice based on window (user decides)

---

<!-- section_id: "6f3e20dc-cc22-49aa-a21b-9e61a9520a7f" -->
## 6. Model Selection

<!-- section_id: "4ff4068e-82a8-42c6-9c1c-68b5accacbe4" -->
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

<!-- section_id: "79531eca-d53e-4eaf-958b-0ea3ac4e0982" -->
### What Codex Does

- **Accepts** model selection via CLI flag (`--model codex-opus`)
- **Applies** reasoning_effort from config.toml
- **Enforces** context window limits per model
- **Routes** requests to correct backend (API endpoint)
- **Reports** token usage and cost estimates

<!-- section_id: "1053ac1e-f215-4775-b68a-501da5a329e4" -->
### What Codex Does NOT Do

- Doesn't auto-select models (user decides)
- Doesn't manage billing (you track costs separately)
- Doesn't limit model changes mid-session (allowed)
- Doesn't validate reasoning_effort for model (assumes valid)

---

<!-- section_id: "4822d18b-2c75-470b-b8bb-9c1c683a4a5a" -->
## 7. Model Context Protocol (MCP)

<!-- section_id: "6b4126c9-cdd6-4fb3-b7fd-3c2b1733e2ef" -->
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

<!-- section_id: "ea986211-09df-4cbb-bede-ebfe5b3c17ba" -->
### What Codex Does

- **Discovers** available MCP servers (from config)
- **Lists** tools provided by each server
- **Invokes** tools when user/model requests them
- **Streams** results back into context
- **Manages** tool failures and timeouts (30s default)

<!-- section_id: "f3a7d7a8-adff-4df7-a0b7-e4eda4a49622" -->
### What Codex Does NOT Do

- Doesn't create MCP servers (requires separate setup)
- Doesn't manage server installation (you install separately)
- Doesn't validate tool safety (relies on MCP spec)
- Doesn't cache tool results (fresh call each time)

---

<!-- section_id: "76539d5f-5e54-44bb-9f09-6d374daea870" -->
## 8. GitHub Integration

<!-- section_id: "432552bb-3b76-4b0a-89c9-e22dfa5562bc" -->
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

<!-- section_id: "673f48ed-4d43-4ce6-ad78-6a75ee906828" -->
### What Codex Does

- **Accepts** GitHub URLs for project init
- **Clones** repo to local workspace
- **Creates** `.codex/` directory structure
- **Links** local state to GitHub project
- **Enables** git-aware context (branch info, recent commits)

<!-- section_id: "c4f8745f-eccc-4f82-8112-0b880d821e58" -->
### What Codex Does NOT Do

- Doesn't manage git commands (user runs `git` directly)
- Doesn't auto-commit changes (manual commit required)
- Doesn't create pull requests (user creates via GitHub)
- Doesn't handle authentication (assumes git auth configured)

---

<!-- section_id: "89f2b9a5-bf0c-443b-a7f8-980666774204" -->
## 9. Cloud Workspace Platform

<!-- section_id: "28c7f46d-540c-471a-9ec3-5e5f77767f86" -->
### The Mechanism

Codex's cloud platform synchronizes project state:

**Web Dashboard**: `https://cloud.codex.ai/workspaces`

**Synchronization**:
- Project metadata synced to cloud
- Session history available on cloud (with permission)
- Conversation history persistent across devices
- Workspace settings synced (config.toml)

<!-- section_id: "9a36684d-5fe6-4f25-a0af-4a498566bf45" -->
### What Codex Does

- **Maintains** cloud workspace account
- **Syncs** metadata to cloud infrastructure
- **Enables** cross-device resumption (login elsewhere, resume session)
- **Provides** web dashboard for workspace management
- **Stores** conversation history on cloud (encrypted)

<!-- section_id: "b9da19ac-b191-4506-ba20-eba91fd6501e" -->
### What Codex Does NOT Do

- Doesn't sync local files automatically (CLI only)
- Doesn't store code on cloud (only metadata/settings)
- Doesn't require cloud (CLI works fully offline)
- Doesn't manage cloud authentication (user manages login)

---

<!-- section_id: "843f7bba-e8c7-4748-96a5-eff84ce05cbf" -->
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

<!-- section_id: "e17294b6-81a9-4a9f-aebf-b7ed9f30842d" -->
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

<!-- section_id: "bb9dcaae-7ac8-45d2-b896-1c32403b992f" -->
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

