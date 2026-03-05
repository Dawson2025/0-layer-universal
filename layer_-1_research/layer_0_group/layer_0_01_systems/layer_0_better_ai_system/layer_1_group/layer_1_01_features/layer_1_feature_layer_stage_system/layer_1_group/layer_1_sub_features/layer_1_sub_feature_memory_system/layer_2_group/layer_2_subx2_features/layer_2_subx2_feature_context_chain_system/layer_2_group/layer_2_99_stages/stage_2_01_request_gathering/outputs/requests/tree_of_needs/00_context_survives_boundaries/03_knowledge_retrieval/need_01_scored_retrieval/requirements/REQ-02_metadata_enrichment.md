---
resource_id: "814f98f1-a85a-474b-b71a-c65bbc81d43f"
resource_type: "output"
resource_name: "REQ-02_metadata_enrichment"
---
# Metadata Enrichment

**Need**: [Scored Context Retrieval](../README.md)

---

- MUST define what metadata each file needs (creation date, last modified, importance, tags)
- SHOULD use YAML frontmatter in markdown files
- SHOULD be backward-compatible (files without metadata still work, just scored lower)
