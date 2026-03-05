---
resource_id: "3e0ecbd4-d52a-4752-a3f1-feebc8d54899"
resource_type: "output"
resource_name: "US-03_active_agent_accesses_own_content"
---
# US-3: Active stage agent accesses its own full content

**Need**: [Three-Tier Delegation](../README.md)

---

**As a** user who tells the AI to continue working on a stage that already has prior outputs,
**I want** the stage agent to have full access to its own stage outputs (Tier 3) so it can build on previous work,
**So that** the AI does not re-create work that already exists in the stage.

<!-- section_id: "be10b04f-9082-46d4-800a-6ac9bbca201b" -->
### What Happens

1. User says "continue the development work" on a stage that already has outputs
2. Manager spawns a stage agent for the development stage
3. Stage agent reads its own Tier 3 content: its stage's outputs and work-in-progress files
4. Stage agent does NOT read other stages' Tier 3 outputs
5. Stage agent builds on existing work rather than starting from scratch

<!-- section_id: "7f8eac2a-dd9d-422e-b28d-bd96c025e096" -->
### Acceptance Criteria

- Stage agent reads its own stage outputs, not other stages' outputs
- Agent can identify and build on prior work within its stage
- Tier 3 access is scoped to the active agent's own stage only
