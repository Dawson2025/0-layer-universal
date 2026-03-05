---
resource_id: "4b10ba43-047d-4693-b3c3-8f21d937a741"
resource_type: "output"
resource_name: "report_porting_contract_test_report"
---
# Report Porting Contract Test Report

<!-- section_id: "74e700ce-e781-48a9-80b7-2c48e8022bbb" -->
## Test Design

<!-- section_id: "d0355154-105b-4545-9278-bdf8312f91aa" -->
### Goal
Verify that active stages in `agent_delegation_system` follow the canonical propagation-funnel report contract.

<!-- section_id: "a9da20da-8ea5-4f17-8844-877249b60b96" -->
### Contract checks (active stages 01, 02, 04, 06)
1. Canonical report exists: `outputs/reports/stage_report.md`
2. Handoff mirrors exist:
- `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md`
- `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md`
3. Canonical report equals both handoff mirrors
4. `outputs/reports/output_report.md` exists
5. Legacy compatibility copy exists: `outputs/stage_report.md`

<!-- section_id: "4e27f9bc-fbef-4e97-9fff-1a24840d29fb" -->
## Implementation

<!-- section_id: "f28454aa-2beb-428a-a5e5-01da80b6487f" -->
### Script
- `outputs/test_report_porting_contract.sh`

<!-- section_id: "5a24be77-04e1-44de-adf6-70af0fc3ee56" -->
### Preparation work performed
- Migrated active stages (01/02/04/06) to canonical report location
- Added missing to-below mirrors
- Added overview mirror files from output reports

<!-- section_id: "61fda93b-af46-4e72-9165-1681cacd99e9" -->
## Run

<!-- section_id: "98102f82-f358-4702-973f-728a62f76ee9" -->
### Command
```bash
cd stage_1_07_testing/outputs
./test_report_porting_contract.sh
```

<!-- section_id: "9ea4222b-3dcb-4af5-ad36-5c24c2e2de6d" -->
### Result
- PASS: 28
- FAIL: 0

<!-- section_id: "d5754182-01eb-40fb-98e7-5cbd94e5a4ad" -->
## Insights

1. Stage-level report contract was partially implemented before test enforcement; explicit checks made drift visible.
2. Canonical+mirror pattern is stable once active stages are normalized.
3. Stage testing should include structural contract checks, not only feature-specific tests.
4. This test now provides reusable validation logic for other entities.
