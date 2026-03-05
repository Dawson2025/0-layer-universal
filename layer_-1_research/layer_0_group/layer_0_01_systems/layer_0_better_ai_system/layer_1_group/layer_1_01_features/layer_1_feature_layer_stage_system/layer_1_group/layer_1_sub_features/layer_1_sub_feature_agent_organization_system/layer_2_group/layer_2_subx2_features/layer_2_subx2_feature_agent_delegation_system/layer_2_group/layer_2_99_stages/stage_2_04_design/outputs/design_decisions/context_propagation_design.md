---
resource_id: "37f8bb04-b355-4ac8-affb-0e4238b244b6"
resource_type: "output"
resource_name: "context_propagation_design"
---
# Design Decision: Context Propagation

**Date**: 2026-02-21
**Status**: Approved — canonical source moved to context chain system (Layer 3)

> **This document is a pointer.** The canonical source of truth for context propagation design lives in the context chain system, which owns this domain.

<!-- section_id: "e9bc78b3-cb35-477f-bb7d-74ef934263c6" -->
## Canonical Source

**Bottom-up consolidation funnel**: `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_context_chain_system/layer_3_group/layer_3_99_stages/stage_3_04_design/outputs/by_topic/04_context_propagation_funnel.md`

**Full design index**: `...stage_3_04_design/outputs/by_topic/README.md`

**Local stage contract**: `outputs/design_decisions/propagation_funnel_stage_contract.md`

<!-- section_id: "7714e658-f4a8-4a15-95e5-2e51fd1f74ce" -->
## Decision Summary

Define how work products consolidate within stages and propagate across the layer-stage hierarchy via a **consolidation funnel** pattern. The funnel is recursive: stages, entities, and root all follow the same pattern of many inputs → consolidation → structured system → summary report → entry point.

<!-- section_id: "4c995131-9051-4422-a258-d873982da158" -->
## Rationale

The context chain system (Layer 3 child of memory_system) is the dedicated sub-feature for context flow architecture. Moving the detailed design there follows the principle that the entity owning the domain should own the source of truth.

---

*Converted to pointer on 2026-02-23 — previously referenced (root)/.0agnostic/01_knowledge/CONTEXT_PROPAGATION_DESIGN.md as the universal artifact.*
