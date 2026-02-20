# US-03: Script regenerates graph after changes

**Need**: [Knowledge Graph](../README.md)

---

**As a** user who just created a new entity,
**I want** to run a script that regenerates the knowledge graph automatically,
**So that** the new entity appears in the graph without me editing JSON-LD by hand.

### What Happens

1. User creates a new entity (with 0AGNOSTIC.md declaring its relationships)
2. User runs the graph regeneration script
3. Script parses all 0AGNOSTIC.md files and outputs valid JSON-LD
4. New entity and its relationships appear in the graph, ready for agents to use

### Acceptance Criteria

- Script parses all 0AGNOSTIC.md files and outputs valid JSON-LD
- Script is idempotent (running it twice produces the same result)
- No manual JSON-LD editing required after entity creation
