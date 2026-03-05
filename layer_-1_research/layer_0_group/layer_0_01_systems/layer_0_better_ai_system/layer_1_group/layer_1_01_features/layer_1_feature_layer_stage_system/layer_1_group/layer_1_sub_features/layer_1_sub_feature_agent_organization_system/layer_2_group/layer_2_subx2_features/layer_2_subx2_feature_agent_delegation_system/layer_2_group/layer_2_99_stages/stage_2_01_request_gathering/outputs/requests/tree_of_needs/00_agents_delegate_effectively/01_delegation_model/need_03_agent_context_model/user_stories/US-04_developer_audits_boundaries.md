---
resource_id: "2c7a54f5-5027-4a83-961f-58100a32b932"
resource_type: "output"
resource_name: "US-04_developer_audits_boundaries"
---
# US-4: Developer can audit context boundaries

**Need**: [Agent Context Model](../README.md)

---

**As a** user who wants to verify agents are loading the right amount of context,
**I want** a documented context model for each agent type showing what goes in static, dynamic, and never-loaded,
**So that** I can audit whether agents are operating within their intended scope.

<!-- section_id: "e06825ea-f64d-4921-b988-02fa6ee72fff" -->
### What Happens

1. User wants to verify the system's context architecture is sound
2. User reads the context model document for each agent type (manager, stage agent, sub-feature agent)
3. Document shows three columns: static (always loaded), dynamic (on-demand), never-loaded
4. User can verify that managers don't carry stage methodology and stage agents don't carry peer details
5. User confirms the boundaries match the intended design

<!-- section_id: "dfb4366b-b6f6-4e3c-a97b-895d74160695" -->
### Acceptance Criteria

- Context model document exists with three columns (static / dynamic / never) for each agent type
- Document covers all three agent types: manager, stage agent, sub-feature agent
- Boundaries are specific enough to be auditable (not vague descriptions)
