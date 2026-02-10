# Entity Instantiation Guide

## Overview

This guide explains how to create new entities in the layer-stage system. For the canonical directory structure, see `@imports/entity_structure.md`.

## General Instantiation Process

### Step 1: Determine Entity Type and Location

| Creating a... | Goes in... | Layer Number |
|---------------|------------|--------------|
| New project | `layer_1/layer_1_projects/` | layer_1 |
| New feature | `<project>/layer_2_group/layer_2_features/` | layer_2 |
| New component | `<feature>/layer_3_group/layer_3_components/` | layer_3 |
| New research project | `layer_-1_research/` | layer_-1 |
| New research feature | `<research>/layer_0_group/layer_0_features/` | layer_0 |

### Step 2: Create Directory Structure

Read `@imports/entity_structure.md` for the full canonical tree and mkdir template.

Replace `N` with the entity's layer number and `N1` with N+1:

```bash
# Entity root config directories (outputs/ and synthesis/ live inside stages, NOT here)
mkdir -p <entity_name>/{.0agnostic/{agents,episodic_memory/{sessions,changes},hooks/scripts,knowledge,rules,skills},.1merge/{.1claude_merge/{0_synced,1_overrides,2_additions},.1cursor_merge/{0_synced,1_overrides,2_additions},.1gemini_merge/{0_synced,1_overrides,2_additions},.1aider_merge/{0_synced,1_overrides,2_additions},.1codex_merge/{0_synced,1_overrides,2_additions},.1copilot_merge/{0_synced,1_overrides,2_additions}},.claude/{rules,episodic_memory/{sessions,changes}},.cursor/{rules,episodic_memory/{sessions,changes}},.gemini/episodic_memory/{sessions,changes},.codex/episodic_memory/{sessions,changes},.github/instructions}

# Internal layer_N_group structure
mkdir -p <entity_name>/layer_N_group/{layer_N_00_layer_registry/proposals,layer_N_01_ai_manager_system,layer_N_02_manager_handoff_documents/{incoming/{from_above,from_below},outgoing/{to_above,to_below}},layer_N_03_sub_layers/{sub_layer_N_00_sub_layer_registry,sub_layer_N_01_prompts,sub_layer_N_02_knowledge_system/{overview,things_learned},sub_layer_N_03_principles,sub_layer_N_04_rules,sub_layer_N_05+_setup_dependant},layer_N_99_stages}

# Children (if entity has children)
mkdir -p <entity_name>/layer_N1_group/{layer_N1_00_layer_registry/proposals}
```

**IMPORTANT**: Internal layer directories MUST use the `_group` suffix: `layer_N_group/` NOT `layer_N/`.

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

Run the agnostic-sync script on the entity root:
```bash
bash layer_0/.0agnostic/agnostic-sync.sh <entity_dir>
```

This generates CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules from 0AGNOSTIC.md.

### Step 5: Create Stages

Create ALL 12 stages (00-11). **Empty stages are valid. Missing stages are NOT.**

```bash
# Create all stage directories
mkdir -p "layer_N_group/layer_N_99_stages/stage_N_00_stage_registry/{outputs,synthesis}"
for i in 01_request_gathering 02_research 03_instructions 04_planning 05_design 06_development 07_testing 08_criticism 09_fixing 10_current_product 11_archives; do
  mkdir -p "layer_N_group/layer_N_99_stages/stage_N_$i/{outputs,synthesis}"
done

# Add config directories to EACH stage
for stage_dir in layer_N_group/layer_N_99_stages/stage_N_*/; do
  mkdir -p "$stage_dir"/{.0agnostic/{agents,episodic_memory/{sessions,changes},hooks/scripts,knowledge,rules,skills},.1merge/{.1claude_merge/{0_synced,1_overrides,2_additions},.1cursor_merge/{0_synced,1_overrides,2_additions},.1gemini_merge/{0_synced,1_overrides,2_additions},.1aider_merge/{0_synced,1_overrides,2_additions},.1codex_merge/{0_synced,1_overrides,2_additions},.1copilot_merge/{0_synced,1_overrides,2_additions}},.claude/{rules,episodic_memory/{sessions,changes}},.cursor/{rules,episodic_memory/{sessions,changes}},.gemini/episodic_memory/{sessions,changes},.codex/episodic_memory/{sessions,changes},.github/instructions,synthesis}
done
```

### Step 6: Create Stage Files

For each stage, create:
- `0AGNOSTIC.md` — Stage-level context
- `stage_N_XX_name_agent.jsonld` — Stage agent stub

Then run `agnostic-sync.sh` on each stage directory to generate tool files.

### Step 7: Create Orchestrators and Agent Files

| File | Location | Purpose |
|---|---|---|
| `layer_N_orchestrator.gab.jsonld` | Entity root | Entity-level orchestrator |
| `layer_N_99_stages_orchestrator.gab.jsonld` | `layer_N_99_stages/` | Stages orchestrator |
| `stage_N_XX_name_agent.jsonld` | Each stage | Stage agent stub |
| `status_N.json` | `layer_N_99_stages/` | Stage workflow tracker |

Copy orchestrators from a sibling entity and adapt all names/references.

### Step 8: Generate Integration Files

**Every `.jsonld` file MUST have a matching `.integration.md` file.**

```bash
for f in $(find <entity> -name "*.jsonld" -type f); do
  bash tools/jsonld-to-md.sh "$f"
  # Fix naming: rename *.jsonld.integration.md → *.integration.md
  base="${f%.jsonld}"
  [ -f "${f}.integration.md" ] && mv "${f}.integration.md" "${base}.integration.md"
done
```

### Step 9: Run agnostic-sync on ALL directories

```bash
SYNC="layer_0/.0agnostic/agnostic-sync.sh"
for f in $(find <entity> -name "0AGNOSTIC.md" -type f); do
  bash "$SYNC" "$(dirname "$f")"
done
```

### Step 10: Validate

```bash
bash tools/validate-entity.sh <entity-path>
```

---

## Specific Entity Instantiation

### Creating a New Project

1. **Location**: `layer_1/layer_1_projects/layer_1_project_<name>/`

2. **Required structure** (see `@imports/entity_structure.md` for full tree):
```
layer_1_project_<name>/
├── 0AGNOSTIC.md
├── 0INDEX.md
├── README.md
├── layer_1_orchestrator.gab.jsonld
├── layer_1_orchestrator.integration.md
├── .0agnostic/                   # Full structure with episodic_memory/
├── .1merge/                      # 6 tools x 3 tiers
├── .claude/{rules,episodic_memory/}
├── .cursor/{rules,episodic_memory/}
├── .gemini/episodic_memory/
├── .codex/episodic_memory/
├── .github/instructions/
├── layer_1_group/                # MUST use _group suffix
│   ├── layer_1_00_layer_registry/proposals/
│   ├── layer_1_01_ai_manager_system/
│   ├── layer_1_02_manager_handoff_documents/
│   │   ├── incoming/{from_above,from_below}
│   │   └── outgoing/{to_above,to_below}
│   ├── layer_1_03_sub_layers/
│   │   ├── sub_layer_1_01_prompts/
│   │   ├── sub_layer_1_02_knowledge_system/{overview,things_learned}
│   │   ├── sub_layer_1_03_principles/
│   │   ├── sub_layer_1_04_rules/
│   │   └── sub_layer_1_05+_setup_dependant/
│   └── layer_1_99_stages/        # All 12 stages (00-11)
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

2. **Required structure**: Same as project but with layer_2/layer_3 (see `@imports/entity_structure.md`)

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
├── 0AGNOSTIC.md
├── CLAUDE.md (auto-generated)
├── AGENTS.md (auto-generated)
├── GEMINI.md (auto-generated)
├── OPENAI.md (auto-generated)
├── stage_N_XX_name_agent.jsonld
├── stage_N_XX_name_agent.integration.md (auto-generated)
├── outputs/
├── .0agnostic/{agents,episodic_memory/{sessions,changes},hooks/scripts,knowledge,rules,skills}
├── .1merge/{6 tools × 3 tiers}
├── .claude/{rules,episodic_memory/{sessions,changes}}
├── .cursor/{rules,episodic_memory/{sessions,changes}}
├── .gemini/episodic_memory/{sessions,changes}
├── .codex/episodic_memory/{sessions,changes}
├── .github/instructions/
└── synthesis/
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

### Entity Root
- [ ] `0AGNOSTIC.md` created with correct identity
- [ ] `0INDEX.md` created with contents
- [ ] `README.md` created with overview
- [ ] `agnostic-sync.sh` run (generates CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules)
- [ ] `layer_N_orchestrator.gab.jsonld` created
- [ ] `layer_N_orchestrator.integration.md` generated via `jsonld-to-md.sh`

### Config Directories (Entity Root)
- [ ] `.0agnostic/` with all 7 subdirs (agents, episodic_memory/{sessions,changes}, hooks/scripts, knowledge, rules, skills)
- [ ] `.1merge/` with 6 tools × 3 tiers = 18 subdirectories
- [ ] `.claude/` with `rules/` AND `episodic_memory/{sessions,changes}/`
- [ ] `.cursor/` with `rules/` AND `episodic_memory/{sessions,changes}/`
- [ ] `.gemini/` with `episodic_memory/{sessions,changes}/`
- [ ] `.codex/` with `episodic_memory/{sessions,changes}/`
- [ ] `.github/instructions/`

### Internal Structure
- [ ] `layer_N_group/` with `_group` suffix (NOT bare `layer_N/`)
- [ ] All internal dirs (00-03, sub-layers) created
- [ ] `0AGNOSTIC.md` in every internal directory
- [ ] `agnostic-sync.sh` run on every internal `0AGNOSTIC.md`

### Stages
- [ ] ALL 12 stages created (00-11)
- [ ] Each stage has config dirs (.0agnostic, .1merge, .claude, .cursor, .gemini, .codex, .github)
- [ ] Each stage has `outputs/` and `synthesis/` directories
- [ ] Each stage has `0AGNOSTIC.md` + auto-generated tool files
- [ ] Each stage has `stage_N_XX_name_agent.jsonld` + matching `.integration.md`
- [ ] `layer_N_99_stages_orchestrator.gab.jsonld` + matching `.integration.md`
- [ ] `status_N.json` created

### Parent Updates
- [ ] Parent's `0INDEX.md` updated to include new entity
- [ ] Parent's registry updated (if applicable)

### Validation
- [ ] `tools/validate-entity.sh <entity-path>` passes all checks

---

*See `@imports/entity_structure.md` for the canonical directory structure.*
*See MAINTENANCE_GUIDE.md for ongoing entity management.*
