<!-- derived_from: "d39b1b99-83b0-4e73-96b4-22fd8b03e835" -->
# Claude Code Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 1 (Project)
**Stage**: stage_1.01_instructions

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## WSL-Specific Context for Claude Code at Layer 1 (Project)

This context builds on Layer 0 Universal WSL context and adds project-level considerations.

### Project-Level WSL Considerations
- Project files should be in native Linux filesystem: `/home/dawson/code/`
- Avoid placing project root in `/mnt/c/` for performance
- Git repository should use LF line endings (configured in `.gitattributes`)
- Consider cross-platform team members (Windows, macOS, Linux)

### Project Dependencies in WSL
- Node.js dependencies installed via Linux npm
- Python packages via Linux pip3
- System dependencies via apt (Linux package manager)
- No Windows-specific build tools required

### Project Execution Environment
- Development servers run on Linux ports (forwarded to Windows)
- Database connections use localhost (WSL2 networking)
- File watchers work on native Linux filesystem
- Environment variables set in bash profile or .env files

### WSL Networking for Projects
- WSL2: Uses virtualized network adapter
- Access from Windows: `localhost:<port>` works for most cases
- Windows firewall may affect external access
- DNS resolution uses Windows resolver

### Project-Specific Paths
- Configuration files: `~/.config/` or project `.config/`
- Log files: Project root or `/var/log/` (if system service)
- Cache files: `~/.cache/` or project `.cache/`

---

## Integration Notes

This context file:
- Inherits from Layer 0 Universal WSL context
- Is overridden by Layer 2 (Feature) and Layer 3 (Component) WSL context
- Works in conjunction with project-level `AGENTS.md` and `GEMINI.md`

---

## Future Extensions

Add project-level WSL-specific:
- Project dependency installation patterns
- Development server configuration
- Database setup considerations
- Cross-platform compatibility notes
