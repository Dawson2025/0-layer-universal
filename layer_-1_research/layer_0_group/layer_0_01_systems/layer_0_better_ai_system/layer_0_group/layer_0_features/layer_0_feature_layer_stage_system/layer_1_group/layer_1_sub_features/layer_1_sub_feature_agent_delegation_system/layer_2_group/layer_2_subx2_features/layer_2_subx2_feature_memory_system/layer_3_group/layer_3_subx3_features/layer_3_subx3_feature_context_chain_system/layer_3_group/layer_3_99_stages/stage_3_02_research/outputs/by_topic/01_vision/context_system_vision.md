# Vision — A Complete AI Context System

## What This Document Is

A vision for what's possible: a context system where AI agents always have the right context at the right time — not too much, not too little — and where the system itself is maintainable, traversable, and works across every AI tool.

---

## The End State

An AI agent opens a session. Within seconds, it knows:
- **Where it is** — which project, layer, stage, and role it's operating in
- **What rules apply** — critical rules always present, situational rules loaded on entry
- **What it can do** — skills, tools, and workflows available for this specific context
- **What happened before** — episodic memory from prior sessions, hand-off notes, status

It knows all of this without loading thousands of lines of context. The static footprint is small. Everything else is a reference away — loaded precisely when needed, at the right level of detail.

---

## Two Types of Context, Sharply Separated

### Static Context (Always Present)

The foundation. Loaded into every API message, every session, every tool. This is the floor — what the agent can never forget.

**What belongs here:**
- Identity: who you are, what layer/stage you're in, what your scope is
- Critical rules: the immutable rules that apply everywhere (modification protocol, commit rules, documentation protocol)
- Navigation pointers: how to find dynamic context (not the context itself, just the map)
- Trigger table: situation → action mappings ("when X, load Y")

**What does NOT belong here:**
- Detailed procedures (move to skills)
- Full directory trees (move to on-demand reads)
- Duplicated content across files (single source of truth)
- Ceremonial annotations that no runtime enforces

**Target: <400 lines total** across the entire static chain (all parent files combined). Currently at ~717 — nearly half is bloat that can be eliminated.

### Dynamic Context (Loaded When Needed)

The depth. Pulled in on-demand through reference chains. The agent follows pointers from static context to load exactly what it needs for the current task.

**Loading mechanisms:**
- **Path-specific rules** — auto-activate when the agent enters a matching directory
- **Skills** — full instructions loaded only when a skill is invoked
- **@import references** — CLAUDE.md points to detailed docs, loaded on first access
- **Child context files** — deeper directories load their own context on entry
- **Episodic memory** — topic files loaded when resuming prior work
- **Selective graph navigation** — query structured definitions for specific nodes (2-5% of file)

**The key principle:** Static context tells the agent *that* something exists and *when* to load it. Dynamic context provides the *how*.

---

## Reference Chains — The Right Detail at the Right Depth

The system uses layered references so context resolves progressively — from overview to detail — and the agent stops at the level it needs.

```
Level 0: Static trigger (always present, ~1-2 lines)
  "When creating entities, load skill: /entity-creation"

    Level 1: Skill summary (loaded on match, ~10-20 lines)
      WHEN/WHEN NOT conditions, high-level steps, key constraints

        Level 2: Full skill content (loaded on invocation, ~50-200 lines)
          Complete procedures, templates, examples, edge cases

            Level 3: Supporting references (loaded if needed)
              Linked docs, knowledge base articles, external sources
```

The agent doesn't load Level 2 until it's actually doing the work. It doesn't load Level 3 unless Level 2 says "see also." Each level adds detail without waste.

**Reference chain rules:**
1. Every reference must be reachable within 5 hops from static context
2. Each hop should narrow scope (general → specific)
3. No circular references — chains flow downward/inward
4. Every chain terminates at an actionable leaf (a procedure, a template, a rule)

---

## Context Chains — How Context Flows Through the Hierarchy

The layer-stage hierarchy itself is a context chain. Each level inherits from its parent and can override or extend.

```
Global context (~/.claude/CLAUDE.md)
  │  Critical rules, universal identity
  │
  ├── User root (~/CLAUDE.md)
  │     Key locations, workspace awareness
  │
  ├── Workspace (~/dawson-workspace/CLAUDE.md)
  │     Sync awareness, project locations
  │
  ├── Code root (~/dawson-workspace/code/CLAUDE.md)
  │     Code-specific context, primary system pointer
  │
  └── Layer-stage root (0_layer_universal/CLAUDE.md)
        │  Triggers, session workflow, navigation
        │
        ├── layer_0/ — Universal rules, knowledge, principles
        ├── layer_1/ — Project-specific context
        └── layer_-1/ — Research context
              │
              └── project/ → feature/ → sub-feature/ → stage/
                    Each level adds its own identity, scope, triggers
```

**Inheritance model:**
- Child inherits all parent context (automatic — tool loads parent chain)
- Child can extend (add new rules, triggers, skills)
- Child can override (more specific instructions replace more general)
- Critical/safety rules cannot be overridden without explicit approval

**The result:** An agent working in `stage_02_research` of a specific sub-feature automatically has the full chain — from global rules down to stage-specific procedures — without any single file being bloated.

---

## AI Traversal — The Agent Navigates Its Own Context

The system isn't just passively loaded — the agent actively navigates it. On session start, the agent:

1. **Reads the static chain** — automatic, tool-provided
2. **Identifies its position** — layer, stage, project, role
3. **Checks trigger table** — does the current task match any triggers?
4. **Loads matching dynamic context** — skills, rules, references
5. **Begins work** with precisely the context it needs

During work, the agent can:
- **Descend** into child contexts when entering subdirectories
- **Query** structured definitions for specific information (selective navigation)
- **Load** additional skills or references as the task evolves
- **Follow** reference chains to deeper detail when surface-level isn't enough

This traversal is guided by the static context — the trigger table and navigation pointers act as a map the agent follows.

---

## AI Maintenance — The System Updates Itself

A context system that requires constant manual curation is unsustainable. The vision includes mechanisms for the AI to maintain its own context:

### What the AI Can Update
- **Episodic memory** — session records, what was done, decisions made
- **Status tracking** — stage progress, task completion, blockers
- **Hand-off documents** — context for the next session or agent
- **Dynamic references** — updating pointers when files move or change

### What Requires Human Approval
- **Critical rules** — the modification protocol requires diagram + approval
- **Structural changes** — adding/removing layers, stages, entities
- **Source-of-truth files** — 0AGNOSTIC.md edits trigger regeneration

### Automated Maintenance
- **Transpiler** — regenerates tool-specific files from source of truth (0AGNOSTIC.md → CLAUDE.md, AGENTS.md, GEMINI.md)
- **Integration summaries** — auto-generated markdown from structured definitions (.gab.jsonld → .integration.md)
- **Sync scripts** — episodic memory sync, agnostic sync, keeping derived files current

### Self-Healing Properties
- If a reference chain breaks (file moved/deleted), the agent can detect the broken link and flag it
- If static context exceeds budget, the system can identify candidates for demotion to dynamic context
- If a skill description drifts from its source definition, the transpiler corrects it on next run

---

## Tool Agnosticism — One System, Every AI Tool

The context system must work across Claude Code, Cursor, Codex CLI, Gemini CLI, Windsurf, and any future tool. This means:

### The Agnostic Layer

```
0AGNOSTIC.md  ← Single source of truth (tool-neutral)
      │
      │  agnostic-sync.sh
      │
      ├── CLAUDE.md    (Claude Code format)
      ├── AGENTS.md    (Codex CLI format)
      ├── GEMINI.md    (Gemini CLI format)
      ├── OPENAI.md    (OpenAI format)
      └── .cursorrules (Cursor format)
```

**0AGNOSTIC.md** contains the universal context: identity, rules, triggers, navigation. The sync script translates this into each tool's native format. Edit once, deploy everywhere.

### What's Shared vs. Tool-Specific

| Shared (in 0AGNOSTIC.md) | Tool-Specific (in .1merge/) |
|--------------------------|----------------------------|
| Identity, scope, role | Tool-specific syntax (@import, paths: frontmatter) |
| Critical rules | Tool-specific features (skills, rules files, commands) |
| Navigation pointers | Tool-specific capabilities |
| Trigger tables | Override format and structure |
| Layer-stage hierarchy | Integration patterns |

### The .1merge/ Override System

Tool-specific needs are handled by a three-tier merge:
1. **Synced content** — auto-generated from 0AGNOSTIC.md (base)
2. **Overrides** — tool-specific modifications to synced content
3. **Additions** — tool-specific content not in the agnostic source

This means each tool gets the full shared context PLUS its own specific features, without polluting the agnostic source.

### Cross-Tool Context Portability

When switching between tools on the same project:
- The same 0AGNOSTIC.md is the source for all
- Each tool reads its own generated file (CLAUDE.md, AGENTS.md, etc.)
- Episodic memory, hand-offs, and status files are tool-neutral (plain markdown)
- Skills concepts translate across tools (Claude Code skills ≈ Codex skills ≈ Cursor rules)
- The layer-stage structure is universal — it's just directories and files

---

## What Makes This System Good

### Lean Static, Rich Dynamic
The agent always has its critical rules and navigation map. Everything else is a reference away. No context budget wasted on information that isn't relevant to the current task.

### Progressive Disclosure
Context resolves from general to specific. The agent starts with an overview and drills into detail only when the task requires it. Each level of the reference chain adds precision without redundancy.

### Self-Documenting
The hierarchy itself documents the system. Where a file lives tells you what it is: which layer, which stage, which feature. Navigation is structural, not dependent on remembering paths.

### Maintainable
Automated sync keeps derived files current. Source-of-truth pattern (0AGNOSTIC.md) prevents drift. The AI maintains its own session records and status. Human intervention is reserved for structural decisions.

### Tool-Agnostic
One source, many outputs. Switch tools without losing context. The system adapts to each tool's format while maintaining a universal core.

### Traversable
The agent can navigate the system — up to parent context, down to child context, sideways to related features. Navigation is explicit (trigger tables, pointers) not implicit (hoping the agent figures it out).

---

## Current Gaps Between Here and the Vision

| Gap | Current State | Vision State |
|-----|--------------|--------------|
| Static context budget | 717 lines (bloated) | <400 lines (lean) |
| Dynamic loading | Ad-hoc, inconsistent | Systematic via triggers, reference chains |
| Skill invocation | Probabilistic, unreliable | Multi-avenue redundancy (jq + descriptions + integration summaries) |
| Agnostic sync | Exists, basic | Full coverage with .1merge/ overrides |
| AI self-maintenance | Manual episodic memory | Automated session records, status updates |
| Reference chains | Implicit (agent discovers) | Explicit (trigger tables, 5-hop maximum) |
| Cross-tool portability | Partial (CLAUDE.md only) | Full (all major tools, shared episodic memory) |

---

## Guiding Principles

1. **The agent should never have to guess** — if context exists, there's a clear path to it
2. **Static context is precious** — every line must earn its place
3. **References over duplication** — say it once, point to it many times
4. **The hierarchy is the navigation** — directory structure = context structure
5. **Source of truth is singular** — 0AGNOSTIC.md for shared context, .gab.jsonld for agent definitions
6. **Automation over manual curation** — sync scripts, transpilers, and the AI itself maintain the system
7. **Progressive detail** — overview first, depth on demand
8. **Tool-neutral by default, tool-specific by exception** — shared core, targeted overrides

---

*Vision document for the context chain system*
*Created: 2026-02-16*
