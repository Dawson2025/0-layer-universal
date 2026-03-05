---
resource_id: "8827c23a-8f2e-4699-b742-a0104df668fb"
resource_type: "knowledge"
resource_name: "depth_markers"
---
# Depth Markers

<!-- section_id: "6ac696f2-beca-4b3f-9134-9973dae0f81f" -->
## Purpose
Depth markers indicate how many levels down from a project root an entity exists.

<!-- section_id: "0c9743b9-1019-425e-acf7-4dfc73c27aae" -->
## Notation
- `subx1` - One level below project
- `subx2` - Two levels below project
- `sub*N` - N levels below project

<!-- section_id: "2c55b1e3-8b1d-4a27-9b0b-3f0b99f9c5cc" -->
## Usage in Directory Names
```
layer_N_subx1_projects/   # Projects 1 level down
layer_N_subx2_features/   # Features 2 levels down
```

<!-- section_id: "89ccd2b0-cefe-41a8-ba8f-503fd3405c19" -->
## Example Structure
```
layer_1_project_main/
├── layer_2/
│   └── layer_2_subx1_projects/      # subx1 from main
│       └── layer_2_project_sub/
│           └── layer_3/
│               └── layer_3_subx2_features/  # subx2 from main
```

<!-- section_id: "e7473a88-1941-4b5f-803e-cc8ac0a5db99" -->
## When to Use
- Tracking depth within large projects
- Organizing deeply nested structures
- Distinguishing sub-projects from root projects

<!-- section_id: "905e957a-4ff7-41ca-a91b-92415b37392a" -->
## Calculation
From any entity:
1. Find nearest ancestor project
2. Count layers between them
3. That count is the sub*N value

<!-- section_id: "b02b31c7-720e-45a2-a100-816195c0abca" -->
## Benefits
- Quick depth assessment
- Prevents excessive nesting
- Clarifies project relationships
- Aids navigation in complex structures
