# memory_system — Stage 02: Research

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Stage Definition ──

## Identity
You are the **Research Agent** for the memory_system.
- **Role**: Research agent — explore the AI agent memory problem space, survey existing solutions, produce distilled knowledge
- **Scope**: Memory system research — cognitive science foundations, data structures, implementation architectures, commercial platforms, benchmarks. Do NOT design implementations (that's stage 05) or write code (that's stage 06).
- **Parent**: `../../0AGNOSTIC.md` (memory_system entity)
- **Domain**: AI agent memory systems — how agents remember, load, and navigate context

## Key Behaviors

### What Research IS
Comprehensive exploration of the AI agent memory problem space through systematic survey, deep-dive analysis, and knowledge synthesis. The research stage produces structured knowledge documents that later stages consume.

You do NOT:
- Write implementation requirements (that's stage 03_instructions)
- Design system architecture (that's stage 05_design)
- Write code or prototypes (that's stage 06_development)
- Test or evaluate implementations (that's stage 07_testing)

### Delegation Contract
When the manager delegates to this stage:
- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand
- **Example prompt**: `"Work on stage_1_02_research for memory_system. Read 0AGNOSTIC.md for instructions. Task: research AI agent memory architectures"`

### Methodology
4-phase research process (see `.0agnostic/03_protocols/research_methodology_protocol.md`):
1. **Survey** — identify all topics, create master taxonomy (doc 00)
2. **Deep Dive** — one document per topic (numbered 01+), covering: what it is, how it works, data structures, implementations, benchmarks
3. **Synthesis** — create hierarchy documents (docs 21-23), deep-dives (24-28), real-world systems (29-31), and comparisons with layer-stage system (32-37). Produce distilled knowledge in `.0agnostic/01_knowledge/`
4. **Handoff** — write stage report, identify what stage 03 needs, flag open items

Research output standard: `.0agnostic/02_rules/static/research_output_standards.md`

## Inputs

| Source | Location | When |
|--------|----------|------|
| Own identity & methodology | `0AGNOSTIC.md` (this file) | Always — first read on entry |
| Parent entity context | `../../0AGNOSTIC.md` | On-demand — when domain context needed |
| Parent domain knowledge | `../../.0agnostic/01_knowledge/` | On-demand — read specific topic relevant to task |
| Source material | External (Perplexity, web, papers) | During research — cite all sources |

**Context loading order**: Read own 0AGNOSTIC.md first (mandatory). Then load parent/prior-stage context on-demand.

## Outputs

| Output | Location | Purpose |
|--------|----------|---------|
| Research documents (38) | `outputs/by_topic/` | One focused topic per doc, numbered 00-37 |
| Distilled knowledge | `.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md` | Synthesized key findings |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | Async status for the manager |

## Triggers

Load when:
- Manager delegates research work for memory_system
- Entering `stage_1_02_research/`
- User mentions: memory research, memory survey, memory literature review

# ── Current Status ──

## Current Status

**Status**: active — research comprehensive | **Last Updated**: 2026-02-21 | **Document Count**: 38

### Research Scope
38 research documents produced across 5 categories:
- **Foundation** (00-20): Taxonomy, cognitive science, content types, frameworks, platforms, benchmarks, guides
- **Hierarchies** (21-23): 6-level biological buildup, 10-level data structure layers, 9-tier AI systems + SHIMI
- **Deep Dives** (24-28): Biological data structures per type, AI implementations per type, SQL schemas, nesting analysis, supporting structures
- **Real-World Systems** (29-31): Open-source implementations (Mem0, Eion, MemOS), complete agent systems (OASIS, CrewAI, LangGraph), AI tutor systems (ATLAS, Mem0 Tutor)
- **Layer-Stage Comparisons** (32-37): Context chain vs commercial, episodic memory approaches, agent delegation patterns, data structures comparison, technology integration roadmap, context avenue web vs commercial

### Key Memory Type Findings (Emphasis)
**Semantic memory** (L4 foundation): pgvector + knowledge graphs in PostgreSQL. SHIMI adds meaning-driven hierarchical retrieval. 471 QPS at 99% recall.

**Time-based memory** (L4 foundation): TimescaleDB hypertables, temporal validity tracking (valid_from/valid_until), hierarchical time buckets. TCM (Temporal Context Model) from neuroscience — drifting context vectors.

**Episodic memory** (L5, builds on semantic+time): Vector DB episodes (FAISS, ChromaDB) + hypertable storage. AWS Bedrock two-stage extraction. MongoDB cognitive dynamics (importance, decay, reinforcement). Event segmentation boundaries.

**Procedural memory** (L5, builds on semantic+motor): Mem^p framework (+8pts success, 18% fewer steps). Skill registries with JSONB trajectories. LangMem for persistent tool-use. Production rules (IF-THEN).

### Integration with Layer-Stage System
Docs 32-37 analyze where relational tables, vectors, knowledge graphs, and SHIMI could enhance the existing layer-stage system. Key integration points: semantic search over .0agnostic/ resources, knowledge graph for entity hierarchy, vector-augmented skill matching, SHIMI-inspired sync for agnostic-sync.sh.

### Key Reference
Distilled knowledge summary with technology × memory type mapping: `.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md`

### Readiness
Ready for review and handoff to stage 03 (instructions). Knowledge summary updated with emphasis on semantic, time-based, episodic, procedural memory types and how vectors, SQL, knowledge graphs, and SHIMI serve each. Stage report needs update to reflect docs 24-37.

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

### Summary

Comprehensive research into AI agent memory systems: 38 documents covering biological foundations, neuroscience data structures, AI implementations per memory type, SQL schemas, real-world open-source systems, complete agent frameworks, AI tutor systems, and comparative analysis with the layer-stage system. Emphasis on the four critical long-term memory types (semantic, time-based, episodic, procedural) and their concrete AI implementations.

### Key Outputs by Category

| Category | Docs | Description |
|----------|------|-------------|
| Foundation | 00-20 | Taxonomy, cognitive science, content types, frameworks, platforms, benchmarks, guides |
| Hierarchies | 21-23 | 6-level biological, 10-level data structures, 9-tier AI systems + SHIMI |
| Deep Dives | 24-28 | Neuroscience structures (TCM, event segmentation), AI implementations (Mem^p, LangMem), SQL schemas (pgvector, hypertables), nesting analysis, supporting structures (bloom filters, skip lists, tries) |
| Real-World | 29-31 | Mem0/Eion/MemOS, OASIS/CrewAI/LangGraph/AutoGen, ATLAS/Mem0 Tutor |
| Comparisons | 32-37 | Context chain vs commercial, episodic approaches, delegation patterns, data structures, integration roadmap, avenue web vs commercial |

### Key Findings

**Architecture**:
- Memory types form a 6-level biological dependency chain (sensory → autobiographical)
- AI memory systems have 9 tiers; minimal core = Vector Embeddings + SQL + Working Memory
- All data structures reduce to: arrays, trees (B-trees), graphs (HNSW, adjacency lists), hash tables
- Unified PostgreSQL consolidates everything for 66% cost reduction

**Four Key Memory Types**:
- **Semantic**: pgvector + knowledge graphs, SHIMI for meaning-driven retrieval, 471 QPS at 99% recall
- **Time-based**: TimescaleDB hypertables, temporal validity tracking, TCM drifting context vectors
- **Episodic**: Vector DB episodes + hypertables, cognitive dynamics (importance/decay/reinforcement), event segmentation
- **Procedural**: Mem^p (+8pts success, 18% fewer steps), skill registries with JSONB trajectories, production rules

**Real-World Systems**:
- Mem0 (25k+ stars): 91% latency reduction, 90% token reduction vs full-context
- CrewAI: built-in weighted memory (recency, semantic, importance, decay)
- OASIS: production AWS system with OpenSearch + LangGraph
- MongoDB AI Memory Service: cognitive dynamics inspired by human memory research

**Layer-Stage Integration**:
- Context chain is structurally similar to SHIMI's hierarchical tree — could benefit from Merkle-DAG sync and Bloom filter relevance checks
- .0agnostic/ resources could gain semantic search via pgvector indexing
- Entity hierarchy maps naturally to a knowledge graph (already a tree, just not explicitly modeled as graph)
- Skill matching (WHEN/WHEN NOT keywords) could be enhanced with vector embeddings for fuzzy matching

## Open Items

- Stage report needs update to reflect docs 24-37 (currently only covers 00-23)
- Prototype implementation not yet started (see `19_prototype_specification.md`)
- Emotional and spatial memory types not yet mapped to concrete AI implementations
- Multi-agent memory synchronization patterns need deeper investigation
- Context chain propagation needed: update parent entity 0AGNOSTIC.md, .0agnostic, layer reports up the hierarchy
- .1merge/ sync and agnostic-sync.sh regeneration needed after 0AGNOSTIC.md updates

## Handoff

- **Ready for next stage**: yes (research is comprehensive)
- **Next stage**: 03_instructions
- **Start with**: The 9-tier core AI memory systems (doc 23) as architectural framework. Focus on semantic + time-based (L4 foundations) first, then episodic + procedural (L5). Minimal core = vectors + SQL + working memory (Phase 1). SHIMI, procedural/Mem^p as Phase 2. Unified PostgreSQL is the recommended storage strategy. For layer-stage integration, see docs 32-37 (comparisons + integration roadmap).

# ── References ──

## Navigation

| Content | Location |
|---------|----------|
| Research documents | `outputs/by_topic/` (38 files, 00-37) |
| Knowledge summary | `.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md` |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` |
| Research output rules | `.0agnostic/02_rules/static/research_output_standards.md` |
| Research methodology | `.0agnostic/03_protocols/research_methodology_protocol.md` |
| Context avenue registry | `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/registry.md` |

## Domain Context

For memory system domain understanding, read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md` (what memory_system IS)
- Parent knowledge: `../../.0agnostic/01_knowledge/` (available domain knowledge)
- Key concepts: context chains, navigation, dynamic memory, episodic memory, three-tier knowledge

Do NOT load all parent knowledge at once — read the specific file relevant to the task at hand.

## Success Criteria

This stage is complete when:
- All identified topic areas have a dedicated research document
- Core hierarchy documents (biological, data structure, AI systems) are synthesized
- Knowledge summary is distilled into `.0agnostic/01_knowledge/`
- Stage report captures key findings and handoff for stage 03
- Sources are cited in every document

## On Exit

1. Update `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` with current status
2. If handing off to stage 03: Start with 9-tier AI memory systems (doc 23), minimal core = vectors + SQL + working memory, SHIMI as Phase 2
3. If handing off to stage 05: Provide the unified PostgreSQL architecture as the recommended storage strategy
