---
resource_id: "3e51e7c8-42a7-4c11-955e-45b876a6f719"
resource_type: "document"
resource_name: "entity_types"
---
# Entity Types

<!-- section_id: "4f4aee9c-9f39-4228-9d39-73a51f039ed3" -->
## Projects
Full work efforts with their own stages and children.
Pattern: `layer_N_project_name/`

<!-- section_id: "b0e7054e-2a62-4a1b-8e2f-c6db80edef2c" -->
### Characteristics
- Has complete stage lifecycle
- Contains features and components
- Represents major deliverables
- Has its own `layer_N/` internals

<!-- section_id: "586b13fa-5c08-420d-b9d4-d53f4718d61a" -->
## Features
Functional units that implement capabilities.
Pattern: `layer_N_feature_name/`

<!-- section_id: "49ea679e-d164-4886-b0ed-04ae79ec29f1" -->
### Characteristics
- Implements specific functionality
- May contain sub-features or components
- Part of a larger project or feature
- Has focused scope

<!-- section_id: "513140a0-7010-46a8-8d09-cf8d116d3886" -->
## Components
Reusable building blocks.
Pattern: `layer_N_component_name/`

<!-- section_id: "4e441e5a-e481-4332-a35e-e31e81c33156" -->
### Characteristics
- Designed for reuse
- Minimal dependencies
- Self-contained functionality
- Can be shared across features

<!-- section_id: "8e7bb692-221c-4544-b796-d60173cee842" -->
## Grouping Directories
- `layer_N_projects/` - Contains projects
- `layer_N_features/` - Contains features
- `layer_N_components/` - Contains components

<!-- section_id: "c7044141-2e1c-4986-b386-cb3d52736ac0" -->
## Type Selection Guide
| Need | Use |
|------|-----|
| Major deliverable | Project |
| Specific capability | Feature |
| Reusable piece | Component |
