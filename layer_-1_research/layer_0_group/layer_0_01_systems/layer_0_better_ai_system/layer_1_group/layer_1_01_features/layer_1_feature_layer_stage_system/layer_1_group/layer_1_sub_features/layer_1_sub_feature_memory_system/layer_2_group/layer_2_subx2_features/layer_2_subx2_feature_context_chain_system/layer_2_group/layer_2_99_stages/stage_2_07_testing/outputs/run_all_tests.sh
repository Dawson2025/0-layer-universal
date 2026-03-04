#!/usr/bin/env bash
# run_all_tests.sh — Run testing suites and generate summary report
#
# Runs each test, captures output, and produces test_results_summary.md

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPORT_DIR="$SCRIPT_DIR/reports"
REPORT="$REPORT_DIR/test_results_summary.md"
LEGACY_REPORT="$SCRIPT_DIR/test_results_summary.md"

TESTS=(
    "test_outputs_purpose_taxonomy.sh"
    "test_cross_entity_porting_bridge.sh"
    "test_reports_funnel_structure.sh"
    "test_agnostic_sync.sh"
    "test_context_chain_traversal.sh"
    "test_avenue_coverage_functional.sh"
    "test_1merge_structure.sh"
    "test_instantiation_readiness.sh"
    "test_codex_projection.sh"
    "test_codex_discovery_chain.sh"
    "test_codex_context_conditions.sh"
    "test_codex_runtime_behavior.sh"
    "test_codex_ci_gate.sh"
)

TOTAL_PASS=0
TOTAL_FAIL=0
TOTAL_SKIP=0
TOTAL_SCAFFOLDED=0

# Start report
mkdir -p "$REPORT_DIR"
cat > "$REPORT" << EOF
# Test Results Summary

**Date**: $(date '+%Y-%m-%d %H:%M:%S')
**Entity**: layer_2_subx3_feature_context_chain_system
**Runner**: run_all_tests.sh

---

EOF

echo "=== Running All Tests ==="
echo ""

for test in "${TESTS[@]}"; do
    test_path="$SCRIPT_DIR/$test"
    test_name="${test%.sh}"

    echo ">>> Running: $test"

    # Capture output
    output=$("$test_path" 2>&1)
    exit_code=$?

    # Extract counts from output
    # Extract counts — handle both PASS/FAIL and READY/NOT READY formats
    p=$(echo "$output" | grep -oP '(PASS|READY).*?:\s*\K[0-9]+' | tail -1 || echo "0")
    f=$(echo "$output" | grep -oP '(FAIL|NOT READY).*?:\s*\K[0-9]+' | tail -1 || echo "0")
    s=$(echo "$output" | grep -oP '(SKIP|WARN).*?:\s*\K[0-9]+' | tail -1 || echo "0")
    sc=$(echo "$output" | grep -oP 'SCAFFOLDED.*?:\s*\K[0-9]+' | tail -1 || echo "0")

    # Default to 0 if empty
    p=${p:-0}; f=${f:-0}; s=${s:-0}; sc=${sc:-0}

    TOTAL_PASS=$((TOTAL_PASS + p))
    TOTAL_FAIL=$((TOTAL_FAIL + f))
    TOTAL_SKIP=$((TOTAL_SKIP + s))
    TOTAL_SCAFFOLDED=$((TOTAL_SCAFFOLDED + sc))

    # Status
    if [ $exit_code -eq 0 ]; then
        status="PASS"
    else
        status="FAIL"
    fi

    echo "    Result: $status (pass=$p, fail=$f, skip=$s, scaffolded=$sc)"
    echo ""

    # Write to report
    cat >> "$REPORT" << EOF
## $test_name

**Status**: $status | **Exit code**: $exit_code
| Metric | Count |
|--------|-------|
| PASS | $p |
| FAIL | $f |
| SKIP | $s |
| SCAFFOLDED | $sc |

<details>
<summary>Full output</summary>

\`\`\`
$output
\`\`\`

</details>

---

EOF

done

# Overall summary
TOTAL=$((TOTAL_PASS + TOTAL_FAIL + TOTAL_SKIP + TOTAL_SCAFFOLDED))
if [ "$TOTAL" -gt 0 ]; then
    READINESS=$((TOTAL_PASS * 100 / TOTAL))
else
    READINESS=0
fi

cat >> "$REPORT" << EOF

## Overall Summary

| Metric | Count |
|--------|-------|
| **Total PASS** | $TOTAL_PASS |
| **Total FAIL** | $TOTAL_FAIL |
| **Total SKIP** | $TOTAL_SKIP |
| **Total SCAFFOLDED** | $TOTAL_SCAFFOLDED |
| **Readiness Score** | ${READINESS}% |

### Interpretation

- **PASS**: Check is fully functional
- **FAIL**: Check failed — must be fixed before instantiation
- **SKIP**: Check was skipped (dependency unavailable)
- **SCAFFOLDED**: Structure exists but content is empty — needs population during instantiation

### Next Steps

$(if [ $TOTAL_FAIL -eq 0 ]; then
    echo "Entity scaffolding is structurally sound. Proceed with instantiation:"
    echo "1. Populate \`.0agnostic/\` with rules, knowledge, skills"
    echo "2. Create \`.claude/rules/\` path rules"
    echo "3. Flesh out \`.gab.jsonld\` with modes, actors, personas"
    echo "4. Generate \`.integration.md\` from \`.gab.jsonld\`"
    echo "5. Run \`agnostic-sync.sh\` to regenerate tool files"
    echo "6. Re-run tests to verify full PASS"
else
    echo "**Fix $TOTAL_FAIL failing checks before instantiation.**"
    echo ""
    echo "Review each FAIL above and resolve the underlying issue."
fi)
EOF

# Keep legacy location for backward compatibility.
cp "$REPORT" "$LEGACY_REPORT"

echo "================================"
echo "  TOTAL PASS:       $TOTAL_PASS"
echo "  TOTAL FAIL:       $TOTAL_FAIL"
echo "  TOTAL SKIP:       $TOTAL_SKIP"
echo "  TOTAL SCAFFOLDED: $TOTAL_SCAFFOLDED"
echo "  Readiness:        ${READINESS}%"
echo "================================"
echo ""
echo "Report written to: $REPORT"
echo "Legacy copy written to: $LEGACY_REPORT"
