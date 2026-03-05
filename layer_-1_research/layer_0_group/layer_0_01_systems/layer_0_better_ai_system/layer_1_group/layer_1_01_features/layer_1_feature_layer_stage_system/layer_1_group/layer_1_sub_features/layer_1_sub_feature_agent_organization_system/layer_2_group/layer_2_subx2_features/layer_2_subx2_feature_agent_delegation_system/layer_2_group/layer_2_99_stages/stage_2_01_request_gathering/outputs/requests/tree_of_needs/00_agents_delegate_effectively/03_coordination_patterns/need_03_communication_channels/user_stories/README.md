---
resource_id: "9a8ae068-40bb-4ba3-a184-c5c95189b334"
resource_type: "readme
output"
resource_name: "README"
---
# Communication Channels -- User Stories Index

**Need**: [Communication Channels](../README.md)

## Overview

These stories cover the mechanisms agents use to share information with each other across time and scope. They validate that stage agents communicate status asynchronously via structured reports, that concurrent agents coordinate in real time without duplicating work, that future agents can discover the full session history of what happened before them, and that agents select the appropriate channel for each type of communication.

## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Stage agent communicates status via report | Agent writes a structured report as the async status channel | [US-01_stage_agent_communicates_status.md](./US-01_stage_agent_communicates_status.md) |
| US-02 | Parallel agents coordinate in real time | Concurrent agents use team tools to avoid conflicts | [US-02_parallel_agents_coordinate.md](./US-02_parallel_agents_coordinate.md) |
| US-03 | Future agent discovers session history | New-session agent reads episodic memory to learn what happened | [US-03_future_agent_discovers_history.md](./US-03_future_agent_discovers_history.md) |
| US-04 | Agent knows which channel to use | Agent selects the correct channel based on message type and audience | [US-04_agent_knows_which_channel.md](./US-04_agent_knows_which_channel.md) |
