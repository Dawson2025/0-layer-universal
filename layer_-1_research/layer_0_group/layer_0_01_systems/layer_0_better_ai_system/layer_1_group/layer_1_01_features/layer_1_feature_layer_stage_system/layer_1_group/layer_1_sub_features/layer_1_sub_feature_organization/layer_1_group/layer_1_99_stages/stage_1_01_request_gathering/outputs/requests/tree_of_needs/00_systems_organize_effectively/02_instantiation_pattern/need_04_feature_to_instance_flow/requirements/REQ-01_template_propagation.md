---
resource_id: "5cba63b0-e50a-4538-bdae-30baf987870d"
resource_type: "output"
resource_name: "REQ-01_template_propagation"
---
# Template Propagation

**Need**: [Feature to Instance Flow](../README.md)

---

- MUST update production templates when features are promoted
- MUST ensure new instances automatically get the latest template
- SHOULD use context chain inheritance rather than copying template content
- SHOULD document what changed in the template update
