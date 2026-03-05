---
resource_id: "11a5b726-230d-41f6-a6cb-a6b5e97397b5"
resource_type: "knowledge"
resource_name: "AGENT_CONFIG_REFERENCE_TEMPLATE"
---
# Agent Configuration File Reference Template
*Template for Agent-Specific Configuration Files*

## Purpose

This template shows how agent-specific configuration files should reference the master terminal execution protocol.

## Template Structure

```markdown
# [Agent Name] Configuration
*Agent-Specific Instructions*

## 🚨 Terminal Execution Protocol

**MANDATORY**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` for complete terminal execution rules.

**Quick Reference for [Agent Name]:**
- Python scripts → `python3 scripts/terminal_wrapper.py --script <script>`
- Node.js commands → `[agent_tool]("npx <command> ; exit")`
- System commands → `[agent_tool]("<command> ; exit")`
- Always add `; exit` to prevent hanging on both success and failure

**Agent-Specific Tool**: `[tool_name]` (e.g., `run_terminal_cmd`, `run_command`)

## [Other Agent-Specific Sections]
...
```

## Examples

### For Cursor
```markdown
## 🚨 Terminal Execution Protocol

**MANDATORY**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` for complete rules.

**Quick Reference for Cursor:**
- Python scripts → `python3 scripts/terminal_wrapper.py --script <script>`
- Node.js commands → `run_terminal_cmd("npx <command> ; exit")`
- System commands → `run_terminal_cmd("<command> ; exit")`
- Always add `; exit` to prevent hanging on both success and failure

**Tool**: `run_terminal_cmd`
```

### For Warp
```markdown
## 🚨 Terminal Execution Protocol

**MANDATORY**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` for complete rules.

**Quick Reference for Warp:**
- Python scripts → `python3 scripts/terminal_wrapper.py --script <script>`
- Node.js commands → `run_command("npx <command> ; exit")`
- System commands → `run_command("<command> ; exit")`
- Always add `; exit` to prevent hanging on both success and failure

**Tool**: `run_command`
```

### For Claude Code
```markdown
## 🚨 Terminal Execution Protocol

**MANDATORY**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` for complete rules.

**Quick Reference for Claude Code:**
- Python scripts → `python3 scripts/terminal_wrapper.py --script <script>`
- Node.js commands → `run_terminal_cmd("npx <command> ; exit")`
- System commands → `run_terminal_cmd("<command> ; exit")`
- Always add `; exit` to prevent hanging on both success and failure

**Tool**: `run_terminal_cmd` (built-in) or VS Code terminal integration
```

## Key Principles

1. **Reference, Don't Duplicate**: Always reference the master document rather than copying rules
2. **Agent-Specific Tool Mapping**: Provide the agent's specific tool name
3. **Quick Reference**: Include a brief quick reference for convenience
4. **Link to Master**: Always include the link to the master document

## Files That Should Use This Template

- `.cursorrules` or Cursor user rules
- `.claude/project_instructions.md` (Claude Code)
- `CLAUDE.md` (Claude Code)
- `Agents.md` (Codex, general agents)
- `cursor-agent-spec-kit.md` (Cursor)
- `warp-agent-spec-kit.md` (Warp)
- Any other agent-specific configuration files

---

**Purpose**: Ensure all agent-specific files reference the master document  
**Master Document**: `MASTER_TERMINAL_EXECUTION_REFERENCE.md`

