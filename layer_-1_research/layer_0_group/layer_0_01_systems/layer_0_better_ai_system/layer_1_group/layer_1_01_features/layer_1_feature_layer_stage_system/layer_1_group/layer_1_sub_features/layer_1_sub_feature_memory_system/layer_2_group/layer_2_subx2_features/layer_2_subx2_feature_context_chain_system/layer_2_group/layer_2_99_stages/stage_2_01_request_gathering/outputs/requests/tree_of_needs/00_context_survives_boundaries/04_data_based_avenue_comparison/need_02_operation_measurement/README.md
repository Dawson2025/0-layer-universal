---
resource_id: "3edb2f14-b386-40f5-beb4-48d1f18438fd"
resource_type: "readme_output"
resource_name: "README"
---
# Need: Comprehensive Operation Measurement

**Branch**: [04_data_based_avenue_comparison](../)
**Question**: "How do we measure what each avenue can DO across all operation types?"
**Version**: 1.0.0

---

<!-- section_id: "a7060f68-f4fa-49ab-9769-9c6db5410c01" -->
## Definition

A comprehensive taxonomy of database operations (20+) covering read, write, maintenance, consistency, and analytics categories. Each operation must have:
- Performance benchmarks with real units
- Hierarchical aggregation (component operations roll up to aggregate operations)
- Quality metrics beyond raw speed

Operations include: point lookup, range query, fuzzy search, semantic search, full-text search, graph traversal, single/bulk insert/update/delete, index operations, transactions, replication, aggregation, joins, and grouping.

---

<!-- section_id: "5991f48f-edb2-44df-ac4b-52d1e1cb70f9" -->
## Why This Matters

- Avenue selection depends on what operations the project actually needs
- Overall query speed is a composite of retrieval speed + read speed -- both must be measured
- Some avenues excel at reads but struggle with writes (or vice versa)
- Maintenance operations (index rebuild, schema migration) affect total cost of ownership
- Consistency operations (transactions, rollback) are critical for some projects and irrelevant for others

---

<!-- section_id: "52fbb795-7661-455f-9715-165b2a9eaaa3" -->
## Acceptance Criteria

- [ ] 20+ operations are defined across 5 categories (read, write, maintenance, consistency, analytics)
- [ ] Each operation has measurement units, methodology, and benchmarks
- [ ] Hierarchical aggregation works (aggregate operations computed from components)
- [ ] Flat SQL structure maintains consistent columns while encoding hierarchy via parent_operation_id
- [ ] Operation quality metrics are tracked alongside speed metrics

---

<!-- section_id: "cfb1c918-2760-49bb-86a0-8db43b82e1ee" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

<!-- section_id: "80cb4b61-2853-440d-95cf-3cf766b3ae13" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "0c7a4161-975b-4f20-bd73-1d6b851ca76b" -->
## Research References

- `proposals/04_design/v2_hierarchical_aggregation_design.md` -- hierarchy design
- `proposals/04_design/v5_comprehensive_operations_with_customizable_importance.md` -- full operation taxonomy
- `proposals/04_design/v6_consolidated_schema_with_improvements.md` -- unified schema
