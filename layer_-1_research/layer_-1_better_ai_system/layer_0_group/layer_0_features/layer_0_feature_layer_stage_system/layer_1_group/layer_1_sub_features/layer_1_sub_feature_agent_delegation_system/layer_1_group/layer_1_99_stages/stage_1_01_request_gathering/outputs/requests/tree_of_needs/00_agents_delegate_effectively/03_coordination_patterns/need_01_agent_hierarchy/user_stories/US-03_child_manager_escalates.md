# US-3: Child manager escalates to parent

**Need**: [Agent Hierarchy](../README.md)

---

**As a** user who works on a sub-feature and expects cross-entity decisions to be made at the right level,
**I want** the child entity manager to have a clear escalation path to its parent manager,
**So that** decisions that affect multiple sub-features are not made in isolation by a single child agent.

### What Happens

1. User is working on a sub-feature and the child manager encounters a cross-entity decision
2. Child manager identifies the issue requires parent-level coordination
3. Child manager escalates to its parent entity manager via the documented escalation path
4. Parent manager receives the escalation and can coordinate across child entities
5. User gets a decision made at the appropriate hierarchical level

### Acceptance Criteria

- Escalation path is documented and follows the entity tree upward
- Child manager knows when to escalate (cross-entity scope, conflicting requirements)
- Parent manager receives sufficient context to make the decision
