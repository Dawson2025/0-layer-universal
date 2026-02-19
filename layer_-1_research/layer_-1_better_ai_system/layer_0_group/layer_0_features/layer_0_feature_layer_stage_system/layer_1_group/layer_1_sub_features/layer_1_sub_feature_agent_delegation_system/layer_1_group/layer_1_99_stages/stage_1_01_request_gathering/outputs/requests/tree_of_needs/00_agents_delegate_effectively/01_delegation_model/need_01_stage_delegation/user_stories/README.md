# Stage Delegation -- User Stories Index

**Need**: [Stage Delegation](../README.md)

## Actors

- **Manager**: Entity-level AI agent that coordinates stages and makes cross-stage decisions
- **Stage Agent**: AI agent spawned to work on a specific stage (e.g., request gathering, research, design)
- **Developer**: Human maintaining the system (Dawson)

---

| US# | Title | Actor | File |
|-----|-------|-------|------|
| US-01 | Manager spawns a stage agent | Manager | [US-01_manager_spawns_stage_agent.md](./US-01_manager_spawns_stage_agent.md) |
| US-02 | Stage agent reads its own identity | Stage Agent | [US-02_stage_agent_reads_identity.md](./US-02_stage_agent_reads_identity.md) |
| US-03 | Stage agent loads domain context from parent | Stage Agent | [US-03_stage_agent_loads_domain_context.md](./US-03_stage_agent_loads_domain_context.md) |
| US-04 | Manager stays out of stage-level work | Developer | [US-04_manager_stays_out.md](./US-04_manager_stays_out.md) |
