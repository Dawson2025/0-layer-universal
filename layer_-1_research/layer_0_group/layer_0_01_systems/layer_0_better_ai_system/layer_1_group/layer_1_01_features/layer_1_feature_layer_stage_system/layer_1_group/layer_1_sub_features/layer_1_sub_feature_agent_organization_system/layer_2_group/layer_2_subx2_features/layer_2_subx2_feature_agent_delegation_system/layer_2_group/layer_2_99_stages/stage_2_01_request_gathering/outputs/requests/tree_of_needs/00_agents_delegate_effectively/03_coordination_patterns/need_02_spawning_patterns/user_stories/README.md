---
resource_id: "988cce45-72f2-4952-b22d-e57e4516222f"
resource_type: "readme
output"
resource_name: "README"
---
# Spawning Patterns -- User Stories Index

**Need**: [Spawning Patterns](../README.md)

<!-- section_id: "d73ee577-8970-4c43-b89f-f4655bef4bf4" -->
## Overview

These stories cover when and how managers create specialized agents, and how those agents follow a defined lifecycle. They validate that managers apply spawning criteria to decide between delegating and doing work directly, that spawning uses the correct mechanism (Task tool, team creation), that spawned agents follow the full lifecycle from creation through reporting to termination, and that parallel agents are coordinated without conflicts.

<!-- section_id: "0d3a0ecb-9ffa-4073-97fd-564140bcac5d" -->
## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Manager decides to delegate | Manager evaluates spawning criteria to decide delegate vs. do directly | [US-01_manager_decides_to_delegate.md](./US-01_manager_decides_to_delegate.md) |
| US-02 | Manager spawns with Task tool | Manager creates a sub-agent using the Task tool mechanism | [US-02_manager_spawns_with_task_tool.md](./US-02_manager_spawns_with_task_tool.md) |
| US-03 | Stage agent follows lifecycle | Agent completes the full spawn-work-report-exit cycle | [US-03_stage_agent_follows_lifecycle.md](./US-03_stage_agent_follows_lifecycle.md) |
| US-04 | Manager coordinates parallel work | Manager runs multiple stage agents concurrently without conflicts | [US-04_manager_coordinates_parallel.md](./US-04_manager_coordinates_parallel.md) |
