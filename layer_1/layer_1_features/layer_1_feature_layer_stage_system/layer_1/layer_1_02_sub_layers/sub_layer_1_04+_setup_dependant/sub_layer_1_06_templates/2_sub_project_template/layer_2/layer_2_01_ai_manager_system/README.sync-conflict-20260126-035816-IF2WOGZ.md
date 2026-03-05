---
resource_id: "27e45bd6-1754-488b-84d3-d0060ca58ba7"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-035816-IF2WOGZ"
---
# Project Manager Agent (Template)

Purpose: Coordinates all feature managers for this project; delegates to project stage agents; reports upstream to the universal manager.

Fill in:
- Entry point (CLI/prompt/API) for this project manager.
- How to select which features/components are active.
- Upstream handoff: `../1.01_manager_handoff_documents/1.00_to_universal/` for rollups to universal manager.
- Downstream handoff: `../1.01_manager_handoff_documents/1.01_to_specific/` for packets to feature managers.
- Stage agents: map stage id → `../../1.99_stages/stage_1.xx_*/ai_agent_system/` entrypoints.
