---
resource_id: "aa556dc1-036c-42ab-b7d2-f0ee5a7e8414"
resource_type: "output"
resource_name: "03_COMPLETE_ARCHITECTURE"
---
# Claude Code CLI — Complete Architecture

**Date**: 2026-02-28
**Focus**: How native mechanisms + application-implemented strategy work together in Claude Code CLI

---

<!-- section_id: "63dc8812-3393-45a5-9d95-b7d0b33afc7f" -->
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

<!-- section_id: "4533b099-23a1-4312-b886-8ac192b6b3b5" -->
## Context Loading Pipeline

<!-- section_id: "ba171d0d-9ffd-4471-90cd-01ee684c1dbd" -->
### Step 1: Session Initialization

**Claude Code Does**:
1. Recognize project via working directory hash
2. Discover project ID: `[hash]`
3. Look for: `~/.claude/projects/[hash]/`

**You Must Have Done**:
- Created project-specific directories (or let Claude Code auto-create them)
- Organized memory/config files
- Set up initial state (or use defaults)

<!-- section_id: "0fcaf061-fae1-49ce-ba33-d3ee9fbd435b" -->
### Step 2: Load Global Configuration

**Claude Code Does**:
1. Find `~/.claude/CLAUDE.md`
2. Load entire file into context
3. Parse rules, triggers, resources

**You Must Have Done**:
- Written `~/.claude/CLAUDE.md` with universal rules
- Defined triggers (when to load context)
- Listed skills, resources, behaviors

<!-- section_id: "13d4a1cb-ebfe-4014-98ed-0a01d217d44f" -->
### Step 3: Load Project CLAUDE.md

**Claude Code Does**:
1. Find `~/.claude/projects/[hash]/CLAUDE.md` (if exists)
2. Merge with global CLAUDE.md
3. Project-level rules override global rules

**You Must Have Done**:
- Written `/project/CLAUDE.md` with project-specific rules (or omit if using global only)
- Defined layer/stage context (if layered project)
- Listed project-specific skills

<!-- section_id: "a6857d03-a9d7-4937-b15f-896d0ec26334" -->
### Step 4: Load Directory Chain CLAUDE.md

**Claude Code Does**:
1. Find `[CURRENT_DIR]/CLAUDE.md` (if exists)
2. Walk up directory tree: parent, grandparent, ..., git root
3. Merge all found files (higher priority = later in chain)

**You Must Have Done**:
- Created CLAUDE.md at layer/stage/entity levels (for hierarchical projects)
- Documented layer-specific identity and context

<!-- section_id: "38357965-efc5-4e03-b60b-6231a8506d8b" -->
### Step 5: Load MEMORY.md (First 200 Lines)

**Claude Code Does**:
1. Find `~/.claude/projects/[hash]/memory/MEMORY.md`
2. Read first 200 lines exactly
3. Inject into system prompt

**You Must Have Done**:
- Created MEMORY.md with most essential info in first 200 lines
- Organized supplementary content after 200-line boundary
- Updated MEMORY.md as you work

<!-- section_id: "a5a2cb02-1547-42f8-aafd-3331e5936f8d" -->
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

<!-- section_id: "0a71b120-1f9d-4fe4-9d13-51af5c0533c1" -->
## On Each Turn

<!-- section_id: "33af2e18-a603-49b8-a5a9-cdb0d75be8eb" -->
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

<!-- section_id: "5520b21d-67b7-4c79-b57c-c7c7fb67bc32" -->
### What You Do

1. **Write** natural requests
2. **Reference** files/folders with @ syntax
3. **Invoke** skills with / syntax
4. **Update** memory with /remember
5. **Check** context with /context
6. **Decide** whether to parallelize (spawn subagents)

---

<!-- section_id: "9175fd36-00db-4ecc-a8b6-86581bf51aa1" -->
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

<!-- section_id: "accbc5c3-f5f5-412c-9923-4ff139fb4220" -->
## Auto-Compaction Flow

<!-- section_id: "128cedb6-4253-461b-b9cd-fd11186ece37" -->
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

<!-- section_id: "d3586078-d367-4fb1-82a3-cc4199619624" -->
## Project Structure and Storage

<!-- section_id: "f528e0fa-cda5-496b-8d72-b7db8916b55a" -->
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

<!-- section_id: "c51b7699-ac34-46bf-a07a-2bed8d293041" -->
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

<!-- section_id: "e9597158-36a5-421a-8be8-85126ed551ed" -->
## Subagent Architecture

<!-- section_id: "6bd8a826-d3be-4088-bfe5-9cd7daec992d" -->
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

<!-- section_id: "c09a2b8a-f368-42c9-8a43-ab087dd92cca" -->
## MEMORY.md Organization Strategy

<!-- section_id: "73f9a1bf-50bb-4663-8035-7ce520a340ba" -->
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

<!-- section_id: "cb59502d-c2bc-431e-bd02-af8a58077d0d" -->
## CLAUDE.md Organization Strategy

<!-- section_id: "b8ccefd9-743c-4d73-bf04-9c569b7cd77d" -->
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

<!-- section_id: "d25d8d2a-3c30-4b05-a4c8-786f590b6be0" -->
## MCP Server Integration

<!-- section_id: "7830bdae-beac-457e-bb69-c2cc8aabb3ef" -->
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

<!-- section_id: "f8da13d8-57c2-47d0-894e-75f8db4d73a6" -->
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

<!-- section_id: "8e7d51a8-e41f-4e5c-8119-9e714912876a" -->
## Token Management Philosophy

<!-- section_id: "56fdddd9-a7ee-4ae5-b737-09a21ccb7e4b" -->
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

<!-- section_id: "d8c4a7f8-425e-4c38-897c-9fc48fe53576" -->
## Scalability: From Small to Large Projects

<!-- section_id: "39f8a13b-7dc9-4959-8390-1fbcdc7c6ac0" -->
### Small Project (1-person, simple codebase)

```
~/.claude/CLAUDE.md          [Global rules]
~/.claude/projects/[hash]/memory/MEMORY.md      [Project memory]
```

**Tokens**: Few hundred, plenty of room.

<!-- section_id: "c0345706-ee8b-4bf5-828c-ccee0b82c809" -->
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

<!-- section_id: "d3f0aece-ba74-4c12-8c69-923de7bb3f12" -->
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

<!-- section_id: "846ea611-62c5-484c-be33-cd32faa4a1ad" -->
## When Things Go Wrong

<!-- section_id: "b84fc0a9-31af-447d-9cfa-bda802a902f7" -->
### Claude Seems Confused

**Check**:
1. Is CLAUDE.md up-to-date? (architecture changed?)
2. Is MEMORY.md accurate? (outdated info?)
3. Is project structure reflected in CLAUDE.md?

**Fix**:
- Update CLAUDE.md with current architecture
- Update MEMORY.md with current state
- Use /remember to add missing context

<!-- section_id: "d43f4603-6dbd-44f9-8e9b-264ac5d44e19" -->
### Running Out of Tokens Quickly

**Check**:
1. Is CLAUDE.md too verbose?
2. Are you loading full codebase with @folder?
3. Are compacted items being evicted too aggressively?

**Fix**:
- Trim CLAUDE.md to essentials
- Use @file instead of @folder
- Use subagents to parallelize large work

<!-- section_id: "6c778a82-1682-4543-a57b-4b47b911b7cc" -->
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

<!-- section_id: "f64fae5a-33da-4d13-ab39-37b37c2c3b22" -->
## Summary: The System Works When

✅ **CLAUDE.md is accurate** (reflects current architecture, rules, available skills)
✅ **MEMORY.md is current** (most important info in first 200 lines)
✅ **Skills are well-documented** (clear WHEN/WHEN NOT)
✅ **Project structure is logical** (easy to @reference)
✅ **MCP servers are configured** (external tools available)
✅ **You parallelize when beneficial** (subagents for large tasks)
✅ **Context is lean** (not bloated, let auto-compaction work)

The system fails when any of these are missing or outdated.
