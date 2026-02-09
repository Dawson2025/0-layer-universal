# Tree of Needs - Better Layer Stage System

## Purpose

This document captures the hierarchical needs that drive this feature's requirements.

---

## Tree Structure

```
better_layer_stage_system
│
├── NEED: Consistent structure across all entities
│   │
│   ├── NEED: All stages always exist
│   │   ├── WHY: Agents know where to put content
│   │   ├── WHY: No guessing which stages exist
│   │   └── SOLUTION: Stage Completeness Rule (all 11 required)
│   │
│   ├── NEED: Clear naming conventions
│   │   ├── WHY: Agents can parse names programmatically
│   │   ├── WHY: Humans can understand at a glance
│   │   └── SOLUTION: subxN naming for depth
│   │
│   └── NEED: Sub-layers as entry points
│       ├── WHY: Agents can start work at any level
│       └── SOLUTION: CLAUDE.md at every entry point
│
├── NEED: Knowledge doesn't get lost (no amnesia)
│   │
│   ├── NEED: Single source of truth
│   │   ├── WHY: Changes in one place propagate everywhere
│   │   └── SOLUTION: Knowledge in sub_layers, skills reference it
│   │
│   ├── NEED: Skills bridge agents to knowledge
│   │   ├── WHY: CLAUDE.md stays minimal
│   │   ├── WHY: Skills load only when needed
│   │   └── SOLUTION: skills/ with references/ folders
│   │
│   └── NEED: Propagation chain is visible
│       ├── WHY: Can trace how context flows
│       └── SOLUTION: Required diagrams for context changes
│
├── NEED: Research is properly tracked
│   │
│   ├── NEED: User decisions are documented
│   │   ├── WHY: Future agents understand "why"
│   │   └── SOLUTION: Document in appropriate stages
│   │
│   └── NEED: Clear handoff to production
│       ├── WHY: Research becomes usable
│       └── SOLUTION: stage_10_current_product → production
│
└── NEED: Clean organization
    │
    ├── NEED: Merge folders consolidated
    │   ├── WHY: Cleaner root directory
    │   └── SOLUTION: .1merge/ parent folder
    │
    └── NEED: Tree of needs in every request gathering
        ├── WHY: Clear hierarchy of requirements
        └── SOLUTION: This document pattern
```

---

## Needs → Solutions Mapping

| Need | Solution | Implemented |
|------|----------|-------------|
| All stages always exist | Stage Completeness Rule | ✅ STAGES_EXPLAINED.md |
| Clear naming conventions | subxN naming | ✅ NESTED_DEPTH_NAMING.md |
| Sub-layers as entry points | CLAUDE.md at entry points | ✅ SUB_LAYERS_AS_ENTRY_POINTS.md |
| Single source of truth | Knowledge in sub_layers | ✅ AI_CONTEXT_FLOW_ARCHITECTURE.md |
| Skills bridge to knowledge | skills/ with references/ | ✅ .claude/skills/ |
| Propagation chain visible | Required diagrams | ✅ AI_CONTEXT_FLOW_ARCHITECTURE.md |
| User decisions documented | Document in stages | ✅ This session |
| Clear handoff to production | stage_10 → production | ⏳ Defined |
| Merge folders consolidated | .1merge/ folder | ✅ Done |
| Tree of needs | This document | ✅ This document |

---

## How to Read This Tree

1. **Top-level needs** are the main goals
2. **Child needs** break down the parent
3. **WHY** explains the motivation
4. **SOLUTION** describes how it's addressed

---

*Every request_gathering stage should have a tree_of_needs.md*
