---
resource_id: "aa556dc1-036c-42ab-b7d2-f0ee5a7e8414"
resource_type: "output"
resource_name: "03_COMPLETE_ARCHITECTURE"
---
# Claude Code CLI — Complete Architecture

**Date**: 2026-02-28
**Focus**: How native mechanisms + application-implemented strategy work together in Claude Code CLI

---

## System Overview

Claude Code CLI combines **native mechanisms** (what it provides) with **application-implemented strategy** (what you provide):

```
┌─────────────────────────────────────────────────────┐
│  Claude Code CLI Native Mechanisms                  │
├─────────────────────────────────────────────────────┤
│  • Hierarchical CLAUDE.md cascade                   │
│  • MEMORY.md auto-injection (first 200 lines)      │
│  • Context window tracking (200K default)           │
│  • Auto-compaction (transparent, automatic)        │
│  • Project identification via directory hash        │
│  • MCP server connections (tool integration)       │
│  • File @references (load on-demand)               │
│  • Skills system (reusable workflows)              │
│  • Commands (/context, /memory, /skill, etc.)     │
│  • Conversation history (JSONL persistence)        │
└─────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────┐
│  Your Application Strategy (What You Provide)      │
├─────────────────────────────────────────────────────┤
│  • CLAUDE.md content (rules, triggers, resources)  │
│  • MEMORY.md organization (what's essential?)      │
│  • Skills design (reusable workflows)              │
│  • MCP server selection (which external tools?)    │
│  • Project organization (layers, stages, entities) │
│  • Context management (static vs. dynamic)         │
│  • File organization (structuring for @refs)       │
└─────────────────────────────────────────────────────┘
                           ↓
                    Working System
```

---

## Context Loading Pipeline

### Step 1: Session Initialization

**Claude Code Does**:
1. Recognize project via working directory hash
2. Discover project ID: `[hash]`
3. Look for: `~/.claude/projects/[hash]/`

**You Must Have Done**:
- Created project-specific directories (or let Claude Code auto-create them)
- Organized memory/config files
- Set up initial state (or use defaults)

### Step 2: Load Global Configuration

**Claude Code Does**:
1. Find `~/.claude/CLAUDE.md`
2. Load entire file into context
3. Parse rules, triggers, resources

**You Must Have Done**:
- Written `~/.claude/CLAUDE.md` with universal rules
- Defined triggers (when to load context)
- Listed skills, resources, behaviors

### Step 3: Load Project CLAUDE.md

**Claude Code Does**:
1. Find `~/.claude/projects/[hash]/CLAUDE.md` (if exists)
2. Merge with global CLAUDE.md
3. Project-level rules override global rules

**You Must Have Done**:
- Written `/project/CLAUDE.md` with project-specific rules (or omit if using global only)
- Defined layer/stage context (if layered project)
- Listed project-specific skills

### Step 4: Load Directory Chain CLAUDE.md

**Claude Code Does**:
1. Find `[CURRENT_DIR]/CLAUDE.md` (if exists)
2. Walk up directory tree: parent, grandparent, ..., git root
3. Merge all found files (higher priority = later in chain)

**You Must Have Done**:
- Created CLAUDE.md at layer/stage/entity levels (for hierarchical projects)
- Documented layer-specific identity and context

### Step 5: Load MEMORY.md (First 200 Lines)

**Claude Code Does**:
1. Find `~/.claude/projects/[hash]/memory/MEMORY.md`
2. Read first 200 lines exactly
3. Inject into system prompt

**You Must Have Done**:
- Created MEMORY.md with most essential info in first 200 lines
- Organized supplementary content after 200-line boundary
- Updated MEMORY.md as you work

### Step 6: Prepare for User Interaction

**Claude Code Does**:
1. Open context window
2. Estimate token usage
3. Set up compaction thresholds
4. Initialize command handlers (/memory, /context, /skill, etc.)

**You Get**:
- Fully loaded context ready for conversation
- Memory available on-demand via /memory
- Full context usage visible via /context

---

## On Each Turn

### What Claude Code Does

1. **Parse** user message
2. **Check** triggers from CLAUDE.md
3. **Load** matching context:
   - File references (@file, @folder)
   - Skill descriptions (if mentioned)
   - MCP tool definitions (if needed)
4. **Monitor** token usage
5. **Generate** response
6. **Update** state (if /remember used, /skill invoked, etc.)
7. **Log** turn to `~/.claude/projects/[hash]/history.jsonl`

### What You Do

1. **Write** natural requests
2. **Reference** files/folders with @ syntax
3. **Invoke** skills with / syntax
4. **Update** memory with /remember
5. **Check** context with /context
6. **Decide** whether to parallelize (spawn subagents)

---

## Context Composition (What's Actually in Context)

At any point, your context window contains:

```
┌─ System Prompt (Claude Code's instructions)
├─ CLAUDE.md (global rules)
├─ ~/.claude/projects/[hash]/CLAUDE.md (project rules, if exists)
├─ [CURRENT_DIR]/CLAUDE.md chain (directory hierarchy, if exists)
├─ MEMORY.md (first 200 lines)
├─ Conversation history (previous turns in session)
├─ Loaded files (@file, @folder references)
├─ Loaded skill descriptions (if mentioning skills)
├─ MCP tool definitions (available tools)
├─ Current user message
└─ Remaining tokens: available for response
```

**Token Budget** (200K default):
- ~5K: System prompt + instructions
- ~3K: CLAUDE.md (global)
- ~2K: CLAUDE.md (project)
- ~2K: CLAUDE.md (directory chain, if deep)
- ~2K: MEMORY.md (first 200 lines)
- ~X: Conversation history (grows as you talk)
- ~Y: Loaded files (depends on what you @reference)
- ~Z: Remaining for response

---

## Auto-Compaction Flow

### When Triggered

```
Context at 90% capacity (~180K of 200K tokens)
  ↓
Claude Code triggers auto-compaction
  ↓
Identify low-value items:
  • Oldest tool outputs
  • Previous explanations
  • Summary snippets
  ↓
Preserve high-value items:
  • Recent CLAUDE.md rules (can't delete)
  • MEMORY.md (can't delete)
  • Recent code from user
  • Recent system responses
  ↓
Evict bottom items to free space
  ↓
Conversation resumes with freed tokens
```

**Result**: Context shrinks but continues seamlessly.

---

## Project Structure and Storage

### Local Storage Locations

```
~/.claude/
├── CLAUDE.md                          (Global context, always loaded)
├── keybindings.json                   (Global keybindings)
├── settings.json                      (Global settings)
│
└── projects/
    └── [PROJECT_HASH]/
        ├── CLAUDE.md                  (Project context, if exists)
        ├── 0INDEX.md                  (Current state tracking)
        ├── status.json                (Project metadata)
        ├── memory/
        │   └── MEMORY.md              (Project memory, first 200 lines auto-loaded)
        └── history.jsonl              (Conversation history, all turns)
```

### Project Hash

Claude Code computes a **deterministic hash** from the working directory:

```
Working Directory: /home/dawson/dawson-workspace/code/0_layer_universal
  ↓ (hash function)
Project Hash: a1b2c3d4e5f6 (stable, same path = same hash)
  ↓
Project Directory: ~/.claude/projects/a1b2c3d4e5f6/
```

**Same directory = same hash** (allows resuming work across sessions)
**Different directory = different hash** (separate project context)

---

## Subagent Architecture

### When You Spawn Subagents

```
You: "I need to analyze 3 components"

You spawn (via Task tool):
  ├─ Subagent 1 (task: analyze component A)
  ├─ Subagent 2 (task: analyze component B)
  └─ Subagent 3 (task: analyze component C)

Each subagent:
  • Gets fresh 200K context window
  • Loads YOUR global CLAUDE.md (same rules)
  • Gets task description (no parent history)
  • Works autonomously
  • Returns summary (not full output)

Main context:
  • Gets 3 summaries back
  • Aggregates findings
  • Context stays lean (only summaries, not full outputs)
```

**Benefit**: Parallelism + token efficiency.

---

## MEMORY.md Organization Strategy

### Structure

```markdown
# Auto Memory — [Project]

## Current Status
[One-line summary of where project is]

## Key Learnings
[Bulleted links to topic files below]

## Quick Reference
[Most essential info (used every session)]

---
[BOUNDARY: 200 lines]
---

## [Topic 1: Debugging]
[Detailed debugging patterns & gotchas]

## [Topic 2: Performance]
[Performance optimization notes]

## [Topic 3: API]
[API endpoints, response formats, gotchas]

## [Topic 4: Database]
[Schema, queries, migration notes]
```

**Loaded Every Session**: First 200 lines
- Current status (what's the project doing now?)
- Quick reference (essential info)
- Topic index (where to find details)

**Loaded On-Demand**: Full file + topic files
- `/memory` command shows everything
- Full details available when needed

---

## CLAUDE.md Organization Strategy

### Structure

```markdown
# [Project/Global] Claude Code Configuration

## [CRITICAL] Rules
[Most important rules first — what MUST happen]

## Layer-Stage Context
[If using layer-stage system: what layer/stage are we in?]

## Triggers
[When to load what context? (table format)]

## Skills
[What skills are available? When to use each?]

## Resources
[Where can Claude find: rules, knowledge, protocols?]

## Current Status
[Summary of project state, architecture, current focus]
```

**Key Principle**: Important info first (no scrolling needed).

---

## MCP Server Integration

### When You Need External Tools

```
User: "Fetch the grade data from Canvas"

Claude Code searches:
  • Is there Canvas MCP server configured?
  • Yes: Lists available Canvas tools
  • Claude calls canvas_assignment_list(course_id=...)
  • MCP server executes against Canvas API
  • Results returned to context
  • Claude processes and responds
```

**Your Responsibility**:
- Install/configure MCP server
- Provide credentials (API keys)
- Claude Code handles the rest

---

## Conversation History

Claude Code automatically persists all conversations:

```
Location: ~/.claude/projects/[HASH]/history.jsonl

Format: JSON Lines (one JSON object per line)

Each turn contains:
  • User message
  • Claude response
  • Timestamp
  • Model used
  • Token usage
  • Any state changes

On Resumption:
  • Load previous turns from history
  • Resume conversation at last turn
  • Full history available for reference
```

**Note**: History is stored locally, never uploaded to Anthropic servers (stays on your machine).

---

## Token Management Philosophy

### Goal: Maximize Quality, Manage Cost

**Token Budgeting**:
1. **Essential** (always loaded): CLAUDE.md, MEMORY.md (200 lines)
2. **Referenced** (load on-demand): @files, skills
3. **Generated** (response space): Leave ~10-20% free

**Optimization**:
- Keep CLAUDE.md concise (300-500 lines ideal)
- Keep MEMORY.md first 200 lines to essentials only
- Use @references instead of loading everything
- Use subagents for large parallel work

**Cost Awareness**:
- Claude Code with 200K context is free tier (capped usage)
- Pro subscription enables higher usage
- Auto-compaction reduces waste
- Lean context = more room for conversation
- Parallelization (subagents) = token efficiency

---

## Scalability: From Small to Large Projects

### Small Project (1-person, simple codebase)

```
~/.claude/CLAUDE.md          [Global rules]
~/.claude/projects/[hash]/memory/MEMORY.md      [Project memory]
```

**Tokens**: Few hundred, plenty of room.

### Medium Project (team, complex codebase)

```
~/.claude/CLAUDE.md          [Global rules]
/project/CLAUDE.md           [Project rules]
~/.claude/projects/[hash]/memory/MEMORY.md      [Project memory]
~/.claude/projects/[hash]/memory/debugging.md   [Topic 1]
~/.claude/projects/[hash]/memory/architecture.md [Topic 2]
~/.claude/skills/[skill1]/   [Reusable skill 1]
~/.claude/skills/[skill2]/   [Reusable skill 2]
```

**Tokens**: Managed carefully, compaction active.

### Large Project (distributed team, massive codebase)

```
[All above, plus:]

~/.claude/projects/[hash]/memory/api_reference.md
~/.claude/projects/[hash]/memory/database_schema.md
~/.claude/projects/[hash]/memory/performance_notes.md

[Multiple MCP servers for different tools]

[Subagents for parallel analysis]

[Strategic use of @folder references (not whole codebase)]
```

**Tokens**: At limit, careful management, parallelization essential.

---

## When Things Go Wrong

### Claude Seems Confused

**Check**:
1. Is CLAUDE.md up-to-date? (architecture changed?)
2. Is MEMORY.md accurate? (outdated info?)
3. Is project structure reflected in CLAUDE.md?

**Fix**:
- Update CLAUDE.md with current architecture
- Update MEMORY.md with current state
- Use /remember to add missing context

### Running Out of Tokens Quickly

**Check**:
1. Is CLAUDE.md too verbose?
2. Are you loading full codebase with @folder?
3. Are compacted items being evicted too aggressively?

**Fix**:
- Trim CLAUDE.md to essentials
- Use @file instead of @folder
- Use subagents to parallelize large work

### Skills Not Being Invoked When Expected

**Check**:
1. Are skills listed in CLAUDE.md?
2. Are triggers defined in CLAUDE.md?
3. Does Claude know when to use skills?

**Fix**:
- Add skill to Triggers table in CLAUDE.md
- Be explicit: "use /skill-name"
- Update skill descriptions to match your intent

---

## Summary: The System Works When

✅ **CLAUDE.md is accurate** (reflects current architecture, rules, available skills)
✅ **MEMORY.md is current** (most important info in first 200 lines)
✅ **Skills are well-documented** (clear WHEN/WHEN NOT)
✅ **Project structure is logical** (easy to @reference)
✅ **MCP servers are configured** (external tools available)
✅ **You parallelize when beneficial** (subagents for large tasks)
✅ **Context is lean** (not bloated, let auto-compaction work)

The system fails when any of these are missing or outdated.
