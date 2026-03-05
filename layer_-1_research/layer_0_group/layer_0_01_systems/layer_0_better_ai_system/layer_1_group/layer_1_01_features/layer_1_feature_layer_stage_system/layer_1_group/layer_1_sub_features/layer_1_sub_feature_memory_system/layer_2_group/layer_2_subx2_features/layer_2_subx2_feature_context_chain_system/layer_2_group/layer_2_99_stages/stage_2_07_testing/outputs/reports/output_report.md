---
resource_id: "c0e364a9-5d57-4721-8612-975bc382dd2d"
resource_type: "output"
resource_name: "output_report"
---
# Output Report: stage_2_07_testing

<!-- section_id: "66be483c-3919-4106-a4ec-bc4010f398f9" -->
## Purpose
Canonical navigation hub for stage 07 testing outputs.

Testing outputs are organized by test purpose, then by suite phase:
- `outputs/by_purpose/<purpose>/design/`
- `outputs/by_purpose/<purpose>/implementation/`
- `outputs/by_purpose/<purpose>/runs/`
- `outputs/by_purpose/<purpose>/results/`
- `outputs/by_purpose/<purpose>/insights/`

<!-- section_id: "05aa91f1-0287-4627-91e8-7f3eb6b64640" -->
## Canonical Reports
- `outputs/reports/stage_report.md`: Stage status, findings, and handoff readiness
- `outputs/reports/test_results_summary.md`: Aggregated automated test run results
- `outputs/reports/codex_runtime_validation_report.md`: Runtime-agent validation and required Codex execution mode

<!-- section_id: "c4b9fd65-5d23-4096-be6a-dd45cbfc1b9b" -->
## Purpose-Based Testing Suites
- `outputs/by_purpose/context_chain_validation/`: Traversal and chain-integrity testing artifacts
- `outputs/by_purpose/codex_runtime_validation/`: Codex runtime behavior and policy artifacts
- `outputs/by_purpose/reports_funnel_validation/`: Canonical-report + handoff-mirror propagation artifacts
- `outputs/by_purpose/avenue_web_validation/`: Avenue coverage and functional validation artifacts
- `outputs/by_purpose/cross_entity_porting_bridge_validation/`: Upstream agnostic -> downstream context-chain bridge contract validation
- `outputs/by_purpose/full_suite_validation/`: Aggregate test runner design/run/result/insight artifacts

<!-- section_id: "5c04657b-23df-47c3-a105-d854ffc87caa" -->
## Quality Gate
- `outputs/test_outputs_purpose_taxonomy.sh`: Enforces purpose/suite folder structure and artifact presence
- `outputs/test_cross_entity_porting_bridge.sh`: Enforces cross-entity bridge contract integrity
- `outputs/run_all_tests.sh`: Includes taxonomy check in full-suite run

<!-- section_id: "fb37dfdb-dcdf-492a-8169-77f426d2e029" -->
## Primary Work Products
- `outputs/run_all_tests.sh`: Master test runner
- `outputs/test_*.sh`: Structural, integration, and Codex-specific validation scripts
- `outputs/by_purpose/`: Canonical purpose-based test suite outputs
- `outputs/by_topic/`: Legacy compatibility surface (transitional)

<!-- section_id: "571646df-5f90-4f39-955f-3fbdf9d28874" -->
## Propagation Notes
- Canonical reports are mirrored to `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/` and `03_to_below/`
- `sync-handoffs.sh` consumes stage reports from handoff outgoing first, then falls back to `outputs/reports/stage_report.md`
- Legacy copies in `outputs/` are retained for compatibility during transition
