---
resource_id: "3969da28-3618-446b-8ae1-45c616f7a8ba"
resource_type: "output"
resource_name: "REQ-01_graph_based_validation"
---
# Graph-Based Validation

**Need**: [Chain Validation Enhancement](../README.md)

---

- MUST validate every node in the knowledge graph against the file system
- MUST validate every edge (source and target both exist and are correctly typed)
- MUST report: orphaned nodes, missing nodes, broken edges, type mismatches
