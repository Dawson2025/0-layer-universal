#!/usr/bin/env bash
# Category test runner
# Usage: bash tests/run_category_tests.sh [repo_root]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CATEGORY_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="${1:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
CATEGORY_NAME="$(basename "$CATEGORY_DIR")"

TOTAL=0; PASS=0; FAIL=0; SKIP=0

echo "Category: $CATEGORY_NAME"
echo "---"

for rule_dir in "$CATEGORY_DIR"/*/; do
    [ -d "$rule_dir/tests" ] || continue
    rule_name="$(basename "$rule_dir")"
    [ "$rule_name" = "tests" ] && continue

    if [ -f "$rule_dir/tests/test_structural.sh" ]; then
        TOTAL=$((TOTAL + 1))
        echo "  $rule_name: "
        if bash "$rule_dir/tests/test_structural.sh" "$REPO_ROOT" 2>&1 | sed 's/^/    /'; then
            PASS=$((PASS + 1))
            echo "    -> PASS"
        else
            FAIL=$((FAIL + 1))
            echo "    -> FAIL"
        fi
    else
        SKIP=$((SKIP + 1))
        TOTAL=$((TOTAL + 1))
        echo "  $rule_name: SKIP (no test_structural.sh)"
    fi
done

echo "---"
echo "Category $CATEGORY_NAME: $TOTAL rules | $PASS PASS | $FAIL FAIL | $SKIP SKIP"
