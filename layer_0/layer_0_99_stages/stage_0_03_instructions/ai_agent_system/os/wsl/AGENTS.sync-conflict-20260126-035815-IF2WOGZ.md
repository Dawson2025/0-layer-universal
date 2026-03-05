---
resource_id: "1b64b4af-0043-43b7-8e9d-aafda9c8e90c"
resource_type: "document"
resource_name: "AGENTS.sync-conflict-20260126-035815-IF2WOGZ"
---
# Agent Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: General Agents (Codex CLI, etc.)

---

<!-- section_id: "278434c5-0e4c-44f6-b2e3-6b8be4621278" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "d3c1ed37-11d2-4dbf-a0b9-52181f0ba22b" -->
## WSL-Specific Context for Worker Agents

<!-- section_id: "6f92ac67-959d-4f5f-8810-9476b7051abd" -->
### Shell Environment
- Default shell: bash (typically `/bin/bash`)
- Shell commands are Linux-style (ls, grep, find, etc.)
- PATH includes Linux binaries first, Windows binaries second

<!-- section_id: "a02348c8-78a9-417a-8562-336ef51a960f" -->
### Command Execution
- Use Linux command syntax (e.g., `ls -la`, not `dir`)
- Python invoked as `python3` (not `python.exe`)
- Node/npm use Linux versions from WSL environment
- Git commands use Linux-style paths

<!-- section_id: "1f51ea7f-53ca-4f1d-bf4b-adf1d110143d" -->
### File Operations
- Read/write to `/home/dawson/` filesystem (native Linux)
- Avoid `/mnt/c/` for performance-critical operations
- Use forward slashes in paths: `/home/dawson/code/`
- Line endings: prefer LF (Unix-style), avoid CRLF

<!-- section_id: "a04c061e-4fd4-4527-bae2-f098fee3bb21" -->
### Package Management
- `apt` for system packages
- `npm` for Node.js packages
- `pip` or `pip3` for Python packages
- No Windows-specific installers (.msi, .exe)

<!-- section_id: "26fe59d8-d9f2-43fd-a703-f5ddd162da86" -->
### Process Management
- Standard Linux process controls (ps, kill, bg, fg)
- Background jobs with `&` work normally
- No Windows Task Manager integration needed

<!-- section_id: "5b5c08fb-f996-4d7e-beb4-25204cba23dd" -->
### Common Pitfalls to Avoid
- Don't use Windows-style paths (C:\Users\...)
- Don't invoke .exe Windows binaries unless necessary
- Don't assume CRLF line endings
- Don't work in /mnt/c for primary development

---

<!-- section_id: "378cc275-1edb-493a-8c74-a979fc78fba9" -->
## Integration Notes

This context file:
- Is used as first user message for Codex CLI and similar worker agents
- Provides OS-specific execution context for short-lived tasks
- Works alongside `CLAUDE.md` (managers) and `GEMINI.md` (research/planning)

---

<!-- section_id: "428ec129-bc94-43be-99fa-f63af50b7227" -->
## Future Extensions

Add WSL-specific:
- Approved command patterns
- Interop scripts for Windows/Linux boundary
- Performance optimization commands
- Resource limit handling
