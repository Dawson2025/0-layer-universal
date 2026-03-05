---
resource_id: "b90e5fd4-91ef-4e76-923a-e1f201110757"
resource_type: "document"
resource_name: "FLEXIBLE_LAYERING_SYSTEM"
---
# Flexible N-Layer Architecture System

**Purpose:** This document defines the flexible, arbitrarily-nested layer system that supports unlimited depth of features and components.

**Location:** `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/FLEXIBLE_LAYERING_SYSTEM.md`

**Last Updated:** 2026-01-14
**Version:** 4.0 - Layer Grouping Convention

---

<!-- section_id: "6c557d93-b6e1-454f-a676-aedf4cd462fc" -->
## Overview

The flexible layering system allows **arbitrary nesting** of features and components to any depth required by your project's complexity, using the **same-type nesting convention** to clearly indicate relationships and the **layer grouping convention** to organize entity internals vs nested content.

**Key Principles:**
1. **Layer numbers indicate depth**, not fixed types
2. **"Sub" prefix only applies to same-type nesting**: A project inside a project = sub_project. A feature inside a feature = sub_feature. But a feature inside a project = feature (NOT sub_feature).
3. **Any layer can contain features AND components** (not sub_features/sub_components at the base level)
4. **Infinite nesting** - create as many levels as needed
5. **Each layer follows the same structure** (manager, handoffs, sub-layers, stages)
6. **Every layer has sub_layers**: ALL features, sub_features, components, and sub_components have `layer_N/layer_N_02_sub_layers/` with content slots
7. **Consistent numbering** shows position in hierarchy
8. **Layer grouping**: Each entity has two sibling folders - `layer_N/` for internals and `layer_N+1/` for nested content

---

<!-- section_id: "b5ee0f6a-d5e3-432e-801d-d4fe9583ddcf" -->
## Layer Grouping Pattern

<!-- section_id: "63a56fc0-72e4-44ec-85df-2cc8711a7dd5" -->
### The Two-Folder Structure

Every project-type entity (project, sub_project, sub*N_project) has two sibling folders at its root:

```
layer_N_<type>_<name>/
├── layer_N/                              # This entity's internals
│   ├── layer_N_00_ai_manager_system/
│   ├── layer_N_01_manager_handoff_documents/
│   ├── layer_N_02_sub_layers/
│   └── layer_N_99_stages/
└── layer_N+1/                            # Nested content (siblings!)
    ├── layer_N+1_sub*X_projects/         # Always present
    ├── layer_N+1_features/               # Always present
    └── layer_N+1_components/             # Always present
```

**Key Points:**
- `layer_N/` groups the entity's **own internals** (ai_manager, handoffs, sub_layers, stages)
- `layer_N+1/` groups **nested content** (sub-projects, features, components)
- These two folders are **SIBLINGS** at the entity root, not nested within each other
- Every project-type entity **always has all three folders** in `layer_N+1/`: sub*X_projects, features, components

<!-- section_id: "eb7f0e48-5e36-4322-b02d-55775826a940" -->
### Why Layer Grouping?

1. **Clear separation**: Entity internals vs nested content are visually distinct
2. **Predictable navigation**: Always know where to find management vs content
3. **Consistent pattern**: Same structure at every depth level
4. **Easy scanning**: All internals grouped, all nested items grouped

---

<!-- section_id: "c3e4cb32-b5f2-4645-b6c3-3ba18deafb60" -->
## Layer Numbering System

<!-- section_id: "debe58e6-e7df-4f7b-ac0c-0e336ddb258a" -->
### Fixed Layers (0-1)

- **Layer 0:** Universal - Applies to all projects
- **Layer 1:** Project - Project-specific context

<!-- section_id: "2e6f1b0d-bb0b-4d78-b270-bfbb6822a27b" -->
### Flexible Layers (2-N)

Starting at Layer 2, the system supports **arbitrary depth** using **same-type nesting convention**:

**CRITICAL NAMING RULE:** The "sub" prefix ONLY applies when nesting the SAME type of entity:
- Project inside project = **sub_project**
- Feature inside feature = **sub_feature**
- Component inside component = **sub_component**

But DIFFERENT types don't get the "sub" prefix:
- Feature inside project = **feature** (NOT sub_feature)
- Component inside project = **component** (NOT sub_component)
- Feature inside sub_project = **feature** (NOT sub_feature)
- Feature inside subx2_project = **feature** (NOT sub_feature)

**Examples of same-type nesting depth:**
- `sub_project` = project 1 level deep
- `subx2_project` = project 2 levels deep
- `sub_feature` = feature 1 level deep (inside another feature)
- `subx2_feature` = feature 2 levels deep (inside a sub_feature)

**The layer number = depth in the hierarchy tree**

---

<!-- section_id: "9cfb2bd1-7501-45f5-90a8-7817252eea74" -->
## Directory Structure Pattern

<!-- section_id: "796fb210-add6-4fbd-a886-cf5805148b7c" -->
### Pattern for Project/Sub_Project/Sub*N_Project

Projects (and sub_projects) contain **features** and **components** directly (not sub_features/sub_components):

```
layer_1_project_<name>/                          # OR layer_2_sub_project_<name>/ OR layer_3_subx2_project_<name>/
├── layer_1/                                     # This entity's internals
│   ├── layer_1_00_ai_manager_system/            # Manager for this layer
│   ├── layer_1_01_manager_handoff_documents/    # Communication
│   │   ├── layer_1_00_to_universal/             # Reports up
│   │   └── layer_1_01_to_specific/              # Context down
│   ├── layer_1_02_sub_layers/                   # Content slots
│   │   └── sub_layer_1.xx.../
│   └── layer_1_99_stages/                       # Workflow stages
│       └── status.json                        # Status tracker
└── layer_2/                                     # Nested content
    ├── layer_2_sub_projects/                    # Sub-projects (same-type nesting)
    │   └── layer_2_sub_project_<name>/
    ├── layer_2_features/                        # Features (NOT sub_features!)
    │   └── layer_2_feature_<name>/
    └── layer_2_components/                      # Components (NOT sub_components!)
        └── layer_2_component_<name>/
```

<!-- section_id: "1f73b6c5-ad9a-45ef-adf3-cda2854fc21a" -->
### Pattern for Feature/Sub_Feature/Sub*N_Feature

Features contain **sub_features** and **sub_components** (because feature inside feature = sub_feature):

```
layer_2_feature_<name>/                          # OR layer_3_sub_feature_<name>/ OR layer_4_subx2_feature_<name>/
├── layer_2/                                     # This entity's internals
│   ├── layer_2_00_ai_manager_system/            # Manager for this layer
│   ├── layer_2_01_manager_handoff_documents/    # Communication
│   │   ├── layer_2_00_to_universal/             # Reports up
│   │   └── layer_2_01_to_specific/              # Context down
│   ├── layer_2_02_sub_layers/                   # Content slots
│   │   └── sub_layer_2.xx.../
│   └── layer_2_99_stages/                       # Workflow stages
│       └── status_2.json                        # Status tracker
└── layer_3/                                     # Nested content
    ├── layer_3_sub_features/                    # Sub-features (feature inside feature)
    │   └── layer_3_sub_feature_<name>/
    └── layer_3_sub_components/                  # Sub-components (component inside feature context)
        └── layer_3_sub_component_<name>/
```

<!-- section_id: "e1b122b4-f62a-4011-9551-3a6901a9c0a9" -->
### Pattern for Component/Sub_Component/Sub*N_Component

Components contain **sub_components** (because component inside component = sub_component):

```
layer_2_component_<name>/                        # OR layer_3_sub_component_<name>/ OR layer_4_subx2_component_<name>/
├── layer_2/                                     # This entity's internals
│   ├── layer_2_00_ai_manager_system/            # Manager for this layer
│   ├── layer_2_01_manager_handoff_documents/    # Communication
│   │   ├── layer_2_00_to_universal/             # Reports up
│   │   └── layer_2_01_to_specific/              # Context down
│   ├── layer_2_02_sub_layers/                   # Content slots
│   │   └── sub_layer_2.xx.../
│   └── layer_2_99_stages/                       # Workflow stages
│       └── status_2.json                        # Status tracker
└── layer_3/                                     # Nested content
    └── layer_3_sub_components/                  # Sub-components (component inside component)
        └── layer_3_sub_component_<name>/
```

**Key Points:**
- **Projects** contain `features/` and `components/` (no "sub" prefix)
- **Sub_projects** also contain `features/` and `components/` (no "sub" prefix, because feature inside project != sub_feature)
- **Features** contain `sub_features/` and `sub_components/` (because feature inside feature = sub_feature)
- **Components** contain `sub_components/` (because component inside component = sub_component)
- **Same-type nesting** uses: `sub`, `subx2`, `subx3`, etc.

---

<!-- section_id: "ac1a61ac-a1ec-46a5-bee4-edfc6a2b7d32" -->
## Naming Conventions

<!-- section_id: "2668edb8-6c08-4692-9508-76d2bb70539c" -->
### Old vs New Directory Naming

The layer grouping convention changes how internal directories are named:

| Old Convention | New Convention |
|----------------|----------------|
| `N.00_ai_manager_system/` | `layer_N/layer_N_00_ai_manager_system/` |
| `N.01_manager_handoff_documents/` | `layer_N/layer_N_01_manager_handoff_documents/` |
| `N.02_sub_layers/` | `layer_N/layer_N_02_sub_layers/` |
| `N.99_stages/` | `layer_N/layer_N_99_stages/` |
| `layer_N+1_features/` | `layer_N+1/layer_N+1_features/` |
| `layer_N+1_components/` | `layer_N+1/layer_N+1_components/` |

<!-- section_id: "ab6701a5-57ac-45f7-97ad-b70abf4596e6" -->
### The "Sub" Prefix Rule

**CRITICAL:** The "sub" prefix indicates **same-type nesting only**:

| Parent Type | Child Type | Uses "sub" prefix? |
|-------------|------------|-------------------|
| Project | Project | YES -> `sub_project` |
| Project | Feature | NO -> `feature` |
| Project | Component | NO -> `component` |
| Sub_project | Feature | NO -> `feature` |
| Sub_project | Component | NO -> `component` |
| Feature | Feature | YES -> `sub_feature` |
| Feature | Component | YES -> `sub_component` (in feature context) |
| Component | Component | YES -> `sub_component` |

<!-- section_id: "0eaf2657-7dcb-4e2c-b970-46fcc1409fd5" -->
### Project Naming

```
layer_1_project_<name>/
layer_2_sub_project_<name>/
layer_3_subx2_project_<name>/
layer_N_sub*<N-1>_project_<name>/
```

<!-- section_id: "7e92d222-bd5b-4143-83e4-40a3c014a474" -->
### Feature Naming

**In a project/sub_project (no "sub" prefix):**
```
layer_2_feature_<name>/        # Feature in project
layer_3_feature_<name>/        # Feature in sub_project
layer_4_feature_<name>/        # Feature in subx2_project
```

**In another feature (uses "sub" prefix):**
```
layer_3_sub_feature_<name>/    # Feature inside a feature
layer_4_subx2_feature_<name>/  # Feature inside a sub_feature
layer_5_subx3_feature_<name>/  # Feature inside a subx2_feature
```

**Examples:**
- `layer_2_feature_in_class_work/` - Feature directly in project (depth 2)
- `layer_3_feature_machine_learning/` - Feature in sub_project (depth 3, still "feature" not "sub_feature")
- `layer_3_sub_feature_derivatives/` - Sub-feature inside a feature (depth 3)
- `layer_4_subx2_feature_power_rule/` - Sub*2-feature inside a sub_feature (depth 4)

<!-- section_id: "4eaea2ab-e616-4efd-a1ce-85dfd3e0a6a1" -->
### Component Naming

**In a project/sub_project (no "sub" prefix):**
```
layer_2_component_<name>/      # Component in project
layer_3_component_<name>/      # Component in sub_project
layer_4_component_<name>/      # Component in subx2_project
```

**In a feature or another component (uses "sub" prefix):**
```
layer_3_sub_component_<name>/  # Component inside a feature
layer_4_subx2_component_<name>/ # Component inside a sub_component
```

**Examples:**
- `layer_2_component_worksheet_1/` - Component in project (depth 2)
- `layer_3_component_web_app/` - Component in sub_project (depth 3, still "component" not "sub_component")
- `layer_3_sub_component_practice_set/` - Sub-component inside a feature (depth 3)

<!-- section_id: "c1423daa-0d1b-428f-a8bb-c66208bcd470" -->
### Directory Naming Within Layers

**Manager and Handoffs (inside `layer_N/`):**
- `layer_N_00_ai_manager_system/`
- `layer_N_01_manager_handoff_documents/`
  - `layer_N_00_to_universal/`
  - `layer_N_01_to_specific/`

**Sub-layers (Every Layer Has These, inside `layer_N/`):**
- `layer_N_02_sub_layers/`
  - `sub_layer_N.01_<name>/` through `sub_layer_N.12_<name>/`
  - **Purpose**: Specialized content at this layer level
  - **Common uses**:
    - `sub_layer_N.01_visual_notes/excalidraw/` - Excalidraw diagrams
    - `sub_layer_N.02_knowledge/` - Documentation, references
    - `sub_layer_N.03_tools/` - Scripts, utilities
    - `sub_layer_N.04_resources/` - Files, assets
  - **Available in**: ALL features, sub_features, components, sub_components

**Stages (inside `layer_N/`):**
- `layer_N_99_stages/`
  - `stage_N.01_instructions/`
  - ... through `stage_N.09_archives/`
  - `status_N.json`

---

<!-- section_id: "6fabf903-fca2-4a03-8ecd-ba26c7a6a43e" -->
## Real-World Example: Applied Calculus

<!-- section_id: "feb5c374-09c5-4054-b303-f812cd64961d" -->
### Scenario: Organizing in-class work with topics and daily components

```
layer_1_project_applied_calculus/                    # Applied Calculus Project (depth 1)
├── layer_1/                                         # Project internals
│   ├── layer_1_00_ai_manager_system/
│   ├── layer_1_01_manager_handoff_documents/
│   ├── layer_1_02_sub_layers/
│   └── layer_1_99_stages/
└── layer_2/                                         # Nested content
    └── layer_2_features/
        └── layer_2_feature_in_class_work/           # Container feature (depth 2)
            ├── layer_2/                             # Feature internals
            │   ├── layer_2_00_ai_manager_system/
            │   ├── layer_2_01_manager_handoff_documents/
            │   ├── layer_2_02_sub_layers/
            │   │   └── sub_layer_2.01_visual_notes/ # General class notes
            │   └── layer_2_99_stages/
            │       └── status_2.json
            └── layer_3/                             # Nested content
                └── layer_3_sub_features/
                    └── layer_3_sub_feature_derivatives/     # Main topic (depth 3)
                        ├── layer_3/                         # Sub-feature internals
                        │   ├── layer_3_00_ai_manager_system/
                        │   ├── layer_3_02_sub_layers/
                        │   │   └── sub_layer_3.01_visual_notes/  # Derivatives overview
                        │   └── layer_3_99_stages/
                        │       ├── stage_3.04_development/
                        │       │   └── hand_off_documents/
                        │       │       └── proactor_lecture_2026-01-09_derivatives.md
                        │       └── status_3.json
                        └── layer_4/                         # Nested content
                            ├── layer_4_subx2_features/
                            │   └── layer_4_subx2_feature_power_rule/    # Subtopic (depth 4)
                            │       ├── layer_4/
                            │       │   ├── layer_4_00_ai_manager_system/
                            │       │   ├── layer_4_02_sub_layers/
                            │       │   │   └── sub_layer_4.01_visual_notes/
                            │       │   └── layer_4_99_stages/
                            │       │       └── status_4.json
                            │       └── layer_5/
                            │           ├── layer_5_subx3_features/
                            │           │   └── layer_5_subx3_feature_negative_exponents/
                            │           │       └── ...
                            │           └── layer_5_subx3_components/
                            │               ├── layer_5_subx3_component_2026_01_09_class/
                            │               │   ├── layer_5/
                            │               │   │   ├── layer_5_00_ai_manager_system/
                            │               │   │   ├── layer_5_02_sub_layers/
                            │               │   │   │   └── sub_layer_5.01_visual_notes/
                            │               │   │   │       └── excalidraw/
                            │               │   │   │           ├── jan09_problem_1.excalidraw
                            │               │   │   │           └── jan09_problem_2.excalidraw
                            │               │   │   └── layer_5_99_stages/
                            │               │   │       └── stage_5.05_testing/
                            │               │   │           └── hand_off_documents/
                            │               │   │               └── byui_math_problems_jan09.md
                            │               │   └── layer_6/
                            │               │       └── layer_6_subx4_components/
                            │               └── layer_5_subx3_component_2026_01_11_class/
                            │                   └── ...
                            └── layer_4_subx2_components/
                                └── ...
```

---

<!-- section_id: "7c13d6bc-6abf-4c03-a379-e05722576d4c" -->
## Applied Calculus Use Case

<!-- section_id: "33c5b1f6-3231-4c57-b178-973d4656dc9b" -->
### Your Classroom Workflow

**During lecture with BYUI Math page, Excalidraw, and Proactor AI:**

1. **Container Feature:** In-Class Work -> Create `layer_2_feature_in_class_work/`

2. **Main Topic:** Derivatives
   - Create: `layer_2_feature_in_class_work/layer_3/layer_3_sub_features/layer_3_sub_feature_derivatives/`
   - Save Proactor AI transcript in: `layer_3/layer_3_99_stages/stage_3.04_development/hand_off_documents/`
   - Save overview diagrams in: `layer_3/layer_3_02_sub_layers/sub_layer_3.01_visual_notes/`

3. **Subtopic in lecture:** Power Rule
   - Create: `layer_3_sub_feature_derivatives/layer_4/layer_4_subx2_features/layer_4_subx2_feature_power_rule/`
   - Save Proactor AI transcript in: `layer_4/layer_4_99_stages/stage_4.04_development/hand_off_documents/`
   - Save Excalidraw work in: `layer_4/layer_4_02_sub_layers/sub_layer_4.01_visual_notes/`

4. **Daily Practice Problems from BYUI Math page**
   - Create: `layer_4_subx2_feature_power_rule/layer_5/layer_5_subx3_components/layer_5_subx3_component_2026_01_09_class/`
   - Show your work in Excalidraw, save to: `layer_5/layer_5_02_sub_layers/sub_layer_5.01_visual_notes/excalidraw/`
   - Document problems from BYUI Math page in: `layer_5/layer_5_99_stages/stage_5.05_testing/hand_off_documents/`

---

<!-- section_id: "99a4a51a-5480-4274-a65e-d34e98ab0a44" -->
## When to Create Each Layer Type

<!-- section_id: "418be94a-1113-454f-afcf-653e9020593b" -->
### Features (Topics/Concepts)

Create a **feature** when you have:
- A distinct topic or concept to learn
- Content that benefits from organized study stages
- Subtopics that need further breakdown

**In Project/Sub_Project context (uses "feature"):**
- `layer_2_feature_derivatives/` - Feature in project
- `layer_3_feature_machine_learning/` - Feature in sub_project

**In Feature context (uses "sub_feature"):**
- `layer_3_sub_feature_power_rule/` - Sub-feature inside a feature
- `layer_4_subx2_feature_negative_exponents/` - Sub*2-feature inside a sub_feature

<!-- section_id: "3df87ee7-7252-4301-9dbd-b1ca0aab6abd" -->
### Components (Work/Artifacts)

Create a **component** when you have:
- Practice problems to work through
- Homework assignments
- Worksheets
- Specific examples or exercises
- Exam prep materials

**In Project/Sub_Project context (uses "component"):**
- `layer_2_component_homework_1/` - Component in project
- `layer_3_component_web_app/` - Component in sub_project

**In Feature/Component context (uses "sub_component"):**
- `layer_3_sub_component_practice_set_1/` - Sub-component inside a feature
- `layer_4_subx2_component_problem_7/` - Sub*2-component inside a sub_component

---

<!-- section_id: "a1a46e4b-f2ed-4db2-8346-5a5eea48152b" -->
## Navigation Patterns

<!-- section_id: "65f3a9b7-18c4-47c2-ad2a-c3a7c72048f9" -->
### Depth-First Navigation (Feature inside Feature)

```bash
# From project context root
cd layer_2/layer_2_features/layer_2_feature_derivatives/

# Navigate to entity internals
cd layer_2/layer_2_00_ai_manager_system/

# Navigate to sub-feature (feature inside feature uses "sub")
cd ../../layer_3/layer_3_sub_features/layer_3_sub_feature_power_rule/

# Navigate to subx2-feature (feature inside sub_feature)
cd layer_4/layer_4_subx2_features/layer_4_subx2_feature_negative_exponents/

# Navigate to subx2-component at this level (component inside feature context)
cd ../layer_4_subx2_components/layer_4_subx2_component_practice_set_1/
```

<!-- section_id: "1aea6524-0f62-413f-952d-6b3deaedf4dd" -->
### Breadth Navigation (Siblings at Same Level)

```bash
# From a layer 3 sub_feature (inside a feature)
cd layer_3/layer_3_sub_features/layer_3_sub_feature_power_rule/

# Move to sibling sub_feature at same level
cd ../layer_3_sub_feature_product_rule/

# Move to another sibling
cd ../layer_3_sub_feature_chain_rule/
```

<!-- section_id: "120723b0-14f2-4a3d-b86b-93e1b275ec1f" -->
### Navigation in Sub_Project Context (uses features, not sub_features)

```bash
# From a sub_project
cd layer_2_sub_project_classes/

# Navigate to feature (NOT sub_feature, because different type)
cd layer_3/layer_3_features/layer_3_feature_machine_learning/

# Navigate to component (NOT sub_component, because different type)
cd ../layer_3_components/layer_3_component_web_app/
```

<!-- section_id: "9c54a60d-c947-43c7-a859-784dc1b4964e" -->
### Accessing Entity Internals

```bash
# From any entity, access its internals
cd layer_2_feature_derivatives/layer_2/

# Access manager system
cd layer_2_00_ai_manager_system/

# Access stages
cd ../layer_2_99_stages/

# Access sub-layers
cd ../layer_2_02_sub_layers/
```

<!-- section_id: "1e442139-f995-4d6e-bc7b-42ec79648e62" -->
### Upward Navigation (Parent Layers)

```bash
# From layer 4 feature, go to parent layer 3 feature
cd ../../../../  # Up to layer_3_sub_feature_power_rule/

# From any depth, go to project root
cd <project_root>/0_context/0_context/
```

---

<!-- section_id: "51b84381-bf85-4b3c-b43c-96478cfdb87b" -->
## Creating New Layers

<!-- section_id: "580abbc6-fb40-481b-b3a0-ad9b79a5f403" -->
### Template Pattern

All layers N >= 2 use the same template structure, just with different numbers.

**For Features:**
```bash
# Copy template and rename to appropriate layer number
cp -r "<universal_context>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template" \
  "layer_N_feature_<name>"

# Update all numbers inside from 2 to N
# Update status_N.json with appropriate layer number
```

**For Components:**
```bash
# Copy component template
cp -r "<universal_context>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/3_component_template" \
  "layer_N_component_<name>"

# Update all numbers inside from 3 to N
# Update status_N.json with appropriate layer number
```

<!-- section_id: "2d762804-e487-4056-b044-dbf3cf87115f" -->
### Automated Creation Script Pattern

```bash
#!/bin/bash
# create_layer.sh <parent_path> <type> <layer_num> <name>

PARENT_PATH=$1
TYPE=$2  # "feature" or "component"
LAYER_NUM=$3
NAME=$4

# Determine template based on type
if [ "$TYPE" = "feature" ]; then
    TEMPLATE="2_feature_template"
    OLD_NUM=2
else
    TEMPLATE="3_component_template"
    OLD_NUM=3
fi

# Copy template
cp -r "<universal_context>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/$TEMPLATE" \
  "$PARENT_PATH/layer_${LAYER_NUM}_${TYPE}_${NAME}"

# Navigate and update numbers
cd "$PARENT_PATH/layer_${LAYER_NUM}_${TYPE}_${NAME}"

# Rename directories (recursively update $OLD_NUM to $LAYER_NUM)
find . -depth -name "layer_${OLD_NUM}*" -execdir bash -c \
  'mv "$1" "${1//layer_'$OLD_NUM'/layer_'$LAYER_NUM'}"' _ {} \;

# Update file contents
find . -type f -exec sed -i "s/layer_${OLD_NUM}_/layer_${LAYER_NUM}_/g" {} +
find . -type f -exec sed -i "s/stage_${OLD_NUM}\./stage_${LAYER_NUM}./g" {} +
find . -type f -exec sed -i "s/status_${OLD_NUM}/status_${LAYER_NUM}/g" {} +

echo "Created layer_${LAYER_NUM}_${TYPE}_${NAME}"
```

---

<!-- section_id: "0a014671-d80b-4537-a516-b5b2fe50bc9b" -->
## Status Tracking at All Levels

Each layer maintains its own `status_N.json` inside `layer_N/layer_N_99_stages/`:

```json
{
  "layer": N,
  "type": "feature",
  "name": "<name>",
  "parent": "layer_<N-1>_<type>_<parent_name>",
  "current_stage": "stage_N.04_development",
  "last_updated": "2026-01-08",
  "stages": {
    "stage_N.01_instructions": "completed",
    "stage_N.02_planning": "completed",
    "stage_N.03_design": "completed",
    "stage_N.04_development": "in_progress",
    "stage_N.05_testing": "not_started",
    "stage_N.06_criticism": "not_started",
    "stage_N.07_fixing": "not_started",
    "stage_N.09_archives": "not_started"
  },
  "sub_features": [
    "layer_<N+1>_feature_<name1>",
    "layer_<N+1>_feature_<name2>"
  ],
  "components": [
    "layer_<N+1>_component_<name1>"
  ],
  "notes": "..."
}
```

---

<!-- section_id: "4f8709a2-0769-4ba8-8f65-ac89b58fc092" -->
## Benefits of Flexible Layering

1. **Unlimited Organization:** Break down topics to any level of detail needed
2. **Natural Hierarchy:** Mirrors how knowledge is actually structured
3. **Consistent Pattern:** Same structure at every level makes it predictable
4. **Scalable:** Works for simple projects (2-3 layers) or complex ones (7+ layers)
5. **Context Preservation:** Each level maintains its own context and status
6. **Tool Integration:** Proactor AI transcripts and Excalidraw diagrams can be organized at any depth
7. **Clear Separation:** Layer grouping clearly separates entity internals from nested content

---

<!-- section_id: "c445a479-dc41-4042-85bd-881d1db0ea5d" -->
## Integration with Learning Tools

<!-- section_id: "05ee9257-247b-42fd-a8d7-13ddf12a5333" -->
### Proactor AI Placement

Store lecture transcripts at the **most specific** applicable layer:

- General derivatives lecture -> `layer_2_feature_derivatives/layer_2/layer_2_99_stages/stage_2.04_development/hand_off_documents/`
- Power rule specific lecture -> `layer_3_sub_feature_power_rule/layer_3/layer_3_99_stages/stage_3.04_development/hand_off_documents/`
- Negative exponents discussion -> `layer_4_subx2_feature_negative_exponents/layer_4/layer_4_99_stages/stage_4.04_development/hand_off_documents/`

<!-- section_id: "20d4c484-e416-466a-b6bb-0f0f24037861" -->
### Excalidraw Placement

Store visual notes at the **layer where the work was done**:

- Derivatives overview diagram -> `layer_2_feature_derivatives/layer_2/layer_2_02_sub_layers/sub_layer_2.01_visual_notes/`
- Power rule examples -> `layer_3_sub_feature_power_rule/layer_3/layer_3_02_sub_layers/sub_layer_3.01_visual_notes/`
- Practice problem work -> `layer_4_subx2_component_practice_set_1/layer_4/layer_4_02_sub_layers/sub_layer_4.01_visual_notes/`

<!-- section_id: "70a22042-f344-4f61-a078-19ddffbcbf79" -->
### BYUI Math Page References

Document problem sources and answers at the appropriate component layer:

- `layer_4_subx2_component_practice_set_1/layer_4/layer_4_99_stages/stage_4.05_testing/hand_off_documents/byui_math_problems.md`

---

<!-- section_id: "cebf930a-be74-46bf-a219-4b1fc6f339e3" -->
## Quick Reference

<!-- section_id: "5959b207-4f55-4f34-8288-372593ba8bc0" -->
### Same-Type Nesting Rules (CRITICAL)

| Context | Features Are | Components Are |
|---------|-------------|----------------|
| Project | `features` | `components` |
| Sub_project | `features` | `components` |
| Sub*N_project | `features` | `components` |
| Feature | `sub_features` | `sub_components` |
| Sub_feature | `subx2_features` | `subx2_components` |
| Component | N/A | `sub_components` |

**Rule:** "sub" prefix ONLY for same-type nesting (project->project, feature->feature, component->component)

<!-- section_id: "966ac905-0e47-4835-918f-04f12db0c696" -->
### Layer Grouping Quick Reference

| Folder | Contains | Purpose |
|--------|----------|---------|
| `layer_N/` | Internals | Manager, handoffs, sub_layers, stages |
| `layer_N+1/` | Nested content | Sub*X_projects, features, components |

<!-- section_id: "5270513d-6b82-4092-854f-bc3f401f55ad" -->
### Maximum Flexibility Rules

1. Projects/Sub_projects contain `features/` and `components/` (NOT sub_*)
2. Features contain `sub_features/` and `sub_components/`
3. Components contain `sub_components/`
4. Same-type nesting increases depth: `sub`, `subx2`, `subx3`...
5. Layer number always indicates depth in hierarchy tree
6. Each layer follows the same structural pattern
7. Entity internals in `layer_N/`, nested content in `layer_N+1/`

<!-- section_id: "a0fc63df-4e76-4cf7-9338-881a15334b5e" -->
### Recommended Depth Guidelines

While **unlimited depth is supported**, consider these practical guidelines:

- **Layers 2-3:** Most common use (topic -> subtopic)
- **Layers 4-5:** Detailed breakdown (specific concepts -> examples)
- **Layers 6+:** Very specific (individual problems, edge cases)
- **Practical limit:** 7-8 layers is usually sufficient for even complex topics

**Remember:** Create depth only when it helps organize and clarify!

---

**Location:** `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/FLEXIBLE_LAYERING_SYSTEM.md`
**Last Updated:** 2026-01-14
**Version:** 4.0 - Layer Grouping Convention
