---
resource_id: "4f9ca7d8-58f4-423e-9348-1266183cf38f"
resource_type: "skill_document"
resource_name: "SKILL"
---
# Entity Creation Skill (Research Context)

<!-- section_id: "f416c3c1-18fd-4f54-89e7-ec0535f4a6ac" -->
## Purpose

Ensure correct naming conventions and canonical structure when creating layer-stage entities within research projects.

<!-- section_id: "0dece152-4da0-43a9-87d8-aa9a71fb1c22" -->
## When to Use

This skill is triggered when:
- Creating a new feature, sub_feature, component, or subproject directory
- Creating a new entity within the research hierarchy

<!-- section_id: "a000b035-cd5e-41d7-b4e6-ff01c47e6ada" -->
## Canonical Structure

Read the root canonical entrypoint first:
`/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`

Project-local files with the same name may exist as compatibility bridges, but the root `0_layer_universal` path is authoritative.

<!-- section_id: "7169b95f-abf0-486d-8fcb-352fe80976df" -->
## Naming Pattern

```
layer_{N}_{type}_{name}
```

Where:
- `{N}` = layer number (0, 1, 2, -1, etc.)
- `{type}` = entity type (feature, sub_feature, component, subproject)
- `{name}` = descriptive name with underscores

<!-- section_id: "c157dcd9-03d0-4730-abae-6c36717c7aa5" -->
## Entity Types

| Type | Pattern | Example |
|------|---------|---------|
| feature | `layer_N_feature_{name}` | `layer_0_feature_context_framework` |
| sub_feature | `layer_N_sub_feature_{name}` | `layer_1_sub_feature_context_system` |
| component | `layer_N_component_{name}` | `layer_2_component_link_validator` |
| subproject | `layer_N_subproject_{name}` | `layer_1_subproject_prototype` |

**Note**: `sub_feature` uses underscore (like `sub_layer`). Other types are single words.

<!-- section_id: "b7b23087-8a54-4538-b4e4-e45417a89931" -->
## Layer Hierarchy

Children are always layer N+1 of their parent:

```
layer_0_group/
  └── layer_0_feature_*/           (layer 0)
        └── layer_1_sub_feature_*/ (layer 1)
              └── layer_2_component_*/ (layer 2)
```

<!-- section_id: "48b3f0ff-ec6c-424f-ae2b-1836de9895e9" -->
## Before Creating an Entity

1. **Read `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`** for canonical directory structure and current source-doc links
2. **Read parent's index.jsonld** (if it exists)
   - Find `conventions.childNaming`
   - Note `currentLayer` and `childLayer`
3. **Determine correct name**: parent layer + 1 = child layer
4. **Create full canonical structure** using the scaffold in the root canonical `entity_structure.md`
5. **Create `0AGNOSTIC.md` and `0INDEX.md`** (see INSTANTIATION_GUIDE.md for templates)
6. **Run `agnostic-sync.sh`** to generate tool files

<!-- section_id: "88cf837a-f0d0-48cd-acec-2555f867c65e" -->
## Checklist

Before creating any entity:

- [ ] Read root canonical `entity_structure.md`
- [ ] Calculate child layer: parent layer + 1
- [ ] Use `sub_feature` (not `subfeature`) for sub-features
- [ ] Include layer prefix: `layer_{N}_`
- [ ] Full canonical directory structure created
- [ ] `0AGNOSTIC.md` and `0INDEX.md` created
- [ ] Parent updated

<!-- section_id: "2aee8367-cc5b-412c-abac-acd605bafcbb" -->
## Common Mistakes

| Wrong | Right | Issue |
|-------|-------|-------|
| `subfeature_*` | `layer_1_sub_feature_*` | Missing layer prefix, missing underscore |
| `layer_1_subfeature_*` | `layer_1_sub_feature_*` | Missing underscore in sub_feature |
| `feature_*` | `layer_0_feature_*` | Missing layer prefix |
| `layer_0_sub_feature_*` in layer 0 feature | `layer_1_sub_feature_*` | Wrong layer (children are +1) |
| `entity_99_stages/` | `layer_N_group/layer_N_99_stages/` | Stages go inside layer_N_group |
| Missing `.1merge/` | Include `.1merge/` | All entities need tool-specific overrides dir |

<!-- section_id: "1ecb92cd-7782-42a8-bd15-2336b12cd557" -->
## Key References

- Canonical structure entrypoint: `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
- Instantiation guide: `layer_1_group/layer_1_01_features/layer_1_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_organization/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_entities/.0agnostic/01_knowledge/overview/production_entity_lifecycle/INSTANTIATION_GUIDE.md`
- Entity types: `layer_1_group/layer_1_01_features/layer_1_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_organization/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_entities/.0agnostic/01_knowledge/overview/production_entity_lifecycle/ENTITY_TYPES.md`
- Maintenance guide: `layer_1_group/layer_1_01_features/layer_1_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_organization/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_entities/.0agnostic/01_knowledge/overview/production_entity_lifecycle/MAINTENANCE_GUIDE.md`

---

*This skill uses the root-level `0_layer_universal/.0agnostic/.../entity_structure.md` file as the stable entrypoint for canonical entity structure*
