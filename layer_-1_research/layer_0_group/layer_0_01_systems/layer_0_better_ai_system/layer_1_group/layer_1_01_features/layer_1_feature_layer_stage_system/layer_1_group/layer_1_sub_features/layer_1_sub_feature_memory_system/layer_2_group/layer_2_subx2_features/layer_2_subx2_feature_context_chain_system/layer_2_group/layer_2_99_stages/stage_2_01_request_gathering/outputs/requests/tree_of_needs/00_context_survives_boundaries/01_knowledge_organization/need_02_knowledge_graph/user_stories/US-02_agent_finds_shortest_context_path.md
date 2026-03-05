---
resource_id: "03b34c7b-b44e-4c1c-8e1c-b33611c46091"
resource_type: "output"
resource_name: "US-02_agent_finds_shortest_context_path"
---
# US-02: Agent finds shortest context path

**Need**: [Knowledge Graph](../README.md)

---

**As a** user who asks the AI to use information from a distant part of the system,
**I want** the AI to find the most direct path to that context instead of walking the entire tree,
**So that** it loads minimum context and doesn't waste my token budget on irrelevant files.

### What Happens

1. User asks the AI something that requires context from a distant entity (e.g., asking about research while working in design)
2. Agent uses graph traversal to find the shortest typed path between current entity and target
3. Agent loads only the files along that path, skipping unrelated branches
4. User gets the answer without the AI needing to read the entire hierarchy

### Acceptance Criteria

- Graph traversal returns a typed path between any two entities
- Path uses minimum intermediate nodes
- Agent loads fewer files than a brute-force tree walk would require
