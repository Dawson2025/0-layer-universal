---
resource_id: "be54f1dc-bfcf-4b9f-8685-d6a536cca3bf"
resource_type: "document"
resource_name: "layer_numbering"
---
# Layer Numbering

## Rules
1. Layer 0 is always the universal root
2. Layer N entities use `layer_N_XX_name` internally
3. Layer N entities' children are Layer N+1
4. Naming uses underscores, not dots: `layer_N_XX_name`

## Examples
- `0_layer_universal/` - Layer 0 entity
- `layer_1_project_school/` - Layer 1 project
- `layer_2_feature_auth/` - Layer 2 feature (child of Layer 1)

## Internal Structure Numbers
Within a layer, directories are numbered for ordering:
- `layer_N_00_*` - Primary/first items
- `layer_N_01_*` through `layer_N_98_*` - Sequential items
- `layer_N_99_*` - Final/status items (often stages)

## Why This Matters
- Consistent numbering enables automation
- Clear parent-child relationships
- Predictable navigation patterns
- Machine-readable structure
