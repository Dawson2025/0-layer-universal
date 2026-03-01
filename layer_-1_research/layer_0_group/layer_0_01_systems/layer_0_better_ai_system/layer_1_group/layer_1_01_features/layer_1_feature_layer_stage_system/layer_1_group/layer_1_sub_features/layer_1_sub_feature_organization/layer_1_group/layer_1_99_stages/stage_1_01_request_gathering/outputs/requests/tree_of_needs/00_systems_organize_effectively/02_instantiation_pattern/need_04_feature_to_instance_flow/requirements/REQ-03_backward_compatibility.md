# Backward Compatibility

**Need**: [Feature to Instance Flow](../README.md)

---

- SHOULD ensure new template versions don't break existing instance data structures
- SHOULD support migration paths for instance data when template format changes
- MUST NOT delete instance-specific context during template updates
- MAY version the template format to support graceful migration
