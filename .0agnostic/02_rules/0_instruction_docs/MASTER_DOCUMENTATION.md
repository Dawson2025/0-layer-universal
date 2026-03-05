---
resource_id: "fb11a57e-d7c9-4d3c-a5ee-9bced3b92d22"
resource_type: "rule"
resource_name: "MASTER_DOCUMENTATION"
---
# Master Documentation
*Single Source of Truth for ALL AI Agents*

<!-- section_id: "a4115d4c-dd9a-4220-812a-88a4494a88ef" -->
## Purpose

This is the **authoritative master document** for all universal AI agent documentation. **ALL agent-specific configuration files** (Cursor, Claude Code, Codex, Gemini CLI, Warp, etc.) should reference this document.

<!-- section_id: "4225535d-4d5e-4aff-a0eb-73391f9c427f" -->
## Location

**Universal Location**: `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_DOCUMENTATION.md`

**This file should be referenced by:**
- `.cursorrules` or Cursor user rules
- `.claude/project_instructions.md` (Claude Code)
- `CLAUDE.md` (Claude Code)
- `Agents.md` (Codex, general agents)
- `cursor-agent-spec-kit.md` (Cursor)
- `warp-agent-spec-kit.md` (Warp)
- Any other agent-specific configuration files

---

<!-- section_id: "03ba7128-08d5-4482-8718-b93bb2c0f138" -->
## Universal Section: Rules for ALL Agents

The following rules and practices apply to **ALL AI agents**, regardless of which IDE or platform they're using.

<!-- section_id: "4e79d27d-1c54-47f1-ad43-745ba0324f3d" -->
### 1. Documentation Standards

**Universal Documentation System**: See `UNIVERSAL_DOCUMENTATION_SYSTEM.md`
- Follow trickle-down hierarchy (Universal → Project → Feature)
- Document as you go
- Update `0_context/` documentation before ending turn

<!-- section_id: "51e262a1-ddd0-461a-981d-7323a35f6ecd" -->
### 2. Testing Protocols

**Testing Agent System**: See `TESTING_AGENT_SYSTEM_README.md`
- Separation of concerns between development and testing
- Use testing agent handoff templates
- Follow testing standards

<!-- section_id: "9b3c0f74-373b-4138-95ca-f45a42622658" -->
### 3. Terminal Execution (Universal Best Practices)

**Universal Terminal Execution**: See `UNIVERSAL_TERMINAL_EXECUTION.md`

**General Principles** (apply to all agents):
- Use appropriate tools for different command types
- Node.js commands → Use agent's terminal tool directly
- System commands → Use agent's terminal tool directly
- Follow command structure patterns
- Handle errors appropriately

**Note**: Terminal hanging issues and Python wrapper solutions are **Cursor-specific**. See agent-specific section below.

<!-- section_id: "cee46e81-1771-492f-b123-325dad580818" -->
### 4. Manual Steps Automation

**Manual Steps Automation**: See `manual-steps-automation.md`
- Never ask users to do manual steps
- Automate browser interactions
- Use MCP tools for web interfaces
- Execute all steps programmatically

<!-- section_id: "638ab8a0-ef48-4e93-b210-d220b167c76c" -->
### 5. Security Protocols

**Security**: See `sudo_password_management.md`
- Handle sensitive credentials securely
- Manage sudo access properly
- Follow security best practices

<!-- section_id: "7e035740-d1e6-47cc-92c8-72cc162fafd1" -->
### 6. Documentation Completion Protocol

**Documentation**: See `post-completion-documentation-protocol.md`
- Create completion reports
- Document decisions made
- Archive completed work
- Maintain documentation quality

---

<!-- section_id: "1d51dfec-0080-4157-8473-7d186cea1bfa" -->
## Agent-Specific Section: Conditional Instructions

**If you are a Cursor agent**, see: `CURSOR_AGENT_GUIDE.md`
- Terminal hanging issues and solutions
- Python wrapper usage
- Cursor-specific workarounds

**If you are a Codex agent**, see: `CODEX_AGENT_GUIDE.md` (create if needed)
- Codex-specific solutions and workarounds

**If you are a Claude Code agent**, see: `CLAUDE_AGENT_GUIDE.md` (create if needed)
- Claude Code-specific solutions and workarounds

**If you are a Warp agent**, see: `WARP_AGENT_GUIDE.md` (create if needed)
- Warp-specific solutions and workarounds

**If you are a Gemini CLI agent**, see: `GEMINI_AGENT_GUIDE.md` (create if needed)
- Gemini CLI-specific solutions and workarounds

---

<!-- section_id: "11e896ee-4a9b-41e5-8563-efc6538718e8" -->
## Complete Documentation Index

<!-- section_id: "d16b380d-9e9a-4acb-b2fc-7a634ecd266c" -->
### Universal Systems

1. **Documentation System**
   - `UNIVERSAL_DOCUMENTATION_SYSTEM.md` - Meta-documentation
   - `README.md` - Overview of all universal systems

2. **Testing System**
   - `TESTING_AGENT_SYSTEM_README.md` - Complete overview
   - `testing-agent-protocol.md` - Core protocol
   - `testing-agent-instructions.md` - How to create tests

3. **Terminal Execution System**
   - `UNIVERSAL_TERMINAL_EXECUTION.md` - Universal best practices
   - `CURSOR_TERMINAL_EXECUTION.md` - Cursor-specific solutions
   - `terminal-tool-replacement.md` - Complete guide
   - `when-to-use-terminal-wrapper.md` - Decision guide

4. **Other Universal Systems**
   - `manual-steps-automation.md` - Automation protocol
   - `sudo_password_management.md` - Security protocols
   - `post-completion-documentation-protocol.md` - Documentation standards

<!-- section_id: "278c1679-eacf-4482-80d1-4ed2108b8726" -->
### Agent-Specific Guides

- `CURSOR_AGENT_GUIDE.md` - All Cursor-specific solutions
- `CODEX_AGENT_GUIDE.md` - Codex-specific (if needed)
- `CLAUDE_AGENT_GUIDE.md` - Claude Code-specific (if needed)
- `WARP_AGENT_GUIDE.md` - Warp-specific (if needed)
- `GEMINI_AGENT_GUIDE.md` - Gemini CLI-specific (if needed)

---

<!-- section_id: "efdb296e-4775-425c-a1f1-3f5048702c15" -->
## Quick Reference for Agent Config Files

When creating or updating agent-specific configuration files, use this format:

```markdown
## Master Documentation Reference

**MANDATORY**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_DOCUMENTATION.md` for complete documentation.

**Universal Rules**: Apply to all agents (see Universal Section above)
**Agent-Specific**: See [AGENT]_AGENT_GUIDE.md for [Agent Name]-specific solutions
```

---

<!-- section_id: "77357f65-c63c-4a7f-85a4-ab30ff2cd6b7" -->
## Key Principles

1. **Universal First**: All agents follow universal rules
2. **Agent-Specific Second**: Agent guides provide solutions for specific issues
3. **Single Source of Truth**: This master document is the entry point
4. **No Duplication**: Agent config files reference, don't copy
5. **Clear Separation**: Universal vs agent-specific is clearly marked

---

**Status**: Master Reference (Single Source of Truth)  
**Last Updated**: November 15, 2025  
**Version**: 1.0  
**Purpose**: Central reference for all agent-specific configuration files

