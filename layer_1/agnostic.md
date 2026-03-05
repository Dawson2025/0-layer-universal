---
resource_id: "cef9ec6c-5dce-4932-9683-26c32f36ac62"
resource_type: "document"
resource_name: "agnostic"
---
# layer_1 - Agnostic Context

## Purpose

Tool-agnostic context for the projects layer.

## Scope

Layer 1 contains actual implementations:
- Projects (full applications/systems)
- Features (cross-project functionality)
- Components (reusable building blocks)

## Structure

```
layer_1/
├── layer_1_projects/        Full project implementations
│   └── layer_1_project_*/   Individual projects
├── layer_1_features/        Cross-project features
│   └── layer_1_feature_*/   Individual features
└── layer_1_components/      Reusable components
    └── layer_3_*/           Component definitions
```

## Project Structure

Each project follows the layer-stage pattern:
```
layer_1_project_*/
├── layer_1/
│   ├── layer_1_03_sub_layers/   Project-specific content
│   └── layer_1_99_stages/       Project workflow stages
└── [additional layers as needed]
```

## Inheritance

- Layer 1 inherits from Layer 0 (universal rules apply)
- Projects can have nested features (Layer 2)
- Features can have nested components (Layer 3)

## Navigation

- Go up to `../` for root context
- Go to `layer_0/` for universal rules
- Go to specific project/feature/component for targeted work
