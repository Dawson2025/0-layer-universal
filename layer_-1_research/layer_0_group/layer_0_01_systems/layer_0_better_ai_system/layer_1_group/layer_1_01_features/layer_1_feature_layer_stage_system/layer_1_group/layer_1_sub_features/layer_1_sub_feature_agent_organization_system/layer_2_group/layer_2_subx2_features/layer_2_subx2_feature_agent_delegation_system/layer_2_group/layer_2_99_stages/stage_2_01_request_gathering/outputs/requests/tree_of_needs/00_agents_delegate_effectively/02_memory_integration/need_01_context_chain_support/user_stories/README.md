---
resource_id: "799754a7-5cbb-4cee-80c9-914b80fb85c5"
resource_type: "readme_output"
resource_name: "README"
---
# Context Chain Support -- User Stories Index

**Need**: [Context Chain Support](../README.md)

<!-- section_id: "75d93f41-fa9f-4136-9629-aa679a5a5983" -->
## Overview

These stories cover how automatic context chain traversal provides agents with the hierarchy-level awareness they need for delegation. They validate that managers receive parent identity and scope automatically, that stage agents inherit domain context from their entity, that chain depth is bounded per agent type, and that chains deliver identity pointers rather than full operational detail.

<!-- section_id: "14887ef7-e184-41a5-8060-32f16ae4ec57" -->
## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Manager receives hierarchy context automatically | Chain loads parent identity and scope into manager on entry | [US-01_manager_receives_hierarchy_context.md](./US-01_manager_receives_hierarchy_context.md) |
| US-02 | Stage agent receives parent domain context | Chain provides entity-level domain knowledge to the stage agent | [US-02_stage_agent_receives_parent_context.md](./US-02_stage_agent_receives_parent_context.md) |
| US-03 | Chain stops at the right depth | Chain traversal terminates at the configured depth limit | [US-03_chain_stops_at_right_depth.md](./US-03_chain_stops_at_right_depth.md) |
| US-04 | Chain loads identity, not detail | Chain delivers pointers and identity, not full stage outputs | [US-04_chain_loads_identity_not_detail.md](./US-04_chain_loads_identity_not_detail.md) |
