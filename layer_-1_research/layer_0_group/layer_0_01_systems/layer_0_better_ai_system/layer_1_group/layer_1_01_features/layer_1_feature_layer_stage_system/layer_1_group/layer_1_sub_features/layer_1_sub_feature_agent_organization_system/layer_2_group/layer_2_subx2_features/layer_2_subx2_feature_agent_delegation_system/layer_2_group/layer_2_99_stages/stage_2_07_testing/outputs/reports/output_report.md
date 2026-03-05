---
resource_id: "616bc437-7a23-429d-80fd-0c939e241a6c"
resource_type: "output"
resource_name: "output_report"
---
# Output Report: stage_1_07_testing

<!-- section_id: "c3f12b8d-2d9d-4720-b636-679c3988de00" -->
## Purpose
Canonical navigation hub for testing outputs.

Testing outputs are organized by test purpose, then suite phase:
- `outputs/by_purpose/<purpose>/design/`
- `outputs/by_purpose/<purpose>/implementation/`
- `outputs/by_purpose/<purpose>/runs/`
- `outputs/by_purpose/<purpose>/results/`
- `outputs/by_purpose/<purpose>/insights/`

<!-- section_id: "d23e7628-9422-4b89-ab54-6960ed0dd959" -->
## Purpose-Based Testing Suites
- `outputs/by_purpose/report_porting_contract_validation/`: Canonical report + handoff mirror contract validation
- `outputs/by_purpose/rule_compliance_validation/`: File change reporting rule discovery/compliance validation
- `outputs/by_purpose/stages_manager_pattern_validation/`: Stages-manager behavior pattern validation
- `outputs/by_purpose/full_suite_validation/`: Aggregate suite-level validation references

<!-- section_id: "3207e128-cd58-4648-9cf3-7c18089a98a7" -->
## Quality Gate
- `outputs/test_outputs_purpose_taxonomy.sh`: Enforces purpose/suite folder structure and artifact presence
- `outputs/test_report_porting_contract.sh`: Enforces active-stage report propagation contract

<!-- section_id: "3ea7b5d4-4dec-455d-b44d-19666ce1f84d" -->
## Runtime Policy
- For Codex runtime behavior validation campaigns, use max-permission mode:
  - `codex exec --dangerously-bypass-approvals-and-sandbox`
