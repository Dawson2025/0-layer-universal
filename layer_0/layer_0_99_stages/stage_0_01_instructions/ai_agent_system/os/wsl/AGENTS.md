# Agent Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0.01_instructions
**Tool Context**: General Agents (Codex CLI, etc.)

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## WSL-Specific Context for Worker Agents

### Shell Environment
- Default shell: bash (typically `/bin/bash`)
- Shell commands are Linux-style (ls, grep, find, etc.)
- PATH includes Linux binaries first, Windows binaries second

### Command Execution
- Use Linux command syntax (e.g., `ls -la`, not `dir`)
- Python invoked as `python3` (not `python.exe`)
- Node/npm use Linux versions from WSL environment
- Git commands use Linux-style paths

### File Operations
- Read/write to `/home/dawson/` filesystem (native Linux)
- Avoid `/mnt/c/` for performance-critical operations
- Use forward slashes in paths: `/home/dawson/code/`
- Line endings: prefer LF (Unix-style), avoid CRLF

### Package Management
- `apt` for system packages
- `npm` for Node.js packages
- `pip` or `pip3` for Python packages
- No Windows-specific installers (.msi, .exe)

### Process Management
- Standard Linux process controls (ps, kill, bg, fg)
- Background jobs with `&` work normally
- No Windows Task Manager integration needed

### Common Pitfalls to Avoid
- Don't use Windows-style paths (C:\Users\...)
- Don't invoke .exe Windows binaries unless necessary
- Don't assume CRLF line endings
- Don't work in /mnt/c for primary development

---

## Integration Notes

This context file:
- Is used as first user message for Codex CLI and similar worker agents
- Provides OS-specific execution context for short-lived tasks
- Works alongside `CLAUDE.md` (managers) and `GEMINI.md` (research/planning)

---

## Future Extensions

Add WSL-specific:
- Approved command patterns
- Interop scripts for Windows/Linux boundary
- Performance optimization commands
- Resource limit handling
