# Entity Creation Skill

## Purpose

Ensure correct naming conventions when creating layer-stage entities (features, sub_features, components, subprojects).

## When to Use

This skill is triggered by `trigger:onEntityCreation` in index.jsonld files when:
- Creating a new feature, sub_feature, component, or subproject directory
- Creating a new index.jsonld for an entity

## Naming Pattern

```
layer_{N}_{type}_{name}
```

Where:
- `{N}` = layer number (0, 1, 2, -1, etc.)
- `{type}` = entity type (see below)
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

1. **Read parent's index.jsonld**
   - Find `conventions.childNaming`
   - Note `currentLayer` and `childLayer`
   - Check the `example` field

2. **Determine correct name**
   ```
   Parent layer: 0
   Child layer: 0 + 1 = 1
   Type: sub_feature
   Name: navigation_system

   Result: layer_1_sub_feature_navigation_system
   ```

3. **Validate before creating**
   - Name must match pattern: `^layer_\d+_(feature|sub_feature|component|subproject)_.+$`
   - Layer number must equal parent layer + 1 (for children)

## Checklist

Before creating any entity:

- [ ] Read parent's index.jsonld
- [ ] Check `conventions.childNaming.pattern`
- [ ] Check `conventions.childNaming.example`
- [ ] Calculate child layer: parent layer + 1
- [ ] Use `sub_feature` (not `subfeature`) for sub-features
- [ ] Include layer prefix: `layer_{N}_`
- [ ] Create with correct naming

## Common Mistakes

| Wrong | Right | Issue |
|-------|-------|-------|
| `subfeature_*` | `layer_1_sub_feature_*` | Missing layer prefix, missing underscore |
| `layer_1_subfeature_*` | `layer_1_sub_feature_*` | Missing underscore in sub_feature |
| `feature_*` | `layer_0_feature_*` | Missing layer prefix |
| `layer_0_sub_feature_*` in layer 0 feature | `layer_1_sub_feature_*` | Wrong layer (children are +1) |

## After Creating an Entity

1. Create `index.jsonld` in new directory with:
   - `@id`: the entity name
   - `layer`: the layer number
   - `conventions.childNaming`: for its own children

2. Update parent's `children` array if needed

## Example: Creating a Sub-Feature

```bash
# 1. Read parent
cat layer_0_feature_context_framework/index.jsonld
# Shows: layer: 0, childLayer: 1, example: layer_1_sub_feature_context_system

# 2. Create with correct name
mkdir layer_0_feature_context_framework/layer_1_sub_feature_new_system

# 3. Create index.jsonld
cat > layer_0_feature_context_framework/layer_1_sub_feature_new_system/index.jsonld << 'EOF'
{
  "@id": "layer_1_sub_feature_new_system",
  "layer": 1,
  "conventions": {
    "childNaming": {
      "pattern": "layer_{N+1}_{type}_{name}",
      "currentLayer": 1,
      "childLayer": 2,
      "example": "layer_2_component_new_component"
    }
  }
}
EOF
```
