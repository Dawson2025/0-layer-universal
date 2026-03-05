---
resource_id: "98343033-1f50-44bd-9cdc-969a8b0252f0"
resource_type: "document"
resource_name: "AGENTS.sync-conflict-20260126-035814-IF2WOGZ"
---
# Agent Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: General Agents (Codex CLI, etc.)

---

<!-- section_id: "72f04597-0817-4348-9bec-e6a2aaee4101" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "90878d5b-73c2-4f40-80aa-f8673ec7f856" -->
## Ubuntu-Specific Context for Worker Agents

<!-- section_id: "7f157e09-1764-456a-aad6-c226b9eb447b" -->
### Shell Environment
- Default shell: bash (typically `/bin/bash`)
- Alternative shells available: zsh, fish, dash
- POSIX-compliant shell scripting
- Full GNU coreutils available

<!-- section_id: "69cc6bd0-1681-44a0-82b6-59de9316ad8e" -->
### Command Execution
- Standard Linux command syntax
- Python invoked as `python3` (python2 may not be installed)
- Node/npm use native Linux builds
- Git with full Linux capabilities
- Package installation via `apt` or `snap`

<!-- section_id: "6b355759-082e-478c-ae0f-40163827d36d" -->
### File Operations
- Native Linux filesystem (ext4, btrfs, xfs)
- Standard Unix permissions (owner, group, other)
- File paths: `/home/dawson/code/`
- Line endings: LF (Unix-style) only
- Symlinks work natively

<!-- section_id: "0fc62720-e40e-4395-a28b-09c33ff658b4" -->
### Package Management
- **System packages**: `apt update && apt install <package>`
- **Node.js**: npm for JavaScript packages
- **Python**: pip3 for Python packages
- **Snap**: `snap install <package>` for universal packages

<!-- section_id: "6f6bb43a-616f-4cfd-968a-0ca247898f09" -->
### Process Management
- Standard Linux process model
- `ps aux` for process listing
- `kill`, `killall` for process termination
- `systemctl` for service management
- Background jobs with `&` and job control

<!-- section_id: "92be7d20-f991-4c6d-b4a8-d7482bfa201f" -->
### Performance Characteristics
- Native filesystem I/O (no translation layer)
- Direct system calls to Linux kernel
- Optimal for CPU and I/O intensive tasks
- No overhead from compatibility layers

<!-- section_id: "f3708358-975b-4a23-92e3-04445472e8da" -->
### Common Best Practices
- Use absolute paths when possible
- Verify file permissions before operations
- Use LF line endings exclusively
- Leverage native Linux tools for text processing
- Check exit codes: `$?`

---

<!-- section_id: "b78cd485-6110-45f9-b4b6-dcc710b24d5d" -->
## Integration Notes

This context file:
- Is used as first user message for Codex CLI and similar worker agents
- Provides OS-specific execution context for short-lived tasks
- Works alongside `CLAUDE.md` (managers) and `GEMINI.md` (research/planning)

---

<!-- section_id: "4f7e3399-7c79-405e-836b-3a43cd3fdc46" -->
## Future Extensions

Add Ubuntu-specific:
- Version-specific package names
- Systemd service patterns
- Security contexts (AppArmor profiles)
- Resource management (cgroups, limits)
