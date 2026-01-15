# Workflow Feature Pattern

**Purpose:** Template and guide for creating "workflow features" with creation → production → results lifecycle.

**Based On:** PAC School DS250 patterns (assignments and coding challenges)

**Last Updated:** 2026-01-09

---

## 🎯 What is a Workflow Feature?

A **workflow feature** is used when you need to:
1. **Create/Develop** workflows or processes
2. **Store/Execute** validated workflows
3. **Track** results from workflow execution

**Key Characteristic:** Distinct phases that don't fit the standard 8-stage pattern.

---

## 📐 Standard Structure vs Workflow Feature

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

## 🏗️ Creating a Workflow Feature

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

## 📋 Real-World Examples

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

## 🔧 Workflow Document Template

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

## 🎯 When to Use Workflow Features

### Use Workflow Features When:
- ✅ You have a **repeatable process** to follow
- ✅ Process needs **development and refinement**
- ✅ You need to **execute process multiple times**
- ✅ You want to **track results** separately
- ✅ Process has **distinct phases** (creation → production → results)

### Use Standard Features When:
- ✅ Learning/studying topics
- ✅ Hierarchical content organization
- ✅ Sequential one-time work
- ✅ Standard 8 stages fit your workflow

---

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

## 📚 Related Documentation

- `EXTENDING_THE_FRAMEWORK.md` - Complete extension patterns
- `FLEXIBLE_LAYERING_SYSTEM.md` - Standard framework
- PAC School examples:
  - `school-pac20026_fall2025/.../layer_2_feature_2.01_2_workflow_feature_2_assignments/`
  - `school-pac20026_fall2025/.../layer_2_feature_2.02_2_workflow_feature_2_coding_challenges/`

---

**Location:** `C:\Users\Dawson\dawson-workspace\code\0_ai_context\0_context\0.01_layer_stage_framework\WORKFLOW_FEATURE_PATTERN.md`
**Last Updated:** 2026-01-09
**Version:** 1.0
