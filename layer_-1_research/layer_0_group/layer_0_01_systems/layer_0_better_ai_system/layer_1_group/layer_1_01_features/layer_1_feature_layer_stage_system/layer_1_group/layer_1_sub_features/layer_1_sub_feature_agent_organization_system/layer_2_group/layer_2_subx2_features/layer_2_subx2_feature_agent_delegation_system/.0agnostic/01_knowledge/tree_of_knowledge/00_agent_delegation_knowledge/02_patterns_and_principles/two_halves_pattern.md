---
resource_id: "92dfafad-7452-48ff-a713-3901e0a10b37"
resource_type: "knowledge"
resource_name: "two_halves_pattern"
---
# Topic: Two-Halves Context Pattern

<!-- section_id: "5096a10d-037f-4157-9a5e-26989c422c94" -->
## Summary

Every 0AGNOSTIC.md (whether for an entity or a stage) needs **two halves**:

1. **Operational Guidance** (written once, rarely changes): Identity, scope boundaries (IS/IS NOT), methodology, domain context pointers, success criteria, exit protocol
2. **Current State Summary** (updated as work progresses): Status, summary, key outputs, key findings, open items, handoff status

Without the current state half, an agent landing in a stage must explore outputs/ manually — wasting context window tokens on orientation instead of productive work. With both halves, the 0AGNOSTIC.md is the single file an agent reads to be immediately oriented and productive.

<!-- section_id: "16db5f0d-ba79-4923-b83b-3d6b6016293f" -->
## Discovery

Discovered during Stage 02 research (via the context_chain_system working example). Observed that agents reading only the operational half of a stage 0AGNOSTIC.md still didn't know what work had been done — they had to manually explore outputs/ to understand the current state.

<!-- section_id: "8c2f425c-01d6-4bd1-b4ee-e2b5c625716d" -->
## Key Points

- Formalized as **Principle 9** in the Stage Delegation Principles
- Applied to both entity-level and stage-level 0AGNOSTIC.md files
- The operational half tells the agent **how to work**; the current state half tells it **what's already here**
- The universal STAGE_AGENT_TEMPLATE.md includes the Current State section

<!-- section_id: "c9bd39e8-3d0c-4112-b094-62b617dae5cb" -->
## References

| What | Where |
|------|-------|
| Principle 9 (Two-Halves Context Pattern) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Universal stage agent template | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| Discovery context (research) | Stage 02: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/0AGNOSTIC.md` → Key Findings |
| Design decision | Stage 04: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/0AGNOSTIC.md` → Key Design Decisions table |
| Things learned doc | `../../things_learned/docs/stage_0agnostic_pattern.md` |
