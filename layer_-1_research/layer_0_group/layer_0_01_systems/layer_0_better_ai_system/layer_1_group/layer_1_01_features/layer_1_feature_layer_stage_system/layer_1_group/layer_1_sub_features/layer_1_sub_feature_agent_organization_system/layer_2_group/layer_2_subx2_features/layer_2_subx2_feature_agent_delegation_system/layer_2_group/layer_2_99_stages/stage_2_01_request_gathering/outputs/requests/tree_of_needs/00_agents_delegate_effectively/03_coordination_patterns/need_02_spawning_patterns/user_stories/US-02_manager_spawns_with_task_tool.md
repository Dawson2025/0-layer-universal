---
resource_id: "16fa6dcf-1615-43f2-b395-46193ddafeb4"
resource_type: "output"
resource_name: "US-02_manager_spawns_with_task_tool"
---
# US-2: Manager spawns with Task tool

**Need**: [Spawning Patterns](../README.md)

---

**As a** user who expects delegated agents to start working immediately with consistent context,
**I want** the manager to use a standard prompt template when spawning agents via the Task tool,
**So that** every spawned agent receives the same reliable starting point regardless of which stage it targets.

### What Happens

1. User tells the AI to work on a specific stage
2. Manager selects the appropriate stage and prepares a Task tool invocation
3. Manager uses a standard prompt template: task description + stage directory path
4. Task tool spawns a stage agent with the template context
5. Stage agent reads its 0AGNOSTIC.md and begins work -- no ad-hoc instructions needed

### Acceptance Criteria

- Standard prompt template exists for Task tool agent spawning
- Template includes task description and directory pointer (nothing more)
- Spawned agent can start work from the template alone without additional manager input
