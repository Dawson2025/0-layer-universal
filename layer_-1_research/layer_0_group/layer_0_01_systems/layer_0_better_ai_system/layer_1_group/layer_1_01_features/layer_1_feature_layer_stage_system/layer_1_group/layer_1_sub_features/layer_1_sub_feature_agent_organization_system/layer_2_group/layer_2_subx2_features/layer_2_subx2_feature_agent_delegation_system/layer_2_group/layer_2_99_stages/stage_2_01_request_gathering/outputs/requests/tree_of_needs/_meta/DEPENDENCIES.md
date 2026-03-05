---
resource_id: "08ae9f10-e54b-49b1-af95-c6b2c9b84291"
resource_type: "output"
resource_name: "DEPENDENCIES"
---
# Dependencies

How this tree of needs relates to lateral entities after the 2026-03-04 hierarchy reorganization.

---

<!-- section_id: "3b352b10-5681-430c-897f-7947cf91ec10" -->
## Entity Cross-References

> **Reorganization note**: memory_system and multi_agent_system were formerly children of agent_delegation_system. After reorganization:
> - memory_system promoted to L1 sibling under layer_stage_system
> - multi_agent_system dissolved — agent_hierarchy and orchestration moved to L2 siblings under agent_organization_system

| Entity | Relationship | Location (from agent_delegation_system root) | Related Branches |
|--------|-------------|----------------------------------------------|-----------------|
| **memory_system** | L1 sibling (was child) | `../../../../layer_1_sub_feature_memory_system/` | 02_memory_integration (directly), 01_delegation_model (context model) |
| **agent_hierarchy** | L2 sibling (was grandchild via multi_agent_system) | `../layer_2_subx2_feature_agent_hierarchy/` | 03_coordination_patterns/need_01 |
| **orchestration** | L2 sibling (was grandchild via multi_agent_system) | `../layer_2_subx2_feature_orchestration/` | 03_coordination_patterns/need_02, need_03 |
| **context_chain_system** | L2 child of memory_system | `../../../../layer_1_sub_feature_memory_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/` | 02_memory_integration/need_01 |

---

<!-- section_id: "39240985-860b-484d-bcce-05c5c6185e99" -->
## Branch-to-Entity Mapping

<!-- section_id: "eedd09e9-b9c1-4d65-8fa8-78c6716be570" -->
### 01_delegation_model
- **memory_system** (lateral): Agent context model requires context chain loading rules (need_03)
- **orchestration** (sibling): Stage delegation and stage reports define multi-agent communication (need_01, need_02)

<!-- section_id: "0858d07b-169c-4456-b419-71737711caea" -->
### 02_memory_integration
- **memory_system** (lateral): All three needs directly inform memory system design
  - Context chain support (need_01) -> context_chain_system
  - Handoff protocols (need_02) -> episodic memory, navigation
  - Three-tier delegation (need_03) -> three-tier knowledge architecture

<!-- section_id: "fd0c55fe-ac69-480f-818f-832f96e22d9d" -->
### 03_coordination_patterns
- **agent_hierarchy** (sibling): Agent hierarchy need (need_01) -> who manages whom
- **orchestration** (sibling): Spawning patterns and communication channels (need_02, need_03) -> Task tool, teams, agent lifecycle
- **memory_system** (lateral): Communication channels (need_03) use memory infrastructure

---

<!-- section_id: "4cc067f7-365c-4c30-941a-4a9d80c912ab" -->
## Dependency Direction

```
agent_delegation_system (this tree)
|
+-- 01_delegation_model
|   +-- informs -> orchestration (sibling: how agents delegate)
|   +-- informs -> memory_system (lateral: what agents know)
|
+-- 02_memory_integration
|   +-- informs -> memory_system (lateral: how memory serves delegation)
|   +-- overlaps -> context_chain_system tree (shared knowledge concepts)
|
+-- 03_coordination_patterns
    +-- informs -> agent_hierarchy (sibling: who manages whom)
    +-- informs -> orchestration (sibling: spawning, communication)
    +-- informs -> memory_system (lateral: communication channels use memory)
```
