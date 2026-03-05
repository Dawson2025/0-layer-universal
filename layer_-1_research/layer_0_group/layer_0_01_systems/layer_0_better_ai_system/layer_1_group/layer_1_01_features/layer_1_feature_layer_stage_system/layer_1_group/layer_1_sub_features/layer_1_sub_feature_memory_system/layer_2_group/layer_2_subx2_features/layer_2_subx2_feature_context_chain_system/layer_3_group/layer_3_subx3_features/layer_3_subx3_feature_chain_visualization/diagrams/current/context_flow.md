---
resource_id: "15e64b61-818e-4e9c-8130-4ffb8a43cfdc"
resource_type: "document"
resource_name: "context_flow"
---
# Context Flow Diagram

**Purpose**: Answer "When does context load and in what order?"
**Last Updated**: 2026-02-05

---

<!-- section_id: "4a302ac6-1a31-4963-8108-2754d2344007" -->
## Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CONTEXT FLOW                                        │
│                            (Current State)                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

                              SESSION START
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: AUTOMATIC LOADING                                                       │
│ ══════════════════════════                                                       │
│                                                                                  │
│ Claude Code automatically loads CLAUDE.md files in path:                         │
│                                                                                  │
│   ~/.claude/CLAUDE.md                                                            │
│         │                                                                        │
│         ▼                                                                        │
│   ~/CLAUDE.md                                                                    │
│         │                                                                        │
│         ▼                                                                        │
│   ~/dawson-workspace/CLAUDE.md                                                   │
│         │                                                                        │
│         ▼                                                                        │
│   ~/dawson-workspace/code/CLAUDE.md                                              │
│         │                                                                        │
│         ▼                                                                        │
│   0_layer_universal/CLAUDE.md                                                    │
│         │                                                                        │
│         ▼                                                                        │
│   (continues to working directory)                                               │
│                                                                                  │
│ Status: ✅ WORKS - Claude Code handles automatically                             │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: PATH-BASED LOADING                                                      │
│ ═══════════════════════════                                                      │
│                                                                                  │
│ Agent should read index.jsonld files in path to working directory:               │
│                                                                                  │
│   layer_-1_research/                                                             │
│   └── layer_-1_better_ai_system/                                                │
│       └── layer_0_group/                                                        │
│           └── index.jsonld  ◄── Should read this                                │
│           └── layer_0_features/                                                 │
│               └── index.jsonld  ◄── Should read this                            │
│               └── layer_0_feature_context_framework/                            │
│                   └── index.jsonld  ◄── Should read this                        │
│                                                                                  │
│ Status: ⚠️ INCONSISTENT - Agent may or may not read these                        │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: TRIGGER-BASED LOADING                                                   │
│ ══════════════════════════════                                                   │
│                                                                                  │
│ Triggers defined in index.jsonld:                                                │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ trigger:onEntityCreation                                                     │ │
│ │ ────────────────────────                                                     │ │
│ │ WHEN: Agent creates new directory/file                                       │ │
│ │ SHOULD LOAD: conventions.childNaming, entity-creation skill                  │ │
│ │                                                                              │ │
│ │ Status: ⚠️ DEFINED but not enforced                                          │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ trigger:onStageEnter                                                         │ │
│ │ ────────────────────                                                         │ │
│ │ WHEN: Agent enters stage_*_* directory                                       │ │
│ │ SHOULD LOAD: Stage workflow skill, stage CLAUDE.md                           │ │
│ │                                                                              │ │
│ │ Status: ⚠️ DEFINED but not enforced                                          │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ trigger:onSessionStart                                                       │ │
│ │ ──────────────────────                                                       │ │
│ │ WHEN: New session begins                                                     │ │
│ │ SHOULD LOAD: CLAUDE.md, index.jsonld, status.json                            │ │
│ │                                                                              │ │
│ │ Status: ⚠️ DEFINED but not enforced                                          │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: ON-DEMAND LOADING                                                       │
│ ══════════════════════════                                                       │
│                                                                                  │
│ Agent follows nav: links when it decides to:                                     │
│                                                                                  │
│   nav:parent ──────▶ Go up to parent directory                                  │
│   nav:children ────▶ List children to explore                                   │
│   nav:siblings ────▶ Find related entities                                      │
│   nav:skills ──────▶ Load relevant skills                                       │
│   nav:stages ──────▶ Find stage directories                                     │
│   rel:treeOfNeedsBranch ──▶ Find requirements                                   │
│                                                                                  │
│ Status: ⚠️ OPTIONAL - Agent may not know these exist                             │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "b48a8402-f62f-4ec0-8c85-b82b2c002c4e" -->
## Flow by Action Type

<!-- section_id: "28641d06-bec4-4002-b45c-4c12f45c9490" -->
### Starting Work in a Directory

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    STARTING WORK IN A DIRECTORY                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

    Agent navigates to: layer_0_feature_context_framework/
                                    │
         ┌──────────────────────────┴──────────────────────────┐
         │                                                      │
         ▼                                                      ▼
┌─────────────────────────┐                    ┌─────────────────────────┐
│   WHAT SHOULD HAPPEN    │                    │   WHAT ACTUALLY HAPPENS │
├─────────────────────────┤                    ├─────────────────────────┤
│                         │                    │                         │
│ 1. Read CLAUDE.md       │                    │ 1. Read CLAUDE.md       │
│    (automatic)          │                    │    (automatic) ✅       │
│                         │                    │                         │
│ 2. Read index.jsonld    │                    │ 2. Maybe read index     │
│    (trigger)            │                    │    (if agent thinks to) │
│                         │                    │    ⚠️                    │
│ 3. Extract conventions  │                    │                         │
│    (from index)         │                    │ 3. Start working        │
│                         │                    │    (without conventions)│
│ 4. Store in context     │                    │    ⚠️                    │
│    (for later use)      │                    │                         │
│                         │                    │                         │
│ 5. Start working        │                    │                         │
│    (with full context)  │                    │                         │
└─────────────────────────┘                    └─────────────────────────┘
```

<!-- section_id: "45214b8f-25b3-4c3b-ae2d-7da3321dd9d4" -->
### Creating a New Entity

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        CREATING A NEW ENTITY                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

    Agent wants to create new sub_feature
                                    │
         ┌──────────────────────────┴──────────────────────────┐
         │                                                      │
         ▼                                                      ▼
┌─────────────────────────┐                    ┌─────────────────────────┐
│   WHAT SHOULD HAPPEN    │                    │   WHAT ACTUALLY HAPPENS │
├─────────────────────────┤                    ├─────────────────────────┤
│                         │                    │                         │
│ 1. Trigger fires:       │                    │ 1. Agent creates:       │
│    onEntityCreation     │                    │    mkdir subfeature_*   │
│                         │                    │    ❌                    │
│ 2. Load conventions:    │                    │                         │
│    conventions.childNaming                   │ 2. No validation        │
│                         │                    │    happens              │
│ 3. Load skill:          │                    │    ❌                    │
│    entity-creation      │                    │                         │
│                         │                    │ 3. Wrong name persists  │
│ 4. Validate name:       │                    │    until someone notices│
│    layer_1_subx2_feature_*│                    │    ❌                    │
│                         │                    │                         │
│ 5. Create if valid      │                    │                         │
└─────────────────────────┘                    └─────────────────────────┘
```

<!-- section_id: "1f05304f-2660-468b-820c-34fec7c34ffa" -->
### Entering a Stage

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          ENTERING A STAGE                                        │
└─────────────────────────────────────────────────────────────────────────────────┘

    Agent enters: stage_-1_05_design/
                                    │
         ┌──────────────────────────┴──────────────────────────┐
         │                                                      │
         ▼                                                      ▼
┌─────────────────────────┐                    ┌─────────────────────────┐
│   WHAT SHOULD HAPPEN    │                    │   WHAT ACTUALLY HAPPENS │
├─────────────────────────┤                    ├─────────────────────────┤
│                         │                    │                         │
│ 1. Trigger fires:       │                    │ 1. Agent enters stage   │
│    onStageEnter         │                    │                         │
│                         │                    │ 2. Maybe reads CLAUDE.md│
│ 2. Load stage skill:    │                    │    (if it exists)       │
│    05_design-workflow   │                    │    ⚠️                    │
│                         │                    │                         │
│ 3. Load stage CLAUDE.md │                    │ 3. Works without stage  │
│                         │                    │    workflow guidance    │
│ 4. Activate stage       │                    │    ⚠️                    │
│    behaviors            │                    │                         │
└─────────────────────────┘                    └─────────────────────────┘
```

---

<!-- section_id: "b36b87c6-0b58-4b8c-8c73-4a4e5475a72f" -->
## Loading Sequence Summary

| Phase | What | When | Status |
|-------|------|------|--------|
| 1 | CLAUDE.md chain | Session start | ✅ Automatic |
| 2 | index.jsonld in path | Entering directory | ⚠️ Inconsistent |
| 3 | Trigger-based context | Specific actions | ⚠️ Not enforced |
| 4 | On-demand via nav: | Agent discretion | ⚠️ Optional |

<!-- section_id: "3a779990-4999-4a77-92d4-5f0955c4e2f1" -->
## Gaps to Address

1. **No index.jsonld auto-loading** - Agent must explicitly read it
2. **Triggers not enforced** - Defined but nothing fires them
3. **No validation on actions** - Can create entities with wrong names
4. **No context discovery** - Agent doesn't know what context is available
