# Output Report: stage_3_07_testing

## Purpose
Canonical navigation hub for stage 07 testing outputs.

Testing outputs are organized by test purpose, then by suite phase:
- `outputs/by_purpose/<purpose>/design/`
- `outputs/by_purpose/<purpose>/implementation/`
- `outputs/by_purpose/<purpose>/runs/`
- `outputs/by_purpose/<purpose>/results/`
- `outputs/by_purpose/<purpose>/insights/`

## Canonical Reports
- `outputs/reports/stage_report.md`: Stage status, findings, and handoff readiness
- `outputs/reports/test_results_summary.md`: Aggregated automated test run results
- `outputs/reports/codex_runtime_validation_report.md`: Runtime-agent validation and required Codex execution mode

## Purpose-Based Testing Suites
- `outputs/by_purpose/context_chain_validation/`: Traversal and chain-integrity testing artifacts
- `outputs/by_purpose/codex_runtime_validation/`: Codex runtime behavior and policy artifacts
- `outputs/by_purpose/reports_funnel_validation/`: Canonical-report + handoff-mirror propagation artifacts
- `outputs/by_purpose/avenue_web_validation/`: Avenue coverage and functional validation artifacts
- `outputs/by_purpose/full_suite_validation/`: Aggregate test runner design/run/result/insight artifacts

## Quality Gate
- `outputs/test_outputs_purpose_taxonomy.sh`: Enforces purpose/suite folder structure and artifact presence
- `outputs/run_all_tests.sh`: Includes taxonomy check in full-suite run

## Primary Work Products
- `outputs/run_all_tests.sh`: Master test runner
- `outputs/test_*.sh`: Structural, integration, and Codex-specific validation scripts
- `outputs/by_purpose/`: Canonical purpose-based test suite outputs
- `outputs/by_topic/`: Legacy compatibility surface (transitional)

## Propagation Notes
- Canonical reports are mirrored to `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/` and `03_to_below/`
- `sync-handoffs.sh` consumes stage reports from handoff outgoing first, then falls back to `outputs/reports/stage_report.md`
- Legacy copies in `outputs/` are retained for compatibility during transition
