# Need: Stage Reports

**Branch**: [01_delegation_model](../)
**Question**: "How does a manager know what happened in a stage without loading all stage details?"
**Version**: 1.0.0

---

## Definition

Stage agents write a `stage_report.md` in `outputs/` before exiting. Managers read these reports to understand status, outcomes, and handoff readiness without needing to load detailed stage outputs.

---

## Why This Matters

- Without stage reports, managers must re-read all stage outputs to understand what happened
- This defeats the purpose of delegation -- the manager ends up loading everything anyway
- Stage reports are the async communication channel between stage agents and managers
- They enable the manager to make informed decisions about what stage to work on next

---

## Requirements

### Report Protocol
- MUST define a `stage_report.md` protocol: where it lives, when it is written, what it contains
- MUST require the stage agent to write or update the report before exiting a session
- MUST place the report at `stage_X_XX_name/outputs/stage_report.md` (consistent location)
- MUST NOT require the manager to read any other stage file to understand current status

### Report Content
- MUST include: stage status (not_started | in_progress | blocked | complete), summary of work done, key outputs produced, and handoff readiness
- MUST include: open questions or blockers that the manager needs to address
- MUST include: what the next agent working on this stage should do first
- SHOULD include: a brief list of files created or modified
- MUST NOT include: full methodology or detailed findings (those live in stage outputs)

### Report Consumption
- MUST be readable by the manager in under 30 lines (concise, not exhaustive)
- MUST enable the manager to decide "should I delegate more work to this stage?" without loading stage details
- SHOULD follow a consistent template across all stages and all entities

---

## Acceptance Criteria

- [ ] Stage report protocol is documented with template
- [ ] Every active stage has a `stage_report.md` in `outputs/`
- [ ] Manager can read a stage report and make a delegation decision without loading other stage files
- [ ] Reports are under 30 lines and follow a consistent format
- [ ] Reports include status, summary, outputs, blockers, and next steps

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Existing protocol: `context_chain_system/.0agnostic/protocols/stage_report_protocol.md` -- working implementation
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- stage reports definition
