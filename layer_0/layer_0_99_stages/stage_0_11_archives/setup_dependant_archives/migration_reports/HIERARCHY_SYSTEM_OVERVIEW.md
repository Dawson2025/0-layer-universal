---
resource_id: "75c1c2c9-379e-4928-b41b-da23fbb119d6"
resource_type: "document"
resource_name: "HIERARCHY_SYSTEM_OVERVIEW"
---
# Universal Setup Hierarchy System

This document describes how the universal setup hierarchy is structured and how to navigate it.

<!-- section_id: "cb57e7b4-79aa-45e4-86b8-e313d59967ea" -->
## Purpose

The hierarchy is a **traversable file tree** that lets you locate setup documentation by following a consistent path from operating system → environment → coding app → AI app → tool/model/protocol/agent setup.

<!-- section_id: "3a5693d6-0f4a-4a2d-926d-75e0ad87cb2a" -->
## Core Path Pattern

Use the following path pattern for any setup configuration:

```
0.05_operating_systems/
  <os>/
    0.06_environments/
      <environment>/
        0.07_coding_apps/
          <coding_app>/
            0.09_ai_apps/
              <ai_app>/
                0.10_mcp_servers_and_apis_and_secrets/
                  <mcp_server>/
                0.11_ai_models/
                  <model>/
                0.12_universal_tools/
                  _shared/
                0.13_protocols/
                0.14_agent_setup/
```

<!-- section_id: "4181e98f-14f9-4955-8b4d-34b4d29cf2ac" -->
## Level Rules

- **Operating systems** are under `0.05_operating_systems/` (e.g., `wsl`, `linux_ubuntu`, `macos`, `windows`).
- **Environments** are currently `local` and `remote` (plus `_shared`).
- **Coding apps** contain editor/IDE choices (e.g., `cursor`) plus `_shared` for universal content.
- **AI apps** are the AI coding tools used inside a coding app (e.g., `claude_code_cli`, `codex_cli`, `gemini_cli`, `cursor_agent`).
- **MCP servers** and **AI models** are **siblings** at the same depth.
- **Universal tools**, **protocols**, and **agent setup** are **siblings** of MCP servers and AI models.

<!-- section_id: "18cdc8bd-81e7-4431-b06c-d17dd1713998" -->
## _shared Conventions

- `_shared` directories store content that applies across all siblings at that level.
- Prefer `_shared` when content is not OS-, environment-, or app-specific.
- When content is specific, place it under the exact OS/environment/app path.

<!-- section_id: "f4268087-8249-4176-a7d7-55b9afce31f5" -->
## Example

```
0.05_operating_systems/wsl/
  0.06_environments/local/
    0.07_coding_apps/cursor/
      0.09_ai_apps/claude_code_cli/
        0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/
```

<!-- section_id: "0459cb16-3b53-487b-a6b1-c36dba610a04" -->
## Integration Notes

- Legacy sublayer content is merged into the hierarchy under the closest matching level.
- When duplicate files exist, the hierarchy keeps both by appending a **Legacy Source** section.
- MCP server content is shared across all AI apps and OS branches when the source is OS-specific.
