---
resource_id: "84747f82-8d8c-4032-8e46-26fe46958447"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-102026-IF2WOGZ"
---
# Universal Manager Agent (Template)

Purpose: Coordinates all project managers, decides which project(s) to activate, and delegates to universal stage agents as needed.

Fill in:
- Contact/entrypoint for this manager (CLI command, prompt, API call, etc.).
- How it discovers active projects (agent registry path, selection rules).
- Escalation/rollup path: `../0.01_manager_handoff_documents/0.00_to_universal/` (usually unused at universal).
- Downstream path: `../0.01_manager_handoff_documents/0.01_to_specific/` (for packets to project managers).
- Stage agents: map stage id → `../../0.99_stages/stage_0_xx_*/ai_agent_system/` entrypoints.
