# Need: Agent Hierarchy

**Branch**: [03_coordination_patterns](../)
**Question**: "Who manages whom in the agent tree?"
**Version**: 1.0.0

---

## Definition

The agent hierarchy defines clear parent-child management relationships between agents. Entity managers manage their stages and their child entities. Stage agents report to their entity manager. The hierarchy follows the layer-stage entity tree.

---

## Why This Matters

- Without a clear hierarchy, agents compete for scope or leave gaps
- Managers must know which agents are "theirs" to manage effectively
- Stage agents must know who they report to and who can give them direction
- The hierarchy prevents circular dependencies and conflicting instructions

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] Agent hierarchy matches the entity tree structure
- [ ] Each entity has exactly one manager with defined authority
- [ ] Stage agents report to their entity manager only
- [ ] Escalation paths are documented from any agent level
- [ ] Hierarchy is discoverable from any agent's 0AGNOSTIC.md

---

## Research References

- Entity structure: `organization/entities/` -- how entities are structured hierarchically
- GAB agent definitions: `.gab.jsonld` files define orchestrator agents per entity
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md`
