# Graph Schema

**Need**: [Knowledge Graph](../README.md)

---

- MUST define node types: feature, sub-feature, stage, knowledge-file, rule, skill, protocol
- MUST define edge types: PARENT_OF, CHILD_OF, CROSS_REFERENCES, DEPENDS_ON, TRIGGERS, AVENUE_DELIVERS, PRECEDES, FOLLOWS, CONTAINS_KNOWLEDGE
- MUST use JSON-LD format (consistent with .gab.jsonld files)
- SHOULD be extensible (new edge/node types without breaking existing graph)
