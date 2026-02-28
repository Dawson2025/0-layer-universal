# Chain Loading for Delegation

**Need**: [Context Chain Support](../README.md)

---

- MUST define which context chain entries are relevant for delegation decisions (entity identity, children list, stage status)
- MUST ensure the manager's context chain includes enough information to decide "which stage needs work?"
- MUST ensure the stage agent's context chain includes the parent entity's identity and scope
- MUST NOT load the full parent knowledge directory automatically -- only pointers and triggers
