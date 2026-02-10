# Reference Implementation - Layer-Stage System

This folder contains a copy of the current Layer-Stage System implementation from:
`/layer_1/layer_1_features/layer_1_feature_layer_stage_system`

**Purpose**: Serve as reference material for the `better_layer_stage_system` research feature.

## Contents Overview

### Root Level
- `CLAUDE.md` - Feature documentation
- `.claude/` - Claude Code integration (commands)

### layer_1/ - Feature Internals
```
layer_1/
├── layer_1_00_ai_manager_system/    # Agent configurations
├── layer_1_02_sub_layers/           # Framework documentation
│   ├── EXTENDING_THE_FRAMEWORK.md
│   ├── FEATURE_TYPE_DECISION_GUIDE.md
│   ├── FLEXIBLE_LAYERING_SYSTEM.md
│   ├── README.md                    # Main framework guide
│   ├── SUB_LAYER_SYSTEM.md
│   └── WORKFLOW_FEATURE_PATTERN.md
└── layer_1_99_stages/               # Workflow stages
    └── stage_1_08_current_product/  # Production content
        ├── changes/                 # Change protocols
        └── setup/                   # Entity creation guides
```

### layer_2/ - Sub-features
```
layer_2/
└── layer_2_features/
    ├── layer_2_feature_handoff_system/       # Handoff documentation
    ├── layer_2_feature_stage_definitions/    # Stage docs (00-10)
    ├── layer_2_feature_layer_definitions/    # Layer rules & numbering
    ├── layer_2_feature_context_gathering/    # Context rules
    └── layer_2_feature_ai_manager_hierarchy/ # Manager patterns
```

## Key Documents to Review

| Document | Location | Purpose |
|----------|----------|---------|
| **Framework Guide** | `layer_1/layer_1_02_sub_layers/README.md` | Core framework explanation |
| **Flexible Layering** | `layer_1/layer_1_02_sub_layers/FLEXIBLE_LAYERING_SYSTEM.md` | Layer flexibility rules |
| **Stage Definitions** | `layer_2/.../layer_2_feature_stage_definitions/` | Stage-by-stage docs |
| **Layer Rules** | `layer_2/.../layer_2_feature_layer_definitions/` | Numbering & nesting |
| **Entity Creation** | `layer_1/layer_1_99_stages/.../setup/` | How to create entities |
| **Handoff Patterns** | `layer_2/.../layer_2_feature_handoff_system/` | Inter-agent handoffs |

## Improvement Areas to Research

Based on this reference implementation, potential areas for improvement:

1. **Naming Consistency**
   - Old: dot notation (`layer_1.02_sub_layers`)
   - New: underscore notation (`layer_0_03_sub_layers`)
   - Status: Partially migrated

2. **Stage Numbering**
   - Old: 00-10 with research at 01
   - New: 00 = registry, 01-11 = workflow stages
   - Status: Implemented in v3.0

3. **Layer Numbering**
   - Absolute vs relative numbering
   - Research context (L-1) handling
   - Status: Needs documentation update

4. **Claude Code Integration**
   - .claude folders with agents/skills/commands/hooks
   - Stage-specific tooling
   - Status: Implemented

5. **Registry Systems**
   - layer_registry at position 00
   - stage_registry at position 00
   - Status: Implemented

## Date Copied
2026-01-25
