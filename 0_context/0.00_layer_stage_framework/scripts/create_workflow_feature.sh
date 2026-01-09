#!/bin/bash
# create_workflow_feature.sh
# Creates a workflow feature with creation → production → results structure
#
# Usage: ./create_workflow_feature.sh <layer_number> <feature_name>
# Example: ./create_workflow_feature.sh 2 assignments

if [ "$#" -ne 2 ]; then
    echo "❌ Error: Wrong number of arguments"
    echo ""
    echo "Usage: $0 <layer_number> <feature_name>"
    echo ""
    echo "Examples:"
    echo "  $0 2 assignments         # Creates layer_2_feature_assignments"
    echo "  $0 2 coding_challenges   # Creates layer_2_feature_coding_challenges"
    echo "  $0 3 data_pipeline       # Creates layer_3_feature_data_pipeline"
    exit 1
fi

LAYER=$1
NAME=$2
FEATURE_DIR="layer_${LAYER}_feature_${NAME}"

echo "🚀 Creating workflow feature: $FEATURE_DIR"
echo ""

# Check if directory already exists
if [ -d "$FEATURE_DIR" ]; then
    echo "❌ Error: Directory already exists: $FEATURE_DIR"
    exit 1
fi

# Create standard directories
echo "📁 Creating standard directories..."
mkdir -p "$FEATURE_DIR/${LAYER}.00_ai_manager_system"
mkdir -p "$FEATURE_DIR/${LAYER}.01_manager_handoff_documents/${LAYER}.00_to_universal"
mkdir -p "$FEATURE_DIR/${LAYER}.01_manager_handoff_documents/${LAYER}.01_to_specific"
mkdir -p "$FEATURE_DIR/${LAYER}.02_sub_layers"

# Create .03 workflow creation directory
echo "📁 Creating workflow creation directory (.03)..."
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.00_ai_manager_system"
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.01_manager_handoff_documents/${LAYER}.00_to_universal"
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.01_manager_handoff_documents/${LAYER}.01_to_specific"
mkdir -p "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.02_sub_layers"

# Create workflow creation stages
echo "📁 Creating workflow creation stages..."
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

# Create status file for workflow creation
cat > "$FEATURE_DIR/${LAYER}.03_workflow_creation/${LAYER}.99_stages/status_${LAYER}.json" << EOF
{
  "layer": ${LAYER},
  "type": "workflow_creation",
  "feature": "${NAME}",
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
    "stage_${LAYER}.08_archives": "not_started"
  },
  "notes": "Developing workflows for ${NAME}"
}
EOF

# Create .04 workflows directory
echo "📁 Creating workflows storage directory (.04)..."
mkdir -p "$FEATURE_DIR/${LAYER}.04_workflows"

# Create .05 results directory
echo "📁 Creating results tracking directory (.05)..."
mkdir -p "$FEATURE_DIR/${LAYER}.05_results"

# Create feature-level stages (optional)
echo "📁 Creating feature-level stages (.99)..."
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
    mkdir -p "$FEATURE_DIR/${LAYER}.99_stages/stage_${LAYER}.${i}_${STAGE}/docs"
    mkdir -p "$FEATURE_DIR/${LAYER}.99_stages/stage_${LAYER}.${i}_${STAGE}/hand_off_documents"
done

# Create feature-level status file
cat > "$FEATURE_DIR/${LAYER}.99_stages/status_${LAYER}.json" << EOF
{
  "layer": ${LAYER},
  "type": "workflow_feature",
  "name": "${NAME}",
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
    "stage_${LAYER}.08_archives": "not_started"
  },
  "workflows": [],
  "notes": "Workflow feature for ${NAME}"
}
EOF

# Create README
echo "📝 Creating README..."
cat > "$FEATURE_DIR/README.md" << EOF
# Feature: ${NAME^}

## Purpose

This workflow feature manages workflows for ${NAME}.

## Directory Structure

\`\`\`text
${FEATURE_DIR}/
├── README.md                          # This file
├── ${LAYER}.00_ai_manager_system/          # Feature-level manager
├── ${LAYER}.01_manager_handoff_documents/  # Feature-level handoffs
│   ├── ${LAYER}.00_to_universal/
│   └── ${LAYER}.01_to_specific/
├── ${LAYER}.02_sub_layers/                 # Feature-level knowledge/tools
├── ${LAYER}.03_workflow_creation/          # PHASE 1: Develop workflows
│   ├── ${LAYER}.00_ai_manager_system/
│   ├── ${LAYER}.01_manager_handoff_documents/
│   ├── ${LAYER}.02_sub_layers/
│   └── ${LAYER}.99_stages/                 # Development stages
├── ${LAYER}.04_workflows/                  # PHASE 2: Production workflows
│   └── workflow_1/                    # (Create workflow instances here)
│       ├── workflow_${NAME}_v1.md
│       └── ${LAYER}.99_stages/             # Execution stages
├── ${LAYER}.05_results/                    # PHASE 3: Output/results
└── ${LAYER}.99_stages/                     # Feature-level stages
\`\`\`

## Workflow Lifecycle

### Phase 1: Creation (\`.03_workflow_creation/\`)

**Purpose:** Design, develop, and test workflows

**Stages:**
1. \`stage_${LAYER}.01_instructions\` - Define workflow requirements
2. \`stage_${LAYER}.02_planning\` - Plan workflow steps
3. \`stage_${LAYER}.03_design\` - Design workflow structure
4. \`stage_${LAYER}.04_development\` - Build and iterate
5. \`stage_${LAYER}.05_testing\` - Test workflow
6. \`stage_${LAYER}.06_criticism\` - Review and refine
7. \`stage_${LAYER}.07_fixing\` - Fix issues
8. \`stage_${LAYER}.08_archives\` - Workflow validated, ready for production

**Output:** Validated workflow document

### Phase 2: Production (\`.04_workflows/\`)

**Purpose:** Store and execute validated workflows

**Structure:**
- Each workflow gets its own directory: \`workflow_1/\`, \`workflow_2/\`, etc.
- Each contains:
  - Workflow document (markdown)
  - Execution stages (\`${LAYER}.99_stages/\`)

**Execution Stages:**
1. \`stage_${LAYER}.01_instructions\` - Workflow instructions
2. \`stage_${LAYER}.04_development\` - Execute workflow
3. \`stage_${LAYER}.05_testing\` - Verify results
4. \`stage_${LAYER}.08_archives\` - Execution complete

### Phase 3: Results (\`.05_results/\`)

**Purpose:** Track outputs and links

**Contents:**
- Links to output files
- Summary of completed work
- Metrics/statistics

## Usage

### To Create a Workflow:
1. Work in \`.03_workflow_creation/\`
2. Progress through development stages
3. When validated, create in \`.04_workflows/workflow_N/\`

### To Execute a Workflow:
1. Navigate to \`.04_workflows/workflow_N/\`
2. Follow the workflow document
3. Track progress in \`${LAYER}.99_stages/\`
4. Link results in \`.05_results/\`

## Current Workflows

_(Add workflows as they're created)_

- \`workflow_1/\` - Description
- \`workflow_2/\` - Description

## Next Steps

1. Define workflow requirements in \`.03_workflow_creation/${LAYER}.99_stages/stage_${LAYER}.01_instructions/\`
2. Begin workflow development
3. Test and refine
4. Move to production when validated

---

**Created:** $(date +%Y-%m-%d)
**Pattern:** Workflow Feature (creation → production → results)
**Documentation:** See \`WORKFLOW_FEATURE_PATTERN.md\` in universal context
EOF

echo ""
echo "✅ Workflow feature created successfully!"
echo ""
echo "📂 Location: $FEATURE_DIR"
echo ""
echo "📝 Next steps:"
echo "   1. Edit $FEATURE_DIR/README.md with specific details"
echo "   2. Start workflow development in ${LAYER}.03_workflow_creation/"
echo "   3. When workflow is validated, create workflow_1/ in ${LAYER}.04_workflows/"
echo ""
echo "📚 Documentation:"
echo "   - Pattern guide: 0.00_layer_stage_framework/WORKFLOW_FEATURE_PATTERN.md"
echo "   - Examples: school-pac20026_fall2025 project"
echo ""
