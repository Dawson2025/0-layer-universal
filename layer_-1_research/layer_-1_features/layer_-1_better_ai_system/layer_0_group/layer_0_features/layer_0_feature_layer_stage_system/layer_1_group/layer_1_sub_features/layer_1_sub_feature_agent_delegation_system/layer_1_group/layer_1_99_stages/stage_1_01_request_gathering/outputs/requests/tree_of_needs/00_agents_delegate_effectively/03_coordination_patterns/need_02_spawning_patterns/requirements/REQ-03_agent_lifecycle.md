# Agent Lifecycle

**Need**: [Spawning Patterns](../README.md)

---

- MUST define the agent lifecycle: spawn -> read 0AGNOSTIC.md -> do work -> write stage report -> exit
- MUST require agents to write a stage report before exiting
- MUST NOT allow agents to exit without updating their handoff state
- SHOULD define maximum agent scope: one stage, one task, one session (not multi-stage sprawl)
