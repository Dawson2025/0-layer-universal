---
resource_id: "5dd4466c-05c8-44fe-81de-2be3fcc09928"
resource_type: "document"
resource_name: "Agents"
---
# AI Agents Configuration

This file provides configuration guidance for all AI agents working with the Language Tracker project.

<!-- section_id: "556aab2f-04a2-4055-8cff-017ad434730a" -->
## Trickle-Down Documentation System

**MANDATORY:** All AI agents must use the hierarchical trickle-down documentation system.

<!-- section_id: "9b26b5d2-47d5-4050-b05b-fe3655d54ee6" -->
### Context Loading Protocol

**Required Loading Order: TD0 ? TD0.5 ? TD1 ? TD2 ? TD3**

**Step 1: Universal Principles (TD0)**
- Location: /docs/1_trickle_down/trickle-down-0-universal/
- Load: universal_instructions.md
- Contains: Cross-project standards, development philosophies

**Step 2: Environment Standards (TD0.5)**
- Location: /docs/1_trickle_down/trickle-down-0.5-environment/
- Load: wsl-ubuntu-environment.md
- Contains: **WSL Ubuntu file system requirements (MANDATORY)**

**Step 3: Project Standards (TD1)**
- Location: /docs/1_trickle_down/trickle-down-1-project/
- Load: constitution.md
- Contains: Language Tracker constitution, TDD framework

**Step 4: Feature Guidance (TD2)**
- Location: /docs/1_trickle_down/trickle-down-2-features/
- Load: Relevant feature domain documentation
- Options: authentication, learning, content-management, advanced, system

**Step 5: Implementation Details (TD3)**
- Location: /docs/1_trickle_down/trickle-down-3-components/
- Load: Relevant implementation summaries and feature details

<!-- section_id: "5235f93c-8587-4a36-b431-822083cea70c" -->
### AI Agent Specific Instructions

**For Claude Code:**
- Primary file: /docs/for_ai/instructions_files/CLAUDE.md
- Follow trickle-down context loading before any work

**For GitHub Copilot:**
- Integrate trickle-down context through IDE workspace
- Reference TD1 constitution for coding standards

**For Warp AI Assistant:**
- Load environment context from TD0.5 before file operations
- Respect WSL Ubuntu file system requirements

**For Other AI Agents:**
- Always start with TD0 ? TD0.5 ? TD1 context loading
- Reference appropriate TD2/TD3 levels based on task scope

<!-- section_id: "7d2d2434-6a8e-4e7c-b4f4-6fa9832c7b0e" -->
### WSL Ubuntu Environment Compliance

**CRITICAL:** All AI agents must comply with TD0.5 environment standards:
- All file operations within WSL Ubuntu file system
- No Windows C:\ drive operations
- Use WSL Ubuntu paths exclusively
- Respect environment tool configurations

<!-- section_id: "09f594a8-7161-4a04-88d0-d2e7e0ba4666" -->
### Error Prevention

**Common AI Agent Mistakes to Avoid:**
- ? Skipping trickle-down context loading order
- ? Using Windows file paths instead of WSL Ubuntu paths
- ? Referencing outdated documentation structures
- ? Failing to cascade higher-level principle changes

**Required Best Practices:**
- ? Always verify trickle-down level before referencing documentation
- ? Load context in proper hierarchical order
- ? Reference most specific applicable trickle-down level
- ? Update documentation at appropriate trickle-down levels

---

**Last Updated**: October 21, 2025
**Trickle-Down System Version**: 1.0 with TD0.5 Environment Standards
