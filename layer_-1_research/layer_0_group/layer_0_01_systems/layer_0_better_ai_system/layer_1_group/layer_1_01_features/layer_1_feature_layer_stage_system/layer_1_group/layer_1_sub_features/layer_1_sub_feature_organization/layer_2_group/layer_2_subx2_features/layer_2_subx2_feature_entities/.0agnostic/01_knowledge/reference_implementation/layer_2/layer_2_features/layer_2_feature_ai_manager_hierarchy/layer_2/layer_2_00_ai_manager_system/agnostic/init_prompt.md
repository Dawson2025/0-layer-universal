---
resource_id: "bf2fbe17-3f2f-4d1e-9551-583cee81eae1"
resource_type: "knowledge"
resource_name: "init_prompt"
---
# Init Prompt - Agnostic Source

## Purpose
Universal initialization context for any AI coding assistant.

## Context Gathering
1. Identify current layer location
2. Read CLAUDE.md at entity root
3. Navigate to layer_N_00_ai_manager_system/agnostic/
4. Apply tool-agnostic instructions

## Universal Instructions
- Follow layer navigation patterns
- Respect entity boundaries
- Apply stage-appropriate context
- Use standardized file patterns

## Tool Resolution
After loading agnostic source, check for specific overrides at:
`layer_N_00_ai_manager_system/specific/os/{os}/environment/{env}/coding_app/{app}/ai_app/{ai}/`
