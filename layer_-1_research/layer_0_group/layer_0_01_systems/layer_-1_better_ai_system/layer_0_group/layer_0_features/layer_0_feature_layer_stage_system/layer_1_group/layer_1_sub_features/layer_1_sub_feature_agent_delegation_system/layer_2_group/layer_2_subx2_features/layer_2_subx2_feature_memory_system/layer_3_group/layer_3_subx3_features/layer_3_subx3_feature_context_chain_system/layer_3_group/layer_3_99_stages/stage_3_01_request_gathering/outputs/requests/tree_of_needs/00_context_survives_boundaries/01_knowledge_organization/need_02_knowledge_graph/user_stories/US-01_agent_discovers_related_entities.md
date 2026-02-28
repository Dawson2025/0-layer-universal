# US-01: Agent discovers related entities

**Need**: [Knowledge Graph](../README.md)

---

**As a** user who tells the AI to work on a specific entity,
**I want** the AI to automatically discover what other entities are related (parent, children, cross-references),
**So that** it loads relevant context without me having to list every related file manually.

### What Happens

1. User tells the AI to work on a specific entity (e.g., "work on the memory system")
2. Agent reads the knowledge graph and identifies parent, children, and cross-referenced entities
3. Agent loads relevant sibling/parent context based on graph relationships
4. User gets informed work that accounts for related entities, not just the immediate one

### Acceptance Criteria

- Agent identifies parent + children + cross-references from the graph in one query
- No manual listing of related files required by the user
- Graph relationships match the actual entity structure on disk
