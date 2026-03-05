---
resource_id: "0d1c3dc8-184a-4bbc-8425-dbd7221b059e"
resource_type: "rule"
resource_name: "AGENT_CONFIG_REFERENCE_TEMPLATE"
---
# Agent Configuration File Reference Template
*Template for Agent-Specific Configuration Files*

<!-- section_id: "cdc2ba6d-6ab9-48af-a477-3aafdb3c6741" -->
## Purpose

This template shows how agent-specific configuration files should reference the master terminal execution protocol.

<!-- section_id: "4d4a34f9-8bcf-4d76-834d-303d73bd2ece" -->
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

<!-- section_id: "fccfa68c-c624-4f2b-948f-02a4fcb09b69" -->
## Examples

<!-- section_id: "7bde6969-5681-4a08-bcd2-f87a6f07fd87" -->
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

<!-- section_id: "99888339-d0bc-4ce2-b1d4-5568bc00e05d" -->
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

<!-- section_id: "61b0223a-dfee-4c81-b337-bb658df84d33" -->
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

<!-- section_id: "b95d4479-bd34-4b54-8b3f-38342a27992e" -->
## Key Principles

1. **Reference, Don't Duplicate**: Always reference the master document rather than copying rules
2. **Agent-Specific Tool Mapping**: Provide the agent's specific tool name
3. **Quick Reference**: Include a brief quick reference for convenience
4. **Link to Master**: Always include the link to the master document

<!-- section_id: "f1fe45df-573f-4f0b-b884-619216792106" -->
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

