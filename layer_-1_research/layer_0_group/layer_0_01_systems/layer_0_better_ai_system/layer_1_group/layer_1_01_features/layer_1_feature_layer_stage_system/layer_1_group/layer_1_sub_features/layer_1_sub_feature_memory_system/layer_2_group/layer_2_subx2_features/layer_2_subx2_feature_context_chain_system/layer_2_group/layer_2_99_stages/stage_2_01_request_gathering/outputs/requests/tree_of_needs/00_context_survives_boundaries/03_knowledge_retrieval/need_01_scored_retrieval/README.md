---
resource_id: "64ebf8e7-9a53-4e45-8ee6-414050b74248"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Scored Context Retrieval

**Branch**: [03_knowledge_retrieval](../)
**Question**: "Which context is most relevant for the current task?"
**Version**: 1.0.0

---

## Definition

Replace manual file selection ("read this file") with scored retrieval that ranks available context by a composite of recency, relevance, and importance. Agents load the top-scoring context instead of guessing.

---

## Why This Matters

- Currently agents follow explicit pointers or guess which files to read
- An agent entering "memory_system" doesn't know whether to read the research files, the design files, or the knowledge files first
- Scored retrieval means the most relevant content surfaces automatically

---

## Acceptance Criteria

- [ ] Scoring function is defined and documented
- [ ] At least one entity's files have metadata enrichment
- [ ] Retrieval returns ranked list of files for a given query/context
- [ ] Top-scored files are demonstrably more relevant than random selection

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Research References

- `memory_system/stage_1_02_research/outputs/by_topic/18_underlying_data_structures.md` — Data structure #13 (scored list)
- `memory_system/stage_1_02_research/outputs/by_topic/13_practitioners_complete_guide.md` — Retrieval strategies
