---
resource_id: "9a0ce052-6d22-4b59-b31d-bbd097edaba5"
resource_type: "knowledge"
resource_name: "cross_layer_stage_references"
---
# Topic: Cross-Layer Stage References

## Summary

When content at one layer becomes detailed enough to warrant its own entity (child layer), both layers must maintain **bidirectional references** between their stages. The parent layer's stages contain overviews and summaries pointing down to the child entity's stages where the detailed work lives. The child entity's 0AGNOSTIC.md points up to the parent layer's stages that provide broader context and the original requirements.

This is the three-tier knowledge principle applied recursively across the layer hierarchy: the parent stage is the "pointer tier" for its child's detailed work.

## When to Push to a Child Layer

- **Depth of detail**: Multiple files needed, deep investigation required
- **Scope independence**: Can be worked on independently of parent work
- **Stage breadth**: Needs its own full stage progression (01-11)
- **Agent specialization**: Needs a specialized agent with domain knowledge

## Key Points

- Formalized as **Principle 10** in the Stage Delegation Principles
- Parent stages have "Child Layer Detail" sections pointing down
- Child entities have "Parent Layer Context" sections pointing up
- Cross-stage traceability extends across layers: a need at parent → research/design/development at child
- Without bidirectional references, agents either don't know child layers exist (lost detail) or don't know where their work fits (lost context)

## Applied In This Entity

| Parent Stage | Points Down To |
|-------------|----------------|
| Stage 01 (needs) | Branch 02 → memory_system, Branch 02/need_01 → context_chain_system, Branch 03 → multi_agent_system |
| Stage 02 (research) | context_chain_system (primary research vehicle), memory_system (memory architecture research) |
| Stage 04 (design) | context_chain_system (all design decisions applied), memory_system & multi_agent_system (design decisions applied) |
| Stage 06 (development) | context_chain_system (working example, 76 PASS), memory_system & multi_agent_system (use universal artifacts) |

## References

| What | Where |
|------|-------|
| Principle 10 (Cross-Layer Stage References) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Stage 01 child layer detail | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/0AGNOSTIC.md` → Child Layer Detail section |
| memory_system parent context | `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/0AGNOSTIC.md` → Parent Layer Context section |
| multi_agent_system parent context | `../../../../../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_multi_agent_system/0AGNOSTIC.md` → Parent Layer Context section |
| context_chain_system parent context | `.../context_chain_system/0AGNOSTIC.md` → Parent Layer Context section |
