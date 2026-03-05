---
resource_id: "b75b69cc-e073-4d09-9685-00020707f43a"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Claude Code Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions

---

<!-- section_id: "c2abfe47-9b2d-46ca-a4a0-6dfa6d04c425" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "2482477a-4c91-4453-b06c-82e15fd2405e" -->
## WSL-Specific Context for Claude Code

<!-- section_id: "33bafe9d-0de0-4f12-b25a-f7bdfe195ab3" -->
### Environment Detection
- Running in Windows Subsystem for Linux
- Check `WSL_DISTRO_NAME` environment variable
- Typically Ubuntu-based distribution
- Access to both Linux and Windows file systems

<!-- section_id: "cdf86bcd-20c4-4001-99ba-01ce899eccb3" -->
### Path Conventions
- **Linux paths**: `/home/dawson/...`
- **Windows paths accessible via**: `/mnt/c/Users/...`
- **WSL paths from Windows**: `\\wsl$\<distro>\...`
- **Project root**: `/home/dawson/code/0_layer_universal/`

<!-- section_id: "03044925-a5cd-46b7-b8b9-e678c63f7004" -->
### Tool Availability
- Standard Linux CLI tools available
- Some Windows tools accessible via `.exe` suffix
- Node.js, npm, Python typically installed in Linux environment
- Git configured for Linux-style line endings (LF)

<!-- section_id: "fbc792d1-14c4-482c-bf79-9b0b943f5133" -->
### Common WSL Quirks
- File permissions may differ between /mnt/c and native Linux filesystem
- Performance is better on native Linux filesystem (not /mnt/c)
- Windows Defender may scan WSL files (can cause slowness)
- `wsl.exe` command available to interact with Windows from Linux

<!-- section_id: "dddcc414-73b9-4e4f-be2c-a24140ca8ff7" -->
### Recommended Practices for This OS
- Prefer native Linux filesystem for code and development
- Use `/home/dawson/` paths, not `/mnt/c/` for primary work
- Be aware of line ending differences (CRLF vs LF)
- Use Linux-native package managers (apt, npm, pip)

---

<!-- section_id: "b325c051-349e-4941-bece-56610128d9bf" -->
## Integration Notes

This context file:
- Is loaded when Claude Code operates in WSL environment
- Supplements the generic Layer 0 instructions context
- May be overridden by more specific layer contexts (L1, L2, L3)
- Works in conjunction with `AGENTS.md` and `GEMINI.md` for other tools

---

<!-- section_id: "c5d7dd96-55bd-4368-9e11-d6a6b69ca81e" -->
## Future Extensions

Add WSL-specific:
- Environment variable requirements
- Interop commands for Windows/Linux boundary crossing
- Performance optimization notes
- Troubleshooting common WSL issues
