# Depth Markers

## Purpose
Depth markers indicate how many levels down from a project root an entity exists.

## Notation
- `sub*1` - One level below project
- `sub*2` - Two levels below project
- `sub*N` - N levels below project

## Usage in Directory Names
```
layer_N_sub*1_projects/   # Projects 1 level down
layer_N_sub*2_features/   # Features 2 levels down
```

## Example Structure
```
layer_1_project_main/
├── layer_2/
│   └── layer_2_sub*1_projects/      # sub*1 from main
│       └── layer_2_project_sub/
│           └── layer_3/
│               └── layer_3_sub*2_features/  # sub*2 from main
```

## When to Use
- Tracking depth within large projects
- Organizing deeply nested structures
- Distinguishing sub-projects from root projects

## Calculation
From any entity:
1. Find nearest ancestor project
2. Count layers between them
3. That count is the sub*N value

## Benefits
- Quick depth assessment
- Prevents excessive nesting
- Clarifies project relationships
- Aids navigation in complex structures
