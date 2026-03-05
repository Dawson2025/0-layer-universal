---
resource_id: "98d25913-8d92-4c35-8d70-f8a33cb59a1f"
resource_type: "output"
resource_name: "REQ-01_tier_to_agent_mapping"
---
# Tier-to-Agent Mapping

**Need**: [Three-Tier Delegation](../README.md)

---

- MUST define which tier each agent type primarily operates at:
  - Manager: Tier 1 (pointers) -- 0AGNOSTIC.md, stage overview, children list
  - Stage Agent: Tier 2 (distilled) -- .0agnostic/knowledge/ files relevant to the task
  - Active Stage Agent: Tier 3 (full) -- stage outputs it is currently producing or consuming
- MUST NOT have managers routinely access Tier 3 content
- MUST NOT have stage agents routinely access Tier 3 content from other stages
