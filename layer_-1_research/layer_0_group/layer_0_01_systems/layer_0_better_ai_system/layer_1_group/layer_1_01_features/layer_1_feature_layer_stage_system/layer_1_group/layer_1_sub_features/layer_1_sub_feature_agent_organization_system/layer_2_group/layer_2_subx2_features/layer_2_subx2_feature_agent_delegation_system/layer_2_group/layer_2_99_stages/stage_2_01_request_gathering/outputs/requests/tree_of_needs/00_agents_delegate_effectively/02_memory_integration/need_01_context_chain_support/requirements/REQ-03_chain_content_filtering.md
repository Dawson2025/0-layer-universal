---
resource_id: "c02cc6d5-be93-440b-bc34-9a92bab5fb7f"
resource_type: "output"
resource_name: "REQ-03_chain_content_filtering"
---
# Chain Content Filtering

**Need**: [Context Chain Support](../README.md)

---

- MUST define what content from each chain level is loaded (identity only? identity + triggers? full 0AGNOSTIC.md?)
- SHOULD load progressively less detail at each parent level (self: full, parent: identity + triggers, grandparent: identity only)
- MUST NOT load sibling entities through the chain (only direct ancestors)
