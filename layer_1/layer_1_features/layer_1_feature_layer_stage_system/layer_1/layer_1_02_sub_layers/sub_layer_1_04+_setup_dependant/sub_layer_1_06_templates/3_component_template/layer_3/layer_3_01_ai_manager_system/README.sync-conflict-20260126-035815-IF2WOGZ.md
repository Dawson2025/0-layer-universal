---
resource_id: "308e1e10-33fb-466e-a963-64ba94f5195c"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-035815-IF2WOGZ"
---
# Component Manager Agent (Template)

Purpose: Manages this component’s stage agents; reports upstream to the feature manager.

Fill in:
- Entry point (CLI/prompt/API) for this component manager.
- Upstream handoff: `../3.01_manager_handoff_documents/3.00_to_universal/` (to feature manager).
- Downstream handoff: `../3.01_manager_handoff_documents/3.01_to_specific/` (usually none; for sub-components if you create them).
- Stage agents: map stage id → `../../3.99_stages/stage_3.xx_*/ai_agent_system/` entrypoints.
