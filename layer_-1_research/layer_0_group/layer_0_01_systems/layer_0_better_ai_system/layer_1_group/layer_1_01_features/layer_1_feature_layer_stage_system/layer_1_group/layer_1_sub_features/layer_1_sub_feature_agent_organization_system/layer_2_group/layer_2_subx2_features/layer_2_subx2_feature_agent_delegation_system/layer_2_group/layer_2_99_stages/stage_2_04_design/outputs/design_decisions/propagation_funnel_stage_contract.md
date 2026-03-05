---
resource_id: "663e3e51-0c90-4d1e-9782-99341df4d4d8"
resource_type: "output"
resource_name: "propagation_funnel_stage_contract"
---
# Design Decision: Propagation Funnel Stage Contract

**Date**: 2026-02-25
**Status**: Approved
**Scope**: agent_delegation_system stages and child entities

<!-- section_id: "a0f58240-7b1d-4e16-be2a-0c41dacf310a" -->
## Purpose
Define required stage/entity structure for propagation funnel behavior so reports are discoverable, syncable, and stable across tool projections.

<!-- section_id: "5f9b833d-a625-48f8-b308-9d99732a2db4" -->
## Contract

<!-- section_id: "ab34ba02-85d6-4fb2-aa2b-92af6b6766ab" -->
### Stage-level required structure

Each active stage must have:
- `outputs/reports/stage_report.md` (canonical status)
- `outputs/reports/output_report.md` (work-product index)
- `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` (manager-facing mirror)
- `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md` (downward mirror)
- `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/overview_report.md` (manager-facing overview)
- `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/overview_report.md` (downward overview)

Compatibility:
- `outputs/stage_report.md` is legacy compatibility only.

<!-- section_id: "2c133bd1-916c-440b-953e-626502713955" -->
### Entity-level required structure

Each entity must have:
- `.0agnostic/05_handoff_documents/01_incoming/03_from_below/stage_reports/` (collected stage signals)
- `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md` (entity roll-up)
- `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stages_report.md` (stage roll-up)

<!-- section_id: "c09104fd-1d89-4405-b043-cf965646c3ff" -->
## Funnel sequence

<!-- section_id: "eeaad196-032d-470b-86d5-a8b00fbb4005" -->
### Stage funnel
1. Produce work in `outputs/`
2. Consolidate into `outputs/reports/output_report.md`
3. Summarize status in `outputs/reports/stage_report.md`
4. Mirror into `.0agnostic/05_handoff_documents/02_outgoing/`
5. Run sync (`sync-handoffs.sh`) for parent/sibling distribution

<!-- section_id: "f00fc692-aac8-45ae-aed1-5497bc904a3a" -->
### Entity funnel
1. Ingest stage reports into incoming `stage_reports/`
2. Consolidate into `stages_report.md`
3. Merge child-layer signals
4. Publish `layer_report.md` upward

<!-- section_id: "f51e65c7-f57a-4751-8717-fa8f48eee73f" -->
## Relationship to canonical propagation architecture

Detailed architecture and hierarchy-wide propagation rationale are owned by context_chain_system:
- `.../stage_3_04_design/outputs/by_topic/04_context_propagation_funnel.md`

This document defines the **local implementation contract** for agent_delegation_system.

<!-- section_id: "7717c42c-8018-4ce3-9352-274ba9a9f2c3" -->
## Enforcement

Required checks:
- Canonical stage report exists for active stages
- Canonical report equals both handoff mirrors
- Output report exists for active stages
- Entity layer/stage roll-up reports exist

Implemented test:
- `stage_1_07_testing/outputs/test_report_porting_contract.sh`
