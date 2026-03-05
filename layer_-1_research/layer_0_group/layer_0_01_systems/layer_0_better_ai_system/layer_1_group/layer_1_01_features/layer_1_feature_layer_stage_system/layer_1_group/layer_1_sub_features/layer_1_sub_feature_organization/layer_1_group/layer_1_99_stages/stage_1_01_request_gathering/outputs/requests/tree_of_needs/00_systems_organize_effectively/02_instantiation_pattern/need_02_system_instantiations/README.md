---
resource_id: "25149742-f3ec-4a2d-bd49-041eae9c5bf4"
resource_type: "readme
output"
resource_name: "README"
---
# Need: System Instantiations

**Branch**: [Instantiation Pattern](../README.md)

<!-- section_id: "0fa1522e-794c-426c-bc5b-785f941b834f" -->
## Definition

A system MUST support creating per-user or per-context instances that inherit from the system's production template while maintaining instance-specific state.

<!-- section_id: "b352b586-3275-408b-94c5-f76decd3b7bd" -->
## Why This Matters

A system built for multiple users (students, teams, projects) needs personalized instances. Each instance inherits the system's proven patterns but adds user-specific context, progress, and adaptations.

<!-- section_id: "8e8f13e5-ed1f-4762-80e8-bea6a8ebce68" -->
## Acceptance Criteria

- [ ] Each instance is a child entity of the system
- [ ] Instances inherit from the production template structure
- [ ] Instances can store user-specific context without modifying the template
- [ ] Multiple instances can coexist independently

<!-- section_id: "1eaa6011-2490-44ae-9a88-a6fc6f02e6ce" -->
## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
