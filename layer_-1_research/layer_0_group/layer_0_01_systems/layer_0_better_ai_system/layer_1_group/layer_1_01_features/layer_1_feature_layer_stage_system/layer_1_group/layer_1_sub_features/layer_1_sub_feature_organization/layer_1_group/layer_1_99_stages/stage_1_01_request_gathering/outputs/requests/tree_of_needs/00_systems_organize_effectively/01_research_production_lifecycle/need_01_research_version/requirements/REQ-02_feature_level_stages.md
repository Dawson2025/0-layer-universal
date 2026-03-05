---
resource_id: "cb77f65d-bc25-4197-93ad-1dacf8978240"
resource_type: "output"
resource_name: "REQ-02_feature_level_stages"
---
# Feature-Level Stages

**Need**: [Research Version](../README.md)

---

- MUST provide all 11 stages in each research entity's `layer_N_99_stages/`
- MUST allow stages to be empty (valid) — missing stages are NOT valid
- SHOULD allow research entities to have sub-features with their own stage cycles
- SHOULD track stage status (empty, active, complete) in the stages container
