# Context Propagation Diagram

> **This document is a pointer.** The canonical source of truth for hierarchy inheritance and propagation lives in the context chain system (Layer 2) design docs.

## Canonical Source

**Hierarchy inheritance model**: `../../../layer_2_group/layer_2_99_stages/stage_2_04_design/outputs/by_topic/05_hierarchy_inheritance_model.md`

**Top-down propagation chain**: `../../../layer_2_group/layer_2_99_stages/stage_2_04_design/outputs/by_topic/03_propagation_chain_architecture.md`

**Full design index**: `../../../layer_2_group/layer_2_99_stages/stage_2_04_design/outputs/by_topic/README.md`

## Quick Summary

- Parent context flows DOWN to children (inheritance model)
- Children INHERIT (can extend, can override) but CANNOT remove parent context
- 4 propagation mechanisms: CLAUDE.md cascade, 0AGNOSTIC parent chain, .0agnostic resource inheritance, hot rule promotion
- 4 documented gaps: childNaming not enforced, layer number not calculated, no inherited context visibility, dynamic rules don't inherit
- See canonical sources for complete diagrams, propagation rules summary table, and mitigation strategies

---

*Previously a full diagram doc (320 lines). Converted to pointer on 2026-02-23 — the parent entity's design docs now contain the detailed architecture with improved diagrams.*
