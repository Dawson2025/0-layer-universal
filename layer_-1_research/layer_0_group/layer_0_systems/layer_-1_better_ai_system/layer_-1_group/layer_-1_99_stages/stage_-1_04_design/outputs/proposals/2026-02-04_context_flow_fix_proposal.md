# Context Flow Fix Proposal

**Date**: 2026-02-04
**Layer**: -1 (Research)
**Stage**: 05 (Design)
**Status**: Implemented

---

## Problem Statement

When creating new layer-stage entities (features, sub_features, components, subprojects), agents don't consistently follow naming conventions. This occurred when creating sub-features:

**What happened:**
- Created `subfeature_automation_system` instead of `layer_1_sub_feature_automation_system`
- Missing layer number prefix
- Missing underscore in `sub_feature`

**Root cause:**
1. Naming convention wasn't in the context loaded when creating entities
2. No trigger mechanism reminded the agent to check conventions before creation
3. `conventions.childNaming` wasn't present in parent index.jsonld files

---

## Context Flow Diagram (Target State)

### Overview: How Context Flows to Agents

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AGENT SESSION START                                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. ENTRY POINT LOADING                                                       │
│    ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐      │
│    │   ~/.claude/    │     │   CLAUDE.md     │     │  index.jsonld   │      │
│    │   CLAUDE.md     │────▶│   (hierarchy)   │────▶│  (navigation)   │      │
│    └─────────────────┘     └─────────────────┘     └─────────────────┘      │
│           │                        │                        │                │
│           │                        │                        │                │
│           ▼                        ▼                        ▼                │
│    ┌──────────────────────────────────────────────────────────────────┐     │
│    │              STATIC CONTEXT (always available)                    │     │
│    │  • Universal rules (layer_0/sub_layer_0_04_rules/)               │     │
│    │  • Naming conventions (conventions.childNaming)                   │     │
│    │  • Navigation links (nav:parent, nav:children, nav:siblings)      │     │
│    │  • Tree of needs mapping (rel:treeOfNeedsBranch)                  │     │
│    └──────────────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 2. TRIGGER-BASED LOADING (on specific actions)                               │
│                                                                              │
│    ┌─────────────────────────────────────────────────────────────────┐      │
│    │  trigger:onEntityCreation                                        │      │
│    │  ════════════════════════                                        │      │
│    │  When agent attempts to create: mkdir, Write new file            │      │
│    │                                                                  │      │
│    │  LOADS:                                                          │      │
│    │  ├── conventions.childNaming from parent index.jsonld            │      │
│    │  ├── entityTypes from schema                                     │      │
│    │  └── layer number context                                        │      │
│    │                                                                  │      │
│    │  VALIDATES:                                                      │      │
│    │  └── Name matches: layer_{N}_{type}_{name}                       │      │
│    └─────────────────────────────────────────────────────────────────┘      │
│                                                                              │
│    ┌─────────────────────────────────────────────────────────────────┐      │
│    │  trigger:onNavigation                                            │      │
│    │  ══════════════════════                                          │      │
│    │  When agent navigates to new directory                           │      │
│    │                                                                  │      │
│    │  LOADS:                                                          │      │
│    │  ├── index.jsonld in target directory                            │      │
│    │  ├── CLAUDE.md in target directory                               │      │
│    │  └── status.json if exists                                       │      │
│    └─────────────────────────────────────────────────────────────────┘      │
│                                                                              │
│    ┌─────────────────────────────────────────────────────────────────┐      │
│    │  trigger:onStageEnter                                            │      │
│    │  ═══════════════════════                                         │      │
│    │  When agent enters a stage directory                             │      │
│    │                                                                  │      │
│    │  LOADS:                                                          │      │
│    │  ├── Stage-specific rules                                        │      │
│    │  ├── Stage workflow skill                                        │      │
│    │  └── Stage handoff documents                                     │      │
│    └─────────────────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 3. ON-DEMAND LOADING (agent follows links)                                   │
│                                                                              │
│    index.jsonld                                                              │
│    ├── nav:parent → "../" (go up)                                            │
│    ├── nav:children → ["layer_1_sub_feature_*/"] (go down)                   │
│    ├── nav:siblings → ["../layer_1_sub_feature_*/"] (go sideways)            │
│    └── rel:treeOfNeedsBranch → links to needs documentation                  │
│                                                                              │
│    Agent can traverse hierarchy to find:                                     │
│    • More detailed context (drill down)                                      │
│    • Broader context (drill up)                                              │
│    • Related context (siblings)                                              │
│    • Requirements context (tree of needs)                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Entity Creation Flow (Detailed)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    AGENT WANTS TO CREATE NEW ENTITY                           │
│                    (e.g., new sub_feature in a feature)                       │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  STEP 1: Read parent's index.jsonld                                           │
│                                                                               │
│  layer_0_feature_context_framework/index.jsonld                               │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │  {                                                                      │  │
│  │    "@id": "layer_0_feature_context_framework",                          │  │
│  │    "layer": 0,           ◄─── Current layer number                      │  │
│  │                                                                         │  │
│  │    "conventions": {                                                     │  │
│  │      "childNaming": {                                                   │  │
│  │        "pattern": "layer_{N+1}_{type}_{name}",  ◄─── Pattern to follow  │  │
│  │        "currentLayer": 0,                                               │  │
│  │        "childLayer": 1,   ◄─── Children are layer 1                     │  │
│  │        "example": "layer_1_sub_feature_context_system" ◄─── Exact example│ │
│  │      }                                                                  │  │
│  │    }                                                                    │  │
│  │  }                                                                      │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  STEP 2: Apply naming pattern                                                 │
│                                                                               │
│  Pattern: layer_{N+1}_{type}_{name}                                           │
│  Current layer: 0                                                             │
│  Child layer: 0 + 1 = 1                                                       │
│  Type: sub_feature (underscore, like sub_layer)                               │
│  Name: navigation_system                                                      │
│                                                                               │
│  Result: layer_1_sub_feature_navigation_system ✓                              │
│                                                                               │
│  ❌ WRONG: subfeature_navigation_system (missing layer, missing underscore)   │
│  ❌ WRONG: layer_1_subfeature_navigation_system (missing underscore)          │
│  ✓  RIGHT: layer_1_sub_feature_navigation_system                              │
└──────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  STEP 3: Create with correct naming                                           │
│                                                                               │
│  mkdir layer_1_sub_feature_navigation_system                                  │
│                                                                               │
│  Then create child's index.jsonld with:                                       │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │  {                                                                      │  │
│  │    "@id": "layer_1_sub_feature_navigation_system",                      │  │
│  │    "layer": 1,                                                          │  │
│  │                                                                         │  │
│  │    "conventions": {                                                     │  │
│  │      "childNaming": {                                                   │  │
│  │        "pattern": "layer_{N+1}_{type}_{name}",                          │  │
│  │        "currentLayer": 1,                                               │  │
│  │        "childLayer": 2,                                                 │  │
│  │        "example": "layer_2_component_link_validator"                    │  │
│  │      }                                                                  │  │
│  │    }                                                                    │  │
│  │  }                                                                      │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  Convention propagates to next level!                                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Navigation Flow (Bidirectional)

```
                              ┌─────────────────────┐
                              │    layer_0_group    │
                              │    index.jsonld     │
                              └──────────┬──────────┘
                                         │ nav:children
                    ┌────────────────────┼────────────────────┐
                    ▼                    ▼                    ▼
        ┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐
        │  layer_0_features │ │ layer_0_components│ │layer_0_subprojects│
        │   index.jsonld    │ │   index.jsonld    │ │   index.jsonld    │
        └─────────┬─────────┘ └───────────────────┘ └───────────────────┘
                  │ features[]                nav:siblings ◄──────────────┘
    ┌─────────────┼─────────────┬─────────────────────────┐
    ▼             ▼             ▼                         ▼
┌─────────┐ ┌─────────┐   ┌─────────┐               ┌─────────┐
│context_ │ │structure│   │governan-│               │tooling_ │
│framework│ │framework│   │ce_frame │               │framework│
└────┬────┘ └─────────┘   └─────────┘               └─────────┘
     │ children[]
     │
     ├──────────────────────────────────────────────┐
     ▼                          ▼                   ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│layer_1_sub_      │  │layer_1_sub_      │  │layer_1_sub_      │
│feature_context_  │◄─│feature_dynamic_  │◄─│feature_navigation│
│system            │  │memory            │  │_system           │
└──────────────────┘  └──────────────────┘  └────────┬─────────┘
      nav:siblings ◄──────────────────────────────────┘
                                                      │ children[]
                                   ┌──────────────────┼──────────────────┐
                                   ▼                  ▼                  ▼
                          ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
                          │layer_2_comp- │   │layer_2_comp- │   │layer_2_comp- │
                          │onent_jsonld_ │   │onent_index_  │   │onent_link_   │
                          │schema        │   │files         │   │validator     │
                          └──────────────┘   └──────────────┘   └──────────────┘

Legend:
  ───▶  nav:children (parent → child)
  ◄───  nav:parent (child → parent, implicit via "../")
  ◄──►  nav:siblings (sibling ↔ sibling)
```

### Context Loading Chain

```
Session Start
     │
     ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ 1. ALWAYS LOADED (Static Context)                                           │
│    ~/.claude/CLAUDE.md → ~/CLAUDE.md → workspace/CLAUDE.md → ...            │
│    Result: Universal rules, session guidelines                              │
└────────────────────────────────────────────────────────────────────────────┘
     │
     ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ 2. PATH-BASED LOADING                                                       │
│    Each CLAUDE.md/index.jsonld in working directory path                    │
│    Result: Layer context, project context, stage context                    │
└────────────────────────────────────────────────────────────────────────────┘
     │
     ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ 3. TRIGGER LOADING (NEW)                                                    │
│    Action-specific context loading:                                         │
│    • Creating entity → conventions.childNaming                              │
│    • Entering stage → stage workflow skill                                  │
│    • Making decision → relevant principles                                  │
│    Result: Action-appropriate context at the moment it's needed             │
└────────────────────────────────────────────────────────────────────────────┘
     │
     ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ 4. ON-DEMAND LOADING                                                        │
│    Agent follows nav: links in index.jsonld                                 │
│    Result: Deeper context when needed, without loading everything upfront   │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Solution Overview

Three-part fix to ensure agents always know naming conventions when creating entities:

### 1. Convention Propagation in index.jsonld

Every `index.jsonld` file now includes a `conventions` block:

```json
{
  "@id": "layer_0_feature_context_framework",
  "layer": 0,

  "conventions": {
    "childNaming": {
      "pattern": "layer_{N+1}_{type}_{name}",
      "currentLayer": 0,
      "childLayer": 1,
      "example": "layer_1_sub_feature_context_system"
    }
  }
}
```

**Why this works:**
- When an agent reads a parent's index.jsonld before creating children, they see the naming pattern
- The `example` field shows exactly what a child should be named
- `currentLayer` and `childLayer` make the math explicit

### 2. Entity Type Naming Reference

Add to schema or root index.jsonld:

```json
{
  "entityTypes": {
    "Feature": {
      "pattern": "layer_{N}_feature_{name}",
      "example": "layer_0_feature_context_framework"
    },
    "SubFeature": {
      "pattern": "layer_{N}_sub_feature_{name}",
      "example": "layer_1_sub_feature_context_system"
    },
    "Component": {
      "pattern": "layer_{N}_component_{name}",
      "example": "layer_2_component_link_validator"
    },
    "Subproject": {
      "pattern": "layer_{N}_subproject_{name}",
      "example": "layer_1_subproject_prototype"
    }
  }
}
```

### 3. Trigger for Entity Creation (Future)

Add trigger mechanism to JSON-LD schema:

```json
{
  "trigger:onEntityCreation": {
    "loads": [
      "conventions.childNaming",
      "entityTypes"
    ],
    "validates": {
      "namePattern": "^layer_\\d+_(feature|sub_feature|component|subproject)_.+$"
    }
  }
}
```

**Implementation path:**
1. Define trigger in schema vocabulary
2. Add trigger detection to context loading system
3. Enforce validation before directory/file creation

---

## Changes Made

### Already Implemented

| File | Change |
|------|--------|
| `layer_0_feature_context_framework/index.jsonld` | Added `layer: 0`, `conventions.childNaming` |
| `layer_0_feature_structure_framework/index.jsonld` | Added `layer: 0`, `conventions.childNaming` |
| `layer_0_feature_governance_framework/index.jsonld` | Added `layer: 0`, `conventions.childNaming` |
| `layer_0_feature_tooling_framework/index.jsonld` | Added `layer: 0`, `conventions.childNaming` |
| `layer_1_sub_feature_navigation_system/index.jsonld` | Added `layer: 1`, `conventions.childNaming` |
| All 9 sub_feature directories | Renamed from `subfeature_*` to `layer_1_sub_feature_*` |

### To Be Implemented

| Item | Priority | Effort | Status |
|------|----------|--------|--------|
| Add entityTypes to root schema | High | Low | ✅ Done |
| Update all remaining index.jsonld with layer + conventions | High | Medium | ✅ Done |
| Create entity-creation skill with validation | Medium | Medium | ✅ Done |
| Add trigger:onEntityCreation to schema | Medium | High | ✅ Done |

**All items implemented on 2026-02-04.**

---

## Naming Convention Reference

### Pattern
```
layer_{N}_{type}_{name}
```

### Types (with underscore rules)
| Type | Pattern | Note |
|------|---------|------|
| feature | `layer_N_feature_name` | Single word type |
| sub_feature | `layer_N_sub_feature_name` | Underscore like `sub_layer` |
| component | `layer_N_component_name` | Single word type |
| subproject | `layer_N_subproject_name` | Single word type |

### Layer Hierarchy
```
layer_0_feature_*
  └── layer_1_sub_feature_*
        └── layer_2_component_*
              └── layer_3_*
```

---

## Tree of Needs Alignment

This fix addresses needs from `06_context_flow`:

| Need | How Addressed |
|------|---------------|
| `need_02_context_propagation_works` | Conventions propagate through index.jsonld hierarchy |
| `need_05_entry_points_right_detail` | Entry points now include naming conventions |
| `need_06_navigation_to_deeper_details` | Agents can find detailed rules via triggers |

---

## Validation Checklist

Before creating any new layer-stage entity:

- [ ] Read parent's index.jsonld
- [ ] Check `conventions.childNaming.pattern`
- [ ] Check `conventions.childNaming.example`
- [ ] Verify name matches pattern: `layer_{N+1}_{type}_{name}`
- [ ] Use underscore for compound types: `sub_feature`, not `subfeature`

---

## Summary

The naming convention mistake happened because:
1. Context didn't include conventions when I created entities
2. No trigger mechanism loaded naming rules

The fix:
1. **Immediate**: Added `conventions.childNaming` to all index.jsonld files
2. **Short-term**: Document entityTypes in schema
3. **Long-term**: Implement trigger:onEntityCreation for validation

This ensures future agents always have naming conventions in context when creating layer-stage entities.
