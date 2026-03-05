---
resource_id: "9847559d-a7dc-488b-8251-c7dee7c0e4af"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-035814-IF2WOGZ"
---
# Claude Code Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions

---

<!-- section_id: "f4289b95-c15e-4966-a2fe-244e5f75c0fe" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "1b2d4c2d-57d0-4753-ac8e-7766771cb527" -->
## Ubuntu-Specific Context for Claude Code

<!-- section_id: "cd10f4b5-b5ac-467c-9f92-c6f1169b46b2" -->
### Environment Detection
- Native Linux Ubuntu installation
- Check `OSTYPE` environment variable (should be `linux-gnu`)
- `lsb_release -a` shows Ubuntu version
- Full Linux kernel and userspace

<!-- section_id: "870bdee5-08f8-484d-8dc8-d107ea56513a" -->
### Path Conventions
- **Home directory**: `/home/dawson/...`
- **Project root**: `/home/dawson/code/0_layer_universal/`
- **System paths**: `/usr/local/bin`, `/usr/bin`, `/bin`
- **Temporary files**: `/tmp/`

<!-- section_id: "4b12f7b0-ca36-484e-b862-171c6f0411a8" -->
### Tool Availability
- Full Linux CLI toolchain (grep, sed, awk, find, etc.)
- APT package manager for system packages
- Node.js via nvm or apt
- Python 3 typically pre-installed
- Git with native Linux performance

<!-- section_id: "e16f61fc-d62e-4dac-8a1f-fb147ba9534f" -->
### Ubuntu-Specific Features
- Systemd for service management
- Native Docker support (no WSL translation layer)
- Direct hardware access
- Standard Linux permissions model
- AppArmor security framework

<!-- section_id: "859df4b9-99b0-406e-8757-9a5489a04b10" -->
### Performance Characteristics
- Native filesystem performance (ext4, btrfs, etc.)
- No Windows kernel translation overhead
- Direct kernel system calls
- Optimal for I/O-intensive operations

<!-- section_id: "f073ec9c-7914-4075-9e71-3c9d3390cb63" -->
### Recommended Practices for This OS
- Use APT for system package management
- Store development files in home directory
- Use systemd for background services
- Follow XDG Base Directory Specification
- Use Linux-native line endings (LF)

---

<!-- section_id: "b34d7d56-72ee-4701-a668-b6c3e79f9915" -->
## Integration Notes

This context file:
- Is loaded when Claude Code operates in native Ubuntu environment
- Supplements the generic Layer 0 instructions context
- May be overridden by more specific layer contexts (L1, L2, L3)
- Works in conjunction with `AGENTS.md` and `GEMINI.md` for other tools

---

<!-- section_id: "790908cd-2c9d-4752-886d-86283130e807" -->
## Future Extensions

Add Ubuntu-specific:
- Package management patterns (apt, snap)
- Systemd service configuration
- Security hardening notes (AppArmor, firewall)
- Distribution version-specific features
