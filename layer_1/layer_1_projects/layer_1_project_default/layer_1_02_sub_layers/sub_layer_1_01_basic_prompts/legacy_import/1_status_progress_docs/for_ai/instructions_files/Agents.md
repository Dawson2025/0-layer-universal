---
resource_id: "8c2dc746-8a12-440a-adb7-bd9a9c44a96e"
resource_type: "document"
resource_name: "Agents"
---
# AI Agents Configuration

This file provides configuration guidance for all AI agents working with the Language Tracker project.

<!-- section_id: "415f3994-d071-4ccc-9de6-8919b77ddf64" -->
## 🚨 Terminal Execution Protocol

**MANDATORY**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_DOCUMENTATION.md` for complete documentation.

**Universal Terminal Execution**: See `0_context/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_TERMINAL_EXECUTION.md` for universal best practices.

**Quick Reference (Universal for ALL Agents):**
- Node.js commands → Use agent's terminal tool directly: `<agent_tool>("npx <command> ; exit")`
- System commands → Use agent's terminal tool directly: `<agent_tool>("<command> ; exit")`
- Always add `; exit` to prevent hanging on both success and failure

**Agent-Specific Tool Names:**
- Cursor: `run_terminal_cmd` (see CURSOR_TERMINAL_EXECUTION.md for Python script handling)
- Claude Code: `run_terminal_cmd`
- Codex: `run_terminal_cmd`
- Warp: `run_command`
- Gemini CLI: Direct terminal execution

**Note**: Python wrapper solutions are Cursor-specific. Other agents can use their terminal tools directly for Python scripts.

<!-- section_id: "3d765ff5-a71d-4aa3-887f-491d3ae66134" -->
## Trickle-Down Documentation System

**MANDATORY:** All AI agents must use the hierarchical trickle-down documentation system.

<!-- section_id: "949ee8e3-dbe4-42c4-b5dc-f095e5207d6f" -->
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

<!-- section_id: "45728af2-b653-446a-b753-8d10d2a62402" -->
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

<!-- section_id: "acc9ca16-6a43-4c00-a88d-607b20c71b35" -->
### WSL Ubuntu Environment Compliance

**CRITICAL:** All AI agents must comply with TD0.5 environment standards:
- All file operations within WSL Ubuntu file system
- No Windows C:\ drive operations
- Use WSL Ubuntu paths exclusively
- Respect environment tool configurations

<!-- section_id: "e2f7aa82-0eb0-4651-8199-b6ff09448044" -->
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
