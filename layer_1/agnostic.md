---
resource_id: "cef9ec6c-5dce-4932-9683-26c32f36ac62"
resource_type: "document"
resource_name: "agnostic"
---
# layer_1 - Agnostic Context

<!-- section_id: "7fd72339-a05f-427a-a040-65091f3614a5" -->
## Purpose

Tool-agnostic context for the projects layer.

<!-- section_id: "6f26d3d9-380a-4219-8ed5-e11849ebc71c" -->
## Scope

Layer 1 contains actual implementations:
- Projects (full applications/systems)
- Features (cross-project functionality)
- Components (reusable building blocks)

<!-- section_id: "e7139060-9b12-41ee-83c3-a22c962c8526" -->
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

<!-- section_id: "f168f730-3f27-42e4-95c0-0876755dbd1f" -->
## Project Structure

Each project follows the layer-stage pattern:
```
layer_1_project_*/
├── layer_1/
│   ├── layer_1_03_sub_layers/   Project-specific content
│   └── layer_1_99_stages/       Project workflow stages
└── [additional layers as needed]
```

<!-- section_id: "413d178a-a86a-458f-9897-2776463af242" -->
## Inheritance

- Layer 1 inherits from Layer 0 (universal rules apply)
- Projects can have nested features (Layer 2)
- Features can have nested components (Layer 3)

<!-- section_id: "d31c7238-e411-486c-b79d-c9d8dbad5f5c" -->
## Navigation

- Go up to `../` for root context
- Go to `layer_0/` for universal rules
- Go to specific project/feature/component for targeted work
