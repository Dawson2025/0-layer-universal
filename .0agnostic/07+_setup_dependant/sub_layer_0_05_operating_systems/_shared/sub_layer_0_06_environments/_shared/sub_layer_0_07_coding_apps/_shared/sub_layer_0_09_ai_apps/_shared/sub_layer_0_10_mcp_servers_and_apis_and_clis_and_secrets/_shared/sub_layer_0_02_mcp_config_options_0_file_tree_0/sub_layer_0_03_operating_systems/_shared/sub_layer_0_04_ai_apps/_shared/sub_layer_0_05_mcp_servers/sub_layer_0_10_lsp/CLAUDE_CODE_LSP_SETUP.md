---
resource_id: "69babb4e-f6fc-49ab-85db-dea718c9bca0"
resource_type: "document"
resource_name: "CLAUDE_CODE_LSP_SETUP"
---
# Claude Code LSP Support (Video Notes)

Source: https://www.youtube.com/watch?v=lffYEu5MhSQ

<!-- section_id: "750c7821-dac2-4e1a-83eb-83a663d38c22" -->
## Overview

Claude Code now has built-in Language Server Protocol (LSP) support. LSP lets Claude Code use language-aware features (find references, go to definition, rich symbol info) instead of relying on plain text search or grep. This makes code navigation and AI edits more accurate, especially in large repositories.

<!-- section_id: "4795486a-9de5-4e84-bb76-1b152a843d71" -->
## Why LSP Matters

- Better reference discovery than grep for questions like "find all references of this function".
- Faster, more precise symbol navigation across files.
- More reliable parameter and type information for non-strict languages like Python.

<!-- section_id: "2eb64a90-6a37-47bc-aa5f-feba267465a9" -->
## Quick Setup (Claude Code)

1. In Claude Code, run `/plugin`.
2. Find the LSP for your language (example in the video: Pyright for Python).
3. Install the plugin (user-local install is fine).
4. Restart Cloud Code.

If your language is not listed, use the linked documentation in the video description to add a custom LSP server.

<!-- section_id: "f8bf468d-b62c-4afb-a8a8-7032b081b64c" -->
## Common Issue Shown in the Video

- Error: "No LSP server is available for Python" and Claude Code falls back to grep.
- Fix: Install the language plugin (Pyright for Python) via `/plugin` and restart.

<!-- section_id: "c3fd588f-393d-44c6-8191-bd5ffdfb863f" -->
## Example Workflows (from the Video)

- Ask Claude Code: "Find all references in the codebase where this function is used" with LSP enabled.
- Use LSP to locate a function definition and navigate directly to it (like Ctrl+Click in an IDE).
- Ask: "What parameters does chat completions create accept?" and let LSP surface accurate parameter lists and descriptions.

<!-- section_id: "b1fe1099-929c-4f81-9166-8d8df651d054" -->
## Notes

- The presenter mentions a temporary issue in the latest Claude Code release and uses a specific version; by the time you watch, it may be fixed.
- Before built-in LSP support, the Serena MCP server was commonly used to expose language servers to AI editors. The video notes it is popular (17k+ GitHub stars) and works well for larger projects.
- Built-in LSP reduces the need to set up a separate MCP server for this capability.

<!-- section_id: "7f13c2dc-9d3d-41f1-8123-56d31d9723dc" -->
## Serena MCP Server (from the Video)

- Serena MCP is an MCP server that exposes LSP features to AI code editors (including Claude Code).
- The presenter has used it for months on larger, non-demo projects and finds it reliable.
- It has strong community adoption (17k+ GitHub stars mentioned in the video).
- With Claude Code's built-in LSP support, Serena MCP becomes optional rather than required.
- Repo: https://github.com/oraios/serena

<!-- section_id: "5a31206a-0608-4e45-b269-832cd07ce377" -->
## Key Takeaway

Enable a language server for your primary language so Cloud Code can use accurate symbol and type information. This improves navigation, reduces incorrect edits, and helps the AI generate more reliable code.
