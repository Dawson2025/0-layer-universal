---
resource_id: "407f8d5b-8015-4020-9595-28856ce8d2de"
resource_type: "skill_document"
resource_name: "SKILL"
---
# Skill: Entity Creation

<!-- section_id: "d8c77b00-4e10-414f-a6b8-dda3a024f2de" -->
## Purpose

Create new layers, sub-layers, stages, features, projects, or components with proper structure.

<!-- section_id: "393b0554-f98c-4cd5-a0d6-a65d79192d29" -->
## When to Use

- Creating a new project, feature, component, or research project
- Creating stages for an entity
- When the user says "create a new project/feature/component"

<!-- section_id: "98a127d5-81fa-49aa-a665-6b09678eba91" -->
## References (MUST READ BEFORE EXECUTING)

| Reference | Path | Why |
|-----------|------|-----|
| **Canonical structure** | `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` | **Full directory tree and mkdir template** |
| Instantiation guide | `layer_0/.../entity_lifecycle/INSTANTIATION_GUIDE.md` | Templates for 0AGNOSTIC.md, 0INDEX.md |
| Entity types | `layer_0/.../entity_lifecycle/ENTITY_TYPES.md` | Type-specific details |
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | **Stage Completeness Rule** |
| Layers | `layer_0/.../layer_stage_system/LAYERS_EXPLAINED.md` | Layer structure |

<!-- section_id: "d23527be-aafe-40c1-b2ee-568d9b965c33" -->
## Protocol

<!-- section_id: "0784dba0-f952-49a6-a649-a09d0a00f24c" -->
### 1. Determine Entity Type and Layer

| Creating a... | Location | Layer N |
|---------------|----------|---------|
| Project | `layer_1/layer_1_projects/` | 1 |
| Feature | `<project>/layer_2_group/layer_2_features/` | 2 |
| Component | `<feature>/layer_3_group/layer_3_components/` | 3 |
| Research project | `layer_-1_research/` | -1 |
| Research feature | `<research>/layer_0_group/layer_0_features/` | 0 |

<!-- section_id: "fb6bfdbb-4555-4514-95c8-69a155341786" -->
### 2. Create Full Canonical Structure

Read `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` for the complete directory tree and mkdir template. Every entity needs:
- `.0agnostic/`, `.1merge/`, `.claude/`, `.cursor/`, `.github/`
- `layer_N_group/` (registry, manager system, handoff docs, sub-layers, stages)
- `layer_N+1_group/` (if entity has children)
- `synthesis/`

<!-- section_id: "734e8b66-1655-46e9-a47b-8389e620121d" -->
### 3. [CRITICAL] Create ALL 11 Stages

**Stage Completeness Rule**: If the entity has stages, create ALL 11. Empty stages are valid. Missing stages are NOT.

<!-- section_id: "a6681b94-3342-4ea4-aa26-64b18409f4df" -->
### 4. Assign UUIDs

Every new entity gets stable UUID identity at creation time:

1. **Entity UUID**: Generate and add `entity_id` to `0AGNOSTIC.md` `## Identity` section:
   ```bash
   ENTITY_UUID=$(uuidgen | tr '[:upper:]' '[:lower:]')
   # Add to 0AGNOSTIC.md: entity_id: "$ENTITY_UUID"
   ```

2. **Stage UUIDs**: Generate a UUID for each of the 12 stages and create `stage_index.json`:
   ```bash
   # In layer_N_group/layer_N_00_layer_registry/stage_index.json
   echo '{"entity": "<entity_name>", "stages": {' > stage_index.json
   first=true
   for stage_dir in layer_N_group/layer_N_99_stages/stage_N_*/; do
     stage_name=$(basename "$stage_dir")
     stage_uuid=$(uuidgen | tr '[:upper:]' '[:lower:]')
     [ "$first" = true ] && first=false || echo ',' >> stage_index.json
     printf '  "%s": "%s"' "$stage_name" "$stage_uuid" >> stage_index.json
   done
   echo -e '\n}}' >> stage_index.json
   ```

3. **Rebuild global index**: After entity creation, run:
   ```bash
   .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --rebuild-index
   ```

<!-- section_id: "6a8b7c9d-0e1f-4a2b-3c4d-5e6f7a8b9c0d" -->
### 5. Create Required Files

- `0AGNOSTIC.md` with `entity_id` in `## Identity` (see INSTANTIATION_GUIDE.md for templates)
- `0INDEX.md`
- Run `.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh` to generate tool files

<!-- section_id: "12f95bd8-c4b3-42bc-a62c-5b6ebb82f19d" -->
### 6. Update Parent

- Update parent's `0INDEX.md` and registry

<!-- section_id: "b8e3e187-26c2-4320-967e-d33b66aed00f" -->
## Naming Convention

```
layer_{N}_{type}_{name}
```

Children are always layer N+1 of their parent. Use `sub_feature` (not `subfeature`).

<!-- section_id: "b9a717a4-2442-4783-9abd-aac04e57514f" -->
## Checklist

Before completing:
- [ ] Read `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
- [ ] Full canonical directory structure created
- [ ] All 11 stages created (if entity has stages)
- [ ] `entity_id` UUID generated and added to `0AGNOSTIC.md` `## Identity`
- [ ] `stage_index.json` created with UUIDs for all stages
- [ ] `0AGNOSTIC.md` and `0INDEX.md` created
- [ ] `agnostic-sync.sh` run
- [ ] `pointer-sync.sh --rebuild-index` run
- [ ] Parent updated

---

*This skill enforces the Stage Completeness Rule and canonical entity structure from `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`*
