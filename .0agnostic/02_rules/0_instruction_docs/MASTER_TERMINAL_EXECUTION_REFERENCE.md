---
resource_id: "3d974d64-ac37-438d-a084-393df47c29b0"
resource_type: "rule"
resource_name: "MASTER_TERMINAL_EXECUTION_REFERENCE"
---
# Master Terminal Execution Reference
*Legacy Document - See MASTER_DOCUMENTATION.md*

## ⚠️ Status: Superseded

**This document has been superseded by `MASTER_DOCUMENTATION.md`**, which provides a comprehensive overview of all universal systems, not just terminal execution.

**For terminal execution:**
- **Universal rules**: See `MASTER_DOCUMENTATION.md` → Universal Section → Terminal Execution
- **Universal best practices**: See `UNIVERSAL_TERMINAL_EXECUTION.md`
- **Cursor-specific solutions**: See `CURSOR_TERMINAL_EXECUTION.md`

**This document is kept for reference but should not be used as the primary source.**

---

## 🎯 Purpose (Legacy)

This was the **authoritative reference** for terminal execution protocol. **ALL agent-specific configuration files** (Cursor, Claude Code, Codex, Gemini CLI, Warp, etc.) should now reference `MASTER_DOCUMENTATION.md` instead.

## 📍 Location

**Universal Location**: `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md`

**This file should be referenced by:**
- `.cursorrules` or Cursor user rules
- `.claude/project_instructions.md` (Claude Code)
- `CLAUDE.md` (Claude Code)
- `Agents.md` (Codex, general agents)
- `cursor-agent-spec-kit.md` (Cursor)
- `warp-agent-spec-kit.md` (Warp)
- Any other agent-specific configuration files

## 🚨 Critical Rules (Universal for ALL Agents)

### Rule 1: Python Scripts - ALWAYS Use Terminal Wrapper

**For ANY Python script execution:**
```bash
# ✅ CORRECT - Use terminal wrapper
python3 scripts/terminal_wrapper.py --script scripts/script.py

# ❌ WRONG - Will hang in Cursor and may hang in other agents
run_terminal_cmd("python3 scripts/script.py")
```

**Why**: Python scripts cause hanging issues in Cursor and may cause issues in other agents. The wrapper solves subprocess communication problems.

### Rule 2: Node.js Commands - Use Agent's Terminal Tool Directly

**For Node.js commands (`npx`, `npm`):**
```bash
# ✅ CORRECT - Use agent's terminal tool directly
# Cursor: run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
# Warp: run_command("npx -y playwright@latest install chromium ; exit")
# Claude Code: run_terminal_cmd("npx -y playwright@latest install chromium ; exit")

# ❌ UNNECESSARY - Don't wrap Node.js commands
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

**Why**: 
- Node.js commands don't have Python subprocess hanging issues
- Wrapping in Python wrapper can cause confusion (e.g., using Python Playwright instead of Node.js Playwright)
- Direct commands are clearer and simpler

### Rule 3: System Commands - Use Agent's Terminal Tool Directly

**For system package managers and simple commands:**
```bash
# ✅ CORRECT - Use agent's terminal tool directly
# Cursor: run_terminal_cmd("sudo apt install ./package.deb ; exit")
# Warp: run_command("sudo apt install ./package.deb ; exit")
# Claude Code: run_terminal_cmd("sudo apt install ./package.deb ; exit")

# ❌ UNNECESSARY - Don't wrap simple system commands
python3 scripts/terminal_wrapper.py "apt install package ; exit"
```

**Why**: System commands don't need wrapper overhead.

### Rule 4: Always Add `; exit` to Commands

**For ALL commands (whether using wrapper or agent's terminal tool):**
```bash
# ✅ CORRECT - Always add ; exit
run_terminal_cmd("npx playwright install chromium ; exit")
python3 scripts/terminal_wrapper.py "quarto render ; exit"

# ❌ WRONG - May hang on failure
run_terminal_cmd("npx playwright install chromium && exit")  # Only exits on success
```

**Why**: 
- `; exit` always closes terminal (works for both success AND failure)
- `&& exit` only works on success, may still hang on failure
- Completion detection is more critical than exit code checking in automation

## 📋 Quick Decision Tree

```
Is it a Python script?
├─ YES → Use: python3 scripts/terminal_wrapper.py --script <script>
└─ NO → Is it Node.js (npx, npm)?
    ├─ YES → Use: <agent_terminal_tool>("npx <command> ; exit")
    └─ NO → Is it a system command (apt, wget, ls)?
        ├─ YES → Use: <agent_terminal_tool>("<command> ; exit")
        └─ NO → Is it complex?
            ├─ YES → Use: python3 scripts/terminal_wrapper.py "<command> ; exit"
            └─ NO → Use: <agent_terminal_tool>("<command> ; exit")
```

## 🔧 Agent-Specific Tool Mappings

### Cursor Agent
- **Tool**: `run_terminal_cmd`
- **Python scripts**: `python3 scripts/terminal_wrapper.py --script <script>`
- **Node.js commands**: `run_terminal_cmd("npx <command> ; exit")`
- **System commands**: `run_terminal_cmd("<command> ; exit")`

### Claude Code Agent
- **Tool**: `run_terminal_cmd` (built-in) or VS Code terminal integration
- **Python scripts**: `python3 scripts/terminal_wrapper.py --script <script>`
- **Node.js commands**: `run_terminal_cmd("npx <command> ; exit")`
- **System commands**: `run_terminal_cmd("<command> ; exit")`

### Codex Agent
- **Tool**: `run_terminal_cmd` (built-in) or VS Code terminal integration
- **Python scripts**: `python3 scripts/terminal_wrapper.py --script <script>`
- **Node.js commands**: `run_terminal_cmd("npx <command> ; exit")`
- **System commands**: `run_terminal_cmd("<command> ; exit")`

### Warp AI Assistant
- **Tool**: `run_command`
- **Python scripts**: `python3 scripts/terminal_wrapper.py --script <script>`
- **Node.js commands**: `run_command("npx <command> ; exit")`
- **System commands**: `run_command("<command> ; exit")`

### Gemini CLI
- **Tool**: Terminal command execution (built-in)
- **Python scripts**: `python3 scripts/terminal_wrapper.py --script <script>`
- **Node.js commands**: Execute directly with `; exit` appended
- **System commands**: Execute directly with `; exit` appended

## 📚 Complete Documentation

### Core Documents (Read These First)

1. **`UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`** - Complete universal protocol
   - Detailed rules and explanations
   - Agent-specific implementations
   - Complete examples

2. **`terminal-tool-replacement.md`** - Complete terminal execution guide
   - When to use wrapper vs run_terminal_cmd
   - Detailed rules and examples
   - Tool selection guide

3. **`when-to-use-terminal-wrapper.md`** - Decision guide
   - When wrapper is needed vs not needed
   - Examples by command type
   - Historical context (Playwright confusion)

### Supporting Documents

4. **`why-&&-exit-works.md`** - Technical explanation
   - Why `; exit` works
   - Why `&& exit` has limitations
   - Best practices

5. **`playwright-installation-confusion-analysis.md`** - Root cause analysis
   - Why wrapping Node.js commands caused confusion
   - How to prevent similar issues

6. **`cursor_terminal_issues.md`** - Cursor-specific issues
   - Terminal output handling problems
   - Cursor-specific workarounds

## ✅ Verification Checklist

Before executing any terminal command, verify:

- [ ] Is it a Python script? → Use terminal wrapper
- [ ] Is it Node.js? → Use agent's terminal tool directly
- [ ] Is it a system command? → Use agent's terminal tool directly
- [ ] Did I add `; exit`? → Always add `; exit` to prevent hanging
- [ ] Am I using the right tool? → Check agent-specific tool mapping above

## 🎯 Key Principles

1. **Python scripts = wrapper** (always)
2. **Node.js/system commands = agent's terminal tool directly** (with `; exit`)
3. **Always add `; exit`** (not `&& exit`) for automation
4. **Don't wrap unnecessarily** (causes confusion and overhead)
5. **Clarity over consistency** (different approaches for different command types)

## 📝 For Agent Configuration File Authors

**When creating or updating agent-specific configuration files:**

1. **Reference this master document** instead of duplicating rules
2. **Provide agent-specific tool mappings** (e.g., Cursor uses `run_terminal_cmd`, Warp uses `run_command`)
3. **Link to this document** for complete details
4. **Keep agent-specific files focused** on agent-specific implementation details

**Example reference format:**
```markdown
## Terminal Execution Protocol

**MANDATORY**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` for complete rules.

**Quick Reference for [Agent Name]:**
- Python scripts → `python3 scripts/terminal_wrapper.py --script <script>`
- Node.js commands → `[agent_tool]("npx <command> ; exit")`
- System commands → `[agent_tool]("<command> ; exit")`
- Always add `; exit` to prevent hanging
```

## 🔗 Related Documentation

- **Universal Instructions**: `universal_instructions.md` - Core AI agent principles
- **Universal Terminal Protocol**: `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md` - Complete universal protocol
- **Terminal Tool Replacement**: `terminal-tool-replacement.md` - Complete guide
- **When to Use Wrapper**: `when-to-use-terminal-wrapper.md` - Decision guide
- **Why && exit Works**: `why-&&-exit-works.md` - Technical details
- **Agent Discovery Guide**: `AGENT_DISCOVERY_GUIDE.md` - How agents find documentation
- **Master Index**: `../MASTER_DOCUMENTATION_INDEX.md` - All documentation

---

**Status**: Master Reference (Single Source of Truth)  
**Last Updated**: November 15, 2025  
**Version**: 1.0  
**Purpose**: Central reference for all agent-specific configuration files

