# Gemini Context

---
resource_id: "ac451a4c-1705-4077-a988-80dfc2f20cd4"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_1_sub_feature_tool_and_app_agnostic

<!-- section_id: "c3728676-d2f9-4f45-8d96-a4a4a6fa42e6" -->
## Identity

entity_id: "56fc3df0-5122-4ebf-b62c-063d22c838dc"

You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Tool and App Agnostic.
- **Role**: Tool-agnostic context system — ensuring the framework works across all AI tools and applications
- **Scope**: Agnostic sync, merge system, tool-specific overrides, cross-tool compatibility, and dedicated porting-system layering
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: `porting_system` (in `layer_2_group/layer_2_subx2_features/`)

<!-- section_id: "d98026c9-8a35-484e-9eff-b35d53308ea3" -->
## Triggers
Load this context when:
- User mentions: tool-agnostic, agnostic sync, merge system, cross-tool, app-agnostic
- Working on: Agnostic system design, merge workflows, tool compatibility
- Entering: `layer_1_sub_feature_tool_and_app_agnostic/`

<!-- section_id: "01055221-99a3-41c8-b297-98a95db095ad" -->
## Pointers
<!-- section_id: "267919cb-05de-481c-8a22-b642a99f579e" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_1_group/layer_1_99_stages/` for stage progress
3. Load bridge contract: `.0agnostic/01_knowledge/overview/docs/agnostic_to_tool_porting_bridge_contract.md`
4. Traverse to `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_porting_system/` when the task is about canonical-to-tool/app projection work

<!-- section_id: "5305ec7a-b0fc-40fb-9bc1-8e877f8cfa8f" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| Children | `layer_2_group/layer_2_subx2_features/` |
| Downstream bridge consumer | `../layer_1_sub_feature_agent_delegation_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_context_chain_system/` |

### Resources
| Resource | Path | Purpose |
|----------|------|---------|
| Overview docs | `.0agnostic/01_knowledge/overview/` | Bridge contracts and production tooling references |
| Principles | `.0agnostic/01_knowledge/principles/` | Stable design principles for tool/app-agnostic context systems |
| Things learned | `.0agnostic/01_knowledge/things_learned/` | Captured implementation lessons and operational discoveries |

<!-- section_id: "d102a1ed-002b-4457-a648-87ea16d0801b" -->
## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/episodic_memory/` |

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
