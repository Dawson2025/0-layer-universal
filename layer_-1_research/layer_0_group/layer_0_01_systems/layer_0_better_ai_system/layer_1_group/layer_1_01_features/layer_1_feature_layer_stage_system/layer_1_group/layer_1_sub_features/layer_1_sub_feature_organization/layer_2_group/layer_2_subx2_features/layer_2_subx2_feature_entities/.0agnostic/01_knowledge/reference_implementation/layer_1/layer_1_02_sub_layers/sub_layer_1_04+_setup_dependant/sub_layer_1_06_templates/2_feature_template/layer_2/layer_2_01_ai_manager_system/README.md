---
resource_id: "6398ce16-4fb9-4a20-be04-537f986012e3"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Feature Manager Agent (Template)

Purpose: Coordinates all component managers for this feature; delegates to feature stage agents; reports upstream to the project manager.

Fill in:
- Entry point (CLI/prompt/API) for this feature manager.
- Upstream handoff: `../2.01_manager_handoff_documents/2.00_to_universal/` (to project manager).
- Downstream handoff: `../2.01_manager_handoff_documents/2.01_to_specific/` (to component managers).
- Stage agents: map stage id → `../../2.99_stages/stage_2.xx_*/ai_agent_system/` entrypoints.
