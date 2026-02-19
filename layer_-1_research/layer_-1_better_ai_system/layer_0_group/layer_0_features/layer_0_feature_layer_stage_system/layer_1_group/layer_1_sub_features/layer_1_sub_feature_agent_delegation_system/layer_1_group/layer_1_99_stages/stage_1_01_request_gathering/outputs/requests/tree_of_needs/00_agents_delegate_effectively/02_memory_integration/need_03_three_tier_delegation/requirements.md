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

### Tier-to-Agent Mapping
- MUST define which tier each agent type primarily operates at:
  - Manager: Tier 1 (pointers) -- 0AGNOSTIC.md, stage overview, children list
  - Stage Agent: Tier 2 (distilled) -- .0agnostic/knowledge/ files relevant to the task
  - Active Stage Agent: Tier 3 (full) -- stage outputs it is currently producing or consuming
- MUST NOT have managers routinely access Tier 3 content
- MUST NOT have stage agents routinely access Tier 3 content from other stages

### Delegation-Aware Tiering
- MUST ensure that delegation decisions can be made from Tier 1 alone (managers never need to read Tier 3 to decide what to delegate)
- MUST ensure that stage agents can do their work with Tier 2 + their own Tier 3 (no dependency on other stages' Tier 3)
- SHOULD define when an agent legitimately needs to access a higher-detail tier (escalation, cross-stage dependency)

### Tier Integrity
- MUST ensure Tier 1 (pointers) is always current -- if a stage report updates, the manager's view updates
- MUST ensure Tier 2 (distilled) is produced from Tier 3 (consolidation), not duplicated
- MUST NOT allow Tier 2 to become a copy of Tier 3 -- distillation is required

---

## Acceptance Criteria

- [ ] Tier-to-agent mapping is documented and unambiguous
- [ ] Manager can make delegation decisions from Tier 1 alone
- [ ] Stage agents can do their work from Tier 2 + their own Tier 3
- [ ] Escalation paths are defined for when an agent needs a higher-detail tier
- [ ] Tier 2 content is distilled from Tier 3, not duplicated

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Context chain system: `00_context_survives_boundaries/01_knowledge_organization/need_01_three_tier_architecture/`
- Memory system research on three-tier knowledge architecture
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- three-tier knowledge definition
