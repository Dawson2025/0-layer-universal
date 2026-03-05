---
resource_id: "f865c152-7f8f-4421-b6ed-5e5fe8444142"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 10: Relational Index

## Purpose

Structured SQL tables of queryable metadata across all entities — enables dashboards, status queries, and inventory reports.

## Comprehensiveness Level

**High** — broad coverage (every entity gets a row) but flat (no relationship depth).

## Data Source

- 0AGNOSTIC.md Identity sections (entity name, layer, role, scope, status)
- Stage reports (stage_report.md: status, last_updated, summary, open_items)
- Episodic memory sessions (date, duration, topics, files_changed)
- Skill inventory (name, WHEN conditions, last_used, success_rate)
- Rule inventory (name, importance, scope, trigger_conditions)

## Schema

```sql
entities (id, name, layer, parent_id, role, scope, status, agnostic_path, last_updated)
stage_reports (id, entity_id, stage_number, stage_name, status, summary, last_updated)
sessions (id, entity_id, session_date, agent_type, topics, files_changed, decisions)
skills (id, name, description, when_conditions, last_used, invocation_count, success_rate)
rules (id, name, importance_level, scope, trigger_conditions, content_hash)
```

## Build Command

```bash
sync-main.sh --avenue 10
# or: build-index.sh <directory>
```

## Query Interface

SQLite for local use, PostgreSQL for multi-agent shared access.

## Dependencies

- SQLite or PostgreSQL
- awk/grep (for parsing markdown into SQL INSERT statements)

## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

## Design Reference

See `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md` for full schema and implementation plan.
