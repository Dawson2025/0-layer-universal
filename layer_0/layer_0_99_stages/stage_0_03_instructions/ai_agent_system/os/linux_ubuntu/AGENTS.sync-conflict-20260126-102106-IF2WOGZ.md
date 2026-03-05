---
resource_id: "d17ff3ba-b50b-4b72-91f7-ffb4485ffca8"
resource_type: "document"
resource_name: "AGENTS.sync-conflict-20260126-102106-IF2WOGZ"
---
# Agent Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: General Agents (Codex CLI, etc.)

---

<!-- section_id: "0777dd09-f238-4222-af12-3ab180a75c3f" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "36587da7-5746-415e-9c6f-f8e345561d55" -->
## Ubuntu-Specific Context for Worker Agents

<!-- section_id: "1be456f3-edbf-46e3-9d0a-2b488f44ecea" -->
### Shell Environment
- Default shell: bash (typically `/bin/bash`)
- Alternative shells available: zsh, fish, dash
- POSIX-compliant shell scripting
- Full GNU coreutils available

<!-- section_id: "edfd24c5-53e7-488c-a495-9b4fe70b0902" -->
### Command Execution
- Standard Linux command syntax
- Python invoked as `python3` (python2 may not be installed)
- Node/npm use native Linux builds
- Git with full Linux capabilities
- Package installation via `apt` or `snap`

<!-- section_id: "64f2c1f1-171b-420f-ab8f-a5e301dfc714" -->
### File Operations
- Native Linux filesystem (ext4, btrfs, xfs)
- Standard Unix permissions (owner, group, other)
- File paths: `/home/dawson/code/`
- Line endings: LF (Unix-style) only
- Symlinks work natively

<!-- section_id: "8805a74c-e8e4-4921-a7ef-c62f41073d3a" -->
### Package Management
- **System packages**: `apt update && apt install <package>`
- **Node.js**: npm for JavaScript packages
- **Python**: pip3 for Python packages
- **Snap**: `snap install <package>` for universal packages

<!-- section_id: "6a9eda10-dbab-4792-842b-e676c03a9e48" -->
### Process Management
- Standard Linux process model
- `ps aux` for process listing
- `kill`, `killall` for process termination
- `systemctl` for service management
- Background jobs with `&` and job control

<!-- section_id: "383526e4-4aec-4b51-92c5-b69d4048ab14" -->
### Performance Characteristics
- Native filesystem I/O (no translation layer)
- Direct system calls to Linux kernel
- Optimal for CPU and I/O intensive tasks
- No overhead from compatibility layers

<!-- section_id: "4d9498ce-0f9e-4411-846b-a23063691fee" -->
### Common Best Practices
- Use absolute paths when possible
- Verify file permissions before operations
- Use LF line endings exclusively
- Leverage native Linux tools for text processing
- Check exit codes: `$?`

---

<!-- section_id: "bd5f0472-c401-4f3e-9e6e-36d905455ab6" -->
## Integration Notes

This context file:
- Is used as first user message for Codex CLI and similar worker agents
- Provides OS-specific execution context for short-lived tasks
- Works alongside `CLAUDE.md` (managers) and `GEMINI.md` (research/planning)

---

<!-- section_id: "a883f15f-3c06-4aa5-a41c-7f84ecdcee2b" -->
## Future Extensions

Add Ubuntu-specific:
- Version-specific package names
- Systemd service patterns
- Security contexts (AppArmor profiles)
- Resource management (cgroups, limits)
