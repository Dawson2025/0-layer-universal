---
resource_id: "9799aad2-4e43-44aa-937c-79404861bf3d"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# memory_system — Stage 04: Design

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Stage Definition ──

<!-- section_id: "25aaf8ba-82ca-43f3-8b6c-109c95c13044" -->
## Identity

stage_id: "3c4440d2-f907-4854-b90e-7c0c24e5a154"

entity_id: "7891ca74-cbfa-4109-9da3-e673f253b107"

You are the **Design Agent** for the memory_system.

- **Role**: Architecture and system design — translate research findings into concrete system designs for memory integration into the layer-stage framework
- **Scope**: Architecture documents, directory structure specs, schema designs, sync pipeline specs, integration point identification — do NOT implement code (that's stage 06) or define requirements (that's stage 03)
- **Parent**: `../../0AGNOSTIC.md` (memory_system entity)
- **Domain**: AI agent memory systems, context delivery architecture, sync pipelines

<!-- section_id: "c433f79d-205d-4fee-a621-bbfd79e85bc0" -->
## Key Behaviors

<!-- section_id: "7898182e-85f8-4069-b6d1-32bb1e4cea50" -->
### What Design IS

Design translates research findings into actionable architecture. You take the 38 research documents from stage 02 and produce system designs that can be directly implemented in stage 06. Focus on concrete specifications: directory structures, schemas, sync pipelines, integration points.

You do NOT:
- Implement code or scripts (that's stage 06)
- Define requirements or constraints (that's stage 03)
- Plan work breakdown or milestones (that's stage 05)
- Test or validate implementations (that's stage 07)

<!-- section_id: "5d084f85-4558-47cc-8925-bb6caf990742" -->
### Delegation Contract

When the manager delegates to this stage:
- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand
- **Example prompt**: `"Work on stage_1_04_design for memory_system. Read 0AGNOSTIC.md for instructions. Task: Design the data-based avenue expansion."`

<!-- section_id: "2db62762-e448-476b-88a2-81f98e34a5a9" -->
### Methodology

1. Read research findings from stage 02 outputs (38 docs)
2. Identify architectural decisions needed
3. Produce design documents with diagrams, schemas, and specifications
4. Trace each design decision back to research evidence
5. Maintain backward compatibility with existing file-based system

<!-- section_id: "97c9e0a2-1d2b-4ee8-9cc4-7447063d9893" -->
## Inputs

| Source | Location | When |
|--------|----------|------|
| Own identity & methodology | `0AGNOSTIC.md` (this file) | Always — first read on entry |
| Research documents (38 docs) | `../stage_1_02_research/outputs/by_topic/` | On-demand — when referencing specific research |
| Research knowledge summary | `../stage_1_02_research/.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md` | On-demand — for distilled findings |
| Parent entity context | `../../0AGNOSTIC.md` | On-demand — when domain context needed |

**Context loading order**: Read own 0AGNOSTIC.md first (mandatory). Then load research docs on-demand — only the specific doc needed, never all 38 at once.

<!-- section_id: "e49fbd62-4f0e-4e62-a728-ddbd9967741e" -->
## Outputs

| Output | Location | Purpose |
|--------|----------|---------|
| Unified Sync Architecture | `outputs/by_topic/01_unified_sync_architecture.md` | sync-main.sh orchestrator spec, sync registry |
| Data Avenue Web Expansion | `outputs/by_topic/02_data_avenue_web_expansion.md` | Avenues 09-13 design: KG, relational, vectors, temporal, SHIMI |
| Enriched Skill Model | `outputs/by_topic/03_enriched_skill_model.md` | Skills as mini-entities with trajectory stores |
| Source of Truth to Avenue Flow | `outputs/by_topic/04_source_of_truth_to_avenue_flow.md` | Holistic context ordering design |
| Design Index | `outputs/by_topic/05_design_index.md` | Index of all design documents |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | Async status for the manager |

<!-- section_id: "3e6d91c7-1478-4268-8bbc-eba98e5dbb8b" -->
## Triggers

Load when:
- Manager delegates design work for memory system
- Entering `stage_1_04_design/`
- Working on: architecture, schema design, sync pipeline design, avenue web expansion

# ── Current Status ──

<!-- section_id: "1008bc61-faac-43d7-b258-74c805dc9268" -->
## Current Status

**active** — 4 architecture documents produced covering sync architecture, data-based avenue expansion (09-13), enriched skill model, and source-of-truth flow. Avenue web restructured with 01_file_based/ and 02_data_based/ subdirectories. Scaffolding complete for avenues 09-13. | Last Updated: 2026-02-22

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "b5b17ee1-105d-44f2-8c72-98b4297d724b" -->
## Current State Detail

<!-- section_id: "0134cbdb-2ac6-4f3e-aa47-0979ad21a80f" -->
### Summary

Stage 04 has produced 4 design documents translating the 38 research documents from stage 02 into concrete system architecture. The designs cover: (1) unified sync orchestration via sync-main.sh, (2) 5 new data-based avenues extending the avenue web, (3) enriched skill model with trajectory stores and temporal data, (4) holistic source-of-truth-to-avenue flow specification.

Additionally, the avenue web at the root level has been physically restructured into `01_file_based/` (01-08) and `02_data_based/` (09-13) subdirectories. Scaffolding (directories + READMEs) for avenues 09-13 is complete. REGISTRY.md and sync-registry.json have been created.

<!-- section_id: "72067de7-1a6f-45aa-aad6-6bb65f3ea2eb" -->
### Key Outputs

| Output | Description |
|--------|-------------|
| `outputs/by_topic/01_unified_sync_architecture.md` | sync-main.sh orchestrator spec, existing script catalog, dependency ordering |
| `outputs/by_topic/02_data_avenue_web_expansion.md` | Avenues 09-13: knowledge graph, relational index, vectors, temporal, SHIMI |
| `outputs/by_topic/03_enriched_skill_model.md` | Skills gain trajectory/, temporal/, knowledge/, rules/ subdirs |
| `outputs/by_topic/04_source_of_truth_to_avenue_flow.md` | 0AGNOSTIC.md → 01-05 source → 06 avenue web flow |
| `outputs/by_topic/05_design_index.md` | Index with research traceability |

<!-- section_id: "381f097d-0acd-4297-a307-5a18edf2ec8a" -->
### Key Architectural Decisions

1. **Files remain source of truth** — databases are derived indexes, always regenerable
2. **Zero-dependency operation preserved** — data-based avenues are optional accelerators
3. **Avenue web extends, not replaces** — avenues 09-13 add to 01-08, same ordering convention
4. **Physical separation** — `01_file_based/` and `02_data_based/` subdirs within `06_context_avenue_web/`
5. **Skills enrich, not promote** — skills gain trajectory/temporal data but do NOT become full entities
6. **Single orchestrator** — sync-main.sh coordinates all sync scripts with dependency ordering
7. **Phased rollout** — scaffold now, build scripts in stage 06, integrate in stage 06, production after stage 07

<!-- section_id: "dce1f433-deea-44fe-947d-9a5e2c812ef4" -->
### Research → Design Traceability

| Research Category | Docs | Design Impact |
|-------------------|------|---------------|
| Foundation (00-20) | Taxonomy, cognitive science, frameworks | Informed avenue ordering and memory type mapping |
| Hierarchies (21-23) | Biological, data structure, AI systems | Drove the 9-tier minimal core recommendation |
| Deep Dives (24-28) | Per-type implementations, SQL schemas | Directly inform avenue 10-12 schema designs |
| Real-World (29-31) | Mem0, CrewAI, OASIS, AI tutors | Validated trajectory stores and cognitive dynamics |
| Comparisons (32-37) | Layer-stage vs commercial | Identified gaps that avenues 09-13 address |

<!-- section_id: "5d5afe28-c1ec-4e98-9e30-ba03a1e41abb" -->
## Open Items

- sync-main.sh implementation (stage 06)
- Data-based avenue build scripts (stage 06)
- Enriched skill model implementation (stage 06)
- Schema validation and testing (stage 07)

<!-- section_id: "00f34029-6aec-4a35-a840-0d8ccca3f104" -->
## Handoff

- **Ready for next stage**: yes (design is comprehensive, scaffolding is in place)
- **Next stage**: 06_development (to implement sync-main.sh, data-based avenue scripts, enriched skill infrastructure)
- **Start with**: Implement sync-main.sh orchestrator first (it's the foundation), then build-graph.sh (avenue 09), then build-index.sh (avenue 10). Skill enrichment can proceed in parallel.

# ── References ──

<!-- section_id: "e174979a-15d4-4b7e-8cf2-e9652b13c232" -->
## Navigation

| Content | Location |
|---------|----------|
| Design documents | `outputs/by_topic/` |
| Design index | `outputs/by_topic/05_design_index.md` |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` |
| Research inputs | `../stage_1_02_research/outputs/by_topic/` |

<!-- section_id: "d0056671-0649-435f-b6ab-8d534d56ab91" -->
## Domain Context

For memory system understanding, read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md` (what this entity IS)
- Parent knowledge: `../../.0agnostic/01_knowledge/memory_systems/` (memory system concepts)
- Research summary: `../stage_1_02_research/.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md`

Do NOT load all parent knowledge at once — read the specific file relevant to the task at hand.

<!-- section_id: "230e292a-82de-430d-aeae-fabbb0c56278" -->
## Success Criteria

This stage is complete when:
- Architecture documents cover all identified gaps from research (semantic search, automation, dynamics)
- Each design decision is traceable to specific research documents
- Designs maintain backward compatibility with existing file-based system
- Directory scaffolding for new avenues is in place

<!-- section_id: "67eeed1f-628b-4032-832e-98fe03209d8a" -->
## On Exit

1. Update `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` with current status
2. If handing off to stage 06: Prioritize sync-main.sh, then data-based avenue scripts
3. If handing off to stage 03: Use design docs to inform requirements and constraints
