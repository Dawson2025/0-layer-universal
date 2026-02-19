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

```
outputs/
├── run_all_tests.sh                  <- Master test runner
├── test_*.sh                         <- Individual test scripts
├── test_results_summary.md           <- Aggregated results with PASS/FAIL counts
├── by_topic/
│   └── validation_report.md          <- Detailed validation analysis
└── stage_report.md
```

### Test Script Format

Each test script:
- Tests one specific aspect or requirement
- Outputs PASS/FAIL/SKIP for each check
- Uses consistent output format for aggregation
- Is idempotent (can be run repeatedly)
- Documents what it tests in comments

### Test Results Summary

The summary includes:
- Total counts: PASS, FAIL, SKIP, SCAFFOLDED
- Per-test breakdown with status
- Coverage analysis: what requirements are tested vs untested
- Gaps identified: what still needs testing

### Test Categories

- **Structural tests**: Does the expected directory/file structure exist?
- **Functional tests**: Do scripts/tools produce correct output?
- **Integration tests**: Do components work together?
- **Constraint tests**: Are stage 03 constraints respected?
- **Regression tests**: Do previously working things still work?

## Inputs

- **Stage 01 outputs** — requirements to validate against
- **Stage 03 outputs** — constraints to verify compliance
- **Stage 04 outputs** — design specs to verify implementation matches
- **Stage 06 outputs** — artifacts to test (and development status for what was built)
- **Parent entity .0agnostic/** — entity structure to validate

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Test scripts | `outputs/test_*.sh` | Executable test scripts |
| Test runner | `outputs/run_all_tests.sh` | Master runner that invokes all tests |
| Results summary | `outputs/test_results_summary.md` | PASS/FAIL/SKIP counts + details |
| Validation report | `outputs/by_topic/` | Detailed analysis |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is complete when:
1. All requirements from stage 01 have corresponding tests
2. All tests pass (or failures are documented with context)
3. Constraint compliance is verified
4. Test coverage is documented (what's tested, what's not)
5. Results summary is up to date

## Exit Protocol

1. Update `outputs/stage_report.md` with current status
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
