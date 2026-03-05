---
resource_id: "c7c16f92-023c-4291-89b2-2b57590f640f"
resource_type: "document"
resource_name: "GEMINI.sync-conflict-20260126-102106-IF2WOGZ"
---
# Gemini CLI Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: Gemini CLI (research, planning, long reasoning)

---

<!-- section_id: "4cab182b-50e1-42ad-a4be-a2e07bd1087f" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "5ba5527f-b073-4d54-ac03-2e8274e5bf84" -->
## Ubuntu-Specific Context for Gemini CLI

<!-- section_id: "8708db76-bf66-409b-879e-923f9d00bcec" -->
### Environment Overview
- Native Linux Ubuntu environment
- Full Linux kernel and userspace (no compatibility layers)
- POSIX-compliant with GNU extensions
- Industry-standard server and development platform

<!-- section_id: "b80cfa6d-f630-4242-8496-b5322bfd2c9d" -->
### File System Considerations
- **Primary workspace**: `/home/dawson/code/`
- **System directories**: `/usr/`, `/opt/`, `/var/`, `/etc/`
- **Filesystem type**: ext4, btrfs, or xfs (typically)
- **Permissions**: Standard Unix DAC (Discretionary Access Control)
- **Line endings**: LF only (Unix convention)

<!-- section_id: "abab8991-a5dd-4138-bd07-2054e7af616d" -->
### Tool and Command Context
- Full GNU/Linux toolchain available
- Bash as standard shell (POSIX sh also available)
- Python 3: Default version via `python3`
- Node.js: via nvm or apt package manager
- Git: Native Linux build with full feature set
- Build tools: gcc, make, cmake available via apt

<!-- section_id: "a2424704-e7be-462f-a42c-83440f7a581e" -->
### Research and Planning Considerations
- Reference Linux-native documentation and resources
- Assume POSIX compliance in design decisions
- Consider Ubuntu LTS versions for stability guidance
- Network access via standard Linux stack
- Container support via Docker (native, not via WSL)

<!-- section_id: "8284bbd5-eb3e-48e0-b87e-5ae9005f83dc" -->
### Long Reasoning Tasks
- Assume full Linux environment for architectural decisions
- Design with Linux filesystem conventions in mind
- Plan for systemd service integration where applicable
- Consider native Linux security models (AppArmor, SELinux)
- Use Linux-native path conventions throughout

<!-- section_id: "c84c3e89-cbfc-42cc-b0ad-d83c63d4ba22" -->
### Gemini-Specific Features in Ubuntu
- Use `systemInstruction` with manually composed context
- Load this file as part of system instruction composition
- Suitable for request gathering and planning stages
- Multi-turn conversations supported
- Can reference extensive Linux documentation ecosystem

---

<!-- section_id: "7d9f0408-74d3-446e-b236-a6fbdafd034f" -->
## Integration Notes

This context file:
- Is loaded as part of Gemini CLI's `systemInstruction` parameter
- Provides OS-specific context for research and planning agents
- Complements `CLAUDE.md` (managers/implementation) and `AGENTS.md` (workers)

---

<!-- section_id: "57574eb5-096c-4219-9cf0-a29af0964712" -->
## Future Extensions

Add Ubuntu-specific:
- LTS version-specific considerations
- Package ecosystem patterns (PPAs, universe, multiverse)
- Security framework integration (AppArmor)
- Performance tuning patterns
- Container and virtualization patterns
