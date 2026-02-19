# Entity Instantiation Guide

## Overview

This guide explains how to create new entities in the layer-stage system.

## General Instantiation Process

### Step 1: Determine Entity Type and Location

| Creating a... | Goes in... | Layer Number |
|---------------|------------|--------------|
| New project | `layer_1/layer_1_projects/` | layer_1 |
| New feature | `<project>/layer_2_group/layer_2_features/` | layer_2 |
| New research project | `layer_-1_research/` | layer_-1 |
| New research feature | `<research>/layer_0_group/layer_0_features/` | layer_0 |

### Step 2: Create Directory Structure

```bash
# Example: Creating a new project
mkdir -p layer_1_project_myapp/{.0agnostic/{hooks/scripts,skills,agents,episodic/{sessions,changes}},layer_1_group/{layer_1_00_layer_registry/proposals,layer_1_03_sub_layers/{sub_layer_1_00_sub_layer_registry,sub_layer_1_01_prompts,sub_layer_1_02_knowledge_system/{overview,things_learned},sub_layer_1_03_principles,sub_layer_1_04_rules,sub_layer_1_05+_setup_dependant_hierarchy},layer_1_99_stages},layer_2_group/{layer_2_00_layer_registry/proposals,layer_2_features}}
```

### Step 3: Create Required Files

#### 0AGNOSTIC.md (Identity)

```markdown
# 0AGNOSTIC.md - <entity_name>

## Identity

You are an agent at **Layer N** (Type), **Entity**: <name>.

- **Role**: <role description>
- **Scope**: <what this entity covers>
- **Parent**: `../0AGNOSTIC.md`
- **Children**: `layer_N+1_group/layer_N+1_<type>/`

## Triggers

Load this context when:
- User mentions: "<keywords>"
- Working on: <activities>
- Entering: `<path>`

## Pointers

### On Entry
1. Read `0INDEX.md` for current state

### Resources (load on-demand)
| Resource | Location |
|----------|----------|
| Rules | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Knowledge | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge_system/` |
```

#### 0INDEX.md (Contents)

```markdown
# Index: <entity_name>

## Purpose
<brief description>

## Structure Overview
<directory tree>

## Contents
| Item | Description | Location |
|------|-------------|----------|
| ... | ... | ... |

## Navigation
| Looking for... | Go to... |
|----------------|----------|
| ... | ... |
```

### Step 4: Generate Tool Files

Run the agnostic-sync script:
```bash
bash .0agnostic/hooks/scripts/agnostic-sync.sh all
```

Or copy from parent and modify.

### Step 5: Create Stage Structure (if needed)

```bash
# Create all 11 stages
for i in 01_request_gathering 02_research 03_instructions 04_planning 05_design 06_development 07_testing 08_criticism 09_fixing 10_current_product 11_archives; do
  mkdir -p "layer_N_99_stages/stage_N_$i/outputs/{by_topic,episodic/{sessions,changes}}"
done
```

---

## Specific Entity Instantiation

### Creating a New Project

1. **Location**: `layer_1/layer_1_projects/layer_1_project_<name>/`

2. **Required structure**:
```
layer_1_project_<name>/
├── 0AGNOSTIC.md
├── 0INDEX.md
├── .0agnostic/
│   ├── hooks/scripts/
│   ├── skills/
│   ├── agents/
│   └── episodic/
├── layer_1_group/
│   ├── layer_1_00_layer_registry/proposals/
│   ├── layer_1_03_sub_layers/
│   │   ├── sub_layer_1_01_prompts/
│   │   ├── sub_layer_1_02_knowledge_system/
│   │   ├── sub_layer_1_03_principles/
│   │   ├── sub_layer_1_04_rules/
│   │   └── sub_layer_1_05+_setup_dependant_hierarchy/
│   └── layer_1_99_stages/
└── layer_2_group/
    ├── layer_2_00_layer_registry/proposals/
    └── layer_2_features/
```

3. **0AGNOSTIC.md template**:
```markdown
# 0AGNOSTIC.md - <project_name>

## Identity
You are an agent at **Layer 1** (Project), **Project**: <name>.
- **Role**: Project Manager
- **Scope**: <project description>
- **Parent**: `../0AGNOSTIC.md`
- **Children**: `layer_2_group/layer_2_features/`
```

### Creating a New Feature

1. **Location**: `<project>/layer_2_group/layer_2_features/layer_2_feature_<name>/`

2. **Required structure**: Same as project but with layer_2/layer_3

3. **0AGNOSTIC.md template**:
```markdown
# 0AGNOSTIC.md - <feature_name>

## Identity
You are an agent at **Layer 2** (Feature), **Feature**: <name>.
- **Role**: Feature Developer
- **Scope**: <feature description>
- **Parent**: `../../0AGNOSTIC.md`
- **Children**: `layer_3_group/layer_3_components/` (if any)
```

### Creating a New Research Project

1. **Location**: `layer_-1_research/layer_-1_<name>/`

2. **Key difference**: Uses layer_0_group for features (not layer_2_group)

3. **0AGNOSTIC.md includes**:
```markdown
- **Scope**: Research, design, planning only. Does not implement in production.
```

### Creating a New Stage

1. **Location**: `<entity>/layer_N_group/layer_N_99_stages/stage_N_XX_<name>/`

2. **Structure**:
```
stage_N_XX_<name>/
├── outputs/
│   ├── by_topic/
│   ├── by_need/
│   └── episodic/
│       ├── sessions/
│       └── changes/
└── hand_off_documents/
    ├── incoming/from_above/
    ├── incoming/from_below/
    ├── outgoing/to_above/
    └── outgoing/to_below/
```

### Creating a Proposal

1. **Location**: `<entity>/layer_N_group/layer_N_00_layer_registry/proposals/`

2. **For new proposals**: Start in `staging/stage_experimental/stage_02_research/`

3. **Structure**:
```markdown
# Proposal: <Name> vX

**Status**: Draft | Experimental | Testing | Rollout | Active | Archived
**Created**: YYYY-MM-DD
**Scope**: <what this proposal changes>

## Problem Statement
...

## Proposed Solution
...

## Implementation Plan
...
```

---

## Post-Instantiation Checklist

- [ ] 0AGNOSTIC.md created with correct identity
- [ ] 0INDEX.md created with contents
- [ ] .0agnostic/ structure created
- [ ] Tool files generated (CLAUDE.md, etc.)
- [ ] Parent's 0INDEX.md updated to include new entity
- [ ] Parent's registry updated (if applicable)

---

*See MAINTENANCE_GUIDE.md for ongoing entity management*
