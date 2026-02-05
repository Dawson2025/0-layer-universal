# Context Visualization System Proposal

**Date**: 2026-02-05
**Layer**: -1 (Research)
**Stage**: 05 (Design)
**Status**: Proposed

---

## Problem Statement

Currently, understanding how context flows through the layer-stage system requires reading multiple files and mentally reconstructing the flow. This makes it difficult to:

1. **Debug context issues** - Why didn't an agent get the right context?
2. **Plan improvements** - What would change if we modify the flow?
3. **Onboard new agents/users** - How does the system actually work?
4. **Validate proposals** - Will this change have the intended effect?

We need a **visualization system** that provides:
- Diagrams of current context flow
- Diagrams of context architecture
- Diagrams of context propagation
- Before/after comparison for proposals

---

## Current State Diagrams

### 1. Context Architecture (Current)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           CONTEXT ARCHITECTURE                                   │
│                              (Current State)                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CONTEXT TYPES                                       │
├─────────────────────────────────┬───────────────────────────────────────────────┤
│         STATIC CONTEXT          │            DYNAMIC CONTEXT                     │
│    (Doesn't change often)       │         (Changes per session)                  │
├─────────────────────────────────┼───────────────────────────────────────────────┤
│                                 │                                                │
│  ┌───────────────────────────┐  │  ┌───────────────────────────────────────┐    │
│  │       CLAUDE.md           │  │  │          status.json                  │    │
│  │  • Identity & role        │  │  │  • Current state                      │    │
│  │  • Navigation hints       │  │  │  • Active tasks                       │    │
│  │  • Key behaviors          │  │  │  • Last modified                      │    │
│  └───────────────────────────┘  │  └───────────────────────────────────────┘    │
│                                 │                                                │
│  ┌───────────────────────────┐  │  ┌───────────────────────────────────────┐    │
│  │      index.jsonld         │  │  │      hand_off_documents/              │    │
│  │  • Navigation graph       │  │  │  • incoming/from_above/               │    │
│  │  • Conventions            │  │  │  • incoming/from_below/               │    │
│  │  • Triggers               │  │  │  • outgoing/to_above/                 │    │
│  │  • Tree of needs links    │  │  │  • outgoing/to_below/                 │    │
│  └───────────────────────────┘  │  └───────────────────────────────────────┘    │
│                                 │                                                │
│  ┌───────────────────────────┐  │  ┌───────────────────────────────────────┐    │
│  │    sub_layer_0_04_rules/  │  │  │       session memory                  │    │
│  │  • Universal rules        │  │  │  • episodic/                          │    │
│  │  • Safety governance      │  │  │  • conversation history               │    │
│  │  • Protocols              │  │  │  • task progress                      │    │
│  └───────────────────────────┘  │  └───────────────────────────────────────┘    │
│                                 │                                                │
│  ┌───────────────────────────┐  │                                                │
│  │    .claude/skills/        │  │                                                │
│  │  • Workflow skills        │  │                                                │
│  │  • Entity creation        │  │                                                │
│  │  • Stage-specific         │  │                                                │
│  └───────────────────────────┘  │                                                │
│                                 │                                                │
└─────────────────────────────────┴───────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────────┐
│                            CONTEXT SOURCES                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│   │   Global    │    │  Workspace  │    │   Project   │    │   Layer     │      │
│   │  ~/.claude/ │───▶│  CLAUDE.md  │───▶│  CLAUDE.md  │───▶│  CLAUDE.md  │      │
│   │  CLAUDE.md  │    │             │    │             │    │             │      │
│   └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘      │
│         │                  │                  │                  │               │
│         ▼                  ▼                  ▼                  ▼               │
│   ┌─────────────────────────────────────────────────────────────────────┐       │
│   │                    MERGED CONTEXT                                    │       │
│   │   (Each level inherits from parent, can override/extend)             │       │
│   └─────────────────────────────────────────────────────────────────────┘       │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Context Flow (Current)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CONTEXT FLOW                                        │
│                            (Current State)                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

                              SESSION START
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: AUTOMATIC LOADING (Claude Code does this)                               │
│                                                                                  │
│   ~/.claude/CLAUDE.md ──▶ ~/CLAUDE.md ──▶ workspace/CLAUDE.md ──▶ ...           │
│                                                                                  │
│   Result: Basic rules, identity, workspace context                               │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: PATH-BASED LOADING (Agent traverses)                                    │
│                                                                                  │
│   Agent working in: layer_-1_better_ai_system/layer_0_group/layer_0_features/    │
│                                                                                  │
│   Loads (or should load):                                                        │
│   ├── layer_-1_research/CLAUDE.md                                               │
│   ├── layer_-1_better_ai_system/CLAUDE.md                                       │
│   ├── layer_0_group/index.jsonld                                                │
│   └── layer_0_features/index.jsonld                                             │
│                                                                                  │
│   ⚠️  PROBLEM: No enforcement that agent actually reads these!                   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: TRIGGER-BASED LOADING (Defined but not enforced)                        │
│                                                                                  │
│   trigger:onEntityCreation ──▶ Should load conventions.childNaming               │
│   trigger:onStageEnter ──▶ Should load stage workflow skill                      │
│   trigger:onSessionStart ──▶ Should load CLAUDE.md + index.jsonld                │
│                                                                                  │
│   ⚠️  PROBLEM: Triggers defined in JSON-LD but nothing enforces them!            │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: ON-DEMAND LOADING (Agent discretion)                                    │
│                                                                                  │
│   Agent follows nav: links when it decides to:                                   │
│   ├── nav:parent ──▶ Go up hierarchy                                            │
│   ├── nav:children ──▶ Go down hierarchy                                        │
│   ├── nav:siblings ──▶ Related entities                                         │
│   └── rel:treeOfNeedsBranch ──▶ Requirements                                    │
│                                                                                  │
│   ⚠️  PROBLEM: Agent may not know to follow links, or may not find them!         │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 3. Context Propagation (Current)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          CONTEXT PROPAGATION                                     │
│                            (Current State)                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────┐
                    │     0_layer_universal/          │
                    │        CLAUDE.md                │
                    │  • Universal rules              │
                    │  • Navigation structure         │
                    └───────────────┬─────────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
    ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
    │    layer_0/     │   │    layer_1/     │   │ layer_-1_research│
    │   (Universal)   │   │   (Projects)    │   │    (Research)    │
    │                 │   │                 │   │                  │
    │  Inherits:      │   │  Inherits:      │   │  Inherits:       │
    │  • All rules    │   │  • All rules    │   │  • All rules     │
    │                 │   │                 │   │                  │
    │  Adds:          │   │  Adds:          │   │  Adds:           │
    │  • sub_layers   │   │  • projects     │   │  • research      │
    │  • principles   │   │  • features     │   │    projects      │
    └────────┬────────┘   └────────┬────────┘   └────────┬─────────┘
             │                     │                     │
             ▼                     ▼                     ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                     INHERITANCE CHAIN                        │
    │                                                              │
    │   Parent context is always available to children             │
    │   Children can override/extend but not remove                │
    │                                                              │
    │   ⚠️  PROBLEM: No visibility into what was inherited!        │
    │   ⚠️  PROBLEM: No validation that inheritance is correct!    │
    └─────────────────────────────────────────────────────────────┘


                         PROPAGATION GAPS (Current)
    ┌─────────────────────────────────────────────────────────────┐
    │                                                              │
    │   1. conventions.childNaming                                 │
    │      ├── Defined in: parent index.jsonld                    │
    │      ├── Should propagate to: child creation                │
    │      └── Actually propagates: ❌ Only if agent reads it     │
    │                                                              │
    │   2. layer number                                            │
    │      ├── Defined in: parent index.jsonld                    │
    │      ├── Should propagate to: child (as N+1)                │
    │      └── Actually propagates: ❌ Only if agent calculates   │
    │                                                              │
    │   3. tree of needs mapping                                   │
    │      ├── Defined in: parent rel:treeOfNeedsBranch           │
    │      ├── Should propagate to: guide child organization      │
    │      └── Actually propagates: ❌ Only if agent follows link │
    │                                                              │
    └─────────────────────────────────────────────────────────────┘
```

---

## Proposed Solution: Context Visualization System

### Location

```
layer_0_group/layer_0_features/layer_0_feature_context_framework/
  └── layer_1_sub_feature_context_visualization/
        ├── index.jsonld
        ├── CLAUDE.md
        ├── diagrams/
        │   ├── current/
        │   │   ├── context_architecture.md
        │   │   ├── context_flow.md
        │   │   └── context_propagation.md
        │   └── proposed/
        │       └── {proposal_name}/
        │           ├── before.md
        │           └── after.md
        └── tools/
            └── generate_diagrams.md (skill for generating diagrams)
```

### Diagram Types

#### Type 1: Context Architecture Diagram
Shows **what** context exists and **where** it lives.

```
PURPOSE: Answer "What context is available?"

SHOWS:
├── Static context locations (CLAUDE.md, index.jsonld, rules/)
├── Dynamic context locations (status.json, handoffs/)
├── Context types (identity, navigation, rules, state)
└── Context ownership (global, project, layer, stage)

FORMAT: Box diagram with categorization
```

#### Type 2: Context Flow Diagram
Shows **when** context loads and **in what order**.

```
PURPOSE: Answer "When does context load?"

SHOWS:
├── Session start sequence
├── Navigation triggers
├── Action triggers (entity creation, stage entry)
└── On-demand loading points

FORMAT: Sequential flow diagram with phases
```

#### Type 3: Context Propagation Diagram
Shows **how** context moves through hierarchy.

```
PURPOSE: Answer "How does context propagate?"

SHOWS:
├── Inheritance chains (parent → child)
├── Override points (where children can modify)
├── Propagation gaps (where context doesn't flow)
└── Required vs optional propagation

FORMAT: Tree diagram with inheritance arrows
```

#### Type 4: Before/After Comparison Diagram
Shows **impact** of proposed changes.

```
PURPOSE: Answer "What will change?"

SHOWS:
├── Current state (before)
├── Proposed state (after)
├── Diff highlighting (what's new, what's removed, what moves)
└── Impact analysis (what entities affected)

FORMAT: Side-by-side comparison
```

---

## Proposed Context Flow (Target State)

### Context Flow Diagram (Proposed)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CONTEXT FLOW                                        │
│                           (Proposed State)                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

                              SESSION START
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: AUTOMATIC LOADING (Claude Code - unchanged)                             │
│                                                                                  │
│   ~/.claude/CLAUDE.md ──▶ ~/CLAUDE.md ──▶ workspace/CLAUDE.md ──▶ ...           │
│                                                                                  │
│   ✓ WORKS: Claude Code handles this automatically                                │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: ENTRY POINT LOADING (NEW - Enforced)                                    │
│                                                                                  │
│   When entering any directory with index.jsonld:                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  1. Read index.jsonld (REQUIRED)                                         │   │
│   │  2. Extract: layer, conventions, triggers, nav links                     │   │
│   │  3. Store in session context for later use                               │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│   Enforcement: Claude Code hook or agent instruction in CLAUDE.md               │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: TRIGGER-BASED LOADING (NEW - Active enforcement)                        │
│                                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  trigger:onEntityCreation                                                │   │
│   │  ════════════════════════                                                │   │
│   │  WHEN: mkdir, Write to new file                                          │   │
│   │  LOADS: conventions.childNaming, entityTypes from schema                 │   │
│   │  VALIDATES: Name matches layer_{N}_{type}_{name}                         │   │
│   │  BLOCKS: Creation if validation fails                                    │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  trigger:onStageEnter                                                    │   │
│   │  ═════════════════════                                                   │   │
│   │  WHEN: cd into stage_*_* directory                                       │   │
│   │  LOADS: Stage workflow skill, stage CLAUDE.md                            │   │
│   │  ACTIVATES: Stage-specific behaviors                                     │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  trigger:onHierarchyTraversal                                            │   │
│   │  ═══════════════════════════                                             │   │
│   │  WHEN: Following nav:parent, nav:children, nav:siblings                  │   │
│   │  LOADS: Target's index.jsonld + CLAUDE.md                                │   │
│   │  UPDATES: Session context with new location info                         │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│   Enforcement: Hook system or skill that intercepts actions                     │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: VALIDATED ON-DEMAND LOADING (NEW - Guided)                              │
│                                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  Context Discovery Helper                                                │   │
│   │  ═════════════════════════                                               │   │
│   │  Agent can ask: "What context is available for [task]?"                  │   │
│   │  System responds with relevant links from index.jsonld                   │   │
│   │                                                                          │   │
│   │  Example:                                                                │   │
│   │  Q: "What context for creating a sub_feature?"                           │   │
│   │  A: "Load: conventions.childNaming, entityTypes, entity-creation skill"  │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
│   Enforcement: Skill that maps tasks to required context                        │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Context Propagation Diagram (Proposed)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          CONTEXT PROPAGATION                                     │
│                           (Proposed State)                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────┐
                    │      ROOT index.jsonld          │
                    │  ┌───────────────────────────┐  │
                    │  │ conventions: {            │  │
                    │  │   childNaming: {...}      │◀─┼── DEFINED HERE
                    │  │ }                         │  │
                    │  │ entityTypes: {...}        │◀─┼── DEFINED HERE
                    │  └───────────────────────────┘  │
                    └───────────────┬─────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
         ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
         │  Feature A   │ │  Feature B   │ │  Feature C   │
         │ ┌──────────┐ │ │ ┌──────────┐ │ │ ┌──────────┐ │
         │ │conventions│ │ │ │conventions│ │ │ │conventions│ │
         │ │ INHERITED │ │ │ │ INHERITED │ │ │ │ INHERITED │ │
         │ │    +      │ │ │ │    +      │ │ │ │    +      │ │
         │ │ EXTENDED  │ │ │ │ EXTENDED  │ │ │ │ EXTENDED  │ │
         │ └──────────┘ │ │ └──────────┘ │ │ └──────────┘ │
         └──────┬───────┘ └──────────────┘ └──────────────┘
                │
                ▼
      ┌───────────────────┐
      │   Sub-Feature     │
      │ ┌───────────────┐ │
      │ │ conventions   │ │
      │ │ INHERITED     │ │
      │ │ from Feature  │ │
      │ │               │ │
      │ │ + childLayer  │ │
      │ │   = N+1       │◀─── CALCULATED automatically
      │ └───────────────┘ │
      └───────────────────┘


              PROPAGATION RULES (Proposed)
    ┌─────────────────────────────────────────────────────────────┐
    │                                                              │
    │   1. conventions.childNaming                                 │
    │      ├── Source: parent index.jsonld                        │
    │      ├── Propagation: AUTOMATIC via trigger                 │
    │      ├── Validation: REQUIRED before entity creation        │
    │      └── Status: ✅ ENFORCED                                 │
    │                                                              │
    │   2. layer number                                            │
    │      ├── Source: parent.layer + 1                           │
    │      ├── Propagation: CALCULATED automatically              │
    │      ├── Validation: Must equal parent + 1                  │
    │      └── Status: ✅ ENFORCED                                 │
    │                                                              │
    │   3. tree of needs mapping                                   │
    │      ├── Source: parent rel:treeOfNeedsBranch               │
    │      ├── Propagation: SUGGESTED (shown in context helper)   │
    │      ├── Validation: OPTIONAL but recommended               │
    │      └── Status: ✅ GUIDED                                   │
    │                                                              │
    │   4. triggers                                                │
    │      ├── Source: parent trigger:* definitions               │
    │      ├── Propagation: INHERITED unless overridden           │
    │      ├── Validation: Schema validates trigger structure     │
    │      └── Status: ✅ INHERITED                                │
    │                                                              │
    └─────────────────────────────────────────────────────────────┘
```

---

## Before/After Comparison: Entity Creation

### Before (What went wrong)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ENTITY CREATION FLOW (BEFORE)                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

    Agent receives task: "Create sub-features for tooling framework"
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │ Agent creates directories:    │
                    │                               │
                    │ mkdir subfeature_automation   │ ❌ Wrong name
                    │ mkdir subfeature_docs         │ ❌ Wrong name
                    │                               │
                    │ (No validation, no warning)   │
                    └───────────────────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │ Result: Incorrectly named     │
                    │ entities that don't follow    │
                    │ layer-stage conventions       │
                    │                               │
                    │ Must be fixed manually later  │
                    └───────────────────────────────┘

    WHY IT FAILED:
    ┌─────────────────────────────────────────────────────────────────────────┐
    │ • No trigger fired to load conventions                                   │
    │ • conventions.childNaming wasn't in agent's context                     │
    │ • No validation prevented the incorrect creation                         │
    │ • Agent didn't know to read parent's index.jsonld                       │
    └─────────────────────────────────────────────────────────────────────────┘
```

### After (How it should work)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ENTITY CREATION FLOW (AFTER)                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

    Agent receives task: "Create sub-features for tooling framework"
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │ PHASE 1: Context Loading      │
                    │ (Automatic via trigger)       │
                    │                               │
                    │ 1. Read parent index.jsonld   │
                    │ 2. Extract conventions        │
                    │ 3. Load entity-creation skill │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │ PHASE 2: Name Validation      │
                    │                               │
                    │ Pattern: layer_{N+1}_{type}_* │
                    │ Parent layer: 0               │
                    │ Child layer: 1                │
                    │ Type: sub_feature             │
                    │                               │
                    │ ✓ layer_1_sub_feature_auto... │
                    │ ✓ layer_1_sub_feature_docs    │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │ PHASE 3: Creation             │
                    │                               │
                    │ mkdir layer_1_sub_feature_*   │ ✅ Correct
                    │                               │
                    │ Create index.jsonld with:     │
                    │ • @id: correct name           │
                    │ • layer: 1                    │
                    │ • conventions for children    │
                    └───────────────────────────────┘

    WHY IT WORKS:
    ┌─────────────────────────────────────────────────────────────────────────┐
    │ • trigger:onEntityCreation fires automatically                          │
    │ • conventions.childNaming loaded before creation                        │
    │ • Validation ensures correct naming                                      │
    │ • New entity inherits conventions for its own children                  │
    └─────────────────────────────────────────────────────────────────────────┘
```

---

## Implementation Plan

### Phase 1: Diagram Infrastructure
- [ ] Create `layer_1_sub_feature_context_visualization/` directory
- [ ] Create diagram templates (architecture, flow, propagation)
- [ ] Document current state diagrams

### Phase 2: Proposal Integration
- [ ] Add before/after diagram requirement to proposal template
- [ ] Create tool/skill for generating comparison diagrams
- [ ] Integrate diagrams into proposal review process

### Phase 3: Enforcement Mechanisms
- [ ] Implement trigger:onEntityCreation enforcement (hook or skill)
- [ ] Implement trigger:onStageEnter enforcement
- [ ] Create context discovery helper skill

### Phase 4: Validation
- [ ] Test entity creation with new flow
- [ ] Validate propagation works as designed
- [ ] Document any gaps found

---

## Files to Create

| File | Purpose |
|------|---------|
| `layer_1_sub_feature_context_visualization/index.jsonld` | Navigation and triggers |
| `layer_1_sub_feature_context_visualization/CLAUDE.md` | Identity and behaviors |
| `diagrams/current/context_architecture.md` | Current architecture diagram |
| `diagrams/current/context_flow.md` | Current flow diagram |
| `diagrams/current/context_propagation.md` | Current propagation diagram |
| `tools/generate_diagrams.md` | Skill for diagram generation |

---

## Summary

This proposal establishes a **Context Visualization System** that provides:

1. **Standardized diagram types** for understanding context
2. **Current state documentation** so we know where we are
3. **Before/after comparisons** for evaluating proposals
4. **Integration with proposal process** to require visualization

The goal is to make context flow **visible** and **predictable**, not hidden and implicit.
