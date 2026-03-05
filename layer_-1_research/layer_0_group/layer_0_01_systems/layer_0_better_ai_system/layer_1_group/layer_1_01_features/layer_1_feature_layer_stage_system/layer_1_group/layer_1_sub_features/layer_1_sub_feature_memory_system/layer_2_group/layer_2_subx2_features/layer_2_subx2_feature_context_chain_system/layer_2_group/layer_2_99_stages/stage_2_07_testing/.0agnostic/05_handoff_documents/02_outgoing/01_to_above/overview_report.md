---
resource_id: "d328cace-b04a-40d4-b2c4-f826746cfb4b"
resource_type: "handoff"
resource_name: "overview_report"
---
# Output Report: stage_2_07_testing

<!-- section_id: "1aabd381-c055-447c-910a-2d4d9ca651b8" -->
## Purpose
Navigation hub for stage 07 testing outputs, organized for propagation-funnel consumption.

<!-- section_id: "6f00d256-954c-4304-b033-4c5c952fa603" -->
## Canonical Reports
- `outputs/reports/stage_report.md`: Stage status, findings, and handoff readiness
- `outputs/reports/test_results_summary.md`: Aggregated automated test run results
- `outputs/reports/codex_runtime_validation_report.md`: Runtime-agent validation and required Codex execution mode

<!-- section_id: "c06bdcfe-1023-4436-aed4-a69d90f8eb5b" -->
## Primary Work Products
- `outputs/run_all_tests.sh`: Master test runner
- `outputs/test_*.sh`: Structural, integration, and Codex-specific validation scripts
- `outputs/by_topic/`: Topic-specific detailed reports and test design documents

<!-- section_id: "7f8acda8-c3a3-444c-ac58-1d62963d3018" -->
## Propagation Notes
- Canonical reports are mirrored to `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/` and `03_to_below/`
- `sync-handoffs.sh` consumes stage reports from handoff outgoing first, then falls back to `outputs/reports/stage_report.md`
- Legacy copies in `outputs/` are retained for compatibility during transition
