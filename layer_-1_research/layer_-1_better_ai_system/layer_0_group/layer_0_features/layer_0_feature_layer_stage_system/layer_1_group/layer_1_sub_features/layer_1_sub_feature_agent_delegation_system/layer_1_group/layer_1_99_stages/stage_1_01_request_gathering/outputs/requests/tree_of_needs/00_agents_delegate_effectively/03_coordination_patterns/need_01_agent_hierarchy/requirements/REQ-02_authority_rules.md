# Authority Rules

**Need**: [Agent Hierarchy](../README.md)

---

- MUST define what decisions each agent level can make independently
- MUST define what decisions require escalation to the parent manager
- MUST define that stage agents cannot make cross-stage decisions (scope violation)
- SHOULD define that child entity managers can escalate to parent entity manager
- MUST NOT allow child entity managers to direct sibling entity managers
