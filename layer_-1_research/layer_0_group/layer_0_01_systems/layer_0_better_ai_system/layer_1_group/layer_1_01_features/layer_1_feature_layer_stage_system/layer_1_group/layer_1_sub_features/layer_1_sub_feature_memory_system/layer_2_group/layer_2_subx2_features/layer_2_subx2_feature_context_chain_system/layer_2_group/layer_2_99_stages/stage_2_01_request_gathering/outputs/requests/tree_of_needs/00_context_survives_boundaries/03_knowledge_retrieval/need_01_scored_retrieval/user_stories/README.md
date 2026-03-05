---
resource_id: "b89a0594-e0e6-44b4-8a02-f231faf094fd"
resource_type: "readme
output"
resource_name: "README"
---
# Scored Context Retrieval -- User Stories Index

**Need**: [Scored Context Retrieval](../README.md)

## Overview

These stories cover the replacement of manual file selection with scored retrieval that ranks available context by recency, relevance, and importance. They validate that agents automatically load the most relevant context when entering an entity, that recent content is prioritized over stale content in the ranking, and that the developer can tune the scoring weights to adjust retrieval behavior as the system evolves.

## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Agent loads most relevant context on entry | Agent receives top-scored files automatically when entering an entity | [US-01_agent_loads_relevant_context.md](./US-01_agent_loads_relevant_context.md) |
| US-02 | Agent prioritizes recent over stale | Scoring ranks recently updated content higher than older material | [US-02_agent_prioritizes_recent.md](./US-02_agent_prioritizes_recent.md) |
| US-03 | Developer tunes scoring weights | Developer adjusts recency, relevance, and importance weights | [US-03_developer_tunes_scoring_weights.md](./US-03_developer_tunes_scoring_weights.md) |
