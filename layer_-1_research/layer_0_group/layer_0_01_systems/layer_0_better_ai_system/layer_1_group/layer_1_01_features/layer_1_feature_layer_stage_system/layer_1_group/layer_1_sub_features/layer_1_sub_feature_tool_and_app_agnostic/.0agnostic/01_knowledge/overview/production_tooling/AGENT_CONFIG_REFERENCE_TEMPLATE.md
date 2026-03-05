---
resource_id: "11a5b726-230d-41f6-a6cb-a6b5e97397b5"
resource_type: "knowledge"
resource_name: "AGENT_CONFIG_REFERENCE_TEMPLATE"
---
# Agent Configuration File Reference Template
*Template for Agent-Specific Configuration Files*

<!-- section_id: "5df5040e-8080-45f9-a761-eb26bfd06052" -->
## Purpose

This template shows how agent-specific configuration files should reference the master terminal execution protocol.

<!-- section_id: "4435420a-308b-4568-9aec-3c42f3810c15" -->
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

<!-- section_id: "d5fb07a2-cc98-480a-bdd5-9fa5bf5a43f3" -->
## Examples

<!-- section_id: "9bf42716-c59f-4e50-b8fe-ca8253b20f4d" -->
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

<!-- section_id: "cdbad7c4-40fa-4489-a4a3-1dac59cbff71" -->
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

<!-- section_id: "493bf687-b9a1-4d60-9e21-3ac997906cb3" -->
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

<!-- section_id: "028f9f52-1e15-492a-9cf3-1b53ebfd3dc9" -->
## Key Principles

1. **Reference, Don't Duplicate**: Always reference the master document rather than copying rules
2. **Agent-Specific Tool Mapping**: Provide the agent's specific tool name
3. **Quick Reference**: Include a brief quick reference for convenience
4. **Link to Master**: Always include the link to the master document

<!-- section_id: "b4ed0efe-312c-4a79-ab89-87dde75ea408" -->
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

