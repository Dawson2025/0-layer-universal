---
resource_id: "4a8b7350-7b0b-44fe-b047-5845b75ad02b"
resource_type: "knowledge"
resource_name: "report_and_porting_contract"
---
# Report And Porting Contract

<!-- section_id: "29bcdd77-c5f0-446f-b7be-b1a0c4338bdb" -->
## Purpose
Define one canonical behavior for report generation and propagation across this entity and all child entities, and define how that behavior must survive tool-specific projection (including Codex).

<!-- section_id: "5131de47-3021-465b-9707-6392e9b7fbbb" -->
## Canonical Report Contract

For every active stage:
- Canonical report path: `outputs/reports/stage_report.md`
- Canonical overview path: `outputs/reports/output_report.md`
- Mirror to handoff (to manager):
  - `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md`
  - `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/overview_report.md`
- Mirror to handoff (to below):
  - `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md`
  - `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/overview_report.md`

Entity-level consolidation:
- Layer report canonical: `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md`
- Stage rollup canonical: `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stages_report.md`

Compatibility note:
- `outputs/stage_report.md` is legacy-only compatibility, not canonical.

<!-- section_id: "a54533cf-8139-4e39-baf1-23c14df03600" -->
## Propagation Funnel Requirements

Funnel sequence (stage scope):
1. Work products in `outputs/`
2. Consolidation in `outputs/reports/output_report.md`
3. Stage status in `outputs/reports/stage_report.md`
4. Mirror to `.0agnostic/05_handoff_documents/02_outgoing/`
5. `sync-handoffs.sh` distributes to entity and siblings

Funnel sequence (entity scope):
1. Collect stage reports in `.0agnostic/05_handoff_documents/01_incoming/03_from_below/stage_reports/`
2. Consolidate into `stages_report.md` and `layer_report.md`
3. Publish to `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/`

<!-- section_id: "d5cfd17f-452c-4ae1-acc2-e1c7b8789a1a" -->
## Codex Porting Contract

Agnostic-source requirement:
- `0AGNOSTIC.md` and `.0agnostic/*` must explicitly mention canonical report paths and mirror expectations.

Projection requirement:
- Generated `AGENTS.md` must preserve report and handoff instructions without tool-specific drift.
- `.1merge/.1codex_merge` content may add Codex-specific runtime/testing constraints, but cannot contradict agnostic report/handoff contract.

Runtime validation requirement:
- Codex runtime validation for this system should run with:
  - `codex --dangerously-bypass-approvals-and-sandbox`
- Reason: sandbox limitations can produce false negatives unrelated to contract correctness.

<!-- section_id: "a4939e37-0a13-4486-a401-09b6c5cdf167" -->
## Enforcement

Minimum checks for each stage:
- `outputs/reports/` exists
- `outputs/reports/stage_report.md` exists
- Handoff mirrors in `01_to_above/` and `03_to_below/` exist
- Canonical and mirrored stage reports are byte-identical

Minimum checks for each entity:
- `.0agnostic/05_handoff_documents/` inbound/outbound structure exists
- `layer_report.md` and `stages_report.md` exist in outbound `01_to_above/`

<!-- section_id: "6c813065-ae51-4159-b06f-8a9c29df175d" -->
## Decision Rule

When agnostic contract and projected tool behavior differ:
1. Treat agnostic contract as source of truth
2. Fix projection (`agnostic-sync` and/or `.1merge`) to conform
3. Add or update tests to prevent recurrence
