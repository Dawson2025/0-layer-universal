---
resource_id: "d06264fb-2ddd-4877-8bfe-8855b81ccff3"
resource_type: "output"
resource_name: "US-03_child_manager_escalates"
---
# US-3: Child manager escalates to parent

**Need**: [Agent Hierarchy](../README.md)

---

**As a** user who works on a sub-feature and expects cross-entity decisions to be made at the right level,
**I want** the child entity manager to have a clear escalation path to its parent manager,
**So that** decisions that affect multiple sub-features are not made in isolation by a single child agent.

<!-- section_id: "96f63f3b-a05d-4a1d-8e3d-ebada472d370" -->
### What Happens

1. User is working on a sub-feature and the child manager encounters a cross-entity decision
2. Child manager identifies the issue requires parent-level coordination
3. Child manager escalates to its parent entity manager via the documented escalation path
4. Parent manager receives the escalation and can coordinate across child entities
5. User gets a decision made at the appropriate hierarchical level

<!-- section_id: "70d0f858-a7af-4c66-bad5-15e6fe7ab961" -->
### Acceptance Criteria

- Escalation path is documented and follows the entity tree upward
- Child manager knows when to escalate (cross-entity scope, conflicting requirements)
- Parent manager receives sufficient context to make the decision
