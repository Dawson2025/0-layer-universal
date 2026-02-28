# Three-Tier Knowledge Architecture

## Source

This document is a reference copy pointing to the primary research in the memory system.

**Full document**: `memory_system/stage_2_02_research/outputs/by_topic/20_three_tier_knowledge_architecture.md`

**Absolute path**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/layer_2_group/layer_2_99_stages/stage_2_02_research/outputs/by_topic/20_three_tier_knowledge_architecture.md`

---

## Summary

Knowledge in the layer-stage system is organized into three tiers:

| Tier | Location | Contains | When Loaded |
|------|----------|----------|-------------|
| **1. Pointers** | `0AGNOSTIC.md` → `CLAUDE.md` | Identity, scope, "where to find things" | Always (static context) |
| **2. Distilled** | `.0agnostic/knowledge/` | Actionable summaries, principles, decisions | On-demand (entering entity) |
| **3. Full** | `stage_*/outputs/` | Complete research, designs, raw analysis | On-demand (need detail) |

### Key Rules

1. **Knowledge files are NOT copies** — they're distilled summaries that reference stage outputs
2. **Stage outputs are source of truth** — if knowledge file and stage output disagree, stage output wins
3. **0AGNOSTIC.md never has substantive content** — only pointers
4. **Consolidation at stage boundaries** — raw findings become distilled knowledge when a stage completes
5. **Directional flow**: stages → knowledge → pointers (never upward)

### Compression Example

19 research files (~5,000 lines) → 5 distilled knowledge files (~260 lines) = 19:1 ratio.
Agent reads 260 lines for competence, 5,000 lines only when specific details needed.

### Brain Analogy

- Tier 3 (stage outputs) = Hippocampus (detailed episodic records)
- Tier 2 (knowledge files) = Neocortex (consolidated semantic memory)
- Tier 1 (pointers) = Prefrontal cortex (executive navigation — knows what you know)
- Stage boundaries = Sleep consolidation (when transfer happens)

---

## Applicability to Context Chain System

This architecture directly applies to how the context chain system organizes its own knowledge:
- Existing `.0agnostic/knowledge/` files (architecture, optimization, principles) = Tier 2
- Existing research in `stage_3_02_research/outputs/` = Tier 3
- `0AGNOSTIC.md` pointers = Tier 1

**Needs defined**: See `stage_3_01_request_gathering/outputs/requests/tree_of_needs/00_context_survives_boundaries/01_knowledge_organization/need_01_three_tier_architecture/`
