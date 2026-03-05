---
resource_id: "36177f83-a610-4cd3-86cf-e5b8da206ba4"
resource_type: "readme
output"
resource_name: "README"
---
# Three-Tier Architecture -- User Stories Index

**Need**: [Three-Tier Architecture](../README.md)

<!-- section_id: "b67ff1af-c9cb-4aef-af16-f268c20dd10f" -->
## Overview

These stories cover the end-to-end experience of agents and developers working with the three-tier knowledge system (pointers, distilled, full). They validate that agents regain competence quickly after context compaction by reading only Tiers 1 and 2, that agents can navigate from pointers to detailed sources when needed, that developers know which tier to place new content in, and that newly created entities follow the pattern consistently.

<!-- section_id: "db1f160a-9135-49db-b2f0-bb6a4fe1fe94" -->
## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Agent regains competence after compaction | Agent reads Tier 1 + 2 to become operational after context loss | [US-01_agent_regains_competence.md](./US-01_agent_regains_competence.md) |
| US-02 | Agent knows where to find details | Agent follows Tier 2 references to locate Tier 3 sources | [US-02_agent_finds_details.md](./US-02_agent_finds_details.md) |
| US-03 | Developer knows what goes where | Developer decides correct tier placement for new content | [US-03_developer_knows_placement.md](./US-03_developer_knows_placement.md) |
| US-04 | New entity follows the pattern | Developer creates a new entity with all three tiers structured correctly | [US-04_new_entity_follows_pattern.md](./US-04_new_entity_follows_pattern.md) |
