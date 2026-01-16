# layer_2_feature_layer_definitions

## Purpose
Defines layer numbering, entity types, and nesting rules for the Layer-Stage Framework.

## Core Concepts

### Layer Numbering
- Layer 0: Universal root
- Layer 1: Projects, features, components under universal
- Layer N+1: Children of Layer N entities

### Entity Types
- **Projects**: Major work efforts (layer_N_project_name)
- **Features**: Functional units (layer_N_feature_name)
- **Components**: Reusable pieces (layer_N_component_name)

### Nesting Pattern
Every entity has:
- `layer_N/` - Its own internals
- `layer_N+1/` - Its children

### Depth Markers
- `sub*1` indicates 1 level down from project
- `sub*2` indicates 2 levels down from project
- Used in: `layer_N_sub*X_projects/`

## Documentation
See `layer_2/layer_2_02_sub_layers/sub_layer_2_05+_setup_dependant/sub_layer_2_05_layer_docs/`
