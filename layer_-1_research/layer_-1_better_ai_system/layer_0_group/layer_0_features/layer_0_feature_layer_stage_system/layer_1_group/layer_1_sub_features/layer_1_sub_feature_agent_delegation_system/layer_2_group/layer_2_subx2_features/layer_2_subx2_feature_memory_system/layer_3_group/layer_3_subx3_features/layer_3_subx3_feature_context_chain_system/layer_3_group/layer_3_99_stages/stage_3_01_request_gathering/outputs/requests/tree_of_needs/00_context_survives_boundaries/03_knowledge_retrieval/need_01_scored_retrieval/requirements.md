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

## Requirements

### Scoring Function
- MUST define composite score: recency × relevance × importance (weights tunable)
- MUST support scoring across tiers (knowledge files, stage outputs, episodic notes)
- SHOULD use metadata embedded in files (frontmatter, headers, or companion metadata files)

### Metadata Enrichment
- MUST define what metadata each file needs (creation date, last modified, importance, tags)
- SHOULD use YAML frontmatter in markdown files
- SHOULD be backward-compatible (files without metadata still work, just scored lower)

### Integration
- SHOULD integrate into context loading decisions (agent reads top-K scored files)
- SHOULD be queryable ("what's most relevant for task X?")

---

## Acceptance Criteria

- [ ] Scoring function is defined and documented
- [ ] At least one entity's files have metadata enrichment
- [ ] Retrieval returns ranked list of files for a given query/context
- [ ] Top-scored files are demonstrably more relevant than random selection

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- `memory_system/stage_2_02_research/outputs/by_topic/18_underlying_data_structures.md` — Data structure #13 (scored list)
- `memory_system/stage_2_02_research/outputs/by_topic/13_practitioners_complete_guide.md` — Retrieval strategies
