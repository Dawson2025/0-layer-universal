# OpenAI Context



## Identity
You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Memory System.
- **Role**: Memory and context system — how AI agents remember, load, and navigate context
- **Scope**: Context chains, navigation, dynamic memory, episodic memory, AI agent memory architectures
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_feature_layer_stage_system)
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
- Stages (00-11) in `layer_1_group/layer_1_99_stages/` handle lifecycle work
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
| Stage outputs | `layer_1_group/layer_1_99_stages/stage_1_*/outputs/` |

## Triggers
Load this context when:
- User mentions: memory system, context chain, context loading, navigation, dynamic memory
- Working on: Memory architecture, context persistence, recall mechanisms
- Entering: `layer_1_sub_feature_memory_system/`


## Current Status
**active** — Stage 02 (research) complete with 38 research documents. Stage 04 (design) active with 4 architecture documents: unified sync, data-based avenues 09-13, enriched skill model, source-of-truth flow. Avenue web restructured with 01_file_based/ and 02_data_based/ subdirs. | Last Updated: 2026-02-22


## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
