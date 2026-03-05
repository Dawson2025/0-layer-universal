---
resource_id: "589c0384-e23f-4e48-98f7-77e41ec23141"
resource_type: "protocol"
resource_name: "research_methodology_protocol"
---
# Research Methodology Protocol — Memory System Stage 02

## Purpose
Defines how research is conducted, organized, and validated for the memory system research stage.

---

## 1. Research Process

### Phase 1: Survey
- Identify all relevant topics in the problem space
- Create master taxonomy (document 00)
- Map cognitive science foundations

### Phase 2: Deep Dive
- One document per topic, numbered sequentially
- Each document covers: what it is, how it works, data structures, implementations, benchmarks
- Cross-reference related documents

### Phase 3: Synthesis
- Create hierarchy documents showing dependency chains
- Identify the minimal core vs optional enhancements
- Produce distilled knowledge summaries for .0agnostic/01_knowledge/

### Phase 4: Handoff
- Write stage report in .0agnostic/05_handoff_documents/
- Identify what next stage (03_instructions) needs
- Flag open items and unresolved questions

---

## 2. Source Requirements

- All claims must be traceable to a source
- Each document must have a Sources section
- Prefer: academic papers (arXiv, PMC), official docs, reputable engineering blogs
- Cite with format: `[Title](URL)` or `[Title](URL) — description`

---

## 3. Quality Criteria

- **Completeness**: Does it cover the full scope of the topic?
- **Accuracy**: Are claims supported by cited sources?
- **Hierarchy clarity**: Are dependency chains and buildup sequences explicit?
- **Actionability**: Can the next stage (instructions) derive requirements from this?
- **Cross-referencing**: Does it link to related documents in the collection?
