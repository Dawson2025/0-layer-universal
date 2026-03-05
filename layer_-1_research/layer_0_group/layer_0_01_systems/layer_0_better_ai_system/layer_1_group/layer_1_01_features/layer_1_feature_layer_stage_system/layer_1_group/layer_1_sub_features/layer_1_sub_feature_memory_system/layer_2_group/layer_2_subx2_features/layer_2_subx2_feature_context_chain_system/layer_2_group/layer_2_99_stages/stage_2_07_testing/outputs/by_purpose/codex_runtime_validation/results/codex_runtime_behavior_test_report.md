---
resource_id: "ed9b167b-ec8a-4c09-ae2e-b039c6fef65f"
resource_type: "output"
resource_name: "codex_runtime_behavior_test_report"
---
# Codex Runtime Behavior Test Report

<!-- section_id: "83f54025-11e4-4ebe-b911-3d3e57e42dc0" -->
## Test Design

<!-- section_id: "8e0b512d-c452-4d39-9e9f-839818fcfc73" -->
### Goal
Validate real Codex-agent behavior (not just static file checks) under the required max-permission runtime mode.

<!-- section_id: "e682506e-514a-462b-ada3-6cf50ddafd68" -->
### Required runtime mode
- `codex --dangerously-bypass-approvals-and-sandbox`

<!-- section_id: "bc381e3e-fb62-4e45-8a47-cfe233c93fa9" -->
### Cases
1. Runtime execution case: Codex runs `test_codex_projection.sh` and returns `PASS`
2. Runtime execution case: Codex runs `test_codex_context_conditions.sh` and returns `PASS`
3. Discovery case: Codex reads `AGENTS.md` and returns the exact codex contract path
4. Discovery case: Codex reads `AGENTS.md` and returns the exact chain-validate skill path

<!-- section_id: "9b8ae394-db30-42ed-9bc6-ad7133aa6750" -->
## Implementation

<!-- section_id: "6b8f0ea0-0377-40dc-8aec-dad555a1a653" -->
### Script
- `outputs/test_codex_runtime_behavior.sh`

<!-- section_id: "8b255800-f1f3-4af7-a5e8-893200945946" -->
### Integration
- Added to `outputs/run_all_tests.sh`
- Added to `outputs/test_codex_ci_gate.sh` so CI gate includes runtime-agent behavior checks

<!-- section_id: "ed72f8de-059d-4e3d-8a67-b16e73954ab9" -->
## Run

<!-- section_id: "cd6ec45b-7728-4c52-a2c6-9aa96dc9d752" -->
### Command
```bash
cd outputs
./test_codex_runtime_behavior.sh
```

<!-- section_id: "a51d9f8a-9567-4920-b73e-b676e6ef82f5" -->
### Result
- PASS: 4
- FAIL: 0
- SKIP: 0

<!-- section_id: "e3d01c58-4c19-42e9-a6b5-05e691e1e5fd" -->
## Full-suite impact

After integrating runtime behavior test:
- `run_all_tests.sh` total: **143 PASS, 0 FAIL, 6 SKIP, 2 SCAFFOLDED**
- Readiness: **94%**

<!-- section_id: "5483cf4a-4c32-4aed-8846-e3cdd7ceb351" -->
## Insights

1. Codex runtime behavior can be validated deterministically by constraining return format and asserting exact values.
2. Dangerous-bypass mode is necessary for authoritative runtime results in this environment.
3. AGENTS discovery behavior can be tested directly by path extraction prompts, not only by shell-script execution.
4. Runtime behavior checks belong in CI gate (`test_codex_ci_gate.sh`) to prevent regressions in actual agent behavior.
