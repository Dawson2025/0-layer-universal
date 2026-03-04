# Entity Creation Flow

**Purpose**: Show how context loads when an agent needs to create a new entity (feature, sub-feature, component).

---

## Current Flow: Entity Creation

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ENTITY CREATION CONTEXT FLOW                                  │
│                    (Creating a new sub-feature)                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

    USER: "Create a new sub-feature called 'session_recovery'"
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 1: Agent has base context (from session start)                      │
    │                                                                           │
    │  Already loaded:                                                          │
    │  • System prompt                                                          │
    │  • Tools                                                                  │
    │  • CLAUDE.md chain to working directory                                   │
    │                                                                           │
    │  Working directory: .../layer_0_feature_context_framework/                │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 2: Agent recognizes this is entity creation                         │
    │                                                                           │
    │  Task type: Entity Creation                                               │
    │  Entity type: sub-feature                                                 │
    │  Parent: layer_0_feature_context_framework                                │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 3: Agent reads index.jsonld of PARENT                               │
    │                                                                           │
    │  READ: .../layer_0_feature_context_framework/index.jsonld                 │
    │                                                                           │
    │  Finds:                                                                   │
    │  • conventions.childNaming.pattern = "layer_{N+1}_{type}_{name}"          │
    │  • conventions.childNaming.currentLayer = 0                               │
    │  • conventions.childNaming.childLayer = 1                                 │
    │  • conventions.childNaming.example = "layer_1_subx2_feature_context_system" │
    │  • trigger:onEntityCreation.skill = ".claude/skills/entity-creation/"     │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 4: Agent follows trigger to load skill                              │
    │                                                                           │
    │  READ: .../layer_0_group/.claude/skills/entity-creation/SKILL.md          │
    │                                                                           │
    │  Finds:                                                                   │
    │  • Naming pattern rules                                                   │
    │  • Layer hierarchy table                                                  │
    │  • Checklist for entity creation                                          │
    │  • Common mistakes table                                                  │
    │  • Reference to schema for entityTypes                                    │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 5: Agent reads schema (optional, for validation)                    │
    │                                                                           │
    │  READ: .../layer_0_group/.claude/schema/layer-stage-schema.jsonld         │
    │                                                                           │
    │  Finds:                                                                   │
    │  • entityTypes definitions                                                │
    │  • Valid type values: feature, sub_feature, component, subproject         │
    │  • Naming patterns for each type                                          │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 6: Agent applies naming convention                                  │
    │                                                                           │
    │  Parent layer: 0                                                          │
    │  Child layer: 1                                                           │
    │  Type: sub_feature (uses underscore)                                      │
    │  Name: session_recovery                                                   │
    │                                                                           │
    │  Result: layer_1_subx2_feature_session_recovery                             │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 7: Agent creates entity with correct structure                      │
    │                                                                           │
    │  Creates:                                                                 │
    │  └── layer_1_subx2_feature_session_recovery/                                │
    │      ├── index.jsonld (with nav:parent, conventions for ITS children)     │
    │      └── CLAUDE.md (with identity, purpose)                               │
    └───────────────────────────────────────────────────────────────────────────┘
```

---

## Context Chain for Entity Creation

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    CONTEXT CHAIN: ENTITY CREATION                                │
└─────────────────────────────────────────────────────────────────────────────────┘

    BASE CONTEXT (auto-loaded at session start)
    ════════════════════════════════════════════
    │
    │   ~/.claude/CLAUDE.md
    │       │
    │       │ Contains: "[CRITICAL] Context Traversal Rule"
    │       │           "read index.jsonld"
    │       ▼
    │   .../0_layer_universal/CLAUDE.md
    │       │
    │       │ Contains: "Follow layer-stage framework conventions"
    │       ▼
    │   .../layer_-1_better_ai_system/CLAUDE.md
    │       │
    │       │ Contains: "Features in layer_0_group/layer_0_features/"
    │       ▼
    ▼
    TASK-TRIGGERED CONTEXT (loaded when creating entity)
    ════════════════════════════════════════════════════
    │
    │   parent/index.jsonld
    │       │
    │       │ Contains: conventions.childNaming
    │       │           trigger:onEntityCreation → skill path
    │       ▼
    │   .claude/skills/entity-creation/SKILL.md
    │       │
    │       │ Contains: Naming rules, checklist
    │       │           "See schema for entityTypes"
    │       ▼
    │   .claude/schema/layer-stage-schema.jsonld
    │       │
    │       │ Contains: entityTypes, valid patterns
    │       ▼
    ▼
    AGENT HAS COMPLETE CONTEXT FOR ENTITY CREATION
```

---

## What Could Go Wrong (Current State)

| Problem | Cause | Result |
|---------|-------|--------|
| Wrong naming | Agent doesn't read parent's index.jsonld | Creates `subfeature_X` instead of `layer_1_subx2_feature_X` |
| Missing conventions | Parent index.jsonld lacks conventions | Agent guesses naming |
| Skill not found | Trigger path is wrong or skill missing | Agent creates without checklist |
| Wrong layer number | Agent doesn't know parent's layer | Creates `layer_0_` when should be `layer_1_` |

---

## Files Involved

| Order | File | What Agent Learns |
|-------|------|-------------------|
| 1 | `parent/index.jsonld` | Naming pattern, trigger to skill |
| 2 | `.claude/skills/entity-creation/SKILL.md` | Procedure, checklist, examples |
| 3 | `.claude/schema/layer-stage-schema.jsonld` | Valid types, validation rules |

---

*Last updated: 2026-02-05*
