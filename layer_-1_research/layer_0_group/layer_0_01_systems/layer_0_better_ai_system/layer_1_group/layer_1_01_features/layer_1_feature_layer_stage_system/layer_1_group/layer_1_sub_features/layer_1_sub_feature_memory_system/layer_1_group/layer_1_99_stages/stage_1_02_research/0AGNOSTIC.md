---
resource_id: "e8765061-6a11-46fd-9ac4-c9d57da0fed2"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# memory_system — Stage 02: Research

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Stage Definition ──

<!-- section_id: "a79ddb34-dd52-4d35-8b5a-ba34a076fa20" -->
## Identity

stage_id: "2a8d8b61-5158-44fd-af2e-919ed912ab16"

entity_id: "540973e5-988f-41b5-892e-71e4224d70c8"

You are the **Research Agent** for the memory_system.
- **Role**: Research agent — explore the AI agent memory problem space, survey existing solutions, produce distilled knowledge
- **Scope**: Memory system research — cognitive science foundations, data structures, implementation architectures, commercial platforms, benchmarks. Do NOT design implementations (that's stage 05) or write code (that's stage 06).
- **Parent**: `../../0AGNOSTIC.md` (memory_system entity)
- **Domain**: AI agent memory systems — how agents remember, load, and navigate context

<!-- section_id: "8b06f3d8-b452-439b-9ec7-30302b256985" -->
## Key Behaviors

<!-- section_id: "e22d4fe5-cbf5-4048-b16d-69b547799efe" -->
### What Research IS
Comprehensive exploration of the AI agent memory problem space through systematic survey, deep-dive analysis, and knowledge synthesis. The research stage produces structured knowledge documents that later stages consume.

You do NOT:
- Write implementation requirements (that's stage 03_instructions)
- Design system architecture (that's stage 05_design)
- Write code or prototypes (that's stage 06_development)
- Test or evaluate implementations (that's stage 07_testing)

<!-- section_id: "803387fd-2707-408e-b3d7-2e9cb1b1784e" -->
### Delegation Contract
When the manager delegates to this stage:
- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand
- **Example prompt**: `"Work on stage_1_02_research for memory_system. Read 0AGNOSTIC.md for instructions. Task: research AI agent memory architectures"`

<!-- section_id: "dd5137b3-4bf0-4dc3-9e0c-f16fd92dd601" -->
### Methodology
4-phase research process (see `.0agnostic/03_protocols/research_methodology_protocol.md`):
1. **Survey** — identify all topics, create master taxonomy (doc 00)
2. **Deep Dive** — one document per topic (numbered 01+), covering: what it is, how it works, data structures, implementations, benchmarks
3. **Synthesis** — create hierarchy documents (docs 21-23), deep-dives (24-28), real-world systems (29-31), and comparisons with layer-stage system (32-37). Produce distilled knowledge in `.0agnostic/01_knowledge/`
4. **Handoff** — write stage report, identify what stage 03 needs, flag open items

Research output standard: `.0agnostic/02_rules/static/research_output_standards.md`

<!-- section_id: "fd02527c-8c49-4ee0-9692-8f308c49867b" -->
## Inputs

| Source | Location | When |
|--------|----------|------|
| Own identity & methodology | `0AGNOSTIC.md` (this file) | Always — first read on entry |
| Parent entity context | `../../0AGNOSTIC.md` | On-demand — when domain context needed |
| Parent domain knowledge | `../../.0agnostic/01_knowledge/` | On-demand — read specific topic relevant to task |
| Source material | External (Perplexity, web, papers) | During research — cite all sources |

**Context loading order**: Read own 0AGNOSTIC.md first (mandatory). Then load parent/prior-stage context on-demand.

<!-- section_id: "98d6e422-46d8-4454-90a2-a8a8e8a898ea" -->
## Outputs

| Output | Location | Purpose |
|--------|----------|---------|
| Research documents (38) | `outputs/by_topic/` | One focused topic per doc, numbered 00-37 |
| Distilled knowledge | `.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md` | Synthesized key findings |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | Async status for the manager |

<!-- section_id: "88756912-e72a-4e1a-8a75-a970b416147d" -->
## Triggers

Load when:
- Manager delegates research work for memory_system
- Entering `stage_1_02_research/`
- User mentions: memory research, memory survey, memory literature review

# ── Current Status ──

<!-- section_id: "ea9a30d5-16db-477c-91fd-b04b0a069a38" -->
## Current Status

**Status**: active — research comprehensive | **Last Updated**: 2026-02-21 | **Document Count**: 38

<!-- section_id: "1397a591-f150-45d1-8b2e-843f49059900" -->
### Research Scope
38 research documents produced across 5 categories:
- **Foundation** (00-20): Taxonomy, cognitive science, content types, frameworks, platforms, benchmarks, guides
- **Hierarchies** (21-23): 6-level biological buildup, 10-level data structure layers, 9-tier AI systems + SHIMI
- **Deep Dives** (24-28): Biological data structures per type, AI implementations per type, SQL schemas, nesting analysis, supporting structures
- **Real-World Systems** (29-31): Open-source implementations (Mem0, Eion, MemOS), complete agent systems (OASIS, CrewAI, LangGraph), AI tutor systems (ATLAS, Mem0 Tutor)
- **Layer-Stage Comparisons** (32-37): Context chain vs commercial, episodic memory approaches, agent delegation patterns, data structures comparison, technology integration roadmap, context avenue web vs commercial

<!-- section_id: "208a0640-8109-4df6-ba82-ab711c06d8bc" -->
### Key Memory Type Findings (Emphasis)
**Semantic memory** (L4 foundation): pgvector + knowledge graphs in PostgreSQL. SHIMI adds meaning-driven hierarchical retrieval. 471 QPS at 99% recall.

**Time-based memory** (L4 foundation): TimescaleDB hypertables, temporal validity tracking (valid_from/valid_until), hierarchical time buckets. TCM (Temporal Context Model) from neuroscience — drifting context vectors.

**Episodic memory** (L5, builds on semantic+time): Vector DB episodes (FAISS, ChromaDB) + hypertable storage. AWS Bedrock two-stage extraction. MongoDB cognitive dynamics (importance, decay, reinforcement). Event segmentation boundaries.

**Procedural memory** (L5, builds on semantic+motor): Mem^p framework (+8pts success, 18% fewer steps). Skill registries with JSONB trajectories. LangMem for persistent tool-use. Production rules (IF-THEN).

<!-- section_id: "6f658bca-27f6-48b0-aa6c-c9f34daa5913" -->
### Integration with Layer-Stage System
Docs 32-37 analyze where relational tables, vectors, knowledge graphs, and SHIMI could enhance the existing layer-stage system. Key integration points: semantic search over .0agnostic/ resources, knowledge graph for entity hierarchy, vector-augmented skill matching, SHIMI-inspired sync for agnostic-sync.sh.

<!-- section_id: "3e3f1887-bd06-4dea-af6d-ebd707758111" -->
### Key Reference
Distilled knowledge summary with technology × memory type mapping: `.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md`

<!-- section_id: "86dd3e71-cf12-40ed-a7bd-1c524daf3492" -->
### Readiness
Ready for review and handoff to stage 03 (instructions). Knowledge summary updated with emphasis on semantic, time-based, episodic, procedural memory types and how vectors, SQL, knowledge graphs, and SHIMI serve each. Stage report needs update to reflect docs 24-37.

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "5d9ec5e4-e547-4e08-9a8b-5a9b5a21c3b2" -->
## Current State Detail

<!-- section_id: "33107e21-e0b3-4092-a94b-873c39dbd5ff" -->
### Summary

Comprehensive research into AI agent memory systems: 38 documents covering biological foundations, neuroscience data structures, AI implementations per memory type, SQL schemas, real-world open-source systems, complete agent frameworks, AI tutor systems, and comparative analysis with the layer-stage system. Emphasis on the four critical long-term memory types (semantic, time-based, episodic, procedural) and their concrete AI implementations.

<!-- section_id: "3834031f-4514-4bba-a735-fd96294d7869" -->
### Key Outputs by Category

| Category | Docs | Description |
|----------|------|-------------|
| Foundation | 00-20 | Taxonomy, cognitive science, content types, frameworks, platforms, benchmarks, guides |
| Hierarchies | 21-23 | 6-level biological, 10-level data structures, 9-tier AI systems + SHIMI |
| Deep Dives | 24-28 | Neuroscience structures (TCM, event segmentation), AI implementations (Mem^p, LangMem), SQL schemas (pgvector, hypertables), nesting analysis, supporting structures (bloom filters, skip lists, tries) |
| Real-World | 29-31 | Mem0/Eion/MemOS, OASIS/CrewAI/LangGraph/AutoGen, ATLAS/Mem0 Tutor |
| Comparisons | 32-37 | Context chain vs commercial, episodic approaches, delegation patterns, data structures, integration roadmap, avenue web vs commercial |

<!-- section_id: "7f1219c1-8f8f-467d-a9ed-c1f495c7eba5" -->
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

<!-- section_id: "b6a80b05-00dd-46e9-8b3b-f7264d68589e" -->
## Open Items

- Stage report needs update to reflect docs 24-37 (currently only covers 00-23)
- Prototype implementation not yet started (see `19_prototype_specification.md`)
- Emotional and spatial memory types not yet mapped to concrete AI implementations
- Multi-agent memory synchronization patterns need deeper investigation
- Context chain propagation needed: update parent entity 0AGNOSTIC.md, .0agnostic, layer reports up the hierarchy
- .1merge/ sync and agnostic-sync.sh regeneration needed after 0AGNOSTIC.md updates

<!-- section_id: "80255b4c-f804-4898-9367-9f28a9122d14" -->
## Handoff

- **Ready for next stage**: yes (research is comprehensive)
- **Next stage**: 03_instructions
- **Start with**: The 9-tier core AI memory systems (doc 23) as architectural framework. Focus on semantic + time-based (L4 foundations) first, then episodic + procedural (L5). Minimal core = vectors + SQL + working memory (Phase 1). SHIMI, procedural/Mem^p as Phase 2. Unified PostgreSQL is the recommended storage strategy. For layer-stage integration, see docs 32-37 (comparisons + integration roadmap).

# ── References ──

<!-- section_id: "64e74b4d-182c-42c2-bade-4ac1332aa762" -->
## Navigation

| Content | Location |
|---------|----------|
| Research documents | `outputs/by_topic/` (38 files, 00-37) |
| Knowledge summary | `.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md` |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` |
| Research output rules | `.0agnostic/02_rules/static/research_output_standards.md` |
| Research methodology | `.0agnostic/03_protocols/research_methodology_protocol.md` |
| Context avenue registry | `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/registry.md` |

<!-- section_id: "3e53b4c7-0eb7-4266-8b4a-2bda6842fcb8" -->
## Domain Context

For memory system domain understanding, read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md` (what memory_system IS)
- Parent knowledge: `../../.0agnostic/01_knowledge/` (available domain knowledge)
- Key concepts: context chains, navigation, dynamic memory, episodic memory, three-tier knowledge

Do NOT load all parent knowledge at once — read the specific file relevant to the task at hand.

<!-- section_id: "dd6a90b3-8f7a-4e3a-8a62-5a6674cf2631" -->
## Success Criteria

This stage is complete when:
- All identified topic areas have a dedicated research document
- Core hierarchy documents (biological, data structure, AI systems) are synthesized
- Knowledge summary is distilled into `.0agnostic/01_knowledge/`
- Stage report captures key findings and handoff for stage 03
- Sources are cited in every document

<!-- section_id: "b1b54762-1312-497c-946c-40b93d812936" -->
## On Exit

1. Update `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` with current status
2. If handing off to stage 03: Start with 9-tier AI memory systems (doc 23), minimal core = vectors + SQL + working memory, SHIMI as Phase 2
3. If handing off to stage 05: Provide the unified PostgreSQL architecture as the recommended storage strategy
