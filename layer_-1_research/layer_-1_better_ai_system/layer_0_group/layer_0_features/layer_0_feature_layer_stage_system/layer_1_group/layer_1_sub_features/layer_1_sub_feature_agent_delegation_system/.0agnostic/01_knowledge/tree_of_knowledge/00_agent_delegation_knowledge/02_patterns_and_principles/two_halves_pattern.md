# Topic: Two-Halves Context Pattern

## Summary

Every 0AGNOSTIC.md (whether for an entity or a stage) needs **two halves**:

1. **Operational Guidance** (written once, rarely changes): Identity, scope boundaries (IS/IS NOT), methodology, domain context pointers, success criteria, exit protocol
2. **Current State Summary** (updated as work progresses): Status, summary, key outputs, key findings, open items, handoff status

Without the current state half, an agent landing in a stage must explore outputs/ manually — wasting context window tokens on orientation instead of productive work. With both halves, the 0AGNOSTIC.md is the single file an agent reads to be immediately oriented and productive.

## Discovery

Discovered during Stage 02 research (via the context_chain_system working example). Observed that agents reading only the operational half of a stage 0AGNOSTIC.md still didn't know what work had been done — they had to manually explore outputs/ to understand the current state.

## Key Points

- Formalized as **Principle 9** in the Stage Delegation Principles
- Applied to both entity-level and stage-level 0AGNOSTIC.md files
- The operational half tells the agent **how to work**; the current state half tells it **what's already here**
- The universal STAGE_AGENT_TEMPLATE.md includes the Current State section

## References

| What | Where |
|------|-------|
| Principle 9 (Two-Halves Context Pattern) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Universal stage agent template | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| Discovery context (research) | Stage 02: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/0AGNOSTIC.md` → Key Findings |
| Design decision | Stage 04: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/0AGNOSTIC.md` → Key Design Decisions table |
| Things learned doc | `../../things_learned/docs/stage_0agnostic_pattern.md` |
