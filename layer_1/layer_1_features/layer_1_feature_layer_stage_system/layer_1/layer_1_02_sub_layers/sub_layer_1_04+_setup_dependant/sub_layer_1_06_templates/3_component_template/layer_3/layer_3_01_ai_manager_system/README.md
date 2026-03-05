---
resource_id: "c479e09a-c94a-4a89-bb88-b961ee09d6a6"
resource_type: "readme
document"
resource_name: "README"
---
# Component Manager Agent (Template)

Purpose: Manages this component’s stage agents; reports upstream to the feature manager.

Fill in:
- Entry point (CLI/prompt/API) for this component manager.
- Upstream handoff: `../3.01_manager_handoff_documents/3.00_to_universal/` (to feature manager).
- Downstream handoff: `../3.01_manager_handoff_documents/3.01_to_specific/` (usually none; for sub-components if you create them).
- Stage agents: map stage id → `../../3.99_stages/stage_3.xx_*/ai_agent_system/` entrypoints.
