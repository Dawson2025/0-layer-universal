---
resource_id: "fdced653-28aa-4611-ae13-52e3d3ef3be6"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: entity-creation
description: "Create new layers, sub-layers, stages, features, projects, or components with proper structure. Use when the user needs a new project, feature, or structural entity in the layer-stage system. Enforces the Stage Completeness Rule (all 12 stages) and canonical entity structure."
---

# Entity Creation Skill

<!-- section_id: "ca243c1c-285d-4777-8cbb-093ef2aae574" -->
## WHEN to Use
- Creating a new project (`layer_1_project_*`)
- Creating a new feature (`layer_2_feature_*`)
- Creating a new component (`layer_3_component_*`)
- Creating a new research project (`layer_-1_*`)
- Creating stages for an entity
- When the user says "create a new project/feature/component"

<!-- section_id: "fb1dec78-c2cd-4ec9-b4eb-66f8f6ec6d6f" -->
## WHEN NOT to Use
- Modifying an existing entity (use normal file editing)
- Creating individual files within an existing entity
- Renaming or reorganizing existing structure

<!-- section_id: "3b107c43-9b29-4c2c-9b26-7e36142d8094" -->
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

<!-- section_id: "670155cc-6f44-4499-a335-1614aa22f527" -->
## Protocol

<!-- section_id: "0cd6a988-0609-46bd-b0e3-9124e2cebed4" -->
### Step 1: Determine Entity Type and Layer

| Creating a... | Location | Layer N |
|---------------|----------|---------|
| Project | `layer_1/layer_1_projects/` | 1 |
| Feature | `<project>/layer_2_group/layer_2_features/` | 2 |
| Component | `<feature>/layer_3_group/layer_3_components/` | 3 |
| Research project | `layer_-1_research/` | -1 |
| Research feature | `<research>/layer_0_group/layer_0_features/` | 0 |

<!-- section_id: "7f18dbf5-1c39-4b18-8f3b-bd7b7bdbbbb8" -->
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

<!-- section_id: "095a9704-ae4a-4454-b5a5-f5b959516507" -->
### Step 3: [CRITICAL] Create ALL 12 Stages (00-11)

**Stage Completeness Rule**: Create ALL 12 stages. **Empty stages are valid. Missing stages are NOT.**

Refer to `entity_structure.md` (link above) for the stage creation bash commands and directory structure.

<!-- section_id: "5b2d63c7-5a15-4f03-a740-5b9a72fc4f45" -->
### Step 4-10: Complete Setup Steps

**All remaining detailed steps** (config directories, required files, orchestrators, integration files, agnostic-sync, validation) are in the **CANONICAL SOURCE**:

**[See entity_structure.md section "Required Files"](../../0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md#required-files)**

Quick summary:
1. Create `0AGNOSTIC.md` (templates in INSTANTIATION_GUIDE.md), `0INDEX.md`, `README.md`
2. **Generate entity_id UUID** in `0AGNOSTIC.md` `## Identity` section: `entity_id: "$(uuidgen | tr '[:upper:]' '[:lower:]')"`
3. **Generate stage_index.json** with UUIDs for all 12 stages in `layer_N_group/layer_N_00_layer_registry/stage_index.json` (see entity_structure.md Stage Creation Template)
4. Create orchestrator and agent .jsonld files (copy from sibling entity)
5. Generate `.integration.md` for each `.jsonld` file
6. Run `agnostic-sync.sh` on ALL `0AGNOSTIC.md` files
7. Run `.0agnostic/pointer-sync.sh --rebuild-index` to register the new entity in the global UUID index
8. Run `validate-entity.sh` to verify

<!-- section_id: "ca201922-5542-4c37-b715-fb060e6a81d1" -->
## Naming Conventions

| Convention | Rule | Example |
|---|---|---|
| Entity naming | `layer_{N}_{type}_{name}` | `layer_2_feature_assignments` |
| Internal dir | **MUST** use `_group` suffix | `layer_7_group/` (NOT `layer_7/`) |
| Children dir | **MUST** use `_group` suffix | `layer_8_group/` (NOT `layer_8/`) |
| Episodic memory | **MUST** be `episodic_memory` | NOT `episodic/` |
| Agent files | Dot-separation | `name.gab.jsonld` (NOT `name_gab.jsonld`) |

Children are always layer N+1 of their parent.

<!-- section_id: "e6ad045b-3fb9-4f7e-b72b-a5b83c3b1b85" -->
## Completion Checklist

**For detailed checklist with complete directory structure**, see:
**[entity_structure.md → Post-Instantiation Checklist](../../0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md#post-instantiation-checklist)**

**Quick validation**:
- [ ] ALL 12 stages created (00-11)
- [ ] `0AGNOSTIC.md`, `0INDEX.md`, `README.md` exist at entity root
- [ ] `entity_id: "uuid"` present in `0AGNOSTIC.md` `## Identity` section
- [ ] `stage_index.json` created with UUIDs for all 12 stages
- [ ] `pointer-sync.sh --rebuild-index` run (registers entity in global UUID index)
- [ ] `agnostic-sync.sh` run on all 0AGNOSTIC.md files
- [ ] `validate-entity.sh <entity-path>` passes all checks

<!-- section_id: "6f2109a5-09db-4176-aeca-73cb92e67651" -->
## AALang Reference

Entity creation follows the GAB format defined in:
`layer_0/layer_0_01_ai_manager_system/professor/gab-formats.jsonld`

---

*This skill enforces both the Stage Completeness Rule and the canonical entity structure from `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`*
