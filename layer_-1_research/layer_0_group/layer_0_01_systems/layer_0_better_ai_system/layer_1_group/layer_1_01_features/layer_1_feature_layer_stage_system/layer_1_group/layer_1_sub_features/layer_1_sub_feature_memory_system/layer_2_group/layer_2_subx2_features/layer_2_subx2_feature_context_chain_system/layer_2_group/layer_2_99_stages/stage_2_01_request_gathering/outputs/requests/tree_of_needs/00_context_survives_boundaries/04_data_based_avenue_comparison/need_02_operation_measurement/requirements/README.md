---
resource_id: "47d9393e-2d51-4696-bfd8-89af4dcdc943"
resource_type: "readme_output"
resource_name: "README"
---
# Operation Measurement -- Requirements Index

**Need**: [Operation Measurement](../README.md)

<!-- section_id: "b6418d56-ff14-4364-9135-981c25a06c1e" -->
## Overview

These requirements define the comprehensive operation taxonomy and measurement framework. They ensure all database operations (read, write, maintenance, consistency, analytics) are categorized, measured with real units, and support hierarchical aggregation.

<!-- section_id: "bfe0e989-7868-4406-af42-bfc2ccd6ead0" -->
## Key Themes

- **Comprehensive Coverage**: 20+ operations across 5 categories
- **Hierarchical Aggregation**: Composite operations computed from components
- **Flat SQL**: Consistent column structure with parent_operation_id for hierarchy

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Operation Taxonomy | Define all operations across 5 categories with hierarchy | [REQ-01_operation_taxonomy.md](./REQ-01_operation_taxonomy.md) |
| REQ-02 | Operation Benchmarks | Measurement units, methodology, and benchmarks for each operation | [REQ-02_operation_benchmarks.md](./REQ-02_operation_benchmarks.md) |
