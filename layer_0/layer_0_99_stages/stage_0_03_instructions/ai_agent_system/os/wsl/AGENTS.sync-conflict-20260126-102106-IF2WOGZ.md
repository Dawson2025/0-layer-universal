---
resource_id: "f766b26f-7113-4f4d-9e8b-ff18339ff562"
resource_type: "document"
resource_name: "AGENTS.sync-conflict-20260126-102106-IF2WOGZ"
---
# Agent Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: General Agents (Codex CLI, etc.)

---

<!-- section_id: "99beb840-1f60-4c62-ad64-203d067694ab" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "180eeb44-eb13-45c3-8847-1f8ede67ae97" -->
## WSL-Specific Context for Worker Agents

<!-- section_id: "5002db60-0b91-4ea3-a3bc-140a0fe998ee" -->
### Shell Environment
- Default shell: bash (typically `/bin/bash`)
- Shell commands are Linux-style (ls, grep, find, etc.)
- PATH includes Linux binaries first, Windows binaries second

<!-- section_id: "06536071-20a5-427b-a81a-235098d1deb6" -->
### Command Execution
- Use Linux command syntax (e.g., `ls -la`, not `dir`)
- Python invoked as `python3` (not `python.exe`)
- Node/npm use Linux versions from WSL environment
- Git commands use Linux-style paths

<!-- section_id: "a353c17a-ebe3-446b-89b2-7b46bd597ccd" -->
### File Operations
- Read/write to `/home/dawson/` filesystem (native Linux)
- Avoid `/mnt/c/` for performance-critical operations
- Use forward slashes in paths: `/home/dawson/code/`
- Line endings: prefer LF (Unix-style), avoid CRLF

<!-- section_id: "cbf651d5-6726-41cf-b047-2c5c4796faef" -->
### Package Management
- `apt` for system packages
- `npm` for Node.js packages
- `pip` or `pip3` for Python packages
- No Windows-specific installers (.msi, .exe)

<!-- section_id: "43994e89-818e-4a4a-82a7-bd427d765b5e" -->
### Process Management
- Standard Linux process controls (ps, kill, bg, fg)
- Background jobs with `&` work normally
- No Windows Task Manager integration needed

<!-- section_id: "aab6c6a6-f94f-426c-9ab1-809b4961bcd5" -->
### Common Pitfalls to Avoid
- Don't use Windows-style paths (C:\Users\...)
- Don't invoke .exe Windows binaries unless necessary
- Don't assume CRLF line endings
- Don't work in /mnt/c for primary development

---

<!-- section_id: "c3145c37-2fa2-427d-a93a-0645f4de487b" -->
## Integration Notes

This context file:
- Is used as first user message for Codex CLI and similar worker agents
- Provides OS-specific execution context for short-lived tasks
- Works alongside `CLAUDE.md` (managers) and `GEMINI.md` (research/planning)

---

<!-- section_id: "5f84b367-c6e2-47d5-b674-2c75c7f71573" -->
## Future Extensions

Add WSL-specific:
- Approved command patterns
- Interop scripts for Windows/Linux boundary
- Performance optimization commands
- Resource limit handling
