# Detection Mechanism

**Need**: [Staleness Detection](../README.md)

---

- MUST compare knowledge file timestamps against referenced stage output timestamps
- MUST flag knowledge files whose sources have been modified since last consolidation
- SHOULD detect content drift (source changed substantially, not just minor edits)
- SHOULD integrate into chain-validate skill
