# 0AGNOSTIC.md - layer_2_subx2_feature_memory_system

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity
You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Memory System.
- **Role**: Memory and context system — how AI agents remember, load, and navigate context
- **Scope**: Context chains, navigation, dynamic memory, episodic memory, AI agent memory architectures
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_agent_delegation_system)
- **Children**: context_chain_system, navigation, dynamic_memory

## Key Behaviors

### What This Entity Covers
- **Context chains**: How context traverses from root to leaf entities through the hierarchy
- **Navigation**: How agents find and load relevant context within the layer-stage system
- **Dynamic memory**: Runtime context that changes during agent execution
- **Episodic memory**: Session records, work history, and continuity across sessions
- **AI agent memory architectures**: Research into biological, cognitive, and computational memory systems for AI agents

### Delegation
- Children (context_chain_system, navigation, dynamic_memory) handle specific sub-domains
- Stages (00-11) in `layer_2_group/layer_2_99_stages/` handle lifecycle work
- Stage 02 (research) is the primary active stage with substantial deliverables

## Delegation Contract

| From | To | What |
|------|----|------|
| Parent (agent_delegation_system) | This entity | Memory-related research, design, and implementation |
| This entity | Stage agents | Stage-specific work (research, design, development, etc.) |
| This entity | Children | Sub-domain specifics (context chains, navigation, dynamic memory) |

## Inputs

| Source | What | Path |
|--------|------|------|
| Parent needs (Branch 02) | memory_integration requirements | `../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/` |
| Parent research | Three-tier knowledge, two-halves pattern findings | `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/` |
| Parent design | Two-halves pattern (P9), stage reports for async | `../../../layer_1_group/layer_1_99_stages/stage_1_04_design/` |

## Outputs

| What | Location |
|------|----------|
| Layer research summary | `.0agnostic/01_knowledge/memory_systems/docs/layer_research_summary.md` |
| Layer report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md` |
| Stage outputs | `layer_2_group/layer_2_99_stages/stage_2_*/outputs/` |

## Triggers
Load this context when:
- User mentions: memory system, context chain, context loading, navigation, dynamic memory
- Working on: Memory architecture, context persistence, recall mechanisms
- Entering: `layer_2_subx2_feature_memory_system/`

# ── Current Status ──

## Current Status
**active** — Stage 02 (research) complete with 38 research documents. Stage 05 (design) active with 4 architecture documents: unified sync, data-based avenues 09-13, enriched skill model, source-of-truth flow. Avenue web restructured with file_based/ and data_based/ subdirs. | Last Updated: 2026-02-22

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

Stage 02 produced 38 research documents on AI agent memory systems. Stage 05 produced 4 design documents translating research into architecture. Key research findings:

- **Biological hierarchy**: Memory types form a 6-level dependency chain (sensory through autobiographical). Build L4 (semantic + time-based) first, then L5 (episodic + procedural), then L6.
- **AI memory tiers**: 9-tier ranking of AI memory systems. Minimal core = Vectors (T1) + SQL (T2) + Working Memory (T5).
- **SHIMI**: Semantic Hierarchical Memory Index at T3.5 provides meaning-driven retrieval superior to flat vector search. Hierarchical tree with explainable paths.
- **Unified storage**: PostgreSQL consolidation (pgvector + TimescaleDB + JSONB) reduces cost 66% with single ACID transactions across all memory types.
- **Consolidation pipeline**: 4-stage standard architecture (extract, consolidate, store, retrieve).
- **Benchmarks**: Mem0 achieves 91% latency reduction, pgvector 471 QPS at 99% recall, Mem^p +8 point success improvement.

## Key Outputs

| Output | Location |
|--------|----------|
| Layer research summary | `.0agnostic/01_knowledge/memory_systems/docs/layer_research_summary.md` |
| 38 research documents | `layer_2_group/layer_2_99_stages/stage_2_02_research/outputs/by_topic/` (00-37) |
| 4 design documents | `layer_2_group/layer_2_99_stages/stage_2_05_design/outputs/by_topic/` (01-05) |
| Stage knowledge summary | `layer_2_group/layer_2_99_stages/stage_2_02_research/.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md` |
| Stage report | `layer_2_group/layer_2_99_stages/stage_2_02_research/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` |
| Layer report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md` |

## Open Items

- Prototype implementation not yet started (see research doc 19_prototype_specification.md)
- SHIMI integration specifics for the layer-stage system need design work
- Emotional and spatial memory types not yet mapped to concrete AI implementations
- Multi-agent memory synchronization patterns need deeper investigation

## Handoff

- **Current transition**: Stage 02 (research) -> Stage 03 (instructions)
- **What stage 03 needs**: Start with the 9-tier core AI memory systems as the architectural framework. Minimal core (vectors + SQL + working memory) = Phase 1 scope. SHIMI and procedural memory = Phase 2. Unified PostgreSQL = recommended storage.

# ── References ──

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_3_group/layer_3_subx3_features/` for sub-features

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_2_group/layer_2_99_stages/` |
| Children | `layer_3_group/layer_3_subx3_features/` |

## .0agnostic/ References

| Section | Path |
|---------|------|
| Knowledge (layer summary) | `.0agnostic/01_knowledge/memory_systems/docs/layer_research_summary.md` |
| Rules | `.0agnostic/02_rules/` |
| Protocols | `.0agnostic/03_protocols/` |
| Episodic memory | `.0agnostic/04_episodic_memory/` |
| Handoff (layer report) | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md` |
| Stage reports | `layer_2_group/layer_2_99_stages/stage_2_02_research/.0agnostic/05_handoff_documents/` |
| Context avenue web | `.0agnostic/06_context_avenue_web/` |

## Parent Layer Context (Principle 10)

This entity details **Branch 02 (memory_integration)** from the parent agent_delegation_system's requirements. The parent layer provides the overview and broader context; this layer provides the detailed work.

| Parent Stage | What It Provides | Path |
|-------------|-----------------|------|
| Stage 01 (needs) | Branch 02: memory_integration — 3 needs (context_chain_support, handoff_protocols, three_tier_delegation) + Branch 01/need_03 (agent_context_model) | `../../../layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/` |
| Stage 02 (research) | Research findings on three-tier knowledge, two-halves pattern — this entity's context_chain_system child was the primary research vehicle | `../../../layer_1_group/layer_1_99_stages/stage_1_02_research/` |
| Stage 04 (design) | Design decisions: two-halves pattern (P9), three-tier knowledge, stage reports for async | `../../../layer_1_group/layer_1_99_stages/stage_1_04_design/` |
| Stage 06 (development) | Universal artifacts used by this entity: stage guides, principles, rules, protocols | `../../../layer_1_group/layer_1_99_stages/stage_1_06_development/` |
| Entity overview | Full agent_delegation_system context with tree of knowledge | `../../../0AGNOSTIC.md` |
| Tree of knowledge | Organized summaries + references to all parent stage content | `../../../.0agnostic/01_knowledge/tree_of_knowledge/00_agent_delegation_knowledge/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/04_episodic_memory/` |
