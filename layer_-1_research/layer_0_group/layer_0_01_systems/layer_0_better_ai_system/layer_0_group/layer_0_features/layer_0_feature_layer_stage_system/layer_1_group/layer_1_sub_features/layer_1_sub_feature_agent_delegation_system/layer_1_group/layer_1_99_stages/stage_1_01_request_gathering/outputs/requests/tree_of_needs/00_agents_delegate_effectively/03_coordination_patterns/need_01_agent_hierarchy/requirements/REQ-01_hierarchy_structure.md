# Hierarchy Structure

**Need**: [Agent Hierarchy](../README.md)

---

- MUST define a 1:1 mapping between entity tree and agent management tree
- MUST define that each entity has exactly one manager agent
- MUST define that each stage has exactly one stage agent (at a time)
- MUST define parent-child relationships: entity manager -> stage agents, entity manager -> child entity managers
- MUST NOT allow stage agents to manage other stage agents (flat within an entity)
