---
resource_id: "8d874630-726f-47d5-b767-e6387dd19e62"
resource_type: "rule"
resource_name: "CURSOR_USER_RULES"
---
# Cursor User Rules - Copy & Paste Ready

## 🚨 **CRITICAL: Terminal Tool Replacement Rules**

**MASTER REFERENCE**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_DOCUMENTATION.md` for complete documentation.

**Cursor-Specific Terminal Solutions**: See `0_context/trickle_down_0_universal/0_instruction_docs/CURSOR_TERMINAL_EXECUTION.md` for Cursor-specific terminal hanging solutions.

Copy and paste the following into your Cursor User Rules:

---

**TERMINAL EXECUTION PROTOCOL - MANDATORY**

Due to a known bug in Cursor's `run_terminal_cmd` tool that causes hanging on Python scripts, you MUST use our robust script runner system instead.

**NEVER USE:**
- `run_terminal_cmd("python3 scripts/script_name.py")` - This will hang indefinitely

**ALWAYS USE:**
- `python3 scripts/terminal_wrapper.py --script scripts/script_name.py` - This works perfectly

**QUICK REFERENCE:**
- Python scripts: `python3 scripts/terminal_wrapper.py --script <script_path>`
- Shell commands (complex): `python3 scripts/terminal_wrapper.py "<command> ; exit"`
- Node.js commands: `run_terminal_cmd("npx <command> ; exit")` or `run_terminal_cmd("npm <command> ; exit")`
- System commands: `run_terminal_cmd("apt install <package> ; exit")` or `run_terminal_cmd("wget <url> ; exit")`
- Long processes: `python3 scripts/run_with_visibility.py <script> <timeout>`
- Complex scripts: `python3 scripts/robust_script_runner.py <script>`

**WHEN TO USE WRAPPER:**
- ✅ Python scripts (always)
- ✅ Complex shell commands
- ✅ Commands that might hang

**WHEN NOT TO USE WRAPPER:**
- ✅ Node.js commands (`npx`, `npm`) - Can use `run_terminal_cmd` directly
- ✅ System package managers (`apt`, `apt-get`) - Can use `run_terminal_cmd` directly
- ✅ Simple commands (`ls`, `echo`, `cat`) - Can use `run_terminal_cmd` directly

**CRITICAL: Always add `; exit` to commands (whether using wrapper or `run_terminal_cmd`) to prevent hanging on both success and failure**

**EXAMPLES:**

**Python Scripts (ALWAYS use wrapper):**
```bash
# Instead of: run_terminal_cmd("python3 scripts/quick_verify.py")
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py

# Instead of: run_terminal_cmd("python3 scripts/setup.py --verbose")
python3 scripts/terminal_wrapper.py --script scripts/setup.py --verbose
```

**Node.js Commands (Can use run_terminal_cmd directly):**
```bash
# ✅ CORRECT - Node.js commands don't need wrapper
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
run_terminal_cmd("npm install ; exit")

# ❌ UNNECESSARY - Don't wrap Node.js commands
# python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

**System Commands (Can use run_terminal_cmd directly):**
```bash
# ✅ CORRECT - System commands don't need wrapper
run_terminal_cmd("sudo apt install ./package.deb ; exit")
run_terminal_cmd("wget https://example.com/file.deb ; exit")

# ❌ UNNECESSARY - Don't wrap simple system commands
# python3 scripts/terminal_wrapper.py "apt install package ; exit"
```

**Complex Shell Commands (Use wrapper for better handling):**
```bash
# ✅ CORRECT - Complex commands benefit from wrapper
python3 scripts/terminal_wrapper.py "quarto render ; exit"
python3 scripts/terminal_wrapper.py "curl -s https://api.example.com | jq . ; exit"
```

**WHY `; exit`?**
- `; exit` always closes terminal (works for both success AND failure)
- Prevents hanging on failed commands (unlike `&& exit` which only works on success)
- Completion detection is more critical than exit code checking in automation

**CRITICAL WARNINGS:**
- ❌ NEVER use `run_terminal_cmd` for Python scripts (will hang)
- ❌ NEVER use `run_terminal_cmd` for interactive commands
- ❌ NEVER use `run_terminal_cmd` for long-running processes
- ✅ ALWAYS use our robust script runner for Python scripts
- ✅ ALWAYS use our robust script runner for complex commands
- ✅ ALWAYS use our robust script runner for critical operations

**BENEFITS:**
- ✅ No hanging - scripts complete properly (both success and failure with `; exit`)
- ✅ Real-time output display
- ✅ Timeout protection
- ✅ Proper error handling
- ✅ Clean process management
- ✅ Always closes terminal - prevents hanging on failed commands

**VERIFICATION:**
Test the solution with: `python3 scripts/terminal_wrapper.py --script scripts/simple_test.py`

---

## 📋 **How to Add to Cursor Settings**

1. **Open Cursor Settings** (Ctrl/Cmd + ,)
2. **Go to "Rules for AI"** section
3. **Paste the rules above** into the text area
4. **Save settings**

## 🎯 **What This Accomplishes**

- **Prevents terminal hanging** on Python script execution
- **Ensures consistent behavior** across all AI interactions
- **Provides clear guidance** for tool selection
- **Maintains productivity** without manual intervention
- **Eliminates the need** to remember specific commands

## ✅ **Testing the Rules**

After adding these rules, test with:
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

You should see:
- ✅ Real-time output display
- ✅ Script completion without hanging
- ✅ Return to normal terminal prompt
- ✅ No manual intervention needed

---

**🚀 This ensures all AI agents will automatically use the robust terminal solution!**
