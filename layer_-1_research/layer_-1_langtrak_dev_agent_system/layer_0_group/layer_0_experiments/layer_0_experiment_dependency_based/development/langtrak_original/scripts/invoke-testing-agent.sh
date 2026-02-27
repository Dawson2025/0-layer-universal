#!/bin/bash
# Testing Agent Invocation Script
# Helps create handoff documents for Testing Agent

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🧪 Testing Agent Invocation Helper${NC}"
echo ""

# Get project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# Layer+stage handoff location (Project Layer → Testing Stage)
HANDOFF_DIR="$PROJECT_ROOT/docs/0_context/layer_1_project/1.99_stages/stage_1.05_testing/hand_off_documents/testing_handoffs"
mkdir -p "$HANDOFF_DIR"

# Get current date
DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Step 1: Change Type
echo -e "${YELLOW}Step 1: What type of change was made?${NC}"
echo "1) New Feature"
echo "2) Bug Fix"
echo "3) Refactoring"
echo "4) API Change"
echo "5) Database Schema Change"
echo "6) Other"
read -p "Enter choice (1-6): " choice

case $choice in
    1) CHANGE_TYPE="New Feature" ;;
    2) CHANGE_TYPE="Bug Fix" ;;
    3) CHANGE_TYPE="Refactoring" ;;
    4) CHANGE_TYPE="API Change" ;;
    5) CHANGE_TYPE="Database Schema Change" ;;
    6) CHANGE_TYPE="Other" ;;
    *) echo -e "${RED}Invalid choice${NC}"; exit 1 ;;
esac

# Step 2: Feature/Fix Name
echo ""
echo -e "${YELLOW}Step 2: Enter feature/fix name${NC}"
read -p "Name (e.g., 'User Authentication', 'Fix Word Deletion Bug'): " FEATURE_NAME

# Step 3: Description
echo ""
echo -e "${YELLOW}Step 3: Describe what changed${NC}"
read -p "Description: " DESCRIPTION

# Step 4: Get changed files from git
echo ""
echo -e "${YELLOW}Step 4: Detecting changed files...${NC}"
CHANGED_FILES=$(git diff --name-only HEAD 2>/dev/null || echo "Unable to detect from git")

if [ "$CHANGED_FILES" == "Unable to detect from git" ]; then
    echo -e "${YELLOW}Cannot auto-detect changed files. Please list them manually:${NC}"
    read -p "Changed files (comma-separated): " MANUAL_FILES
    CHANGED_FILES=$MANUAL_FILES
fi

# Step 5: Test types needed
echo ""
echo -e "${YELLOW}Step 5: What types of tests are needed?${NC}"
read -p "Unit tests needed? (y/n): " NEED_UNIT
read -p "Integration tests needed? (y/n): " NEED_INTEGRATION
read -p "E2E tests needed? (y/n): " NEED_E2E
read -p "Regression tests needed? (y/n): " NEED_REGRESSION

# Format test types
UNIT_CHECK=$([ "$NEED_UNIT" == "y" ] && echo "[X]" || echo "[ ]")
INTEGRATION_CHECK=$([ "$NEED_INTEGRATION" == "y" ] && echo "[X]" || echo "[ ]")
E2E_CHECK=$([ "$NEED_E2E" == "y" ] && echo "[X]" || echo "[ ]")
REGRESSION_CHECK=$([ "$NEED_REGRESSION" == "y" ] && echo "[X]" || echo "[ ]")

# Step 6: Critical paths
echo ""
echo -e "${YELLOW}Step 6: Describe critical user paths (one per line, empty line to finish)${NC}"
CRITICAL_PATHS=""
while true; do
    read -p "User path: " path
    [ -z "$path" ] && break
    CRITICAL_PATHS="${CRITICAL_PATHS}${path}\n"
done

# Step 7: Acceptance criteria
echo ""
echo -e "${YELLOW}Step 7: Describe acceptance criteria (one per line, empty line to finish)${NC}"
ACCEPTANCE_CRITERIA=""
while true; do
    read -p "Criterion: " criterion
    [ -z "$criterion" ] && break
    ACCEPTANCE_CRITERIA="${ACCEPTANCE_CRITERIA}- [ ] ${criterion}\n"
done

# Step 8: Known risks
echo ""
echo -e "${YELLOW}Step 8: Any known risks or concerns? (optional)${NC}"
read -p "Risks: " RISKS

# Generate filename
FILENAME="handoff_${TIMESTAMP}_$(echo $FEATURE_NAME | tr ' ' '_' | tr '[:upper:]' '[:lower:]').md"
FILEPATH="$HANDOFF_DIR/$FILENAME"

# Create handoff document
cat > "$FILEPATH" << EOF
# Testing Request - $FEATURE_NAME

**Date**: $DATE
**Development Agent**: $(whoami)
**Change Type**: $CHANGE_TYPE

---

## 1️⃣ **What Changed**

### Files Modified
\`\`\`
$(echo "$CHANGED_FILES" | sed 's/^/- /')
\`\`\`

### Description of Changes
$DESCRIPTION

---

## 2️⃣ **Testing Scope Required**

### Test Types Needed
- $UNIT_CHECK **Unit Tests** - Test individual functions/methods
- $INTEGRATION_CHECK **Integration Tests** - Test component interactions
- $E2E_CHECK **E2E Tests** - Test complete user workflows
- $REGRESSION_CHECK **Regression Tests** - Prevent bug recurrence

---

## 3️⃣ **Critical User Paths**

### Primary User Workflow
$(echo -e "$CRITICAL_PATHS" | sed 's/^/- /')

---

## 4️⃣ **Acceptance Criteria**

Tests must verify:
$(echo -e "$ACCEPTANCE_CRITERIA")

---

## 5️⃣ **Known Risks and Concerns**

$( [ -n "$RISKS" ] && echo "- $RISKS" || echo "None identified" )

---

## 6️⃣ **Testing Environment Requirements**

### Environment Setup
- [ ] Database: [Specify]
- [ ] External Services: [List any]
- [ ] Test Data: [Describe]
- [ ] Configuration: [Special config]

---

## 7️⃣ **Success Criteria for Testing Agent**

Testing Agent should:
1. ✅ Create comprehensive test plan
2. ✅ Implement all required tests
3. ✅ Achieve minimum 80% code coverage (target: 95%)
4. ✅ All tests pass successfully
5. ✅ Provide detailed testing report

---

## ✅ **Handoff Checklist**

- [ ] All sections above reviewed and completed
- [ ] Code is committed to version control
- [ ] Manual testing has been performed
- [ ] Documentation is updated
- [ ] Ready for Testing Agent

---

**Handoff Created**: $DATE
**Ready for Testing Agent**: YES

---

## 📝 **For Testing Agent**

Please review this handoff document and:
1. Create a comprehensive test plan
2. Implement all required tests following the Testing Agent Protocol
3. Report results using the testing report template

Protocol: docs/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.04_project_rules/legacy/universal_instruction_docs/testing-agent-protocol.md
EOF

# Success message
echo ""
echo -e "${GREEN}✅ Handoff document created successfully!${NC}"
echo ""
echo -e "${BLUE}📄 File location:${NC} $FILEPATH"
echo ""
echo -e "${YELLOW}📋 Next Steps:${NC}"
echo "1. Review and complete the handoff document"
echo "2. Share with Testing Agent (AI or human)"
echo "3. Testing Agent will create test plan and implement tests"
echo "4. Testing Agent will report results"
echo ""
echo -e "${BLUE}🔗 View handoff document:${NC}"
echo "   cat $FILEPATH"
echo ""
echo -e "${BLUE}📚 Testing Agent Protocol:${NC}"
echo "   docs/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.04_project_rules/legacy/universal_instruction_docs/testing-agent-protocol.md"
echo ""
