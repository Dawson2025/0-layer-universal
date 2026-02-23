# Design Decision: Context Propagation

**Date**: 2026-02-21
**Status**: Approved and implemented

## Decision

Define how work products consolidate within stages and propagate across the layer-stage hierarchy via a **consolidation funnel** pattern.

## Universal Artifact

The full design document is a universal artifact at:
`(root)/.0agnostic/01_knowledge/CONTEXT_PROPAGATION_DESIGN.md`

It is universal because the propagation pattern applies to ALL entities, not just the agent_delegation_system.

## Summary

Two core diagrams:

1. **Stage-Internal Consolidation Funnel**: outputs → output_report → .0agnostic/ → stage_report → 0AGNOSTIC.md (most detail → most consolidated)
2. **Cross-Level Connection Map**: stages → entity (via stage_reports), child entities → parent entity (via layer_reports), with consolidation reports (stages_report.md, child_layers_report.md) at the entity level

Key insight: stages and entities follow the **same pattern** — many inputs → consolidation overview → structured system → summary report → entry point.

## Rationale

- Existing docs covered top-down loading (how agents receive context) but not bottom-up propagation (how outputs flow upward)
- Without this design, the consolidation funnel was implicit — agents didn't know the expected flow
- The handoff document system had structure (incoming/outgoing × above/sides/below) but no documented lifecycle

## Alternatives Considered

| Alternative | Why Rejected |
|-------------|-------------|
| Merge into AI_CONTEXT_FLOW_ARCHITECTURE.md | That doc is already 680+ lines; different concern (loading vs propagation) |
| Per-entity propagation docs | The pattern is universal — one doc covers all |
| No formal doc (keep implicit) | Agents need explicit guidance on the consolidation order |

## Artifacts Produced

- `(root)/.0agnostic/01_knowledge/CONTEXT_PROPAGATION_DESIGN.md` — the design doc
- Cross-reference added to `AI_CONTEXT_FLOW_ARCHITECTURE.md`
- This entity (ADS) serves as the first implementation example

## Related Decisions

- 0AGNOSTIC.md as stage identity (prior decision)
- Stage reports for async communication (prior decision)
- Two-halves context pattern — Principle 9 (prior decision)
- Handoff document population — sync-handoffs.sh (prior implementation)
