---
resource_id: "26567e07-964e-42f3-bc76-e9a2ce01c971"
resource_type: "document"
resource_name: "GEMINI.sync-conflict-20260126-035814-IF2WOGZ"
---
# Gemini CLI Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: Gemini CLI (research, planning, long reasoning)

---

<!-- section_id: "80bbe6d8-40a0-4792-91d6-f9870da25388" -->
## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

<!-- section_id: "1ff559e4-fee0-4930-984c-d3d2f99f9c8f" -->
## Ubuntu-Specific Context for Gemini CLI

<!-- section_id: "154e24ed-6f4f-4c80-ad26-19ec0db863c5" -->
### Environment Overview
- Native Linux Ubuntu environment
- Full Linux kernel and userspace (no compatibility layers)
- POSIX-compliant with GNU extensions
- Industry-standard server and development platform

<!-- section_id: "ea257707-6835-4b5b-b90d-1daa6f9fd8c2" -->
### File System Considerations
- **Primary workspace**: `/home/dawson/code/`
- **System directories**: `/usr/`, `/opt/`, `/var/`, `/etc/`
- **Filesystem type**: ext4, btrfs, or xfs (typically)
- **Permissions**: Standard Unix DAC (Discretionary Access Control)
- **Line endings**: LF only (Unix convention)

<!-- section_id: "f625224a-b7f7-4717-a6a6-187933c77c9b" -->
### Tool and Command Context
- Full GNU/Linux toolchain available
- Bash as standard shell (POSIX sh also available)
- Python 3: Default version via `python3`
- Node.js: via nvm or apt package manager
- Git: Native Linux build with full feature set
- Build tools: gcc, make, cmake available via apt

<!-- section_id: "193591e2-6e2a-4657-aa8a-a9fc9b337748" -->
### Research and Planning Considerations
- Reference Linux-native documentation and resources
- Assume POSIX compliance in design decisions
- Consider Ubuntu LTS versions for stability guidance
- Network access via standard Linux stack
- Container support via Docker (native, not via WSL)

<!-- section_id: "d37bafbc-7128-434a-9daf-a27e9d72a8b1" -->
### Long Reasoning Tasks
- Assume full Linux environment for architectural decisions
- Design with Linux filesystem conventions in mind
- Plan for systemd service integration where applicable
- Consider native Linux security models (AppArmor, SELinux)
- Use Linux-native path conventions throughout

<!-- section_id: "04209e4a-bc2d-40d7-a44b-4c8657d70922" -->
### Gemini-Specific Features in Ubuntu
- Use `systemInstruction` with manually composed context
- Load this file as part of system instruction composition
- Suitable for request gathering and planning stages
- Multi-turn conversations supported
- Can reference extensive Linux documentation ecosystem

---

<!-- section_id: "4ea723df-c34c-43a8-9ee1-8634dc4763f5" -->
## Integration Notes

This context file:
- Is loaded as part of Gemini CLI's `systemInstruction` parameter
- Provides OS-specific context for research and planning agents
- Complements `CLAUDE.md` (managers/implementation) and `AGENTS.md` (workers)

---

<!-- section_id: "30cd5f1f-b531-499d-814b-15e32e2d3b1f" -->
## Future Extensions

Add Ubuntu-specific:
- LTS version-specific considerations
- Package ecosystem patterns (PPAs, universe, multiverse)
- Security framework integration (AppArmor)
- Performance tuning patterns
- Container and virtualization patterns
