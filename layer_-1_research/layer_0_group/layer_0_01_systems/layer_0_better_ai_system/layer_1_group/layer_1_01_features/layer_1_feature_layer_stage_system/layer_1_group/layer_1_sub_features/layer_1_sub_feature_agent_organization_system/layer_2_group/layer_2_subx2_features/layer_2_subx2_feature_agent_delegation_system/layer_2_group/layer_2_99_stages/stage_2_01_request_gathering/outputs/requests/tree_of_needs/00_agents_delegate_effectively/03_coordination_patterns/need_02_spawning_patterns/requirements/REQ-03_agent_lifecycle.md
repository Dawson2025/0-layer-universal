---
resource_id: "de85a83d-7e6f-4ad2-b10f-7b1b901516d8"
resource_type: "output"
resource_name: "REQ-03_agent_lifecycle"
---
# Agent Lifecycle

**Need**: [Spawning Patterns](../README.md)

---

- MUST define the agent lifecycle: spawn -> read 0AGNOSTIC.md -> do work -> write stage report -> exit
- MUST require agents to write a stage report before exiting
- MUST NOT allow agents to exit without updating their handoff state
- SHOULD define maximum agent scope: one stage, one task, one session (not multi-stage sprawl)
