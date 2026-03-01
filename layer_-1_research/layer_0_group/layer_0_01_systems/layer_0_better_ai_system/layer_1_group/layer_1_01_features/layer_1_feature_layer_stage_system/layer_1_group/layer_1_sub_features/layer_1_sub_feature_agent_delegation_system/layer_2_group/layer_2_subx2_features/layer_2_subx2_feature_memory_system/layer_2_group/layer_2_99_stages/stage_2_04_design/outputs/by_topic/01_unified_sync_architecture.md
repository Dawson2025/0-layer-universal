# Unified Sync Architecture

> **This document is a pointer.** The canonical source of truth lives in the context chain system (Layer 3).

## Canonical Source

**Full design**: `layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_context_chain_system/layer_3_group/layer_3_99_stages/stage_3_04_design/outputs/by_topic/07_unified_sync_architecture.md`

## Quick Summary

5 existing sync scripts (agnostic-sync.sh, episodic-sync.sh, jsonld-to-md.sh, sync-handoffs.sh, user-level-sync.sh) plus a designed orchestrator (sync-main.sh) that coordinates them in 4 phases:

1. **Foundation** (sequential): agnostic-sync → jsonld-to-md → sync-handoffs
2. **Aggregation** (sequential): episodic-sync
3. **Data avenues** (parallel): build-graph, build-index, build-embeddings, build-temporal, build-shimi
4. **Extension** (sequential): user-level-sync

Zero-dependency guarantee: file-based syncs always work with standard unix tools. Data-based syncs are optional.

See the canonical source for complete CLI interface, execution order, sync registry, and implementation status.

---

*Converted to pointer on 2026-02-23 — the context chain system (Layer 3) now owns the detailed design.*
