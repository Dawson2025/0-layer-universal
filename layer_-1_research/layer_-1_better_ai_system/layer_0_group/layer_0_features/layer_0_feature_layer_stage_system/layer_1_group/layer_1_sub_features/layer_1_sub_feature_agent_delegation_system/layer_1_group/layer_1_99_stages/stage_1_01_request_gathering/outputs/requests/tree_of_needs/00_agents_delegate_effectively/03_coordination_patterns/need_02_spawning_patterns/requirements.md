# Need: Spawning Patterns

**Branch**: [03_coordination_patterns](../)
**Question**: "When and how should specialized agents be created?"
**Version**: 1.0.0

---

## Definition

Spawning patterns define the rules for when a manager should create a new agent (vs doing work itself), how to create agents (Task tool, team creation, direct delegation), and how agent lifecycle works (creation, work, reporting, termination).

---

## Why This Matters

- Without spawning rules, managers either do everything themselves (no delegation) or spawn too many agents (coordination overhead)
- The mechanism for spawning matters: Task tool sub-agents have different context than team members
- Agent lifecycle must be defined: when does an agent start, how does it report, when does it end?
- Spawning without lifecycle management leads to orphaned agents and incomplete work

---

## Requirements

### When to Spawn
- MUST define criteria for when a manager should spawn a stage agent vs do work directly
- MUST define the rule: if the work requires stage methodology, spawn a stage agent
- MUST define the rule: if the work is a quick status check or decision, the manager can do it directly
- SHOULD define thresholds: work expected to take more than N steps should be delegated
- MUST NOT allow managers to spawn agents for cross-stage coordination (that is the manager's job)

### How to Spawn
- MUST define the Task tool spawning pattern: manager creates a sub-agent with task description and directory pointer
- MUST define the team creation pattern: when multiple agents need to work in parallel
- MUST define what context the spawned agent receives (task description, directory pointer, not full manager context)
- SHOULD define how to spawn agents using Claude Code's Task tool, SendMessage, or team tools

### Agent Lifecycle
- MUST define the agent lifecycle: spawn -> read 0AGNOSTIC.md -> do work -> write stage report -> exit
- MUST require agents to write a stage report before exiting
- MUST NOT allow agents to exit without updating their handoff state
- SHOULD define maximum agent scope: one stage, one task, one session (not multi-stage sprawl)

### Parallel Agents
- MUST define rules for when parallel agents are appropriate (independent stages, non-overlapping scope)
- MUST define rules for when parallel agents are NOT appropriate (dependent stages, shared outputs)
- SHOULD define coordination mechanisms for parallel agents (shared status file, team tools)

---

## Acceptance Criteria

- [ ] Spawning criteria are documented (when to delegate vs do directly)
- [ ] Spawning mechanisms are documented (Task tool, team creation)
- [ ] Agent lifecycle is defined (spawn -> work -> report -> exit)
- [ ] Parallel agent rules are defined
- [ ] A manager can follow the spawning rules to decide whether and how to create a sub-agent

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Claude Code Task tool documentation
- Claude Code SendMessage / team tools
- Context chain system's manager 0AGNOSTIC.md as working example of spawning patterns
