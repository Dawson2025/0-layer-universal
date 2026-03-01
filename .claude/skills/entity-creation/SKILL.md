---
name: entity-creation
description: "Create new layers, sub-layers, stages, features, projects, or components with proper structure. Use when the user needs a new project, feature, or structural entity in the layer-stage system. Enforces the Stage Completeness Rule (all 12 stages) and canonical entity structure."
---

# Entity Creation Skill

## WHEN to Use
- Creating a new project (`layer_1_project_*`)
- Creating a new feature (`layer_2_feature_*`)
- Creating a new component (`layer_3_component_*`)
- Creating a new research project (`layer_-1_*`)
- Creating stages for an entity
- When the user says "create a new project/feature/component"

## WHEN NOT to Use
- Modifying an existing entity (use normal file editing)
- Creating individual files within an existing entity
- Renaming or reorganizing existing structure

## References (MUST READ BEFORE EXECUTING)

| Reference | Path | Why |
|-----------|------|-----|
| **Canonical structure** | `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` | **Full directory tree, stage structure, naming conventions, mkdir templates** |
| Instantiation guide | `layer_0/.../entity_lifecycle/INSTANTIATION_GUIDE.md` | Templates for 0AGNOSTIC.md, 0INDEX.md |
| Entity types | `layer_0/.../entity_lifecycle/ENTITY_TYPES.md` | Type-specific details |
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | **Stage Completeness Rule** |
| Layers | `layer_0/.../layer_stage_system/LAYERS_EXPLAINED.md` | Layer structure |
| Sub-layers | `layer_0/.../layer_stage_system/SUB_LAYERS_EXPLAINED.md` | Sub-layer types |
| Nested depth | `layer_0/.../layer_stage_system/NESTED_DEPTH_NAMING.md` | subxN naming |
| Renumbering | `.0agnostic/01_knowledge/layer_stage_system/docs/RENUMBERING_GUIDE.md` | Layer number shifting |
| Renumber tool | `.0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh` | Shift layer_N references |

**Full paths**:
- `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/` = `0_layer_universal/.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/`
- `layer_stage_system/` = `.0agnostic/01_knowledge/layer_stage_system/`
- `entity_lifecycle/` = `.0agnostic/01_knowledge/entity_lifecycle/`

## Protocol

### Step 1: Determine Entity Type and Layer

| Creating a... | Location | Layer N |
|---------------|----------|---------|
| Project | `layer_1/layer_1_projects/` | 1 |
| Feature | `<project>/layer_2_group/layer_2_features/` | 2 |
| Component | `<feature>/layer_3_group/layer_3_components/` | 3 |
| Research project | `layer_-1_research/` | -1 |
| Research feature | `<research>/layer_0_group/layer_0_features/` | 0 |

### Step 2: Create Full Directory Structure

**⚠️ CRITICAL**: All directory structure details, mkdir templates, and configuration come from the CANONICAL SOURCE:

**[Read this FIRST](../../0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md)**

That document provides:
- Complete directory tree with all subdirectories
- Full mkdir template with nested paths
- Stage structure details
- Naming conventions
- File requirements

Use those templates exactly.

### Step 3: [CRITICAL] Create ALL 12 Stages (00-11)

**Stage Completeness Rule**: Create ALL 12 stages. **Empty stages are valid. Missing stages are NOT.**

Refer to `entity_structure.md` (link above) for the stage creation bash commands and directory structure.

### Step 4-10: Complete Setup Steps

**All remaining detailed steps** (config directories, required files, orchestrators, integration files, agnostic-sync, validation) are in the **CANONICAL SOURCE**:

**[See entity_structure.md section "Required Files"](../../0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md#required-files)**

Quick summary:
1. Create `0AGNOSTIC.md` (templates in INSTANTIATION_GUIDE.md), `0INDEX.md`, `README.md`
2. Create orchestrator and agent .jsonld files (copy from sibling entity)
3. Generate `.integration.md` for each `.jsonld` file
4. Run `agnostic-sync.sh` on ALL `0AGNOSTIC.md` files
5. Run `validate-entity.sh` to verify

## Naming Conventions

| Convention | Rule | Example |
|---|---|---|
| Entity naming | `layer_{N}_{type}_{name}` | `layer_2_feature_assignments` |
| Internal dir | **MUST** use `_group` suffix | `layer_7_group/` (NOT `layer_7/`) |
| Children dir | **MUST** use `_group` suffix | `layer_8_group/` (NOT `layer_8/`) |
| Episodic memory | **MUST** be `episodic_memory` | NOT `episodic/` |
| Agent files | Dot-separation | `name.gab.jsonld` (NOT `name_gab.jsonld`) |

Children are always layer N+1 of their parent.

## Completion Checklist

**For detailed checklist with complete directory structure**, see:
**[entity_structure.md → Post-Instantiation Checklist](../../0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md#post-instantiation-checklist)**

**Quick validation**:
- [ ] ALL 12 stages created (00-11)
- [ ] `0AGNOSTIC.md`, `0INDEX.md`, `README.md` exist at entity root
- [ ] `agnostic-sync.sh` run on all 0AGNOSTIC.md files
- [ ] `validate-entity.sh <entity-path>` passes all checks

## AALang Reference

Entity creation follows the GAB format defined in:
`layer_0/layer_0_01_ai_manager_system/professor/gab-formats.jsonld`

---

*This skill enforces both the Stage Completeness Rule and the canonical entity structure from `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`*
