# Entity Creation Skill (Research Context)

## Purpose

Ensure correct naming conventions and canonical structure when creating layer-stage entities within research projects.

## When to Use

This skill is triggered when:
- Creating a new feature, sub_feature, component, or subproject directory
- Creating a new entity within the research hierarchy

## Canonical Structure

Read `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` for the complete directory tree every entity needs. This is the single source of truth for entity structure.

## Naming Pattern

```
layer_{N}_{type}_{name}
```

Where:
- `{N}` = layer number (0, 1, 2, -1, etc.)
- `{type}` = entity type (feature, sub_feature, component, subproject)
- `{name}` = descriptive name with underscores

## Entity Types

| Type | Pattern | Example |
|------|---------|---------|
| feature | `layer_N_feature_{name}` | `layer_0_feature_context_framework` |
| sub_feature | `layer_N_sub_feature_{name}` | `layer_1_sub_feature_context_system` |
| component | `layer_N_component_{name}` | `layer_2_component_link_validator` |
| subproject | `layer_N_subproject_{name}` | `layer_1_subproject_prototype` |

**Note**: `sub_feature` uses underscore (like `sub_layer`). Other types are single words.

## Layer Hierarchy

Children are always layer N+1 of their parent:

```
layer_0_group/
  └── layer_0_feature_*/           (layer 0)
        └── layer_1_sub_feature_*/ (layer 1)
              └── layer_2_component_*/ (layer 2)
```

## Before Creating an Entity

1. **Read `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`** for canonical directory structure
2. **Read parent's index.jsonld** (if it exists)
   - Find `conventions.childNaming`
   - Note `currentLayer` and `childLayer`
3. **Determine correct name**: parent layer + 1 = child layer
4. **Create full canonical structure** using mkdir template from `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
5. **Create `0AGNOSTIC.md` and `0INDEX.md`** (see INSTANTIATION_GUIDE.md for templates)
6. **Run `agnostic-sync.sh`** to generate tool files

## Checklist

Before creating any entity:

- [ ] Read `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
- [ ] Calculate child layer: parent layer + 1
- [ ] Use `sub_feature` (not `subfeature`) for sub-features
- [ ] Include layer prefix: `layer_{N}_`
- [ ] Full canonical directory structure created
- [ ] `0AGNOSTIC.md` and `0INDEX.md` created
- [ ] Parent updated

## Common Mistakes

| Wrong | Right | Issue |
|-------|-------|-------|
| `subfeature_*` | `layer_1_sub_feature_*` | Missing layer prefix, missing underscore |
| `layer_1_subfeature_*` | `layer_1_sub_feature_*` | Missing underscore in sub_feature |
| `feature_*` | `layer_0_feature_*` | Missing layer prefix |
| `layer_0_sub_feature_*` in layer 0 feature | `layer_1_sub_feature_*` | Wrong layer (children are +1) |
| `entity_99_stages/` | `layer_N_group/layer_N_99_stages/` | Stages go inside layer_N_group |
| Missing `.1merge/` | Include `.1merge/` | All entities need tool-specific overrides dir |

## Key References

- Canonical structure: `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
- Instantiation guide: `layer_0/.../entity_lifecycle/INSTANTIATION_GUIDE.md`
- Entity types: `layer_0/.../entity_lifecycle/ENTITY_TYPES.md`

---

*This skill enforces naming conventions and canonical entity structure from `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`*
