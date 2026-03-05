---
resource_id: "8209522f-7326-4f9d-b244-22d7145675e1"
resource_type: "output"
resource_name: "REQ-03_boundary_rules"
---
# Boundary Rules

**Need**: [Stage Delegation](../README.md)

---

- MUST define what stays with the manager (status overview, cross-stage coordination, priority decisions)
- MUST define what stays with the stage agent (methodology, detailed outputs, domain-specific procedures)
- MUST NOT allow stage agents to make cross-stage decisions (that is the manager's role)
- SHOULD define escalation paths: when a stage agent encounters something outside its scope
