---
resource_id: "18ada08b-f57d-4f45-894d-d5c3ca1eb3df"
resource_type: "output"
resource_name: "REQ-01_graph_schema"
---
# Graph Schema

**Need**: [Knowledge Graph](../README.md)

---

- MUST define node types: feature, sub-feature, stage, knowledge-file, rule, skill, protocol
- MUST define edge types: PARENT_OF, CHILD_OF, CROSS_REFERENCES, DEPENDS_ON, TRIGGERS, AVENUE_DELIVERS, PRECEDES, FOLLOWS, CONTAINS_KNOWLEDGE
- MUST use JSON-LD format (consistent with .gab.jsonld files)
- SHOULD be extensible (new edge/node types without breaking existing graph)
