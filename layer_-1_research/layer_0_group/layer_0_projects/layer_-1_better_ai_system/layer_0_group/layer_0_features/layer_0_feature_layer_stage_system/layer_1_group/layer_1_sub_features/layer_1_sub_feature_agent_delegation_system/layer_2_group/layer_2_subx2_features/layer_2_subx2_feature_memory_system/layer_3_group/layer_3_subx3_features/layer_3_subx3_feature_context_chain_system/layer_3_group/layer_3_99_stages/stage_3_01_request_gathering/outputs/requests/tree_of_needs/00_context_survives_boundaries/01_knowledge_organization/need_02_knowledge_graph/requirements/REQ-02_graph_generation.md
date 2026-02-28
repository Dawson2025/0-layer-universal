# Graph Generation

**Need**: [Knowledge Graph](../README.md)

---

- MUST auto-generate from 0AGNOSTIC.md declarations (Identity, Pointers, Triggers sections)
- MUST be idempotent (same input -> same output)
- MUST handle missing fields gracefully
- SHOULD integrate into agnostic-sync.sh workflow
- SHOULD run in under 10 seconds for the full tree
