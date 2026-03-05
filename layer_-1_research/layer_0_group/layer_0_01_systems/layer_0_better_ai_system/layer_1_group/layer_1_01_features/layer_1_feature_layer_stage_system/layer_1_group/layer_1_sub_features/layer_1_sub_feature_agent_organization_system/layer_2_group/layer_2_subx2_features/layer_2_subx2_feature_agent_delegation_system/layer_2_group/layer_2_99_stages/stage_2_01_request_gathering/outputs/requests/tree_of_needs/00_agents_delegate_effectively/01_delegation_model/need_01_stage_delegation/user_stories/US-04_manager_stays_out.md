---
resource_id: "2b8f94c1-8519-4b5c-98a7-8025db009925"
resource_type: "output"
resource_name: "US-04_manager_stays_out"
---
# US-4: Manager stays out of stage-level work

**Need**: [Stage Delegation](../README.md)

---

**As a** user who wants to verify the AI system is well-organized,
**I want** the manager agent to contain only coordination logic and no stage-level methodology,
**So that** I can trust the manager is focused on orchestration and not bloated with operational detail.

<!-- section_id: "86f4f89f-1a78-48db-b1e2-b8e3977735a2" -->
### What Happens

1. User reviews the manager's 0AGNOSTIC.md to check system health
2. User sees only: status overview, cross-stage coordination rules, and priority decisions
3. User confirms there is zero stage-level methodology or procedure in the manager
4. User knows the manager has room in its context window for actual coordination work

<!-- section_id: "605bf0d1-4995-4b3c-8ef7-9e42604299ce" -->
### Acceptance Criteria

- Manager's 0AGNOSTIC.md contains zero stage-level methodology or procedure descriptions
- Manager context focuses on status overview, children list, and delegation rules
- A human reviewer can confirm the separation by reading the manager's identity file
