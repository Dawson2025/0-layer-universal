---
resource_id: "cfe0ce85-c8b5-43a5-98da-7d72f718fd89"
resource_type: "output"
resource_name: "REQ-01_systems_contain_subsystems"
---
# Systems Contain Sub-Systems

**Need**: [Nested Systems](../README.md)

---

- MUST allow entities to contain child entities (sub-systems)
- MUST use the layer hierarchy for nesting (e.g., layer_0 contains layer_1, layer_1 contains layer_2)
- MUST give each sub-system its own `0AGNOSTIC.md` and `.0agnostic/`
- SHOULD support arbitrary nesting depth
