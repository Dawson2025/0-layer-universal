---
resource_id: "de873c6b-a8da-4891-8d6a-2054929d8de1"
resource_type: "output"
resource_name: "REQ-01_scoring_function"
---
# Scoring Function

**Need**: [Scored Context Retrieval](../README.md)

---

- MUST define composite score: recency x relevance x importance (weights tunable)
- MUST support scoring across tiers (knowledge files, stage outputs, episodic notes)
- SHOULD use metadata embedded in files (frontmatter, headers, or companion metadata files)
