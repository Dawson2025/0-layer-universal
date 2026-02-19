# Context Propagation Diagram

**Purpose**: Answer "How does context move through the hierarchy?"
**Last Updated**: 2026-02-05

---

## Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          CONTEXT PROPAGATION                                     │
│                            (Current State)                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

                              INHERITANCE MODEL
                              ═════════════════

    ┌─────────────────────────────────────────────────────────────────────────┐
    │                                                                          │
    │   Parent context flows DOWN to children                                  │
    │   Children INHERIT from parents (can extend, can override)               │
    │   Children CANNOT remove parent context                                  │
    │                                                                          │
    └─────────────────────────────────────────────────────────────────────────┘
```

---

## Hierarchy Propagation

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         HIERARCHY PROPAGATION                                    │
└─────────────────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────┐
                    │     0_layer_universal/          │
                    │                                 │
                    │  CLAUDE.md contains:            │
                    │  ├── Universal rules            │
                    │  ├── Navigation structure       │
                    │  ├── Modification protocol      │
                    │  └── Commit/push rules          │
                    │                                 │
                    │  PROPAGATES: Everything         │
                    └───────────────┬─────────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
    ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
    │    layer_0/     │   │    layer_1/     │   │ layer_-1_       │
    │   (Universal)   │   │   (Projects)    │   │ research/       │
    │                 │   │                 │   │                 │
    │ INHERITS:       │   │ INHERITS:       │   │ INHERITS:       │
    │ • All rules ✅  │   │ • All rules ✅  │   │ • All rules ✅  │
    │ • Protocols ✅  │   │ • Protocols ✅  │   │ • Protocols ✅  │
    │                 │   │                 │   │                 │
    │ ADDS:           │   │ ADDS:           │   │ ADDS:           │
    │ • sub_layers    │   │ • projects      │   │ • research      │
    │ • principles    │   │ • features      │   │   projects      │
    │ • knowledge     │   │ • components    │   │ • experiments   │
    └─────────────────┘   └─────────────────┘   └────────┬────────┘
                                                         │
                                                         ▼
                                              ┌─────────────────────┐
                                              │ layer_-1_better_    │
                                              │ ai_system/          │
                                              │                     │
                                              │ INHERITS:           │
                                              │ • All rules ✅      │
                                              │ • Research context  │
                                              │                     │
                                              │ ADDS:               │
                                              │ • Project identity  │
                                              │ • Feature list      │
                                              │ • Tree of needs     │
                                              └──────────┬──────────┘
                                                         │
                                                         ▼
                                              ┌─────────────────────┐
                                              │   layer_0_group/    │
                                              │                     │
                                              │ INHERITS:           │
                                              │ • All above ✅      │
                                              │                     │
                                              │ ADDS:               │
                                              │ • conventions       │
                                              │ • triggers          │
                                              │ • nav links         │
                                              └──────────┬──────────┘
                                                         │
                              ┌───────────────────────────┼───────────────────────────┐
                              │                           │                           │
                              ▼                           ▼                           ▼
                    ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
                    │ layer_0_features│         │layer_0_components         │layer_0_subprojects
                    │                 │         │                 │         │                 │
                    │ INHERITS:       │         │ INHERITS:       │         │ INHERITS:       │
                    │ • conventions ✅│         │ • conventions ✅│         │ • conventions ✅│
                    │ • triggers ✅   │         │ • triggers ✅   │         │ • triggers ✅   │
                    └────────┬────────┘         └─────────────────┘         └─────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ layer_0_feature_│
                    │ context_framework
                    │                 │
                    │ INHERITS:       │
                    │ • conventions ✅│
                    │                 │
                    │ DEFINES for     │
                    │ children:       │
                    │ • childNaming   │
                    │ • layer: 0      │
                    │ • childLayer: 1 │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │layer_2_sub_  │ │layer_2_sub_  │ │layer_2_sub_  │
    │feature_      │ │feature_      │ │feature_      │
    │context_system│ │dynamic_memory│ │navigation_   │
    │              │ │              │ │system        │
    │              │ │              │ │              │
    │ INHERITS:    │ │ INHERITS:    │ │ INHERITS:    │
    │ • conventions│ │ • conventions│ │ • conventions│
    │   (should) ⚠️│ │   (should) ⚠️│ │   ✅         │
    │              │ │              │ │              │
    │ DEFINES for  │ │ DEFINES for  │ │ DEFINES for  │
    │ children:    │ │ children:    │ │ children:    │
    │ • childLayer │ │ • childLayer │ │ • childLayer │
    │   = 2        │ │   = 2        │ │   = 2 ✅     │
    └──────────────┘ └──────────────┘ └──────────────┘
```

---

## What Should Propagate

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         WHAT SHOULD PROPAGATE                                    │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                  │
│  ALWAYS PROPAGATE (Inherited by all children)                                    │
│  ═══════════════════════════════════════════                                     │
│                                                                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐                  │
│  │  Universal      │  │  Safety         │  │  Modification   │                  │
│  │  Rules          │  │  Governance     │  │  Protocol       │                  │
│  │                 │  │                 │  │                 │                  │
│  │  Source:        │  │  Source:        │  │  Source:        │                  │
│  │  layer_0/rules/ │  │  layer_0/rules/ │  │  CLAUDE.md      │                  │
│  │                 │  │                 │  │                 │                  │
│  │  Status: ✅     │  │  Status: ✅     │  │  Status: ✅     │                  │
│  │  (always in     │  │  (always in     │  │  (always in     │                  │
│  │   context)      │  │   context)      │  │   context)      │                  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘                  │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                  │
│  PROPAGATE TO CHILDREN (From parent to immediate children)                       │
│  ═════════════════════════════════════════════════════════                       │
│                                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────────────┐│
│  │  conventions.childNaming                                                     ││
│  │  ───────────────────────                                                     ││
│  │                                                                              ││
│  │  From: parent/index.jsonld                                                   ││
│  │  To:   child entity creation                                                 ││
│  │                                                                              ││
│  │  Contains:                                                                   ││
│  │  • pattern: "layer_{N+1}_{type}_{name}"                                      ││
│  │  • currentLayer: N                                                           ││
│  │  • childLayer: N+1                                                           ││
│  │  • example: "layer_2_subx2_feature_example"                                    ││
│  │                                                                              ││
│  │  Status: ⚠️ SHOULD propagate but not enforced                                ││
│  └─────────────────────────────────────────────────────────────────────────────┘│
│                                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────────────┐│
│  │  layer number                                                                ││
│  │  ────────────                                                                ││
│  │                                                                              ││
│  │  From: parent.layer                                                          ││
│  │  To:   child.layer = parent.layer + 1                                        ││
│  │                                                                              ││
│  │  Rule: Children are always parent layer + 1                                  ││
│  │                                                                              ││
│  │  Status: ⚠️ SHOULD propagate but not enforced                                ││
│  └─────────────────────────────────────────────────────────────────────────────┘│
│                                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────────────┐│
│  │  triggers                                                                    ││
│  │  ────────                                                                    ││
│  │                                                                              ││
│  │  From: parent/index.jsonld trigger:*                                         ││
│  │  To:   inherited unless overridden                                           ││
│  │                                                                              ││
│  │  Status: ⚠️ DEFINED but not enforced                                         ││
│  └─────────────────────────────────────────────────────────────────────────────┘│
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                  │
│  OPTIONAL PROPAGATION (Suggested but not required)                               │
│  ═════════════════════════════════════════════════                               │
│                                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────────────┐│
│  │  rel:treeOfNeedsBranch                                                       ││
│  │  ─────────────────────                                                       ││
│  │                                                                              ││
│  │  From: parent feature                                                        ││
│  │  To:   guide child organization                                              ││
│  │                                                                              ││
│  │  Status: ⚠️ OPTIONAL - helps with organization                               ││
│  └─────────────────────────────────────────────────────────────────────────────┘│
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Propagation Gaps

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          PROPAGATION GAPS                                        │
│                         (Current Problems)                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                  │
│  GAP 1: conventions.childNaming not enforced                                     │
│  ═══════════════════════════════════════════                                     │
│                                                                                  │
│  DEFINED IN:                                                                     │
│  layer_0_feature_*/index.jsonld                                                 │
│  ┌─────────────────────────────────┐                                            │
│  │ "conventions": {                │                                            │
│  │   "childNaming": {              │                                            │
│  │     "pattern": "layer_{N+1}_*", │                                            │
│  │     "example": "layer_2_sub_*"  │                                            │
│  │   }                             │                                            │
│  │ }                               │                                            │
│  └─────────────────────────────────┘                                            │
│                 │                                                                │
│                 ▼                                                                │
│  SHOULD FLOW TO:                                                                 │
│  Agent creating child entity                                                    │
│                 │                                                                │
│                 ▼                                                                │
│  ACTUALLY FLOWS TO:                                                              │
│  ❌ NOTHING - Agent doesn't read it unless explicitly told                       │
│                                                                                  │
│  RESULT:                                                                         │
│  Agent creates "subfeature_*" instead of "layer_2_subx2_feature_*"                │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                  │
│  GAP 2: layer number not calculated automatically                                │
│  ════════════════════════════════════════════════                                │
│                                                                                  │
│  PARENT HAS:                                                                     │
│  ┌─────────────────────────────────┐                                            │
│  │ "@id": "layer_0_feature_*",     │                                            │
│  │ "layer": 0                      │                                            │
│  └─────────────────────────────────┘                                            │
│                 │                                                                │
│                 ▼                                                                │
│  CHILD SHOULD HAVE:                                                              │
│  ┌─────────────────────────────────┐                                            │
│  │ "@id": "layer_2_subx2_feature_*", │                                            │
│  │ "layer": 1  (0 + 1)             │                                            │
│  └─────────────────────────────────┘                                            │
│                 │                                                                │
│                 ▼                                                                │
│  ACTUALLY:                                                                       │
│  ❌ Agent must manually calculate and set                                        │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                  │
│  GAP 3: No visibility into what was inherited                                    │
│  ════════════════════════════════════════════                                    │
│                                                                                  │
│  QUESTION: "What context does this entity have access to?"                       │
│                                                                                  │
│  ANSWER: ❌ Unknown without manually tracing ancestry                            │
│                                                                                  │
│  NEED: Tool to show inherited context at any point                               │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Propagation Rules Summary

| Context | Source | Target | Should Propagate | Actually Propagates |
|---------|--------|--------|------------------|---------------------|
| Universal rules | layer_0/rules/ | All entities | ✅ Always | ✅ Yes (in CLAUDE.md chain) |
| Modification protocol | CLAUDE.md | All entities | ✅ Always | ✅ Yes (in CLAUDE.md chain) |
| conventions.childNaming | parent index.jsonld | Child creation | ✅ Required | ⚠️ Only if agent reads it |
| layer number | parent.layer + 1 | Child entity | ✅ Required | ⚠️ Only if agent calculates |
| triggers | parent index.jsonld | Children | ✅ Inherited | ⚠️ Not enforced |
| rel:treeOfNeedsBranch | parent feature | Child organization | Optional | ⚠️ Only if agent follows link |
