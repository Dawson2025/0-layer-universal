# US-3: Sub-feature agent sees its own tree

**Need**: [Agent Context Model](../README.md)

---

**As a** user who tells the AI to work on a specific sub-feature,
**I want** the sub-feature agent to see only its own entity and stages, not sibling entities,
**So that** the AI stays focused on the sub-feature I asked about and does not get distracted.

### What Happens

1. User says "work on the memory system sub-feature"
2. System spawns a sub-feature agent for the memory system
3. Sub-feature agent's context includes: its own entity identity, its own stages, and parent context
4. Sub-feature agent's context does NOT include sibling entities (e.g., multi-agent system internals)
5. Agent focuses entirely on its own scope without distraction from unrelated entities

### Acceptance Criteria

- Sub-feature agent's context excludes all sibling entity details
- Agent loads only its own entity identity and its own stages
- User can trust the agent is scoped to the sub-feature they requested
