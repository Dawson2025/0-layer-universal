---
resource_id: "10e3c554-bb11-43ec-85d1-dcc327397dae"
resource_type: "readme
output"
resource_name: "README"
---
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

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] Spawning criteria are documented (when to delegate vs do directly)
- [ ] Spawning mechanisms are documented (Task tool, team creation)
- [ ] Agent lifecycle is defined (spawn -> work -> report -> exit)
- [ ] Parallel agent rules are defined
- [ ] A manager can follow the spawning rules to decide whether and how to create a sub-agent

---

## Research References

- Claude Code Task tool documentation
- Claude Code SendMessage / team tools
- Context chain system's manager 0AGNOSTIC.md as working example of spawning patterns
