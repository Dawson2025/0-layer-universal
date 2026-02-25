# Codex Runtime Behavior Test Report

## Test Design

### Goal
Validate real Codex-agent behavior (not just static file checks) under the required max-permission runtime mode.

### Required runtime mode
- `codex --dangerously-bypass-approvals-and-sandbox`

### Cases
1. Runtime execution case: Codex runs `test_codex_projection.sh` and returns `PASS`
2. Runtime execution case: Codex runs `test_codex_context_conditions.sh` and returns `PASS`
3. Discovery case: Codex reads `AGENTS.md` and returns the exact codex contract path
4. Discovery case: Codex reads `AGENTS.md` and returns the exact chain-validate skill path

## Implementation

### Script
- `outputs/test_codex_runtime_behavior.sh`

### Integration
- Added to `outputs/run_all_tests.sh`
- Added to `outputs/test_codex_ci_gate.sh` so CI gate includes runtime-agent behavior checks

## Run

### Command
```bash
cd outputs
./test_codex_runtime_behavior.sh
```

### Result
- PASS: 4
- FAIL: 0
- SKIP: 0

## Full-suite impact

After integrating runtime behavior test:
- `run_all_tests.sh` total: **143 PASS, 0 FAIL, 6 SKIP, 2 SCAFFOLDED**
- Readiness: **94%**

## Insights

1. Codex runtime behavior can be validated deterministically by constraining return format and asserting exact values.
2. Dangerous-bypass mode is necessary for authoritative runtime results in this environment.
3. AGENTS discovery behavior can be tested directly by path extraction prompts, not only by shell-script execution.
4. Runtime behavior checks belong in CI gate (`test_codex_ci_gate.sh`) to prevent regressions in actual agent behavior.
