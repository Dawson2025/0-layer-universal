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

### Stage Agent Identity
- MUST have a `0AGNOSTIC.md` in every stage directory with: identity (role, scope), methodology, output format, and success criteria
- MUST define the stage agent's scope boundary -- what it does and does NOT do
- MUST reference parent entity for domain context (e.g., "Read `../../.0agnostic/knowledge/` for domain understanding")
- SHOULD include triggers that define when this stage agent is activated

### Manager Delegation Protocol
- MUST NOT have managers carry operational knowledge for stages (methodology, templates, step-by-step procedures)
- MUST support the pattern: manager reads status -> decides what stage needs work -> spawns stage agent with task description -> stage agent reads its own 0AGNOSTIC.md
- MUST define what the manager provides to the stage agent (task description, pointers to relevant context)
- MUST define what the stage agent discovers on its own (methodology from 0AGNOSTIC.md, domain knowledge from parent)

### Boundary Rules
- MUST define what stays with the manager (status overview, cross-stage coordination, priority decisions)
- MUST define what stays with the stage agent (methodology, detailed outputs, domain-specific procedures)
- MUST NOT allow stage agents to make cross-stage decisions (that is the manager's role)
- SHOULD define escalation paths: when a stage agent encounters something outside its scope

---

## Acceptance Criteria

- [ ] Every active stage has a `0AGNOSTIC.md` with identity, methodology, output format, and success criteria
- [ ] A manager can delegate to a stage agent with only a task description and a directory pointer
- [ ] The stage agent can begin work by reading its own `0AGNOSTIC.md` without additional instructions from the manager
- [ ] Manager context does not include stage-level methodology or procedures
- [ ] Boundary between manager and stage agent responsibilities is documented and unambiguous

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- stage delegation model definition
- Context chain system research on what goes in static vs dynamic context
- Existing implementation: `context_chain_system/` stages as working example of this pattern
