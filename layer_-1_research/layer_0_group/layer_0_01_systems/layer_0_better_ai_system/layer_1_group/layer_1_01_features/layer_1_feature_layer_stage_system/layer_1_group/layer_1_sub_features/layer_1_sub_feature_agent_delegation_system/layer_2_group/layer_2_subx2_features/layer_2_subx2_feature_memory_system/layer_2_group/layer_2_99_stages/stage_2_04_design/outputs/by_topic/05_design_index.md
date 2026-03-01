# Design Stage Index — Memory System (Stage 04)

## Purpose

This stage produces architecture and design documents that translate research findings (stage 02, 38 docs) into concrete system designs for the memory system integration into the layer-stage framework.

## Design Documents

| # | Document | Summary | Research Basis |
|---|----------|---------|----------------|
| 01 | [Unified Sync Architecture](01_unified_sync_architecture.md) | **Pointer** → canonical at context_chain_system stage_3_04 doc 07 | Docs 32, 36, 37 |
| 02 | [Data Avenue Web Expansion](02_data_avenue_web_expansion.md) | Avenues 09-13 design: knowledge graph, relational index, vectors, temporal, SHIMI | Docs 23, 24, 25, 29, 32-37 |
| 03 | [Enriched Skill Model](03_enriched_skill_model.md) | Skills as mini-entities with knowledge, rules, trajectory stores, temporal data | Docs 25, 30, 34, 36 |
| 04 | [Source of Truth to Avenue Flow](04_source_of_truth_to_avenue_flow.md) | **Pointer** → canonical at context_chain_system stage_3_04 doc 06 | Docs 32-37 |
| 05 | [Design Index](05_design_index.md) | This file — index of all design documents |

## Scope Boundaries

**This stage (04 design) covers**:
- Architecture and system design documents
- Directory structure specifications
- Schema designs (graph, SQL, embedding, temporal)
- Sync pipeline specifications
- Integration point identification

**This stage does NOT cover** (belongs to other stages):
- Implementation requirements and constraints → stage 03 (instructions)
- Work breakdown and milestones → stage 05 (planning)
- Actual code and scripts → stage 06 (development)
- Testing and validation → stage 07 (testing)

## Key Architectural Decisions

1. **Files remain source of truth** — databases are derived indexes, always regenerable
2. **Zero-dependency operation preserved** — data-based avenues are optional accelerators
3. **Avenue web extends, not replaces** — avenues 09-13 add to 01-08, same ordering convention
4. **Skills enrich, not promote** — skills gain trajectory/temporal data but do NOT become full entities
5. **Single orchestrator** — sync-main.sh coordinates all sync scripts with dependency ordering
6. **Phased rollout** — scaffold now, build scripts in stage 06, integrate in stage 06, production after stage 07

## Research → Design Traceability

| Research Category | Docs | Design Impact |
|-------------------|------|---------------|
| Foundation (00-20) | Taxonomy, cognitive science, frameworks | Informed avenue ordering and memory type mapping |
| Hierarchies (21-23) | Biological, data structure, AI systems | Drove the 9-tier minimal core recommendation |
| Deep Dives (24-28) | Per-type implementations, SQL schemas | Directly inform avenue 10-12 schema designs |
| Real-World (29-31) | Mem0, CrewAI, OASIS, AI tutors | Validated trajectory stores and cognitive dynamics |
| Comparisons (32-37) | Layer-stage vs commercial | Identified gaps (semantic search, automation, dynamics) that avenues 09-13 address |
