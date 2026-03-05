---
resource_id: "801fc053-f733-41e9-b52d-d82a9ec85c14"
resource_type: "output"
resource_name: "REQ-01_stage_agent_identity"
---
# Stage Agent Identity

**Need**: [Stage Delegation](../README.md)

---

- MUST have a `0AGNOSTIC.md` in every stage directory with: identity (role, scope), methodology, output format, and success criteria
- MUST define the stage agent's scope boundary -- what it does and does NOT do
- MUST reference parent entity for domain context (e.g., "Read `../../.0agnostic/knowledge/` for domain understanding")
- SHOULD include triggers that define when this stage agent is activated
