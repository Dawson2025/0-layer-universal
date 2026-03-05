---
resource_id: "d328cace-b04a-40d4-b2c4-f826746cfb4b"
resource_type: "handoff"
resource_name: "overview_report"
---
# Output Report: stage_2_07_testing

## Purpose
Navigation hub for stage 07 testing outputs, organized for propagation-funnel consumption.

## Canonical Reports
- `outputs/reports/stage_report.md`: Stage status, findings, and handoff readiness
- `outputs/reports/test_results_summary.md`: Aggregated automated test run results
- `outputs/reports/codex_runtime_validation_report.md`: Runtime-agent validation and required Codex execution mode

## Primary Work Products
- `outputs/run_all_tests.sh`: Master test runner
- `outputs/test_*.sh`: Structural, integration, and Codex-specific validation scripts
- `outputs/by_topic/`: Topic-specific detailed reports and test design documents

## Propagation Notes
- Canonical reports are mirrored to `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/` and `03_to_below/`
- `sync-handoffs.sh` consumes stage reports from handoff outgoing first, then falls back to `outputs/reports/stage_report.md`
- Legacy copies in `outputs/` are retained for compatibility during transition
