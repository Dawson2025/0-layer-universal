---
resource_id: "3f857ca4-7245-41d7-ab20-0bfdaa99ab76"
resource_type: "output"
resource_name: "COMPLETE_ARCHITECTURE"
---
# Codex CLI — Complete Architecture

**Date**: 2026-02-27
**Focus**: How native mechanisms + application-implemented strategy work together

---

<!-- section_id: "898ad460-49da-4276-8dc1-398dfadeac38" -->
## System Overview

Codex combines **native mechanisms** (what it provides) with **application-implemented strategy** (what you provide):

```
┌─────────────────────────────────────────────────┐
│  Codex CLI Native Mechanisms                    │
├─────────────────────────────────────────────────┤
│  • Three-level AGENTS.md hierarchy              │
│  • config.toml configuration system             │
│  • Session persistence (JSONL storage)          │
│  • IDE extensions (VS Code, Cursor, Windsurf)   │
│  • Context window management (token budgeting)  │
│  • Model selection (Opus/Sonnet/Haiku)          │
│  • Reasoning effort levels (low/medium/high)    │
│  • Model Context Protocol (MCP) support         │
│  • GitHub integration (workspace sync)          │
│  • Cloud workspace platform                     │
└─────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────┐
│  Your Application Strategy (What You Provide)   │
├─────────────────────────────────────────────────┤
│  • AGENTS.md content (rules, instructions)      │
│  • config.toml settings (model, temperature)    │
│  • Workspace initialization (linked projects)   │
│  • Session management (when to resume)          │
│  • IDE extension setup (which IDEs, config)     │
│  • MCP server selection (which tools to use)    │
│  • Project structure (folder hierarchy)         │
│  • GitHub organization (repo structure)         │
└─────────────────────────────────────────────────┘
                           ↓
                    Working System
```

---

<!-- section_id: "bf0e1f98-ff45-42eb-9c0f-9add22041949" -->
## Context Loading Pipeline

<!-- section_id: "3967a76a-79ad-43a4-887e-c87135b51c53" -->
### Step 1: Workspace Initialization

**Codex Does**:
1. Recognize project (identifies repo or local project)
2. Discover workspace location: `~/.codex/sessions/[project-id]/`
3. Load config.toml if exists

**You Must Have Done**:
- Linked project via `codex init` (GitHub or local)
- Created initial config.toml (or relying on defaults)

<!-- section_id: "95be55ad-b8e7-44b0-8568-5deaf2faa705" -->
### Step 2: Load Global AGENTS.md

**Codex Does**:
1. Find `~/.codex/AGENTS.md` (if exists)
2. Load entire file into context
3. Parse instructions, context declarations

**You Must Have Done**:
- Written `~/.codex/AGENTS.md` with universal instructions
- Defined global context and resources

<!-- section_id: "4a499e3d-b299-4e55-b12a-d9836fcf31e9" -->
### Step 3: Load Project AGENTS.md

**Codex Does**:
1. Find `/project/AGENTS.md` (if exists)
2. Merge with global AGENTS.md (project overrides global)
3. Inject merged context into system prompt

**You Must Have Done**:
- Written `/project/AGENTS.md` with project-specific instructions
- Defined project tech stack, conventions, workspace config

<!-- section_id: "7fec1f09-83e6-4b88-bca2-bb59a3a171b0" -->
### Step 4: Load Directory-Specific AGENTS.md

**Codex Does**:
1. Detect current working directory
2. Find `/project/subdir/AGENTS.md` (if exists)
3. Apply directory-specific context (lowest priority, most specific)

**You Must Have Done**:
- Create AGENTS.md at subdirectory level (optional)
- Document component-specific context

<!-- section_id: "020d5467-6f78-4ce5-b3bc-e56227d9d85a" -->
### Step 5: Load config.toml Settings

**Codex Does**:
1. Parse global `~/.codex/config.toml`
2. Merge with project `/project/config.toml` (project overrides global)
3. Apply settings: model, temperature, reasoning_effort, max_tokens, context_window

**You Must Have Done**:
- Configure appropriate settings per project
- Choose model (opus/sonnet/haiku) and reasoning_effort

<!-- section_id: "f30b1173-f9ed-4505-9ba9-cdb206c6d8f8" -->
### Step 6: Restore Session (if resuming)

**Codex Does**:
1. Find session directory: `~/.codex/sessions/[project-id]/[session-id]/`
2. Load conversation history (JSONL format)
3. Restore context from previous turns
4. Ready to continue conversation

**You Must Have Done**:
- Decide to resume via `codex resume [session-id]`
- Maintain session state (no cleanup between turns)

<!-- section_id: "3e0d402f-488d-4feb-89fb-f05f4ea1c1e6" -->
### Step 7: Prepare for User Interaction

**Codex Does**:
1. Merge all context: global AGENTS.md + project AGENTS.md + directory AGENTS.md + config + session history
2. Estimate token usage
3. Set up model routing (to correct Codex model backend)
4. Initialize command handlers

**You Get**:
- Fully loaded context ready for conversation
- Model and reasoning_effort applied
- Session history (if resuming) available

---

<!-- section_id: "d498f56c-969b-4cc2-bbd2-80f56325356f" -->
## On Each Turn

<!-- section_id: "4efbcc5a-cf2a-496e-9607-e67b5d3dfe7b" -->
### What Codex Does

1. **Parse** user message
2. **Check** if MCP server calls needed (user requests tool use)
3. **Load** any additional AGENTS.md files (if directory changed)
4. **Apply** config settings (current model, reasoning_effort)
5. **Estimate** tokens used
6. **Generate** response (using selected model + reasoning_effort)
7. **Save** turn to session JSONL
8. **Report** token usage (if requested via `/context` command)

<!-- section_id: "f3b42339-96a4-41bf-88d9-0aaa3c8fa19b" -->
### What You Do

1. **Write** natural requests
2. **Reference** files/code by path (mention file names, path structure)
3. **Invoke** MCP tools if needed (request tool use)
4. **Manage** sessions (decide when to resume vs. start new)
5. **Check** context usage (via `codex context` command)
6. **Choose** model/reasoning_effort (via CLI flag or config)

---

<!-- section_id: "4db87ea5-5d1c-4b6e-946e-b41a210c86c8" -->
## Context Composition (What's Actually in Context)

At any point, your context window contains:

```
┌─ System Prompt (Codex's instructions)
├─ AGENTS.md (global)
├─ AGENTS.md (project)
├─ AGENTS.md (directory-specific, if applicable)
├─ config.toml settings (applied as context metadata)
├─ Conversation history (all turns in session)
├─ IDE context (if using IDE extension — current file, selection)
├─ MCP tool definitions (available tools)
├─ Session metadata (project, branch, date/time)
├─ Current user message
└─ Remaining tokens: available for response
```

**Token Budget** (128K default, up to 1M possible):
- ~2K: System prompt
- ~1K: AGENTS.md (global)
- ~2K: AGENTS.md (project)
- ~0.5K: AGENTS.md (directory)
- ~X: Conversation history (grows as you talk)
- ~Y: IDE context (current file, if using IDE)
- ~Z: MCP tool descriptions
- ~Remaining: Available for response

---

<!-- section_id: "fd05bfd2-c845-44df-b583-d4dd5baf7966" -->
## AGENTS.md Organization Strategy

<!-- section_id: "9feef7e4-dfa2-42db-8e52-105063ceeb5d" -->
### Structure

```markdown
# [Project Name] — Codex Instructions

## [CRITICAL] Rules

[Most important rules first — what MUST happen]

## Tech Stack & Architecture

[Languages, frameworks, conventions, design patterns]

## Model Settings

[Recommended model, temperature, reasoning_effort]

## Context & Resources

[Links to documentation, knowledge bases]

## Directory Guidelines

[If this file is in a subdirectory: what's special about THIS component?]

## Current Status

[What's the current state of the project/component?]
```

**Key Principle**: Important info first (no scrolling needed).

---

<!-- section_id: "237c2dd8-17de-4c99-8355-e9de66d44817" -->
## config.toml Organization Strategy

<!-- section_id: "94f97555-613d-42e3-acf6-73ebc83d0a3b" -->
### Structure

```toml
[default]
model = "codex-sonnet"
temperature = 0.7
max_tokens = 4096
reasoning_effort = "medium"
context_window = "128k"
session_persistence = true
github_integration = true

[project.your-project]
model = "codex-opus"
reasoning_effort = "high"
max_tokens = 8192
```

**Key Principle**: Global defaults, project-specific overrides.

<!-- section_id: "b3e6f9a7-d788-4858-8ef9-09f5cd6c973c" -->
### Settings You'll Adjust

| Setting | Effect | When to Change |
|---------|--------|-----------------|
| `model` | Which Codex model | Use opus for complex work, haiku for speed |
| `temperature` | Randomness (0=deterministic, 2=creative) | Higher for creative writing, lower for code |
| `max_tokens` | Response length limit | Increase for long responses, decrease for quick answers |
| `reasoning_effort` | Thinking depth (low/medium/high) | high for complex problems, low for speed |
| `context_window` | Input token limit | Expand if needing more history/files |
| `session_persistence` | Save conversations | Keep true unless experimenting |

---

<!-- section_id: "fd0ee7e7-0308-4176-a090-e5ae8adc251e" -->
## IDE Extension Integration

<!-- section_id: "87009826-a62a-40c7-a709-28c2ede4b89c" -->
### VS Code Extension

**Setup**:
```bash
# Install from marketplace or via command palette
# Codex will read ~/.codex/AGENTS.md and config.toml
# Current file is automatically included in context
```

**UX**:
- Inline completions
- Chat sidebar
- Command palette (quick actions)

<!-- section_id: "cab00f8e-45b5-4b05-b341-57f1fe7d1e96" -->
### Cursor IDE

**Setup**:
```
# Built-in Codex integration
# Also reads ~/.codex/AGENTS.md + config.toml
# Plus .cursor/rules (if you want IDE-specific rules)
```

**UX**:
- Enhanced with semantic search
- Memory Bank (persistent notes)
- Agent interface (agentic execution)

<!-- section_id: "4d22a5cb-ceff-4b88-ab9b-a0fb16ce4fbf" -->
### Windsurf IDE

**Setup**:
```
# Install Codex extension or use built-in
# Configure agent-first workflow
```

**UX**:
- Flow mode (continuous agent execution)
- Automatically completes tasks

---

<!-- section_id: "19ebc3d0-92c7-4d64-ac69-d7e1dd0a7003" -->
## Session Persistence Flow

<!-- section_id: "c4952e2f-d6fa-4093-8926-c84eb6e6c3cd" -->
### Creating Sessions

```
codex /project
  ↓
Creates: ~/.codex/sessions/[project-id]/[timestamp]/
  ↓
Session contains:
  - history.jsonl (conversation turns)
  - metadata.json (created date, turn count)
  - state/ (if model supports checkpoints)
```

<!-- section_id: "b61999ba-252a-4dcc-83f1-f692a9ae5928" -->
### Resuming Sessions

```
codex resume [session-id]
  ↓
Loads: ~/.codex/sessions/[project-id]/[session-id]/history.jsonl
  ↓
Restores conversation context
  ↓
Ready to continue from last turn
```

<!-- section_id: "c1ea0733-8cd7-42d9-bced-9f4b7ebc2485" -->
### Session Cleanup

Sessions persist indefinitely. You manually:
- Archive old sessions (`codex archive [session-id]`)
- Delete completed sessions (optional)
- List active sessions (`codex list-sessions`)

---

<!-- section_id: "0e870987-9789-46bd-a8bc-9d13b0ffa894" -->
## MCP Server Integration

<!-- section_id: "0b7f1bf2-9a40-4999-b9f7-1387246c5a90" -->
### When You Need External Tools

```
User: "Fetch Canvas grades for MATH 119"
  ↓
Codex CLI checks: Do I have Canvas MCP server?
  ↓
Yes: Lists available Canvas tools
  ↓
Codex calls: canvas_assignment_list(course_id=398938)
  ↓
MCP server executes against Canvas API
  ↓
Results returned to context
  ↓
Codex processes and responds
```

**Your Responsibility**:
- Install/configure MCP server
- Provide credentials (API keys)
- Enable in config.toml (if per-project)
- Codex handles the rest

---

<!-- section_id: "c6ae3e15-92a5-4b9c-b683-3112b78538bf" -->
## GitHub Integration

<!-- section_id: "75faacdf-cc58-4e80-8090-5bf68d02ac28" -->
### Workspace Sync

**Initialization**:
```bash
codex init https://github.com/user/repo
  ↓
Clones repo to local workspace
Creates ~/.codex/sessions/[repo-id]/
Links to GitHub for sync
```

**Context Available to Codex**:
- Git branch (current branch awareness)
- Recent commits (context about recent work)
- File tree (knows about .gitignore, structure)
- GitHub status (if synced)

---

<!-- section_id: "7d383ad4-44ff-48b2-90d9-248af2a4fd65" -->
## Cloud Workspace Platform

<!-- section_id: "d691574a-1194-4615-8ad6-a097e6b76b84" -->
### What Syncs to Cloud

**Metadata**:
- Project information
- Workspace settings
- Session list (available sessions)

**Not Synced** (stays local):
- Actual conversation history (unless you opt-in)
- Code files (stay on local machine)

<!-- section_id: "8aaa91ce-f15a-43e1-92fd-a1c4e9843e52" -->
### Cross-Device Resumption

If you log into cloud.codex.ai on another device:
- Can see your workspaces
- Can resume sessions (if cloud sync enabled)
- Can access project metadata

---

<!-- section_id: "3dc92ffc-27f0-4762-8bfe-a7198df74175" -->
## Model and Reasoning Selection

<!-- section_id: "9b4e89b3-bf12-41c0-b679-bb89d1df5ea0" -->
### Model Choice

| Model | Speed | Depth | Cost | Best For |
|-------|-------|-------|------|----------|
| codex-haiku | Very Fast | Basic | $ | Quick questions, lightweight |
| codex-sonnet | Fast | Good | $$ | Typical coding tasks, chat |
| codex-opus | Slow | Very Deep | $$$ | Complex analysis, research |

**When to Use**:
- Simple questions → haiku (2-3 seconds)
- Standard work → sonnet (5-15 seconds)
- Complex problems → opus (30+ seconds)

<!-- section_id: "37218acb-c0fe-4cb8-9613-8bdaa81c99c4" -->
### Reasoning Effort

| Level | Time | Depth | When to Use |
|-------|------|-------|-------------|
| low | <5s | Surface | Quick drafts, simple tasks |
| medium | 10-30s | Standard | Most coding work (default) |
| high | 30-120s | Deep | Complex logic, math, debugging |

**Cost**: high = ~4x more expensive than low.

---

<!-- section_id: "449e3ccf-1114-415d-83dd-d1641be0dfa5" -->
## Token Management Philosophy

<!-- section_id: "c13cc8bc-039e-4076-95d7-3ea55766b374" -->
### Goal: Maximize Quality, Manage Cost

**Token Budgeting**:
1. **Essential** (always loaded): AGENTS.md files, config metadata
2. **Session history** (grows as you talk): Previous turns
3. **IDE context** (variable): Current file and selection
4. **Generated** (response space): Leave ~10-20% free

**Optimization**:
- Keep AGENTS.md concise (300-500 lines ideal per level)
- Use summary comments (point to detailed docs, don't include them)
- Archive old sessions (don't keep 50 session histories active)
- Monitor token usage (via `codex context` command)

**Cost Awareness**:
- Every token costs money (tokens = billing)
- reasoning_effort scales cost (high = 4x)
- Longer context window = proportionally more tokens
- Monitoring usage helps catch runaway costs

---

<!-- section_id: "ad4cb411-22fd-44e2-ac39-fbec122484d0" -->
## Troubleshooting

<!-- section_id: "417d963a-8e1a-47d3-a650-527e1efb0df1" -->
### Codex Seems Confused

**Check**:
1. Is AGENTS.md up-to-date? (architecture changed?)
2. Is config.toml pointing to right model? (using opus when haiku is fine?)
3. Is project structure reflected in AGENTS.md?

**Fix**:
- Update AGENTS.md with current architecture
- Adjust config.toml (maybe use sonnet instead of opus to save cost)
- Create directory-level AGENTS.md for specific context

<!-- section_id: "3aef2ab3-fa47-46b3-9e2e-6d0e50e5bd7c" -->
### Reasoning Effort Not Deep Enough

**Check**:
1. Is reasoning_effort set to "high" in config?
2. Do you need reasoning_effort? (not all tasks need deep reasoning)
3. Is the model capable? (haiku doesn't support high reasoning)

**Fix**:
- Set `reasoning_effort = "high"` in config
- Switch to sonnet or opus (`model = "codex-sonnet"`)
- Ask more specific questions (better prompts = better reasoning)

<!-- section_id: "30220208-bad3-48c6-abd6-1b59f332459f" -->
### Tokens Running Out Quickly

**Check**:
1. Is AGENTS.md too verbose?
2. Is session history accumulating? (very long conversations)
3. Is reasoning_effort set to high? (costs 4x tokens)

**Fix**:
- Trim AGENTS.md to essentials
- Archive old sessions
- Switch reasoning_effort to medium (or low for simple work)
- Use separate sessions for unrelated tasks

<!-- section_id: "aeb21434-4932-4448-ad28-167608f11041" -->
### IDE Not Getting Context from Codex

**Check**:
1. Is IDE extension installed?
2. Is AGENTS.md present? (required for context)
3. Is config.toml correctly parsed?

**Fix**:
- Reinstall IDE extension
- Create AGENTS.md if missing
- Verify config.toml syntax (TOML format must be valid)

---

<!-- section_id: "3b322e5d-6625-4b16-bbc5-1e463234707c" -->
## Summary: The System Works When

✅ **AGENTS.md is accurate** (reflects current architecture, rules, resources)
✅ **config.toml is optimized** (model/reasoning_effort matched to task)
✅ **Sessions are managed** (not accumulating hundreds of old sessions)
✅ **Project structure is logical** (AGENTS.md can be placed at useful levels)
✅ **MCP servers are configured** (needed tools available, credentials set)
✅ **IDE extensions work** (VS Code/Cursor configured correctly)
✅ **GitHub integration is set up** (workspace linked to repo, if applicable)
✅ **Context is lean** (AGENTS.md files concise, not 2000+ lines)

The system fails when any of these are missing or outdated.

