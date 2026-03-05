#!/usr/bin/env bash
# resource_id: "cccce2bb-d3aa-4208-87fe-6e3109eecdcf"
# resource_type: "script"
# resource_name: "test_outputs_purpose_taxonomy"
# test_outputs_purpose_taxonomy.sh — Validate purpose/suite output organization for stage_1_07_testing

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PURPOSE_DIR="$SCRIPT_DIR/by_purpose"

PASS=0
FAIL=0
SKIP=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: Outputs Purpose Taxonomy (stage_1_07_testing) ==="

required_purposes=(
  "report_porting_contract_validation"
  "rule_compliance_validation"
  "stages_manager_pattern_validation"
  "full_suite_validation"
)

required_suite_dirs=(
  "design"
  "implementation"
  "runs"
  "results"
  "insights"
)

[ -d "$PURPOSE_DIR" ] && pass "Exists: outputs/by_purpose" || fail "Missing: outputs/by_purpose"

for purpose in "${required_purposes[@]}"; do
  pdir="$PURPOSE_DIR/$purpose"
  if [ -d "$pdir" ]; then
    pass "Purpose exists: $purpose"
  else
    fail "Missing purpose directory: $purpose"
    continue
  fi

  for suite in "${required_suite_dirs[@]}"; do
    sdir="$pdir/$suite"
    if [ -d "$sdir" ]; then
      pass "Suite dir exists: $purpose/$suite"
      if find "$sdir" -maxdepth 1 -type f -name "*.md" | grep -q .; then
        pass "Suite has artifacts: $purpose/$suite"
      else
        fail "Suite missing markdown artifacts: $purpose/$suite"
      fi
    else
      fail "Missing suite dir: $purpose/$suite"
    fi
  done
done

[ -f "$PURPOSE_DIR/README.md" ] && pass "Exists: outputs/by_purpose/README.md" || fail "Missing: outputs/by_purpose/README.md"

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
