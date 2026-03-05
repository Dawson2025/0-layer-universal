---
resource_id: "c6d1099b-29d8-4fac-8044-6e53a853823d"
resource_type: "document"
resource_name: "GEMINI.sync-conflict-20260126-035815-IF2WOGZ"
---
# Gemini CLI Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: Gemini CLI (research, planning, long reasoning)

---

<!-- section_id: "33945c3a-c0c1-455d-af7d-d4bf01af82e6" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "25c99c86-e18a-4a43-aa6f-b4446736e9e6" -->
## WSL-Specific Context for Gemini CLI

<!-- section_id: "3f374b49-4553-4148-b182-653db6c16f75" -->
### Environment Overview
- WSL provides a Linux environment running on Windows kernel
- Hybrid architecture: Linux userspace + Windows kernel + Windows filesystem access
- Suitable for long-form research and planning tasks that span both ecosystems

<!-- section_id: "daec2771-859a-448b-a34b-e97b0690e383" -->
### File System Considerations
- **Primary workspace**: `/home/dawson/code/` (native Linux filesystem)
- **Windows access**: `/mnt/c/`, `/mnt/d/`, etc.
- **Performance**: Native Linux filesystem significantly faster than /mnt/c
- **Permissions**: Linux permissions on native FS, Windows ACLs on /mnt/c

<!-- section_id: "b9085176-32c2-4a99-9b20-8a845abdc869" -->
### Tool and Command Context
- Linux commands available: bash, grep, find, awk, sed
- Python: `python3` (Linux version)
- Node.js: Linux build via nvm or apt
- Git: Configured for Linux (LF line endings)
- Windows tools: Available via .exe suffix (e.g., `notepad.exe`)

<!-- section_id: "79d36532-ecb3-47bb-8989-451a4ad6f291" -->
### Research and Planning Considerations
- Can reference both Linux and Windows documentation
- Path translations needed when working across boundary
- Consider cross-platform compatibility in design decisions
- Network access works normally (both Linux and Windows stacks available)

<!-- section_id: "0531d945-fd03-4041-94c2-903131e6ed9f" -->
### Long Reasoning Tasks
- Assume POSIX-compliant environment for scripting
- File paths use forward slashes
- Line endings default to LF (Unix-style)
- Shell scripts use bash shebang: `#!/bin/bash`

<!-- section_id: "2d7e00f8-9e6a-488f-b65e-56f10e0c03b2" -->
### Gemini-Specific Features in WSL
- Use `systemInstruction` with manually composed context
- Load this file as part of system instruction composition
- Suitable for request gathering and planning stages
- Can handle multi-turn conversations for complex designs

---

<!-- section_id: "fea70b02-164c-4858-ab82-0edb2af847ee" -->
## Integration Notes

This context file:
- Is loaded as part of Gemini CLI's `systemInstruction` parameter
- Provides OS-specific context for research and planning agents
- Complements `CLAUDE.md` (managers/implementation) and `AGENTS.md` (workers)

---

<!-- section_id: "6424c22b-1f4e-4572-abf4-365b06ac1410" -->
## Future Extensions

Add WSL-specific:
- Interop patterns for Windows/Linux tooling
- Cross-platform design considerations
- Research resource locations (docs, references)
- Long-running task optimization strategies
