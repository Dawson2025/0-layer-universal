---
resource_id: "e056d2f4-5101-4285-8205-44d73246ec04"
resource_type: "knowledge"
resource_name: "nesting_rules"
---
# Nesting Rules

<!-- section_id: "f9695306-05b7-4e19-9824-05448a12461c" -->
## Core Principle
Every entity has two key directories:
- `layer_N/` - Its own internals (same layer number as entity)
- `layer_N+1/` - Its children (next layer number)

<!-- section_id: "7ebc2eb6-c6b1-4fb8-bd46-0ae720d2cf61" -->
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

<!-- section_id: "6bdaf89c-e428-4320-b261-0355e85da0fe" -->
## Rules
1. Internal directories match entity's layer number
2. Child directories are exactly N+1
3. Grouping directories hold same-type entities
4. CLAUDE.md exists at entity root

<!-- section_id: "46b4f56c-4048-4799-a0be-69c66f32d7a7" -->
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

<!-- section_id: "dd97e948-0b96-4997-8545-a40bde006c3a" -->
## Why Nesting Matters
- Clear ownership hierarchy
- Predictable navigation
- Consistent depth calculation
- Enables automated tooling
