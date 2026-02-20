# Terminal Tool Replacement System
*Universal AI Agent Terminal Execution Protocol*

## 🚨 **CRITICAL: Terminal Tool Hanging Issue**

**PROBLEM**: The `run_terminal_cmd` tool has a known bug where it hangs indefinitely after executing **Python scripts**, even though the scripts complete successfully.

**SOLUTION**: 
- **Python scripts**: Use our robust script runner system
- **Other commands**: Use `run_terminal_cmd` with `; exit` workaround

**⚠️ IMPORTANT**: 
- The wrapper is specifically designed for **Python script hanging issues**
- Node.js commands (`npx`, `npm`) don't have the same hanging issues - use `run_terminal_cmd` directly
- System commands (`apt`, `wget`) don't need the wrapper - use `run_terminal_cmd` directly
- Always add `; exit` to prevent hanging on both success and failure

## 🔧 **Mandatory Terminal Tool Replacement**

### **❌ NEVER USE:**
```python
run_terminal_cmd("python3 scripts/script_name.py")
```

### **✅ ALWAYS USE:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/script_name.py
```

## 📋 **Universal Terminal Execution Rules**

### **Rule 1: Python Scripts (ALWAYS use wrapper)**
**For ANY Python script execution:**
- **Use**: `python3 scripts/terminal_wrapper.py --script <script_path> [args...]`
- **Never use**: `run_terminal_cmd` with Python scripts (will hang!)
- **Timeout**: Default 30 seconds (configurable)
- **Why**: Python scripts are the primary cause of Cursor's hanging issues

### **Rule 2: Node.js Commands (Use run_terminal_cmd directly)**
**For Node.js commands (`npx`, `npm`):**
- **Use**: `run_terminal_cmd("npx <command> ; exit")` or `run_terminal_cmd("npm <command> ; exit")`
- **Don't use wrapper**: Node.js commands don't have Python subprocess hanging issues
- **Examples**:
  ```bash
  run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
  run_terminal_cmd("npm install ; exit")
  run_terminal_cmd("npx @playwright/mcp@latest ; exit")
  ```

### **Rule 3: System Commands (Use run_terminal_cmd directly)**
**For system package managers and simple commands:**
- **Use**: `run_terminal_cmd("command ; exit")`
- **Don't use wrapper**: System commands don't need wrapper overhead
- **Examples**:
  ```bash
  run_terminal_cmd("sudo apt install ./package.deb ; exit")
  run_terminal_cmd("wget https://example.com/file.deb ; exit")
  run_terminal_cmd("google-chrome --version ; exit")
  ```

### **Rule 4: Complex Shell Commands (Wrapper optional but recommended)**
**For complex commands that might benefit from timeout protection:**
- **Use**: `python3 scripts/terminal_wrapper.py "<command> ; exit"` (recommended)
- **Alternative**: `run_terminal_cmd("<command> ; exit")` (also works)
- **Examples**:
  ```bash
  python3 scripts/terminal_wrapper.py "quarto render ; exit"
  python3 scripts/terminal_wrapper.py "command1 | command2 | command3 ; exit"
  ```

### **Rule 5: Complex/Long-Running Scripts**
**For complex or long-running Python scripts:**
- **Use**: `python3 scripts/robust_script_runner.py <script_path> [args...]`
- **Features**: Real-time output, timeout protection, error handling
- **Monitoring**: Built-in process monitoring and cleanup

## 🛠️ **Available Tools**

### **1. Terminal Wrapper (`scripts/terminal_wrapper.py`)**
**Primary replacement for `run_terminal_cmd`**
```bash
# Python scripts
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py

# Shell commands
python3 scripts/terminal_wrapper.py "echo 'Hello World'"

# With custom timeout
python3 scripts/terminal_wrapper.py --script scripts/long_script.py --timeout 60
```

### **2. Robust Script Runner (`scripts/robust_script_runner.py`)**
**Advanced script execution with monitoring**
```bash
# Basic usage
python3 scripts/robust_script_runner.py scripts/quick_verify.py

# With arguments
python3 scripts/robust_script_runner.py scripts/script.py arg1 arg2

# With custom timeout
python3 scripts/robust_script_runner.py scripts/script.py --timeout 120
```

### **3. Script Monitor (`scripts/run_with_visibility.py`)**
**Enhanced visibility and monitoring**
```bash
# Run with visibility
python3 scripts/run_with_visibility.py scripts/script.py 30

# Monitor long-running scripts
python3 scripts/run_with_visibility.py scripts/deploy.py 300
```

## 📊 **Tool Selection Guide**

| Use Case | Tool | Command |
|----------|------|---------|
| **Python Scripts** | `terminal_wrapper.py` | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Node.js Commands** | `run_terminal_cmd` | `run_terminal_cmd("npx <command> ; exit")` |
| **System Commands** | `run_terminal_cmd` | `run_terminal_cmd("apt install <package> ; exit")` |
| **Complex Commands** | `terminal_wrapper.py` (optional) | `python3 scripts/terminal_wrapper.py "<command> ; exit"` |
| **Complex Scripts** | `robust_script_runner.py` | `python3 scripts/robust_script_runner.py <script>` |
| **Long-running Scripts** | `run_with_visibility.py` | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Simple Commands** | `run_terminal_cmd` | `run_terminal_cmd("echo 'test' ; exit")` |

## ⚠️ **Critical Warnings**

### **NEVER Use `run_terminal_cmd` For:**
- ❌ Python scripts (will hang - use wrapper instead)
- ❌ Interactive commands (without `; exit`)

### **ALWAYS Use Terminal Wrapper For:**
- ✅ Python script execution (mandatory)
- ✅ Complex shell commands (optional but recommended)

### **ALWAYS Use `run_terminal_cmd` For:**
- ✅ Node.js commands (`npx`, `npm`) - Don't need wrapper
- ✅ System commands (`apt`, `wget`) - Don't need wrapper
- ✅ Simple commands (`ls`, `echo`, `cat`) - Don't need wrapper
- ✅ **Always add `; exit`** to prevent hanging

## 🔍 **Verification Commands**

### **Test Terminal Wrapper:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/simple_test.py
```

### **Test Robust Runner:**
```bash
python3 scripts/robust_script_runner.py scripts/simple_test.py
```

### **Test Script Monitor:**
```bash
python3 scripts/run_with_visibility.py scripts/simple_test.py 10
```

## 📝 **Implementation Examples**

### **Example 1: Running Verification Script**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/quick_verify.py")

# NEW (works perfectly):
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

### **Example 2: Running Complex Setup**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/setup_environment.py --verbose")

# NEW (works perfectly):
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py --verbose
```

### **Example 3: Running Long Process**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/deploy.py")

# NEW (works perfectly):
python3 scripts/run_with_visibility.py scripts/deploy.py 300
```

## 🎯 **Agent-Specific Implementation**

### **For Cursor Agent**
- **Primary Tool**: `terminal_wrapper.py`
- **Fallback**: `robust_script_runner.py` for complex tasks
- **Monitoring**: `run_with_visibility.py` for long processes

### **For Claude Code Agent**
- **Primary Tool**: `terminal_wrapper.py`
- **Integration**: Use with VS Code terminal integration
- **Debugging**: `run_with_visibility.py` for debugging

### **For Warp AI Assistant**
- **Primary Tool**: `terminal_wrapper.py`
- **Command Integration**: Use with `run_command` tool
- **Monitoring**: Built-in process monitoring

## 🚀 **Benefits of Our Solution**

✅ **Reduces Hanging**: Helps with subprocess communication issues  
✅ **Real-time Output**: See output as it's generated  
✅ **Timeout Protection**: Long-running scripts are automatically terminated  
✅ **Error Handling**: Proper capture and reporting of errors  
✅ **Process Monitoring**: Built-in monitoring and cleanup  
✅ **Easy to Use**: Simple command-line interface  
✅ **Proven Methods**: Uses verified subprocess handling techniques

## ⚠️ **Important Limitations**

**The wrapper is a mitigation, not a complete fix:**
- ✅ Helps with subprocess communication deadlocks
- ✅ Provides timeout protection
- ✅ Improves output handling
- ❌ **May not completely solve Cursor's terminal detection issue** - The root cause is in Cursor's shell integration, not subprocess handling
- ❌ Commands may complete successfully but Cursor may not detect completion

**For best results, combine methods:**
1. Use the terminal wrapper for subprocess improvements
2. Add `&& exit` to commands to force terminal closure
3. Use non-interactive flags when possible
4. Wait for Cursor to fix the underlying terminal detection bug

**See**: `METHOD_VERIFICATION_REPORT.md` for detailed research findings  

## 📚 **Documentation References**

- **When to Use Wrapper**: `when-to-use-terminal-wrapper.md` - Detailed guide on when wrapper is needed
- **Why && exit Works**: `why-&&-exit-works.md` - Technical explanation of exit workaround
- **Terminal Hanging Solution**: `scripts/TERMINAL_HANGING_SOLUTION.md`
- **Cursor Agent Solution**: `scripts/CURSOR_AGENT_TERMINAL_HANGING_SOLUTION.md`
- **Tool Documentation**: Individual tool files in `scripts/`

## 🔧 **Recommended Workaround: "&& exit"**

**Status**: ✅ **MOST RECOMMENDED** - Automatic, reliable, no manual intervention required

**Confirmed Effective** (GitHub Issue #3200): Adding `&& exit` to commands forces the terminal to close after completion.

### Why `&& exit` is Recommended

1. **Automatic** - No manual clicking required (unlike "pop out terminal")
2. **Explicit Signal** - `exit` provides unambiguous completion signal that Cursor can detect
3. **Works with Automation** - Doesn't break agent workflows
4. **Preserves Errors** - `&&` only exits on success, preserving error states
5. **Reliable** - Works consistently across different shell configurations
6. **Simple** - Easy to add to any command

### How It Works

The `&&` operator executes `exit` **only if** the previous command succeeds:
- **Success**: Command completes → `exit` runs → Terminal closes → Cursor detects completion ✅
- **Failure**: Command fails → `exit` doesn't run → Error state preserved ⚠️ **BUT terminal may still hang**

**⚠️ Important Limitation**: `&& exit` only prevents hanging on **successful** commands. Failed commands may still hang because `exit` doesn't run.

### For Both Success and Failure Cases

**Use `; exit` instead** to always close the terminal:

```bash
# ✅ Always exits (both success and failure)
python3 scripts/terminal_wrapper.py "quarto render ; exit"
```

**Trade-off**: 
- ✅ Always closes terminal (no hanging on failures)
- ❌ Can't check exit code (but completion detection is more critical)

**Recommended for automation**: Use `; exit` when completion detection is more important than exit code checking.

### Examples

```bash
# ✅ RECOMMENDED FOR AUTOMATION - Always exits (both success/failure)
python3 scripts/terminal_wrapper.py "quarto render ; exit"
python3 scripts/terminal_wrapper.py "python3 script.py ; exit"
python3 scripts/terminal_wrapper.py "npm install ; exit"

# ✅ FOR SUCCESS CASES ONLY - Preserves error states
python3 scripts/terminal_wrapper.py "quarto render && exit"

# ✅ Also works without wrapper (but wrapper is still recommended)
run_terminal_cmd("echo 'test' ; exit")
```

### Best Practice Formulas

**For Automation (Recommended):**
```
Terminal Wrapper + ; exit = Maximum Reliability (Always Closes)
```

**For Success Cases Only:**
```
Terminal Wrapper + && exit = Preserves Error States
```

**Why `; exit` for automation:**
- Prevents hanging on **both** successful and failed commands
- Completion detection is more critical than exit code checking
- Cursor may not reliably detect exit codes anyway

**See**: `why-&&-exit-works.md` for detailed technical explanation

---

**⚠️ CRITICAL REMINDER**: 
- Always use our robust script runner system instead of `run_terminal_cmd` for Python scripts
- Add `&& exit` to commands for better terminal detection
- Understand that these are mitigations - the root cause is Cursor's terminal detection mechanism
- See `METHOD_VERIFICATION_REPORT.md` for detailed research findings
