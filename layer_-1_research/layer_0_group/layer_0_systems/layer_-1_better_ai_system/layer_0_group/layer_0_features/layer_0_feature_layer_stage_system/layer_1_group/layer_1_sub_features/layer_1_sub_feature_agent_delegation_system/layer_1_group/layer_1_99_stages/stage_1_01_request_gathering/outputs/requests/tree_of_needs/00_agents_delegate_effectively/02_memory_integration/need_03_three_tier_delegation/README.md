# Need: Three-Tier Delegation

**Branch**: [02_memory_integration](../)
**Question**: "How does the three-tier pattern (pointers, distilled, full) apply to delegation context?"
**Version**: 1.0.0

---

## Definition

The three-tier knowledge pattern (pointers -> distilled -> full) directly supports delegation by giving each agent type access to the right tier. Managers work at the pointer tier (0AGNOSTIC.md, stage overview). Stage agents work at the distilled tier (.0agnostic/knowledge/). Full detail lives in stage outputs and is accessed only when needed.

---

## Why This Matters

- The three-tier pattern was designed for knowledge organization, but it maps perfectly to delegation
- Managers need pointers (what exists, where to find it) -- not full detail
- Stage agents need distilled knowledge (actionable summaries) -- not raw research
- Full content (stage outputs) should only be loaded by the agent actively working on that stage
- Mismatching tier to agent type is the root cause of context overflow

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] Tier-to-agent mapping is documented and unambiguous
- [ ] Manager can make delegation decisions from Tier 1 alone
- [ ] Stage agents can do their work from Tier 2 + their own Tier 3
- [ ] Escalation paths are defined for when an agent needs a higher-detail tier
- [ ] Tier 2 content is distilled from Tier 3, not duplicated

---

## Research References

- Context chain system: `00_context_survives_boundaries/01_knowledge_organization/need_01_three_tier_architecture/`
- Memory system research on three-tier knowledge architecture
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- three-tier knowledge definition
