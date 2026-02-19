# Need: Three-Tier Architecture

**Branch**: [01_knowledge_organization](../)
**Question**: "What goes in each tier, and what are the rules?"
**Version**: 1.0.0

---

## Definition

Knowledge is organized into three tiers with clear boundaries:
- **Tier 1 (Pointers)**: 0AGNOSTIC.md / CLAUDE.md — identity, scope, "where to find things"
- **Tier 2 (Distilled)**: .0agnostic/knowledge/ — actionable summaries, principles, decisions
- **Tier 3 (Full)**: stage_*/outputs/ — complete research, designs, raw analysis

Each tier serves a different access pattern and has strict rules about what belongs there.

---

## Why This Matters

- Without tiers, agents either load everything (overflow) or nothing (incompetence)
- The 19:1 compression ratio (5,000 lines → 260 lines) means agents regain competence in minutes, not hours
- Clear tier boundaries prevent the "two sources of truth" problem
- Matches the brain's consolidation pattern (episodic → semantic → executive pointers)

---

## Requirements

### Tier Definitions
- MUST define exactly what content belongs in each tier
- MUST define what content does NOT belong in each tier (anti-patterns)
- MUST define the directional flow: stages → knowledge → pointers (not the reverse)
- MUST define size budgets per tier (lean static context principle)

### Knowledge File Standards
- MUST define a standard template for .0agnostic/knowledge/ files
- MUST require knowledge files to include references to source stage outputs
- MUST NOT allow knowledge files to be copies of stage outputs (distill, don't duplicate)
- SHOULD define naming conventions for knowledge files

### Pointer Standards
- MUST keep 0AGNOSTIC.md limited to identity, pointers, and triggers
- MUST NOT put substantive content in 0AGNOSTIC.md
- SHOULD point to both knowledge files and stage output index

---

## Acceptance Criteria

- [ ] Tier boundary rules are documented and unambiguous
- [ ] Knowledge file template exists and is followed by all new knowledge files
- [ ] 0AGNOSTIC.md contains only pointers, never substantive content
- [ ] An agent reading only Tier 1 + Tier 2 can work competently (without Tier 3)
- [ ] Anti-patterns are documented with examples of what NOT to do

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- `memory_system/stage_2_02_research/outputs/by_topic/20_three_tier_knowledge_architecture.md` — full design
- `memory_system/stage_2_02_research/outputs/by_topic/04_memory_dynamics_and_operations.md` — consolidation theory
