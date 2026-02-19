# Need: Consolidation Process

**Branch**: [02_knowledge_lifecycle](../)
**Question**: "When and how are stage outputs distilled into knowledge files?"
**Version**: 1.0.0

---

## Definition

A defined process for creating distilled knowledge files (Tier 2) from stage outputs (Tier 3). Consolidation happens at stage boundaries — when research completes, when design is finalized — not continuously.

---

## Why This Matters

- Without consolidation, knowledge files never get created and agents always read raw outputs
- Without triggers, consolidation is forgotten and knowledge drifts from reality
- The 19:1 compression (5,000 → 260 lines) only works if someone actually does the distillation
- Matches brain's sleep consolidation — raw episodes become semantic knowledge at natural boundaries

---

## Requirements

### Trigger Definition
- MUST define when consolidation happens (stage completion, major milestone)
- MUST NOT require continuous maintenance (event-driven, not polling)
- SHOULD integrate into stage-workflow skill transitions

### Consolidation Protocol
- MUST define step-by-step process: read outputs → identify key findings → distill → reference sources → validate
- MUST require knowledge files to be shorter than source outputs (distill, not copy)
- MUST require references back to source stage outputs
- SHOULD provide a checklist for consolidation quality

### Tooling
- SHOULD provide a script or skill to assist with distillation
- SHOULD generate a consolidation report (what was distilled, compression ratio, references)

---

## Acceptance Criteria

- [ ] Triggers are defined and documented
- [ ] Protocol is documented with step-by-step instructions
- [ ] At least one consolidation has been performed (memory_system research → knowledge files)
- [ ] Compression ratio is measurable (source lines → distilled lines)

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- `memory_system/stage_2_02_research/outputs/by_topic/20_three_tier_knowledge_architecture.md` — Section "The Consolidation Process"
- `memory_system/stage_2_02_research/outputs/by_topic/04_memory_dynamics_and_operations.md` — Consolidation theory
- `memory_system/stage_2_02_research/outputs/by_topic/15_vectors_graphs_and_neurology.md` — Sleep replay mechanism
