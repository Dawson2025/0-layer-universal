---
resource_id: "b07e2881-e9c1-4b70-9b40-d71b7dfa8215"
resource_type: "output"
resource_name: "REQ-01_context_model_definition"
---
# Context Model Definition

**Need**: [Agent Context Model](../README.md)

---

- MUST define the context model for three agent types: manager, stage agent, sub-feature agent
- MUST specify for each type: what is in static context (always loaded via context chain)
- MUST specify for each type: what is in dynamic context (loaded on demand when needed)
- MUST specify for each type: what is never loaded (out of scope)
