---
resource_id: "9e4bebc9-5246-4b1b-b469-fd62e33db0b0"
resource_type: "readme
output"
resource_name: "README"
---
# Knowledge Graph -- Requirements Index

**Need**: [Knowledge Graph](../README.md)

<!-- section_id: "b95b8b0b-4470-4b64-98e8-360053dedd42" -->
## Overview

These requirements define how the implicit web of entity relationships scattered across 0AGNOSTIC.md files is formalized into an explicit, machine-readable JSON-LD knowledge graph. The graph must be auto-generated (not manually maintained), use typed nodes and edges that match the layer-stage vocabulary, and be stored in a predictable location where both agents and validation tools can consume it. This enables relationship queries like "what depends on X?" without scanning every file in the hierarchy.

<!-- section_id: "3f10d977-c7f0-41a0-b031-8459c97114e0" -->
## Key Themes

- **Formal Schema**: Node types (feature, stage, knowledge-file, skill, etc.) and edge types (PARENT_OF, DEPENDS_ON, AVENUE_DELIVERS, etc.) are explicitly defined in JSON-LD format, extensible without breaking existing consumers
- **Automated Generation**: The graph is auto-generated from 0AGNOSTIC.md declarations, must be idempotent, and should integrate into the existing agnostic-sync.sh workflow
- **Accessibility**: The graph is stored at a canonical location within .0agnostic/knowledge/ and must be human-readable so agents can query it directly

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Graph Schema | Define node types, edge types, and JSON-LD format | [REQ-01_graph_schema.md](./REQ-01_graph_schema.md) |
| REQ-02 | Graph Generation | Auto-generate from 0AGNOSTIC.md declarations | [REQ-02_graph_generation.md](./REQ-02_graph_generation.md) |
| REQ-03 | Graph Location | Where the graph is stored and readability requirements | [REQ-03_graph_location.md](./REQ-03_graph_location.md) |
