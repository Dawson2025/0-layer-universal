---
resource_id: "cdcc7da2-46b8-48fa-84b5-29347dba1b78"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 12: Temporal Index

<!-- section_id: "6bd556b7-2baf-45ef-8ead-f446aea786bd" -->
## Purpose

Time-series views of system activity — enables "what happened this week?", decay/reinforcement, and temporal range queries.

<!-- section_id: "18b2866e-76c3-4157-ab96-c4bb5419916d" -->
## Comprehensiveness Level

**Low** — only models the WHEN dimension, not WHAT or WHY.

<!-- section_id: "5d64b099-debf-4481-afb9-58197ec227c7" -->
## Data Source

- `.0agnostic/04_episodic_memory/` session files (timestamps, topics, changes)
- Stage reports (status transitions with dates)
- Git commit history (file changes over time)
- Skill trajectory stores (invocation timestamps)

<!-- section_id: "efd82eaf-8e8d-4981-b8bc-0e674ee7d78a" -->
## Schema

```sql
events (
  id, entity_path, event_type,
  timestamp TIMESTAMPTZ,
  agent_type, summary, details_json,
  importance FLOAT DEFAULT 0.5,
  decay_factor FLOAT DEFAULT 1.0
)
```

<!-- section_id: "6b34af51-c21b-4085-ac32-2b7bdb99d6e4" -->
## Key Feature: Cognitive Dynamics

- **Decay**: effective_importance = importance x decay_factor^(days_since_event)
- **Reinforcement**: When a session references an old event, its importance increases
- **Consolidation**: Old events with similar topics merge into summary events

<!-- section_id: "7a583ec3-060c-48c6-bedf-970a08d0e840" -->
## Build Command

```bash
sync-main.sh --avenue 12
# or: build-temporal.sh <directory>
```

<!-- section_id: "21ff209e-4c71-4083-9b2e-f2db3368f000" -->
## Query Interface

Temporal range queries, decay-weighted retrieval.

<!-- section_id: "9d554c7f-ecea-43f5-b625-c4d850412597" -->
## Dependencies

- PostgreSQL with TimescaleDB (or regular SQL with timestamp indexes)
- Git (for commit history)

<!-- section_id: "de0eddaf-6b50-4722-af79-a2b178959272" -->
## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

<!-- section_id: "76ab666b-08f1-4c30-90d5-673cee68d531" -->
## Design Reference

See `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md` for full schema and implementation plan.
