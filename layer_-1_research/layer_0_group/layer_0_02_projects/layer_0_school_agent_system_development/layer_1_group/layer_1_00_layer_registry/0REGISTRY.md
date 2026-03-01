# Layer 1 Registry — School Agent System Projects

## Purpose

This registry documents the layer_1 organizational structure. Layer_1 is organized as a **GROUP** (container) that holds layer_2 feature and project entities.

## Layer 1 Organization

### Grouping Containers

Layer_1 uses numbered grouping containers to organize layer_2 child entities:

| Container | Type | Purpose | Entities |
|-----------|------|---------|----------|
| `layer_1_01_features/` | Feature container | Organizes layer_2 feature entities | Currently empty — ready for layer_2 features |
| `layer_1_02_projects/` | Project container | Optional: organizes layer_2 projects | Not yet created |
| `layer_1_03_*` | Other | Optional: other organizational purposes | Not yet created |

### Child Entities

Each entity placed in a grouping container is a **layer_2 entity** (actual layer, not container). Examples:
- `layer_1_01_features/layer_2_feature_teacher_assistant/`
- `layer_1_01_features/layer_2_feature_student_dashboard/`
- etc.

Each layer_2 entity will have:
- Own `0AGNOSTIC.md` defining layer_2 identity
- Own `layer_2_group/` with registry and stages
- 11 workflow stages (`layer_2_99_stages/stage_2_01_*` through `stage_2_11_*`)
- Full `.0agnostic/`, `.1merge/`, tool configurations

## Critical Distinction

**This is a GROUP, not a LAYER.**

- ❌ `layer_1_group/` has NO `layer_1_99_stages/` — groups don't have stages
- ✅ Each child entity (layer_2) inside grouping containers HAS its own stages
- ✅ `layer_1_00_layer_registry/` exists to document organizational structure
- ✅ `layer_1_0X_*` grouping containers exist to organize children

## Hierarchy Visualization

```
layer_0_school_agent_system_development/     (Layer 0 entity)
├── layer_0_group/                           (Layer 0's internal structure)
│   ├── layer_0_00_layer_registry/
│   └── layer_0_99_stages/                   ✅ Layer 0 has stages
│       ├── stage_0_01_request_gathering/
│       └── ... (stages 02-11)
│
└── layer_1_group/                           (Layer 0's child container — NOT a layer)
    ├── layer_1_00_layer_registry/           (This file)
    ├── layer_1_01_features/                 (Organizational grouping)
    │   ├── layer_2_feature_one/             (Layer 2 entity — IS a layer)
    │   │   ├── layer_2_group/
    │   │   │   └── layer_2_99_stages/       ✅ Layer 2 has stages
    │   │   └── [other layer_2 resources]
    │   └── layer_2_feature_two/
    └── layer_1_02_projects/                 (Optional: another grouping)
        └── [layer_2 project entities]
```

## Status

| Item | Status |
|------|--------|
| Layer 1 registry | ✅ Created |
| Feature grouping container | ✅ Created |
| Project grouping container | ⏳ Not yet created |
| Layer 2 feature entities | ⏳ Pending |

## Next Steps

1. Create layer_2 feature entities as needed
2. Each feature entity goes inside `layer_1_01_features/`
3. Each feature entity gets its own full layer_2 structure (0AGNOSTIC.md, stages, etc.)
4. Use `/entity-creation` skill to create properly-structured layer_2 features

---

*Registry of organizational structure. For entity-level context, see parent `../0AGNOSTIC.md`.*
