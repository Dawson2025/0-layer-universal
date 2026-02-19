# Chain Content Filtering

**Need**: [Context Chain Support](../README.md)

---

- MUST define what content from each chain level is loaded (identity only? identity + triggers? full 0AGNOSTIC.md?)
- SHOULD load progressively less detail at each parent level (self: full, parent: identity + triggers, grandparent: identity only)
- MUST NOT load sibling entities through the chain (only direct ancestors)
