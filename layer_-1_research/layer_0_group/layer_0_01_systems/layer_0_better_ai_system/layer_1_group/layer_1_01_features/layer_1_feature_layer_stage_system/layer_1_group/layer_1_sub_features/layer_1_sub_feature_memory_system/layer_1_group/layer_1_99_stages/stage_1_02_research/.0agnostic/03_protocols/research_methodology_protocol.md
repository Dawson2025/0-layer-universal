---
resource_id: "589c0384-e23f-4e48-98f7-77e41ec23141"
resource_type: "protocol"
resource_name: "research_methodology_protocol"
---
# Research Methodology Protocol — Memory System Stage 02

<!-- section_id: "ea10c8e1-5d06-4bae-a788-027476d831e3" -->
## Purpose
Defines how research is conducted, organized, and validated for the memory system research stage.

---

<!-- section_id: "3819234c-ebd3-4286-95da-65fd9971ba7f" -->
## 1. Research Process

<!-- section_id: "e73107c3-7744-4e97-b1a1-0157ff130dec" -->
### Phase 1: Survey
- Identify all relevant topics in the problem space
- Create master taxonomy (document 00)
- Map cognitive science foundations

<!-- section_id: "eb6edb05-b4b0-4f56-8a0f-ebfcecdf75ef" -->
### Phase 2: Deep Dive
- One document per topic, numbered sequentially
- Each document covers: what it is, how it works, data structures, implementations, benchmarks
- Cross-reference related documents

<!-- section_id: "0e675559-d6bc-4999-b6bd-a766f7f000f3" -->
### Phase 3: Synthesis
- Create hierarchy documents showing dependency chains
- Identify the minimal core vs optional enhancements
- Produce distilled knowledge summaries for .0agnostic/01_knowledge/

<!-- section_id: "538c3f13-e162-4dfe-b00f-bc0c5b7e9c91" -->
### Phase 4: Handoff
- Write stage report in .0agnostic/05_handoff_documents/
- Identify what next stage (03_instructions) needs
- Flag open items and unresolved questions

---

<!-- section_id: "4df6a4db-f007-4c71-95a6-983fa973f4a0" -->
## 2. Source Requirements

- All claims must be traceable to a source
- Each document must have a Sources section
- Prefer: academic papers (arXiv, PMC), official docs, reputable engineering blogs
- Cite with format: `[Title](URL)` or `[Title](URL) — description`

---

<!-- section_id: "bc581963-cba1-4644-9421-2d20d0298a49" -->
## 3. Quality Criteria

- **Completeness**: Does it cover the full scope of the topic?
- **Accuracy**: Are claims supported by cited sources?
- **Hierarchy clarity**: Are dependency chains and buildup sequences explicit?
- **Actionability**: Can the next stage (instructions) derive requirements from this?
- **Cross-referencing**: Does it link to related documents in the collection?
