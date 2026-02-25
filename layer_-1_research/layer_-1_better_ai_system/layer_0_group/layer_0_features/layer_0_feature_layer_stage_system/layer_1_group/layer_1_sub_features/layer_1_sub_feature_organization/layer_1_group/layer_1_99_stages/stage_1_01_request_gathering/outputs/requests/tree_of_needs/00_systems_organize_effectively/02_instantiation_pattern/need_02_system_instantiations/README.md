# Need: System Instantiations

**Branch**: [Instantiation Pattern](../README.md)

## Definition

A system MUST support creating per-user or per-context instances that inherit from the system's production template while maintaining instance-specific state.

## Why This Matters

A system built for multiple users (students, teams, projects) needs personalized instances. Each instance inherits the system's proven patterns but adds user-specific context, progress, and adaptations.

## Acceptance Criteria

- [ ] Each instance is a child entity of the system
- [ ] Instances inherit from the production template structure
- [ ] Instances can store user-specific context without modifying the template
- [ ] Multiple instances can coexist independently

## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
