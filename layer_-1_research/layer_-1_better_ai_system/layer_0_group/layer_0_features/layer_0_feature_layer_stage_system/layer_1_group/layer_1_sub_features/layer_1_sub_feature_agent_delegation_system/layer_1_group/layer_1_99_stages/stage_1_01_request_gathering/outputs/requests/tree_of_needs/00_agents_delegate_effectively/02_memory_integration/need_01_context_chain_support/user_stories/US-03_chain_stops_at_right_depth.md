# US-3: Chain stops at the right depth

**Need**: [Context Chain Support](../README.md)

---

**As a** stage agent deep in the hierarchy,
**I want** the context chain to load only my stage and my parent entity (not every ancestor up to root),
**So that** my context window is not consumed by irrelevant ancestor context.

**Acceptance**: Stage agent's chain is limited to 2 levels (self + parent entity).
