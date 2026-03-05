---
resource_id: "2968cde8-e549-4a5e-9b27-c3525a74863d"
resource_type: "output"
resource_name: "REQ-03_stage_agent_context_model"
---
# Stage Agent Context Model

**Need**: [Agent Context Model](../README.md)

---

- MUST include in static: stage identity (stage 0AGNOSTIC.md), parent entity identity
- MUST include in dynamic: parent knowledge files (only relevant ones), prior stage report
- MUST NOT include: peer stage outputs, sibling stage methodology, manager-level coordination
- SHOULD include in dynamic: relevant sub-layer rules (static rules always, dynamic rules when triggered)
