---
resource_id: "33d4373c-ecbc-479a-b2d9-0b99b9c15f65"
resource_type: "rule"
resource_name: "UNIVERSAL_TERMINAL_EXECUTION"
---
# Universal Terminal Execution
*Best Practices for ALL AI Agents*

<!-- section_id: "4a43dc5d-ae84-4773-963f-2ef4881e0cd2" -->
## Purpose

This document provides **universal terminal execution best practices** that apply to **ALL AI agents**, regardless of which IDE or platform they're using. This ensures consistent, reliable terminal command execution across all AI agent interactions.

<!-- section_id: "bf5f00a5-d4c2-43ce-8b1f-2fe1dd0d7043" -->
## Location

**Universal Location**: `0_context/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_TERMINAL_EXECUTION.md`

**Referenced by**: `MASTER_DOCUMENTATION.md`

---

<!-- section_id: "069491c1-e129-4edc-80f4-920e7814b212" -->
## Universal Rules for ALL Agents

<!-- section_id: "ed4a8867-ce67-42b6-990d-02c8eae3bd9d" -->
### Rule 1: Use Appropriate Tools for Command Types

**Node.js Commands** - Use agent's terminal tool directly:
```bash
# Cursor: run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
# Warp: run_command("npx -y playwright@latest install chromium ; exit")
# Claude Code: run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
```

**System Commands** - Use agent's terminal tool directly:
```bash
# Cursor: run_terminal_cmd("sudo apt install ./package.deb ; exit")
# Warp: run_command("sudo apt install ./package.deb ; exit")
# Claude Code: run_terminal_cmd("sudo apt install ./package.deb ; exit")
```

**Why**: 
- Node.js and system commands don't typically have subprocess communication issues
- Direct commands are clearer and simpler
- No need for wrapper overhead

<!-- section_id: "aebc2652-3ae0-4199-9589-bef8627b9581" -->
### Rule 2: Always Add `; exit` to Commands

**For ALL commands**:
```bash
# ✅ CORRECT - Always add ; exit
run_terminal_cmd("npx playwright install chromium ; exit")
run_terminal_cmd("apt install package ; exit")

# ❌ WRONG - May hang on failure
run_terminal_cmd("npx playwright install chromium && exit")  # Only exits on success
```

**Why**: 
- `; exit` always closes terminal (works for both success AND failure)
- `&& exit` only works on success, may still hang on failure
- Completion detection is more critical than exit code checking in automation

<!-- section_id: "9361dd10-5c61-4083-af33-d61905e8c362" -->
### Rule 3: Command Structure Patterns

**Best Practices**:
- Use clear, descriptive commands
- Include error handling where appropriate
- Use appropriate flags for non-interactive execution
- Avoid commands that require user interaction

**Examples**:
```bash
# ✅ Good - Non-interactive, clear
run_terminal_cmd("apt-get update -y ; exit")
run_terminal_cmd("npm install --no-interactive ; exit")

# ❌ Avoid - Requires interaction
run_terminal_cmd("apt install package")  # May prompt for confirmation
```

<!-- section_id: "10c84c73-28e1-45e4-89a9-81abeb5296a5" -->
### Rule 4: Error Handling

**Principles**:
- Always check command output for errors
- Handle failures gracefully
- Provide clear error messages
- Don't assume commands succeeded without verification

---

<!-- section_id: "c9bd1ec1-8cb6-457e-8bfc-254591f09e11" -->
## Agent-Specific Tool Mappings

<!-- section_id: "df5294b8-92b1-4f70-9939-0864e0b73847" -->
### Cursor Agent
- **Tool**: `run_terminal_cmd`
- **Node.js commands**: `run_terminal_cmd("npx <command> ; exit")`
- **System commands**: `run_terminal_cmd("<command> ; exit")`
- **Note**: Python scripts require special handling - see `CURSOR_TERMINAL_EXECUTION.md`

<!-- section_id: "13f7decb-c975-4098-8596-c228f94c0181" -->
### Claude Code Agent
- **Tool**: `run_terminal_cmd` (built-in) or VS Code terminal integration
- **Node.js commands**: `run_terminal_cmd("npx <command> ; exit")`
- **System commands**: `run_terminal_cmd("<command> ; exit")`

<!-- section_id: "ec8b2d7e-3942-4ff9-99f8-1be16b01c13b" -->
### Codex Agent
- **Tool**: `run_terminal_cmd` (built-in) or VS Code terminal integration
- **Node.js commands**: `run_terminal_cmd("npx <command> ; exit")`
- **System commands**: `run_terminal_cmd("<command> ; exit")`

<!-- section_id: "c9ca7db0-b511-4502-b5d2-07022f12a923" -->
### Warp AI Assistant
- **Tool**: `run_command`
- **Node.js commands**: `run_command("npx <command> ; exit")`
- **System commands**: `run_command("<command> ; exit")`

<!-- section_id: "bd007960-5041-4bde-b046-27dcb4997a87" -->
### Gemini CLI
- **Tool**: Terminal command execution (built-in)
- **Node.js commands**: Execute directly with `; exit` appended
- **System commands**: Execute directly with `; exit` appended

---

<!-- section_id: "7c24bd30-4e2b-4773-bfba-6d8c1390cf07" -->
## Quick Decision Tree

```
Is it a Node.js command (npx, npm)?
├─ YES → Use: <agent_terminal_tool>("npx <command> ; exit")
└─ NO → Is it a system command (apt, wget, ls)?
    ├─ YES → Use: <agent_terminal_tool>("<command> ; exit")
    └─ NO → Is it a Python script?
        ├─ YES → See agent-specific guide (Cursor has special handling)
        └─ NO → Use: <agent_terminal_tool>("<command> ; exit")
```

---

<!-- section_id: "06be63cc-fd60-4d06-967a-84b9966b3018" -->
## Agent-Specific Solutions

**If you encounter terminal issues specific to your agent**, see:
- **Cursor**: `CURSOR_TERMINAL_EXECUTION.md` - Terminal hanging, Python wrapper
- **Other agents**: Create agent-specific guide if needed

---

<!-- section_id: "b40d4164-b29c-4499-a4dd-55b9df7b6037" -->
## Related Documentation

- **Master Documentation**: `MASTER_DOCUMENTATION.md` - Complete overview
- **Cursor-Specific**: `CURSOR_TERMINAL_EXECUTION.md` - Cursor terminal hanging solution
- **Terminal Tool Replacement**: `terminal-tool-replacement.md` - Complete guide
- **When to Use Wrapper**: `when-to-use-terminal-wrapper.md` - Decision guide
- **Why && exit Works**: `why-&&-exit-works.md` - Technical details

---

**Status**: Universal (applies to all AI agents)  
**Last Updated**: November 15, 2025  
**Version**: 1.0  
**Purpose**: Universal terminal execution best practices

