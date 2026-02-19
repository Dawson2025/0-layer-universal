# US-3: Sub-feature agent sees its own tree

**Need**: [Agent Context Model](../README.md)

---

**As a** sub-feature agent managing a child entity,
**I want** my context model to include my entity identity and my own stages, but not my sibling entities' internals,
**So that** I stay focused on my scope without being distracted by unrelated context.

**Acceptance**: Sub-feature agent's context excludes all sibling entity details.
