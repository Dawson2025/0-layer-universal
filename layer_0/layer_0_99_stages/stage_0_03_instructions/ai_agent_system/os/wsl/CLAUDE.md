# Claude Code Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## WSL-Specific Context for Claude Code

### Environment Detection
- Running in Windows Subsystem for Linux
- Check `WSL_DISTRO_NAME` environment variable
- Typically Ubuntu-based distribution
- Access to both Linux and Windows file systems

### Path Conventions
- **Linux paths**: `/home/dawson/...`
- **Windows paths accessible via**: `/mnt/c/Users/...`
- **WSL paths from Windows**: `\\wsl$\<distro>\...`
- **Project root**: `/home/dawson/code/0_layer_universal/`

### Tool Availability
- Standard Linux CLI tools available
- Some Windows tools accessible via `.exe` suffix
- Node.js, npm, Python typically installed in Linux environment
- Git configured for Linux-style line endings (LF)

### Common WSL Quirks
- File permissions may differ between /mnt/c and native Linux filesystem
- Performance is better on native Linux filesystem (not /mnt/c)
- Windows Defender may scan WSL files (can cause slowness)
- `wsl.exe` command available to interact with Windows from Linux

### Recommended Practices for This OS
- Prefer native Linux filesystem for code and development
- Use `/home/dawson/` paths, not `/mnt/c/` for primary work
- Be aware of line ending differences (CRLF vs LF)
- Use Linux-native package managers (apt, npm, pip)

---

## Integration Notes

This context file:
- Is loaded when Claude Code operates in WSL environment
- Supplements the generic Layer 0 instructions context
- May be overridden by more specific layer contexts (L1, L2, L3)
- Works in conjunction with `AGENTS.md` and `GEMINI.md` for other tools

---

## Future Extensions

Add WSL-specific:
- Environment variable requirements
- Interop commands for Windows/Linux boundary crossing
- Performance optimization notes
- Troubleshooting common WSL issues
