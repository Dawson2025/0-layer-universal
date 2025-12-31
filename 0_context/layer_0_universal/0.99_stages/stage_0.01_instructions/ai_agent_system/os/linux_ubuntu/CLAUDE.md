# Claude Code Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0.01_instructions

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/dawson-workspace/code/0_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## Ubuntu-Specific Context for Claude Code

### Environment Detection
- Native Linux Ubuntu installation
- Check `OSTYPE` environment variable (should be `linux-gnu`)
- `lsb_release -a` shows Ubuntu version
- Full Linux kernel and userspace

### Path Conventions
- **Home directory**: `/home/dawson/...`
- **Project root**: `/home/dawson/dawson-workspace/code/0_ai_context/`
- **System paths**: `/usr/local/bin`, `/usr/bin`, `/bin`
- **Temporary files**: `/tmp/`

### Tool Availability
- Full Linux CLI toolchain (grep, sed, awk, find, etc.)
- APT package manager for system packages
- Node.js via nvm or apt
- Python 3 typically pre-installed
- Git with native Linux performance

### Ubuntu-Specific Features
- Systemd for service management
- Native Docker support (no WSL translation layer)
- Direct hardware access
- Standard Linux permissions model
- AppArmor security framework

### Performance Characteristics
- Native filesystem performance (ext4, btrfs, etc.)
- No Windows kernel translation overhead
- Direct kernel system calls
- Optimal for I/O-intensive operations

### Recommended Practices for This OS
- Use APT for system package management
- Store development files in home directory
- Use systemd for background services
- Follow XDG Base Directory Specification
- Use Linux-native line endings (LF)

---

## Integration Notes

This context file:
- Is loaded when Claude Code operates in native Ubuntu environment
- Supplements the generic Layer 0 instructions context
- May be overridden by more specific layer contexts (L1, L2, L3)
- Works in conjunction with `AGENTS.md` and `GEMINI.md` for other tools

---

## Future Extensions

Add Ubuntu-specific:
- Package management patterns (apt, snap)
- Systemd service configuration
- Security hardening notes (AppArmor, firewall)
- Distribution version-specific features
