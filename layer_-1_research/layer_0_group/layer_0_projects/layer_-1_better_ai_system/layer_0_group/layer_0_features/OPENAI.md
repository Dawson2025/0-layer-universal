# OpenAI Context


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
