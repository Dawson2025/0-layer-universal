---
resource_id: "b6261de7-ff38-4283-a608-cb5ea45c95eb"
resource_type: "document"
resource_name: "CLAUDE_CODE_LSP_SETUP"
---
# Claude Code LSP Support (Video Notes)

Source: https://www.youtube.com/watch?v=lffYEu5MhSQ

<!-- section_id: "58b96fd2-9053-436a-9b99-46c79ff43aeb" -->
## Overview

Claude Code now has built-in Language Server Protocol (LSP) support. LSP lets Claude Code use language-aware features (find references, go to definition, rich symbol info) instead of relying on plain text search or grep. This makes code navigation and AI edits more accurate, especially in large repositories.

<!-- section_id: "ead15984-936a-4be5-8033-250ce74c244e" -->
## Why LSP Matters

- Better reference discovery than grep for questions like "find all references of this function".
- Faster, more precise symbol navigation across files.
- More reliable parameter and type information for non-strict languages like Python.

<!-- section_id: "f8a7cc79-d705-464c-b101-e74f33c57258" -->
## Quick Setup (Claude Code)

1. In Claude Code, run `/plugin`.
2. Find the LSP for your language (example in the video: Pyright for Python).
3. Install the plugin (user-local install is fine).
4. Restart Cloud Code.

If your language is not listed, use the linked documentation in the video description to add a custom LSP server.

<!-- section_id: "2f1e5faf-0e33-46dd-9dcd-95ed52081bbd" -->
## Common Issue Shown in the Video

- Error: "No LSP server is available for Python" and Claude Code falls back to grep.
- Fix: Install the language plugin (Pyright for Python) via `/plugin` and restart.

<!-- section_id: "71c95309-088d-46f9-b9cd-4738102900c1" -->
## Example Workflows (from the Video)

- Ask Claude Code: "Find all references in the codebase where this function is used" with LSP enabled.
- Use LSP to locate a function definition and navigate directly to it (like Ctrl+Click in an IDE).
- Ask: "What parameters does chat completions create accept?" and let LSP surface accurate parameter lists and descriptions.

<!-- section_id: "ee737a8f-ebc8-432f-b8ea-b2e4aef0def4" -->
## Notes

- The presenter mentions a temporary issue in the latest Claude Code release and uses a specific version; by the time you watch, it may be fixed.
- Before built-in LSP support, the Serena MCP server was commonly used to expose language servers to AI editors. The video notes it is popular (17k+ GitHub stars) and works well for larger projects.
- Built-in LSP reduces the need to set up a separate MCP server for this capability.

<!-- section_id: "d706fbf5-9fd4-407d-b843-7b1ee81c840b" -->
## Serena MCP Server (from the Video)

- Serena MCP is an MCP server that exposes LSP features to AI code editors (including Claude Code).
- The presenter has used it for months on larger, non-demo projects and finds it reliable.
- It has strong community adoption (17k+ GitHub stars mentioned in the video).
- With Claude Code's built-in LSP support, Serena MCP becomes optional rather than required.
- Repo: https://github.com/oraios/serena

<!-- section_id: "df186bfb-17bb-419d-b2ca-09b4fe018492" -->
## Key Takeaway

Enable a language server for your primary language so Cloud Code can use accurate symbol and type information. This improves navigation, reduces incorrect edits, and helps the AI generate more reliable code.
