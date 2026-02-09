---
name: entity-creation
description: "Create new layers, sub-layers, stages, features, projects, or components with proper structure. Use when the user needs a new project, feature, or structural entity in the layer-stage system. Enforces the Stage Completeness Rule (all 11 stages) and canonical entity structure."
---

# Entity Creation Skill

## WHEN to Use
- Creating a new project (`layer_1_project_*`)
- Creating a new feature (`layer_2_feature_*`)
- Creating a new component (`layer_3_component_*`)
- Creating a new research project (`layer_-1_*`)
- Creating stages for an entity
- Creating sub-layers for an entity
- When the user says "create a new project/feature/component"

## WHEN NOT to Use
- Modifying an existing entity (use normal file editing)
- Creating individual files within an existing entity
- Renaming or reorganizing existing structure

## References (MUST READ BEFORE EXECUTING)

| Reference | Path | Why |
|-----------|------|-----|
| **Canonical structure** | `@imports/entity_structure.md` | **Full directory tree and mkdir template** |
| Instantiation guide | `layer_0/.../entity_lifecycle/INSTANTIATION_GUIDE.md` | Templates for 0AGNOSTIC.md, 0INDEX.md |
| Entity types | `layer_0/.../entity_lifecycle/ENTITY_TYPES.md` | Type-specific details |
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | **Stage Completeness Rule** |
| Layers | `layer_0/.../layer_stage_system/LAYERS_EXPLAINED.md` | Layer structure |
| Sub-layers | `layer_0/.../layer_stage_system/SUB_LAYERS_EXPLAINED.md` | Sub-layer types |
| Nested depth | `layer_0/.../layer_stage_system/NESTED_DEPTH_NAMING.md` | subxN naming |

**Full paths**:
- `@imports/` = `0_layer_universal/@imports/`
- `layer_stage_system/` = `layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/layer_stage_system/`
- `entity_lifecycle/` = `layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/entity_lifecycle/`

## Protocol

### 1. Determine Entity Type and Layer

| Creating a... | Location | Layer N |
|---------------|----------|---------|
| Project | `layer_1/layer_1_projects/` | 1 |
| Feature | `<project>/layer_2_group/layer_2_features/` | 2 |
| Component | `<feature>/layer_3_group/layer_3_components/` | 3 |
| Research project | `layer_-1_research/` | -1 |
| Research feature | `<research>/layer_0_group/layer_0_features/` | 0 |

### 2. Create Full Canonical Structure

Read `@imports/entity_structure.md` for the complete directory tree. Every entity needs:

- `0AGNOSTIC.md`, `0INDEX.md` (manually created)
- `.0agnostic/` with agents, episodic, hooks/scripts, knowledge, rules, skills
- `.1merge/` with 6 tools x 3 tiers each
- `.claude/rules/`, `.cursor/rules/`, `.github/instructions/`
- `layer_N_group/` with:
  - `layer_N_00_layer_registry/proposals/`
  - `layer_N_01_ai_manager_system/`
  - `layer_N_02_manager_handoff_documents/{incoming/{from_above,from_below},outgoing/{to_above,to_below}}`
  - `layer_N_03_sub_layers/` (with sub_layer_N_00 through 05+, knowledge_system has overview/ and things_learned/)
  - `layer_N_99_stages/` (at minimum stage_N_02_research/outputs/by_topic/)
- `layer_N+1_group/` (if entity has children)
- `synthesis/`

Use the mkdir template from `@imports/entity_structure.md`.

### 3. [CRITICAL] Create ALL 11 Stages

**Stage Completeness Rule**: If the entity has stages, create ALL 11.

```bash
for i in 01_request_gathering 02_research 03_instructions 04_planning 05_design 06_development 07_testing 08_criticism 09_fixing 10_current_product 11_archives; do
  mkdir -p "layer_N_group/layer_N_99_stages/stage_N_$i/outputs/{by_topic,episodic/{sessions,changes}}"
done
```

**Empty stages are valid. Missing stages are NOT.**

### 4. Create Required Files

- `0AGNOSTIC.md` — See INSTANTIATION_GUIDE.md for template
- `0INDEX.md` — See INSTANTIATION_GUIDE.md for template
- Run `agnostic-sync.sh` to generate CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md

**agnostic-sync.sh location**: `layer_0/.0agnostic/agnostic-sync.sh`

### 5. Update Parent

- Update parent's `0INDEX.md` to include new entity
- Update parent's registry if applicable

## Naming Convention

```
layer_{N}_{type}_{name}
```

| Type | Pattern | Example |
|------|---------|---------|
| feature | `layer_N_feature_{name}` | `layer_0_feature_context_framework` |
| sub_feature | `layer_N_sub_feature_{name}` | `layer_1_sub_feature_context_system` |
| component | `layer_N_component_{name}` | `layer_2_component_link_validator` |
| project | `layer_1_project_{name}` | `layer_1_project_school` |

Children are always layer N+1 of their parent.

## Checklist

Before completing:
- [ ] Read `@imports/entity_structure.md` for canonical structure
- [ ] Full directory structure created (all dirs from canonical tree)
- [ ] All 11 stages created (if entity has stages)
- [ ] `0AGNOSTIC.md` created with correct identity
- [ ] `0INDEX.md` created for navigation
- [ ] `agnostic-sync.sh` run to generate tool files
- [ ] Parent's 0INDEX.md updated
- [ ] Parent's registry updated (if applicable)

## AALang Reference

Entity creation follows the GAB format defined in:
`layer_0/layer_0_01_ai_manager_system/professor/gab-formats.jsonld`

---

*This skill enforces both the Stage Completeness Rule and the canonical entity structure from `@imports/entity_structure.md`*
