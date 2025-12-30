# Gemini CLI Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 0 (Universal)
**Stage**: stage_0.01_instructions
**Tool Context**: Gemini CLI (research, planning, long reasoning)

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## WSL-Specific Context for Gemini CLI

### Environment Overview
- WSL provides a Linux environment running on Windows kernel
- Hybrid architecture: Linux userspace + Windows kernel + Windows filesystem access
- Suitable for long-form research and planning tasks that span both ecosystems

### File System Considerations
- **Primary workspace**: `/home/dawson/code/` (native Linux filesystem)
- **Windows access**: `/mnt/c/`, `/mnt/d/`, etc.
- **Performance**: Native Linux filesystem significantly faster than /mnt/c
- **Permissions**: Linux permissions on native FS, Windows ACLs on /mnt/c

### Tool and Command Context
- Linux commands available: bash, grep, find, awk, sed
- Python: `python3` (Linux version)
- Node.js: Linux build via nvm or apt
- Git: Configured for Linux (LF line endings)
- Windows tools: Available via .exe suffix (e.g., `notepad.exe`)

### Research and Planning Considerations
- Can reference both Linux and Windows documentation
- Path translations needed when working across boundary
- Consider cross-platform compatibility in design decisions
- Network access works normally (both Linux and Windows stacks available)

### Long Reasoning Tasks
- Assume POSIX-compliant environment for scripting
- File paths use forward slashes
- Line endings default to LF (Unix-style)
- Shell scripts use bash shebang: `#!/bin/bash`

### Gemini-Specific Features in WSL
- Use `systemInstruction` with manually composed context
- Load this file as part of system instruction composition
- Suitable for request gathering and planning stages
- Can handle multi-turn conversations for complex designs

---

## Integration Notes

This context file:
- Is loaded as part of Gemini CLI's `systemInstruction` parameter
- Provides OS-specific context for research and planning agents
- Complements `CLAUDE.md` (managers/implementation) and `AGENTS.md` (workers)

---

## Future Extensions

Add WSL-specific:
- Interop patterns for Windows/Linux tooling
- Cross-platform design considerations
- Research resource locations (docs, references)
- Long-running task optimization strategies
