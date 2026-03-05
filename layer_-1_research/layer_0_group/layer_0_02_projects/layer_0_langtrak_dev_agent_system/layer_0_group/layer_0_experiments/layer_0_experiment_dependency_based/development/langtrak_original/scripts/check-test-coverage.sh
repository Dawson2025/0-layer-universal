#!/bin/bash
# resource_id: "01108d42-f7b0-4cce-aabb-e45ed2014074"
# resource_type: "script"
# resource_name: "check-test-coverage"
# Test Coverage Check Script
# Verifies test coverage meets project standards

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔍 Test Coverage Analysis${NC}"
echo ""

# Get project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Configuration
MIN_COVERAGE=80
TARGET_COVERAGE=95
COVERAGE_DIR="htmlcov"

# Check if pytest and coverage are installed
if ! command -v pytest &> /dev/null; then
    echo -e "${RED}❌ pytest not found. Install with: pip install pytest pytest-cov${NC}"
    exit 1
fi

# Run tests with coverage
echo -e "${YELLOW}Running tests with coverage analysis...${NC}"
echo ""

# Run pytest with coverage
pytest tests/ \
    --cov=. \
    --cov-report=term-missing \
    --cov-report=html \
    --cov-config=.coveragerc \
    -v \
    || TEST_EXIT_CODE=$?

echo ""

# Extract coverage percentage
COVERAGE_OUTPUT=$(coverage report | grep "TOTAL")
if [ -z "$COVERAGE_OUTPUT" ]; then
    echo -e "${RED}❌ Could not extract coverage data${NC}"
    exit 1
fi

COVERAGE=$(echo "$COVERAGE_OUTPUT" | awk '{print $4}' | sed 's/%//')

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}           COVERAGE ANALYSIS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "  Current Coverage:  ${YELLOW}${COVERAGE}%${NC}"
echo -e "  Minimum Required:  ${MIN_COVERAGE}%"
echo -e "  Target Coverage:   ${TARGET_COVERAGE}%"
echo ""

# Determine status
if (( $(echo "$COVERAGE >= $TARGET_COVERAGE" | bc -l) )); then
    echo -e "${GREEN}✅ EXCELLENT${NC} - Coverage meets target!"
    STATUS="excellent"
elif (( $(echo "$COVERAGE >= $MIN_COVERAGE" | bc -l) )); then
    echo -e "${YELLOW}⚠️  ACCEPTABLE${NC} - Coverage meets minimum (aim for ${TARGET_COVERAGE}%)"
    STATUS="acceptable"
else
    echo -e "${RED}❌ INSUFFICIENT${NC} - Coverage below minimum ${MIN_COVERAGE}%"
    STATUS="insufficient"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Show uncovered files
echo ""
echo -e "${YELLOW}Files with low coverage:${NC}"
coverage report | awk -v min="$MIN_COVERAGE" '
    NR > 2 && $NF != "100%" {
        cov = $4;
        gsub(/%/, "", cov);
        if (cov+0 < min+0) {
            printf "  %-50s %6s\n", $1, $4
        }
    }
'

echo ""

# Show HTML report location
if [ -d "$COVERAGE_DIR" ]; then
    echo -e "${BLUE}📊 Detailed HTML report:${NC} file://$PROJECT_ROOT/$COVERAGE_DIR/index.html"
    echo ""
fi

# Summary recommendations
echo -e "${YELLOW}📋 Recommendations:${NC}"
echo ""

if [ "$STATUS" == "insufficient" ]; then
    echo "  1. Add unit tests for uncovered functions"
    echo "  2. Add integration tests for API endpoints"
    echo "  3. Add E2E tests for critical user workflows"
    echo "  4. Focus on files with < ${MIN_COVERAGE}% coverage first"
elif [ "$STATUS" == "acceptable" ]; then
    echo "  1. Good job! Coverage meets minimum standards"
    echo "  2. Add tests to reach ${TARGET_COVERAGE}% target"
    echo "  3. Focus on files with < ${TARGET_COVERAGE}% coverage"
else
    echo "  1. Excellent coverage! Keep it up!"
    echo "  2. Maintain coverage as code grows"
fi

echo ""

# Exit with appropriate code
if [ "$STATUS" == "insufficient" ]; then
    exit 1
elif [ -n "$TEST_EXIT_CODE" ] && [ "$TEST_EXIT_CODE" != "0" ]; then
    echo -e "${RED}⚠️  Tests failed - see output above${NC}"
    exit "$TEST_EXIT_CODE"
else
    exit 0
fi
