# Universal Setup Hierarchy System

This document describes how the universal setup hierarchy is structured and how to navigate it.

## Purpose

The hierarchy is a **traversable file tree** that lets you locate setup documentation by following a consistent path from operating system → environment → coding app → AI app → tool/model/protocol/agent setup.

## Core Path Pattern

Use the following path pattern for any setup configuration:

```
0.02_operating_systems/
  <os>/
    0.03_environments/
      <environment>/
        0.04_coding_apps/
          <coding_app>/
            0.05_ai_apps/
              <ai_app>/
                0.06_mcp_servers/
                  <mcp_server>/
                0.06_ai_models/
                  <model>/
                0.07_universal_tools/
                  _shared/
                0.08_protocols/
                0.09_agent_setup/
```

## Level Rules

- **Operating systems** are under `0.02_operating_systems/` (e.g., `wsl`, `linux_ubuntu`, `macos`, `windows`).
- **Environments** are currently `local` and `remote` (plus `_shared`).
- **Coding apps** contain editor/IDE choices (e.g., `cursor`) plus `_shared` for universal content.
- **AI apps** are the AI coding tools used inside a coding app (e.g., `claude_code_cli`, `codex_cli`, `gemini_cli`, `cursor_agent`).
- **MCP servers** and **AI models** are **siblings** at the same depth.
- **Universal tools**, **protocols**, and **agent setup** are **siblings** of MCP servers and AI models.

## _shared Conventions

- `_shared` directories store content that applies across all siblings at that level.
- Prefer `_shared` when content is not OS-, environment-, or app-specific.
- When content is specific, place it under the exact OS/environment/app path.

## Example

```
0.02_operating_systems/wsl/
  0.03_environments/local/
    0.04_coding_apps/cursor/
      0.05_ai_apps/claude_code_cli/
        0.06_mcp_servers/playwright-mcp/
```

## Integration Notes

- Legacy sublayer content is merged into the hierarchy under the closest matching level.
- When duplicate files exist, the hierarchy keeps both by appending a **Legacy Source** section.
- MCP server content is shared across all AI apps and OS branches when the source is OS-specific.
