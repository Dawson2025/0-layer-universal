---
resource_id: "e25f7508-e279-4eb4-9f50-1b4879513ee9"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Research Version

**Branch**: [Research/Production Lifecycle](../README.md)

<!-- section_id: "3b650ac9-83e5-4243-ae92-4d180354c6c0" -->
## Definition

A system MUST have a dedicated research version (layer_-1) where experimental features, exploratory work, and unproven ideas can be developed without affecting production stability.

<!-- section_id: "d2de98db-c73e-4c92-90e6-0deb66b8de77" -->
## Why This Matters

Without a research space, either (a) all changes go directly to production (risky), or (b) experimentation is discouraged (stagnation). Research entities give explicit permission to fail and iterate.

<!-- section_id: "aa3eb3a1-fc69-4be9-8de5-d21772fc0ff4" -->
## Acceptance Criteria

- [ ] Research entities live in `layer_-1_research/` at the system level
- [ ] Research entities have full stage lifecycle (01-11)
- [ ] Research entities can reference production entities without modifying them
- [ ] Research entities are isolated — failures don't cascade to production

<!-- section_id: "865406d6-9410-472e-b590-b5ab9fdba004" -->
## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
