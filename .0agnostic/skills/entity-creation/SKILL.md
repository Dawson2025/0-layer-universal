# Skill: Entity Creation

## Purpose

Create new layers, sub-layers, stages, features, projects, or components with proper structure.

## When to Use

- Creating a new project
- Creating a new feature
- Creating a new component
- Creating stages for an entity

## References (MUST READ BEFORE EXECUTING)

Load these knowledge docs before creating entities:

| Reference | Path | Why |
|-----------|------|-----|
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | **Stage Completeness Rule** |
| Layers | `layer_0/.../layer_stage_system/LAYERS_EXPLAINED.md` | Layer structure |
| Sub-layers | `layer_0/.../layer_stage_system/SUB_LAYERS_EXPLAINED.md` | Sub-layer types |
| Nested depth | `layer_0/.../layer_stage_system/NESTED_DEPTH_NAMING.md` | subxN naming |

**Full path**: `layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/layer_stage_system/`

## Protocol

### 1. Determine Entity Type

| Type | Parent | Naming |
|------|--------|--------|
| Project | layer_1/ | `layer_1_project_<name>/` |
| Feature | project's layer_2_group/ | `layer_2_feature_<name>/` |
| Component | feature's layer_3_group/ | `layer_3_component_<name>/` |
| Sub-layer | parent's sub_layers/ | `sub_layer_N_XX_<name>/` |

### 2. Create Required Structure

Every entity needs:
```
entity/
├── CLAUDE.md              ← Agent entry point
├── 0INDEX.md              ← Navigation index
└── entity_99_stages/      ← If using stages (see step 3)
```

### 3. [CRITICAL] Create ALL 11 Stages

**Stage Completeness Rule**: If the entity has stages, create ALL 11.

```bash
# Required stage structure
mkdir -p entity_99_stages/stage_X_{01_request_gathering,02_research,03_instructions,04_planning,05_design,06_development,07_testing,08_criticism,09_fixing,10_current_product,11_archives}/outputs
```

**Empty stages are valid. Missing stages are NOT.**

### 4. Create Sub-layers (if needed)

```
entity_03_sub_layers/
├── sub_layer_X_01_prompts/
├── sub_layer_X_02_knowledge_system/
├── sub_layer_X_03_principles/
├── sub_layer_X_04_rules/
└── sub_layer_X_05+_setup_dependant/
```

### 5. Update Parent's Registry

Add the new entity to parent's registry or index.

## Checklist

Before completing:
- [ ] All 11 stages created (if entity has stages)
- [ ] Each stage has outputs/ folder
- [ ] CLAUDE.md created with proper identity
- [ ] 0INDEX.md created for navigation
- [ ] Parent registry updated

---

*This skill enforces the Stage Completeness Rule from STAGES_EXPLAINED.md*
