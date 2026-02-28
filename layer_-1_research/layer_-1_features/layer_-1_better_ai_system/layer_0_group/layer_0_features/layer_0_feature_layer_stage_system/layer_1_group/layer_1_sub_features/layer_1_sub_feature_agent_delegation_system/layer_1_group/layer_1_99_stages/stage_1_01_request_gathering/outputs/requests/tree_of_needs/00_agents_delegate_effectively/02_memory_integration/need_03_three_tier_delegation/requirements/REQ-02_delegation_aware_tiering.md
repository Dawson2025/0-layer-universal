# Delegation-Aware Tiering

**Need**: [Three-Tier Delegation](../README.md)

---

- MUST ensure that delegation decisions can be made from Tier 1 alone (managers never need to read Tier 3 to decide what to delegate)
- MUST ensure that stage agents can do their work with Tier 2 + their own Tier 3 (no dependency on other stages' Tier 3)
- SHOULD define when an agent legitimately needs to access a higher-detail tier (escalation, cross-stage dependency)
