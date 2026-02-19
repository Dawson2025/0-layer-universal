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

### Hierarchy Structure
- MUST define a 1:1 mapping between entity tree and agent management tree
- MUST define that each entity has exactly one manager agent
- MUST define that each stage has exactly one stage agent (at a time)
- MUST define parent-child relationships: entity manager -> stage agents, entity manager -> child entity managers
- MUST NOT allow stage agents to manage other stage agents (flat within an entity)

### Authority Rules
- MUST define what decisions each agent level can make independently
- MUST define what decisions require escalation to the parent manager
- MUST define that stage agents cannot make cross-stage decisions (scope violation)
- SHOULD define that child entity managers can escalate to parent entity manager
- MUST NOT allow child entity managers to direct sibling entity managers

### Hierarchy Navigation
- MUST make the hierarchy discoverable from any agent's context (who is my manager? who are my direct reports?)
- MUST define hierarchy navigation through 0AGNOSTIC.md (parent pointer, children list)
- SHOULD support hierarchy visualization for developer oversight

---

## Acceptance Criteria

- [ ] Agent hierarchy matches the entity tree structure
- [ ] Each entity has exactly one manager with defined authority
- [ ] Stage agents report to their entity manager only
- [ ] Escalation paths are documented from any agent level
- [ ] Hierarchy is discoverable from any agent's 0AGNOSTIC.md

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Entity structure: `organization/entities/` -- how entities are structured hierarchically
- GAB agent definitions: `.gab.jsonld` files define orchestrator agents per entity
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md`
