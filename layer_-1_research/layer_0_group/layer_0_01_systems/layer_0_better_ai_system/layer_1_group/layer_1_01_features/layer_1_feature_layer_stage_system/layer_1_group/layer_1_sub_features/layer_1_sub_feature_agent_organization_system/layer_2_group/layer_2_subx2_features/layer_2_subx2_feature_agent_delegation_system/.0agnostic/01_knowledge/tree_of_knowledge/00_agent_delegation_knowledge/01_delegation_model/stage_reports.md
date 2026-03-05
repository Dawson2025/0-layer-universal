---
resource_id: "b1d74277-0cda-40ba-98f1-972b93970161"
resource_type: "knowledge"
resource_name: "stage_reports"
---
# Topic: Stage Reports

<!-- section_id: "40afc09e-cd59-4da1-802c-2fcd18346144" -->
## Summary

Stage reports are the async communication channel between stage agents and entity managers. Before exiting a stage, the agent writes `outputs/stage_report.md` summarizing what was done, what's left, and what the next stage needs to know. The manager reads these to understand stage status without loading stage outputs.

This design decision means managers never need to explore stage output directories — the report provides sufficient context for coordination decisions.

<!-- section_id: "c6423e68-30f2-4829-882b-4a032abf7ff3" -->
## Key Points

- Stage reports follow the universal stage report protocol
- Reports are the handoff mechanism between stages
- Managers read reports at the pointer tier — no need to load full stage outputs
- Reports are complementary to the 0AGNOSTIC.md Current State section

<!-- section_id: "1ddc5cba-0840-4fc7-9e2d-024d58552249" -->
## References

| What | Where |
|------|-------|
| Design decision: stage reports | Stage 04: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/0AGNOSTIC.md` → Key Design Decisions table |
| Universal stage report protocol | `.0agnostic/03_protocols/stage_report_protocol.md` |
| Stage report rule | `.0agnostic/02_rules/static/STAGE_REPORT_RULE.md` |
| Principle 4 (Stage Reports) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Stage 01 requirements (need_02) | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/00_agents_delegate_effectively/01_delegation_model/need_02_stage_reports/` |
