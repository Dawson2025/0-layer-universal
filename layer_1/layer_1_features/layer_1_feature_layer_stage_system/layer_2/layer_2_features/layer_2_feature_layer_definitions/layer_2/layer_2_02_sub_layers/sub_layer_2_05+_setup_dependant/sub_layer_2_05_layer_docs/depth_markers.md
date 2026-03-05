---
resource_id: "35771bb3-f938-45da-8253-7c85bdab7a9d"
resource_type: "document"
resource_name: "depth_markers"
---
# Depth Markers

<!-- section_id: "92a580de-c33a-46ee-90d1-23702b7f01b5" -->
## Purpose
Depth markers indicate how many levels down from a project root an entity exists.

<!-- section_id: "adede413-49f0-4230-ad6b-ac331da665fd" -->
## Notation
- `subx1` - One level below project
- `subx2` - Two levels below project
- `sub*N` - N levels below project

<!-- section_id: "eaa048f6-4f31-4800-a570-809c0abd9cd9" -->
## Usage in Directory Names
```
layer_N_subx1_projects/   # Projects 1 level down
layer_N_subx2_features/   # Features 2 levels down
```

<!-- section_id: "2ee31aef-81f0-47d6-8fb9-bd66c9e0ac7e" -->
## Example Structure
```
layer_1_project_main/
├── layer_2/
│   └── layer_2_subx1_projects/      # subx1 from main
│       └── layer_2_project_sub/
│           └── layer_3/
│               └── layer_3_subx2_features/  # subx2 from main
```

<!-- section_id: "60af2a60-dd46-4545-b2d3-500d1adabca4" -->
## When to Use
- Tracking depth within large projects
- Organizing deeply nested structures
- Distinguishing sub-projects from root projects

<!-- section_id: "57c4a1e8-5284-49fc-87a5-d703d795d211" -->
## Calculation
From any entity:
1. Find nearest ancestor project
2. Count layers between them
3. That count is the sub*N value

<!-- section_id: "a1fd5182-19f5-4508-9f7c-e7775b7b9fac" -->
## Benefits
- Quick depth assessment
- Prevents excessive nesting
- Clarifies project relationships
- Aids navigation in complex structures
