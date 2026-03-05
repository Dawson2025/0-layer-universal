---
resource_id: "733ea389-ea1a-4f78-8e00-b7745955aa49"
resource_type: "knowledge"
resource_name: "avenue_redundancy"
---
# Principle: Avenue Redundancy

**Type**: Reliability
**Severity**: High
**Date**: 2026-02-17

---

<!-- section_id: "10d6984b-5342-449d-889c-d2a5d8fa0b36" -->
## Statement

**Critical context must be reachable through at least 3 independent avenues. No single point of failure should prevent an agent from accessing essential information.**

---

<!-- section_id: "99394e30-f515-4854-90e8-d48e2c25bd82" -->
## Rationale

AI agents operate in unpredictable conditions:
- A CLAUDE.md file might not be in the cascade path (launched from different cwd)
- A .gab.jsonld might fail to parse (JSON syntax error)
- An agent might not know to check .0agnostic/rules/
- Episodic memory might be empty (first session)

Avenue redundancy ensures that even when some delivery mechanisms fail, the agent can still access critical context through alternative paths.

---

<!-- section_id: "34f44358-6781-413e-95ee-8ae995a74621" -->
## The 8 Avenues

1. **System Prompt** (CLAUDE.md cascade) — static, automatic
2. **Path Rules** (.claude/rules/) — triggered by directory
3. **Skills** (.0agnostic/skills/) — listed + invocable
4. **Parent References** (0AGNOSTIC.md chain) — explicit traversal
5. **JSON-LD Agent Defs** (.gab.jsonld) — mode/actor constraints
6. **Integration Summaries** (.integration.md) — readable summaries
7. **Episodic Memory** (session history) — historical context
8. **Agnostic System** (.0agnostic/) — on-demand resources

---

<!-- section_id: "44f86e83-c977-449a-8a5e-a1534db91407" -->
## Minimum Coverage Target

| Context Category | Minimum Avenues | Why |
|-----------------|----------------|-----|
| Entity identity | 3 | Agent must know its role regardless of entry point |
| Applicable rules | 3 | Rules must be discoverable through multiple paths |
| Available skills | 2 | Skills are listed and invocable — two natural avenues |
| Mode constraints | 2 | GAB + integration summary provide paired coverage |
| Session history | 1 | Episodic memory is the sole avenue (acceptable — not critical for first session) |

---

<!-- section_id: "2ffaf4c1-fe5e-4eb6-92a7-a04133d9f154" -->
## How to Add Redundancy

If a context item has fewer than 3 avenues:

| Missing Avenue | How to Add |
|---------------|-----------|
| A1 (System Prompt) | Mention in 0AGNOSTIC.md (syncs to CLAUDE.md) |
| A2 (Path Rules) | Create a .claude/rules/*.md referencing the item |
| A3 (Skills) | Create a skill that loads/validates the item |
| A4 (Parent Refs) | Ensure 0AGNOSTIC.md has proper Parent + Pointers |
| A5 (JSON-LD) | Add to .gab.jsonld mode constraints |
| A6 (Integration) | Regenerate .integration.md from .gab.jsonld |
| A8 (.0agnostic/) | Add to rules/ or knowledge/ |

---

<!-- section_id: "aa018877-321b-41cd-823f-7428d09fc641" -->
## Measurement

Avenue coverage is tested by `test_avenue_coverage_functional.sh`:
- Checks each avenue for functional content (not just directory existence)
- Reports PASS / SCAFFOLDED / FAIL per avenue
- Calculates overall coverage percentage

**Target**: 100% PASS on all 8 avenues (SCAFFOLDED is acceptable for episodic memory on first use)

---

<!-- section_id: "76b388e3-77f6-4f70-8c7c-93a1df0bc540" -->
## Related Principles

- Chain Continuity — avenue A4 depends on unbroken parent chains
- Graceful Degradation — redundancy enables degradation rather than failure
