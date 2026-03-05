---
resource_id: "020580ab-e5fe-4b8e-9a8d-72c2ac108589"
resource_type: "knowledge"
resource_name: "context_chains"
---
# Context Chains

<!-- section_id: "0bb9c71b-4142-4c03-9e7c-9a75d0484b9f" -->
## Summary

A context chain is the sequence of `0AGNOSTIC.md` files linked by `Parent:` references, forming an inheritance path from any entity to the system root. Every entity participates in exactly one chain. The chain serves two purposes: inheritance (context, rules, and knowledge flow downward) and navigation (agents traverse upward for escalation or scope validation).

Each `0AGNOSTIC.md` contains a relative `Parent:` reference (e.g., `../../../0AGNOSTIC.md`). Following these links produces a leaf-to-root chain. The context_chain_system entity has a depth of 7 levels. Not every node is a full entity -- container nodes (like `layer_N_group/`) exist for routing and have minimal 0AGNOSTIC.md files, while entity nodes have full stage structures and orchestrators.

The parent chain (0AGNOSTIC.md) and the CLAUDE.md cascade are two independent mechanisms. The 0AGNOSTIC chain is the canonical path (explicit, dynamic, on-demand). The CLAUDE.md cascade is the delivery mechanism for Claude Code (implicit, static, auto-loaded via filesystem walk). Both produce context inheritance but through different timing and triggers.

<!-- section_id: "1208f529-9e42-422d-aafe-b0f6d301bb2a" -->
## Key Concepts

- **Parent reference**: Every 0AGNOSTIC.md (except root) has a `Parent:` line pointing to its parent
- **Chain depth**: Varies by entity type; sub-sub-features traverse 3 `../` levels through group/features containers
- **Container vs entity**: Containers route (no stages, lightweight GAB); entities do work (11 stages, full GAB)
- **Traversal direction**: Leaf-to-root for context loading/escalation; root-to-leaf for delegation
- **Dual mechanism**: 0AGNOSTIC chain (canonical, dynamic) vs CLAUDE.md cascade (delivery, static)

<!-- section_id: "e6ebf9e2-ea80-4bcd-9ef8-1c2764a90b35" -->
## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Full architecture doc | `.0agnostic/01_knowledge/context_chain_architecture.md` | Chain structure, rules, traversal algorithm |
| Stage 02 research | `layer_2_99_stages/stage_2_02_research/outputs/by_topic/architecture/` | Original research findings |
| Chain visualization | `layer_3_group/.../chain_visualization/diagrams/current/context_chain/` | Visual diagrams |
| Chain optimization | `.0agnostic/01_knowledge/chain_optimization_strategies.md` | 6 optimization strategies |
