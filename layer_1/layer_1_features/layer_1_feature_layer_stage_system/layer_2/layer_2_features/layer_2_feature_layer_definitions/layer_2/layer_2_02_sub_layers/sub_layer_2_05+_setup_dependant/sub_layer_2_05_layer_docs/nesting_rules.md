---
resource_id: "ca440cea-285e-41c0-9c0d-53c069b6205f"
resource_type: "document"
resource_name: "nesting_rules"
---
# Nesting Rules

<!-- section_id: "d790129d-e90f-431f-acf7-d4e893d0179b" -->
## Core Principle
Every entity has two key directories:
- `layer_N/` - Its own internals (same layer number as entity)
- `layer_N+1/` - Its children (next layer number)

<!-- section_id: "c51251ff-3c18-4767-bb38-66c24695cf69" -->
## Visual Pattern
```
layer_N_entity_name/           # Entity at Layer N
├── CLAUDE.md                  # Entity description
├── layer_N/                   # Internal structure
│   ├── layer_N_00_*/          # Internal item 1
│   ├── layer_N_01_*/          # Internal item 2
│   └── layer_N_99_stages/     # Status tracking
└── layer_N+1/                 # Children
    ├── layer_N+1_features/    # Child features
    ├── layer_N+1_projects/    # Child projects
    └── layer_N+1_components/  # Child components
```

<!-- section_id: "48cf8056-cee5-4857-9b4e-a2548ebec470" -->
## Rules
1. Internal directories match entity's layer number
2. Child directories are exactly N+1
3. Grouping directories hold same-type entities
4. CLAUDE.md exists at entity root

<!-- section_id: "42ba4695-42b8-477f-acc3-ec559eafe469" -->
## Example Chain
```
0_layer_universal/             # Layer 0
└── layer_1/
    └── layer_1_projects/
        └── layer_1_project_app/   # Layer 1
            └── layer_2/
                └── layer_2_features/
                    └── layer_2_feature_auth/  # Layer 2
                        └── layer_3/
                            └── layer_3_components/  # Layer 3
```

<!-- section_id: "8e58b2ce-4065-4b8f-97d8-b0002c3202cc" -->
## Why Nesting Matters
- Clear ownership hierarchy
- Predictable navigation
- Consistent depth calculation
- Enables automated tooling
