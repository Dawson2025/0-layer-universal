# Stage Delegation -- User Stories Index

**Need**: [Stage Delegation](../README.md)

## Overview

These stories cover the end-to-end workflow of a manager handing off work to a stage agent and that agent becoming operational independently. They validate that managers can delegate with minimal information, that stage agents self-configure from their own 0AGNOSTIC.md, and that clear boundaries prevent managers from doing stage-level work themselves.

## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Manager spawns a stage agent | Manager creates a stage agent with only a task and directory pointer | [US-01_manager_spawns_stage_agent.md](./US-01_manager_spawns_stage_agent.md) |
| US-02 | Stage agent reads its own identity | Newly spawned agent bootstraps from its own 0AGNOSTIC.md | [US-02_stage_agent_reads_identity.md](./US-02_stage_agent_reads_identity.md) |
| US-03 | Stage agent loads domain context from parent | Agent reads parent entity knowledge for domain understanding | [US-03_stage_agent_loads_domain_context.md](./US-03_stage_agent_loads_domain_context.md) |
| US-04 | Manager stays out of stage-level work | Developer verifies manager does not carry stage methodology | [US-04_manager_stays_out.md](./US-04_manager_stays_out.md) |
