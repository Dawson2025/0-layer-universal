---
resource_id: "0896e767-c62e-47c7-8dca-a3d85802bcb0"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 09: Knowledge Graph

## Purpose

Explicit typed relationships between all system entities — enables structural queries, impact analysis, and dependency visualization.

## Comprehensiveness Level

**Most comprehensive** data-based avenue — captures the entire system topology with explicit relationship types.

## Data Source

- Entity hierarchy (directories with 0AGNOSTIC.md)
- JSON-LD agent definitions (.gab.jsonld)
- Cross-references in 0AGNOSTIC.md (Parent, Children, Inputs, Outputs)
- Skill WHEN conditions (maps skills to entity types)
- Rule scoping (which rules apply where)

## Schema

**Node types**: Entity, Stage, Skill, Rule, Protocol, Knowledge_Doc, Agent_Definition

**Edge types**: CHILD_OF, HAS_STAGE, PRODUCES, DEPENDS_ON, APPLIES_TO, MATCHES, DELEGATES_TO, REFERENCES

## Build Command

```bash
sync-main.sh --avenue 09
# or: build-graph.sh <directory>
```

## Query Interface

SQL adjacency lists in SQLite (portable, zero-server) or PostgreSQL for production.

## Dependencies

- SQLite (zero-server, portable) or PostgreSQL (production)
- jq (for parsing .gab.jsonld)
- awk/grep (for parsing 0AGNOSTIC.md cross-references)

## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

## Design Reference

See `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md` for full schema and implementation plan.
