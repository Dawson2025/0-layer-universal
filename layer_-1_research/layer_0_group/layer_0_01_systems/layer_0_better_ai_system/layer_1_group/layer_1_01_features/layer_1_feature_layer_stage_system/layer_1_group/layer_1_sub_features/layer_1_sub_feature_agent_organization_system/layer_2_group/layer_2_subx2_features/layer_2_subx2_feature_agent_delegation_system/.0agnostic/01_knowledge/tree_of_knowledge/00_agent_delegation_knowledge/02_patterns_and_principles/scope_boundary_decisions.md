---
resource_id: "b2e07bcb-c9c7-45b9-a83b-775847e15a6c"
resource_type: "knowledge"
resource_name: "scope_boundary_decisions"
---
# Topic: Scope Boundary Decisions

<!-- section_id: "567ee69c-2cc5-4738-aeca-e82b22c4d4d9" -->
## Summary

When an agent reaches the boundary of its layer or stage scope, it must make a **delegation decision** with three options:

1. **Do it yourself** — when the out-of-scope work is small and tightly coupled to the current task
2. **Delegate to existing agent** — when the work is significant and an agent already exists for the target scope
3. **Instantiate a new agent** — when the work is significant but no agent has been instantiated for the target layer/stage yet

The default should be **delegate**. The key factor driving the decision is **context window preservation**: an agent that tries to work across too many layers/stages will overflow its context, lose track of its methodology, and produce lower-quality work.

Scope boundaries exist at two levels: **stage boundaries** (work belonging to another stage within the same entity) and **layer boundaries** (work belonging to a sibling, parent, or child entity).

<!-- section_id: "aa9c499d-39f6-47c6-acbf-4c13311b7664" -->
## Discovery

Discovered through practice: agents working in one stage would naturally encounter work belonging to other stages or entities. Without a framework for making the decision, agents would either try to do everything (context overflow) or hand off everything (even trivial work).

<!-- section_id: "3b04049e-3465-419c-811d-7be5adbb0951" -->
## Key Points

- Formalized as **Principle 8** in the Stage Delegation Principles
- Codified as the **Scope Boundary Rule** (expanded from the original Stage Boundary Rule)
- Decision factors: size of work, coupling, context window capacity, whether an agent exists, domain knowledge needed
- Default is always delegate — spawning an agent is cheap, confused context is expensive

<!-- section_id: "c8bdec9e-12ed-455b-8ab7-c5aacb5f10f4" -->
## References

| What | Where |
|------|-------|
| Principle 8 (Scope Boundary Decisions) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Scope Boundary Rule | `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md` |
| Design decision | Stage 04: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/0AGNOSTIC.md` → Key Design Decisions table |
| Things learned doc | `../../things_learned/docs/stage_0agnostic_pattern.md` (second section) |
| Stage 01 requirements (coordination) | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/00_agents_delegate_effectively/03_coordination_patterns/` |
