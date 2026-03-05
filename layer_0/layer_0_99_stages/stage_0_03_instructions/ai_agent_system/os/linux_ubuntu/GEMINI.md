<!-- derived_from: "aa24709f-a54e-43db-ac3b-f2b61b2bbaac" -->
# Gemini CLI Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 0 (Universal)
**Stage**: stage_0_03_instructions
**Tool Context**: Gemini CLI (research, planning, long reasoning)

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## Ubuntu-Specific Context for Gemini CLI

### Environment Overview
- Native Linux Ubuntu environment
- Full Linux kernel and userspace (no compatibility layers)
- POSIX-compliant with GNU extensions
- Industry-standard server and development platform

### File System Considerations
- **Primary workspace**: `/home/dawson/code/`
- **System directories**: `/usr/`, `/opt/`, `/var/`, `/etc/`
- **Filesystem type**: ext4, btrfs, or xfs (typically)
- **Permissions**: Standard Unix DAC (Discretionary Access Control)
- **Line endings**: LF only (Unix convention)

### Tool and Command Context
- Full GNU/Linux toolchain available
- Bash as standard shell (POSIX sh also available)
- Python 3: Default version via `python3`
- Node.js: via nvm or apt package manager
- Git: Native Linux build with full feature set
- Build tools: gcc, make, cmake available via apt

### Research and Planning Considerations
- Reference Linux-native documentation and resources
- Assume POSIX compliance in design decisions
- Consider Ubuntu LTS versions for stability guidance
- Network access via standard Linux stack
- Container support via Docker (native, not via WSL)

### Long Reasoning Tasks
- Assume full Linux environment for architectural decisions
- Design with Linux filesystem conventions in mind
- Plan for systemd service integration where applicable
- Consider native Linux security models (AppArmor, SELinux)
- Use Linux-native path conventions throughout

### Gemini-Specific Features in Ubuntu
- Use `systemInstruction` with manually composed context
- Load this file as part of system instruction composition
- Suitable for request gathering and planning stages
- Multi-turn conversations supported
- Can reference extensive Linux documentation ecosystem

---

## Integration Notes

This context file:
- Is loaded as part of Gemini CLI's `systemInstruction` parameter
- Provides OS-specific context for research and planning agents
- Complements `CLAUDE.md` (managers/implementation) and `AGENTS.md` (workers)

---

## Future Extensions

Add Ubuntu-specific:
- LTS version-specific considerations
- Package ecosystem patterns (PPAs, universe, multiverse)
- Security framework integration (AppArmor)
- Performance tuning patterns
- Container and virtualization patterns
