---
resource_id: "a8090b7c-883d-46f7-a3ad-70c66ab7d735"
resource_type: "output"
resource_name: "TREE_TO_FEATURES_MAPPING"
---
# Tree of Needs → Further Layering

<!-- section_id: "b3c8e9b0-5982-496b-86ec-c594284cb3a7" -->
## Principle

**The tree of needs hierarchy informs further layering from the current position.**

Wherever you are in the layer hierarchy, the tree of needs for that entity drives how its children are organized:

```
Tree of Needs                    →    Further Layering (Relative to Current)
─────────────────────────────────────────────────────────────────────────────
00_root_need/                    →    (current entity)
├── 01_branch/                   →    ├── child entity (+1 depth)
│   ├── need_01_xxx/             →    │   ├── grandchild entity (+2 depth)
│   ├── need_02_yyy/             →    │   ├── grandchild entity (+2 depth)
│   └── need_03_zzz/             →    │   └── grandchild entity (+2 depth)
├── 02_branch/                   →    ├── child entity (+1 depth)
│   └── ...                      →    │   └── ...
```

<!-- section_id: "baf5de66-c9c8-4e29-a9b2-7fe1aa69afd9" -->
## Context-Dependent Naming

| If Current Entity Is | Branches Become | Needs Become |
|---------------------|-----------------|--------------|
| Project (layer_1) | Features | Components |
| Feature (layer_2) | Components | Sub-components |
| Component (layer_3) | Sub-components | Modules |
| Research project (layer_-1) | Target layers/features | Target components |

---

<!-- section_id: "0ccd84c0-95a0-4ba9-b1f2-cd801afc568d" -->
## This Feature's Mapping

```
Tree of Needs                         Feature Organization
───────────────────────────────────────────────────────────────────────────

00_better_layer_stage_system/         layer_0_feature_better_layer_stage_system/
│                                     └── layer_0_group/layer_0_features/
│
├── 01_consistent_structure/          ├── layer_1_feature_consistent_structure/
│   ├── need_01_all_stages_exist      │   ├── layer_2_component_stage_completeness/
│   ├── need_02_clear_naming          │   ├── layer_2_component_naming_conventions/
│   └── need_03_entry_points          │   └── layer_2_component_entry_points/
│
├── 02_knowledge_accessible/          ├── layer_1_feature_knowledge_accessible/
│   ├── need_01_propagation_chain     │   ├── layer_2_component_propagation_chain/
│   ├── need_02_skills_reference      │   ├── layer_2_component_skills_system/
│   └── need_03_minimal_claude_md     │   └── layer_2_component_minimal_context/
│
├── 03_properly_documented/           ├── layer_1_feature_properly_documented/
│   ├── need_01_tree_of_needs         │   ├── layer_2_component_tree_of_needs/
│   ├── need_02_decisions_in_stages   │   ├── layer_2_component_stage_documentation/
│   └── need_03_diagrams_required     │   └── layer_2_component_diagrams/
│
└── 04_clean_organization/            └── layer_1_feature_clean_organization/
    ├── need_01_merge_consolidated        ├── layer_2_component_merge_system/
    └── need_02_all_11_stages             └── layer_2_component_stage_enforcement/
```

---

<!-- section_id: "16017706-a426-49e1-802d-ae416f9248de" -->
## Why This Mapping Matters

1. **Traceability**: Every feature maps to a need
2. **Completeness**: If a need exists, a feature should address it
3. **Organization**: Hierarchy is consistent and navigable
4. **Documentation**: Tree of needs serves as requirements, features serve as solutions

---

<!-- section_id: "508757b8-8411-4a9d-8c06-f1e641b446b9" -->
## Pattern (Relative Depth)

| Tree Level | Relative Depth | Example at Layer 1 (Project) | Example at Layer 2 (Feature) |
|------------|----------------|------------------------------|------------------------------|
| Root need | Current (+0) | The project itself | The feature itself |
| Branch | Child (+1) | Feature | Component |
| Need | Grandchild (+2) | Component | Sub-component |
| Sub-need | Great-grandchild (+3) | Sub-component | Module |

---

<!-- section_id: "af64cbc9-517d-4e5e-bc8f-5f01bd0669ee" -->
## Version

- **Created**: 2026-02-03
- **Session**: Context Flow Architecture

