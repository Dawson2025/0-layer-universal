---
resource_id: "1aefb7e0-206f-40ba-85ad-458e877f7632"
resource_type: "knowledge"
resource_name: "graceful_degradation"
---
# Principle: Graceful Degradation

<!-- section_id: "b7b4b156-a899-4e12-865a-bf5055e315ec" -->
## Summary

When one or more context delivery avenues fail, the system must continue functioning with reduced but sufficient context. No single avenue failure should render an entity unusable. The system is designed to fail open: missing context means the agent operates with less guidance, not that it stops working.

Degradation tiers range from Full (all 8 avenues functional) through Good (5-7), Adequate (3-4), Minimal (1-2), to Failed (0, must escalate). The minimum viable context for an agent to function is: identity (who am I), parent (where do I fit), and one rule source. This minimum is achievable through any single avenue that provides identity -- CLAUDE.md cascade (A1), 0AGNOSTIC.md chain (A4), or integration summary (A6).

Avenue overlap is intentional resilience engineering, not waste. Paired avenues (A5+A6 for structured+readable, A1+A4 for generated+source, A2+A8 for auto-loaded+manual) ensure that if one member fails, the other provides coverage. The one exception to fail-open behavior: if the agent cannot determine its identity/role/scope, it should escalate to the user rather than guessing.

<!-- section_id: "65ed73a3-3128-4dcd-b6cb-aec34d51a32b" -->
## Key Concepts

- **Fail-open design**: Missing context reduces guidance, does not stop the agent
- **5 degradation tiers**: Full, Good, Adequate, Minimal, Failed
- **Minimum viable context**: Identity + parent + one rule source
- **Paired avenues**: A5+A6, A1+A4, A2+A8 provide mutual backup
- **Identity exception**: If identity is unknown, escalate -- do not guess

<!-- section_id: "2d8760d5-3197-4da9-870e-fcec070bbf28" -->
## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Full principle doc | `.0agnostic/01_knowledge/principles/graceful_degradation.md` | Degradation tiers, failure scenarios, mitigations |
| Avenue redundancy | `.0agnostic/01_knowledge/principles/avenue_redundancy.md` | Redundancy enables degradation |
| Avenue architecture | `.0agnostic/01_knowledge/avenue_web_architecture.md` | Avenue health metrics and test results |
