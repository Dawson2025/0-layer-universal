---
resource_id: "ad8da56f-9e6f-411e-b0db-43432b7fba98"
resource_type: "output"
resource_name: "REQ-02_instance_inherits_template"
---
# Instance Inherits Template

**Need**: [System Instantiations](../README.md)

---

- MUST base each instance on the system's production template structure
- MUST inherit universal `.0agnostic/` content from parent layers
- SHOULD NOT copy all production content — use the context chain for inheritance
- SHOULD allow instances to override specific template elements when needed
