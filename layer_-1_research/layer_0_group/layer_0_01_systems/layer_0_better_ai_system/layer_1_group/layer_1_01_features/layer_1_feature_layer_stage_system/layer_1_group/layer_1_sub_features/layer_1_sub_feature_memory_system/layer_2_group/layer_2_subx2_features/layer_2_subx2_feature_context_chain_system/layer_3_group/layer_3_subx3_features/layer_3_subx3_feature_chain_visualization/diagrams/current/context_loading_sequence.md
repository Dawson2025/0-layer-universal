---
resource_id: "34fb76d0-b479-4616-a52d-d5caefc4c540"
resource_type: "document"
resource_name: "context_loading_sequence"
---
# Context Loading Sequence

**Purpose**: Show the exact order in which context loads from session start to end.

---

<!-- section_id: "77f0ebc5-f7f2-42fc-bfd6-4b5a9d1f8217" -->
## Overview: Complete Loading Sequence

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│           CONTEXT LOADING SEQUENCE (Session Start to Working State)             │
└─────────────────────────────────────────────────────────────────────────────────┘

    ════════════════════════════════════════════════════════════════════════════
    PHASE 0: PRE-SESSION (Before Claude Code Starts)
    ════════════════════════════════════════════════════════════════════════════

    User runs: claude (in some directory)
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Working Directory Captured: /home/dawson/.../layer_0_group/              │
    │  This determines ALL path-based context that will load                    │
    └───────────────────────────────────────────────────────────────────────────┘

    ════════════════════════════════════════════════════════════════════════════
    PHASE 1: CLAUDE CODE BOOTSTRAP (Automatic, No User Control)
    ════════════════════════════════════════════════════════════════════════════

    STEP 1.1: System Prompt Injection
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Anthropic's system prompt loaded (immutable)                             │
    │  • Model identity, safety rules, tool instructions                        │
    │  ORDER: 1 (always first)                                                  │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    STEP 1.2: Tool Registration
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Built-in tools registered:                                               │
    │  Read, Write, Edit, Bash, Glob, Grep, Task, WebFetch, WebSearch,         │
    │  AskUserQuestion, Skill, EnterPlanMode, TaskCreate/Update/List...        │
    │  ORDER: 2                                                                 │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    STEP 1.3: MCP Server Connection
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SOURCE: ~/.claude/settings.json                                          │
    │  Connects to configured MCP servers:                                      │
    │  • mcp__perplexity__*                                                     │
    │  • mcp__playwright__*                                                     │
    │  • mcp__canvas__*                                                         │
    │  • mcp__filesystem__*                                                     │
    │  • etc.                                                                   │
    │  ORDER: 3                                                                 │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    STEP 1.4: Global Settings
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SOURCE: ~/.claude/settings.json                                          │
    │  • Permissions, model preferences, denied tools                           │
    │  ORDER: 4                                                                 │
    └───────────────────────────────────────────────────────────────────────────┘

    ════════════════════════════════════════════════════════════════════════════
    PHASE 2: CLAUDE.md CHAIN (Automatic, Path-Based)
    ════════════════════════════════════════════════════════════════════════════

    Claude Code traverses from ~ to working directory, loading each CLAUDE.md

    STEP 2.1: Global CLAUDE.md
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SOURCE: ~/.claude/CLAUDE.md                                              │
    │  • Machine-level rules, universal behaviors                               │
    │  • Critical rules (modification protocol, commit rules)                   │
    │  ORDER: 5                                                                 │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    STEP 2.2: User Root CLAUDE.md
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SOURCE: ~/CLAUDE.md                                                      │
    │  • User root, workspace pointers                                          │
    │  ORDER: 6                                                                 │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    STEP 2.3: Path CLAUDE.md Files (varies by working directory)
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Example: Working dir = .../layer_0_group/                                │
    │                                                                           │
    │  ~/dawson-workspace/CLAUDE.md                    ORDER: 7                 │
    │      ↓                                                                    │
    │  ~/dawson-workspace/code/CLAUDE.md               ORDER: 8                 │
    │      ↓                                                                    │
    │  .../0_layer_universal/CLAUDE.md                 ORDER: 9                 │
    │      ↓                                                                    │
    │  .../layer_-1_research/CLAUDE.md                 ORDER: 10                │
    │      ↓                                                                    │
    │  .../layer_-1_better_ai_system/CLAUDE.md         ORDER: 11                │
    │      ↓                                                                    │
    │  .../layer_0_group/CLAUDE.md (if exists)         ORDER: 12                │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    STEP 2.4: Project Settings
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SOURCE: {working_dir}/.claude/settings.json                              │
    │  • Project-specific permissions                                           │
    │  ORDER: 13                                                                │
    └───────────────────────────────────────────────────────────────────────────┘

    ════════════════════════════════════════════════════════════════════════════
    PHASE 3: SESSION READY (Agent Takes Over)
    ════════════════════════════════════════════════════════════════════════════

    Agent now has all auto-loaded context. From here, agent decides what to read.

    STEP 3.1: User Message Received
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  User sends first message                                                 │
    │  ORDER: 14                                                                │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    STEP 3.2: Agent Reads Additional Context (Optional, Agent-Driven)
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Based on CLAUDE.md instructions, agent MAY read:                         │
    │                                                                           │
    │  • index.jsonld (for navigation, conventions)                             │
    │  • status.json (for current state)                                        │
    │  • AGENTS.md (for delegation rules)                                       │
    │  • sub_layer files (rules, knowledge, etc.)                               │
    │                                                                           │
    │  ORDER: 15+ (varies by task)                                              │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    STEP 3.3: Instruction-Triggered Context (Chain Loading)
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Files reference other files, creating chains:                            │
    │                                                                           │
    │  index.jsonld → trigger:onEntityCreation → SKILL.md → schema.jsonld      │
    │  CLAUDE.md → "see rules/" → rules/*.md                                    │
    │                                                                           │
    │  ORDER: 16+ (varies by chain depth)                                       │
    └───────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "aa6eab70-8513-41cd-8faa-4f1afd503ef9" -->
## Example: Specific Directory Loading

<!-- section_id: "0819ebeb-6ec5-4709-ae45-c9332e4b287c" -->
### Working Directory: `.../layer_0_group/`

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  COMPLETE CONTEXT FOR: .../layer_0_group/                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

ORDER   SOURCE                                          CONTENT
─────   ──────                                          ───────
  1     [Anthropic System Prompt]                       Identity, safety, tools
  2     [Built-in Tools]                                Read, Write, Bash, etc.
  3     ~/.claude/settings.json                         MCP servers
  4     ~/.claude/settings.json                         Global permissions
  5     ~/.claude/CLAUDE.md                             Machine rules
  6     ~/CLAUDE.md                                     User root pointers
  7     ~/dawson-workspace/CLAUDE.md                    Sync awareness
  8     ~/dawson-workspace/code/CLAUDE.md               Code root
  9     .../0_layer_universal/CLAUDE.md                 Layer-stage framework
 10     .../layer_-1_research/CLAUDE.md                 Research layer
 11     .../layer_-1_better_ai_system/CLAUDE.md         Project context
 12     .../layer_0_group/CLAUDE.md                     Feature group (if exists)
 13     .../layer_0_group/.claude/settings.json         Project permissions

─── SESSION READY ───

 14     [User Message]                                  Task arrives
 15+    Agent reads as needed:
        • index.jsonld                                  Navigation, conventions
        • .claude/skills/*/SKILL.md                     Task procedures
        • .claude/schema/*.jsonld                       Type definitions
```

<!-- section_id: "3eb3f89c-ab82-49dd-ab96-c1052742f265" -->
### Working Directory: `~/` (Minimal Context)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  COMPLETE CONTEXT FOR: ~/                                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

ORDER   SOURCE                                          CONTENT
─────   ──────                                          ───────
  1     [Anthropic System Prompt]                       Identity, safety, tools
  2     [Built-in Tools]                                Read, Write, Bash, etc.
  3     ~/.claude/settings.json                         MCP servers
  4     ~/.claude/settings.json                         Global permissions
  5     ~/.claude/CLAUDE.md                             Machine rules
  6     ~/CLAUDE.md                                     User root pointers

─── SESSION READY ───

 7      [User Message]                                  Task arrives

Note: Much less context! No layer-stage framework, no project conventions.
```

---

<!-- section_id: "51d10dcb-7043-4af6-97ea-ae3b61c08632" -->
## Context Loading Summary Table

| Phase | Steps | Source | Auto-loaded? | User Control? |
|-------|-------|--------|--------------|---------------|
| 0 | Working dir capture | CLI invocation | N/A | Yes (user chooses where to run) |
| 1.1 | System prompt | Anthropic | ✅ | ❌ |
| 1.2 | Tools | Claude Code | ✅ | ❌ |
| 1.3 | MCP servers | ~/.claude/settings.json | ✅ | ✅ (configure) |
| 1.4 | Global settings | ~/.claude/settings.json | ✅ | ✅ (configure) |
| 2.1 | Global CLAUDE.md | ~/.claude/CLAUDE.md | ✅ | ✅ (edit file) |
| 2.2 | User CLAUDE.md | ~/CLAUDE.md | ✅ | ✅ (edit file) |
| 2.3 | Path CLAUDE.md | ~ to cwd | ✅ | ✅ (edit files) |
| 2.4 | Project settings | cwd/.claude/ | ✅ | ✅ (configure) |
| 3+ | Agent-driven | Various | ❌ | ❌ (agent decides) |

---

*Last updated: 2026-02-05*
