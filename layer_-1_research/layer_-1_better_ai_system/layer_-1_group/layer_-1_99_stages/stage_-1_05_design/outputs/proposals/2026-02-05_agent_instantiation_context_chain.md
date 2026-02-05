# Agent Instantiation & Context Chain Proposal

**Date**: 2026-02-05
**Layer**: -1 (Research)
**Stage**: 05 (Design)
**Status**: Proposed

---

## Problem Statement

Current context diagrams show **what** context exists and **how** it flows, but they don't show:

1. **What agents start with** - The foundational context present at instantiation
2. **How working directory affects context** - Different starting points = different context
3. **The full chain** - From system prompt → tools → personal files → skills → jsonld → sub_layers → sub-agents
4. **Decision points** - Where agents decide to load more context or spawn sub-agents

---

## Diagram: Agent Instantiation & Context Chain

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│              AGENT INSTANTIATION & CONTEXT CHAIN                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

                              AGENT INSTANTIATED
                              (claude code starts)
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TIER 0: IMMUTABLE FOUNDATION                                                     │
│ ════════════════════════════                                                     │
│                                                                                  │
│ Source: Anthropic (cannot be changed by user)                                    │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │                         SYSTEM PROMPT                                        │ │
│ │  • Model identity (Claude)                                                   │ │
│ │  • Safety rules and boundaries                                               │ │
│ │  • Tool usage instructions                                                   │ │
│ │  • Ethical guidelines                                                        │ │
│ │                                                                              │ │
│ │  Status: LOCKED - User cannot modify                                         │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TIER 1: PLATFORM LAYER                                                           │
│ ══════════════════════                                                           │
│                                                                                  │
│ Source: Claude Code application                                                  │
│                                                                                  │
│ ┌──────────────────────────┐  ┌──────────────────────────┐                      │
│ │      BUILT-IN TOOLS      │  │      MCP SERVERS         │                      │
│ │  • Read, Write, Edit     │  │  From: ~/.claude/        │                      │
│ │  • Bash, Glob, Grep      │  │        settings.json     │                      │
│ │  • Task (subagents)      │  │                          │                      │
│ │  • WebFetch, WebSearch   │  │  • mcp__perplexity__*    │                      │
│ │  • AskUserQuestion       │  │  • mcp__playwright__*    │                      │
│ │  • Skill                 │  │  • mcp__canvas__*        │                      │
│ │  • ...                   │  │  • mcp__ide__*           │                      │
│ └──────────────────────────┘  └──────────────────────────┘                      │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │  ~/.claude/settings.json - MCP configs, permissions, model prefs             │ │
│ │  Project .claude/settings.json - Project-specific permissions                │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TIER 2: GLOBAL PERSONAL SYSTEM PROMPT                                            │
│ ═════════════════════════════════════                                            │
│                                                                                  │
│ Source: User's global configuration                                              │
│ Auto-loaded: YES (Claude Code handles)                                           │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │  ~/.claude/CLAUDE.md                                                         │ │
│ │  • Machine-level rules                                                       │ │
│ │  • Universal behaviors                                                       │ │
│ │  • Critical rules (modification protocol, commit rules)                      │ │
│ │  • Self-compliance checklist                                                 │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TIER 3: PATH-BASED CONTEXT (varies by working directory)                         │
│ ════════════════════════════════════════════════════════                         │
│                                                                                  │
│ Claude Code traverses from ~ to working directory, loading each CLAUDE.md       │
│                                                                                  │
│ ╔═══════════════════════════════════════════════════════════════════════════╗   │
│ ║  WORKING DIR: ~/                                                           ║   │
│ ║  Loads: ~/CLAUDE.md                                                        ║   │
│ ║  Context: User root, workspace pointers                                    ║   │
│ ╚═══════════════════════════════════════════════════════════════════════════╝   │
│                                                                                  │
│ ╔═══════════════════════════════════════════════════════════════════════════╗   │
│ ║  WORKING DIR: ~/dawson-workspace/                                          ║   │
│ ║  Loads: ~/CLAUDE.md → ~/dawson-workspace/CLAUDE.md                         ║   │
│ ║  Context: + Workspace conventions, sync awareness                          ║   │
│ ╚═══════════════════════════════════════════════════════════════════════════╝   │
│                                                                                  │
│ ╔═══════════════════════════════════════════════════════════════════════════╗   │
│ ║  WORKING DIR: ~/dawson-workspace/code/0_layer_universal/                   ║   │
│ ║  Loads: ~/CLAUDE.md → .../dawson-workspace/CLAUDE.md                       ║   │
│ ║         → .../code/CLAUDE.md → .../0_layer_universal/CLAUDE.md             ║   │
│ ║  Context: + Layer-stage framework, universal rules, navigation             ║   │
│ ╚═══════════════════════════════════════════════════════════════════════════╝   │
│                                                                                  │
│ ╔═══════════════════════════════════════════════════════════════════════════╗   │
│ ║  WORKING DIR: .../layer_-1_better_ai_system/layer_0_group/                 ║   │
│ ║  Loads: (all above) + layer_-1_research/CLAUDE.md                          ║   │
│ ║         + layer_-1_better_ai_system/CLAUDE.md                              ║   │
│ ║  Context: + Research project context, feature organization                 ║   │
│ ╚═══════════════════════════════════════════════════════════════════════════╝   │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TIER 4: DIRECTORY-LEVEL CONTEXT                                                  │
│ ═══════════════════════════════                                                  │
│                                                                                  │
│ ┌──────────────────────────┐  ┌──────────────────────────┐                      │
│ │  AUTO-LOADED             │  │  AGENT MUST READ         │                      │
│ │  • CLAUDE.md (in path)   │  │  • index.jsonld          │                      │
│ │  • .claude/settings.json │  │  • AGENTS.md             │                      │
│ │                          │  │  • status.json           │                      │
│ │  Status: ✅              │  │  Status: ⚠️ Optional     │                      │
│ └──────────────────────────┘  └──────────────────────────┘                      │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │  .claude/ FOLDER                                                             │ │
│ │  ├── settings.json      ← Auto-loaded                                        │ │
│ │  ├── skills/            ← Agent discovers via CLAUDE.md or index.jsonld      │ │
│ │  │   └── {skill}/SKILL.md                                                    │ │
│ │  └── schema/*.jsonld    ← Agent discovers via skills                         │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TIER 5: INSTRUCTION-TRIGGERED CONTEXT (Chain Loading)                            │
│ ═════════════════════════════════════════════════════                            │
│                                                                                  │
│ Each file can reference others, creating a CONTEXT CHAIN:                        │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │                                                                              │ │
│ │  CLAUDE.md                                                                   │ │
│ │      │ says: "Read sub_layer_0_04_rules/ for universal rules"               │ │
│ │      ▼                                                                       │ │
│ │  sub_layer_0_04_rules/safety_governance.md                                   │ │
│ │      │ says: "See principles for guidance"                                   │ │
│ │      ▼                                                                       │ │
│ │  sub_layer_0_03_principles/least_privilege.md                                │ │
│ │                                                                              │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │                                                                              │ │
│ │  index.jsonld                                                                │ │
│ │      │ has: trigger:onEntityCreation → skill path                           │ │
│ │      ▼                                                                       │ │
│ │  .claude/skills/entity-creation/SKILL.md                                     │ │
│ │      │ says: "See schema for entityTypes"                                    │ │
│ │      ▼                                                                       │ │
│ │  .claude/schema/layer-stage-schema.jsonld                                    │ │
│ │      │ defines: entityTypes, conventions                                     │ │
│ │      ▼                                                                       │ │
│ │  Agent now has naming conventions for entity creation                        │ │
│ │                                                                              │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│ MARKDOWN ←→ JSONLD ←→ MARKDOWN ←→ JSONLD ... (chain continues)                  │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ TIER 6: AGENT DECISIONS                                                          │
│ ═══════════════════════                                                          │
│                                                                                  │
│ Based on context loaded, agent decides:                                          │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │  DECISION 1: Navigate or Stay?                                               │ │
│ │                                                                              │ │
│ │  ├── Stay (have enough context for task)                                     │ │
│ │  ├── Navigate deeper (nav:children → sub_features, components)               │ │
│ │  ├── Navigate up (nav:parent → broader context)                              │ │
│ │  └── Navigate sideways (nav:siblings → related entities)                     │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │  DECISION 2: Do Myself or Spawn Sub-Agent?                                   │ │
│ │                                                                              │ │
│ │  Do myself if:                                                               │ │
│ │  • Task is within current context                                            │ │
│ │  • Don't need to lose current context                                        │ │
│ │                                                                              │ │
│ │  Spawn sub-agent if:                                                         │ │
│ │  • Task needs different layer's context                                      │ │
│ │  • Want to preserve current context                                          │ │
│ │  • Task is parallelizable                                                    │ │
│ │                                                                              │ │
│ │  Sub-agent process:                                                          │ │
│ │  1. Task tool spawns with working directory                                  │ │
│ │  2. Sub-agent starts at TIER 0, builds own context chain                     │ │
│ │  3. Sub-agent works and returns result                                       │ │
│ │  4. Parent integrates result                                                 │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │  DECISION 3: What On-Demand Context to Load?                                 │ │
│ │                                                                              │ │
│ │  • "Need naming convention" → read conventions.childNaming                   │ │
│ │  • "Need requirements" → follow rel:treeOfNeedsBranch                        │ │
│ │  • "Need stage workflow" → read .claude/skills/{stage}-workflow              │ │
│ │  • "Need deeper detail" → follow nav:children links                          │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## File Format Roles in the Chain

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    FILE FORMATS & THEIR ROLES                                    │
└─────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────┬────────────────────┬────────────────────┬──────────────────┐
│     CLAUDE.md      │    index.jsonld    │     SKILL.md       │  schema.jsonld   │
├────────────────────┼────────────────────┼────────────────────┼──────────────────┤
│                    │                    │                    │                  │
│  PURPOSE:          │  PURPOSE:          │  PURPOSE:          │  PURPOSE:        │
│  Identity, rules,  │  Navigation,       │  Detailed task     │  Type defs,      │
│  human-readable    │  conventions,      │  instructions,     │  validation,     │
│  instructions      │  triggers          │  procedures        │  vocabulary      │
│                    │                    │                    │                  │
├────────────────────┼────────────────────┼────────────────────┼──────────────────┤
│  AUTO-LOADED: ✅   │  AUTO-LOADED: ❌   │  AUTO-LOADED: ❌   │  AUTO-LOADED: ❌ │
│  (Claude Code)     │  (agent reads)     │  (via trigger)     │  (via skill)     │
│                    │                    │                    │                  │
├────────────────────┼────────────────────┼────────────────────┼──────────────────┤
│  BEST FOR:         │  BEST FOR:         │  BEST FOR:         │  BEST FOR:       │
│  • Complex rules   │  • Nav graphs      │  • Procedures      │  • Type systems  │
│  • Identity        │  • Conventions     │  • Validation      │  • Patterns      │
│  • Behaviors       │  • Triggers        │  • Examples        │  • Vocabulary    │
│                    │                    │                    │                  │
├────────────────────┼────────────────────┼────────────────────┼──────────────────┤
│  REFERENCES:       │  REFERENCES:       │  REFERENCES:       │  REFERENCES:     │
│  → rules/          │  → skills/         │  → schema/         │  → (terminal)    │
│  → principles/     │  → children        │  → other md        │                  │
│  → sub_layers/     │  → siblings        │  → jsonld          │                  │
│                    │                    │                    │                  │
└────────────────────┴────────────────────┴────────────────────┴──────────────────┘

                          TYPICAL CHAIN:

    CLAUDE.md ──────▶ index.jsonld ──────▶ SKILL.md ──────▶ schema.jsonld
        │                  │                   │
        ▼                  ▼                   ▼
    rules/*.md        nav:children        other/*.md
    principles/       nav:siblings
    sub_layers/       rel:treeOfNeeds
```

---

## Sub-Agent Spawning

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        SUB-AGENT SPAWNING                                        │
└─────────────────────────────────────────────────────────────────────────────────┘

    PARENT AGENT (layer_0_group/)
           │
           │ Task requires different context
           │
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │  Task(                                                            │
    │    subagent_type="Explore",                                       │
    │    prompt="Research X in layer_1_sub_feature_Y"                   │
    │  )                                                                │
    └──────────────────────────────────────────────────────────────────┘
           │
           │ Sub-agent instantiated
           │
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │  SUB-AGENT CONTEXT CHAIN                                          │
    │                                                                   │
    │  TIER 0: Same system prompt                                       │
    │  TIER 1: Same tools + MCP servers                                 │
    │  TIER 2: Same global CLAUDE.md                                    │
    │  TIER 3: PATH from parent's working directory                     │
    │  TIER 4-6: Sub-agent builds own chain                             │
    │                                                                   │
    │  Key: Sub-agent has FRESH context appropriate to its task         │
    └──────────────────────────────────────────────────────────────────┘
           │
           │ Sub-agent completes
           │
           ▼
    PARENT AGENT (receives result, integrates, continues)
```

---

## Context Summary by Starting Point

| Working Directory | CLAUDE.md Files Loaded | Key Context |
|-------------------|------------------------|-------------|
| `~/` | 1 (user root) | Basic pointers |
| `~/dawson-workspace/` | 2 | + Sync awareness |
| `.../0_layer_universal/` | 4 | + Layer-stage framework |
| `.../layer_-1_better_ai_system/` | 6 | + Research project |
| `.../layer_0_feature_*/` | 7+ | + Feature conventions |

---

## Implementation Plan

### Phase 1: Create Diagram File
- [ ] Create `diagrams/current/agent_instantiation_chain.md`
- [ ] Add to diagrams/index.jsonld

### Phase 2: Working Directory Examples
- [ ] Document 5+ common starting points
- [ ] Show exact context at each

### Phase 3: Integration
- [ ] Reference from context visualization CLAUDE.md
- [ ] Add to onboarding docs

---

## Summary

This diagram shows:

1. **TIER 0-2**: Every agent starts with (immutable + tools + global)
2. **TIER 3**: How working directory determines path-based context
3. **TIER 4**: Directory-level files (auto vs manual)
4. **TIER 5**: How instructions chain to more context (md → jsonld → md → ...)
5. **TIER 6**: Agent decisions (navigate, spawn, load on-demand)

**Key insight**: Working directory determines initial context, instructions create chains.
