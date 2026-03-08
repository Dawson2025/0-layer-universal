---
resource_id: "106287ad-f8eb-412a-9a07-6ba1eea1623e"
resource_type: "readme_document"
resource_name: "README"
---
# Universal Manager Agent (Template)

Purpose: Coordinates all project managers, decides which project(s) to activate, and delegates to universal stage agents as needed.

Fill in:
- Contact/entrypoint for this manager (CLI command, prompt, API call, etc.).
- How it discovers active projects (agent registry path, selection rules).
- Escalation/rollup path: `../0.01_manager_handoff_documents/0.00_to_universal/` (usually unused at universal).
- Downstream path: `../0.01_manager_handoff_documents/0.01_to_specific/` (for packets to project managers).
- Stage agents: map stage id → `../../0.99_stages/stage_0_xx_*/ai_agent_system/` entrypoints.
