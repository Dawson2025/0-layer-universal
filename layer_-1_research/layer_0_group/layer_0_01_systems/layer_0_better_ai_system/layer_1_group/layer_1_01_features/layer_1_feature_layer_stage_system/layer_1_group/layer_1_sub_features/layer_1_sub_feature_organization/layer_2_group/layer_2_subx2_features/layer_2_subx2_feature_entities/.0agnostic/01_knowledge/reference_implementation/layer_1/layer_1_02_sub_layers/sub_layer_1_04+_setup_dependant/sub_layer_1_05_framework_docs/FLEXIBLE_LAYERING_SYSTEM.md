---
resource_id: "f5ddb1bc-13ab-4bab-9200-26e1535b8f96"
resource_type: "knowledge"
resource_name: "FLEXIBLE_LAYERING_SYSTEM"
---
# Flexible N-Layer Architecture System

**Purpose:** This document defines the flexible, arbitrarily-nested layer system that supports unlimited depth of features and components.

**Location:** `0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/FLEXIBLE_LAYERING_SYSTEM.md`

**Last Updated:** 2026-01-14
**Version:** 4.0 - Layer Grouping Convention

---

<!-- section_id: "d25cfa79-8e68-4aa6-8633-a3ab863750c4" -->
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

<!-- section_id: "120a2bbd-fb2d-486e-a5c1-f5063faaf62c" -->
## Layer Grouping Pattern

<!-- section_id: "0304980a-a0d2-4eb1-85d7-5c09b734f601" -->
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

<!-- section_id: "a83f2f05-69ef-46aa-a20f-dcd801539713" -->
### Why Layer Grouping?

1. **Clear separation**: Entity internals vs nested content are visually distinct
2. **Predictable navigation**: Always know where to find management vs content
3. **Consistent pattern**: Same structure at every depth level
4. **Easy scanning**: All internals grouped, all nested items grouped

---

<!-- section_id: "11917b1e-cfb7-485b-ab36-2ac5d1b34797" -->
## Layer Numbering System

<!-- section_id: "c80f83d8-a189-4870-ae86-c9c878d326f5" -->
### Fixed Layers (0-1)

- **Layer 0:** Universal - Applies to all projects
- **Layer 1:** Project - Project-specific context

<!-- section_id: "38157a25-7987-404b-8077-81a8f2d07a79" -->
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

<!-- section_id: "c29766db-0ec9-404d-a65f-a53bd7e0d6a5" -->
## Directory Structure Pattern

<!-- section_id: "fa66ff4a-5f9c-4070-ad66-a30f3c971bea" -->
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
│       └── status_1.json                        # Status tracker
└── layer_2/                                     # Nested content
    ├── layer_2_sub_projects/                    # Sub-projects (same-type nesting)
    │   └── layer_2_sub_project_<name>/
    ├── layer_2_features/                        # Features (NOT sub_features!)
    │   └── layer_2_feature_<name>/
    └── layer_2_components/                      # Components (NOT sub_components!)
        └── layer_2_component_<name>/
```

<!-- section_id: "f9c4b9c8-e38b-48e3-aef6-ac61fa23d8fe" -->
### Pattern for Feature/Sub_Feature/Sub*N_Feature

Features contain **sub_features** and **sub_components** (because feature inside feature = sub_feature):

```
layer_2_feature_<name>/                          # OR layer_3_subx3_feature_<name>/ OR layer_4_subx2_feature_<name>/
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
    ├── layer_3_subx3_features/                    # Sub-features (feature inside feature)
    │   └── layer_3_subx3_feature_<name>/
    └── layer_3_sub_components/                  # Sub-components (component inside feature context)
        └── layer_3_sub_component_<name>/
```

<!-- section_id: "62da8a97-43dd-44e9-8d2b-a9afc8bf6078" -->
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

<!-- section_id: "e2f7f51b-35dd-497c-93f7-9cc8600e773b" -->
## Naming Conventions

<!-- section_id: "8515cb58-06a1-42b3-a712-e52c7c761031" -->
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

<!-- section_id: "528e8f5b-0eda-4e86-857c-7662b42568c7" -->
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

<!-- section_id: "7b128c34-58a5-49b6-a858-251eebe18085" -->
### Project Naming

```
layer_1_project_<name>/
layer_2_sub_project_<name>/
layer_3_subx2_project_<name>/
layer_N_sub*<N-1>_project_<name>/
```

<!-- section_id: "d6c43f52-fbce-4d28-bed7-4b9b524b395c" -->
### Feature Naming

**In a project/sub_project (no "sub" prefix):**
```
layer_2_feature_<name>/        # Feature in project
layer_3_feature_<name>/        # Feature in sub_project
layer_4_feature_<name>/        # Feature in subx2_project
```

**In another feature (uses "sub" prefix):**
```
layer_3_subx3_feature_<name>/    # Feature inside a feature
layer_4_subx2_feature_<name>/  # Feature inside a sub_feature
layer_5_subx3_feature_<name>/  # Feature inside a subx2_feature
```

**Examples:**
- `layer_2_feature_in_class_work/` - Feature directly in project (depth 2)
- `layer_3_feature_machine_learning/` - Feature in sub_project (depth 3, still "feature" not "sub_feature")
- `layer_3_subx3_feature_derivatives/` - Sub-feature inside a feature (depth 3)
- `layer_4_subx2_feature_power_rule/` - Sub*2-feature inside a sub_feature (depth 4)

<!-- section_id: "b43f50a4-a3c0-4d76-aa33-2b04c5180552" -->
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

<!-- section_id: "0555d6b1-7876-4006-a09e-32e94e19627d" -->
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

<!-- section_id: "9034e210-e865-449a-bfcc-f6badcfb6cf7" -->
## Real-World Example: Applied Calculus

<!-- section_id: "5d4c20f9-445b-4a6e-84d8-120b5609db30" -->
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
                └── layer_3_subx3_features/
                    └── layer_3_subx3_feature_derivatives/     # Main topic (depth 3)
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

<!-- section_id: "7a257f49-81c7-4387-97c2-22458639ce8a" -->
## Applied Calculus Use Case

<!-- section_id: "3805bc8e-744e-4482-a8ba-d5973c343655" -->
### Your Classroom Workflow

**During lecture with BYUI Math page, Excalidraw, and Proactor AI:**

1. **Container Feature:** In-Class Work -> Create `layer_2_feature_in_class_work/`

2. **Main Topic:** Derivatives
   - Create: `layer_2_feature_in_class_work/layer_3/layer_3_subx3_features/layer_3_subx3_feature_derivatives/`
   - Save Proactor AI transcript in: `layer_3/layer_3_99_stages/stage_3.04_development/hand_off_documents/`
   - Save overview diagrams in: `layer_3/layer_3_02_sub_layers/sub_layer_3.01_visual_notes/`

3. **Subtopic in lecture:** Power Rule
   - Create: `layer_3_subx3_feature_derivatives/layer_4/layer_4_subx2_features/layer_4_subx2_feature_power_rule/`
   - Save Proactor AI transcript in: `layer_4/layer_4_99_stages/stage_4.04_development/hand_off_documents/`
   - Save Excalidraw work in: `layer_4/layer_4_02_sub_layers/sub_layer_4.01_visual_notes/`

4. **Daily Practice Problems from BYUI Math page**
   - Create: `layer_4_subx2_feature_power_rule/layer_5/layer_5_subx3_components/layer_5_subx3_component_2026_01_09_class/`
   - Show your work in Excalidraw, save to: `layer_5/layer_5_02_sub_layers/sub_layer_5.01_visual_notes/excalidraw/`
   - Document problems from BYUI Math page in: `layer_5/layer_5_99_stages/stage_5.05_testing/hand_off_documents/`

---

<!-- section_id: "99721310-d3c0-4cbc-a0cb-a53a136276e1" -->
## When to Create Each Layer Type

<!-- section_id: "0e2ca3de-8106-4adc-aa6b-20ee3c7f14b6" -->
### Features (Topics/Concepts)

Create a **feature** when you have:
- A distinct topic or concept to learn
- Content that benefits from organized study stages
- Subtopics that need further breakdown

**In Project/Sub_Project context (uses "feature"):**
- `layer_2_feature_derivatives/` - Feature in project
- `layer_3_feature_machine_learning/` - Feature in sub_project

**In Feature context (uses "sub_feature"):**
- `layer_3_subx3_feature_power_rule/` - Sub-feature inside a feature
- `layer_4_subx2_feature_negative_exponents/` - Sub*2-feature inside a sub_feature

<!-- section_id: "34f302fd-62ad-41d2-be5a-5903cdb0e648" -->
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

<!-- section_id: "ed63e73f-2278-433d-9529-94a573a15505" -->
## Navigation Patterns

<!-- section_id: "97075760-dc03-4e46-8a86-5fcd38d08c5b" -->
### Depth-First Navigation (Feature inside Feature)

```bash
# From project context root
cd layer_2/layer_2_features/layer_2_feature_derivatives/

# Navigate to entity internals
cd layer_2/layer_2_00_ai_manager_system/

# Navigate to sub-feature (feature inside feature uses "sub")
cd ../../layer_3/layer_3_subx3_features/layer_3_subx3_feature_power_rule/

# Navigate to subx2-feature (feature inside sub_feature)
cd layer_4/layer_4_subx2_features/layer_4_subx2_feature_negative_exponents/

# Navigate to subx2-component at this level (component inside feature context)
cd ../layer_4_subx2_components/layer_4_subx2_component_practice_set_1/
```

<!-- section_id: "89f21f93-38e4-43d9-9b7f-0ef67f1b05c4" -->
### Breadth Navigation (Siblings at Same Level)

```bash
# From a layer 3 sub_feature (inside a feature)
cd layer_3/layer_3_subx3_features/layer_3_subx3_feature_power_rule/

# Move to sibling sub_feature at same level
cd ../layer_3_subx3_feature_product_rule/

# Move to another sibling
cd ../layer_3_subx3_feature_chain_rule/
```

<!-- section_id: "d901ca7e-92cb-44b5-8006-ffac003bcad4" -->
### Navigation in Sub_Project Context (uses features, not sub_features)

```bash
# From a sub_project
cd layer_2_sub_project_classes/

# Navigate to feature (NOT sub_feature, because different type)
cd layer_3/layer_3_features/layer_3_feature_machine_learning/

# Navigate to component (NOT sub_component, because different type)
cd ../layer_3_components/layer_3_component_web_app/
```

<!-- section_id: "11070223-f752-40d8-971f-9419c38dd16a" -->
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

<!-- section_id: "755b33c0-5f38-401a-9364-9543bccd5c71" -->
### Upward Navigation (Parent Layers)

```bash
# From layer 4 feature, go to parent layer 3 feature
cd ../../../../  # Up to layer_3_subx3_feature_power_rule/

# From any depth, go to project root
cd <project_root>/0_context/0_context/
```

---

<!-- section_id: "6f69965b-ef16-43b6-a2e4-5493658513f6" -->
## Creating New Layers

<!-- section_id: "ae176e43-5da1-49cc-8965-5c576816454a" -->
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

<!-- section_id: "d8d8226e-b7ff-4ada-9398-d5ef7bc49267" -->
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

<!-- section_id: "0d3f022c-2875-4af6-88af-942e82a279e8" -->
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

<!-- section_id: "2a438185-636a-474c-910c-0e65a9b00ef0" -->
## Benefits of Flexible Layering

1. **Unlimited Organization:** Break down topics to any level of detail needed
2. **Natural Hierarchy:** Mirrors how knowledge is actually structured
3. **Consistent Pattern:** Same structure at every level makes it predictable
4. **Scalable:** Works for simple projects (2-3 layers) or complex ones (7+ layers)
5. **Context Preservation:** Each level maintains its own context and status
6. **Tool Integration:** Proactor AI transcripts and Excalidraw diagrams can be organized at any depth
7. **Clear Separation:** Layer grouping clearly separates entity internals from nested content

---

<!-- section_id: "803abdc6-c284-4d5b-9713-0ad16fedeec1" -->
## Integration with Learning Tools

<!-- section_id: "741743f4-9ac4-4c72-9180-a76af8abc93f" -->
### Proactor AI Placement

Store lecture transcripts at the **most specific** applicable layer:

- General derivatives lecture -> `layer_2_feature_derivatives/layer_2/layer_2_99_stages/stage_2.04_development/hand_off_documents/`
- Power rule specific lecture -> `layer_3_subx3_feature_power_rule/layer_3/layer_3_99_stages/stage_3.04_development/hand_off_documents/`
- Negative exponents discussion -> `layer_4_subx2_feature_negative_exponents/layer_4/layer_4_99_stages/stage_4.04_development/hand_off_documents/`

<!-- section_id: "a5603f74-958d-4220-866a-daf1eee5d409" -->
### Excalidraw Placement

Store visual notes at the **layer where the work was done**:

- Derivatives overview diagram -> `layer_2_feature_derivatives/layer_2/layer_2_02_sub_layers/sub_layer_2.01_visual_notes/`
- Power rule examples -> `layer_3_subx3_feature_power_rule/layer_3/layer_3_02_sub_layers/sub_layer_3.01_visual_notes/`
- Practice problem work -> `layer_4_subx2_component_practice_set_1/layer_4/layer_4_02_sub_layers/sub_layer_4.01_visual_notes/`

<!-- section_id: "fbd6caa4-4c2b-4b5e-81f7-c5ea012cb751" -->
### BYUI Math Page References

Document problem sources and answers at the appropriate component layer:

- `layer_4_subx2_component_practice_set_1/layer_4/layer_4_99_stages/stage_4.05_testing/hand_off_documents/byui_math_problems.md`

---

<!-- section_id: "26a13f81-1c21-4aad-bf00-54ccae3db490" -->
## Quick Reference

<!-- section_id: "b4726c89-4fc3-4006-af35-f7dfb84bec6d" -->
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

<!-- section_id: "d1390f87-e730-4efb-9364-21bbe64370e8" -->
### Layer Grouping Quick Reference

| Folder | Contains | Purpose |
|--------|----------|---------|
| `layer_N/` | Internals | Manager, handoffs, sub_layers, stages |
| `layer_N+1/` | Nested content | Sub*X_projects, features, components |

<!-- section_id: "50b18d11-1d29-4272-a49a-85b5ffb59eed" -->
### Maximum Flexibility Rules

1. Projects/Sub_projects contain `features/` and `components/` (NOT sub_*)
2. Features contain `sub_features/` and `sub_components/`
3. Components contain `sub_components/`
4. Same-type nesting increases depth: `sub`, `subx2`, `subx3`...
5. Layer number always indicates depth in hierarchy tree
6. Each layer follows the same structural pattern
7. Entity internals in `layer_N/`, nested content in `layer_N+1/`

<!-- section_id: "4e1b6836-5117-4a57-90b1-16a1db8c6801" -->
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
