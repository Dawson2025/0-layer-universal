# Flexible N-Layer Architecture System

**Purpose:** This document defines the flexible, arbitrarily-nested layer system that supports unlimited depth of features and components.

**Location:** `0_ai_context/0_context/0.00_layer_stage_framework/FLEXIBLE_LAYERING_SYSTEM.md`

**Last Updated:** 2026-01-09
**Version:** 2.2 - Sub Naming Convention

---

## 🎯 Overview

The flexible layering system allows **arbitrary nesting** of features and components to any depth required by your project's complexity, using the **sub naming convention** to clearly indicate nesting depth.

**Key Principles:**
1. **Layer numbers indicate depth**, not fixed types
2. **Sub naming shows nesting level**: `sub`, `sub*2`, `sub*3`, ... `sub*n`
3. **Any layer can contain sub-features AND sub-components**
4. **Infinite nesting** - create as many levels as needed
5. **Each layer follows the same structure** (manager, handoffs, sub-layers, stages)
6. **Every layer has sub_layers**: ALL features, sub_features, components, and sub_components have `<N>.02_sub_layers/` with 12 content slots
7. **Consistent numbering** shows position in hierarchy

---

## 📐 Layer Numbering System

### Fixed Layers (0-1)

- **Layer 0:** Universal - Applies to all projects
- **Layer 1:** Project - Project-specific context

### Flexible Layers (2-N)

Starting at Layer 2, the system supports **arbitrary depth** using **sub naming convention**:

- **Layer 2:** Top-level `features` and `components`
- **Layer 3:** `sub_features` and `sub_components` (1st level of nesting)
- **Layer 4:** `sub*2_features` and `sub*2_components` (2nd level of nesting)
- **Layer 5:** `sub*3_features` and `sub*3_components` (3rd level of nesting)
- **Layer N:** `sub*n_features` and `sub*n_components` (nth level of nesting)

**The layer number = depth in the hierarchy tree**

**Mini naming indicates nesting depth:**
- No "sub" prefix = Layer 2 (top-level)
- `sub` = Layer 3 (1 level deep)
- `sub*2` = Layer 4 (2 levels deep)
- `sub*n` = Layer N (n-2 levels deep)

---

## 🌳 Directory Structure Pattern

### Pattern for Layer 2 (Top-Level)

```
layer_2_feature_<name>/                      # OR layer_2_component_<name>/
├── 2.00_ai_manager_system/                  # Manager for this layer
├── 2.01_manager_handoff_documents/          # Communication
│   ├── 2.00_to_universal/                   # Reports up
│   └── 2.01_to_specific/                    # Context down
├── 2.02_sub_layers/                         # Content slots
│   ├── sub_layer_2.01_basic_prompts_throughout/
│   ├── sub_layer_2.02_knowledge/
│   ├── ... (2.01 through 2.12)
│   └── sub_layer_2.12_agent_setup/
├── 2.99_stages/                             # Workflow stages
│   ├── stage_2.01_instructions/
│   ├── ... (2.01 through 2.08)
│   ├── stage_2.08_archives/
│   └── status_2.json                        # Status tracker
├── layer_3_sub_features/                   # Sub-features (optional)
│   ├── README.md
│   └── layer_3_sub_feature_<name>/         # Recursive structure
└── layer_3_sub_components/                 # Sub-components (optional)
    ├── README.md
    └── layer_3_sub_component_<name>/       # Recursive structure
```

### Pattern for Layer 3+ (Nested Layers)

```
layer_N_sub*x_feature_<name>/               # OR layer_N_sub*x_component_<name>/
├── N.00_ai_manager_system/                  # Manager for this layer
├── N.01_manager_handoff_documents/          # Communication
│   ├── N.00_to_universal/                   # Reports up
│   └── N.01_to_specific/                    # Context down
├── N.02_sub_layers/                         # Content slots
│   ├── sub_layer_N.01_basic_prompts_throughout/
│   ├── sub_layer_N.02_knowledge/
│   ├── ... (N.01 through N.12)
│   └── sub_layer_N.12_agent_setup/
├── N.99_stages/                             # Workflow stages
│   ├── stage_N.01_instructions/
│   ├── ... (N.01 through N.08)
│   ├── stage_N.08_archives/
│   └── status_N.json                        # Status tracker
├── layer_N+1_sub*x+1_features/             # Deeper sub-features (optional)
│   ├── README.md
│   └── layer_N+1_sub*x+1_feature_<name>/   # Recursive structure
└── layer_N+1_sub*x+1_components/           # Deeper sub-components (optional)
    ├── README.md
    └── layer_N+1_sub*x+1_component_<name>/ # Recursive structure
```

**Key Points:**
- **Every layer** follows this structure
- **Layer 2** uses `layer_3_sub_features/` and `layer_3_sub_components/` (no "sub" prefix at Layer 2 itself)
- **Layer 3+** uses `sub`, `sub*2`, `sub*3`, etc. in both folder names AND item names
- **Recursion:** Each nested feature/component follows the same pattern

---

## 🔢 Naming Conventions

### Feature Naming

**Layer 2 (Top-Level):**
```
layer_2_feature_<name>/
```

**Layer 3+ (Nested):**
```
layer_3_sub_feature_<name>/
layer_4_sub*2_feature_<name>/
layer_5_sub*3_feature_<name>/
layer_N_sub*n_feature_<name>/
```

**Examples:**
- `layer_2_feature_in_class_work/` - Top-level feature (depth 2)
- `layer_3_sub_feature_derivatives/` - Sub-feature (depth 3, 1 level deep)
- `layer_4_sub*2_feature_power_rule/` - Mini*2-feature (depth 4, 2 levels deep)
- `layer_5_sub*3_feature_negative_exponents/` - Mini*3-feature (depth 5, 3 levels deep)

### Component Naming

**Layer 2 (Top-Level):**
```
layer_2_component_<name>/
```

**Layer 3+ (Nested):**
```
layer_3_sub_component_<name>/
layer_4_sub*2_component_<name>/
layer_5_sub*3_component_<name>/
layer_N_sub*n_component_<name>/
```

**Examples:**
- `layer_3_sub_component_worksheet_1/` - Sub-component (depth 3)
- `layer_4_sub*2_component_practice_set/` - Mini*2-component (depth 4)
- `layer_5_sub*3_component_2026_01_09_class/` - Mini*3-component (depth 5)

### Directory Naming Within Layers

**Manager and Handoffs:**
- `N.00_ai_manager_system/`
- `N.01_manager_handoff_documents/`
  - `N.00_to_universal/`
  - `N.01_to_specific/`

**Sub-layers (Every Layer Has These):**
- `N.02_sub_layers/`
  - `sub_layer_N.01_<name>/` through `sub_layer_N.12_<name>/`
  - **Purpose**: Specialized content at this layer level
  - **Common uses**:
    - `sub_layer_N.01_visual_notes/excalidraw/` - Excalidraw diagrams
    - `sub_layer_N.02_knowledge/` - Documentation, references
    - `sub_layer_N.03_tools/` - Scripts, utilities
    - `sub_layer_N.04_resources/` - Files, assets
  - **Available in**: ALL features, sub_features, components, sub_components

**Stages:**
- `N.99_stages/`
  - `stage_N.01_instructions/`
  - ... through `stage_N.08_archives/`
  - `status_N.json`

---

## 📚 Real-World Example: Applied Calculus

### Scenario: Organizing in-class work with topics and daily components

```
layer_1_project/                                 # Applied Calculus Project (depth 1)
└── layer_2_features/                            # Features directory
    └── layer_2_feature_in_class_work/           # Container feature (depth 2)
        ├── 2.00_ai_manager_system/
        ├── 2.01_manager_handoff_documents/
        ├── 2.02_sub_layers/
        │   └── sub_layer_2.01_visual_notes/    # General class notes
        ├── 2.99_stages/
        │   └── status_2.json
        └── layer_3_sub_features/               # Sub-features folder
            └── layer_3_sub_feature_derivatives/      # Main topic (depth 3)
                ├── 3.00_ai_manager_system/
                ├── 3.02_sub_layers/
                │   └── sub_layer_3.01_visual_notes/  # Derivatives overview diagrams
                ├── 3.99_stages/
                │   ├── stage_3.04_development/
                │   │   └── hand_off_documents/
                │   │       └── proactor_lecture_2026-01-09_derivatives.md
                │   └── status_3.json
                └── layer_4_sub*2_features/          # Mini*2-features folder
                    └── layer_4_sub*2_feature_power_rule/    # Subtopic (depth 4)
                        ├── 4.00_ai_manager_system/
                        ├── 4.02_sub_layers/
                        │   └── sub_layer_4.01_visual_notes/  # Power rule specific diagrams
                        ├── 4.99_stages/
                        │   └── status_4.json
                        ├── layer_5_sub*3_features/      # Mini*3-features folder
                        │   └── layer_5_sub*3_feature_negative_exponents/  # (depth 5)
                        │       ├── 5.00_ai_manager_system/
                        │       ├── 5.02_sub_layers/
                        │       └── 5.99_stages/
                        │           └── status_5.json
                        └── layer_5_sub*3_components/    # Daily work folder
                            ├── layer_5_sub*3_component_2026_01_09_class/  # (depth 5)
                            │   ├── 5.00_ai_manager_system/
                            │   ├── 5.02_sub_layers/
                            │   │   └── sub_layer_5.01_visual_notes/
                            │   │       └── excalidraw/
                            │   │           ├── jan09_problem_1.excalidraw
                            │   │           └── jan09_problem_2.excalidraw
                            │   └── 5.99_stages/
                            │       └── stage_5.05_testing/
                            │           └── hand_off_documents/
                            │               └── byui_math_problems_jan09.md
                            └── layer_5_sub*3_component_2026_01_11_class/  # (depth 5)
                                └── ...
```

---

## 🎓 Applied Calculus Use Case

### Your Classroom Workflow

**During lecture with BYUI Math page, Excalidraw, and Proactor AI:**

1. **Container Feature:** In-Class Work → Create `layer_2_feature_in_class_work/`

2. **Main Topic:** Derivatives
   - Create: `layer_2_feature_in_class_work/layer_3_sub_features/layer_3_sub_feature_derivatives/`
   - Save Proactor AI transcript in: `3.99_stages/stage_3.04_development/hand_off_documents/`
   - Save overview diagrams in: `3.02_sub_layers/sub_layer_3.01_visual_notes/`

3. **Subtopic in lecture:** Power Rule
   - Create: `layer_3_sub_feature_derivatives/layer_4_sub*2_features/layer_4_sub*2_feature_power_rule/`
   - Save Proactor AI transcript in: `4.99_stages/stage_4.04_development/hand_off_documents/`
   - Save Excalidraw work in: `4.02_sub_layers/sub_layer_4.01_visual_notes/`

4. **Daily Practice Problems from BYUI Math page**
   - Create: `layer_4_sub*2_feature_power_rule/layer_5_sub*3_components/layer_5_sub*3_component_2026_01_09_class/`
   - Show your work in Excalidraw, save to: `5.02_sub_layers/sub_layer_5.01_visual_notes/excalidraw/`
   - Document problems from BYUI Math page in: `5.99_stages/stage_5.05_testing/hand_off_documents/`

---

## 🔍 When to Create Each Layer Type

### Features (Topics/Concepts)

Create a **feature** when you have:
- A distinct topic or concept to learn
- Content that benefits from organized study stages
- Subtopics that need further breakdown

**Examples:**
- Layer 2: `layer_2_feature_derivatives/` (main calculus topic)
- Layer 3: `layer_3_feature_power_rule/` (specific derivative rule)
- Layer 4: `layer_4_feature_negative_exponents/` (specific case of power rule)
- Layer 5: `layer_5_feature_minus_two_exponent/` (even more specific example)

### Components (Work/Artifacts)

Create a **component** when you have:
- Practice problems to work through
- Homework assignments
- Worksheets from BYUI Math page
- Specific examples or exercises
- Exam prep materials

**Examples:**
- Layer 3: `layer_3_component_homework_1/` (homework for derivatives)
- Layer 4: `layer_4_component_practice_set_1/` (practice for power rule)
- Layer 5: `layer_5_component_problem_7/` (single complex problem)

---

## 📋 Navigation Patterns

### Depth-First Navigation

```bash
# From project context root
cd layer_2_features/layer_2_feature_derivatives/

# Navigate to sub-feature
cd layer_3_features/layer_3_feature_power_rule/

# Navigate to sub-sub-feature
cd layer_4_features/layer_4_feature_negative_exponents/

# Navigate to component at this level
cd ../../layer_4_components/layer_4_component_practice_set_1/
```

### Breadth Navigation (Siblings at Same Level)

```bash
# From a layer 3 feature
cd layer_3_features/layer_3_feature_power_rule/

# Move to sibling feature at same level
cd ../layer_3_feature_product_rule/

# Move to another sibling
cd ../layer_3_feature_chain_rule/
```

### Upward Navigation (Parent Layers)

```bash
# From layer 4 feature, go to parent layer 3 feature
cd ../../../  # Up to layer_3_feature_power_rule/

# From any depth, go to project root
cd <project_root>/0_context/0_context/
```

---

## 🛠️ Creating New Layers

### Template Pattern

All layers N ≥ 2 use the same template structure, just with different numbers.

**For Features:**
```bash
# Copy template and rename to appropriate layer number
cp -r "<universal_context>/0.00_layer_stage_framework/2_feature_template" \
  "layer_N_feature_<name>"

# Update all numbers inside from 2 to N
# Update status_N.json with appropriate layer number
```

**For Components:**
```bash
# Copy component template
cp -r "<universal_context>/0.00_layer_stage_framework/3_component_template" \
  "layer_N_component_<name>"

# Update all numbers inside from 3 to N
# Update status_N.json with appropriate layer number
```

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
cp -r "<universal_context>/0.00_layer_stage_framework/$TEMPLATE" \
  "$PARENT_PATH/layer_${LAYER_NUM}_${TYPE}_${NAME}"

# Navigate and update numbers
cd "$PARENT_PATH/layer_${LAYER_NUM}_${TYPE}_${NAME}"

# Rename directories (recursively update $OLD_NUM to $LAYER_NUM)
find . -depth -name "${OLD_NUM}.*" -execdir bash -c \
  'mv "$1" "${1//'$OLD_NUM'\./'$LAYER_NUM'.}"' _ {} \;

# Update file contents
find . -type f -exec sed -i "s/layer_${OLD_NUM}_/layer_${LAYER_NUM}_/g" {} +
find . -type f -exec sed -i "s/stage_${OLD_NUM}\./stage_${LAYER_NUM}./g" {} +
find . -type f -exec sed -i "s/status_${OLD_NUM}/status_${LAYER_NUM}/g" {} +

echo "Created layer_${LAYER_NUM}_${TYPE}_${NAME}"
```

---

## 📊 Status Tracking at All Levels

Each layer maintains its own `status_N.json`:

```json
{
  "layer": N,
  "type": "feature",  // or "component"
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
    "stage_N.08_archives": "not_started"
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

## 🎯 Benefits of Flexible Layering

1. **Unlimited Organization:** Break down topics to any level of detail needed
2. **Natural Hierarchy:** Mirrors how knowledge is actually structured
3. **Consistent Pattern:** Same structure at every level makes it predictable
4. **Scalable:** Works for simple projects (2-3 layers) or complex ones (7+ layers)
5. **Context Preservation:** Each level maintains its own context and status
6. **Tool Integration:** Proactor AI transcripts and Excalidraw diagrams can be organized at any depth

---

## 🔗 Integration with Learning Tools

### Proactor AI Placement

Store lecture transcripts at the **most specific** applicable layer:

- General derivatives lecture → `layer_2_feature_derivatives/2.99_stages/stage_2.04_development/hand_off_documents/`
- Power rule specific lecture → `layer_3_feature_power_rule/3.99_stages/stage_3.04_development/hand_off_documents/`
- Negative exponents discussion → `layer_4_feature_negative_exponents/4.99_stages/stage_4.04_development/hand_off_documents/`

### Excalidraw Placement

Store visual notes at the **layer where the work was done**:

- Derivatives overview diagram → `layer_2_feature_derivatives/2.02_sub_layers/sub_layer_2.01_visual_notes/`
- Power rule examples → `layer_3_feature_power_rule/3.02_sub_layers/sub_layer_3.01_visual_notes/`
- Practice problem work → `layer_4_component_practice_set_1/4.02_sub_layers/sub_layer_4.01_visual_notes/`

### BYUI Math Page References

Document problem sources and answers at the appropriate component layer:

- `layer_4_component_practice_set_1/4.99_stages/stage_4.05_testing/hand_off_documents/byui_math_problems.md`

---

## 📝 Quick Reference

### Maximum Flexibility Rules

1. ✅ Features can contain sub-features to any depth
2. ✅ Features can contain components at any level
3. ✅ Components can contain sub-components to any depth
4. ✅ Any layer N can have both `layer_N+1_features/` AND `layer_N+1_components/` directories
5. ✅ Layer number always indicates depth in hierarchy tree
6. ✅ Each layer follows the same structural pattern

### Recommended Depth Guidelines

While **unlimited depth is supported**, consider these practical guidelines:

- **Layers 2-3:** Most common use (topic → subtopic)
- **Layers 4-5:** Detailed breakdown (specific concepts → examples)
- **Layers 6+:** Very specific (individual problems, edge cases)
- **Practical limit:** 7-8 layers is usually sufficient for even complex topics

**Remember:** Create depth only when it helps organize and clarify!

---

**Location:** `C:\Users\Dawson\dawson-workspace\code\0_ai_context\0_context\0.00_layer_stage_framework\FLEXIBLE_LAYERING_SYSTEM.md`
**Last Updated:** 2026-01-08
**Version:** 2.0 - Arbitrary Nesting Support
