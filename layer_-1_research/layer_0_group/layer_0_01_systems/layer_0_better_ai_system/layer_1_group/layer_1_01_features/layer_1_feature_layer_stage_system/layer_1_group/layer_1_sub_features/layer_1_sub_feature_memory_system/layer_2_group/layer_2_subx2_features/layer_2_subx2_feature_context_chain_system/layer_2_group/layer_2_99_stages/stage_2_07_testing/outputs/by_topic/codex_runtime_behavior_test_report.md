---
resource_id: "fc05e9a3-d486-446d-9af7-ae8236c974fb"
resource_type: "output"
resource_name: "codex_runtime_behavior_test_report"
---
# Codex Runtime Behavior Test Report

<!-- section_id: "30bee1cd-9b16-440c-b5d2-945929224e4a" -->
## Test Design

<!-- section_id: "e4349c7e-682e-48f0-87a0-e8e4dd6cc6bc" -->
### Goal
Validate real Codex-agent behavior (not just static file checks) under the required max-permission runtime mode.

<!-- section_id: "942b5185-37fc-4102-ba6f-116166f264fa" -->
### Required runtime mode
- `codex --dangerously-bypass-approvals-and-sandbox`

<!-- section_id: "608657e7-bd76-4884-9c42-0c87e8b17ce0" -->
### Cases
1. Runtime execution case: Codex runs `test_codex_projection.sh` and returns `PASS`
2. Runtime execution case: Codex runs `test_codex_context_conditions.sh` and returns `PASS`
3. Discovery case: Codex reads `AGENTS.md` and returns the exact codex contract path
4. Discovery case: Codex reads `AGENTS.md` and returns the exact chain-validate skill path

<!-- section_id: "36d412ea-3024-42ca-a241-1135a2851ddd" -->
## Implementation

<!-- section_id: "a37f1ce4-77fe-4f96-bcd2-8440e8faa646" -->
### Script
- `outputs/test_codex_runtime_behavior.sh`

<!-- section_id: "127e2a22-7ecb-4653-9a4f-ed7fb0b624a4" -->
### Integration
- Added to `outputs/run_all_tests.sh`
- Added to `outputs/test_codex_ci_gate.sh` so CI gate includes runtime-agent behavior checks

<!-- section_id: "23be0cce-e8bc-4275-81f3-8d1856edd335" -->
## Run

<!-- section_id: "6f2a3f3d-419c-42b0-88ba-8cc13c71c48f" -->
### Command
```bash
cd outputs
./test_codex_runtime_behavior.sh
```

<!-- section_id: "107fb0b7-bac0-4509-b0fc-c2b0197c7141" -->
### Result
- PASS: 4
- FAIL: 0
- SKIP: 0

<!-- section_id: "76df9b1f-e8c2-4e13-8e5c-e7b4ef21d56d" -->
## Full-suite impact

After integrating runtime behavior test:
- `run_all_tests.sh` total: **143 PASS, 0 FAIL, 6 SKIP, 2 SCAFFOLDED**
- Readiness: **94%**

<!-- section_id: "d45c1099-a3ac-4c70-b89d-2da2f09a1461" -->
## Insights

1. Codex runtime behavior can be validated deterministically by constraining return format and asserting exact values.
2. Dangerous-bypass mode is necessary for authoritative runtime results in this environment.
3. AGENTS discovery behavior can be tested directly by path extraction prompts, not only by shell-script execution.
4. Runtime behavior checks belong in CI gate (`test_codex_ci_gate.sh`) to prevent regressions in actual agent behavior.
