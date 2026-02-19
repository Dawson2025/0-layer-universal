# Agent Instantiation & Context Chain

**Purpose**: Show what context agents receive at instantiation and how they load more.

---

## Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    AGENT INSTANTIATION & CONTEXT CHAIN                           │
└─────────────────────────────────────────────────────────────────────────────────┘

                              AGENT INSTANTIATED
                              (claude code starts)
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │  TIER 0: System Prompt (immutable)  │
                    │  • Model identity, safety rules     │
                    └─────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │  TIER 1: Tools + MCP Servers        │
                    │  • Built-in tools (Read, Write...)  │
                    │  • MCP from ~/.claude/settings.json │
                    └─────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │  TIER 2: Global CLAUDE.md           │
                    │  • ~/.claude/CLAUDE.md              │
                    │  • Machine-level rules              │
                    └─────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │  TIER 3: Path-Based Context         │
                    │  • All CLAUDE.md files from ~ to cwd│
                    │  • Varies by working directory!     │
                    └─────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │  TIER 4: Directory-Level Context    │
                    │  • Agent reads index.jsonld         │
                    │  • Agent discovers .claude/         │
                    └─────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │  TIER 5: Instruction-Triggered      │
                    │  • Files reference other files      │
                    │  • Creates context chain            │
                    └─────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │  TIER 6: Agent Decisions            │
                    │  • Navigate deeper/up/sideways      │
                    │  • Spawn sub-agent                  │
                    │  • Load on-demand context           │
                    └─────────────────────────────────────┘
```

---

## Working Directory Impact

The agent's working directory determines TIER 3 context:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ WORKING DIRECTORY EXAMPLES                                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════════════════════╗
║  ~/                                                                            ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  CLAUDE.md Chain: ~/.claude/CLAUDE.md → ~/CLAUDE.md                           ║
║  Context: Basic user preferences, workspace pointers                           ║
╚═══════════════════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════════╗
║  ~/dawson-workspace/code/0_layer_universal/                                    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  CLAUDE.md Chain:                                                              ║
║    ~/.claude/CLAUDE.md                                                         ║
║    → ~/CLAUDE.md                                                               ║
║    → ~/dawson-workspace/CLAUDE.md                                              ║
║    → ~/dawson-workspace/code/CLAUDE.md                                         ║
║    → .../0_layer_universal/CLAUDE.md                                           ║
║                                                                                ║
║  Context: Full layer-stage framework, universal rules, navigation              ║
╚═══════════════════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════════╗
║  .../layer_-1_better_ai_system/layer_0_group/                                  ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  CLAUDE.md Chain: (all above) +                                                ║
║    → layer_-1_research/CLAUDE.md                                               ║
║    → layer_-1_better_ai_system/CLAUDE.md                                       ║
║                                                                                ║
║  Context: + Research project context, feature organization, JSON-LD nav        ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Context Chain Loading

Files reference each other, creating chains:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ CONTEXT CHAIN: ENTITY CREATION EXAMPLE                                           │
└─────────────────────────────────────────────────────────────────────────────────┘

  CLAUDE.md (layer_0_group/)
      │
      │ says: "For context navigation, see index.jsonld"
      ▼
  index.jsonld
      │
      │ has: trigger:onEntityCreation → skill path
      ▼
  .claude/skills/entity-creation/SKILL.md
      │
      │ says: "See schema for entityTypes"
      ▼
  .claude/schema/layer-stage-schema.jsonld
      │
      │ defines: entityTypes, naming patterns, conventions
      ▼
  Agent now knows: layer_2_subx2_feature_{name} for sub-features
```

---

## File Format Roles

```
┌────────────────────┬────────────────────┬────────────────────┬──────────────────┐
│     CLAUDE.md      │    index.jsonld    │     SKILL.md       │  schema.jsonld   │
├────────────────────┼────────────────────┼────────────────────┼──────────────────┤
│  Identity, rules,  │  Navigation,       │  Detailed task     │  Type defs,      │
│  human-readable    │  conventions,      │  instructions,     │  validation,     │
│  instructions      │  triggers          │  procedures        │  vocabulary      │
├────────────────────┼────────────────────┼────────────────────┼──────────────────┤
│  AUTO-LOADED: ✅   │  AUTO-LOADED: ❌   │  AUTO-LOADED: ❌   │  AUTO-LOADED: ❌ │
│  (Claude Code)     │  (agent reads)     │  (via trigger)     │  (via skill)     │
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
    │    prompt="Research X in layer_2_subx2_feature_Y"                   │
    │  )                                                                │
    └──────────────────────────────────────────────────────────────────┘
           │
           │ Sub-agent instantiated at PARENT'S working directory
           │
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │  SUB-AGENT CONTEXT CHAIN                                          │
    │                                                                   │
    │  TIER 0: Same system prompt                                       │
    │  TIER 1: Same tools + MCP servers                                 │
    │  TIER 2: Same global CLAUDE.md                                    │
    │  TIER 3: Same PATH-based context (inherits cwd)                   │
    │  TIER 4-6: Sub-agent builds own chain from there                  │
    │                                                                   │
    │  Key: Sub-agent has FRESH context, no parent's conversation       │
    └──────────────────────────────────────────────────────────────────┘
           │
           │ Sub-agent completes
           │
           ▼
    PARENT AGENT (receives result string, integrates, continues)
```

---

## Agent Decisions (TIER 6)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  DECISION 1: Navigate or Stay?                                                   │
│                                                                                  │
│  ├── Stay (have enough context for task)                                         │
│  ├── Navigate deeper (nav:children → sub_features, components)                   │
│  ├── Navigate up (nav:parent → broader context)                                  │
│  └── Navigate sideways (nav:siblings → related entities)                         │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  DECISION 2: Do Myself or Spawn Sub-Agent?                                       │
│                                                                                  │
│  Do myself if:                                                                   │
│  • Task is within current context                                                │
│  • Don't need to preserve conversation state                                     │
│                                                                                  │
│  Spawn sub-agent if:                                                             │
│  • Task is parallelizable                                                        │
│  • Need fresh context window                                                     │
│  • Want to preserve current conversation                                         │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│  DECISION 3: What On-Demand Context to Load?                                     │
│                                                                                  │
│  • "Need naming convention" → read conventions.childNaming from index.jsonld     │
│  • "Need requirements" → follow rel:treeOfNeedsBranch                            │
│  • "Need stage workflow" → read .claude/skills/{stage}-workflow                  │
│  • "Need deeper detail" → follow nav:children links                              │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Summary Table

| Working Directory | CLAUDE.md Files | Key Context Gained |
|-------------------|-----------------|-------------------|
| `~/` | 2 | Basic user prefs |
| `~/dawson-workspace/` | 3 | + Sync awareness |
| `.../0_layer_universal/` | 5 | + Layer-stage framework |
| `.../layer_-1_better_ai_system/` | 7 | + Research project |
| `.../layer_0_feature_*/` | 8+ | + Feature conventions |

---

*Last updated: 2026-02-05*
