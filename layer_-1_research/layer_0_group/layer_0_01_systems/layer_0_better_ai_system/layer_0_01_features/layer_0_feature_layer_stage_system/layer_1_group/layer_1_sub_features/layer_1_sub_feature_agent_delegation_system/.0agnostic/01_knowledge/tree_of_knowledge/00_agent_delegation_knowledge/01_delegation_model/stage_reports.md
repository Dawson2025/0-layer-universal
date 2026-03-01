# Topic: Stage Reports

## Summary

Stage reports are the async communication channel between stage agents and entity managers. Before exiting a stage, the agent writes `outputs/stage_report.md` summarizing what was done, what's left, and what the next stage needs to know. The manager reads these to understand stage status without loading stage outputs.

This design decision means managers never need to explore stage output directories — the report provides sufficient context for coordination decisions.

## Key Points

- Stage reports follow the universal stage report protocol
- Reports are the handoff mechanism between stages
- Managers read reports at the pointer tier — no need to load full stage outputs
- Reports are complementary to the 0AGNOSTIC.md Current State section

## References

| What | Where |
|------|-------|
| Design decision: stage reports | Stage 04: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_04_design/0AGNOSTIC.md` → Key Design Decisions table |
| Universal stage report protocol | `.0agnostic/03_protocols/stage_report_protocol.md` |
| Stage report rule | `.0agnostic/02_rules/static/STAGE_REPORT_RULE.md` |
| Principle 4 (Stage Reports) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Stage 01 requirements (need_02) | `../../../../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/00_agents_delegate_effectively/01_delegation_model/need_02_stage_reports/` |
