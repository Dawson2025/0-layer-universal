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

<!-- section_id: "362764be-2d9b-43c3-b45f-6deb3430b4ee" -->
## Definition

Spawning patterns define the rules for when a manager should create a new agent (vs doing work itself), how to create agents (Task tool, team creation, direct delegation), and how agent lifecycle works (creation, work, reporting, termination).

---

<!-- section_id: "ec04bebe-181a-44b5-9d37-6dd9d35e3c6f" -->
## Why This Matters

- Without spawning rules, managers either do everything themselves (no delegation) or spawn too many agents (coordination overhead)
- The mechanism for spawning matters: Task tool sub-agents have different context than team members
- Agent lifecycle must be defined: when does an agent start, how does it report, when does it end?
- Spawning without lifecycle management leads to orphaned agents and incomplete work

---

<!-- section_id: "0cc423cc-a98c-443b-9351-6dd41703db56" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

---

<!-- section_id: "a76a2e2f-d3c2-466f-9ad9-48a43b1a6180" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "fa19b3a6-e8f5-4c2b-8bc8-217049bbb63f" -->
## Acceptance Criteria

- [ ] Spawning criteria are documented (when to delegate vs do directly)
- [ ] Spawning mechanisms are documented (Task tool, team creation)
- [ ] Agent lifecycle is defined (spawn -> work -> report -> exit)
- [ ] Parallel agent rules are defined
- [ ] A manager can follow the spawning rules to decide whether and how to create a sub-agent

---

<!-- section_id: "83201a41-c411-497f-8b5a-88c6dcb30d91" -->
## Research References

- Claude Code Task tool documentation
- Claude Code SendMessage / team tools
- Context chain system's manager 0AGNOSTIC.md as working example of spawning patterns
