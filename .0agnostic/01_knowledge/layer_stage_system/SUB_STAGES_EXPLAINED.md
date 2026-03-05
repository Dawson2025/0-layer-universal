---
resource_id: "22366ffc-14f0-4aad-b746-d7667ef8ebf4"
resource_type: "knowledge"
resource_name: "SUB_STAGES_EXPLAINED"
---
# Sub-Stages Explained (sub_stage and subxN_stage)

<!-- section_id: "60fc5ea5-ea6c-409e-8730-4b9dbd6aa9ff" -->
## Overview

Just as layers can have sub-layers, **stages can have sub-stages**. Sub-stages break down workflow phases into finer-grained steps, each potentially being an agent entry point.

---

<!-- section_id: "58ed36ac-4b41-47cd-9163-aaf99915629a" -->
## What Are Sub-Stages?

Sub-stages are nested divisions within a stage:

```
stage_06_development/
├── sub_stage_06_01_setup/
├── sub_stage_06_02_implementation/
├── sub_stage_06_03_integration/
└── sub_stage_06_04_cleanup/
```

Each sub-stage represents a **distinct phase** within the parent stage's workflow.

---

<!-- section_id: "4741c8f8-13d0-4738-a2a5-3893b5df5528" -->
## Why Sub-Stages?

<!-- section_id: "e944df29-446a-4ba5-ba2a-927a561c130c" -->
### Problem: Stage Too Broad

```
stage_06_development/
└── outputs/
    └── [Everything mixed together]
```

<!-- section_id: "021daf5e-810f-48e8-b3df-3f98e21f827f" -->
### Solution: Sub-Stages for Organization

```
stage_06_development/
├── sub_stage_06_01_setup/
│   └── outputs/
│       └── [Setup artifacts]
├── sub_stage_06_02_implementation/
│   └── outputs/
│       └── [Implementation artifacts]
└── sub_stage_06_03_integration/
    └── outputs/
        └── [Integration artifacts]
```

---

<!-- section_id: "ea3a774a-042e-4951-8079-cc7519a2e3ba" -->
## Sub-Stage Naming Convention

```
sub[x{depth}]_stage_{layer}_{stage_num}_{sequence}_{name}/
```

| Component | Meaning | Example |
|-----------|---------|---------|
| `sub` | Sub-stage prefix | sub |
| `x{depth}` | Depth indicator (omit for depth 1) | x2, x3 |
| `stage_` | Stage marker | stage_ |
| `{layer}` | Parent layer number | 0, 1, 2 |
| `{stage_num}` | Parent stage number | 01-11 |
| `{sequence}` | Sub-stage order | 01, 02, 03 |
| `{name}` | Descriptive name | setup, implementation |

---

<!-- section_id: "e236e428-60d6-4a12-9236-c0c8f14bf971" -->
## Sub-Stage Depth Levels

<!-- section_id: "3c622f95-a7a6-4ac2-a0cd-4070394f6fb6" -->
### Depth 1: `sub_stage_`

Direct children of a stage.

```
stage_06_development/
├── sub_stage_06_01_environment_setup/      # Depth 1
├── sub_stage_06_02_core_implementation/    # Depth 1
├── sub_stage_06_03_feature_integration/    # Depth 1
└── sub_stage_06_04_final_polish/           # Depth 1
```

<!-- section_id: "01a5af2e-0252-4af0-a840-7b29cfe95d50" -->
### Depth 2: `subx2_stage_`

Nested within a depth-1 sub-stage.

```
sub_stage_06_02_core_implementation/
├── subx2_stage_06_02_01_models/            # Depth 2
├── subx2_stage_06_02_02_services/          # Depth 2
├── subx2_stage_06_02_03_controllers/       # Depth 2
└── subx2_stage_06_02_04_views/             # Depth 2
```

<!-- section_id: "bc0d7bb3-c016-470f-8b41-e8132794c360" -->
### Depth 3+: `subx3_stage_`, `subx4_stage_`, etc.

Continue pattern as needed.

```
subx2_stage_06_02_02_services/
├── subx3_stage_06_02_02_01_auth_service/   # Depth 3
├── subx3_stage_06_02_02_02_user_service/   # Depth 3
└── subx3_stage_06_02_02_03_data_service/   # Depth 3
```

---

<!-- section_id: "1ee2f4d2-6029-4d4c-b1fb-8df2531c730f" -->
## Sub-Stage Structure

Each sub-stage can be an agent entry point:

```
sub_stage_06_02_implementation/
├── 0AGNOSTIC.md              # Identity, triggers
├── 0INDEX.md                 # Contents
├── CLAUDE.md                 # Tool context (generated)
├── .0agnostic/               # Sync source
│   ├── hooks/scripts/
│   └── episodic/
├── .claude/                  # Tool config
├── outputs/                  # Sub-stage outputs
├── hand_off_documents/       # Handoffs to next sub-stage
└── <working_content>/        # Working files
```

---

<!-- section_id: "73b19c6b-3699-4299-80dc-23c81452598f" -->
## Sub-Stage Context Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SUB-STAGE CONTEXT FLOW                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LAYER CASCADE                                                              │
│  ─────────────                                                              │
│  layer_0/CLAUDE.md                          (Universal)                     │
│       │                                                                     │
│       ▼                                                                     │
│  layer_1/project/CLAUDE.md                  (Project)                       │
│       │                                                                     │
│       ▼                                                                     │
│  STAGE CASCADE                                                              │
│  ─────────────                                                              │
│  layer_1_group/layer_1_99_stages/CLAUDE.md  (Stages root)                  │
│       │                                                                     │
│       ▼                                                                     │
│  stage_06_development/CLAUDE.md             (Parent stage)                  │
│       │                                                                     │
│       ▼                                                                     │
│  SUB-STAGE CASCADE                                                          │
│  ────────────────                                                           │
│  sub_stage_06_02_implementation/CLAUDE.md   (Depth 1)                      │
│       │                                                                     │
│       ▼                                                                     │
│  subx2_stage_06_02_02_services/CLAUDE.md    (Depth 2)                      │
│       │                                                                     │
│       │ points to                                                           │
│       ▼                                                                     │
│  .claude/                                   (tool config)                   │
│  .0agnostic/                                (sync source)                   │
│  outputs/                                   (deliverables)                  │
│  hand_off_documents/                        (transitions)                   │
│                                                                             │
│  CRITICAL RULES INHERITED:                                                  │
│  - All layer_0 rules                                                        │
│  - All project rules                                                        │
│  - All stage_06_development rules                                           │
│  - All sub_stage_06_02 rules                                               │
│  - subx2_stage_06_02_02 specific rules                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "18a54d06-8a1b-457f-8f86-3b60b7c18226" -->
## When to Use Sub-Stages

<!-- section_id: "8f17fdfb-6015-4787-8912-01112684b360" -->
### Use Sub-Stages When:

1. **Complex Stage**
   - Stage has multiple distinct phases
   - Each phase produces different outputs

2. **Different Agents/Roles**
   - Different expertise needed per phase
   - Example: Setup (DevOps) vs Implementation (Developer)

3. **Clear Handoffs**
   - Work flows from one phase to next
   - Handoff documents needed between phases

4. **Large Output Volume**
   - Too many outputs to organize in one stage
   - Need finer-grained organization

<!-- section_id: "5cfca1bf-632b-471d-9efc-bf0a4ed06c3c" -->
### Don't Use Sub-Stages When:

1. **Simple Stage**
   - Work is straightforward
   - Single phase sufficient

2. **Few Outputs**
   - Easy to organize in parent stage
   - No need for subdivision

---

<!-- section_id: "209990a3-de12-431e-83c3-3227da07c897" -->
## Sub-Stage Critical Rules

Each sub-stage level can add rules:

```
stage_06_development/CLAUDE.md
├── CRITICAL: "All code must have tests"
│
└── sub_stage_06_02_implementation/CLAUDE.md
    ├── INHERITS: stage_06 rules
    ├── ADDS: "Follow architecture patterns"
    │
    └── subx2_stage_06_02_02_services/CLAUDE.md
        ├── INHERITS: stage + sub_stage rules
        └── ADDS: "Services must be stateless"
```

---

<!-- section_id: "ea3c596d-71ea-44a6-a4a7-d2c03d0910d4" -->
## Sub-Stage CLAUDE.md Template

```markdown
# sub_stage_N_XX_YY_<name> - CLAUDE.md

## Identity

**Role**: [Phase specialist]
**Scope**: [What this sub-stage covers]
**Parent Stage**: [Parent stage path]
**Previous Sub-Stage**: [For handoff reference]
**Next Sub-Stage**: [For handoff reference]

## [CRITICAL] Rules - EVERY API Call

⚠️ These rules MUST be followed in this sub-stage:

### Inherited from layer_0 (Universal)
- [ ] [Universal rules...]

### Inherited from Parent Stage
- [ ] [Stage rules...]

### This Sub-Stage
- [ ] [Sub-stage specific rules...]

## Triggers

Load this context when:
- Stage is: [parent stage number]
- Phase is: [this phase description]
- Working on: [phase-specific topics]

## Pointers

| Resource | Location |
|----------|----------|
| Outputs | `outputs/` |
| Handoffs | `hand_off_documents/` |
| Parent Stage | `../` |
| Previous Sub-Stage | `../sub_stage_XX_YY-1_name/` |
| Next Sub-Stage | `../sub_stage_XX_YY+1_name/` |

## Workflow

1. [Step 1 in this sub-stage]
2. [Step 2 in this sub-stage]
3. Create handoff document for next sub-stage
```

---

<!-- section_id: "1f94170c-5d0f-49dd-9700-27021b251089" -->
## Sub-Stage Workflow Example

```
┌──────────────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT STAGE WORKFLOW                         │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  sub_stage_06_01_setup                                               │
│  ├── outputs/: Environment configs, dependencies                     │
│  └── handoff → sub_stage_06_02_implementation                       │
│                     │                                                │
│                     ▼                                                │
│  sub_stage_06_02_implementation                                      │
│  ├── subx2_stage_06_02_01_models/                                   │
│  │   └── outputs/: Data models, schemas                             │
│  │   └── handoff → services                                         │
│  ├── subx2_stage_06_02_02_services/                                 │
│  │   └── outputs/: Service classes                                  │
│  │   └── handoff → controllers                                      │
│  ├── subx2_stage_06_02_03_controllers/                              │
│  │   └── outputs/: API endpoints                                    │
│  │   └── handoff → views                                            │
│  └── subx2_stage_06_02_04_views/                                    │
│      └── outputs/: UI components                                     │
│      └── handoff → integration                                       │
│                     │                                                │
│                     ▼                                                │
│  sub_stage_06_03_integration                                         │
│  ├── outputs/: Integrated system                                     │
│  └── handoff → stage_07_testing                                     │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "aeee3a2f-ea41-4682-bfae-28925746e9a5" -->
## Generalized Pattern: subxN_stage_

For any depth N:

```
subx{N}_stage_{layer}_{parent_stage}_{sequence}_{name}/
```

| Depth | Prefix | Example |
|-------|--------|---------|
| 1 | `sub_stage_` | `sub_stage_06_01_setup/` |
| 2 | `subx2_stage_` | `subx2_stage_06_01_01_local/` |
| 3 | `subx3_stage_` | `subx3_stage_06_01_01_01_deps/` |
| N | `subx{N}_stage_` | `subx{N}_stage_...` |

---

<!-- section_id: "5255610b-0dbd-4214-9193-82d9b6fb02dc" -->
## AI Agent Navigation in Sub-Stages

```
1. Identify parent stage from context
2. Check if stage has sub-stages
3. Identify current sub-stage depth
4. Load context cascade: layer → stage → sub-stages
5. Accumulate critical rules from each level
6. Check handoff docs from previous sub-stage
7. Work within current sub-stage scope
8. Create handoff for next sub-stage when done
```

---

<!-- section_id: "a9895b7e-6099-495e-8084-16960f8742b5" -->
## Self-Check for Sub-Stage Work

- [ ] Did I load parent stage context?
- [ ] Did I identify my current sub-stage?
- [ ] Am I following ALL inherited rules?
- [ ] Did I read handoff from previous sub-stage?
- [ ] Am I putting outputs in the right sub-stage?
- [ ] Will I create a handoff for the next sub-stage?

---

*See SUB_LAYERS_AS_ENTRY_POINTS.md for sub-layer context architecture*
*See NESTED_DEPTH_NAMING.md for subxN naming conventions*
