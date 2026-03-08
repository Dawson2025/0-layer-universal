---
resource_id: "798d96cf-3991-49ec-b827-29b1d8d71419"
resource_type: "readme_output"
resource_name: "README"
---
# Need: Three-Tier Delegation

**Branch**: [02_memory_integration](../)
**Question**: "How does the three-tier pattern (pointers, distilled, full) apply to delegation context?"
**Version**: 1.0.0

---

<!-- section_id: "01b58a0b-65dc-4792-8822-ee85a07c178d" -->
## Definition

The three-tier knowledge pattern (pointers -> distilled -> full) directly supports delegation by giving each agent type access to the right tier. Managers work at the pointer tier (0AGNOSTIC.md, stage overview). Stage agents work at the distilled tier (.0agnostic/knowledge/). Full detail lives in stage outputs and is accessed only when needed.

---

<!-- section_id: "6f3962e1-b485-4d07-b6e6-3fe7fd108412" -->
## Why This Matters

- The three-tier pattern was designed for knowledge organization, but it maps perfectly to delegation
- Managers need pointers (what exists, where to find it) -- not full detail
- Stage agents need distilled knowledge (actionable summaries) -- not raw research
- Full content (stage outputs) should only be loaded by the agent actively working on that stage
- Mismatching tier to agent type is the root cause of context overflow

---

<!-- section_id: "bd0c37c9-3dbb-494c-8965-dc840b4dbdca" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

---

<!-- section_id: "edfe9131-3eeb-4ed9-b2a2-d48230aa75f3" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "432e9c54-e7c0-4af8-9c2c-3036da67c2cd" -->
## Acceptance Criteria

- [ ] Tier-to-agent mapping is documented and unambiguous
- [ ] Manager can make delegation decisions from Tier 1 alone
- [ ] Stage agents can do their work from Tier 2 + their own Tier 3
- [ ] Escalation paths are defined for when an agent needs a higher-detail tier
- [ ] Tier 2 content is distilled from Tier 3, not duplicated

---

<!-- section_id: "9817e117-b52a-4efa-82d3-9b1a0015dded" -->
## Research References

- Context chain system: `00_context_survives_boundaries/01_knowledge_organization/need_01_three_tier_architecture/`
- Memory system research on three-tier knowledge architecture
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- three-tier knowledge definition
