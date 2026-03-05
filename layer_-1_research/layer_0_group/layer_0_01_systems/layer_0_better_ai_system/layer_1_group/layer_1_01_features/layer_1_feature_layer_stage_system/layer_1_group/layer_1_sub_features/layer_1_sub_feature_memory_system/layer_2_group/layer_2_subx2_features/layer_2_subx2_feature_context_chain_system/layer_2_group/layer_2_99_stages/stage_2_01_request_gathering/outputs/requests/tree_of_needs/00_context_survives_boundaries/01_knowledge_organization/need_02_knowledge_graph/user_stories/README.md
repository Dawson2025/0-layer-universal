---
resource_id: "af551ab3-8096-4453-b291-ae9dd4ea3b95"
resource_type: "readme
output"
resource_name: "README"
---
# Knowledge Graph -- User Stories Index

**Need**: [Knowledge Graph](../README.md)

## Overview

These stories cover how entity relationships are formalized into an explicit JSON-LD knowledge graph and how that graph is used in practice. They validate that agents can discover related entities through graph traversal, that agents find the shortest path to relevant context, that the graph regenerates automatically after structural changes, and that the developer can validate the integrity of the full relationship web.

## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Agent discovers related entities | Agent uses the graph to find entities connected to its current scope | [US-01_agent_discovers_related_entities.md](./US-01_agent_discovers_related_entities.md) |
| US-02 | Agent finds shortest context path | Agent traverses the graph to locate the most direct route to needed context | [US-02_agent_finds_shortest_context_path.md](./US-02_agent_finds_shortest_context_path.md) |
| US-03 | Script regenerates graph after changes | Automated script rebuilds the graph when entity structure changes | [US-03_script_regenerates_graph.md](./US-03_script_regenerates_graph.md) |
| US-04 | Developer validates chain integrity | Developer runs validation against the graph to check relationship correctness | [US-04_developer_validates_chain_integrity.md](./US-04_developer_validates_chain_integrity.md) |
