# Feature Isolation

**Need**: [System Features](../README.md)

---

- MUST ensure features don't share mutable state
- MUST allow features to reference shared resources (universal `.0agnostic/`)
- SHOULD use the entity boundary as the isolation unit
- SHOULD NOT allow cross-feature modifications without explicit protocols
