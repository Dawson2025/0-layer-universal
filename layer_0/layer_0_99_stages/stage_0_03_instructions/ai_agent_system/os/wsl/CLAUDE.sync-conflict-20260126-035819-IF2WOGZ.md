---
resource_id: "de897cc3-0c1d-4497-bac1-228ba6c739c5"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-035819-IF2WOGZ"
---
# Claude Code Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions

---

<!-- section_id: "b43cb56d-1aad-4f3b-90ac-2ab66f86b24f" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "d111b0d2-bafb-4543-9f52-1849c1e4931c" -->
## WSL-Specific Context for Claude Code

<!-- section_id: "cfe5e12e-1ce3-4ed8-8fe1-694c40ba729e" -->
### Environment Detection
- Running in Windows Subsystem for Linux
- Check `WSL_DISTRO_NAME` environment variable
- Typically Ubuntu-based distribution
- Access to both Linux and Windows file systems

<!-- section_id: "62050ff0-1a54-4d97-b502-cdf42f14c4e4" -->
### Path Conventions
- **Linux paths**: `/home/dawson/...`
- **Windows paths accessible via**: `/mnt/c/Users/...`
- **WSL paths from Windows**: `\\wsl$\<distro>\...`
- **Project root**: `/home/dawson/code/0_layer_universal/`

<!-- section_id: "b9d535b5-aab9-4663-a887-14fca5ca8d29" -->
### Tool Availability
- Standard Linux CLI tools available
- Some Windows tools accessible via `.exe` suffix
- Node.js, npm, Python typically installed in Linux environment
- Git configured for Linux-style line endings (LF)

<!-- section_id: "54dabd19-e11e-42fa-a77d-73dbaaa30549" -->
### Common WSL Quirks
- File permissions may differ between /mnt/c and native Linux filesystem
- Performance is better on native Linux filesystem (not /mnt/c)
- Windows Defender may scan WSL files (can cause slowness)
- `wsl.exe` command available to interact with Windows from Linux

<!-- section_id: "df7137bf-17d2-4b8f-9391-305429b62cc6" -->
### Recommended Practices for This OS
- Prefer native Linux filesystem for code and development
- Use `/home/dawson/` paths, not `/mnt/c/` for primary work
- Be aware of line ending differences (CRLF vs LF)
- Use Linux-native package managers (apt, npm, pip)

---

<!-- section_id: "e28ff393-615b-4bbb-85fd-c7d356a552f8" -->
## Integration Notes

This context file:
- Is loaded when Claude Code operates in WSL environment
- Supplements the generic Layer 0 instructions context
- May be overridden by more specific layer contexts (L1, L2, L3)
- Works in conjunction with `AGENTS.md` and `GEMINI.md` for other tools

---

<!-- section_id: "ea2c75ed-30bf-488d-abd4-3ff31cb62ea9" -->
## Future Extensions

Add WSL-specific:
- Environment variable requirements
- Interop commands for Windows/Linux boundary crossing
- Performance optimization notes
- Troubleshooting common WSL issues
