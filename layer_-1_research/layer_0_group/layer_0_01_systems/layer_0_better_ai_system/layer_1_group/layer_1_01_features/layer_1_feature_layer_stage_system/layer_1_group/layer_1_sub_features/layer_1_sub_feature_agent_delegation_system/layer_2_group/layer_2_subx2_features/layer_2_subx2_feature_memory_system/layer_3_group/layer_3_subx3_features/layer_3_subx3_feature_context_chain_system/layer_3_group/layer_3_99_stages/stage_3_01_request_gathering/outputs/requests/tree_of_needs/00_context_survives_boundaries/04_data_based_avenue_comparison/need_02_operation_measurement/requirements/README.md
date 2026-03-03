# Operation Measurement -- Requirements Index

**Need**: [Operation Measurement](../README.md)

## Overview

These requirements define the comprehensive operation taxonomy and measurement framework. They ensure all database operations (read, write, maintenance, consistency, analytics) are categorized, measured with real units, and support hierarchical aggregation.

## Key Themes

- **Comprehensive Coverage**: 20+ operations across 5 categories
- **Hierarchical Aggregation**: Composite operations computed from components
- **Flat SQL**: Consistent column structure with parent_operation_id for hierarchy

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Operation Taxonomy | Define all operations across 5 categories with hierarchy | [REQ-01_operation_taxonomy.md](./REQ-01_operation_taxonomy.md) |
| REQ-02 | Operation Benchmarks | Measurement units, methodology, and benchmarks for each operation | [REQ-02_operation_benchmarks.md](./REQ-02_operation_benchmarks.md) |
