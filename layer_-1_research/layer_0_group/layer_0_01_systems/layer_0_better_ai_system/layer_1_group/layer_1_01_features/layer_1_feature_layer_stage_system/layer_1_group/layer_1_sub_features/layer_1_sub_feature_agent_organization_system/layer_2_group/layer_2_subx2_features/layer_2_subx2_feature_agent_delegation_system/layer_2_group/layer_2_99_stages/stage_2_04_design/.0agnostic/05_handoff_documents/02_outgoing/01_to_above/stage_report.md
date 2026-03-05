# Stage Report: 04_design

## Status
active

## Last Updated
2026-02-26

## Summary
10 architecture decisions for agent delegation — 7 made implicitly through development (0AGNOSTIC.md pattern, two-halves, stage reports, scope boundaries, universal guides), plus 3 formal designs: context propagation (consolidation funnel), minimal context model (own STATIC + neighbor interfaces + on-demand), and directional scope boundaries (3-step scope decision with per-direction communication).

## Key Outputs
- `outputs/design_decisions/context_propagation_design.md`: Consolidation funnel design (references universal artifact at root `.0agnostic/01_knowledge/CONTEXT_PROPAGATION_DESIGN.md`)
- `outputs/design_decisions/propagation_funnel_stage_contract.md`: Local stage/entity contract for canonical report and handoff structure
- `outputs/design_decisions/minimal_context_model.md`: Agents get own STATIC + compact neighbor interfaces + on-demand DYNAMIC. No full ancestor cascade. Validated by tool cascading and multi-agent framework research.
- `outputs/design_decisions/directional_scope_boundaries.md`: 3-step scope decision: identify direction (up/down/left/right/sideways/multi-location) → decide handling → communicate per direction. Multi-location escalates to nearest common ancestor.
- `outputs/design_decisions/stages_manager_pattern.md`: Manager-stage delegation patterns
- 7 implicit decisions documented in 0AGNOSTIC.md Current State Detail

## Findings
- **Context propagation design**: Stages and entities follow the same consolidation funnel — outputs → output_report → .0agnostic → stage_report → 0AGNOSTIC.md
- **Entity consolidation**: Entities need stages_report.md + child_layers_report.md to consolidate incoming reports before producing their own layer_report.md
- **0AGNOSTIC.md as entry point**: The most consolidated document at any level — comes LAST in the funnel, not first
- **Minimal context model**: Three-layer context — own STATIC, compact neighbor interfaces, on-demand DYNAMIC. Full cascade rejected (context waste at depth, validated by multi-agent framework research showing minimal + on-demand outperforms)
- **Directional scope boundaries**: Scope decisions are directional — direction determines communication method. Multi-location work escalates to nearest common ancestor with scope over all affected locations
- **Tool cascading supports minimal model**: 3/4 AI coding tools cascade CLAUDE.md natively, making lean content per level critical to prevent bloat at depth

## Open Items
- Multi-agent spawning patterns not yet designed
- Cursor-specific context strategy (glob targeting vs self-contained rules) needs design doc
- Propagation design applied to ADS entity but not yet to other entities

## Handoff
- **Ready for next stage**: yes
- **Next stage**: 05_planning / 06_development
- **What next stage needs to know**: Apply minimal context model when writing 0AGNOSTIC.md files — keep STATIC lean, use neighbor interfaces not full cascade. Apply directional scope boundaries when agents cross boundaries. Context propagation funnel for report structure.
