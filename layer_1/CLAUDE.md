# layer_1

## Role

**Layer Manager** - Projects, features, and components layer.

## Responsibilities

- Manage project-level work (layer_1_projects/)
- Manage feature-level work (layer_1_features/)
- Manage component-level work (layer_1_components/)
- Receive tasks from Root Manager via `hand_off_documents/incoming/from_above/`
- Delegate to appropriate project, feature, or component
- Aggregate results and report via `hand_off_documents/outgoing/to_above/`
- Handle escalations from projects, features, components

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for tasks from root
2. Check `hand_off_documents/incoming/from_below/` for results/escalations
3. Process pending work or await delegation

## Children

| Child | Purpose |
|-------|---------|
| `layer_1_projects/` | Full project implementations |
| `layer_1_features/` | Cross-project features |
| `layer_1_components/` | Reusable components |

## Navigation

- **Parent**: `../` (0_layer_universal - Root Manager)
- **Projects**: `layer_1_projects/`
- **Features**: `layer_1_features/`
- **Components**: `layer_1_components/`

## Scope

This layer contains:
- **Projects**: Complete applications or systems (each with own stages)
- **Features**: Functionality that spans projects
- **Components**: Reusable building blocks
