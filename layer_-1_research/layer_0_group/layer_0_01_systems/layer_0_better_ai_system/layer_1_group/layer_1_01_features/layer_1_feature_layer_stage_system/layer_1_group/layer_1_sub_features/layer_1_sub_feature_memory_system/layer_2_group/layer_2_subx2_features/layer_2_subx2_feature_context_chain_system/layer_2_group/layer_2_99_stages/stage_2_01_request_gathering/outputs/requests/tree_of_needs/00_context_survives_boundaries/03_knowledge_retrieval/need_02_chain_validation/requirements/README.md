---
resource_id: "8e22ed03-8178-4cca-a7ae-3f8039695307"
resource_type: "readme_output"
resource_name: "README"
---
# Chain Validation Enhancement -- Requirements Index

**Need**: [Chain Validation Enhancement](../README.md)

<!-- section_id: "153ac5df-382b-4e8a-9b80-12686038f28f" -->
## Overview

These requirements define how the existing chain-validate skill is upgraded from simple file-existence checks to full graph-based and reference-aware validation. By validating against the knowledge graph, the system can detect orphaned nodes, broken edges, type mismatches, and moved or renamed targets -- not just missing files. The requirements also integrate staleness detection into the validation report, producing a unified health report that covers chain integrity, reference validity, and knowledge freshness in a single pass.

<!-- section_id: "a6d7096e-d4a1-446f-aad2-c5eb087b17a7" -->
## Key Themes

- **Graph-Based Validation**: Every node and edge in the knowledge graph is validated against the file system, reporting orphaned nodes, missing nodes, broken edges, and type mismatches
- **Cross-Tier Reference Checking**: References between knowledge files and stage outputs are validated for existence, correctness, and section-level accuracy, detecting moves, renames, and deletions
- **Unified Health Report**: Staleness detection is integrated into the validation output, producing a single report that covers chain integrity, reference validity, and knowledge freshness together

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Graph-Based Validation | Validate nodes and edges against the file system | [REQ-01_graph_based_validation.md](./REQ-01_graph_based_validation.md) |
| REQ-02 | Reference Validation | Validate cross-tier references between knowledge and stage files | [REQ-02_reference_validation.md](./REQ-02_reference_validation.md) |
| REQ-03 | Staleness Integration | Integrate staleness detection into validation report | [REQ-03_staleness_integration.md](./REQ-03_staleness_integration.md) |
