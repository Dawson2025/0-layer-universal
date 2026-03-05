---
resource_id: "3866f883-d6cf-4c61-8455-4bb3b03baf9c"
resource_type: "output"
resource_name: "REQ-02_manager_delegation_protocol"
---
# Manager Delegation Protocol

**Need**: [Stage Delegation](../README.md)

---

- MUST NOT have managers carry operational knowledge for stages (methodology, templates, step-by-step procedures)
- MUST support the pattern: manager reads status -> decides what stage needs work -> spawns stage agent with task description -> stage agent reads its own 0AGNOSTIC.md
- MUST define what the manager provides to the stage agent (task description, pointers to relevant context)
- MUST define what the stage agent discovers on its own (methodology from 0AGNOSTIC.md, domain knowledge from parent)
