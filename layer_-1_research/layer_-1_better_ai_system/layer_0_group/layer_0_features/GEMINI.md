# Gemini Context


## Identity
Features registry for the better_ai_system research project.
- **Role**: Container for research features at Layer 0
- **Parent**: `../0AGNOSTIC.md` (layer_0_group)
- **Children**: layer_stage_system, multi_os_multi_machine_system, multimodal_system

## Triggers
Load this context when:
- Browsing or selecting research features
- Entering: `layer_0_features/`

## Pointers
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../0AGNOSTIC.md` |
| Layer-Stage System | `layer_0_feature_layer_stage_system/` |
| Multi-OS System | `layer_0_feature_multi_os_multi_machine_system/` |
| Multimodal System | `layer_0_feature_multimodal_system/` |

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
