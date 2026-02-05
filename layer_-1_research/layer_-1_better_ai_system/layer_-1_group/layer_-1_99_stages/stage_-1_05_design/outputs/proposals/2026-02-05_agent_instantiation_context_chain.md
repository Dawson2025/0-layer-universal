# Agent Instantiation & Context Chain Proposal

**Date**: 2026-02-05
**Layer**: -1 (Research)
**Stage**: 05 (Design)
**Status**: Proposed

---

## Problem Statement

Current context visualization diagrams show **what** context exists and **how** it flows, but they don't show:

1. **What agents start with** when instantiated at a given location
2. **The complete boot sequence** from system prompt to loaded context
3. **How foundational context leads to loading more context**
4. **Decision points** where agents choose to load more or spawn sub-agents

We need a diagram that shows the **complete agent context chain** from instantiation to full operation.

---

## Proposed Diagram: Agent Instantiation & Context Chain

### Purpose

Answer: "When an agent starts at location X, what context does it have and how does it get more?"

### What It Shows

1. **Immutable foundation** - System prompt we can't change
2. **Platform layer** - Claude Code tools, MCP servers
3. **Global layer** - ~/.claude/ configuration
4. **Path-based layer** - CLAUDE.md files in path to working directory
5. **Directory layer** - Local context files (.claude/, index.jsonld)
6. **Triggered layer** - Context loaded by triggers
7. **On-demand layer** - Context loaded by agent decisions
8. **Delegation layer** - Sub-agent instantiation

---

## The Complete Context Chain

### Layer 0: Immutable System Prompt (Anthropic)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 0: IMMUTABLE SYSTEM PROMPT                                                 │
│ ════════════════════════════════                                                 │
│                                                                                  │
│ Source: Anthropic (cannot be changed)                                            │
│                                                                                  │
│ Contains:                                                                        │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ • Model identity and capabilities                                            │ │
│ │ • Safety guidelines and refusals                                             │ │
│ │ • Base behaviors and ethics                                                  │ │
│ │ • Tool usage instructions                                                    │ │
│ │ • Output formatting defaults                                                 │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│ Status: ✅ Always present, cannot modify                                         │
│ Agent sees: Implicitly, shapes all behavior                                      │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
```

### Layer 1: Platform Layer (Claude Code)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: PLATFORM LAYER (Claude Code)                                            │
│ ═════════════════════════════════════                                            │
│                                                                                  │
│ Source: Claude Code CLI application                                              │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ BUILT-IN TOOLS                                                             │   │
│ │ ─────────────                                                              │   │
│ │ • Read, Write, Edit (file operations)                                      │   │
│ │ • Bash (command execution)                                                 │   │
│ │ • Glob, Grep (search)                                                      │   │
│ │ • Task (sub-agent spawning)                                                │   │
│ │ • WebFetch, WebSearch (web access)                                         │   │
│ │ • AskUserQuestion (interaction)                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ MCP SERVERS & TOOLS                                                        │   │
│ │ ────────────────────                                                       │   │
│ │ Configured in: ~/.claude/settings.json or project .claude/settings.json   │   │
│ │                                                                            │   │
│ │ Examples:                                                                  │   │
│ │ • mcp__perplexity__* (research tools)                                      │   │
│ │ • mcp__canvas__* (Canvas LMS tools)                                        │   │
│ │ • mcp__playwright__* (browser automation)                                  │   │
│ │ • mcp__claude-in-chrome__* (Chrome extension)                              │   │
│ │ • mcp__ide__* (IDE integration)                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ ENVIRONMENT INFO                                                           │   │
│ │ ────────────────                                                           │   │
│ │ • Working directory                                                        │   │
│ │ • Platform (linux/mac/windows)                                             │   │
│ │ • Git repo status                                                          │   │
│ │ • Today's date                                                             │   │
│ │ • Model name                                                               │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ Status: ✅ Always present when using Claude Code                                 │
│ Agent sees: In system prompt, available for use                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
```

### Layer 2: Global User Configuration

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 2: GLOBAL USER CONFIGURATION                                               │
│ ══════════════════════════════════                                               │
│                                                                                  │
│ Source: ~/.claude/ directory                                                     │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ ~/.claude/CLAUDE.md                                                        │   │
│ │ ─────────────────────                                                      │   │
│ │ • Machine-level rules (CRITICAL rules that apply everywhere)               │   │
│ │ • Universal behaviors                                                      │   │
│ │ • Global settings                                                          │   │
│ │ • Cross-project conventions                                                │   │
│ │                                                                            │   │
│ │ Loaded: ✅ Automatically by Claude Code                                    │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ ~/.claude/settings.json                                                    │   │
│ │ ─────────────────────────                                                  │   │
│ │ • MCP server configurations                                                │   │
│ │ • Permission settings                                                      │   │
│ │ • Default behaviors                                                        │   │
│ │                                                                            │   │
│ │ Loaded: ✅ Automatically by Claude Code                                    │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ Status: ✅ Loaded at session start                                               │
│ Agent sees: As part of system context                                            │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
```

### Layer 3: Path-Based Context Chain

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 3: PATH-BASED CONTEXT CHAIN                                                │
│ ═════════════════════════════════                                                │
│                                                                                  │
│ Source: CLAUDE.md files from ~ to working directory                              │
│                                                                                  │
│ Claude Code traverses path and loads each CLAUDE.md:                             │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │                                                                            │   │
│ │   ~/CLAUDE.md                                                              │   │
│ │       │ • User root context                                                │   │
│ │       │ • Workspace pointers                                               │   │
│ │       ▼                                                                    │   │
│ │   ~/dawson-workspace/CLAUDE.md                                             │   │
│ │       │ • Workspace conventions                                            │   │
│ │       │ • Sync awareness                                                   │   │
│ │       ▼                                                                    │   │
│ │   ~/dawson-workspace/code/CLAUDE.md                                        │   │
│ │       │ • Code root context                                                │   │
│ │       │ • Project pointers                                                 │   │
│ │       ▼                                                                    │   │
│ │   0_layer_universal/CLAUDE.md                                              │   │
│ │       │ • Layer-stage rules                                                │   │
│ │       │ • Universal conventions                                            │   │
│ │       │ • Sub-layer navigation                                             │   │
│ │       ▼                                                                    │   │
│ │   layer_-1_research/CLAUDE.md                                              │   │
│ │       │ • Research layer context                                           │   │
│ │       ▼                                                                    │   │
│ │   layer_-1_better_ai_system/CLAUDE.md                                      │   │
│ │       │ • Project-specific context                                         │   │
│ │       ▼                                                                    │   │
│ │   (continues to working directory)                                         │   │
│ │                                                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ Inheritance: Each level inherits from parent, can extend/override               │
│ Status: ✅ Loaded automatically by Claude Code                                   │
│ Agent sees: Merged context from all levels                                       │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
```

### Layer 4: Working Directory Context

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 4: WORKING DIRECTORY CONTEXT                                               │
│ ══════════════════════════════════                                               │
│                                                                                  │
│ Source: Files in working directory                                               │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ index.jsonld                                                               │   │
│ │ ────────────                                                               │   │
│ │ • Navigation graph (nav:parent, nav:children, nav:siblings)                │   │
│ │ • Conventions (childNaming, layer numbers)                                 │   │
│ │ • Triggers (onEntityCreation, onStageEnter)                                │   │
│ │ • Tree of needs links                                                      │   │
│ │                                                                            │   │
│ │ Loaded: ⚠️ Agent should read, but not automatic                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ .claude/ directory                                                         │   │
│ │ ─────────────────                                                          │   │
│ │                                                                            │   │
│ │ .claude/settings.json                                                      │   │
│ │ • Project-specific MCP servers                                             │   │
│ │ • Project permissions                                                      │   │
│ │ Loaded: ✅ Automatic                                                       │   │
│ │                                                                            │   │
│ │ .claude/skills/                                                            │   │
│ │ • Workflow skills (SKILL.md files)                                         │   │
│ │ • Stage-specific workflows                                                 │   │
│ │ • Entity creation skill                                                    │   │
│ │ Loaded: ⚠️ On-demand or triggered                                          │   │
│ │                                                                            │   │
│ │ .claude/commands/                                                          │   │
│ │ • Custom slash commands                                                    │   │
│ │ Loaded: ✅ Available for invocation                                        │   │
│ │                                                                            │   │
│ │ .claude/hooks/                                                             │   │
│ │ • Pre/post action hooks                                                    │   │
│ │ Loaded: ✅ Automatic                                                       │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ Other context files                                                        │   │
│ │ ────────────────────                                                       │   │
│ │ • AGENTS.md - Multi-agent coordination info                                │   │
│ │ • 0AGNOSTIC.md - Platform-agnostic context                                 │   │
│ │ • status.json - Current state (dynamic)                                    │   │
│ │                                                                            │   │
│ │ Loaded: ⚠️ Agent should read, but not automatic                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ Status: Partially automatic, partially agent-driven                              │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
```

### Layer 5: Triggered Context Loading

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 5: TRIGGERED CONTEXT LOADING                                               │
│ ══════════════════════════════════                                               │
│                                                                                  │
│ Source: Triggers defined in index.jsonld → load additional context              │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ TRIGGER: onEntityCreation                                                  │   │
│ │ ─────────────────────────────                                              │   │
│ │                                                                            │   │
│ │ When: Agent creates new directory/file                                     │   │
│ │                                                                            │   │
│ │ Loads:                                                                     │   │
│ │ ├── .claude/skills/entity-creation/SKILL.md                                │   │
│ │ │   └── Contains: Naming conventions, validation rules                     │   │
│ │ │                                                                          │   │
│ │ ├── conventions.childNaming from parent index.jsonld                       │   │
│ │ │   └── Contains: Pattern, example, layer numbers                          │   │
│ │ │                                                                          │   │
│ │ └── entityTypes from schema                                                │   │
│ │     └── Contains: Valid types and patterns                                 │   │
│ │                                                                            │   │
│ │ Status: ⚠️ Defined but not auto-enforced                                   │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ TRIGGER: onStageEnter                                                      │   │
│ │ ────────────────────────                                                   │   │
│ │                                                                            │   │
│ │ When: Agent enters stage_*_* directory                                     │   │
│ │                                                                            │   │
│ │ Loads:                                                                     │   │
│ │ ├── .claude/skills/{stage}-workflow/SKILL.md                               │   │
│ │ │   └── Contains: Stage-specific workflow guidance                         │   │
│ │ │                                                                          │   │
│ │ ├── stage CLAUDE.md                                                        │   │
│ │ │   └── Contains: Stage identity, behaviors                                │   │
│ │ │                                                                          │   │
│ │ └── hand_off_documents/incoming/                                           │   │
│ │     └── Contains: Tasks from parent                                        │   │
│ │                                                                            │   │
│ │ Status: ⚠️ Defined but not auto-enforced                                   │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ TRIGGER: onSessionStart                                                    │   │
│ │ ──────────────────────────                                                 │   │
│ │                                                                            │   │
│ │ When: New session begins                                                   │   │
│ │                                                                            │   │
│ │ Loads:                                                                     │   │
│ │ ├── CLAUDE.md (already automatic)                                          │   │
│ │ ├── index.jsonld (should be automatic)                                     │   │
│ │ └── status.json (for current state)                                        │   │
│ │                                                                            │   │
│ │ Status: Partially automatic                                                │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
```

### Layer 6: On-Demand Context Loading

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 6: ON-DEMAND CONTEXT LOADING                                               │
│ ══════════════════════════════════                                               │
│                                                                                  │
│ Source: Agent follows links in loaded context                                    │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ FOLLOWING nav: LINKS                                                       │   │
│ │ ────────────────────────                                                   │   │
│ │                                                                            │   │
│ │ index.jsonld contains:                                                     │   │
│ │                                                                            │   │
│ │ nav:parent → "../"                                                         │   │
│ │ └── Agent reads parent's index.jsonld for broader context                  │   │
│ │                                                                            │   │
│ │ nav:children → ["layer_1_sub_feature_*/"]                                  │   │
│ │ └── Agent explores children for detailed context                           │   │
│ │                                                                            │   │
│ │ nav:siblings → ["../layer_1_sub_feature_*/"]                               │   │
│ │ └── Agent finds related entities                                           │   │
│ │                                                                            │   │
│ │ nav:skills → ".claude/skills/"                                             │   │
│ │ └── Agent loads skill for specific task                                    │   │
│ │                                                                            │   │
│ │ nav:stages → "layer_0_group/layer_0_99_stages/"                            │   │
│ │ └── Agent navigates to appropriate stage                                   │   │
│ │                                                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ FOLLOWING rel: LINKS                                                       │   │
│ │ ────────────────────────                                                   │   │
│ │                                                                            │   │
│ │ rel:treeOfNeedsBranch → links to requirements                              │   │
│ │ └── Agent understands why this entity exists                               │   │
│ │                                                                            │   │
│ │ rel:satisfiesNeed → links to specific need                                 │   │
│ │ └── Agent understands what problem this solves                             │   │
│ │                                                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ LOADING DETAILED CONTEXT                                                   │   │
│ │ ──────────────────────────                                                 │   │
│ │                                                                            │   │
│ │ SKILL.md can reference:                                                    │   │
│ │ ├── Other skills: "../other-skill/SKILL.md"                                │   │
│ │ ├── JSON-LD files: "index.jsonld" for navigation                           │   │
│ │ ├── Schema files: ".claude/schema/*.jsonld"                                │   │
│ │ └── Documentation: "README.md", detailed docs                              │   │
│ │                                                                            │   │
│ │ index.jsonld can reference:                                                │   │
│ │ ├── CLAUDE.md for identity context                                         │   │
│ │ ├── SKILL.md for workflow context                                          │   │
│ │ └── Other index.jsonld for navigation                                      │   │
│ │                                                                            │   │
│ │ Markdown may be better for:                                                │   │
│ │ ├── Complex instructions (model performs better)                           │   │
│ │ ├── Examples and code snippets                                             │   │
│ │ └── Detailed explanations                                                  │   │
│ │                                                                            │   │
│ │ JSON-LD is better for:                                                     │   │
│ │ ├── Navigation graphs                                                      │   │
│ │ ├── Structured data (conventions, triggers)                                │   │
│ │ └── Machine-parseable relationships                                        │   │
│ │                                                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ Status: Agent-driven, based on task needs                                        │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
```

### Layer 7: Sub-Agent Delegation

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 7: SUB-AGENT DELEGATION                                                    │
│ ═════════════════════════════                                                    │
│                                                                                  │
│ Source: Agent decides to spawn sub-agents for specific tasks                     │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ DECISION POINTS                                                            │   │
│ │ ───────────────                                                            │   │
│ │                                                                            │   │
│ │ Agent may spawn sub-agent when:                                            │   │
│ │ • Task requires different layer context                                    │   │
│ │ • Task is complex and benefits from isolation                              │   │
│ │ • Parallel work is possible                                                │   │
│ │ • Different expertise is needed                                            │   │
│ │                                                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ SUB-AGENT INSTANTIATION                                                    │   │
│ │ ───────────────────────────                                                │   │
│ │                                                                            │   │
│ │ Using Task tool:                                                           │   │
│ │                                                                            │   │
│ │ Task(                                                                      │   │
│ │   subagent_type: "Explore" | "Plan" | "Bash" | etc.                        │   │
│ │   prompt: "Task description with context"                                  │   │
│ │   working_directory: "/path/to/target/"  ◄── Different location!           │   │
│ │ )                                                                          │   │
│ │                                                                            │   │
│ │ Sub-agent gets:                                                            │   │
│ │ • Fresh Layer 0-4 context for NEW working directory                        │   │
│ │ • Task description from parent agent                                       │   │
│ │ • NO memory of parent's session                                            │   │
│ │                                                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ ┌───────────────────────────────────────────────────────────────────────────┐   │
│ │ HANDOFF PATTERN                                                            │   │
│ │ ───────────────                                                            │   │
│ │                                                                            │   │
│ │ Parent Agent                        Sub-Agent                              │   │
│ │ ────────────                        ─────────                              │   │
│ │      │                                   │                                 │   │
│ │      │ Write task to:                    │                                 │   │
│ │      │ hand_off_documents/outgoing/      │                                 │   │
│ │      │ to_below/                         │                                 │   │
│ │      │──────────────────────────────────▶│                                 │   │
│ │      │                                   │ Reads from:                     │   │
│ │      │                                   │ hand_off_documents/incoming/    │   │
│ │      │                                   │ from_above/                     │   │
│ │      │                                   │                                 │   │
│ │      │                                   │ Does work...                    │   │
│ │      │                                   │                                 │   │
│ │      │                                   │ Write result to:                │   │
│ │      │                                   │ hand_off_documents/outgoing/    │   │
│ │      │◀──────────────────────────────────│ to_above/                       │   │
│ │      │ Reads from:                       │                                 │   │
│ │      │ hand_off_documents/incoming/      │                                 │   │
│ │      │ from_below/                       │                                 │   │
│ │      │                                   │                                 │   │
│ │      ▼                                   ▼                                 │   │
│ │                                                                            │   │
│ └───────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│ Status: Agent-driven delegation                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Example: Agent Instantiation at Different Locations

### Example 1: Starting at ~/

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ WORKING DIRECTORY: ~/                                                            │
└─────────────────────────────────────────────────────────────────────────────────┘

CONTEXT LOADED:
├── Layer 0: Anthropic system prompt ✅
├── Layer 1: Claude Code tools, MCP servers ✅
├── Layer 2: ~/.claude/CLAUDE.md, ~/.claude/settings.json ✅
├── Layer 3: ~/CLAUDE.md ✅
├── Layer 4: (none - no project context) ⚠️
├── Layer 5: (no triggers) ⚠️
└── Layer 6: (limited navigation) ⚠️

AGENT KNOWS:
• Universal rules from ~/.claude/CLAUDE.md
• User preferences
• Where workspaces are (pointers in ~/CLAUDE.md)

AGENT DOESN'T KNOW:
• Project-specific context
• Layer-stage conventions
• Current tasks or state
```

### Example 2: Starting at ~/dawson-workspace/code/0_layer_universal/

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ WORKING DIRECTORY: ~/dawson-workspace/code/0_layer_universal/                    │
└─────────────────────────────────────────────────────────────────────────────────┘

CONTEXT LOADED:
├── Layer 0: Anthropic system prompt ✅
├── Layer 1: Claude Code tools, MCP servers ✅
├── Layer 2: ~/.claude/CLAUDE.md, ~/.claude/settings.json ✅
├── Layer 3: ✅
│   ├── ~/CLAUDE.md
│   ├── ~/dawson-workspace/CLAUDE.md
│   ├── ~/dawson-workspace/code/CLAUDE.md
│   └── ~/dawson-workspace/code/0_layer_universal/CLAUDE.md
├── Layer 4: ✅
│   ├── .claude/settings.json (project MCP servers)
│   ├── (should read index.jsonld) ⚠️
│   └── (should read status.json) ⚠️
├── Layer 5: (triggers available if index.jsonld read) ⚠️
└── Layer 6: (navigation available if index.jsonld read) ⚠️

AGENT KNOWS:
• Universal rules
• Layer-stage conventions
• Sub-layer navigation (rules, knowledge, prompts, principles)
• Modification protocol
• Commit/push rules

AGENT SHOULD ALSO KNOW (if reads index.jsonld):
• Navigation graph
• Conventions for child naming
• Triggers for entity creation
```

### Example 3: Starting at a Feature Directory

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ WORKING DIRECTORY: .../layer_0_feature_context_framework/                        │
└─────────────────────────────────────────────────────────────────────────────────┘

CONTEXT LOADED:
├── Layer 0: Anthropic system prompt ✅
├── Layer 1: Claude Code tools, MCP servers ✅
├── Layer 2: ~/.claude/CLAUDE.md ✅
├── Layer 3: All CLAUDE.md files in path ✅
│   ├── ~/CLAUDE.md
│   ├── .../0_layer_universal/CLAUDE.md
│   ├── .../layer_-1_research/CLAUDE.md
│   └── .../layer_-1_better_ai_system/CLAUDE.md
├── Layer 4: ✅
│   ├── index.jsonld (if read) ⚠️
│   │   ├── conventions.childNaming
│   │   ├── trigger:onEntityCreation
│   │   └── nav:children (sub_features)
│   └── CLAUDE.md (feature identity)
├── Layer 5: Triggers ⚠️
│   └── onEntityCreation → entity-creation skill
└── Layer 6: Navigation available
    ├── nav:parent → layer_0_features/
    ├── nav:children → layer_1_sub_feature_*/
    └── rel:treeOfNeedsBranch → 06_context_flow

AGENT KNOWS:
• Feature identity and purpose
• What sub-features exist
• Tree of needs this addresses

AGENT CAN DO:
• Navigate to sub-features
• Create new sub-features (if reads conventions)
• Understand requirements context
```

---

## Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE AGENT CONTEXT CHAIN                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

                         ┌─────────────────────────┐
                         │    INSTANTIATION        │
                         │    (claude code start)  │
                         └───────────┬─────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                    ▼                ▼                ▼
            ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
            │  Layer 0    │  │  Layer 1    │  │  Layer 2    │
            │  (Immutable)│  │  (Platform) │  │  (Global)   │
            │             │  │             │  │             │
            │ System      │  │ Tools       │  │ ~/.claude/  │
            │ prompt      │  │ MCP servers │  │ CLAUDE.md   │
            │             │  │ Environment │  │ settings    │
            └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
                   │                │                │
                   └────────────────┼────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────────┐
                         │       Layer 3           │
                         │    (Path-based)         │
                         │                         │
                         │  CLAUDE.md chain from   │
                         │  ~ to working directory │
                         └───────────┬─────────────┘
                                     │
                                     ▼
                         ┌─────────────────────────┐
                         │       Layer 4           │
                         │   (Working Directory)   │
                         │                         │
                         │  index.jsonld ⚠️        │
                         │  .claude/skills/ ⚠️     │
                         │  status.json ⚠️         │
                         └───────────┬─────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                    ▼                ▼                ▼
            ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
            │  Layer 5    │  │  Layer 6    │  │  Layer 7    │
            │ (Triggered) │  │ (On-demand) │  │ (Delegation)│
            │             │  │             │  │             │
            │ onCreate ⚠️ │  │ nav: links  │  │ Task tool   │
            │ onEnter ⚠️  │  │ rel: links  │  │ Sub-agents  │
            │ onStart ⚠️  │  │ SKILL.md    │  │ Handoffs    │
            └─────────────┘  └─────────────┘  └─────────────┘

            ✅ = Automatic        ⚠️ = Agent must explicitly read/trigger
```

---

## Implementation Plan

### Phase 1: Diagram Creation
- [ ] Create `agent_instantiation_chain.md` in `diagrams/current/`
- [ ] Create location-specific examples
- [ ] Document the 7 layers

### Phase 2: Integration
- [ ] Update CLAUDE.md files to reference this diagram
- [ ] Add "what you have" section to entry points
- [ ] Document what agents should read at each location

### Phase 3: Enforcement Research
- [ ] Investigate Claude Code hooks for auto-loading index.jsonld
- [ ] Investigate trigger enforcement mechanisms
- [ ] Document gaps between "should load" and "actually loads"

---

## Files to Create

| File | Purpose |
|------|---------|
| `diagrams/current/agent_instantiation_chain.md` | Complete 7-layer chain |
| `diagrams/current/location_examples.md` | Examples at different working directories |

---

## Summary

This diagram shows the **complete picture** of how an agent "boots up":

1. **Immutable foundation** - Can't change (Anthropic system prompt)
2. **Platform** - Claude Code provides (tools, MCP, environment)
3. **Global** - User configures (~/.claude/)
4. **Path-based** - Automatically loaded (CLAUDE.md chain)
5. **Directory** - Should be read (index.jsonld, skills)
6. **Triggered** - Should fire on actions
7. **Delegation** - Agent spawns sub-agents

The key insight: **Layers 0-3 are automatic, Layers 4-7 are agent-driven or should-be-triggered**.

This explains why the naming convention mistake happened: Layer 5 triggers weren't enforced, so the agent never loaded conventions before creating entities.
