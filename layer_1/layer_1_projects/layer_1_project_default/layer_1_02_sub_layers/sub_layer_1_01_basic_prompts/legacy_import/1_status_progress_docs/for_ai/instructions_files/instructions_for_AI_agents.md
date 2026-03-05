---
resource_id: "206c6ff7-a4a5-4d3f-a6fc-b04a14906034"
resource_type: "document"
resource_name: "instructions_for_AI_agents"
---
# Instructions for AI Agents

This file provides universal instructions for all AI agents working with the Language Tracker project.

<!-- section_id: "a6334af5-b1ac-40a1-b033-01b4d4dc7c4e" -->
## Trickle-Down Documentation System

**CRITICAL:** All AI agents must follow the hierarchical trickle-down documentation system.

<!-- section_id: "ab9b0d35-31d1-4699-9926-ed29249f09f5" -->
### Mandatory Context Loading Order

**TD0 ? TD0.5 ? TD1 ? TD2 ? TD3**

All AI agents must load context in this exact hierarchical order before beginning any work:

1. **TD0 - Universal Principles** (/docs/1_trickle_down/trickle-down-0-universal/)
2. **TD0.5 - Environment Standards** (/docs/1_trickle_down/trickle-down-0.5-environment/)
3. **TD1 - Project Standards** (/docs/1_trickle_down/trickle-down-1-project/)
4. **TD2 - Feature Guidance** (/docs/1_trickle_down/trickle-down-2-features/)
5. **TD3 - Implementation Details** (/docs/1_trickle_down/trickle-down-3-components/)

<!-- section_id: "3420901c-20ea-4089-907e-53531a1e37d5" -->
### WSL Ubuntu Environment Requirement

**MANDATORY:** All AI agents must comply with TD0.5 environment standards:
- All file operations within WSL Ubuntu file system
- Project location: /home/dawson/code/lang-trak-in-progress/
- No Windows C:\ drive operations
- Use WSL Ubuntu development tools exclusively

<!-- section_id: "b99dcff7-9d4f-4cdc-8ad4-ea47135f670d" -->
### Agent-Specific Configuration Files

**Primary Configuration Files:**
- **Claude Code**: CLAUDE.md - Comprehensive development guidance
- **Warp AI**: WARP.md - File system and environment operations
- **All Agents**: Agents.md - Universal agent configuration

<!-- section_id: "86631178-862c-41e1-9375-8f4a2fcdb28e" -->
### Documentation Migration Notice

**Legacy System**: The /docs/for_ai structure is being phased out in favor of the trickle-down system.

**Migration Status:**
- ? Trickle-down system fully implemented
- ? Agent configuration files updated
- ?? Legacy files maintained for transition period
- ?? Full migration target: Complete by spec kit implementation

<!-- section_id: "eb3f0aa7-d3ad-4951-81e1-0f1d7e0b3c04" -->
### Required AI Agent Behaviors

**Context Loading:**
- Always start with TD0 universal principles
- Load TD0.5 environment standards (critical for file operations)
- Reference TD1 project constitution for all development decisions
- Load relevant TD2/TD3 levels based on task scope

**File Operations:**
- Verify WSL Ubuntu environment before any file operations
- Use relative paths from project root when possible
- Respect trickle-down documentation organization
- Update appropriate trickle-down levels for documentation changes

**Error Prevention:**
- Never use Windows file paths for development operations
- Always validate trickle-down level appropriateness
- Maintain hierarchical referencing in documentation
- Follow cascade rules when making changes

---

**Instructions Version**: 2.0 (Trickle-Down System)
**Last Updated**: October 21, 2025
**Migration Status**: Active transition to trickle-down system
