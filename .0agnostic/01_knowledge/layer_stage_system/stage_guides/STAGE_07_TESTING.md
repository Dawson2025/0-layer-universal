# Stage 07: Testing — Universal Guide

## Purpose

Validate that built artifacts work correctly and meet requirements. This is the **verification stage** — prove that what was built actually works.

## What This Stage IS

The testing agent:
- Writes test scripts that verify artifacts against requirements (stage 01) and design (stage 04)
- Runs tests and documents results (PASS/FAIL/SKIP/SCAFFOLDED)
- Validates that constraints (stage 03) are respected
- Produces a test results summary with coverage analysis
- Identifies gaps where testing is insufficient

## What This Stage IS NOT

The testing agent does NOT:
- **Gather requirements** — that's stage 01
- **Research alternatives** — that's stage 02
- **Design architectures** — that's stage 04
- **Build new artifacts** — that's stage 06 (testing verifies, not builds)
- **Judge quality or suggest improvements** — that's stage 08 (criticism)
- **Fix issues** — that's stage 09 (fixing)

The agent determines **whether things work**, not **how to fix them**.

## Methodology

### Output Structure

```
stage_N_07_testing/
│
├── .0agnostic/
│   └── 05_handoff_documents/
│       └── 02_outgoing/
│           ├── 01_to_above/                     ← For manager / stages manager consumption
│           │   ├── stage_report.md              ← Status summary (handoff document, <30 lines)
│           │   ├── test_results_summary.md      ← Rolled-up results across all suites
│           │   └── testing_overview.md          ← Navigation hub — links to all suites, designs, results
│           │
│           └── 03_to_below/                     ← For test suites / sub-work to reference
│               ├── stage_report.md              ← Same report — provides stage-level context downward
│               ├── test_results_summary.md      ← Same summary — suites can see cross-suite status
│               └── testing_overview.md          ← Same overview — suites can navigate to siblings
│
└── outputs/
    ├── run_all_tests.sh                         ← Master runner (invokes all per-suite runners)
    │
    └── by_suite/
        ├── README.md                            ← Index of all test suites, status, coverage map
        │
        ├── {suite_name}/                        ← One directory per test suite (topic-organized)
        │   ├── design/                          ← Test design documents (what to test, why, test cases)
        │   │   └── test_design.md
        │   ├── tests/                           ← Actual test scripts (executable)
        │   │   ├── test_{name}.sh
        │   │   └── run_suite.sh                 ← Suite-level runner
        │   ├── results/                         ← Test run outputs, logs, timestamps
        │   │   └── run_YYYY-MM-DD.md
        │   └── insights/                        ← Coverage gaps, analysis, findings from runs
        │       └── coverage_analysis.md
        │
        ├── {another_suite}/
        │   ├── design/
        │   ├── tests/
        │   ├── results/
        │   └── insights/
        └── ...
```

**Key separation**: `outputs/` contains only work products (test suites). Handoff documents (stage report, results summary) live in `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/` because they exist to communicate upward to the manager, not as deliverables of the testing work itself.

### Suite Organization

Each test suite groups everything about one testing topic:
- **design/**: The test design — what to test, why, test case definitions (TC-XX-XX)
- **tests/**: The actual executable test scripts
- **results/**: Output from running the tests — timestamped run reports
- **insights/**: Analysis that emerges from testing — coverage gaps, patterns, findings

Suite names should reflect the topic being tested (e.g., `context_chain_validation`, `agnostic_sync`, `1merge_structure`, `hierarchy_inheritance`).

### Test Script Format

Each test script:
- Tests one specific aspect or requirement
- Outputs PASS/FAIL/SKIP for each check
- Uses consistent output format for aggregation
- Is idempotent (can be run repeatedly)
- Documents what it tests in comments

### Test Results Summary (Handoff)

The test results summary (`.0agnostic/05_handoff_documents/02_outgoing/01_to_above/test_results_summary.md`) includes:
- Total counts: PASS, FAIL, SKIP, SCAFFOLDED across all suites
- Per-suite breakdown with status
- Coverage analysis: what requirements are tested vs untested
- Gaps identified: what still needs testing

This is a companion to the stage report — the stage report gives the high-level summary (under 30 lines), the test results summary gives the detailed breakdown.

### Test Categories

- **Structural tests**: Does the expected directory/file structure exist?
- **Functional tests**: Do scripts/tools produce correct output?
- **Integration tests**: Do components work together?
- **Behavioral tests**: Do agents discover and follow rules/protocols correctly?
- **Constraint tests**: Are stage 03 constraints respected?
- **Regression tests**: Do previously working things still work?

## Inputs

- **Stage 01 outputs** — requirements to validate against
- **Stage 03 outputs** — constraints to verify compliance
- **Stage 04 outputs** — design specs to verify implementation matches
- **Stage 06 outputs** — artifacts to test (and development status for what was built)
- **Parent entity .0agnostic/** — entity structure to validate

## Outputs

### Work Products (in `outputs/`)

| Output | Location | Format |
|--------|----------|--------|
| Master test runner | `outputs/run_all_tests.sh` | Invokes all per-suite runners |
| Suite index | `outputs/by_suite/README.md` | Index of all suites, status, coverage map |
| Test designs | `outputs/by_suite/{suite}/design/` | Test case definitions per suite |
| Test scripts | `outputs/by_suite/{suite}/tests/` | Executable test scripts per suite |
| Test results | `outputs/by_suite/{suite}/results/` | Timestamped run reports per suite |
| Test insights | `outputs/by_suite/{suite}/insights/` | Coverage analysis, findings per suite |
| Suite runner | `outputs/by_suite/{suite}/tests/run_suite.sh` | Per-suite runner |

### Handoff Documents (in `.0agnostic/05_handoff_documents/02_outgoing/`)

Same content goes to both `01_to_above/` (for the manager) and `03_to_below/` (for test suites to reference).

| Output | Filename | Format |
|--------|----------|--------|
| Stage report | `stage_report.md` | Standard stage report format (under 30 lines) |
| Test results summary | `test_results_summary.md` | Cross-suite PASS/FAIL/SKIP counts + details |
| Overview document | `testing_overview.md` | Navigation hub — references all suites, designs, results, insights |

The **testing overview** (`testing_overview.md`) is the master reference document. It links to all test suites, their designs, their results, and their insights. Both the stage report and test results summary reference this overview for detailed navigation. The overview is the document you read to understand the full picture of testing for this entity.

The **to_below** copy lets individual test suites see the broader context — overall test status, what other suites exist, and where the stage stands. A suite agent working on `agnostic_sync/` can read the downward-facing overview to understand what `1merge_structure/` found.

## Success Criteria

This stage is complete when:
1. All requirements from stage 01 have corresponding tests
2. All tests pass (or failures are documented with context)
3. Constraint compliance is verified
4. Test coverage is documented (what's tested, what's not)
5. Results summary is up to date

## Exit Protocol

1. Write/update handoff documents in both outgoing directions (`01_to_above/` and `03_to_below/`):
   - `stage_report.md` — current status (under 30 lines)
   - `test_results_summary.md` — cross-suite PASS/FAIL/SKIP counts
   - `testing_overview.md` — navigation hub linking to all suites
2. If handing off to **stage 08** (criticism): include test results for the critic to review
3. If handing off to **stage 09** (fixing): list specific failures that need fixing
4. If handing off to **stage 06** (development): note implementation gaps discovered during testing

## Common Patterns

- **Test-driven verification**: Write tests based on requirements, not just what was built
- **Automation**: Tests should be executable scripts, not manual checklists
- **Progressive coverage**: Start with structural tests, add functional, then integration
- **Loop to fixing**: Failed tests trigger stage 09 (fixing), then re-run

## Anti-Patterns

- Writing tests only for what passes (testing should find failures)
- Manual-only testing (automate what you can)
- Testing without referencing requirements (tests should trace to needs)
- Fixing bugs during testing (flag them, let stage 09 handle fixes)
