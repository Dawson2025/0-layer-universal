---
resource_id: "5e1693d6-7601-4c48-8510-4130cb15ae54"
resource_type: "readme_output"
resource_name: "README"
---
# Need: Stage Delegation

**Branch**: [01_delegation_model](../)
**Question**: "How does a manager hand off work to a stage agent?"
**Version**: 1.0.0

---

<!-- section_id: "13547a6f-ec65-4d55-9ce1-bb22369f9e41" -->
## Definition

A manager delegates work to a stage agent by providing the task and pointing to the stage directory. The stage agent reads its own `0AGNOSTIC.md` for identity, methodology, output format, and success criteria. The manager never carries this operational knowledge.

---

<!-- section_id: "855f2003-4d78-4edb-8a4f-4f3662be08a8" -->
## Why This Matters

- Without stage delegation, managers become monolithic agents that carry all methodology for all stages
- Context windows overflow when one agent tries to hold everything
- Managers lose focus on coordination when they also carry operational detail
- Stage agents cannot be specialized if there is no clear boundary between manager and agent responsibilities

---

<!-- section_id: "d94c4296-c436-4457-8a64-f27eeb375217" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

---

<!-- section_id: "dbdebee1-cfc4-4642-ab60-401ab563ef0b" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "326219a5-7424-4485-a81c-b6cc695e4053" -->
## Acceptance Criteria

- [ ] Every active stage has a `0AGNOSTIC.md` with identity, methodology, output format, and success criteria
- [ ] A manager can delegate to a stage agent with only a task description and a directory pointer
- [ ] The stage agent can begin work by reading its own `0AGNOSTIC.md` without additional instructions from the manager
- [ ] Manager context does not include stage-level methodology or procedures
- [ ] Boundary between manager and stage agent responsibilities is documented and unambiguous

---

<!-- section_id: "7c7bbc7f-37cc-4afb-b66d-74266693663a" -->
## Research References

- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- stage delegation model definition
- Context chain system research on what goes in static vs dynamic context
- Existing implementation: `context_chain_system/` stages as working example of this pattern
