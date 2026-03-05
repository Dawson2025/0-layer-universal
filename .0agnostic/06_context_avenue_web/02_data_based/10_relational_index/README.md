---
resource_id: "f865c152-7f8f-4421-b6ed-5e5fe8444142"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 10: Relational Index

<!-- section_id: "81a267d5-3c80-4171-92fd-fd3fffdd6ab2" -->
## Purpose

Structured SQL tables of queryable metadata across all entities — enables dashboards, status queries, and inventory reports.

<!-- section_id: "2c546faf-1727-4f70-8745-6eacc4cb30ca" -->
## Comprehensiveness Level

**High** — broad coverage (every entity gets a row) but flat (no relationship depth).

<!-- section_id: "42588030-c0f8-4cc4-8f68-25a27bfdea6d" -->
## Data Source

- 0AGNOSTIC.md Identity sections (entity name, layer, role, scope, status)
- Stage reports (stage_report.md: status, last_updated, summary, open_items)
- Episodic memory sessions (date, duration, topics, files_changed)
- Skill inventory (name, WHEN conditions, last_used, success_rate)
- Rule inventory (name, importance, scope, trigger_conditions)

<!-- section_id: "a68c94ad-e11a-4515-9674-87c3347e766b" -->
## Schema

```sql
entities (id, name, layer, parent_id, role, scope, status, agnostic_path, last_updated)
stage_reports (id, entity_id, stage_number, stage_name, status, summary, last_updated)
sessions (id, entity_id, session_date, agent_type, topics, files_changed, decisions)
skills (id, name, description, when_conditions, last_used, invocation_count, success_rate)
rules (id, name, importance_level, scope, trigger_conditions, content_hash)
```

<!-- section_id: "342d5cc4-a15f-4a4e-8ffa-2584b155d304" -->
## Build Command

```bash
sync-main.sh --avenue 10
# or: build-index.sh <directory>
```

<!-- section_id: "c6e20f70-d8cc-4180-a115-80e0001a6105" -->
## Query Interface

SQLite for local use, PostgreSQL for multi-agent shared access.

<!-- section_id: "412eec11-fdf3-45e2-8541-ed6934e16657" -->
## Dependencies

- SQLite or PostgreSQL
- awk/grep (for parsing markdown into SQL INSERT statements)

<!-- section_id: "cf391ecb-7717-4ed9-a11a-15ff699fd9ea" -->
## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

<!-- section_id: "bc99fce2-248e-493b-b5c1-8244d9b9822b" -->
## Design Reference

See `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md` for full schema and implementation plan.
