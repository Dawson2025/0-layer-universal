---
resource_id: "b25aec2e-207e-4282-985f-f32093833528"
resource_type: "document"
resource_name: "features_init_prompt"
---
# Universal Features Initialization Prompt Template

<!-- section_id: "920e4de6-d974-4541-9c12-14764bda3037" -->
## Purpose

This is the **universal template** for creating project-level features initialization prompts. It provides the standard structure and instructions that should be instantiated in each project's `layer_2_features/` folder.

<!-- section_id: "ee883f01-ecba-4f4d-9037-51697ec3586e" -->
## When to Use This

- When creating a new project's features layer
- When instantiating a project's `features_init_prompt.md`
- When setting up the features folder structure in a project

<!-- section_id: "b25bc384-6ebc-49b3-92a6-4b15bbacc871" -->
## Template Structure

Each project's `layer_2_features/` folder should have:

```
layer_2_features/
├── README.md                              # Features layer overview
├── features_init_prompt.md                # Project-level features init (instantiated from this template)
├── 2.00_ai_manager_system/                # Features layer manager
├── 2.01_manager_handoff_documents/        # Features layer handoffs
│   ├── 2.00_to_universal/
│   └── 2.01_to_specific/
├── 2.02_sub_layers/                       # Features layer knowledge/tools
│   └── sub_layer_2.01_basic_prompts_throughout/
│       └── features_init_prompt.md        # This file (project-specific instantiation)
├── 2.99_stages/                           # Features layer stages
│   ├── stage_2.01_instructions/
│   ├── stage_2.02_planning/
│   ├── stage_2.03_design/
│   ├── stage_2.04_development/
│   ├── stage_2.05_testing/
│   ├── stage_2.06_criticism/
│   ├── stage_2.07_fixing/
│   └── stage_2.09_archives/
└── layer_2_feature_<N>.<XX>_*/           # Individual feature folders
    └── [feature-specific content]
```

<!-- section_id: "fb9a0d80-8d94-4241-9e32-34ca34dc601b" -->
## Features Init Prompt Content Template

When instantiating this in a project, the `features_init_prompt.md` should include:

<!-- section_id: "562ecfff-fa1d-4c0e-8708-edad4887538d" -->
### 1. Critical Reading Order
- Reference to Universal Init Prompt
- Reference to Project Init Prompt
- Reference to this Features Init Prompt

<!-- section_id: "2b5a80ca-8c8e-4629-aedb-dc2b096380de" -->
### 2. Features Layer Purpose
- What the features layer manages in this project
- How features relate to the project's goals
- How features are organized and numbered

<!-- section_id: "52341b51-51f3-43bb-8103-ee43eb266181" -->
### 3. Feature Instantiation Process
- How to create a new feature
- What templates to use
- How to set up feature structure
- How to create feature-specific init prompts

<!-- section_id: "63d5ad22-026f-4b78-8ed5-d5d94f1806ad" -->
### 4. Navigation Patterns
- How to navigate from project → features → specific feature
- How to use the features layer manager system
- How to use handoff documents

<!-- section_id: "3b19e30f-ea40-45a1-a2d2-9e933f389271" -->
### 5. Feature Management
- How features are coordinated
- How features report to the project layer
- How features communicate with each other

<!-- section_id: "b9d3dbfb-71d0-4239-8277-718dad4bb74f" -->
## Instantiation Instructions

When creating a project's `features_init_prompt.md`:

1. **Copy this template structure**
2. **Customize for the project**:
   - Add project-specific feature types
   - Add project-specific navigation patterns
   - Add project-specific feature management rules
3. **Reference the universal and project init prompts**
4. **Provide clear instructions for feature creation**

<!-- section_id: "a629b6b6-0a20-476a-a69e-e6cfdf3b963a" -->
## Key Principles

- **Hierarchy**: Universal → Project → Features → Individual Feature
- **Consistency**: All features follow the same structure
- **Navigation**: Clear paths between layers
- **Handoffs**: Proper use of manager handoff documents
- **Stages**: Features can have their own stage progression

<!-- section_id: "0479c725-1964-40c7-95e1-70bdd0cc5836" -->
## Related Documentation

- **Universal Init Prompt**: `universal_init_prompt.md` (same directory)
- **Layer/Stage Framework**: `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`
- **Feature Template**: `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/`

