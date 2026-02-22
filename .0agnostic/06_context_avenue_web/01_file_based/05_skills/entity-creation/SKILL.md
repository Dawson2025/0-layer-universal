# Skill: Entity Creation

## Purpose

Create new layers, sub-layers, stages, features, projects, or components with proper structure.

## When to Use

- Creating a new project, feature, component, or research project
- Creating stages for an entity
- When the user says "create a new project/feature/component"

## References (MUST READ BEFORE EXECUTING)

| Reference | Path | Why |
|-----------|------|-----|
| **Canonical structure** | `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` | **Full directory tree and mkdir template** |
| Instantiation guide | `layer_0/.../entity_lifecycle/INSTANTIATION_GUIDE.md` | Templates for 0AGNOSTIC.md, 0INDEX.md |
| Entity types | `layer_0/.../entity_lifecycle/ENTITY_TYPES.md` | Type-specific details |
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | **Stage Completeness Rule** |
| Layers | `layer_0/.../layer_stage_system/LAYERS_EXPLAINED.md` | Layer structure |

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

Read `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` for the complete directory tree and mkdir template. Every entity needs:
- `.0agnostic/`, `.1merge/`, `.claude/`, `.cursor/`, `.github/`
- `layer_N_group/` (registry, manager system, handoff docs, sub-layers, stages)
- `layer_N+1_group/` (if entity has children)
- `synthesis/`

### 3. [CRITICAL] Create ALL 11 Stages

**Stage Completeness Rule**: If the entity has stages, create ALL 11. Empty stages are valid. Missing stages are NOT.

### 4. Create Required Files

- `0AGNOSTIC.md` and `0INDEX.md` (see INSTANTIATION_GUIDE.md for templates)
- Run `agnostic-sync.sh` to generate tool files

### 5. Update Parent

- Update parent's `0INDEX.md` and registry

## Naming Convention

```
layer_{N}_{type}_{name}
```

Children are always layer N+1 of their parent. Use `sub_feature` (not `subfeature`).

## Checklist

Before completing:
- [ ] Read `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
- [ ] Full canonical directory structure created
- [ ] All 11 stages created (if entity has stages)
- [ ] `0AGNOSTIC.md` and `0INDEX.md` created
- [ ] `agnostic-sync.sh` run
- [ ] Parent updated

---

*This skill enforces the Stage Completeness Rule and canonical entity structure from `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`*
