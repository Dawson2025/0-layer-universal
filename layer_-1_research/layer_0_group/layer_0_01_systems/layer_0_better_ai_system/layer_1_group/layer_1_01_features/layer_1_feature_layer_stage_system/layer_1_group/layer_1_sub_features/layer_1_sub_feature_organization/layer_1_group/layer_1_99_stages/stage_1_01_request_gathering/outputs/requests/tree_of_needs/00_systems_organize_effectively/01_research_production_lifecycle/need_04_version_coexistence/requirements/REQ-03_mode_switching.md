---
resource_id: "d0a6e076-4612-4190-9438-420f181ffdda"
resource_type: "output"
resource_name: "REQ-03_mode_switching"
---
# Mode Switching

**Need**: [Version Coexistence](../README.md)

---

- SHOULD support context chain mode switching (production ↔ research)
- SHOULD log when an agent switches modes for traceability
- MAY support hybrid mode where both production and research context are loaded
- MUST ensure mode switch does not corrupt either version's state
