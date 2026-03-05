---
resource_id: "cdcc7da2-46b8-48fa-84b5-29347dba1b78"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 12: Temporal Index

## Purpose

Time-series views of system activity — enables "what happened this week?", decay/reinforcement, and temporal range queries.

## Comprehensiveness Level

**Low** — only models the WHEN dimension, not WHAT or WHY.

## Data Source

- `.0agnostic/04_episodic_memory/` session files (timestamps, topics, changes)
- Stage reports (status transitions with dates)
- Git commit history (file changes over time)
- Skill trajectory stores (invocation timestamps)

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

## Key Feature: Cognitive Dynamics

- **Decay**: effective_importance = importance x decay_factor^(days_since_event)
- **Reinforcement**: When a session references an old event, its importance increases
- **Consolidation**: Old events with similar topics merge into summary events

## Build Command

```bash
sync-main.sh --avenue 12
# or: build-temporal.sh <directory>
```

## Query Interface

Temporal range queries, decay-weighted retrieval.

## Dependencies

- PostgreSQL with TimescaleDB (or regular SQL with timestamp indexes)
- Git (for commit history)

## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

## Design Reference

See `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md` for full schema and implementation plan.
