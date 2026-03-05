---
resource_id: "be52261a-719f-4e34-8742-73c6f9c4f593"
resource_type: "readme
output"
resource_name: "README"
---
# Stage 3.04 Design — By Topic Index

Design documents for the context chain system. These are the **canonical source of truth** for context propagation, discovery, and chaining architecture.

<!-- section_id: "5afafdf8-9a01-4695-8d54-ac4809e02e53" -->
## Documents

| # | Document | Scope |
|---|----------|-------|
| 01 | `01_context_chain_system_design.md` | Avenue web technical design — 4 architecture layers, 8 MVP avenues |
| 02 | `02_0agnostic_1merge_avenue_web_integration_design.md` | How .0agnostic, .1merge, and avenue web integrate |
| 03 | `03_propagation_chain_architecture.md` | Top-down 4-layer chain: Knowledge → Agnostic Source → Tool Files → Agent Action |
| 04 | `04_context_propagation_funnel.md` | Bottom-up consolidation: outputs → reports → .0agnostic → 0AGNOSTIC.md |
| 05 | `05_hierarchy_inheritance_model.md` | What propagates across hierarchy levels, enforcement gaps |
| 06 | `06_source_of_truth_to_avenue_flow.md` | .0agnostic numbering, three zones, avenue ordering |
| 07 | `07_unified_sync_architecture.md` | Sync scripts, sync-main.sh orchestrator, execution order |
| 08 | `08_discovery_temperature_model.md` | Hot/Warm/Cold discovery, promotion system, defense in depth |

<!-- section_id: "631dac43-8bbb-4797-ab60-8cd125db78e3" -->
## Reading Order

For a complete picture, read in this order:

1. **03** (top-down chain) — how context reaches agents
2. **04** (bottom-up funnel) — how work products consolidate upward
3. **05** (inheritance) — what propagates across levels and what doesn't
4. **06** (source-to-avenue) — how .0agnostic numbering encodes information flow
5. **01** (avenue web) — the 8-avenue delivery system design
6. **02** (integration) — how .0agnostic, .1merge, and avenues connect
7. **07** (sync) — how sync scripts orchestrate propagation
8. **08** (discovery) — how agents discover context at Hot/Warm/Cold temperatures

<!-- section_id: "3c18f804-193f-4838-bccf-2fb422446feb" -->
## Ancestry

These documents supersede earlier design work at ancestor levels. The following ancestor docs now reference back here:

- `(root)/.0agnostic/01_knowledge/CONTEXT_PROPAGATION_DESIGN.md` → docs 03, 04
- `stage_-1_04_design/outputs/2026-02-03_propagation_chain_architecture.md` → doc 03
- `stage_1_04_design/outputs/design_decisions/context_propagation_design.md` → doc 04
- `stage_1_04_design/outputs/by_topic/04_source_of_truth_to_avenue_flow.md` → doc 06
- `stage_1_04_design/outputs/by_topic/01_unified_sync_architecture.md` → doc 07
- `chain_visualization/diagrams/current/context_propagation.md` → doc 05
