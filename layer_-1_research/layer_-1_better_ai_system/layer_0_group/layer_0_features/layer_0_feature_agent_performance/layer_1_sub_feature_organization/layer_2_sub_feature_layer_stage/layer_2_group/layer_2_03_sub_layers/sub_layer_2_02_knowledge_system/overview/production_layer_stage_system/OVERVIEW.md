# Layer-Stage System Overview

## What Is It?

The layer-stage system is a hierarchical framework for organizing AI-assisted work. It provides:
- **Layers**: Scope levels (universal → project → feature → component)
- **Stages**: Workflow phases (01-11: gather → research → design → develop → archive)
- **Sub-layers**: Content types (prompts, knowledge, rules, setup-dependent)

## Core Principles

### 1. Hierarchical Inheritance
Lower layers inherit from higher layers:
```
layer_0 (universal) → applies to ALL
  └── layer_1 (projects) → project-specific, inherits from layer_0
      └── layer_2 (features) → feature-specific, inherits from layer_1
          └── layer_3 (components) → component-specific, inherits from layer_2
```

### 2. Scope Isolation
Each layer only contains what's specific to that scope:
- Don't put universal rules in a project
- Don't put project-specific config in universal

### 3. Stage-Based Workflow
Work progresses through stages:
```
01_request_gathering → 02_research → 03_instructions → 04_planning →
05_design → 06_development → 07_testing → 08_criticism → 09_fixing →
10_current_product → 11_archives
```

## Visual Structure

```
0_layer_universal/                           # Root
├── layer_0/                                 # Universal (applies to ALL)
│   ├── layer_0_03_sub_layers/              # Sub-layers (content types)
│   │   ├── sub_layer_0_01_prompts/
│   │   ├── sub_layer_0_02_knowledge_system/  ← You are here
│   │   ├── sub_layer_0_03_principles/
│   │   ├── sub_layer_0_04_rules/
│   │   └── sub_layer_0_05+_setup_dependant_hierarchy/
│   └── layer_0_99_stages/                  # Workflow stages
│       ├── stage_0_01_request_gathering/
│       ├── stage_0_02_research/
│       └── ... (01-11)
├── layer_1/                                 # Projects
│   └── layer_1_projects/
│       └── layer_1_project_<name>/
│           ├── layer_1_group/              # Project internals
│           └── layer_2_group/              # Project's features
└── layer_-1_research/                       # Research layer
    └── layer_-1_<project>/
        ├── layer_-1_group/                 # Research internals
        └── layer_0_group/                  # Research features
```

## Key Concepts

### Layers (Scope)

| Layer | Purpose | Example |
|-------|---------|---------|
| layer_0 | Universal rules, knowledge | Applies to all projects |
| layer_1 | Projects | A specific application |
| layer_2 | Features | A feature within a project |
| layer_3+ | Components | Sub-components |
| layer_-1 | Research | Experimental/research work |

### Stages (Workflow)

| Stage | Purpose |
|-------|---------|
| 01_request_gathering | Collect and clarify requirements |
| 02_research | Explore problem space, gather information |
| 03_instructions | Define constraints and guidelines |
| 04_planning | Break work into subtasks |
| 05_design | Architecture and design decisions |
| 06_development | Implementation |
| 07_testing | Verification and validation |
| 08_criticism | Review and critique |
| 09_fixing | Address issues found |
| 10_current_product | Final deliverable |
| 11_archives | Historical versions |

### Sub-Layers (Content Types)

| Sub-Layer | Purpose |
|-----------|---------|
| 01_prompts | System prompts, init prompts |
| 02_knowledge_system | Documentation, reference material |
| 03_principles | Guiding principles, philosophy |
| 04_rules | Mandatory rules, protocols |
| 05+_setup_dependant_hierarchy | OS/environment-specific content |

## The Two Containers

Every entity has two main containers:

1. **`layer_N_group/`** - Internal content (this layer's stuff)
   - Sub-layers (03_sub_layers)
   - Stages (99_stages)
   - Registry (00_layer_registry)

2. **`layer_N+1_group/`** - Children (next layer down)
   - Features, components, sub-projects

```
my_project/
├── layer_1_group/        # My internal stuff
│   ├── layer_1_03_sub_layers/
│   └── layer_1_99_stages/
└── layer_2_group/        # My children (features)
    └── layer_2_features/
```

## How It All Connects

```
                    ┌─────────────────┐
                    │   layer_0       │  Universal
                    │   (applies to   │  rules, knowledge
                    │    everything)  │
                    └────────┬────────┘
                             │ inherits
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌──────────┐   ┌──────────┐   ┌──────────┐
       │ layer_1  │   │ layer_1  │   │ layer_-1 │
       │ Project A│   │ Project B│   │ Research │
       └────┬─────┘   └────┬─────┘   └────┬─────┘
            │              │              │
      ┌─────┴─────┐        │        ┌─────┴─────┐
      ▼           ▼        ▼        ▼           ▼
   Feature 1  Feature 2   ...    Research    Research
   (layer_2)  (layer_2)          Feature 1   Feature 2
```

---

*See LAYERS_EXPLAINED.md, STAGES_EXPLAINED.md, SUB_LAYERS_EXPLAINED.md for details*
