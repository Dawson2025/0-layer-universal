---
resource_id: "0896e767-c62e-47c7-8dca-a3d85802bcb0"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 09: Knowledge Graph

<!-- section_id: "0ffce44e-9ff9-4122-9222-34abb85aae0d" -->
## Purpose

Explicit typed relationships between all system entities — enables structural queries, impact analysis, and dependency visualization.

<!-- section_id: "17760c1d-34d6-43ad-b713-96ad2d485389" -->
## Comprehensiveness Level

**Most comprehensive** data-based avenue — captures the entire system topology with explicit relationship types.

<!-- section_id: "e7ef21c1-a2a0-4f9b-855f-6de982f505b4" -->
## Data Source

- Entity hierarchy (directories with 0AGNOSTIC.md)
- JSON-LD agent definitions (.gab.jsonld)
- Cross-references in 0AGNOSTIC.md (Parent, Children, Inputs, Outputs)
- Skill WHEN conditions (maps skills to entity types)
- Rule scoping (which rules apply where)

<!-- section_id: "56a93fe0-27e4-49dc-aca7-9cde5d077293" -->
## Schema

**Node types**: Entity, Stage, Skill, Rule, Protocol, Knowledge_Doc, Agent_Definition

**Edge types**: CHILD_OF, HAS_STAGE, PRODUCES, DEPENDS_ON, APPLIES_TO, MATCHES, DELEGATES_TO, REFERENCES

<!-- section_id: "87881e97-9c23-49db-8358-f693529337c5" -->
## Build Command

```bash
sync-main.sh --avenue 09
# or: build-graph.sh <directory>
```

<!-- section_id: "cd271624-04b5-4e37-b2dc-6a779f8732e2" -->
## Query Interface

SQL adjacency lists in SQLite (portable, zero-server) or PostgreSQL for production.

<!-- section_id: "390badb5-499b-4c5e-8d6d-2b9efdda99a3" -->
## Dependencies

- SQLite (zero-server, portable) or PostgreSQL (production)
- jq (for parsing .gab.jsonld)
- awk/grep (for parsing 0AGNOSTIC.md cross-references)

<!-- section_id: "81a586b7-4109-47fc-a214-05247c8184a6" -->
## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

<!-- section_id: "181fe939-eeaf-464a-938c-a9688dd965a6" -->
## Design Reference

See `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md` for full schema and implementation plan.
