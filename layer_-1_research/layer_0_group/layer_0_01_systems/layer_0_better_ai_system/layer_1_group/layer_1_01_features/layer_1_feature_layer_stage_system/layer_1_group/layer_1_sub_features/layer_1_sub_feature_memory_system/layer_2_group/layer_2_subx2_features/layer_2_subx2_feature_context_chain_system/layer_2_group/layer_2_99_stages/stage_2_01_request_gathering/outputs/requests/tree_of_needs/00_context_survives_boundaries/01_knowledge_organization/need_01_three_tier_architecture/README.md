---
resource_id: "d493d706-1cfd-4000-b52d-0d61c66120dc"
resource_type: "readme
output"
resource_name: "README"
---
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
- The 19:1 compression ratio (5,000 lines to 260 lines) means agents regain competence in minutes, not hours
- Clear tier boundaries prevent the "two sources of truth" problem
- Matches the brain's consolidation pattern (episodic to semantic to executive pointers)

---

## Acceptance Criteria

- [ ] Tier boundary rules are documented and unambiguous
- [ ] Knowledge file template exists and is followed by all new knowledge files
- [ ] 0AGNOSTIC.md contains only pointers, never substantive content
- [ ] An agent reading only Tier 1 + Tier 2 can work competently (without Tier 3)
- [ ] Anti-patterns are documented with examples of what NOT to do

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Research References

- `memory_system/stage_1_02_research/outputs/by_topic/20_three_tier_knowledge_architecture.md` — full design
- `memory_system/stage_1_02_research/outputs/by_topic/04_memory_dynamics_and_operations.md` — consolidation theory
