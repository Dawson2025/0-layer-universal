---
resource_id: "b6088ad5-3b84-48a9-89d1-3d2752a119f3"
resource_type: "knowledge"
resource_name: "entity_types"
---
# Entity Types

<!-- section_id: "a4a54588-004a-4fcf-bc4c-12030594db91" -->
## Projects
Full work efforts with their own stages and children.
Pattern: `layer_N_project_name/`

<!-- section_id: "807eff88-d7fc-4211-bc3d-6fe359d08e01" -->
### Characteristics
- Has complete stage lifecycle
- Contains features and components
- Represents major deliverables
- Has its own `layer_N/` internals

<!-- section_id: "607f525d-4d7f-48d0-ad59-1ebe185521fc" -->
## Features
Functional units that implement capabilities.
Pattern: `layer_N_feature_name/`

<!-- section_id: "d568bbdc-8a5b-4e90-9365-32ab84668e6d" -->
### Characteristics
- Implements specific functionality
- May contain sub-features or components
- Part of a larger project or feature
- Has focused scope

<!-- section_id: "9b01f07c-dc03-4fa4-b5de-1ca5483016b1" -->
## Components
Reusable building blocks.
Pattern: `layer_N_component_name/`

<!-- section_id: "6b1926d8-41e8-46fe-80d2-d106b9c80ecd" -->
### Characteristics
- Designed for reuse
- Minimal dependencies
- Self-contained functionality
- Can be shared across features

<!-- section_id: "293f7053-c400-40e4-93c2-1f72170088f3" -->
## Grouping Directories
- `layer_N_projects/` - Contains projects
- `layer_N_features/` - Contains features
- `layer_N_components/` - Contains components

<!-- section_id: "1049b57d-60d2-4d20-97d3-702d16ce7bb2" -->
## Type Selection Guide
| Need | Use |
|------|-----|
| Major deliverable | Project |
| Specific capability | Feature |
| Reusable piece | Component |
