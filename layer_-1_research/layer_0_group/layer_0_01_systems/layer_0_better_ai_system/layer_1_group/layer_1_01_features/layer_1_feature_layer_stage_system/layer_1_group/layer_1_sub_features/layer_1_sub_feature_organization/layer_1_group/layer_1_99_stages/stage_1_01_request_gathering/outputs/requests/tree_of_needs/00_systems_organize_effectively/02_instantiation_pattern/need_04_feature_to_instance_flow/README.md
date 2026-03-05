---
resource_id: "f86831bf-0dcc-4c64-af6c-15dd68285004"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Feature to Instance Flow

**Branch**: [Instantiation Pattern](../README.md)

## Definition

When new features are developed and promoted to production, instances MUST be able to receive those improvements through a controlled update flow.

## Why This Matters

Features evolve the system; instances serve users. The feature-to-instance flow ensures that system improvements reach every personalized instance without breaking existing instance state.

## Acceptance Criteria

- [ ] Template propagation delivers new features to instance templates
- [ ] Instances can upgrade to incorporate new features
- [ ] Existing instance context is preserved during upgrades
- [ ] Backward compatibility is maintained for instance data

## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
