---
resource_id: "ece7fe28-a5f9-414f-9cf5-b0f1a3025f13"
resource_type: "readme_output"
resource_name: "README"
---
# Need: Agent Hierarchy

**Branch**: [03_coordination_patterns](../)
**Question**: "Who manages whom in the agent tree?"
**Version**: 1.0.0

---

<!-- section_id: "3001aa13-b5e6-4d0d-8ef3-5ddc1d9155c1" -->
## Definition

The agent hierarchy defines clear parent-child management relationships between agents. Entity managers manage their stages and their child entities. Stage agents report to their entity manager. The hierarchy follows the layer-stage entity tree.

---

<!-- section_id: "1925b217-aa2c-484e-9747-161095a03840" -->
## Why This Matters

- Without a clear hierarchy, agents compete for scope or leave gaps
- Managers must know which agents are "theirs" to manage effectively
- Stage agents must know who they report to and who can give them direction
- The hierarchy prevents circular dependencies and conflicting instructions

---

<!-- section_id: "14beb5d1-acd1-4708-8a27-2959f862905e" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

---

<!-- section_id: "9ac8969f-1c10-40e0-bee6-3d4b5852d731" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "56cc24dc-3e15-4e9f-8c28-d1b50a2be71b" -->
## Acceptance Criteria

- [ ] Agent hierarchy matches the entity tree structure
- [ ] Each entity has exactly one manager with defined authority
- [ ] Stage agents report to their entity manager only
- [ ] Escalation paths are documented from any agent level
- [ ] Hierarchy is discoverable from any agent's 0AGNOSTIC.md

---

<!-- section_id: "07381612-0e4e-41c8-9d62-e393379cafd2" -->
## Research References

- Entity structure: `organization/entities/` -- how entities are structured hierarchically
- GAB agent definitions: `.gab.jsonld` files define orchestrator agents per entity
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md`
