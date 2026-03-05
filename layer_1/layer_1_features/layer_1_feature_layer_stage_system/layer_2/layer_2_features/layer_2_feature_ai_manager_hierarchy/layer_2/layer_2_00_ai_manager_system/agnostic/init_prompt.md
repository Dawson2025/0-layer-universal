---
resource_id: "ea03f3bb-167f-4a90-a194-140bdf961374"
resource_type: "document"
resource_name: "init_prompt"
---
# Init Prompt - Agnostic Source

<!-- section_id: "1a515805-65d3-4bd6-8fdc-b66796b8552a" -->
## Purpose
Universal initialization context for any AI coding assistant.

<!-- section_id: "76f1aa19-69ff-40bd-aa39-60433dcdd0ef" -->
## Context Gathering
1. Identify current layer location
2. Read CLAUDE.md at entity root
3. Navigate to layer_N_00_ai_manager_system/agnostic/
4. Apply tool-agnostic instructions

<!-- section_id: "3f2a496f-1140-4882-8d03-c67cb7fad52f" -->
## Universal Instructions
- Follow layer navigation patterns
- Respect entity boundaries
- Apply stage-appropriate context
- Use standardized file patterns

<!-- section_id: "39f469c4-a196-4d75-980b-68aeae9c5f6c" -->
## Tool Resolution
After loading agnostic source, check for specific overrides at:
`layer_N_00_ai_manager_system/specific/os/{os}/environment/{env}/coding_app/{app}/ai_app/{ai}/`
