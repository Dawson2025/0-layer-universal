---
resource_id: "78a70854-5829-4061-8d53-84b11412be84"
resource_type: "document"
resource_name: "HIERARCHY_SYSTEM_OVERVIEW.sync-conflict-20260126-035815-IF2WOGZ"
---
# Universal Setup Hierarchy System

This document describes how the universal setup hierarchy is structured and how to navigate it.

<!-- section_id: "6a56f5bf-6ad3-4944-a5d6-07e64c591470" -->
## Purpose

The hierarchy is a **traversable file tree** that lets you locate setup documentation by following a consistent path from operating system → environment → coding app → AI app → tool/model/protocol/agent setup.

<!-- section_id: "6e235914-8458-46c5-949e-d3bdad713c5b" -->
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

<!-- section_id: "d1c943cb-4d2b-4d94-baf6-9e3245f4cea0" -->
## Level Rules

- **Operating systems** are under `0.05_operating_systems/` (e.g., `wsl`, `linux_ubuntu`, `macos`, `windows`).
- **Environments** are currently `local` and `remote` (plus `_shared`).
- **Coding apps** contain editor/IDE choices (e.g., `cursor`) plus `_shared` for universal content.
- **AI apps** are the AI coding tools used inside a coding app (e.g., `claude_code_cli`, `codex_cli`, `gemini_cli`, `cursor_agent`).
- **MCP servers** and **AI models** are **siblings** at the same depth.
- **Universal tools**, **protocols**, and **agent setup** are **siblings** of MCP servers and AI models.

<!-- section_id: "32d9360b-9b24-4b48-be93-27277ff77376" -->
## _shared Conventions

- `_shared` directories store content that applies across all siblings at that level.
- Prefer `_shared` when content is not OS-, environment-, or app-specific.
- When content is specific, place it under the exact OS/environment/app path.

<!-- section_id: "1b5636e0-63c8-4e6d-b467-3a5b3fb5ce39" -->
## Example

```
0.05_operating_systems/wsl/
  0.06_environments/local/
    0.07_coding_apps/cursor/
      0.09_ai_apps/claude_code_cli/
        0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/
```

<!-- section_id: "d4546818-3601-4040-8c02-dee165674c0c" -->
## Integration Notes

- Legacy sublayer content is merged into the hierarchy under the closest matching level.
- When duplicate files exist, the hierarchy keeps both by appending a **Legacy Source** section.
- MCP server content is shared across all AI apps and OS branches when the source is OS-specific.
