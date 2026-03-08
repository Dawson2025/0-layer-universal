---
resource_id: "42c00d7b-24cf-4892-b675-b8ccb8899771"
resource_type: "readme_document"
resource_name: "README"
---
# Avenue 11: Vector Embeddings

<!-- section_id: "511eb093-22d6-4505-9e60-ba13b16bd5c3" -->
## Purpose

Semantic similarity search across all text content — enables "find everything about X" queries without knowing file paths.

<!-- section_id: "eb0c2afa-e9b3-4ef6-aca7-915e2b4efd6b" -->
## Comprehensiveness Level

**Medium** — broad coverage (all text content) but lossy (reduces to similarity scores).

<!-- section_id: "b9f3473b-8cc2-49b2-87ef-014be51b95cc" -->
## Data Source

- All `.0agnostic/01_knowledge/` documents
- All 0AGNOSTIC.md sections (STATIC content)
- Skill SKILL.md descriptions
- Research documents in `outputs/by_topic/`
- Stage reports
- Episodic memory session files

<!-- section_id: "c4bfbeed-122b-4fa0-97a8-307367990922" -->
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

<!-- section_id: "771e2ca7-a0ff-4d9f-851c-af2e32fcb537" -->
## Key Feature: Avenue-Weighted Search

Results weighted by source avenue comprehensiveness:
```
effective_score = cosine_similarity x avenue_weight
Avenue weights: 01=1.0, 02=0.9, 03=0.8, ..., 08=0.3
```

<!-- section_id: "f247ed9d-48ab-47ea-a7c7-7e1ac538f38b" -->
## Build Command

```bash
sync-main.sh --avenue 11
# or: build-embeddings.sh <directory>
```

<!-- section_id: "459edf9c-0714-4d60-947e-cc129d619828" -->
## Query Interface

Semantic search CLI + integration into context-gathering skill.

<!-- section_id: "0d5df08a-ebb5-4ede-b43a-fe8464a1e777" -->
## Dependencies

- PostgreSQL with pgvector extension
- Embedding API (OpenAI, local model, etc.)
- Python (for embedding pipeline)

<!-- section_id: "7d56b122-3cff-4747-87c2-21847b1f3768" -->
## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

<!-- section_id: "4d5305aa-4afd-4210-bf2b-39438e7b72fd" -->
## Design Reference

See `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md` for full schema and implementation plan.
