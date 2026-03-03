# Operation Taxonomy

**Need**: [Operation Measurement](../README.md)

---

- MUST define 20+ operations across 5 categories (read, write, maintenance, consistency, analytics)
- MUST support hierarchical aggregation via parent_operation_id
- MUST use flat naming (query_point_lookup, insert_bulk) compatible with SQL
- MUST define calculation_rule for composite operations (e.g., "AVG of components")
- MUST include use_case description for each operation
