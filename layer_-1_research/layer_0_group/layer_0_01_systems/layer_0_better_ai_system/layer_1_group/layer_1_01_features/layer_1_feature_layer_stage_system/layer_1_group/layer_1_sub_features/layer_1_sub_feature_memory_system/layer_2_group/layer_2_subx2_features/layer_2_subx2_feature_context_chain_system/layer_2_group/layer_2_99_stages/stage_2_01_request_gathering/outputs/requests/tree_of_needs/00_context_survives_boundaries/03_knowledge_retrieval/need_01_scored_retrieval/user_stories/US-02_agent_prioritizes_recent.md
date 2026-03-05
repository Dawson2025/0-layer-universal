---
resource_id: "d7bbd097-0fc5-4b05-a80a-fa05450fabda"
resource_type: "output"
resource_name: "US-02_agent_prioritizes_recent"
---
# US-02: Agent prioritizes recent over stale

**Need**: [Scored Context Retrieval](../README.md)

---

**As a** user working on an active design task with the AI,
**I want** the system to prioritize recently updated files over old ones,
**So that** the AI works with current information instead of outdated research from months ago.

<!-- section_id: "15fe5ae4-b436-40de-a256-38bf8b55fc53" -->
### What Happens

1. User tells the AI to work on an active task (e.g., design iteration)
2. Scoring function weights recently updated files higher than old ones
3. Agent loads current design files before older research files
4. User gets work based on the latest decisions, not superseded earlier thinking

<!-- section_id: "00d0a4f4-85d3-4c6f-bd7a-6bd28ef80c68" -->
### Acceptance Criteria

- Recency factor visibly affects file ranking (recently updated files score higher)
- A file updated today scores higher than an equivalent file last updated 3 months ago
- Agent's loaded context reflects current state, not historical state
