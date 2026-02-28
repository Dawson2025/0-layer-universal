# Spawning Patterns -- Requirements Index

**Need**: [Spawning Patterns](../README.md)

## Overview

These requirements define when and how managers spawn specialized agents. If work requires stage methodology, spawn a stage agent; if it's a quick decision or status check, do it directly. Spawned agents receive a task description and directory pointer (never the manager's full context), follow a defined lifecycle (spawn, read 0AGNOSTIC.md, work, write report, exit), and parallel agents are only permitted for independent, non-overlapping work.

## Key Themes

- **When to Spawn**: Clear criteria — spawn for methodology-requiring work, do directly for quick checks; work expected to exceed N steps should be delegated
- **How to Spawn**: Standard Task tool pattern with task description + directory pointer; team creation for parallel work; spawned agents get minimal starting context
- **Agent Lifecycle**: Spawn → read 0AGNOSTIC.md → do work → write stage report → exit; agents must not exit without updating handoff state
- **Parallel Agent Rules**: Only for independent stages with non-overlapping scope; dependent or shared-output work must be sequential

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | When to Spawn | Criteria for spawning vs doing work directly | [REQ-01_when_to_spawn.md](./REQ-01_when_to_spawn.md) |
| REQ-02 | How to Spawn | Task tool, team creation, context given to spawned agents | [REQ-02_how_to_spawn.md](./REQ-02_how_to_spawn.md) |
| REQ-03 | Agent Lifecycle | Spawn -> read -> work -> report -> exit protocol | [REQ-03_agent_lifecycle.md](./REQ-03_agent_lifecycle.md) |
| REQ-04 | Parallel Agents | Rules for when parallel agents are appropriate | [REQ-04_parallel_agents.md](./REQ-04_parallel_agents.md) |
