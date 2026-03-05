---
resource_id: "81cffb24-3a2e-4436-85ba-0036cc55f138"
resource_type: "output"
resource_name: "CLAUDE_CODE_NATIVE_CONTEXT_SYSTEM_VERIFIED"
---
# Claude Code CLI — Native Context System (Verified)

**Date Created**: 2026-02-27
**Status**: Verified via research
**Sources**: code.claude.com docs, memory docs, YouTube tutorials, developer blogs

---

## Overview

Claude Code CLI is Anthropic's terminal-native command-line interface for AI-powered coding assistance. Its **native context system** is built around:

1. **Context Window** (~200K tokens default, expandable to 1M)
2. **Hierarchical CLAUDE.md Files** (global → project → subdirectory cascade)
3. **MEMORY.md System** (200 lines in system prompt, rest on-demand)
4. **Subagents** (isolated context for parallel specialized tasks)
5. **Model Context Protocol (MCP)** (connection to external tools/APIs)
6. **Auto-Compaction** (evicts low-value items when context fills)

---

## Part 1: Context Window Management

### Size and Behavior

- **Default**: 200,000 input tokens
- **Expandable**: Up to 1 million tokens (with `--model sonnet[1m]`)
- **Auto-compaction**: When context nears limit, Claude evicts low-value items in this order:
  1. Old tool outputs first
  2. Then summarized conversation segments
  3. Preserves: Recent requests, code snippets, key memory files

### What Fills the Context

1. **Conversation history** — All previous turns in session
2. **File contents** — Code you're working on (via references like `@path/to/file`)
3. **Command outputs** — Results from shell commands, git operations
4. **CLAUDE.md instructions** — Loaded from hierarchy
5. **MEMORY.md** — First 200 lines auto-injected; rest loaded on-demand
6. **Skills** — Full content when invoked (descriptions at start)
7. **Subagent outputs** — Summaries returned from spawned agents
8. **System prompts** — Claude Code's internal instructions

### Compaction Control

Users can control compaction via:
- `/compact [focus]` — Summarize context, prioritizing elements matching `focus`
- `/context` — Show token usage breakdown
- `/status` — Show model, context state, memory status
- `/memory` — Toggle auto-memory on/off

Environment variable override:
```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1  # Force off
CLAUDE_CODE_DISABLE_AUTO_MEMORY=0  # Force on
```

---

## Part 2: Hierarchical CLAUDE.md System

### Loading Order (Root to Leaf)

Claude Code loads CLAUDE.md files in **hierarchical cascade**:

```
~/.claude/CLAUDE.md                    (User global — highest priority)
  ↓
/path/to/project/CLAUDE.md             (Project root)
  ↓
/path/to/project/subdirectory/CLAUDE.md (Subdirectory — lowest priority)
```

### When Loaded

| File | When Loaded | Purpose |
|------|------------|---------|
| **~/.claude/CLAUDE.md** | Every session start | Personal preferences, global rules |
| **Project CLAUDE.md** | Session launch + ancestor dirs | Project-specific instructions |
| **Subdir CLAUDE.md** | On-demand when files in subdir read | Subdirectory context |

### What Goes in CLAUDE.md

- **Critical rules** (I0_* constraints)
- **Key behaviors** (how Claude should work)
- **Skills descriptions** (when to invoke /skill-name)
- **File references** (what to read on-demand)
- **Integration links** (to MCP servers, knowledge bases)

---

## Part 3: MEMORY.md System (Session Persistence)

### File Location

```
~/.claude/projects/<project-name>/memory/MEMORY.md
```

### Loading Behavior

| Content | Loading | Purpose |
|---------|---------|---------|
| **First 200 lines** | Auto-injected in system prompt (every session) | Session index, quick reference |
| **Rest of file** | On-demand via `/memory` command | Full session history |
| **Topic files** (e.g., `debugging.md`) | On-demand (Claude reads/writes) | Organized knowledge by topic |

### Auto-Memory Features

- Claude **automatically reads** MEMORY.md at session start
- Claude **automatically writes** to MEMORY.md throughout session (with `/remember` command)
- Topic files created on-demand (e.g., "remember X" creates `topic.md`)
- Only first 200 lines loaded into system prompt (rest is on-demand to save tokens)

### Example Structure

```
# Auto Memory — Project X

## Current Status
[Session summary, last 3 entries]

## Key Learnings
[Topic 1](#topic1)
[Topic 2](#topic2)

## Quick Reference
[Essential info]

---

[Detailed content beyond 200 lines]

---
[Topic 1 - Debugging patterns, detailed notes]
[Topic 2 - Performance issues and solutions]
```

---

## Part 4: Subagents (Isolated Context)

### When Spawned

**Spawn via Task tool**:
```
Task(
    description="Analyze database schema for performance bottlenecks",
    subagent_type="general-purpose"
)
```

### Isolation Model

Each subagent gets:
- **Fresh context window** (independent of parent)
- **Lighter model** (e.g., Haiku for exploration)
- **Task description** only (no parent conversation history)
- **Optional mode**: plan (returns spec), acceptEdits (makes changes), delegate (spawns more agents)

### Why Subagents

- **Parallel work**: Up to 10 agents work simultaneously
- **Token efficiency**: Subagent returns *summary* not full output (parent doesn't get bloated)
- **Specialization**: Different agent types for different tasks

### Example: Parallel Exploration

```
Parent Agent:
├─ Spawn SubAgent 1: "Analyze API layer"
├─ Spawn SubAgent 2: "Analyze database layer"
└─ Spawn SubAgent 3: "Analyze UI layer"

(All run in parallel)

Results:
├─ SubAgent 1 returns: "API summary"
├─ SubAgent 2 returns: "DB summary"
└─ SubAgent 3 returns: "UI summary"

Parent integrates summaries (not full outputs)
```

---

## Part 5: Model Context Protocol (MCP)

### Purpose

MCP acts as the "nervous system" connecting Claude Code to external tools and APIs:

- **Databases**: Query execution, schema inspection
- **GitHub**: Repository access, PR operations
- **Testing frameworks**: Run tests, check coverage
- **Build tools**: Compile, lint, format
- **Custom tools**: Any custom integration

### MCP Tools in Context

When an MCP server is connected:
- Tool definitions are **included in API requests**
- Claude can invoke tools automatically (with user approval)
- Tool outputs are **fed back into context**
- Cost is monitored via `/mcp` command

### Example: Canvas MCP

```bash
# Connect Canvas LMS via MCP
/mcp enable canvas

# Claude can now invoke:
- canvas_assignment_list(course_id=398938)
- canvas_get_my_submission(course_id=398938, assignment_id=12345)
- etc.

# Results flow back into context
```

---

## Part 6: Context Loading (Reference-Based, Not Copy-Paste)

### How Files Are Included

**NOT**: Full file copy-paste into context
**YES**: Reference system where Claude loads on-demand

```
User: "@src/utils/helpers.ts: How does this function work?"

Claude loads:
1. Only the referenced file content (not entire codebase)
2. Relevant imports and dependencies
3. Related type definitions

Claude excludes:
- Unrelated files
- Large node_modules
- Binary files
```

### Reference Syntax

- `@path/to/file` — Specific file
- `@path/to/folder/` — Entire folder
- `/context` — Show what's loaded
- `/skill name` — Invoke a skill

### On-Demand Loading

For large codebases:
1. **Session launch**: Load only .claude/ files + project CLAUDE.md
2. **As needed**: Load files as user references them
3. **Auto-discovery**: Related files loaded based on imports/dependencies
4. **Lazy loading**: Topic files in MEMORY.md loaded only on `/memory` command

---

## Part 7: Skills System

### How Skills Load

| Phase | Content | Tokens |
|-------|---------|--------|
| **Initial** | Skill descriptions, metadata | ~50-100 per skill |
| **On invoke** | Full skill content | ~500-2000 per skill |

### Example: Canvas Skill

```
Initial context:
- Description: "Fetch Canvas grade data"
- Location: ~/.claude/skills/canvas-dashboard/

User invokes: `/calc-dashboard`
- Full skill code loaded (only then)
- Executes workflow
- Results returned to context
```

---

## Part 8: How Context Flows (Complete Picture)

```
SESSION START
  ↓
Load ~/.claude/CLAUDE.md (global)
  ↓
Load /project/CLAUDE.md (project root)
  ↓
Load first 200 lines of MEMORY.md
  ↓
Ready for conversation

USER MESSAGE: "Analyze this code"
  ↓
AUTO-GATHER:
  - Current file content
  - Recent edited files
  - Related imports
  - Semantic context
  ↓
CHECK TRIGGERS in CLAUDE.md
  ↓
LOAD MATCHING RESOURCES:
  - Relevant skills descriptions
  - Related .claude/rules/
  - MCP tool definitions
  ↓
CONTEXT WINDOW STATUS:
  - Used: ~X tokens
  - Available: ~(200K - X) tokens
  ↓
IF APPROACHING LIMIT:
  - /compact command runs automatically
  - Low-value items evicted
  - Summaries created
  ↓
CLAUDE RESPONDS

USER INVOKES SKILL: `/skill-name`
  ↓
Load full skill content
  ↓
Execute workflow
  ↓
Return results to context
  ↓
MEMORY.md updated (if /remember used)
```

---

## Part 9: Critical Native Features

### Auto-Compaction (Transparent to User)

When context nears limit (~190K tokens):
1. Identify low-value items (old outputs, previous summaries)
2. Evict in priority order
3. Create compressed versions if needed
4. Preserve: recent turns, code, key instructions

### Hooks for Customization

Users can define hooks in `.claude/hooks/` for:
- `PreCompact.md` — What to preserve before compaction
- `OnSessionStart.md` — Run before each session
- Other lifecycle events

### Ephemeral vs. Persistent Context

| Type | Persistence | Location |
|------|-------------|----------|
| **Ephemeral** | Session only | Conversation history |
| **Persistent** | Across sessions | MEMORY.md, .claude/ files |
| **Hybrid** | Session + saved | Loaded from files at start |

---

## Summary: What's Native vs. What's Custom

### NATIVE TO CLAUDE CODE
✅ CLAUDE.md hierarchy
✅ MEMORY.md system (200 lines in prompt, rest on-demand)
✅ Subagents (isolated context, parallel execution)
✅ MCP integration
✅ Auto-compaction (context management)
✅ Reference-based file loading (@path syntax)
✅ Skills system (descriptions + on-invoke)
✅ Commands: /context, /compact, /memory, /status, /mcp

### NOT NATIVE (Custom Systems)
❌ 0AGNOSTIC.md (user-designed layer-stage system)
❌ Layer-stage architecture (user-designed hierarchy)
❌ .0agnostic/ numbered directories (user-designed)
❌ Triggers table (user-designed)

---

## References

- **Official**: https://code.claude.com/docs/en/overview
- **Memory System**: https://code.claude.com/docs/en/memory
- **Context Management**: https://code.claude.com/docs/en/how-claude-code-works
- **CLI Reference**: https://code.claude.com/docs/en/cli-reference
- **YouTube**: "Claude Code Context, Subagents, and the Discipline of..."
- **Blog**: dev.to article on conversational development
