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

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] Stage report protocol is documented with template
- [ ] Every active stage has a `stage_report.md` in `outputs/`
- [ ] Manager can read a stage report and make a delegation decision without loading other stage files
- [ ] Reports are under 30 lines and follow a consistent format
- [ ] Reports include status, summary, outputs, blockers, and next steps

---

## Research References

- Existing protocol: `context_chain_system/.0agnostic/protocols/stage_report_protocol.md` -- working implementation
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- stage reports definition
