# Topic: Stage Delegation

## Summary

Stage delegation is the core pattern: entity managers delegate work to stage-specialized agents. Each stage agent has its own 0AGNOSTIC.md that defines its identity, methodology, scope (IS and IS NOT), and success criteria. Managers don't carry stage-level operational knowledge — they coordinate via stage reports.

The pattern prevents context overflow: instead of one agent trying to hold requirements + research + design + development, each stage agent loads only what it needs.

## Key Points

- Managers delegate, agents operate (Principle 1)
- Every stage agent has a 0AGNOSTIC.md with the two-halves pattern (Principle 9)
- Explicit scope boundaries with IS/IS NOT lists prevent scope creep (Principle 2)
- Stages are reentrant — can loop back from testing to design (Principle 5)

## References

| What | Where |
|------|-------|
| Design decision: stage delegation model | Stage 04: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/0AGNOSTIC.md` → Key Design Decisions table |
| Universal stage guides (11) | `layer_0/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_NN_NAME.md` |
| Stage agent template | `layer_0/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| Principle 1 (Managers Delegate) | `layer_0/.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Stage 01 requirements (need_01) | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/00_agents_delegate_effectively/01_delegation_model/need_01_stage_delegation/` |
