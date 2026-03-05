---
resource_id: "4b182e41-242a-4e2a-8a3b-c023757d88ca"
resource_type: "output"
resource_name: "REQ-02_how_to_spawn"
---
# How to Spawn

**Need**: [Spawning Patterns](../README.md)

---

- MUST define the Task tool spawning pattern: manager creates a sub-agent with task description and directory pointer
- MUST define the team creation pattern: when multiple agents need to work in parallel
- MUST define what context the spawned agent receives (task description, directory pointer, not full manager context)
- SHOULD define how to spawn agents using Claude Code's Task tool, SendMessage, or team tools
