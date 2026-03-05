---
resource_id: "d11b5109-efd0-4f07-84d8-b2e3e367ce07"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Claude Code Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions

---

<!-- section_id: "8d287631-a9b9-46ae-971e-7d5b4da47e60" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "d3ea8ff0-75ef-438c-94c1-a65cf2a2cbe1" -->
## Ubuntu-Specific Context for Claude Code

<!-- section_id: "27268a4a-e392-4cc8-aec6-b96735ca979e" -->
### Environment Detection
- Native Linux Ubuntu installation
- Check `OSTYPE` environment variable (should be `linux-gnu`)
- `lsb_release -a` shows Ubuntu version
- Full Linux kernel and userspace

<!-- section_id: "f99a2f58-13aa-43fa-8dde-daec7062eb95" -->
### Path Conventions
- **Home directory**: `/home/dawson/...`
- **Project root**: `/home/dawson/code/0_layer_universal/`
- **System paths**: `/usr/local/bin`, `/usr/bin`, `/bin`
- **Temporary files**: `/tmp/`

<!-- section_id: "a9caa767-40eb-469c-b804-80da4f535899" -->
### Tool Availability
- Full Linux CLI toolchain (grep, sed, awk, find, etc.)
- APT package manager for system packages
- Node.js via nvm or apt
- Python 3 typically pre-installed
- Git with native Linux performance

<!-- section_id: "af39ff0a-7f0b-441c-acaa-f38c7583f5c0" -->
### Ubuntu-Specific Features
- Systemd for service management
- Native Docker support (no WSL translation layer)
- Direct hardware access
- Standard Linux permissions model
- AppArmor security framework

<!-- section_id: "d05bb8e4-4461-457c-8896-cd083f80135e" -->
### Performance Characteristics
- Native filesystem performance (ext4, btrfs, etc.)
- No Windows kernel translation overhead
- Direct kernel system calls
- Optimal for I/O-intensive operations

<!-- section_id: "ef17647c-174f-4396-81e7-964114bb6752" -->
### Recommended Practices for This OS
- Use APT for system package management
- Store development files in home directory
- Use systemd for background services
- Follow XDG Base Directory Specification
- Use Linux-native line endings (LF)

---

<!-- section_id: "0fece81a-3280-44d3-bf1c-8f9be1946ec1" -->
## Integration Notes

This context file:
- Is loaded when Claude Code operates in native Ubuntu environment
- Supplements the generic Layer 0 instructions context
- May be overridden by more specific layer contexts (L1, L2, L3)
- Works in conjunction with `AGENTS.md` and `GEMINI.md` for other tools

---

<!-- section_id: "d7afba93-cb01-4d9b-8c2c-31eda2317e1b" -->
## Future Extensions

Add Ubuntu-specific:
- Package management patterns (apt, snap)
- Systemd service configuration
- Security hardening notes (AppArmor, firewall)
- Distribution version-specific features
