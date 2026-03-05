---
resource_id: "bf2fbe17-3f2f-4d1e-9551-583cee81eae1"
resource_type: "knowledge"
resource_name: "init_prompt"
---
# Init Prompt - Agnostic Source

<!-- section_id: "0c90438a-317d-42bf-8294-9f232fd301b7" -->
## Purpose
Universal initialization context for any AI coding assistant.

<!-- section_id: "ed7f61d6-cf3c-497d-85f9-f9c17a0ba7af" -->
## Context Gathering
1. Identify current layer location
2. Read CLAUDE.md at entity root
3. Navigate to layer_N_00_ai_manager_system/agnostic/
4. Apply tool-agnostic instructions

<!-- section_id: "179402b1-a0ed-41c5-bcb9-c609e6cc4b8c" -->
## Universal Instructions
- Follow layer navigation patterns
- Respect entity boundaries
- Apply stage-appropriate context
- Use standardized file patterns

<!-- section_id: "7850a926-5f33-4bea-af70-af90d43652cb" -->
## Tool Resolution
After loading agnostic source, check for specific overrides at:
`layer_N_00_ai_manager_system/specific/os/{os}/environment/{env}/coding_app/{app}/ai_app/{ai}/`
