---
resource_id: "5f3a9da9-5e70-4da9-8abb-61bf386104c8"
resource_type: "protocol"
resource_name: "features_init_prompt"
---
# Universal Features Initialization Prompt Template

<!-- section_id: "d92b10a1-4208-49d2-8c78-b2e802ea5a74" -->
## Purpose

This is the **universal template** for creating project-level features initialization prompts. It provides the standard structure and instructions that should be instantiated in each project's `layer_2_features/` folder.

<!-- section_id: "c2a45334-0ab6-4a65-8129-d4dfac208fdf" -->
## When to Use This

- When creating a new project's features layer
- When instantiating a project's `features_init_prompt.md`
- When setting up the features folder structure in a project

<!-- section_id: "abc7ae18-9697-4c1c-aaac-0767c4ee64b0" -->
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

<!-- section_id: "5e9015f0-f3e0-401e-a01f-ac416290e2e3" -->
## Features Init Prompt Content Template

When instantiating this in a project, the `features_init_prompt.md` should include:

<!-- section_id: "cca26624-4f71-4fba-b620-e4ef57bd9675" -->
### 1. Critical Reading Order
- Reference to Universal Init Prompt
- Reference to Project Init Prompt
- Reference to this Features Init Prompt

<!-- section_id: "731c412f-680d-4819-baa3-957c82387fd8" -->
### 2. Features Layer Purpose
- What the features layer manages in this project
- How features relate to the project's goals
- How features are organized and numbered

<!-- section_id: "2777fdc6-2d6f-42db-a9a3-6bf750580201" -->
### 3. Feature Instantiation Process
- How to create a new feature
- What templates to use
- How to set up feature structure
- How to create feature-specific init prompts

<!-- section_id: "b12c4ddb-0392-4930-bac2-ab2704045bdf" -->
### 4. Navigation Patterns
- How to navigate from project → features → specific feature
- How to use the features layer manager system
- How to use handoff documents

<!-- section_id: "ec1d39b8-f523-4cc8-97e0-8a39dfe06e86" -->
### 5. Feature Management
- How features are coordinated
- How features report to the project layer
- How features communicate with each other

<!-- section_id: "433a56ff-cb80-4fb4-ba44-c3798d60ee64" -->
## Instantiation Instructions

When creating a project's `features_init_prompt.md`:

1. **Copy this template structure**
2. **Customize for the project**:
   - Add project-specific feature types
   - Add project-specific navigation patterns
   - Add project-specific feature management rules
3. **Reference the universal and project init prompts**
4. **Provide clear instructions for feature creation**

<!-- section_id: "3a6ac0dc-1c96-45fc-b37d-805ebed5386a" -->
## Key Principles

- **Hierarchy**: Universal → Project → Features → Individual Feature
- **Consistency**: All features follow the same structure
- **Navigation**: Clear paths between layers
- **Handoffs**: Proper use of manager handoff documents
- **Stages**: Features can have their own stage progression

<!-- section_id: "4530369e-57ef-48c8-930e-a5dd3f8bf68f" -->
## Related Documentation

- **Universal Init Prompt**: `universal_init_prompt.md` (same directory)
- **Layer/Stage Framework**: `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`
- **Feature Template**: `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/`

