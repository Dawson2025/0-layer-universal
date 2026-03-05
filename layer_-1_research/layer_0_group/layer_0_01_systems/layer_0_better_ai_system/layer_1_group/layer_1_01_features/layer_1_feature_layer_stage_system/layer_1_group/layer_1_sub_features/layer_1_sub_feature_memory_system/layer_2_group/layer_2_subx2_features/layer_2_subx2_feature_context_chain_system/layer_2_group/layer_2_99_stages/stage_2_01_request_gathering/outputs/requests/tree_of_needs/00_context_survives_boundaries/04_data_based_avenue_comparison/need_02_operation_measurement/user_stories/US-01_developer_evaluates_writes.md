---
resource_id: "895c946d-eecb-4984-a798-15086b99ea82"
resource_type: "output"
resource_name: "US-01_developer_evaluates_writes"
---
# US-01: Developer evaluates write performance

**Need**: [Operation Measurement](../README.md)

---

**As a** developer building a write-heavy application,
**I want** to compare write operation benchmarks (single insert, bulk insert, update, delete) across avenues,
**So that** I can choose the avenue that handles my write workload best.

<!-- section_id: "aaeb511b-b9cb-434e-a0d6-313ba29e4df4" -->
### What Happens

1. Developer queries operation benchmarks filtered by write category
2. System returns all write operations with raw speeds and normalized scores per avenue
3. Developer sees aggregate write speed (composite of components) alongside individual operations
4. Developer identifies which avenue handles their specific write pattern best

<!-- section_id: "a69932e9-2636-4999-a8ab-502a7cf9c202" -->
### Acceptance Criteria

- Write operations are broken down into sub-operations (single, bulk)
- Aggregate write score combines sub-operation scores via calculation_rule
- Results include raw units (ms, ops/sec) alongside normalized scores
