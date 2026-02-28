# Need: System Features

**Branch**: [Instantiation Pattern](../README.md)

## Definition

A system MUST organize its capabilities as features, each with its own research lifecycle and stage progression.

## Why This Matters

Features represent the R&D side of a system. Each feature is a capability being developed — it has its own requirements, research, design, and implementation stages. This structured approach prevents feature sprawl and ensures each capability is thoroughly developed.

## Acceptance Criteria

- [ ] Each feature is a separate entity with its own layer-stage hierarchy
- [ ] Features have full stage lifecycle (stages 01-11)
- [ ] Features are isolated from each other — one feature's changes don't break another
- [ ] Features can have sub-features for finer granularity

## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
