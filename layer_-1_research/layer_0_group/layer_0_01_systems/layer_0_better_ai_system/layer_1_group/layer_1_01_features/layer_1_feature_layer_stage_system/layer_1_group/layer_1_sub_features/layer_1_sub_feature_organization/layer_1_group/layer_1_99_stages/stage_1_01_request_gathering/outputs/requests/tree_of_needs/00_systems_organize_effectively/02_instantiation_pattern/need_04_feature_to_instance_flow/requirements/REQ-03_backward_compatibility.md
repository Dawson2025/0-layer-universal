---
resource_id: "0355ef42-9e07-4de7-8e23-6999168d39f9"
resource_type: "output"
resource_name: "REQ-03_backward_compatibility"
---
# Backward Compatibility

**Need**: [Feature to Instance Flow](../README.md)

---

- SHOULD ensure new template versions don't break existing instance data structures
- SHOULD support migration paths for instance data when template format changes
- MUST NOT delete instance-specific context during template updates
- MAY version the template format to support graceful migration
