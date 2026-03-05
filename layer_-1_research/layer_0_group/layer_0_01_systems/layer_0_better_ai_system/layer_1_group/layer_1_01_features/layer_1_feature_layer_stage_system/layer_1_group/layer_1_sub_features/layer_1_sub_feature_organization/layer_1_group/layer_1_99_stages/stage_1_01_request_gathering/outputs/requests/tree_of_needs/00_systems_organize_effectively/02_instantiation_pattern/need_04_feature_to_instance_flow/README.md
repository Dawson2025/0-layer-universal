---
resource_id: "f86831bf-0dcc-4c64-af6c-15dd68285004"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Feature to Instance Flow

**Branch**: [Instantiation Pattern](../README.md)

<!-- section_id: "9763bb04-02a3-45af-adc0-bef3fc9d1674" -->
## Definition

When new features are developed and promoted to production, instances MUST be able to receive those improvements through a controlled update flow.

<!-- section_id: "9093c1c6-25aa-45a7-907d-9c8b27e68857" -->
## Why This Matters

Features evolve the system; instances serve users. The feature-to-instance flow ensures that system improvements reach every personalized instance without breaking existing instance state.

<!-- section_id: "0702f732-23bb-43ac-9602-bc29a7e9c0d6" -->
## Acceptance Criteria

- [ ] Template propagation delivers new features to instance templates
- [ ] Instances can upgrade to incorporate new features
- [ ] Existing instance context is preserved during upgrades
- [ ] Backward compatibility is maintained for instance data

<!-- section_id: "5aa90e85-8b0d-4f1c-8b0f-033e4029cfe1" -->
## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
