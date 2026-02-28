# Need: Stage Delegation

**Branch**: [01_delegation_model](../)
**Question**: "How does a manager hand off work to a stage agent?"
**Version**: 1.0.0

---

## Definition

A manager delegates work to a stage agent by providing the task and pointing to the stage directory. The stage agent reads its own `0AGNOSTIC.md` for identity, methodology, output format, and success criteria. The manager never carries this operational knowledge.

---

## Why This Matters

- Without stage delegation, managers become monolithic agents that carry all methodology for all stages
- Context windows overflow when one agent tries to hold everything
- Managers lose focus on coordination when they also carry operational detail
- Stage agents cannot be specialized if there is no clear boundary between manager and agent responsibilities

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] Every active stage has a `0AGNOSTIC.md` with identity, methodology, output format, and success criteria
- [ ] A manager can delegate to a stage agent with only a task description and a directory pointer
- [ ] The stage agent can begin work by reading its own `0AGNOSTIC.md` without additional instructions from the manager
- [ ] Manager context does not include stage-level methodology or procedures
- [ ] Boundary between manager and stage agent responsibilities is documented and unambiguous

---

## Research References

- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- stage delegation model definition
- Context chain system research on what goes in static vs dynamic context
- Existing implementation: `context_chain_system/` stages as working example of this pattern
