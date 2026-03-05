---
resource_id: "737cb997-e290-4a56-a62e-9c866587c50b"
resource_type: "readme
output"
resource_name: "README"
---
# Handoff Protocols -- User Stories Index

**Need**: [Handoff Protocols](../README.md)

<!-- section_id: "91d8e58a-9f1e-47b8-9268-a6ac0310e682" -->
## Overview

These stories cover how context is preserved across agent transitions -- session-to-session, agent-to-agent, and parent-to-child entity. They validate that stage agents leave sufficient state for the next session to continue without re-discovery, that managers delegate with enough context for the receiving agent, that child entities receive proper handoff from parent entities, and that agents recover gracefully after context compaction.

<!-- section_id: "37f67e60-f025-476b-a334-85d53433d100" -->
## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Stage agent hands off to next session | Agent writes handoff state before session ends | [US-01_stage_agent_hands_off.md](./US-01_stage_agent_hands_off.md) |
| US-02 | Manager delegates with sufficient context | Manager provides enough background for receiving agent to start | [US-02_manager_delegates_with_context.md](./US-02_manager_delegates_with_context.md) |
| US-03 | Child entity receives handoff from parent | Child agent bootstraps from parent-provided handoff document | [US-03_child_receives_handoff.md](./US-03_child_receives_handoff.md) |
| US-04 | Agent recovers after compaction | Agent rebuilds working state from persisted handoff after context loss | [US-04_agent_recovers_after_compaction.md](./US-04_agent_recovers_after_compaction.md) |
