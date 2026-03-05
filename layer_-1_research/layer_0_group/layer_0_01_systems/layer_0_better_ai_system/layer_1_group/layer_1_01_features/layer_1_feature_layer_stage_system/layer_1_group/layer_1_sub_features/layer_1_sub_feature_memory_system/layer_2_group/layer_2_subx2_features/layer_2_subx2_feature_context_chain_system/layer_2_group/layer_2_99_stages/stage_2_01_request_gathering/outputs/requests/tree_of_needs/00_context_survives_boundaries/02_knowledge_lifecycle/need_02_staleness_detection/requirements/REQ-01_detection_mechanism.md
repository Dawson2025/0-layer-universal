---
resource_id: "54915394-7fb2-41af-9963-db70c272d84d"
resource_type: "output"
resource_name: "REQ-01_detection_mechanism"
---
# Detection Mechanism

**Need**: [Staleness Detection](../README.md)

---

- MUST compare knowledge file timestamps against referenced stage output timestamps
- MUST flag knowledge files whose sources have been modified since last consolidation
- SHOULD detect content drift (source changed substantially, not just minor edits)
- SHOULD integrate into chain-validate skill
