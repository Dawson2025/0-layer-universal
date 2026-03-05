---
resource_id: "84fc8f19-d499-42c8-96ce-2f878af4e9be"
resource_type: "output"
resource_name: "codex_governance_runtime_report"
---
# Codex Governance Runtime Report

<!-- section_id: "c63f6521-2c60-4d61-8b1f-ba77d06c79e1" -->
## Scope
Runtime validation of Codex behavior against `.0agnostic` governance categories:
- knowledge
- principles
- rules (static + dynamic)
- protocols

<!-- section_id: "68f22eff-4727-498a-9f67-f7cb9d12c15b" -->
## Runtime Mode
- `codex exec --dangerously-bypass-approvals-and-sandbox`

<!-- section_id: "019d56d1-b10d-451d-8584-09bbae08c2f2" -->
## Run
```bash
cd outputs
./test_codex_governance_runtime.sh
```

<!-- section_id: "2cb105f3-2aba-4df4-8d1d-fca53250c3e1" -->
## Result
- PASS: 6
- FAIL: 0
- SKIP: 0

<!-- section_id: "a49d9c5a-da74-4cec-b6b9-4842471901df" -->
## Cases
1. Principle: single source of truth
2. Principle: lean static context
3. Knowledge: static vs dynamic context
4. Static rule: context traversal
5. Dynamic rule: sync after agnostic edits
6. Protocol: stage report protocol

<!-- section_id: "ef8b15e1-8c8f-4ed7-9865-9152a96ce0b5" -->
## Insight
Codex reliably discovers and applies all four governance categories when prompted with scenario-constrained retrieval tasks.
