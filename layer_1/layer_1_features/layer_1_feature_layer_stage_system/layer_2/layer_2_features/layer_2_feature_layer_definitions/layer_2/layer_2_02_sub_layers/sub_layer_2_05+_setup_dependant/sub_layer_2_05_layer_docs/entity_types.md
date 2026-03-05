---
resource_id: "3e51e7c8-42a7-4c11-955e-45b876a6f719"
resource_type: "document"
resource_name: "entity_types"
---
# Entity Types

## Projects
Full work efforts with their own stages and children.
Pattern: `layer_N_project_name/`

### Characteristics
- Has complete stage lifecycle
- Contains features and components
- Represents major deliverables
- Has its own `layer_N/` internals

## Features
Functional units that implement capabilities.
Pattern: `layer_N_feature_name/`

### Characteristics
- Implements specific functionality
- May contain sub-features or components
- Part of a larger project or feature
- Has focused scope

## Components
Reusable building blocks.
Pattern: `layer_N_component_name/`

### Characteristics
- Designed for reuse
- Minimal dependencies
- Self-contained functionality
- Can be shared across features

## Grouping Directories
- `layer_N_projects/` - Contains projects
- `layer_N_features/` - Contains features
- `layer_N_components/` - Contains components

## Type Selection Guide
| Need | Use |
|------|-----|
| Major deliverable | Project |
| Specific capability | Feature |
| Reusable piece | Component |
