# Agent Registry Template

Use this file (copy/rename to your repo, e.g., `agent_registry.md`) to register manager and stage agents so the universal manager knows where to find and call them.

## Context: AI Setup Dependency Chain

Agents depend on the AI setup dependency chain in the universal layer (0.09–0.13):
- **0.09 AI Apps/Tools Setup**: Agents run within AI applications (Cursor IDE, Claude Code, etc.)
- **0.10 MCP Servers and Tools Setup**: Agents use MCP servers for capabilities (browser automation, documentation, etc.)
- **0.11 AI Models**: Agents require AI models to function
- **0.12 Universal Tools**: Agents use universal tools for capabilities (browser automation, development frameworks, etc.)
- **0.13 Agent Setup**: Agent configuration with model fallbacks, MCP integration, and tool access

When registering agents, ensure the AI setup layers (0.09–0.13) are configured before agents can be invoked.

## Required entries
- **layer**: `0|1|2|3`
- **name**: human-friendly label (e.g., `universal_manager`, `project_checkout_manager`).
- **manager_path**: path to the manager folder (e.g., `layer_1_project/1.00_ai_manager_system/`).
- **handoff_up**: path to `<N>.01_manager_handoff_documents/<N>.00_to_universal/`.
- **handoff_down**: path to `<N>.01_manager_handoff_documents/<N>.01_to_specific/`.
- **stages_root**: path to `<N>.99_stages/`.
- **stage_agents**: list of stage agent entries with stage id and location.
- **invoke_notes**: how to call the manager/stage agents (CLI/API prompt patterns).

## Example (YAML)
```
- layer: 0
  name: universal_manager
  manager_path: layer_0_universal/0.00_ai_manager_system/
  handoff_up: null
  handoff_down: layer_0_universal/0.01_manager_handoff_documents/0.01_to_specific/
  stages_root: layer_0_universal/0.99_stages/
  stage_agents:
    - id: stage_0.01_instructions
      path: layer_0_universal/0.99_stages/stage_0.01_instructions/ai_agent_system/
    - id: stage_0.02_planning
      path: layer_0_universal/0.99_stages/stage_0.02_planning/ai_agent_system/
  invoke_notes: |
    - Call via: "run universal manager, then delegate to stage agent <id>".
    - Upstream handoff: not applicable.
    - Downstream handoff: drop packets in 0.01_to_specific/ for project managers.

- layer: 1
  name: project_manager_checkout
  manager_path: layer_1_project/1.00_ai_manager_system/
  handoff_up: layer_1_project/1.01_manager_handoff_documents/1.00_to_universal/
  handoff_down: layer_1_project/1.01_manager_handoff_documents/1.01_to_specific/
  stages_root: layer_1_project/1.99_stages/
  stage_agents:
    - id: stage_1.01_instructions
      path: layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/
  invoke_notes: |
    - Called by universal manager when this project is active.
    - For feature delegation, place packets in 1.01_to_specific/.
```

## Agent Configuration and Model Fallbacks

When configuring agents in the registry, consider:

- **Model Selection**: Agents should specify primary models and fallback order (see `sub_layer_0.13_agent_setup`)
- **MCP Integration**: Agents may depend on specific MCP servers configured in `sub_layer_0.10_mcp_servers_and_tools_setup`
- **Tool Access**: Agents may use universal tools from `sub_layer_0.12_universal_tools`
- **App Context**: Agents run within AI applications configured in `sub_layer_0.09_ai_apps_tools_setup`

Example agent configuration with model fallbacks:
```yaml
invoke_notes: |
  - Primary model: Claude Sonnet 4.5
  - Fallback order: Claude Sonnet 4.0 → GPT-4 → Claude Haiku
  - MCP servers: browser-automation (Playwright), documentation (Context7)
  - App context: Cursor IDE
```

## Usage
1) Copy this template to your repo (e.g., `agent_registry.yaml`).
2) Ensure AI setup layers (0.09–0.13) are configured before registering agents.
3) Fill entries for every manager agent you will use in the session.
4) Specify model fallbacks and MCP dependencies in `invoke_notes`.
5) Keep it near the top-level context (e.g., next to `MASTER_DOCUMENTATION_INDEX.md`) so universal manager can load it first.
