---
resource_id: "c9912856-871c-4860-8c72-5c25610e3aeb"
resource_type: "readme
output"
resource_name: "README"
---
# Root Need: Context Survives Boundaries

**The fundamental goal all context chain requirements derive from.**

---

<!-- section_id: "5b93fefe-12eb-4ff9-92eb-9d16c484a0f9" -->
## Definition

> Agents never lose competence when crossing session boundaries, compaction events, or tool switches. Context is always recoverable without re-reading everything.

---

<!-- section_id: "b1c71607-e250-4a84-967e-30ad4f526ee4" -->
## The Problem

Current AI agent sessions are fragile:
- Agents lose all understanding after compaction
- New sessions start with no memory of prior work
- Re-reading all stage outputs to regain competence blows the context window
- No clear rule for what goes in static context vs on-demand knowledge vs detailed outputs
- Knowledge files and stage outputs drift apart with no detection
- Context loading is manual — agents guess which files to read

---

<!-- section_id: "63de06cb-f9b7-44f1-9203-163d2ced1e30" -->
## The Vision

A system where:
- An agent reads ~260 lines of distilled knowledge and is competent (not 5,000 lines of raw research)
- Knowledge is tiered: pointers → summaries → full content, each loaded only when needed
- Entity relationships are formalized as a graph, enabling smart traversal
- Consolidation happens at stage boundaries — raw findings become distilled knowledge
- Stale knowledge is detected and flagged automatically
- Context loading is scored, not guessed

---

<!-- section_id: "c4b63936-1580-428c-8904-91c3315d452b" -->
## Four Branches

| Branch | Question | Description |
|--------|----------|-------------|
| [**01_knowledge_organization**](./01_knowledge_organization/) | "Where does each kind of content live?" | Three-tier architecture, knowledge graphs, reference standards |
| [**02_knowledge_lifecycle**](./02_knowledge_lifecycle/) | "How does knowledge move and stay current?" | Consolidation at stage boundaries, staleness detection |
| [**03_knowledge_retrieval**](./03_knowledge_retrieval/) | "How do agents find the right context?" | Scored retrieval, graph-based chain validation |
| [**04_data_based_avenue_comparison**](./04_data_based_avenue_comparison/) | "Which avenue delivers context best?" | Measurable benchmarks, operation taxonomy, project-specific weighting |

---

<!-- section_id: "b92bdc76-7a51-4044-b266-6ae0fe273014" -->
## Branch Structure

```
00_context_survives_boundaries/           (this folder - the root)
│
├── 01_knowledge_organization/            Where content lives
│   ├── need_01_three_tier_architecture   Pointer → distilled → full pattern
│   ├── need_02_knowledge_graph           Formalize entity relationships as JSON-LD
│   └── need_03_reference_format          Standard for cross-tier references
│
├── 02_knowledge_lifecycle/               How knowledge moves and stays current
│   ├── need_01_consolidation_process     Distill stage outputs → knowledge files
│   └── need_02_staleness_detection       Detect when knowledge drifts from source
│
├── 03_knowledge_retrieval/               How agents find the right context
│   ├── need_01_scored_retrieval          Rank context by recency × relevance × importance
│   ├── need_02_chain_validation          Validate chain integrity against the KG
│   └── need_03_auto_discovery            Auto-discover update protocols and propagation chain
│
└── 04_data_based_avenue_comparison/      Which avenue delivers context best
    ├── need_01_avenue_benchmarking       Measurable capabilities with real units
    ├── need_02_operation_measurement     Comprehensive operation taxonomy with benchmarks
    └── need_03_customizable_importance   Project-specific importance weighting + decision matrix
```

---

<!-- section_id: "f8f32664-ca89-40f6-b643-8ccc9558983f" -->
## Success Criteria

The root need is satisfied when:
- [ ] Agent can recover full competence after compaction by reading distilled knowledge (~5 min, not ~30 min)
- [ ] Three tiers are clearly defined and enforced (pointers / distilled / full)
- [ ] Knowledge graph represents all entity relationships as JSON-LD
- [ ] Consolidation runs at stage boundaries, producing distilled knowledge files
- [ ] Stale knowledge files are detected and flagged
- [ ] Context loading uses scored retrieval, not manual file selection
- [ ] Chain validation checks typed relationships, not just file existence

---

<!-- section_id: "86cc4a5b-4c97-4d8c-9e1c-8cc1d736e291" -->
## Research Grounding

All needs trace to `memory_system/stage_1_02_research/outputs/by_topic/`:
- Files 00-14: AI memory system landscape
- File 15: Vectors, knowledge graphs, and neurology
- File 18: Underlying data structures (16 types)
- File 19: Prototype specification
- File 20: Three-tier knowledge architecture
