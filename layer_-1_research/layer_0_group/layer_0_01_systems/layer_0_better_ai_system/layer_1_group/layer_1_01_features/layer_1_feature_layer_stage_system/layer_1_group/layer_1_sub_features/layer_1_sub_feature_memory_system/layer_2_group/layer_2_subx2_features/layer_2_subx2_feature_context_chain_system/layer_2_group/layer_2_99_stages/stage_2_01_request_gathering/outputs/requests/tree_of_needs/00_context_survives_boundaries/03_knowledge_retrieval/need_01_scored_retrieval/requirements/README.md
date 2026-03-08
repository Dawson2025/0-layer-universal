---
resource_id: "645cf795-ec75-4419-8124-e29a5e509a04"
resource_type: "readme_output"
resource_name: "README"
---
# Scored Context Retrieval -- Requirements Index

**Need**: [Scored Context Retrieval](../README.md)

<!-- section_id: "d6f8b7f8-caa1-4449-9e63-bb13655227be" -->
## Overview

These requirements define how agents move from manual file selection ("read this file") to scored retrieval that automatically ranks available context by a composite of recency, relevance, and importance. They cover the scoring function definition with tunable weights, the metadata enrichment that files need to be scoreable, and how scored retrieval integrates into context loading decisions so agents read the top-K most relevant files instead of guessing.

<!-- section_id: "93d41651-7ab3-49ff-a0b8-90ad8e936895" -->
## Key Themes

- **Composite Scoring**: A tunable scoring function combines recency, relevance, and importance to rank files across all tiers -- knowledge files, stage outputs, and episodic notes alike
- **Metadata Enrichment**: Files require structured metadata (creation date, last modified, importance, tags) via YAML frontmatter, with backward compatibility so un-enriched files still work at lower scores
- **Context Loading Integration**: Scored retrieval feeds directly into agent context loading, making it queryable ("what's most relevant for task X?") and actionable (agent reads top-K results)

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Scoring Function | Composite score definition with tunable weights | [REQ-01_scoring_function.md](./REQ-01_scoring_function.md) |
| REQ-02 | Metadata Enrichment | File metadata requirements for scoring | [REQ-02_metadata_enrichment.md](./REQ-02_metadata_enrichment.md) |
| REQ-03 | Integration | How scored retrieval integrates with context loading | [REQ-03_integration.md](./REQ-03_integration.md) |
