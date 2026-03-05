---
resource_id: "11041ecb-3399-4776-a520-03882781b580"
resource_type: "rule"
resource_name: "CURSOR_TERMINAL_EXECUTION"
---
# Cursor Terminal Execution
*Cursor-Specific Terminal Solutions*

<!-- section_id: "095627dd-00ea-41d4-bf25-7d16bba5fc06" -->
## Purpose

This document provides **Cursor-specific solutions** for terminal execution issues. The terminal hanging problem and Python wrapper solution are **Cursor-specific only** and do not apply to other agents.

<!-- section_id: "5ee6c7bf-602b-4551-a21a-14af1ca77725" -->
## Location

**Universal Location**: `0_context/trickle_down_0_universal/0_instruction_docs/CURSOR_TERMINAL_EXECUTION.md`

**Referenced by**: `CURSOR_AGENT_GUIDE.md` and `MASTER_DOCUMENTATION.md`

---

<!-- section_id: "53dede42-88d3-4174-9081-210b0e26ed60" -->
## Cursor-Specific Problem: Terminal Hanging

<!-- section_id: "0d4fa097-30bb-4eea-a208-1b6ba73083e1" -->
### Issue

The `run_terminal_cmd` tool in Cursor has a known bug where it hangs indefinitely after executing Python scripts, even though the scripts complete successfully.

<!-- section_id: "cd837393-882a-4bf8-b949-ab0959e9761a" -->
### Solution: Python Wrapper

**For Python scripts in Cursor, ALWAYS use the terminal wrapper:**

```bash
# ✅ CORRECT - Use terminal wrapper
python3 scripts/terminal_wrapper.py --script scripts/script.py

# ❌ WRONG - Will hang in Cursor
run_terminal_cmd("python3 scripts/script.py")
```

**Why**: The wrapper solves subprocess communication problems specific to Cursor's terminal handling.

<!-- section_id: "4707349e-cfce-46d8-812c-88dedfe409ce" -->
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

<!-- section_id: "62ca66dc-8961-4144-9ef3-8f06ec2e1600" -->
## Cursor Terminal Execution Rules

<!-- section_id: "0fd35a04-e106-416a-ac3e-9e250bae7956" -->
### Rule 1: Python Scripts - ALWAYS Use Terminal Wrapper

**For ANY Python script execution in Cursor:**
```bash
# ✅ CORRECT
python3 scripts/terminal_wrapper.py --script scripts/script.py

# ❌ WRONG - Will hang
run_terminal_cmd("python3 scripts/script.py")
```

<!-- section_id: "ba35904f-f557-41df-abe7-f662b9da7ecc" -->
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

<!-- section_id: "8b331754-acc9-4923-b774-2769ef26c23a" -->
### Rule 3: System Commands - Use run_terminal_cmd Directly

**For system commands in Cursor:**
```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("sudo apt install ./package.deb ; exit")
run_terminal_cmd("wget https://example.com/file.deb ; exit")

# ❌ UNNECESSARY - Don't wrap simple system commands
python3 scripts/terminal_wrapper.py "apt install package ; exit"
```

<!-- section_id: "68b94fb8-8440-4505-8bf0-f1f288cee0ee" -->
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

<!-- section_id: "587630b4-c1e8-46c8-844c-f2ce49237edb" -->
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

<!-- section_id: "ab034f86-c7ff-4372-ad62-fb34810b9b76" -->
## Common Examples

<!-- section_id: "bfe45369-0328-47a8-9b43-e9f73b4c778e" -->
### Python Scripts (ALWAYS use wrapper)
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
python3 scripts/terminal_wrapper.py --script scripts/setup.py --verbose
```

<!-- section_id: "4713431e-2a77-43ba-ab46-80893377dc84" -->
### Node.js Commands (Use run_terminal_cmd directly)
```bash
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
run_terminal_cmd("npm install ; exit")
```

<!-- section_id: "6a3d1a0c-8161-4d40-a3a9-72fd8419c477" -->
### System Commands (Use run_terminal_cmd directly)
```bash
run_terminal_cmd("sudo apt install ./package.deb ; exit")
run_terminal_cmd("wget https://example.com/file.deb ; exit")
```

---

<!-- section_id: "e2d1df7e-8051-472b-b442-a7427c01bd68" -->
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

