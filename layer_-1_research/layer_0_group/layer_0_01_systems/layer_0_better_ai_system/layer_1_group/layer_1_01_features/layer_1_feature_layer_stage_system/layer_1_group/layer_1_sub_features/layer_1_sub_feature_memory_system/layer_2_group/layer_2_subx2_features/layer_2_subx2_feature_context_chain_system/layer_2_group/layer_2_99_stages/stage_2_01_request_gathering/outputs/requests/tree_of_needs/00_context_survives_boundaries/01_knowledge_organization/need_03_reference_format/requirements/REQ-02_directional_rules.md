---
resource_id: "4861647b-fe0f-4f3f-a066-f51ac87c24d8"
resource_type: "output"
resource_name: "REQ-02_directional_rules"
---
# Directional Rules

**Need**: [Reference Format Standard](../README.md)

---

- MUST define: knowledge files reference stage outputs (downward)
- MUST define: 0AGNOSTIC.md references knowledge files and stage index (downward)
- MUST NOT: stage outputs reference knowledge files (upward references create coupling)
- SHOULD: stage outputs be self-contained (readable without knowledge files)
