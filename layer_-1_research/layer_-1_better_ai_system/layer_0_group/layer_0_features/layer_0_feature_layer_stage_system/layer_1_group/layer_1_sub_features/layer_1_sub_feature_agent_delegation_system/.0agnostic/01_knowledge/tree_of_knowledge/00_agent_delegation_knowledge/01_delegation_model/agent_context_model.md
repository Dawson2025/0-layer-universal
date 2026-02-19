# Topic: Agent Context Model

## Summary

The agent context model defines what each agent type (entity manager, stage agent, sub-feature agent) knows in its static context vs what it loads on demand. This follows the three-tier knowledge principle: pointers load automatically, distilled knowledge loads on demand, full detail stays within stages.

The critical insight is that managers work at the pointer tier — they read 0AGNOSTIC.md and stage reports. Stage agents load distilled knowledge from .0agnostic/ on demand. Full detail (research outputs, design specs, test results) stays within stage output directories.

## Key Points

- Entity managers: static context = 0AGNOSTIC.md, dynamic = stage reports + .0agnostic/ summaries
- Stage agents: static context = stage 0AGNOSTIC.md, dynamic = parent .0agnostic/ knowledge, sibling stage outputs
- Context window is finite — every loaded byte must earn its place (Principle 7)

## References

| What | Where |
|------|-------|
| Design decision: agent context model | Stage 04: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/0AGNOSTIC.md` → Key Design Decisions table |
| Principle 3 (Three-Tier Knowledge) | `layer_0/.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Principle 7 (Selective Context Loading) | Same file |
| Stage 01 requirements (need_03) | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/00_agents_delegate_effectively/01_delegation_model/need_03_agent_context_model/` |
| Research findings on context model | Stage 02: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/0AGNOSTIC.md` → Key Findings |
