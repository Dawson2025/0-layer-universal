---
resource_id: "5d758ed6-d48b-413c-80e0-750ed96eefc6"
resource_type: "knowledge"
resource_name: "stage_delegation"
---
# Topic: Stage Delegation

<!-- section_id: "1f60a3a3-2614-4a69-94d7-9c43a5795e68" -->
## Summary

Stage delegation is the core pattern: entity managers delegate work to stage-specialized agents. Each stage agent has its own 0AGNOSTIC.md that defines its identity, methodology, scope (IS and IS NOT), and success criteria. Managers don't carry stage-level operational knowledge — they coordinate via stage reports.

The pattern prevents context overflow: instead of one agent trying to hold requirements + research + design + development, each stage agent loads only what it needs.

<!-- section_id: "b0faf762-64ef-4299-ac7b-82e0f88cf193" -->
## Key Points

- Managers delegate, agents operate (Principle 1)
- Every stage agent has a 0AGNOSTIC.md with the two-halves pattern (Principle 9)
- Explicit scope boundaries with IS/IS NOT lists prevent scope creep (Principle 2)
- Stages are reentrant — can loop back from testing to design (Principle 5)

<!-- section_id: "e83c61e7-1ab2-461a-84b9-e5250e3a0d6d" -->
## References

| What | Where |
|------|-------|
| Design decision: stage delegation model | Stage 04: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/0AGNOSTIC.md` → Key Design Decisions table |
| Universal stage guides (11) | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_NN_NAME.md` |
| Stage agent template | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| Principle 1 (Managers Delegate) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Stage 01 requirements (need_01) | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/00_agents_delegate_effectively/01_delegation_model/need_01_stage_delegation/` |
