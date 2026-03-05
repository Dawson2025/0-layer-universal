---
resource_id: "876729fa-5cb4-4975-a47f-8ca583e7db20"
resource_type: "output"
resource_name: "three_tier_knowledge_architecture"
---
# Three-Tier Knowledge Architecture

<!-- section_id: "cf6db278-ec63-4a1e-b0aa-84c05cbae6b5" -->
## Source

This document is a reference copy pointing to the primary research in the memory system.

**Full document**: `memory_system/stage_1_02_research/outputs/by_topic/20_three_tier_knowledge_architecture.md`

**Absolute path**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_subx2_features/layer_1_subx2_feature_memory_system/layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/by_topic/20_three_tier_knowledge_architecture.md`

---

<!-- section_id: "b5a39386-0aa3-4dbc-82ef-6fec1e24df2a" -->
## Summary

Knowledge in the layer-stage system is organized into three tiers:

| Tier | Location | Contains | When Loaded |
|------|----------|----------|-------------|
| **1. Pointers** | `0AGNOSTIC.md` → `CLAUDE.md` | Identity, scope, "where to find things" | Always (static context) |
| **2. Distilled** | `.0agnostic/knowledge/` | Actionable summaries, principles, decisions | On-demand (entering entity) |
| **3. Full** | `stage_*/outputs/` | Complete research, designs, raw analysis | On-demand (need detail) |

<!-- section_id: "c7648a7f-e181-4f5d-a960-ca2d25cb5447" -->
### Key Rules

1. **Knowledge files are NOT copies** — they're distilled summaries that reference stage outputs
2. **Stage outputs are source of truth** — if knowledge file and stage output disagree, stage output wins
3. **0AGNOSTIC.md never has substantive content** — only pointers
4. **Consolidation at stage boundaries** — raw findings become distilled knowledge when a stage completes
5. **Directional flow**: stages → knowledge → pointers (never upward)

<!-- section_id: "7b31ac68-212e-4aa9-858a-38c3cc989cba" -->
### Compression Example

19 research files (~5,000 lines) → 5 distilled knowledge files (~260 lines) = 19:1 ratio.
Agent reads 260 lines for competence, 5,000 lines only when specific details needed.

<!-- section_id: "c717e488-b175-4b6d-bb12-0d99f582dfec" -->
### Brain Analogy

- Tier 3 (stage outputs) = Hippocampus (detailed episodic records)
- Tier 2 (knowledge files) = Neocortex (consolidated semantic memory)
- Tier 1 (pointers) = Prefrontal cortex (executive navigation — knows what you know)
- Stage boundaries = Sleep consolidation (when transfer happens)

---

<!-- section_id: "eb206f29-ac67-4c13-b44a-e44b6c33482a" -->
## Applicability to Context Chain System

This architecture directly applies to how the context chain system organizes its own knowledge:
- Existing `.0agnostic/knowledge/` files (architecture, optimization, principles) = Tier 2
- Existing research in `stage_2_02_research/outputs/` = Tier 3
- `0AGNOSTIC.md` pointers = Tier 1

**Needs defined**: See `stage_2_01_request_gathering/outputs/requests/tree_of_needs/00_context_survives_boundaries/01_knowledge_organization/need_01_three_tier_architecture/`
