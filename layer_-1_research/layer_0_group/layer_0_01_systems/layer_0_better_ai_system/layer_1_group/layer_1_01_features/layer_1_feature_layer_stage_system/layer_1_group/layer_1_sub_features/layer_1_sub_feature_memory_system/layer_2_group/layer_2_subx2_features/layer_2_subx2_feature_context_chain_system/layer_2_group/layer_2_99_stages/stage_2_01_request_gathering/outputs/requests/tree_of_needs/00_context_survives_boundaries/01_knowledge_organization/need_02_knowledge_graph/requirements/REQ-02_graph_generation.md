---
resource_id: "391e5b3e-32c5-4d6f-8afb-418c09af8ad3"
resource_type: "output"
resource_name: "REQ-02_graph_generation"
---
# Graph Generation

**Need**: [Knowledge Graph](../README.md)

---

- MUST auto-generate from 0AGNOSTIC.md declarations (Identity, Pointers, Triggers sections)
- MUST be idempotent (same input -> same output)
- MUST handle missing fields gracefully
- SHOULD integrate into agnostic-sync.sh workflow
- SHOULD run in under 10 seconds for the full tree
