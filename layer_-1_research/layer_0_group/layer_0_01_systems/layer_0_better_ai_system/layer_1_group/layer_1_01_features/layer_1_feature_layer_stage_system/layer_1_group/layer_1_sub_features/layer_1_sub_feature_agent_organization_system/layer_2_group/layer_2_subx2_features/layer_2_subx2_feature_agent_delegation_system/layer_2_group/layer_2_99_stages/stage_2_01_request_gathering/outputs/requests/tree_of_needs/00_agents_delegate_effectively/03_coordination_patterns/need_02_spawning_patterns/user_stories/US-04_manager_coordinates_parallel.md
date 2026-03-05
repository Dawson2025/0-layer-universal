---
resource_id: "af79ac04-f81a-483d-8929-d91812689060"
resource_type: "output"
resource_name: "US-04_manager_coordinates_parallel"
---
# US-4: Manager coordinates parallel work

**Need**: [Spawning Patterns](../README.md)

---

**As a** user who wants the AI to work on multiple independent tasks simultaneously,
**I want** the manager to spawn parallel agents for independent work but avoid parallelism for dependent work,
**So that** I get faster results for independent tasks without introducing conflicts.

<!-- section_id: "9e3aad7c-d901-4b24-9b4b-05e5bc4451e2" -->
### What Happens

1. User says "research topic A and topic B" (two independent tasks)
2. Manager evaluates whether the tasks are independent or dependent
3. For independent tasks: manager spawns parallel stage agents
4. For dependent tasks: manager sequences them (stage A completes before stage B starts)
5. Parallel agents work simultaneously; user gets faster results with no conflicts

<!-- section_id: "231ae212-2830-40cf-9ce6-fc62631c1c82" -->
### Acceptance Criteria

- Parallel spawning rules clearly distinguish independent vs dependent work
- Manager spawns parallel agents only for genuinely independent tasks
- Dependent tasks are sequenced, not parallelized
- User gets faster results for independent work without conflicting outputs
