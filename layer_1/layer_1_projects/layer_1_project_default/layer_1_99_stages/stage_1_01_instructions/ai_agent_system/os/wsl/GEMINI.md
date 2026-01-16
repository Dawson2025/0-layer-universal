# Gemini CLI Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 1 (Project)
**Stage**: stage_1.01_instructions
**Tool Context**: Gemini CLI (research, planning, long reasoning)

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## WSL-Specific Context for Gemini CLI at Layer 1 (Project)

This context builds on Layer 0 Universal WSL context and adds project-level planning considerations.

### Project Architecture in WSL
- Design with Linux-native performance in mind
- Consider WSL2 networking for server components
- Plan for cross-platform compatibility when team uses Windows/macOS
- Account for WSL-specific limitations (GUI apps require WSLg)

### Technology Stack Considerations
- Backend frameworks: Can use any Linux-compatible stack
- Databases: Run natively in WSL (PostgreSQL, MySQL, Redis, etc.)
- Container orchestration: Docker Desktop integrates with WSL2
- Build tools: Use Linux-native versions (make, cmake, gcc)

### Project Planning for WSL Environment
- Development environment setup assumes WSL2
- File system performance: Keep code on native Linux FS
- Network services accessible from Windows host
- Integration testing can span Windows/Linux boundary if needed

### Long-Term Design Decisions
- Production deployment likely Linux-based (matches dev environment)
- CI/CD pipelines can assume Linux environment
- Dependency management via Linux package ecosystems
- Cross-platform considerations for desktop apps (if applicable)

### Research and Documentation Context
- Reference Linux/WSL documentation for project setup
- Consider Windows integration points (VS Code, Windows Terminal)
- Plan for team onboarding (WSL installation, configuration)
- Document WSL-specific quirks in project README

---

## Integration Notes

This context file:
- Inherits from Layer 0 Universal WSL context
- Is overridden by Layer 2 (Feature) and Layer 3 (Component) WSL contexts
- Provides project-level planning context for Gemini CLI

---

## Future Extensions

Add project-level WSL-specific:
- Architecture decision records (ADRs) for WSL choices
- Project dependency documentation
- Development environment setup guides
- Cross-platform testing strategies
