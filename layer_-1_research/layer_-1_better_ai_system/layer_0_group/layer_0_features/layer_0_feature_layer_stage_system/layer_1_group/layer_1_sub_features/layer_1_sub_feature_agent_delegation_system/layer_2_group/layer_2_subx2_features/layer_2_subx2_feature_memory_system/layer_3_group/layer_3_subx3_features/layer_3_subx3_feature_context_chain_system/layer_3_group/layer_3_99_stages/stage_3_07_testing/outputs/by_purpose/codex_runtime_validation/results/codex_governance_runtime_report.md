# Codex Governance Runtime Report

## Scope
Runtime validation of Codex behavior against `.0agnostic` governance categories:
- knowledge
- principles
- rules (static + dynamic)
- protocols

## Runtime Mode
- `codex exec --dangerously-bypass-approvals-and-sandbox`

## Run
```bash
cd outputs
./test_codex_governance_runtime.sh
```

## Result
- PASS: 6
- FAIL: 0
- SKIP: 0

## Cases
1. Principle: single source of truth
2. Principle: lean static context
3. Knowledge: static vs dynamic context
4. Static rule: context traversal
5. Dynamic rule: sync after agnostic edits
6. Protocol: stage report protocol

## Insight
Codex reliably discovers and applies all four governance categories when prompted with scenario-constrained retrieval tasks.
