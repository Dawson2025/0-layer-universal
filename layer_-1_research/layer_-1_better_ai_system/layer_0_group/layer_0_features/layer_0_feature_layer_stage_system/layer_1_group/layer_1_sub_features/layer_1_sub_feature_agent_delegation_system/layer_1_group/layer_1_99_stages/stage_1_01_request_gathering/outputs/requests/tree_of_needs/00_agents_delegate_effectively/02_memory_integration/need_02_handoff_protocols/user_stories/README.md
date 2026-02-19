# Handoff Protocols -- User Stories Index

**Need**: [Handoff Protocols](../README.md)

## Actors

- **Manager**: Entity-level AI agent that coordinates stages
- **Stage Agent**: AI agent working within a specific stage
- **Next Agent**: The agent that picks up work after a transition (could be same role, new session)
- **Child Agent**: Agent managing a child entity

---

| US# | Title | Actor | File |
|-----|-------|-------|------|
| US-01 | Stage agent hands off to next session | Stage Agent | [US-01_stage_agent_hands_off.md](./US-01_stage_agent_hands_off.md) |
| US-02 | Manager delegates with sufficient context | Manager | [US-02_manager_delegates_with_context.md](./US-02_manager_delegates_with_context.md) |
| US-03 | Child entity receives handoff from parent | Child Agent | [US-03_child_receives_handoff.md](./US-03_child_receives_handoff.md) |
| US-04 | Agent recovers after compaction | Next Agent | [US-04_agent_recovers_after_compaction.md](./US-04_agent_recovers_after_compaction.md) |
