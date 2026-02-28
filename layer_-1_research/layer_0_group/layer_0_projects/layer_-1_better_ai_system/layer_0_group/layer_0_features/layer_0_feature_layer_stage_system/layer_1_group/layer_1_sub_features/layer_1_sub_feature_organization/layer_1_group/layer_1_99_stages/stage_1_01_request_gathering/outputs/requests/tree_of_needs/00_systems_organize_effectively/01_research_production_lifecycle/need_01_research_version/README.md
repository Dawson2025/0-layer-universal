# Need: Research Version

**Branch**: [Research/Production Lifecycle](../README.md)

## Definition

A system MUST have a dedicated research version (layer_-1) where experimental features, exploratory work, and unproven ideas can be developed without affecting production stability.

## Why This Matters

Without a research space, either (a) all changes go directly to production (risky), or (b) experimentation is discouraged (stagnation). Research entities give explicit permission to fail and iterate.

## Acceptance Criteria

- [ ] Research entities live in `layer_-1_research/` at the system level
- [ ] Research entities have full stage lifecycle (01-11)
- [ ] Research entities can reference production entities without modifying them
- [ ] Research entities are isolated — failures don't cascade to production

## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
