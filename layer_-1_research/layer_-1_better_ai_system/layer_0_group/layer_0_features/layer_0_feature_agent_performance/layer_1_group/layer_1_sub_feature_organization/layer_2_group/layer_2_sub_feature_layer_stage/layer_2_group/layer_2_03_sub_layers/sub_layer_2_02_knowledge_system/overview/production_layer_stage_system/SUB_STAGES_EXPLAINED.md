# Sub-Stages Explained (sub_stage and subxN_stage)

## Overview

Just as layers can have sub-layers, **stages can have sub-stages**. Sub-stages break down workflow phases into finer-grained steps, each potentially being an agent entry point.

---

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

## Why Sub-Stages?

### Problem: Stage Too Broad

```
stage_06_development/
└── outputs/
    └── [Everything mixed together]
```

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

## Sub-Stage Depth Levels

### Depth 1: `sub_stage_`

Direct children of a stage.

```
stage_06_development/
├── sub_stage_06_01_environment_setup/      # Depth 1
├── sub_stage_06_02_core_implementation/    # Depth 1
├── sub_stage_06_03_feature_integration/    # Depth 1
└── sub_stage_06_04_final_polish/           # Depth 1
```

### Depth 2: `subx2_stage_`

Nested within a depth-1 sub-stage.

```
sub_stage_06_02_core_implementation/
├── subx2_stage_06_02_01_models/            # Depth 2
├── subx2_stage_06_02_02_services/          # Depth 2
├── subx2_stage_06_02_03_controllers/       # Depth 2
└── subx2_stage_06_02_04_views/             # Depth 2
```

### Depth 3+: `subx3_stage_`, `subx4_stage_`, etc.

Continue pattern as needed.

```
subx2_stage_06_02_02_services/
├── subx3_stage_06_02_02_01_auth_service/   # Depth 3
├── subx3_stage_06_02_02_02_user_service/   # Depth 3
└── subx3_stage_06_02_02_03_data_service/   # Depth 3
```

---

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

## When to Use Sub-Stages

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

### Don't Use Sub-Stages When:

1. **Simple Stage**
   - Work is straightforward
   - Single phase sufficient

2. **Few Outputs**
   - Easy to organize in parent stage
   - No need for subdivision

---

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
