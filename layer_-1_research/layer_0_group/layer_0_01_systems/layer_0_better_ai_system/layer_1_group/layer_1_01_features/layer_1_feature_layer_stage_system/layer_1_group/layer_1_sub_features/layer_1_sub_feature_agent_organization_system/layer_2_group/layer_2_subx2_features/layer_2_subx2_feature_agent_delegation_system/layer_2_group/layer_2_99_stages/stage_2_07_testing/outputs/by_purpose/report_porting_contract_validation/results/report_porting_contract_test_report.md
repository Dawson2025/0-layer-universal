---
resource_id: "4b10ba43-047d-4693-b3c3-8f21d937a741"
resource_type: "output"
resource_name: "report_porting_contract_test_report"
---
# Report Porting Contract Test Report

## Test Design

### Goal
Verify that active stages in `agent_delegation_system` follow the canonical propagation-funnel report contract.

### Contract checks (active stages 01, 02, 04, 06)
1. Canonical report exists: `outputs/reports/stage_report.md`
2. Handoff mirrors exist:
- `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md`
- `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md`
3. Canonical report equals both handoff mirrors
4. `outputs/reports/output_report.md` exists
5. Legacy compatibility copy exists: `outputs/stage_report.md`

## Implementation

### Script
- `outputs/test_report_porting_contract.sh`

### Preparation work performed
- Migrated active stages (01/02/04/06) to canonical report location
- Added missing to-below mirrors
- Added overview mirror files from output reports

## Run

### Command
```bash
cd stage_1_07_testing/outputs
./test_report_porting_contract.sh
```

### Result
- PASS: 28
- FAIL: 0

## Insights

1. Stage-level report contract was partially implemented before test enforcement; explicit checks made drift visible.
2. Canonical+mirror pattern is stable once active stages are normalized.
3. Stage testing should include structural contract checks, not only feature-specific tests.
4. This test now provides reusable validation logic for other entities.
