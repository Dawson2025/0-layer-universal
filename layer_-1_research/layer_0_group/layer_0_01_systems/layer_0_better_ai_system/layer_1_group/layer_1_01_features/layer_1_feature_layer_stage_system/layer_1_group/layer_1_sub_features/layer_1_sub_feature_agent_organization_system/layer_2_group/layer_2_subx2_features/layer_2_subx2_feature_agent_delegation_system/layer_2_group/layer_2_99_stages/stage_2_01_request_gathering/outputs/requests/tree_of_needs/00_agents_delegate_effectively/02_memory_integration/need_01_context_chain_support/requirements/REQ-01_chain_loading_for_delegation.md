---
resource_id: "153e8251-6fb7-4a5a-ad86-9e5d84c240bc"
resource_type: "output"
resource_name: "REQ-01_chain_loading_for_delegation"
---
# Chain Loading for Delegation

**Need**: [Context Chain Support](../README.md)

---

- MUST define which context chain entries are relevant for delegation decisions (entity identity, children list, stage status)
- MUST ensure the manager's context chain includes enough information to decide "which stage needs work?"
- MUST ensure the stage agent's context chain includes the parent entity's identity and scope
- MUST NOT load the full parent knowledge directory automatically -- only pointers and triggers
