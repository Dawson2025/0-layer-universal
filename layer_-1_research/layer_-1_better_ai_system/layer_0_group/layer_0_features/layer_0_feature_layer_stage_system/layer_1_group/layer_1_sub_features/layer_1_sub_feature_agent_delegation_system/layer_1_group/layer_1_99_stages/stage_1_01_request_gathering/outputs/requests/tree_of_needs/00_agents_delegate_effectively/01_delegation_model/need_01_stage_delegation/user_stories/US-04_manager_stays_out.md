# US-4: Manager stays out of stage-level work

**Need**: [Stage Delegation](../README.md)

---

**As a** user who wants to verify the AI system is well-organized,
**I want** the manager agent to contain only coordination logic and no stage-level methodology,
**So that** I can trust the manager is focused on orchestration and not bloated with operational detail.

### What Happens

1. User reviews the manager's 0AGNOSTIC.md to check system health
2. User sees only: status overview, cross-stage coordination rules, and priority decisions
3. User confirms there is zero stage-level methodology or procedure in the manager
4. User knows the manager has room in its context window for actual coordination work

### Acceptance Criteria

- Manager's 0AGNOSTIC.md contains zero stage-level methodology or procedure descriptions
- Manager context focuses on status overview, children list, and delegation rules
- A human reviewer can confirm the separation by reading the manager's identity file
