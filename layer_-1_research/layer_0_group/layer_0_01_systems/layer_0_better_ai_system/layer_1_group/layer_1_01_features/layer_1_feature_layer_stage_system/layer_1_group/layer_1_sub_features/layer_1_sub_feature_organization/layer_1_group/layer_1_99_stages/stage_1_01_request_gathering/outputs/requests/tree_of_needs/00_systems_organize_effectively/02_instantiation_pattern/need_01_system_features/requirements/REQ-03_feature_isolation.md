---
resource_id: "9460f2e3-6d53-4e3b-bec6-9aa121a4b210"
resource_type: "output"
resource_name: "REQ-03_feature_isolation"
---
# Feature Isolation

**Need**: [System Features](../README.md)

---

- MUST ensure features don't share mutable state
- MUST allow features to reference shared resources (universal `.0agnostic/`)
- SHOULD use the entity boundary as the isolation unit
- SHOULD NOT allow cross-feature modifications without explicit protocols
