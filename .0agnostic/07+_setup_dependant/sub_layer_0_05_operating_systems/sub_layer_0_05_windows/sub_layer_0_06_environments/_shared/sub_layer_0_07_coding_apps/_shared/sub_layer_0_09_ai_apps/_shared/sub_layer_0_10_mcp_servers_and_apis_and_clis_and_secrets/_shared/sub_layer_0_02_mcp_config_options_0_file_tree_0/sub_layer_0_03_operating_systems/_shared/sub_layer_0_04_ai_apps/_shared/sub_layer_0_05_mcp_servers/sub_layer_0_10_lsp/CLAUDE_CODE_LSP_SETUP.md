---
resource_id: "6430c288-c3cd-463f-a199-c258e7358ed3"
resource_type: "document"
resource_name: "CLAUDE_CODE_LSP_SETUP"
---
# Claude Code LSP Support (Video Notes)

Source: https://www.youtube.com/watch?v=lffYEu5MhSQ

<!-- section_id: "66484234-d4ae-4e38-868d-5e1cc7616972" -->
## Overview

Claude Code now has built-in Language Server Protocol (LSP) support. LSP lets Claude Code use language-aware features (find references, go to definition, rich symbol info) instead of relying on plain text search or grep. This makes code navigation and AI edits more accurate, especially in large repositories.

<!-- section_id: "2f977c8a-2cbb-4691-bf18-e64bcfe47cd5" -->
## Why LSP Matters

- Better reference discovery than grep for questions like "find all references of this function".
- Faster, more precise symbol navigation across files.
- More reliable parameter and type information for non-strict languages like Python.

<!-- section_id: "be8683f8-15c1-4b25-b974-1bc2c268d29c" -->
## Quick Setup (Claude Code)

1. In Claude Code, run `/plugin`.
2. Find the LSP for your language (example in the video: Pyright for Python).
3. Install the plugin (user-local install is fine).
4. Restart Cloud Code.

If your language is not listed, use the linked documentation in the video description to add a custom LSP server.

<!-- section_id: "79eecc97-8a94-44cd-83f2-6dbe39f6edab" -->
## Common Issue Shown in the Video

- Error: "No LSP server is available for Python" and Claude Code falls back to grep.
- Fix: Install the language plugin (Pyright for Python) via `/plugin` and restart.

<!-- section_id: "bb60d852-4a43-41c5-93dc-bd8bf5ecba44" -->
## Example Workflows (from the Video)

- Ask Claude Code: "Find all references in the codebase where this function is used" with LSP enabled.
- Use LSP to locate a function definition and navigate directly to it (like Ctrl+Click in an IDE).
- Ask: "What parameters does chat completions create accept?" and let LSP surface accurate parameter lists and descriptions.

<!-- section_id: "fda38c03-2967-4255-97ff-19a89f9979cd" -->
## Notes

- The presenter mentions a temporary issue in the latest Claude Code release and uses a specific version; by the time you watch, it may be fixed.
- Before built-in LSP support, the Serena MCP server was commonly used to expose language servers to AI editors. The video notes it is popular (17k+ GitHub stars) and works well for larger projects.
- Built-in LSP reduces the need to set up a separate MCP server for this capability.

<!-- section_id: "9f529f56-4e9d-4fa0-b82c-92117c5eb5d9" -->
## Serena MCP Server (from the Video)

- Serena MCP is an MCP server that exposes LSP features to AI code editors (including Claude Code).
- The presenter has used it for months on larger, non-demo projects and finds it reliable.
- It has strong community adoption (17k+ GitHub stars mentioned in the video).
- With Claude Code's built-in LSP support, Serena MCP becomes optional rather than required.
- Repo: https://github.com/oraios/serena

<!-- section_id: "c28b435c-a8e0-4e6c-8534-3177c709945b" -->
## Key Takeaway

Enable a language server for your primary language so Cloud Code can use accurate symbol and type information. This improves navigation, reduces incorrect edits, and helps the AI generate more reliable code.
