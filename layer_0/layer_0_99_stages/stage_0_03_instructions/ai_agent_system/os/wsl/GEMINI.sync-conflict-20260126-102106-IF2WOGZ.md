---
resource_id: "7603eb8e-75f2-40ce-92dd-01cd862e368b"
resource_type: "document"
resource_name: "GEMINI.sync-conflict-20260126-102106-IF2WOGZ"
---
# Gemini CLI Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: Gemini CLI (research, planning, long reasoning)

---

<!-- section_id: "48707d12-e054-4a2c-8c01-dacb629a0e87" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "e4339345-990c-4548-afcc-a3d0ef44fde0" -->
## WSL-Specific Context for Gemini CLI

<!-- section_id: "66e96126-a984-4a9f-9041-bf67d3c63a7d" -->
### Environment Overview
- WSL provides a Linux environment running on Windows kernel
- Hybrid architecture: Linux userspace + Windows kernel + Windows filesystem access
- Suitable for long-form research and planning tasks that span both ecosystems

<!-- section_id: "5f7d009f-c975-48e1-be60-4dfe671d66b5" -->
### File System Considerations
- **Primary workspace**: `/home/dawson/code/` (native Linux filesystem)
- **Windows access**: `/mnt/c/`, `/mnt/d/`, etc.
- **Performance**: Native Linux filesystem significantly faster than /mnt/c
- **Permissions**: Linux permissions on native FS, Windows ACLs on /mnt/c

<!-- section_id: "6b73a4fb-a29e-4ae2-a9d8-7ec599ac7986" -->
### Tool and Command Context
- Linux commands available: bash, grep, find, awk, sed
- Python: `python3` (Linux version)
- Node.js: Linux build via nvm or apt
- Git: Configured for Linux (LF line endings)
- Windows tools: Available via .exe suffix (e.g., `notepad.exe`)

<!-- section_id: "7ee24c6a-4530-4c64-91b4-6b56f7cb8f76" -->
### Research and Planning Considerations
- Can reference both Linux and Windows documentation
- Path translations needed when working across boundary
- Consider cross-platform compatibility in design decisions
- Network access works normally (both Linux and Windows stacks available)

<!-- section_id: "62fcae32-24cb-4aa2-836a-aa70ecf77764" -->
### Long Reasoning Tasks
- Assume POSIX-compliant environment for scripting
- File paths use forward slashes
- Line endings default to LF (Unix-style)
- Shell scripts use bash shebang: `#!/bin/bash`

<!-- section_id: "4bc93216-5af8-4cf2-bc8f-4b9db762a2b2" -->
### Gemini-Specific Features in WSL
- Use `systemInstruction` with manually composed context
- Load this file as part of system instruction composition
- Suitable for request gathering and planning stages
- Can handle multi-turn conversations for complex designs

---

<!-- section_id: "8a870849-d9d4-45e5-962c-86f82f743501" -->
## Integration Notes

This context file:
- Is loaded as part of Gemini CLI's `systemInstruction` parameter
- Provides OS-specific context for research and planning agents
- Complements `CLAUDE.md` (managers/implementation) and `AGENTS.md` (workers)

---

<!-- section_id: "07886b6d-2961-48ba-8dae-eb4a6b3bbfd4" -->
## Future Extensions

Add WSL-specific:
- Interop patterns for Windows/Linux tooling
- Cross-platform design considerations
- Research resource locations (docs, references)
- Long-running task optimization strategies
