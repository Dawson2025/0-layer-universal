---
resource_id: "b72eea0b-4a14-4543-810e-fefc68b18741"
resource_type: "proposal"
resource_name: "resource_index_promotion_summary"
proposal_id: "cd5d4f2c-5ed4-46fd-ab2f-1cd6968f53f2"
status: "Executed"
created: "2026-03-06"
---
# Resource Index Promotion Proposal

## Objective

Promote resource-level UUID indexing from research prototypes into the canonical AI-context toolchain so pointer resolution can target exact resources via `canonical_resource_id`.

## Scope

This proposal is intentionally limited to a first canonical rollout:

1. Add a canonical root script to generate per-entity `resource_index.json` files.
2. Update root pointer sync to aggregate resource indexes into `.uuid-index.json`.
3. Update root pointer sync to resolve `canonical_resource_id` directly.
4. Generate one pilot canonical `resource_index.json` for the active context-chain entity.
5. Update required discovery/sync files caused by `.0agnostic/` changes.

## Planned File Changes

### Root canonical tooling

- `UPDATE` `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/pointer-sync.sh`
  - Read per-entity `resource_index.json`
  - Include resource UUIDs in root `.uuid-index.json`
  - Resolve `canonical_resource_id` before entity/stage fallback

- `NEW` `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/create-resource-indexes.sh`
  - Build per-entity `.0agnostic/resource_index.json` from tracked UUID-bearing files

- `UPDATE` `/home/dawson/dawson-workspace/code/0_layer_universal/.uuid-index.json`
  - Rebuilt aggregated index with resource entries included

### Root discovery/sync chain

- `UPDATE` `/home/dawson/dawson-workspace/code/0_layer_universal/0AGNOSTIC.md`
  - Register the new canonical resource-index generator in discovery pointers

- `UPDATE` `/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md`
- `UPDATE` `/home/dawson/dawson-workspace/code/0_layer_universal/AGENTS.md`
- `UPDATE` `/home/dawson/dawson-workspace/code/0_layer_universal/GEMINI.md`
- `UPDATE` `/home/dawson/dawson-workspace/code/0_layer_universal/OPENAI.md`
  - Regenerated via `agnostic-sync.sh`

### Pilot entity rollout

- `NEW` `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_0_group/layer_0_01_systems/layer_0_better_ai_system/layer_1_group/layer_1_01_features/layer_1_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_memory_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/.0agnostic/resource_index.json`
  - Authoritative resource UUID index for the active context-chain entity

- `UPDATE` `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_0_group/layer_0_01_systems/layer_0_better_ai_system/layer_1_group/layer_1_01_features/layer_1_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_memory_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/0AGNOSTIC.md`
  - Add discovery reference for the new local `resource_index.json`

## Explicit Non-Scope

- No bulk rollout to every entity in the repository yet
- No pointer migration/backfill in `migrate-pointers.sh` yet
- No post-merge hook updates yet
- No directory UUID index work in this proposal

## Validation Plan

1. Generate pilot `resource_index.json` for the context-chain entity.
2. Rebuild root `.uuid-index.json` and confirm resource UUIDs are present.
3. Validate existing pointers still pass.
4. Add one controlled `canonical_resource_id` test case and confirm direct resolution works.

## Approval Checklist

- [x] Proposal reviewed
- [x] File set approved
- [x] Propagation chain approved
- [x] Ready to execute

## Execution Status

- Approval: Approved on 2026-03-06
- Execution: Completed on 2026-03-06

## Execution Notes

- Canonical `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/create-resource-indexes.sh` added.
- Canonical `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/pointer-sync.sh` updated to aggregate `resource_index.json` entries and resolve `canonical_resource_id`.
- Pilot `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_0_group/layer_0_01_systems/layer_0_better_ai_system/layer_1_group/layer_1_01_features/layer_1_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_memory_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/.0agnostic/resource_index.json` generated.
- Root and pilot generated tool files were regenerated via `agnostic-sync.sh` to satisfy the agnostic update protocol.
