---
resource_id: "42c00d7b-24cf-4892-b675-b8ccb8899771"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 11: Vector Embeddings

## Purpose

Semantic similarity search across all text content — enables "find everything about X" queries without knowing file paths.

## Comprehensiveness Level

**Medium** — broad coverage (all text content) but lossy (reduces to similarity scores).

## Data Source

- All `.0agnostic/01_knowledge/` documents
- All 0AGNOSTIC.md sections (STATIC content)
- Skill SKILL.md descriptions
- Research documents in `outputs/by_topic/`
- Stage reports
- Episodic memory session files

## Schema

```sql
content_embeddings (
  id, source_path, source_section, chunk_text,
  embedding vector(1536),
  avenue_type,
  entity_path,
  last_updated
)
```

## Key Feature: Avenue-Weighted Search

Results weighted by source avenue comprehensiveness:
```
effective_score = cosine_similarity x avenue_weight
Avenue weights: 01=1.0, 02=0.9, 03=0.8, ..., 08=0.3
```

## Build Command

```bash
sync-main.sh --avenue 11
# or: build-embeddings.sh <directory>
```

## Query Interface

Semantic search CLI + integration into context-gathering skill.

## Dependencies

- PostgreSQL with pgvector extension
- Embedding API (OpenAI, local model, etc.)
- Python (for embedding pipeline)

## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

## Design Reference

See `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md` for full schema and implementation plan.
