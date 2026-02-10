# Cursor Terminal Execution
*Cursor-Specific Terminal Solutions*

## Purpose

This document provides **Cursor-specific solutions** for terminal execution issues. The terminal hanging problem and Python wrapper solution are **Cursor-specific only** and do not apply to other agents.

## Location

**Universal Location**: `0_context/trickle_down_0_universal/0_instruction_docs/CURSOR_TERMINAL_EXECUTION.md`

**Referenced by**: `CURSOR_AGENT_GUIDE.md` and `MASTER_DOCUMENTATION.md`

---

## Cursor-Specific Problem: Terminal Hanging

### Issue

The `run_terminal_cmd` tool in Cursor has a known bug where it hangs indefinitely after executing Python scripts, even though the scripts complete successfully.

### Solution: Python Wrapper

**For Python scripts in Cursor, ALWAYS use the terminal wrapper:**

```bash
# ✅ CORRECT - Use terminal wrapper
python3 scripts/terminal_wrapper.py --script scripts/script.py

# ❌ WRONG - Will hang in Cursor
run_terminal_cmd("python3 scripts/script.py")
```

**Why**: The wrapper solves subprocess communication problems specific to Cursor's terminal handling.

### Solution: `; exit` Workaround

**For ALL commands in Cursor, add `; exit`:**

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
- This is a Cursor-specific workaround

---

## Cursor Terminal Execution Rules

### Rule 1: Python Scripts - ALWAYS Use Terminal Wrapper

**For ANY Python script execution in Cursor:**
```bash
# ✅ CORRECT
python3 scripts/terminal_wrapper.py --script scripts/script.py

# ❌ WRONG - Will hang
run_terminal_cmd("python3 scripts/script.py")
```

### Rule 2: Node.js Commands - Use run_terminal_cmd Directly

**For Node.js commands in Cursor:**
```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
run_terminal_cmd("npm install ; exit")

# ❌ UNNECESSARY - Don't wrap Node.js commands
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

**Why**: Node.js commands don't have the Python subprocess hanging issue.

### Rule 3: System Commands - Use run_terminal_cmd Directly

**For system commands in Cursor:**
```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("sudo apt install ./package.deb ; exit")
run_terminal_cmd("wget https://example.com/file.deb ; exit")

# ❌ UNNECESSARY - Don't wrap simple system commands
python3 scripts/terminal_wrapper.py "apt install package ; exit"
```

### Rule 4: Always Add `; exit` to Commands

**For ALL commands in Cursor:**
```bash
# ✅ CORRECT - Always add ; exit
run_terminal_cmd("npx playwright install chromium ; exit")
python3 scripts/terminal_wrapper.py "quarto render ; exit"

# ❌ WRONG - May hang on failure
run_terminal_cmd("npx playwright install chromium && exit")
```

---

## Quick Decision Tree for Cursor

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

---

## Common Examples

### Python Scripts (ALWAYS use wrapper)
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
python3 scripts/terminal_wrapper.py --script scripts/setup.py --verbose
```

### Node.js Commands (Use run_terminal_cmd directly)
```bash
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
run_terminal_cmd("npm install ; exit")
```

### System Commands (Use run_terminal_cmd directly)
```bash
run_terminal_cmd("sudo apt install ./package.deb ; exit")
run_terminal_cmd("wget https://example.com/file.deb ; exit")
```

---

## Related Documentation

- **Master Documentation**: `MASTER_DOCUMENTATION.md` - Complete overview
- **Universal Terminal**: `UNIVERSAL_TERMINAL_EXECUTION.md` - Universal best practices
- **Cursor Agent Guide**: `CURSOR_AGENT_GUIDE.md` - All Cursor-specific solutions
- **Terminal Tool Replacement**: `terminal-tool-replacement.md` - Complete guide
- **When to Use Wrapper**: `when-to-use-terminal-wrapper.md` - Decision guide
- **Why && exit Works**: `why-&&-exit-works.md` - Technical details
- **Cursor Terminal Issues**: `cursor_terminal_issues.md` - Detailed Cursor issues

---

**Status**: Cursor-Specific (does not apply to other agents)  
**Last Updated**: November 15, 2025  
**Version**: 1.0  
**Purpose**: Cursor-specific terminal execution solutions

