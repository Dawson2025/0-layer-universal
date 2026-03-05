---
resource_id: "967f3650-7c33-47cf-be0c-45ab4cbe880c"
resource_type: "document"
resource_name: "0REGISTRY"
---
# Layer 1 Registry — School Agent System Projects

<!-- section_id: "027ccf40-b56b-4b1f-8fb5-8b7fb6325bc8" -->
## Purpose

This registry documents the layer_1 organizational structure. Layer_1 is organized as a **GROUP** (container) that holds layer_2 feature and project entities.

<!-- section_id: "4cd12701-7aa6-4fbd-85ff-79c97eff7d32" -->
## Layer 1 Organization

<!-- section_id: "90ee6324-7204-42b0-8a3e-1b7b9ae85356" -->
### Grouping Containers

Layer_1 uses numbered grouping containers to organize layer_2 child entities:

| Container | Type | Purpose | Entities |
|-----------|------|---------|----------|
| `layer_1_01_features/` | Feature container | Organizes layer_2 feature entities | Currently empty — ready for layer_2 features |
| `layer_1_02_projects/` | Project container | Optional: organizes layer_2 projects | Not yet created |
| `layer_1_03_*` | Other | Optional: other organizational purposes | Not yet created |

<!-- section_id: "0521e620-0e9f-4890-9ac0-042646a9543b" -->
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

<!-- section_id: "780dce62-1f43-4548-999f-1ebd53cb83a3" -->
## Critical Distinction

**This is a GROUP, not a LAYER.**

- ❌ `layer_1_group/` has NO `layer_1_99_stages/` — groups don't have stages
- ✅ Each child entity (layer_2) inside grouping containers HAS its own stages
- ✅ `layer_1_00_layer_registry/` exists to document organizational structure
- ✅ `layer_1_0X_*` grouping containers exist to organize children

<!-- section_id: "466ef1ba-7309-43f0-9b7a-a1e266b5afdc" -->
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

<!-- section_id: "950c78c2-e939-4476-84ed-ba808665ff9d" -->
## Status

| Item | Status |
|------|--------|
| Layer 1 registry | ✅ Created |
| Feature grouping container | ✅ Created |
| Project grouping container | ⏳ Not yet created |
| Layer 2 feature entities | ⏳ Pending |

<!-- section_id: "7d6e7311-e9ec-4221-bafb-7fb90e52adc7" -->
## Next Steps

1. Create layer_2 feature entities as needed
2. Each feature entity goes inside `layer_1_01_features/`
3. Each feature entity gets its own full layer_2 structure (0AGNOSTIC.md, stages, etc.)
4. Use `/entity-creation` skill to create properly-structured layer_2 features

---

*Registry of organizational structure. For entity-level context, see parent `../0AGNOSTIC.md`.*
