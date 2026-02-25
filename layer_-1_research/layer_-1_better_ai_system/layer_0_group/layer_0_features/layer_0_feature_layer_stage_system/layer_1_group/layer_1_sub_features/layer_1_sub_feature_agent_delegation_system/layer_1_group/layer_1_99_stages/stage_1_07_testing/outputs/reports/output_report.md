# Output Report: stage_1_07_testing

## Purpose
Canonical navigation hub for testing outputs.

Testing outputs are organized by test purpose, then suite phase:
- `outputs/by_purpose/<purpose>/design/`
- `outputs/by_purpose/<purpose>/implementation/`
- `outputs/by_purpose/<purpose>/runs/`
- `outputs/by_purpose/<purpose>/results/`
- `outputs/by_purpose/<purpose>/insights/`

## Purpose-Based Testing Suites
- `outputs/by_purpose/report_porting_contract_validation/`: Canonical report + handoff mirror contract validation
- `outputs/by_purpose/rule_compliance_validation/`: File change reporting rule discovery/compliance validation
- `outputs/by_purpose/stages_manager_pattern_validation/`: Stages-manager behavior pattern validation
- `outputs/by_purpose/full_suite_validation/`: Aggregate suite-level validation references

## Quality Gate
- `outputs/test_outputs_purpose_taxonomy.sh`: Enforces purpose/suite folder structure and artifact presence
- `outputs/test_report_porting_contract.sh`: Enforces active-stage report propagation contract

## Runtime Policy
- For Codex runtime behavior validation campaigns, use max-permission mode:
  - `codex exec --dangerously-bypass-approvals-and-sandbox`
