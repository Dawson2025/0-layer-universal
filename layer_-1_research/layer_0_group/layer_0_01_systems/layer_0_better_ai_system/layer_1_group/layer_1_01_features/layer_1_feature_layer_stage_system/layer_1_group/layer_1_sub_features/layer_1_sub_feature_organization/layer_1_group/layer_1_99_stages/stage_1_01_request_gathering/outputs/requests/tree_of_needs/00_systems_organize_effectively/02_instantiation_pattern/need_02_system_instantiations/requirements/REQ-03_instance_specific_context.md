---
resource_id: "4950d453-30e4-4644-94a0-5e74b503cf97"
resource_type: "output"
resource_name: "REQ-03_instance_specific_context"
---
# Instance-Specific Context

**Need**: [System Instantiations](../README.md)

---

- MUST allow each instance to store user-specific data in its own `.0agnostic/` or outputs/
- MUST NOT modify shared (parent) content when storing instance-specific data
- SHOULD support user profiles, progress tracking, and adaptation state
- SHOULD use the entity's `0AGNOSTIC.md` Current Status for instance-level state
