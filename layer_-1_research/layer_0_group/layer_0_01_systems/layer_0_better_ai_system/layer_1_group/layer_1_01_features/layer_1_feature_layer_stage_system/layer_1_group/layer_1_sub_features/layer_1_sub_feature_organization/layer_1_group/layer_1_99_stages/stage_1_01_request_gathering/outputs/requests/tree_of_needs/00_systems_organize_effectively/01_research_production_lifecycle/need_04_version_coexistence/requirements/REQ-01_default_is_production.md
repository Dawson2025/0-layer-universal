---
resource_id: "fffdc48b-066e-41a0-bd0b-7173d4ed4de1"
resource_type: "output"
resource_name: "REQ-01_default_is_production"
---
# Default is Production

**Need**: [Version Coexistence](../README.md)

---

- MUST make production content the default context chain for all agents
- MUST NOT require agents to explicitly request production mode — it's the baseline
- SHOULD load research context only when triggered by explicit user request or rule
