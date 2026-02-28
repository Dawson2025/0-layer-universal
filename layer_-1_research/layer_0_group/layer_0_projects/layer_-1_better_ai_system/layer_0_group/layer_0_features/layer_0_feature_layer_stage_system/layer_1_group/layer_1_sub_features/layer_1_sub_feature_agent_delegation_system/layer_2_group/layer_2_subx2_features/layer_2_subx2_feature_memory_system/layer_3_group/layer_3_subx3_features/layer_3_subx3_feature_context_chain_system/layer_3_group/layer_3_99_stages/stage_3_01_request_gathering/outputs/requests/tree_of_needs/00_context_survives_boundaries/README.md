# Root Need: Context Survives Boundaries

**The fundamental goal all context chain requirements derive from.**

---

## Definition

> Agents never lose competence when crossing session boundaries, compaction events, or tool switches. Context is always recoverable without re-reading everything.

---

## The Problem

Current AI agent sessions are fragile:
- Agents lose all understanding after compaction
- New sessions start with no memory of prior work
- Re-reading all stage outputs to regain competence blows the context window
- No clear rule for what goes in static context vs on-demand knowledge vs detailed outputs
- Knowledge files and stage outputs drift apart with no detection
- Context loading is manual — agents guess which files to read

---

## The Vision

A system where:
- An agent reads ~260 lines of distilled knowledge and is competent (not 5,000 lines of raw research)
- Knowledge is tiered: pointers → summaries → full content, each loaded only when needed
- Entity relationships are formalized as a graph, enabling smart traversal
- Consolidation happens at stage boundaries — raw findings become distilled knowledge
- Stale knowledge is detected and flagged automatically
- Context loading is scored, not guessed

---

## Three Branches

| Branch | Question | Description |
|--------|----------|-------------|
| [**01_knowledge_organization**](./01_knowledge_organization/) | "Where does each kind of content live?" | Three-tier architecture, knowledge graphs, reference standards |
| [**02_knowledge_lifecycle**](./02_knowledge_lifecycle/) | "How does knowledge move and stay current?" | Consolidation at stage boundaries, staleness detection |
| [**03_knowledge_retrieval**](./03_knowledge_retrieval/) | "How do agents find the right context?" | Scored retrieval, graph-based chain validation |

---

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
└── 03_knowledge_retrieval/               How agents find the right context
    ├── need_01_scored_retrieval          Rank context by recency × relevance × importance
    ├── need_02_chain_validation          Validate chain integrity against the KG
    └── need_03_auto_discovery            Auto-discover update protocols and propagation chain
```

---

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

## Research Grounding

All needs trace to `memory_system/stage_2_02_research/outputs/by_topic/`:
- Files 00-14: AI memory system landscape
- File 15: Vectors, knowledge graphs, and neurology
- File 18: Underlying data structures (16 types)
- File 19: Prototype specification
- File 20: Three-tier knowledge architecture
