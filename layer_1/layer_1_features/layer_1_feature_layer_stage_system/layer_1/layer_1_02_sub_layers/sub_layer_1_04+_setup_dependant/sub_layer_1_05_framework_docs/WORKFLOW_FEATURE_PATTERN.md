---
resource_id: "351adfab-22bd-431d-8161-8f5711d008bb"
resource_type: "document"
resource_name: "WORKFLOW_FEATURE_PATTERN"
---
# Workflow Feature Pattern

**Purpose:** Template and guide for creating "workflow features" with creation → production → results lifecycle.

**Based On:** PAC School DS250 patterns (assignments and coding challenges)

**Last Updated:** 2026-01-09

---

<!-- section_id: "9e06b52c-5d41-423f-8c60-666fb68bde79" -->
## 🎯 What is a Workflow Feature?

A **workflow feature** is used when you need to:
1. **Create/Develop** workflows or processes
2. **Store/Execute** validated workflows
3. **Track** results from workflow execution

**Key Characteristic:** Distinct phases that don't fit the standard 8-stage pattern.

---

<!-- section_id: "c6acea39-7f22-40c6-b07b-c3d2611e9e35" -->
## 📐 Standard Structure vs Workflow Feature

<!-- section_id: "a489fccc-2cfb-4fcb-b3c1-d47873d58ec4" -->
### Standard Feature
```
layer_<N>_feature_<name>/
├── <N>.00_ai_manager_system/
├── <N>.01_manager_handoff_documents/
├── <N>.02_sub_layers/
├── <N>.99_stages/                    # Single workflow: instructions → archives
├── layer_<N+1>_features/
└── layer_<N+1>_components/
```

**Good for:** Topics, learning, sequential work

<!-- section_id: "e0df6fb1-b0f4-4472-9639-4cc17249c15f" -->
### Workflow Feature
```
layer_<N>_feature_<name>/
├── <N>.00_ai_manager_system/
├── <N>.01_manager_handoff_documents/
├── <N>.02_sub_layers/
├── <N>.03_workflow_creation/         # PHASE 1: Create workflows
│   ├── <N>.00_ai_manager_system/
│   ├── <N>.01_manager_handoff_documents/
│   ├── <N>.02_sub_layers/
│   └── <N>.99_stages/                # Development stages
├── <N>.04_workflows/                 # PHASE 2: Production workflows
│   ├── workflow_1/
│   │   ├── workflow_<name>_v1.md
│   │   └── <N>.99_stages/            # Execution stages
│   └── workflow_2/
├── <N>.05_results/                   # PHASE 3: Output tracking
└── <N>.99_stages/                    # Optional: Feature-level stages
```

**Good for:** Workflow management, repeated processes, multi-phase work

---

<!-- section_id: "204e022f-5ac3-470c-a623-b2430c8fd842" -->
## 🏗️ Creating a Workflow Feature

<!-- section_id: "4ea0ae4a-19ac-4809-b7ff-4e47887ae09b" -->
### Step 1: Create Base Structure

```bash
#!/bin/bash
# create_workflow_feature.sh <layer_num> <feature_name>

LAYER=$1
NAME=$2
FEATURE_DIR="layer_${LAYER}_feature_${NAME}"

# Create base directories
mkdir -p "$FEATURE_DIR/${LAYER}.00_ai_manager_system"
mkdir -p "$FEATURE_DIR/${LAYER}.01_manager_handoff_documents/${LAYER}.00_to_universal"
mkdir -p "$FEATURE_DIR/${LAYER}.01_manager_handoff_documents/${LAYER}.01_to_specific"
mkdir -p "$FEATURE_DIR/${LAYER}.02_sub_layers"

# Create workflow creation directory (custom .03)
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.00_ai_manager_system"
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.01_manager_handoff_documents"
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.02_sub_layers"
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.99_stages"

# Create workflows directory (custom .04)
mkdir -p "$FEATURE_DIR/${LAYER}.04_workflows"

# Create results directory (custom .05)
mkdir -p "$FEATURE_DIR/${LAYER}.05_results"

# Create feature-level stages (standard .99)
mkdir -p "$FEATURE_DIR/${LAYER}.99_stages"

echo "Workflow feature created: $FEATURE_DIR"
```

<!-- section_id: "35c7905a-24c4-44e3-ad26-056d00842730" -->
### Step 2: Add README Documentation

```bash
cat > "$FEATURE_DIR/README.md" << 'EOF'
# Feature: <Feature Name>

## Purpose

This feature manages workflows for <purpose>.

## Directory Structure

```text
layer_<N>_feature_<name>/
├── README.md                          # This file
├── <N>.00_ai_manager_system/          # Feature-level manager
├── <N>.01_manager_handoff_documents/  # Feature-level handoffs
├── <N>.02_sub_layers/                 # Feature-level knowledge/tools
├── <N>.03_workflow_creation/          # PHASE 1: Develop workflows
│   ├── <N>.00_ai_manager_system/
│   ├── <N>.01_manager_handoff_documents/
│   ├── <N>.02_sub_layers/
│   └── <N>.99_stages/                 # Development stages
├── <N>.04_workflows/                  # PHASE 2: Production workflows
│   └── workflow_1/
│       ├── workflow_<name>_v1.md
│       └── <N>.99_stages/             # Execution stages
└── <N>.05_results/                    # PHASE 3: Output/results
```

## Workflow Lifecycle

### Phase 1: Creation (`.03_workflow_creation/`)

**Purpose:** Design, develop, and test workflows

**Stages:**
1. `stage_<N>.01_instructions` - Define workflow requirements
2. `stage_<N>.02_planning` - Plan workflow steps
3. `stage_<N>.03_design` - Design workflow structure
4. `stage_<N>.04_development` - Build and iterate
5. `stage_<N>.05_testing` - Test workflow
6. `stage_<N>.06_criticism` - Review and refine
7. `stage_<N>.07_fixing` - Fix issues
8. `stage_<N>.09_archives` - Workflow validated, ready for production

**Output:** Validated workflow document ready to move to production

### Phase 2: Production (`.04_workflows/`)

**Purpose:** Store validated workflows and track execution

**Structure:**
- Each workflow gets its own slot: `workflow_1/`, `workflow_2/`, etc.
- Each workflow contains:
  - The workflow document (markdown)
  - Execution stages (`<N>.99_stages/`)

**Execution Stages:**
1. `stage_<N>.01_instructions` - Workflow instructions
2. `stage_<N>.04_development` - Execute workflow
3. `stage_<N>.05_testing` - Verify results
4. `stage_<N>.09_archives` - Execution complete

### Phase 3: Results (`.05_results/`)

**Purpose:** Track outputs and links to completed work

**Contents:**
- Links to output files
- Summary of completed work
- Metrics/statistics

## Usage

### To Create a New Workflow:
1. Work in `.03_workflow_creation/`
2. Progress through development stages
3. When validated, create document in `.04_workflows/workflow_N/`

### To Execute a Workflow:
1. Navigate to `.04_workflows/workflow_N/`
2. Follow the workflow document
3. Track progress in `<N>.99_stages/`
4. Link results in `.05_results/`

## Current Workflows

- `workflow_1/` - <Description>
- `workflow_2/` - <Description>

EOF
```

<!-- section_id: "c8f5ce83-4a9e-48c8-9fcd-bc3a562a6070" -->
### Step 3: Create Development Stages

```bash
# In .03_workflow_creation/.99_stages/
for i in 01 02 03 04 05 06 07 08; do
    STAGE_NAME=""
    case $i in
        01) STAGE_NAME="instructions" ;;
        02) STAGE_NAME="planning" ;;
        03) STAGE_NAME="design" ;;
        04) STAGE_NAME="development" ;;
        05) STAGE_NAME="testing" ;;
        06) STAGE_NAME="criticism" ;;
        07) STAGE_NAME="fixing" ;;
        08) STAGE_NAME="archives" ;;
    esac

    mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.99_stages/stage_${LAYER}.${i}_${STAGE_NAME}/docs"
    mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.99_stages/stage_${LAYER}.${i}_${STAGE_NAME}/hand_off_documents"
done

# Create status file
cat > "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.99_stages/status_${LAYER}.json" << EOF
{
  "phase": "workflow_creation",
  "current_stage": "stage_${LAYER}.01_instructions",
  "last_updated": "$(date +%Y-%m-%d)",
  "stages": {
    "stage_${LAYER}.01_instructions": "in_progress",
    "stage_${LAYER}.02_planning": "not_started",
    "stage_${LAYER}.03_design": "not_started",
    "stage_${LAYER}.04_development": "not_started",
    "stage_${LAYER}.05_testing": "not_started",
    "stage_${LAYER}.06_criticism": "not_started",
    "stage_${LAYER}.07_fixing": "not_started",
    "stage_${LAYER}.09_archives": "not_started"
  },
  "notes": "Developing workflow for <name>"
}
EOF
```

---

<!-- section_id: "7a38946c-965a-4786-88a6-099e2811532e" -->
## 📋 Real-World Examples

<!-- section_id: "77afdc50-1efa-44e5-96d5-9d60436cbbac" -->
### Example 1: PAC School DS250 Assignments

**Feature:** `layer_2_feature_2.01_2_workflow_feature_2_assignments`

**Custom Directories:**
- `.03_workflow_creation/` - Develop assignment completion workflows
- `.04_workflows/` - Store workflows for unit setup, template completion, verification
- `.05_results/` - Links to completed assignments in course repos

**Workflows:**
- `workflow_1/workflow_ds250_assignments_v1.md` - Unit setup and template completion

**Why Workflow Feature:**
- ✅ Repeated process (each assignment uses same workflow)
- ✅ Distinct phases (creation vs execution)
- ✅ Multiple workflow instances needed
- ❌ Doesn't fit standard 8-stage pattern

<!-- section_id: "4eeac8d9-b0b3-4b64-a322-0341e371a419" -->
### Example 2: PAC School DS250 Coding Challenges

**Feature:** `layer_2_feature_2.02_2_workflow_feature_2_coding_challenges`

**Custom Directories:**
- `.03_workflow_creation/` - Develop quiz completion workflow
- `.04_workflows/` - Store validated quiz workflow
- `.05_results/` - Links to completed quizzes

**Workflows:**
- `workflow_ds250_coding_challenge_v1.md` - Timed quiz completion workflow

**Why Workflow Feature:**
- ✅ Repeated process (each quiz uses same workflow)
- ✅ Need to develop and refine process
- ✅ Execution tracking separate from development
- ❌ Standard stages don't fit

---

<!-- section_id: "80931f0e-1e39-4676-bc93-27c68245c242" -->
## 🔧 Workflow Document Template

<!-- section_id: "098d9edd-a2f8-4ea7-b198-9620019ca8e5" -->
### workflow_<name>_v1.md

```markdown
# Workflow: <Name> v1

**Purpose:** <Brief purpose>
**Created:** YYYY-MM-DD
**Status:** Production / In Development
**Execution Stages:** <List which stages are used>

---

## Prerequisites

- Tool/resource 1
- Tool/resource 2
- Access to X

## Inputs

- Input 1: Description
- Input 2: Description

## Steps

### Step 1: <Action>

**Objective:** <What this accomplishes>

**Actions:**
1. Sub-action 1
2. Sub-action 2

**Output:** <What this produces>

### Step 2: <Action>

[...]

## Outputs

- Output 1: Description
- Output 2: Description

## Validation

- [ ] Check 1
- [ ] Check 2

## Notes

- Special considerations
- Edge cases
```

---

<!-- section_id: "b98685dc-8668-4677-9072-593a3477ad73" -->
## 🎯 When to Use Workflow Features

<!-- section_id: "faf25ea6-b761-4b38-b747-686555d1a046" -->
### Use Workflow Features When:
- ✅ You have a **repeatable process** to follow
- ✅ Process needs **development and refinement**
- ✅ You need to **execute process multiple times**
- ✅ You want to **track results** separately
- ✅ Process has **distinct phases** (creation → production → results)

<!-- section_id: "388563c3-9cb6-48b7-ab1b-a806a14492ad" -->
### Use Standard Features When:
- ✅ Learning/studying topics
- ✅ Hierarchical content organization
- ✅ Sequential one-time work
- ✅ Standard 8 stages fit your workflow

---

<!-- section_id: "60db02cf-46b2-44a7-877f-d51db53557a4" -->
## 📊 Comparison: Standard vs Workflow Feature

| Aspect | Standard Feature | Workflow Feature |
|--------|------------------|------------------|
| **Stages** | Single `<N>.99_stages/` | Multiple nested stages |
| **Lifecycle** | Linear: instructions → archives | Cyclical: develop → execute → track |
| **Reusability** | One-time or ad-hoc | Repeatable processes |
| **Complexity** | Simple to moderate | Moderate to complex |
| **Setup Time** | Quick | Longer (but worth it for repeated use) |
| **Best For** | Learning, content | Automation, repeated tasks |

---

<!-- section_id: "e797ebe1-eb1b-4c31-87d1-c1935b34acef" -->
## 🛠️ Quick Setup Script

Save this as `create_workflow_feature.sh`:

```bash
#!/bin/bash
# Usage: ./create_workflow_feature.sh 2 assignments

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <layer_number> <feature_name>"
    echo "Example: $0 2 assignments"
    exit 1
fi

LAYER=$1
NAME=$2
FEATURE_DIR="layer_${LAYER}_feature_${NAME}"

echo "Creating workflow feature: $FEATURE_DIR"

# Standard directories
mkdir -p "$FEATURE_DIR/${LAYER}.00_ai_manager_system"
mkdir -p "$FEATURE_DIR/${LAYER}.01_manager_handoff_documents/${LAYER}.00_to_universal"
mkdir -p "$FEATURE_DIR/${LAYER}.01_manager_handoff_documents/${LAYER}.01_to_specific"
mkdir -p "$FEATURE_DIR/${LAYER}.02_sub_layers"

# Workflow creation
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.00_ai_manager_system"
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.01_manager_handoff_documents"
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.02_sub_layers"

# Create workflow creation stages
for i in 01 02 03 04 05 06 07 08; do
    case $i in
        01) STAGE="instructions" ;;
        02) STAGE="planning" ;;
        03) STAGE="design" ;;
        04) STAGE="development" ;;
        05) STAGE="testing" ;;
        06) STAGE="criticism" ;;
        07) STAGE="fixing" ;;
        08) STAGE="archives" ;;
    esac
    mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.99_stages/stage_${LAYER}.${i}_${STAGE}/docs"
    mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.99_stages/stage_${LAYER}.${i}_${STAGE}/hand_off_documents"
done

# Workflow storage
mkdir -p "$FEATURE_DIR/${LAYER}.04_workflows"

# Results tracking
mkdir -p "$FEATURE_DIR/${LAYER}.05_results"

# Feature-level stages
mkdir -p "$FEATURE_DIR/${LAYER}.99_stages"

# Create README
cat > "$FEATURE_DIR/README.md" << EOF
# Feature: ${NAME^}

## Purpose

This workflow feature manages <purpose>.

## Structure

- \`${LAYER}.03_workflow_creation/\` - Develop workflows
- \`${LAYER}.04_workflows/\` - Production workflows
- \`${LAYER}.05_results/\` - Execution results

## Current Workflows

_(Add workflows as they're created)_

EOF

echo "✅ Created workflow feature at: $FEATURE_DIR"
echo ""
echo "Next steps:"
echo "1. Edit $FEATURE_DIR/README.md with your feature description"
echo "2. Start workflow development in ${LAYER}.03_workflow_creation/"
echo "3. When validated, move workflow to ${LAYER}.04_workflows/workflow_1/"
```

Make executable: `chmod +x create_workflow_feature.sh`

---

<!-- section_id: "67ea1054-60ae-42bf-b5a8-7c6c831ec627" -->
## 📚 Related Documentation

- `EXTENDING_THE_FRAMEWORK.md` - Complete extension patterns
- `FLEXIBLE_LAYERING_SYSTEM.md` - Standard framework
- PAC School examples:
  - `school-pac20026_fall2025/.../layer_2_feature_2.01_2_workflow_feature_2_assignments/`
  - `school-pac20026_fall2025/.../layer_2_feature_2.02_2_workflow_feature_2_coding_challenges/`

---

**Location:** `C:\Users\Dawson\dawson-workspace\code\0_layer_universal\0_context\layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers\WORKFLOW_FEATURE_PATTERN.md`
**Last Updated:** 2026-01-09
**Version:** 1.0
