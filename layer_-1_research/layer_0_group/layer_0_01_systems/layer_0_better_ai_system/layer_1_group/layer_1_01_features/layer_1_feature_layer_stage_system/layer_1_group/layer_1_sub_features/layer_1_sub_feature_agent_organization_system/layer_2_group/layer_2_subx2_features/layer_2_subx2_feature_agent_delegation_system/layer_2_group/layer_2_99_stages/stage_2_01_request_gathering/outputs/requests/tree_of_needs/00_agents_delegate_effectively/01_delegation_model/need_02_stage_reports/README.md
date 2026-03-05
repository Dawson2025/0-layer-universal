---
resource_id: "9f5642a0-876d-43b0-92e7-6622e687b9a7"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Stage Reports

**Branch**: [01_delegation_model](../)
**Question**: "How does a manager know what happened in a stage without loading all stage details?"
**Version**: 1.0.0

---

<!-- section_id: "595b1094-8072-4d27-9811-527dca4f63ca" -->
## Definition

Stage agents write a `stage_report.md` in `outputs/` before exiting. Managers read these reports to understand status, outcomes, and handoff readiness without needing to load detailed stage outputs.

---

<!-- section_id: "04a536cd-4400-421f-a7d5-14aadc7da291" -->
## Why This Matters

- Without stage reports, managers must re-read all stage outputs to understand what happened
- This defeats the purpose of delegation -- the manager ends up loading everything anyway
- Stage reports are the async communication channel between stage agents and managers
- They enable the manager to make informed decisions about what stage to work on next

---

<!-- section_id: "f030e7d7-f973-49d0-b98f-86eb4cd19b41" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

---

<!-- section_id: "a4add219-eeee-48d2-b7b3-da767b3f6a86" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "a5739a11-9fef-42c6-a177-6c30a3a02c24" -->
## Acceptance Criteria

- [ ] Stage report protocol is documented with template
- [ ] Every active stage has a `stage_report.md` in `outputs/`
- [ ] Manager can read a stage report and make a delegation decision without loading other stage files
- [ ] Reports are under 30 lines and follow a consistent format
- [ ] Reports include status, summary, outputs, blockers, and next steps

---

<!-- section_id: "967ce9f5-d31b-4a6b-927f-45b3ad3df94b" -->
## Research References

- Existing protocol: `context_chain_system/.0agnostic/protocols/stage_report_protocol.md` -- working implementation
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- stage reports definition
