---
resource_id: "3a9d2591-59f0-4b71-9ec4-6a166dcd1ab9"
resource_type: "output"
resource_name: "01_unified_sync_architecture"
---
# Unified Sync Architecture

> **This document is a pointer.** The canonical source of truth lives in the context chain system (Layer 2).

<!-- section_id: "6da3e9fe-1f22-4f43-9e2c-6443ac5594ba" -->
## Canonical Source

**Full design**: `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/layer_2_group/layer_2_99_stages/stage_2_04_design/outputs/by_topic/07_unified_sync_architecture.md`

<!-- section_id: "793c5537-0b18-4a40-9fc7-e57342028ccc" -->
## Quick Summary

5 existing sync scripts (agnostic-sync.sh, episodic-sync.sh, jsonld-to-md.sh, sync-handoffs.sh, user-level-sync.sh) plus a designed orchestrator (sync-main.sh) that coordinates them in 4 phases:

1. **Foundation** (sequential): agnostic-sync → jsonld-to-md → sync-handoffs
2. **Aggregation** (sequential): episodic-sync
3. **Data avenues** (parallel): build-graph, build-index, build-embeddings, build-temporal, build-shimi
4. **Extension** (sequential): user-level-sync

Zero-dependency guarantee: file-based syncs always work with standard unix tools. Data-based syncs are optional.

See the canonical source for complete CLI interface, execution order, sync registry, and implementation status.

---

*Converted to pointer on 2026-02-23 — the context chain system (Layer 2) now owns the detailed design.*
