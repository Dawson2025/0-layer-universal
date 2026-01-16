# When to Use Terminal Wrapper vs. run_terminal_cmd

## Overview

The terminal wrapper is designed to solve **Python script hanging issues** in Cursor. However, **not all commands need the wrapper**. This guide clarifies when to use it and when not to.

## ✅ **USE Terminal Wrapper For:**

### 1. Python Scripts (ALWAYS)
**Why**: Python scripts are the primary cause of Cursor's hanging issues.

```bash
# ✅ ALWAYS use wrapper for Python scripts
python3 scripts/terminal_wrapper.py --script scripts/script.py

# ❌ NEVER use run_terminal_cmd for Python scripts
run_terminal_cmd("python3 scripts/script.py")  # Will hang!
```

### 2. Complex Shell Commands
**Why**: Complex commands benefit from timeout protection and better error handling.

```bash
# ✅ Use wrapper for complex commands
python3 scripts/terminal_wrapper.py "quarto render ; exit"
python3 scripts/terminal_wrapper.py "command1 | command2 | command3 ; exit"

# ✅ Can also use run_terminal_cmd with ; exit
run_terminal_cmd("quarto render ; exit")
```

### 3. Commands That Might Hang
**Why**: Wrapper provides timeout protection and process monitoring.

```bash
# ✅ Use wrapper for potentially long-running commands
python3 scripts/terminal_wrapper.py "long_running_script.sh ; exit"
```

## ❌ **DON'T Use Terminal Wrapper For:**

### 1. Node.js Commands (`npx`, `npm`)
**Why**: Node.js commands don't have the same hanging issues as Python scripts. The wrapper is unnecessary overhead.

```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
run_terminal_cmd("npm install ; exit")
run_terminal_cmd("npx @playwright/mcp@latest ; exit")

# ❌ UNNECESSARY - Don't wrap Node.js commands
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

**Examples:**
- `npx playwright install chromium` - Node.js command, use `run_terminal_cmd` directly
- `npm install` - Node.js command, use `run_terminal_cmd` directly
- `npx @playwright/mcp@latest` - Node.js command, use `run_terminal_cmd` directly

### 2. System Package Managers (`apt`, `apt-get`, `yum`, etc.)
**Why**: System commands are typically fast and don't have Python subprocess issues.

```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("sudo apt install ./package.deb ; exit")
run_terminal_cmd("sudo apt-get update ; exit")

# ❌ UNNECESSARY - Don't wrap simple system commands
python3 scripts/terminal_wrapper.py "apt install package ; exit"
```

### 3. Simple Shell Commands
**Why**: Simple commands don't need the wrapper's complexity.

```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("ls -la ; exit")
run_terminal_cmd("echo 'test' ; exit")
run_terminal_cmd("cat file.txt ; exit")
run_terminal_cmd("git status ; exit")

# ❌ UNNECESSARY - Don't wrap simple commands
python3 scripts/terminal_wrapper.py "ls -la ; exit"
```

### 4. Download Commands (`wget`, `curl` for downloads)
**Why**: These are simple system commands that don't need wrapper overhead.

```bash
# ✅ CORRECT - Use run_terminal_cmd directly
run_terminal_cmd("wget https://example.com/file.deb ; exit")
run_terminal_cmd("curl -O https://example.com/file.zip ; exit")

# ❌ UNNECESSARY - Don't wrap simple download commands
python3 scripts/terminal_wrapper.py "wget https://example.com/file.deb ; exit"
```

## 📋 **Decision Tree**

```
Is it a Python script?
├─ YES → ✅ Use terminal_wrapper.py --script
└─ NO → Is it a Node.js command (npx, npm)?
    ├─ YES → ✅ Use run_terminal_cmd with ; exit
    └─ NO → Is it a simple system command?
        ├─ YES → ✅ Use run_terminal_cmd with ; exit
        └─ NO → Is it complex or might hang?
            ├─ YES → ✅ Use terminal_wrapper.py with ; exit
            └─ NO → ✅ Use run_terminal_cmd with ; exit
```

## 🎯 **Key Principle**

**The wrapper solves Python subprocess hanging issues. If it's not a Python script, you probably don't need the wrapper.**

## 📝 **Examples by Category**

### Python Scripts (ALWAYS use wrapper)
```bash
# ✅ CORRECT
python3 scripts/terminal_wrapper.py --script scripts/verify.py
python3 scripts/terminal_wrapper.py --script scripts/setup.py --verbose

# ❌ WRONG
run_terminal_cmd("python3 scripts/verify.py")  # Will hang!
```

### Node.js Commands (Use run_terminal_cmd)
```bash
# ✅ CORRECT
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
run_terminal_cmd("npm install ; exit")
run_terminal_cmd("npx @playwright/mcp@latest ; exit")

# ❌ UNNECESSARY (but will work)
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"
```

### System Commands (Use run_terminal_cmd)
```bash
# ✅ CORRECT
run_terminal_cmd("sudo apt install ./package.deb ; exit")
run_terminal_cmd("wget https://example.com/file.deb ; exit")
run_terminal_cmd("google-chrome --version ; exit")

# ❌ UNNECESSARY (but will work)
python3 scripts/terminal_wrapper.py "apt install package ; exit"
```

### Complex Commands (Wrapper recommended)
```bash
# ✅ RECOMMENDED - Complex commands benefit from wrapper
python3 scripts/terminal_wrapper.py "quarto render ; exit"
python3 scripts/terminal_wrapper.py "command1 | command2 | command3 ; exit"

# ✅ ALSO OK - Simple run_terminal_cmd works too
run_terminal_cmd("quarto render ; exit")
```

## ⚠️ **Important Notes**

1. **Always add `; exit`** - Whether using wrapper or `run_terminal_cmd`, always add `; exit` to prevent hanging
2. **Wrapper can cause confusion** - Using wrapper for Node.js commands can lead to confusion (e.g., using Python Playwright instead of Node.js Playwright)
3. **When in doubt** - For Node.js/system commands, use `run_terminal_cmd` directly (it's clearer)
4. **Python scripts are the priority** - The wrapper was created specifically for Python script hanging issues
5. **Visual clarity matters** - Direct commands (`npx`, `npm`, `apt`) are clearer than wrapped commands

## 🔍 **Why This Matters**

**We were unnecessarily using the wrapper for Node.js commands** because we applied the "always use wrapper" rule too broadly. The wrapper is specifically designed for Python subprocess issues, not for all terminal commands.

**Correct approach:**
- Python scripts → Always use wrapper
- Node.js commands → Use `run_terminal_cmd` with `; exit`
- System commands → Use `run_terminal_cmd` with `; exit`
- Complex commands → Use wrapper (optional but recommended)

## 🔍 **Historical Context: Why This Matters**

### The Playwright Installation Confusion

**Problem**: We experienced issues where browsers were installed using Python Playwright (`python3 -m playwright install`) instead of Node.js Playwright (`npx playwright install`), causing MCP server failures.

**Root Cause**: Using Python wrapper for Node.js commands may have contributed to this confusion:
- Seeing `python3` at the start of commands might suggest using Python tools
- Pattern matching: "If we use Python wrapper, maybe Python Playwright is correct"
- This led to using `python3 -m playwright install` instead of `npx playwright install`

**Solution**: Use `run_terminal_cmd` directly for Node.js commands to make it clear they're Node.js tools, not Python tools.

**See**: `playwright-installation-confusion-analysis.md` for detailed analysis

---

**Summary**: Use the wrapper for Python scripts and complex commands. For Node.js and simple system commands, use `run_terminal_cmd` with `; exit` directly. **This prevents confusion that can lead to using wrong tools (like Python Playwright instead of Node.js Playwright).**

