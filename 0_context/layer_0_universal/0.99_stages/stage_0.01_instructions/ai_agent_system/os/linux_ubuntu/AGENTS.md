# Agent Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0.01_instructions
**Tool Context**: General Agents (Codex CLI, etc.)

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## Ubuntu-Specific Context for Worker Agents

### Shell Environment
- Default shell: bash (typically `/bin/bash`)
- Alternative shells available: zsh, fish, dash
- POSIX-compliant shell scripting
- Full GNU coreutils available

### Command Execution
- Standard Linux command syntax
- Python invoked as `python3` (python2 may not be installed)
- Node/npm use native Linux builds
- Git with full Linux capabilities
- Package installation via `apt` or `snap`

### File Operations
- Native Linux filesystem (ext4, btrfs, xfs)
- Standard Unix permissions (owner, group, other)
- File paths: `/home/dawson/code/`
- Line endings: LF (Unix-style) only
- Symlinks work natively

### Package Management
- **System packages**: `apt update && apt install <package>`
- **Node.js**: npm for JavaScript packages
- **Python**: pip3 for Python packages
- **Snap**: `snap install <package>` for universal packages

### Process Management
- Standard Linux process model
- `ps aux` for process listing
- `kill`, `killall` for process termination
- `systemctl` for service management
- Background jobs with `&` and job control

### Performance Characteristics
- Native filesystem I/O (no translation layer)
- Direct system calls to Linux kernel
- Optimal for CPU and I/O intensive tasks
- No overhead from compatibility layers

### Common Best Practices
- Use absolute paths when possible
- Verify file permissions before operations
- Use LF line endings exclusively
- Leverage native Linux tools for text processing
- Check exit codes: `$?`

---

## Integration Notes

This context file:
- Is used as first user message for Codex CLI and similar worker agents
- Provides OS-specific execution context for short-lived tasks
- Works alongside `CLAUDE.md` (managers) and `GEMINI.md` (research/planning)

---

## Future Extensions

Add Ubuntu-specific:
- Version-specific package names
- Systemd service patterns
- Security contexts (AppArmor profiles)
- Resource management (cgroups, limits)
