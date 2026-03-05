---
resource_id: "be2cccdf-3de4-4fef-bec7-49113dbad5c6"
resource_type: "output"
resource_name: "US-02_manager_delegates_with_context"
---
# US-2: Manager delegates with sufficient context

**Need**: [Handoff Protocols](../README.md)

---

**As a** user who tells the AI to work on a stage and expects it to just start,
**I want** the manager to provide sufficient context when delegating so the stage agent can begin immediately,
**So that** the AI never comes back asking me for clarification about what it should do.

### What Happens

1. User says "do the design for this feature"
2. Manager reads its stage overview and identifies the design stage
3. Manager spawns a stage agent with: task description + stage directory path
4. Stage agent's first action is reading its own 0AGNOSTIC.md (not asking the manager for clarification)
5. Stage agent begins productive work immediately

### Acceptance Criteria

- Stage agent's first action is reading its 0AGNOSTIC.md, not asking the manager for clarification
- Manager provides task description and directory pointer, nothing more
- User is not asked to provide additional context or instructions
