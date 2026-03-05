---
resource_id: "b8f6c0fb-cdc3-4709-978d-4553b24772b2"
resource_type: "rule"
resource_name: "UNIVERSAL_AGENT_TERMINAL_PROTOCOL"
---
# Universal Agent Terminal Execution Protocol
*For ALL AI Agents: Cursor, Codex, Gemini CLI, Claude Code, Warp, and others*

<!-- section_id: "4b128bbd-9a6b-436b-8b9f-73e90dc31ab6" -->
## 🎯 Purpose

This document provides **universal terminal execution rules** that apply to **ALL AI agents**, regardless of which IDE or platform they're using. This ensures consistent, reliable terminal command execution across all AI agent interactions.

**📌 MASTER REFERENCE**: This document is referenced by `MASTER_TERMINAL_EXECUTION_REFERENCE.md`, which serves as the single source of truth for all agent-specific configuration files. Agent-specific files should reference the master document rather than duplicating rules.

<!-- section_id: "895f6e10-11ca-43aa-b233-a1ad90f70397" -->
## 📍 Location

**Universal Location**: `0_context/trickle_down_0_universal/0_instruction_docs/`

**All agents should read this file** when starting work or when encountering terminal execution issues.

<!-- section_id: "be3d69e1-7722-49a1-adb1-ada8f72b0203" -->
## 🚨 Critical Rules for ALL Agents

<!-- section_id: "215616df-9983-441a-9673-7400a52fa95e" -->
### Rule 1: Python Scripts - ALWAYS Use Terminal Wrapper

**For ANY Python script execution:**
```bash
# ✅ CORRECT - Use terminal wrapper
python3 scripts/terminal_wrapper.py --script scripts/script.py

# ❌ WRONG - Will hang in Cursor and may hang in other agents
run_terminal_cmd("python3 scripts/script.py")
```

**Why**: Python scripts cause hanging issues in Cursor and may cause issues in other agents. The wrapper solves subprocess communication problems.

<!-- section_id: "3225f395-040d-45cf-8371-af1376d7dd25" -->
### Rule 2: Node.js Commands - Use run_terminal_cmd Directly

**For Node.js commands (`npx`, `npm`):**
```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
run_terminal_cmd("npm install ; exit")

# ❌ UNNECESSARY - Don't wrap Node.js commands
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

**Why**: 
- Node.js commands don't have Python subprocess hanging issues
- Wrapping in Python wrapper can cause confusion (e.g., using Python Playwright instead of Node.js Playwright)
- Direct commands are clearer and simpler

<!-- section_id: "f8a0d891-4cfd-40e3-af67-392c3b4ad239" -->
### Rule 3: System Commands - Use run_terminal_cmd Directly

**For system package managers and simple commands:**
```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("sudo apt install ./package.deb ; exit")
run_terminal_cmd("wget https://example.com/file.deb ; exit")
run_terminal_cmd("ls -la ; exit")

# ❌ UNNECESSARY - Don't wrap simple system commands
python3 scripts/terminal_wrapper.py "apt install package ; exit"
```

**Why**: System commands don't need wrapper overhead.

<!-- section_id: "c3f7eb33-2b85-4921-aaa6-5fa8b373a511" -->
### Rule 4: Always Add `; exit` to Commands

**For ALL commands (whether using wrapper or run_terminal_cmd):**
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

<!-- section_id: "1abf79cb-87c8-4f6c-8364-3d253587c225" -->
## 📋 Quick Decision Tree

```
Is it a Python script?
├─ YES → Use: python3 scripts/terminal_wrapper.py --script <script>
└─ NO → Is it Node.js (npx, npm)?
    ├─ YES → Use: run_terminal_cmd("npx <command> ; exit")
    └─ NO → Is it a system command (apt, wget, ls)?
        ├─ YES → Use: run_terminal_cmd("<command> ; exit")
        └─ NO → Is it complex?
            ├─ YES → Use: python3 scripts/terminal_wrapper.py "<command> ; exit"
            └─ NO → Use: run_terminal_cmd("<command> ; exit")
```

<!-- section_id: "433725b1-47bc-4e30-8264-a268a1a6b02f" -->
## 🔧 Agent-Specific Implementation

<!-- section_id: "815eb1a9-c33d-43a6-ac8d-7c63471a2dd6" -->
### For Cursor Agent
- **Tool**: `run_terminal_cmd` (built-in)
- **Python scripts**: Use `python3 scripts/terminal_wrapper.py --script <script>`
- **Other commands**: Use `run_terminal_cmd("<command> ; exit")`
- **Reference**: `terminal-tool-replacement.md`

<!-- section_id: "272ed534-199a-4129-b29d-a81ce3e13e4b" -->
### For Claude Code Agent
- **Tool**: `run_terminal_cmd` (built-in) or VS Code terminal integration
- **Python scripts**: Use `python3 scripts/terminal_wrapper.py --script <script>`
- **Other commands**: Use `run_terminal_cmd("<command> ; exit")` or VS Code terminal
- **Reference**: `terminal-tool-replacement.md`

<!-- section_id: "123ac259-51d4-4c30-8ad8-d228517deee5" -->
### For Codex Agent
- **Tool**: `run_terminal_cmd` (built-in) or VS Code terminal integration
- **Python scripts**: Use `python3 scripts/terminal_wrapper.py --script <script>`
- **Other commands**: Use `run_terminal_cmd("<command> ; exit")` or VS Code terminal
- **Reference**: `terminal-tool-replacement.md`

<!-- section_id: "a9ee64d3-2bdb-41c2-919f-b34491ffc8b8" -->
### For Warp AI Assistant
- **Tool**: `run_command` (Warp's tool)
- **Python scripts**: Use `python3 scripts/terminal_wrapper.py --script <script>`
- **Other commands**: Use `run_command("npx <command> ; exit")` or `run_command("apt install <package> ; exit")`
- **Reference**: `terminal-tool-replacement.md`

<!-- section_id: "9cbd1ddf-166f-4b6b-9bce-8b8904dedc5d" -->
### For Gemini CLI
- **Tool**: Terminal command execution (built-in)
- **Python scripts**: Use `python3 scripts/terminal_wrapper.py --script <script>`
- **Other commands**: Execute directly with `; exit` appended
- **Reference**: `terminal-tool-replacement.md`

<!-- section_id: "7c80c6b7-5ec2-42b2-8b90-dcbcc17c162f" -->
## 📚 Complete Documentation

<!-- section_id: "73ebc27f-f117-434d-8a3b-c25e673e6d9b" -->
### Core Documents (Read These First)

1. **`terminal-tool-replacement.md`** - Complete terminal execution guide
   - When to use wrapper vs run_terminal_cmd
   - Detailed rules and examples
   - Tool selection guide

2. **`when-to-use-terminal-wrapper.md`** - Decision guide
   - When wrapper is needed vs not needed
   - Examples by command type
   - Historical context (Playwright confusion)

3. **`why-&&-exit-works.md`** - Technical explanation
   - Why `; exit` works
   - Why `&& exit` has limitations
   - Best practices

<!-- section_id: "978059e2-0627-4fd9-98b8-49a572550936" -->
### Supporting Documents

4. **`playwright-installation-confusion-analysis.md`** - Root cause analysis
   - Why wrapping Node.js commands caused confusion
   - How to prevent similar issues

5. **`pop-out-terminal-explanation.md`** - UI workaround explanation
   - What "pop out terminal" is
   - Why it works (but not recommended)

6. **`cursor_terminal_issues.md`** - Cursor-specific issues
   - Terminal output handling problems
   - Cursor-specific workarounds

<!-- section_id: "4ad0c4ad-c006-4703-b29f-28bf54a7e2f5" -->
## ✅ Verification Checklist

Before executing any terminal command, verify:

- [ ] Is it a Python script? → Use terminal wrapper
- [ ] Is it Node.js? → Use `run_terminal_cmd` directly
- [ ] Is it a system command? → Use `run_terminal_cmd` directly
- [ ] Did I add `; exit`? → Always add `; exit` to prevent hanging
- [ ] Am I using the right tool? → Check agent-specific implementation above

<!-- section_id: "abc49bc1-ef1f-445d-a516-082f22acdfdf" -->
## 🎯 Key Principles

1. **Python scripts = wrapper** (always)
2. **Node.js/system commands = run_terminal_cmd directly** (with `; exit`)
3. **Always add `; exit`** (not `&& exit`) for automation
4. **Don't wrap unnecessarily** (causes confusion and overhead)
5. **Clarity over consistency** (different approaches for different command types)

<!-- section_id: "c0facf05-2436-4f1c-bd19-79fe01f402aa" -->
## 🔗 Related Documentation

- **Universal Instructions**: `universal_instructions.md` - Core AI agent principles
- **Terminal Tool Replacement**: `terminal-tool-replacement.md` - Complete guide
- **When to Use Wrapper**: `when-to-use-terminal-wrapper.md` - Decision guide
- **Why && exit Works**: `why-&&-exit-works.md` - Technical details
- **Master Index**: `../MASTER_DOCUMENTATION_INDEX.md` - All documentation

<!-- section_id: "17733aaa-0013-4015-ab2f-80d038110a98" -->
## 📝 For Agent Developers

If you're implementing support for a new AI agent:

1. **Read this file first** - Understand the universal rules
2. **Check agent-specific section** - See if your agent is listed
3. **If not listed** - Follow the general pattern:
   - Python scripts → Use terminal wrapper
   - Node.js/system commands → Use agent's native terminal tool with `; exit`
4. **Test thoroughly** - Verify commands complete properly
5. **Document your agent** - Add agent-specific section to this file

---

**Status**: Universal (applies to all AI agents)  
**Last Updated**: November 15, 2025  
**Version**: 2.0 (Updated with `; exit` recommendation and Node.js command clarification)

