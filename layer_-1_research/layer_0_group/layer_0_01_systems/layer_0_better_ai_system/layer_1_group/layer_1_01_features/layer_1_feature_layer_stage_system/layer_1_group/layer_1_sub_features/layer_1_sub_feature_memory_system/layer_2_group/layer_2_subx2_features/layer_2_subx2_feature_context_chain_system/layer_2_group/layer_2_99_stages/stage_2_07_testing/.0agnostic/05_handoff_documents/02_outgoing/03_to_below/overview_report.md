---
resource_id: "6dfb7208-010d-4695-a3ad-dec1c495d20a"
resource_type: "handoff"
resource_name: "overview_report"
---
# Output Report: stage_2_07_testing

<!-- section_id: "448314ee-f4f9-4fe3-b248-da4edc0c6918" -->
## Purpose
Navigation hub for stage 07 testing outputs, organized for propagation-funnel consumption.

<!-- section_id: "ab708c3f-93a7-4d94-adab-3ff3ddd13bd3" -->
## Canonical Reports
- `outputs/reports/stage_report.md`: Stage status, findings, and handoff readiness
- `outputs/reports/test_results_summary.md`: Aggregated automated test run results
- `outputs/reports/codex_runtime_validation_report.md`: Runtime-agent validation and required Codex execution mode

<!-- section_id: "adcfe489-1bea-4ca8-8890-2fd3c25944f8" -->
## Primary Work Products
- `outputs/run_all_tests.sh`: Master test runner
- `outputs/test_*.sh`: Structural, integration, and Codex-specific validation scripts
- `outputs/by_topic/`: Topic-specific detailed reports and test design documents

<!-- section_id: "b00b6084-c86f-461d-9a8e-f3f9ae44c00c" -->
## Propagation Notes
- Canonical reports are mirrored to `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/` and `03_to_below/`
- `sync-handoffs.sh` consumes stage reports from handoff outgoing first, then falls back to `outputs/reports/stage_report.md`
- Legacy copies in `outputs/` are retained for compatibility during transition
