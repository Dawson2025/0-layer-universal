#!/usr/bin/env bash
# test_outputs_purpose_taxonomy.sh — Validate purpose/suite output organization for testing stage

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="$SCRIPT_DIR"
PURPOSE_DIR="$OUT_DIR/by_purpose"

PASS=0
FAIL=0
SKIP=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: Outputs Purpose Taxonomy ==="

required_purposes=(
  "context_chain_validation"
  "codex_runtime_validation"
  "reports_funnel_validation"
  "avenue_web_validation"
  "cross_entity_porting_bridge_validation"
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
      # Require at least one markdown artifact in each suite dir.
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

# by_topic remains as compatibility surface.
if [ -f "$OUT_DIR/by_topic/README.md" ]; then
  pass "Compatibility note exists: outputs/by_topic/README.md"
else
  skip "Compatibility note missing: outputs/by_topic/README.md"
fi

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
