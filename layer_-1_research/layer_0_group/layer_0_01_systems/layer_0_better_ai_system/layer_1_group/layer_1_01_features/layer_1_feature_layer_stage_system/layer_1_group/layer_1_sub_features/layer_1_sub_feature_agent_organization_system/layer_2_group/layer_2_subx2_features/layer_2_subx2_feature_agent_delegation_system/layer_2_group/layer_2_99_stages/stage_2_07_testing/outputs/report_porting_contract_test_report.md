---
resource_id: "669e8a2c-0424-42ea-ab4c-ba8e0206e896"
resource_type: "output"
resource_name: "report_porting_contract_test_report"
---
# Report Porting Contract Test Report

<!-- section_id: "3be835f0-627f-43ae-9eb3-fd52d5db0efa" -->
## Test Design

<!-- section_id: "decf5688-d0d5-48e7-b0f5-c5afec37e133" -->
### Goal
Verify that active stages in `agent_delegation_system` follow the canonical propagation-funnel report contract.

<!-- section_id: "527c9452-615a-40b4-b6e6-aaf75616d5a5" -->
### Contract checks (active stages 01, 02, 04, 06)
1. Canonical report exists: `outputs/reports/stage_report.md`
2. Handoff mirrors exist:
- `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md`
- `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md`
3. Canonical report equals both handoff mirrors
4. `outputs/reports/output_report.md` exists
5. Legacy compatibility copy exists: `outputs/stage_report.md`

<!-- section_id: "57b491e1-5e5e-4738-b62f-160907b23f83" -->
## Implementation

<!-- section_id: "ac90b294-6ae7-45c4-8802-186cc7a5ba9a" -->
### Script
- `outputs/test_report_porting_contract.sh`

<!-- section_id: "6f94ca3c-525a-4302-a241-b4e48f612b41" -->
### Preparation work performed
- Migrated active stages (01/02/04/06) to canonical report location
- Added missing to-below mirrors
- Added overview mirror files from output reports

<!-- section_id: "51a87616-f722-410b-887a-c013ecb93aa6" -->
## Run

<!-- section_id: "a06450d9-25c1-47c9-a435-3e6e5c72b94c" -->
### Command
```bash
cd stage_1_07_testing/outputs
./test_report_porting_contract.sh
```

<!-- section_id: "8411f096-c639-485e-b1ba-ffb345c4c845" -->
### Result
- PASS: 28
- FAIL: 0

<!-- section_id: "6a596bf3-ee59-4b16-acf8-6e2186a90604" -->
## Insights

1. Stage-level report contract was partially implemented before test enforcement; explicit checks made drift visible.
2. Canonical+mirror pattern is stable once active stages are normalized.
3. Stage testing should include structural contract checks, not only feature-specific tests.
4. This test now provides reusable validation logic for other entities.
