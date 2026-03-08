---
resource_id: "ec65bd1a-b9ae-4dfd-bdc9-57546668d9be"
resource_type: "readme_output"
resource_name: "README"
---
# Agent Hierarchy -- User Stories Index

**Need**: [Agent Hierarchy](../README.md)

<!-- section_id: "34d13906-5c04-446f-8853-227497373f61" -->
## Overview

These stories cover how parent-child management relationships are established and maintained across the agent tree. They validate that entity managers discover their direct reports from the entity structure, that stage agents know their reporting manager, that child managers can escalate issues upward, and that the developer can visualize the full agent tree to confirm correctness.

<!-- section_id: "1bbf0eba-cf25-48f6-9fb5-b0f348734d08" -->
## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Entity manager knows its direct reports | Manager discovers its stages and child entities from 0AGNOSTIC.md | [US-01_manager_knows_direct_reports.md](./US-01_manager_knows_direct_reports.md) |
| US-02 | Stage agent knows its manager | Stage agent identifies its reporting manager from context | [US-02_stage_agent_knows_manager.md](./US-02_stage_agent_knows_manager.md) |
| US-03 | Child manager escalates to parent | Child entity manager routes an issue to the parent manager | [US-03_child_manager_escalates.md](./US-03_child_manager_escalates.md) |
| US-04 | Developer visualizes the agent tree | Developer inspects the full hierarchy of who manages whom | [US-04_developer_visualizes_tree.md](./US-04_developer_visualizes_tree.md) |
