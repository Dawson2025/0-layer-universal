---
resource_id: "8af790c4-abad-4376-8797-b0306f3bd7bc"
resource_type: "document"
resource_name: "terminal-tool-replacement"
---
# Terminal Tool Replacement System
*Universal AI Agent Terminal Execution Protocol*

<!-- section_id: "df8707f1-f5fe-4040-ae6b-f6c3e3e89033" -->
## 🚨 **CRITICAL: Terminal Tool Hanging Issue**

**PROBLEM**: The `run_terminal_cmd` tool has a known bug where it hangs indefinitely after executing Python scripts, even though the scripts complete successfully.

**SOLUTION**: Use our robust script runner system instead.

<!-- section_id: "d07316c7-fa43-4726-b779-6282e71c8002" -->
## 🔧 **Mandatory Terminal Tool Replacement**

<!-- section_id: "dbc0195f-02b4-4a15-8526-289521ff775a" -->
### **❌ NEVER USE:**
```python
run_terminal_cmd("python3 scripts/script_name.py")
```

<!-- section_id: "d37f761c-7e0a-4edb-a02d-eec37321f192" -->
### **✅ ALWAYS USE:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/script_name.py
```

<!-- section_id: "6c3cb817-47ed-4d51-afa2-fee8f30e7a72" -->
## 📋 **Universal Terminal Execution Rules**

<!-- section_id: "9816f52f-67e7-4301-9117-e177ab41473b" -->
### **Rule 1: Python Scripts**
**For ANY Python script execution:**
- **Use**: `python3 scripts/terminal_wrapper.py --script <script_path> [args...]`
- **Never use**: `run_terminal_cmd` with Python scripts
- **Timeout**: Default 30 seconds (configurable)

<!-- section_id: "33ac2d80-9dcf-4748-9eae-eeb163fd6535" -->
### **Rule 2: Shell Commands**
**For shell commands:**
- **Use**: `python3 scripts/terminal_wrapper.py "<command>"`
- **Alternative**: `run_terminal_cmd` only for simple, non-interactive commands
- **Timeout**: Always specify explicit timeouts

<!-- section_id: "5a90224b-64f0-45e2-af8f-70cdc0ac808a" -->
### **Rule 3: Complex Scripts**
**For complex or long-running scripts:**
- **Use**: `python3 scripts/robust_script_runner.py <script_path> [args...]`
- **Features**: Real-time output, timeout protection, error handling
- **Monitoring**: Built-in process monitoring and cleanup

<!-- section_id: "f7e110fc-0942-4f9b-8ba2-b90497f67fa4" -->
## 🛠️ **Available Tools**

<!-- section_id: "69bb8b20-3a05-4ed4-8c1e-4b80ab68cd80" -->
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

<!-- section_id: "c7a87b51-ebe0-4391-8682-5f43d37bc6c6" -->
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

<!-- section_id: "880eda5e-7016-4e1c-a542-7ab58f3724a1" -->
### **3. Script Monitor (`scripts/run_with_visibility.py`)**
**Enhanced visibility and monitoring**
```bash
# Run with visibility
python3 scripts/run_with_visibility.py scripts/script.py 30

# Monitor long-running scripts
python3 scripts/run_with_visibility.py scripts/deploy.py 300
```

<!-- section_id: "d7acaf86-a067-48de-9a5f-6bd8ba6681ca" -->
## 📊 **Tool Selection Guide**

| Use Case | Tool | Command |
|----------|------|---------|
| **Python Scripts** | `terminal_wrapper.py` | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell Commands** | `terminal_wrapper.py` | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Complex Scripts** | `robust_script_runner.py` | `python3 scripts/robust_script_runner.py <script>` |
| **Long-running Scripts** | `run_with_visibility.py` | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Simple Commands** | `run_terminal_cmd` | `run_terminal_cmd("echo 'test'")` |

<!-- section_id: "4c56708c-ff86-4629-98f6-af8e1b6d224a" -->
## ⚠️ **Critical Warnings**

<!-- section_id: "17ebfdaa-cf0a-421b-a0ae-e9633f948dbf" -->
### **NEVER Use `run_terminal_cmd` For:**
- ❌ Python scripts (will hang)
- ❌ Interactive commands
- ❌ Long-running processes
- ❌ Scripts with complex output
- ❌ Any command that might not exit cleanly

<!-- section_id: "d278a37e-a539-482c-b272-c5ea27c43257" -->
### **ALWAYS Use Our Tools For:**
- ✅ Python script execution
- ✅ Complex shell commands
- ✅ Long-running processes
- ✅ Scripts requiring monitoring
- ✅ Any critical operations

<!-- section_id: "12f86be9-8eb0-4038-9a3c-5d0fc06ee5db" -->
## 🔍 **Verification Commands**

<!-- section_id: "17ac1f2b-d7ab-4900-96c3-38d01392a5bf" -->
### **Test Terminal Wrapper:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/simple_test.py
```

<!-- section_id: "4b8651b8-7a15-4dd8-abc5-81a575823516" -->
### **Test Robust Runner:**
```bash
python3 scripts/robust_script_runner.py scripts/simple_test.py
```

<!-- section_id: "93fc9cbb-255a-4d32-a3de-70e0b16b42ab" -->
### **Test Script Monitor:**
```bash
python3 scripts/run_with_visibility.py scripts/simple_test.py 10
```

<!-- section_id: "d07abb59-b185-416b-972c-24bef991bfde" -->
## 📝 **Implementation Examples**

<!-- section_id: "2b4b5cef-2eee-4b7d-86d3-2713f4ed0f97" -->
### **Example 1: Running Verification Script**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/quick_verify.py")

# NEW (works perfectly):
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

<!-- section_id: "9535cb0f-723a-4b94-b364-b300fafc1c6e" -->
### **Example 2: Running Complex Setup**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/setup_environment.py --verbose")

# NEW (works perfectly):
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py --verbose
```

<!-- section_id: "c7f5d767-a147-492e-9610-fa25c75343f1" -->
### **Example 3: Running Long Process**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/deploy.py")

# NEW (works perfectly):
python3 scripts/run_with_visibility.py scripts/deploy.py 300
```

<!-- section_id: "2bfc1432-edcb-4c68-9224-366f5aafc71c" -->
## 🎯 **Agent-Specific Implementation**

<!-- section_id: "406393b4-5b36-4528-946a-d0c417968be7" -->
### **For Cursor Agent**
- **Primary Tool**: `terminal_wrapper.py`
- **Fallback**: `robust_script_runner.py` for complex tasks
- **Monitoring**: `run_with_visibility.py` for long processes

<!-- section_id: "e68b4f0f-831c-4dc5-861f-9cea0219b303" -->
### **For Claude Code Agent**
- **Primary Tool**: `terminal_wrapper.py`
- **Integration**: Use with VS Code terminal integration
- **Debugging**: `run_with_visibility.py` for debugging

<!-- section_id: "8dc63245-357b-4284-8768-509c288967d8" -->
### **For Warp AI Assistant**
- **Primary Tool**: `terminal_wrapper.py`
- **Command Integration**: Use with `run_command` tool
- **Monitoring**: Built-in process monitoring

<!-- section_id: "dd2104f2-b621-46ae-98b6-1e5cd1210940" -->
## 🚀 **Benefits of Our Solution**

✅ **No More Hanging**: Scripts complete properly without infinite waiting  
✅ **Real-time Output**: See output as it's generated  
✅ **Timeout Protection**: Long-running scripts are automatically terminated  
✅ **Error Handling**: Proper capture and reporting of errors  
✅ **Process Monitoring**: Built-in monitoring and cleanup  
✅ **Easy to Use**: Simple command-line interface  
✅ **Reliable**: Tested and proven to work  

<!-- section_id: "3bc5fc7b-abab-4d9a-b7b9-6c4cec21afd6" -->
## 📚 **Documentation References**

- **Terminal Hanging Solution**: `scripts/TERMINAL_HANGING_SOLUTION.md`
- **Cursor Agent Solution**: `scripts/CURSOR_AGENT_TERMINAL_HANGING_SOLUTION.md`
- **Tool Documentation**: Individual tool files in `scripts/`

---

**⚠️ CRITICAL REMINDER: Always use our robust script runner system instead of `run_terminal_cmd` for Python scripts to prevent hanging issues!**
