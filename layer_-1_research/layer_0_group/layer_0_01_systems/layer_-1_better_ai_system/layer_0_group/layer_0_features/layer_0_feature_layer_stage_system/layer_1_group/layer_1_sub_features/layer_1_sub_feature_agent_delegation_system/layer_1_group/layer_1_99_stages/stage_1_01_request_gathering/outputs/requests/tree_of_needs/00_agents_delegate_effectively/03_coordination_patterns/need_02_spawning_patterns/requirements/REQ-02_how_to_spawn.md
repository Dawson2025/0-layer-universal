# How to Spawn

**Need**: [Spawning Patterns](../README.md)

---

- MUST define the Task tool spawning pattern: manager creates a sub-agent with task description and directory pointer
- MUST define the team creation pattern: when multiple agents need to work in parallel
- MUST define what context the spawned agent receives (task description, directory pointer, not full manager context)
- SHOULD define how to spawn agents using Claude Code's Task tool, SendMessage, or team tools
