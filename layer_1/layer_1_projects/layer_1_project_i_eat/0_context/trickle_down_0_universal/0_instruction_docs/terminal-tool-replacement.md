---
resource_id: "1f84209e-1548-4297-afee-fd52ffd5ac2f"
resource_type: "document"
resource_name: "terminal-tool-replacement"
---
# Terminal Tool Replacement System
*Universal AI Agent Terminal Execution Protocol*

<!-- section_id: "08783f80-3dc0-4072-b388-6ae97aad6adb" -->
## 🚨 **CRITICAL: Terminal Tool Hanging Issue**

**PROBLEM**: The `run_terminal_cmd` tool has a known bug where it hangs indefinitely after executing Python scripts, even though the scripts complete successfully.

**SOLUTION**: Use our robust script runner system instead.

<!-- section_id: "e0530699-f453-475a-b492-3e700c62b830" -->
## 🔧 **Mandatory Terminal Tool Replacement**

<!-- section_id: "9b071c45-40ed-4cea-9919-d317d867a87a" -->
### **❌ NEVER USE:**
```python
run_terminal_cmd("python3 scripts/script_name.py")
```

<!-- section_id: "6b83f3de-7db8-4250-b9f0-375224d980a9" -->
### **✅ ALWAYS USE:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/script_name.py
```

<!-- section_id: "f849dda6-b997-4185-88d3-c421cc0928e3" -->
## 📋 **Universal Terminal Execution Rules**

<!-- section_id: "da770cf8-4eaf-43a0-a62c-24ca0ec28f4a" -->
### **Rule 1: Python Scripts**
**For ANY Python script execution:**
- **Use**: `python3 scripts/terminal_wrapper.py --script <script_path> [args...]`
- **Never use**: `run_terminal_cmd` with Python scripts
- **Timeout**: Default 30 seconds (configurable)

<!-- section_id: "525a7bff-0333-428c-864c-e1a6594d4d68" -->
### **Rule 2: Shell Commands**
**For shell commands:**
- **Use**: `python3 scripts/terminal_wrapper.py "<command>"`
- **Alternative**: `run_terminal_cmd` only for simple, non-interactive commands
- **Timeout**: Always specify explicit timeouts

<!-- section_id: "4e567a16-9c62-441b-bcb2-4ff6812042ef" -->
### **Rule 3: Complex Scripts**
**For complex or long-running scripts:**
- **Use**: `python3 scripts/robust_script_runner.py <script_path> [args...]`
- **Features**: Real-time output, timeout protection, error handling
- **Monitoring**: Built-in process monitoring and cleanup

<!-- section_id: "69cf8118-0a82-44cb-969f-d44d9140ae4f" -->
## 🛠️ **Available Tools**

<!-- section_id: "e2a26ac9-7678-4737-94d1-90dc110dce4d" -->
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

<!-- section_id: "483acb2c-e68d-40d2-891f-7a7d6143cdcb" -->
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

<!-- section_id: "77f25a65-9e45-4b12-88a6-ffc4b36e7449" -->
### **3. Script Monitor (`scripts/run_with_visibility.py`)**
**Enhanced visibility and monitoring**
```bash
# Run with visibility
python3 scripts/run_with_visibility.py scripts/script.py 30

# Monitor long-running scripts
python3 scripts/run_with_visibility.py scripts/deploy.py 300
```

<!-- section_id: "d397b4bb-907b-4b5b-98b8-5ba1e63a90d1" -->
## 📊 **Tool Selection Guide**

| Use Case | Tool | Command |
|----------|------|---------|
| **Python Scripts** | `terminal_wrapper.py` | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell Commands** | `terminal_wrapper.py` | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Complex Scripts** | `robust_script_runner.py` | `python3 scripts/robust_script_runner.py <script>` |
| **Long-running Scripts** | `run_with_visibility.py` | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Simple Commands** | `run_terminal_cmd` | `run_terminal_cmd("echo 'test'")` |

<!-- section_id: "c15f2f16-39c0-4b53-919a-018789190ca1" -->
## ⚠️ **Critical Warnings**

<!-- section_id: "04f78b55-9057-4e89-ae5a-b809a713adb0" -->
### **NEVER Use `run_terminal_cmd` For:**
- ❌ Python scripts (will hang)
- ❌ Interactive commands
- ❌ Long-running processes
- ❌ Scripts with complex output
- ❌ Any command that might not exit cleanly

<!-- section_id: "6583d91a-ffa6-476d-bb09-9e10af6e88ed" -->
### **ALWAYS Use Our Tools For:**
- ✅ Python script execution
- ✅ Complex shell commands
- ✅ Long-running processes
- ✅ Scripts requiring monitoring
- ✅ Any critical operations

<!-- section_id: "f87bd164-5735-4599-a18e-8b3e2e3dad35" -->
## 🔍 **Verification Commands**

<!-- section_id: "400c2b63-77ac-4118-947e-2e4031058596" -->
### **Test Terminal Wrapper:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/simple_test.py
```

<!-- section_id: "7f9ba9d4-fa86-44b5-97d3-3ba41be7b2e4" -->
### **Test Robust Runner:**
```bash
python3 scripts/robust_script_runner.py scripts/simple_test.py
```

<!-- section_id: "b0e880b3-7400-4b7e-967e-f9ab1562ea9e" -->
### **Test Script Monitor:**
```bash
python3 scripts/run_with_visibility.py scripts/simple_test.py 10
```

<!-- section_id: "805a43cc-5c38-4a0d-9585-ccb896be9cc8" -->
## 📝 **Implementation Examples**

<!-- section_id: "c0e61030-d071-4ec0-b1be-3fb91d13e28a" -->
### **Example 1: Running Verification Script**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/quick_verify.py")

# NEW (works perfectly):
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

<!-- section_id: "7fd08d69-2065-4c73-bf49-0dd9effc15fd" -->
### **Example 2: Running Complex Setup**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/setup_environment.py --verbose")

# NEW (works perfectly):
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py --verbose
```

<!-- section_id: "486948de-e47f-4f1b-8527-3c5dd554dd78" -->
### **Example 3: Running Long Process**
```bash
# OLD (hangs):
run_terminal_cmd("python3 scripts/deploy.py")

# NEW (works perfectly):
python3 scripts/run_with_visibility.py scripts/deploy.py 300
```

<!-- section_id: "b621d4b3-7154-45ed-8b5b-5abaa2757666" -->
## 🎯 **Agent-Specific Implementation**

<!-- section_id: "e58e877a-4e87-48d3-a3d2-02b80d7e9d3f" -->
### **For Cursor Agent**
- **Primary Tool**: `terminal_wrapper.py`
- **Fallback**: `robust_script_runner.py` for complex tasks
- **Monitoring**: `run_with_visibility.py` for long processes

<!-- section_id: "f3dbcb31-9664-4066-b5d6-9b8ad918524d" -->
### **For Claude Code Agent**
- **Primary Tool**: `terminal_wrapper.py`
- **Integration**: Use with VS Code terminal integration
- **Debugging**: `run_with_visibility.py` for debugging

<!-- section_id: "2bfa6df6-d999-4985-82ac-4229283decda" -->
### **For Warp AI Assistant**
- **Primary Tool**: `terminal_wrapper.py`
- **Command Integration**: Use with `run_command` tool
- **Monitoring**: Built-in process monitoring

<!-- section_id: "7a28760e-b607-4ab7-ae52-aebe7ab108d9" -->
## 🚀 **Benefits of Our Solution**

✅ **No More Hanging**: Scripts complete properly without infinite waiting  
✅ **Real-time Output**: See output as it's generated  
✅ **Timeout Protection**: Long-running scripts are automatically terminated  
✅ **Error Handling**: Proper capture and reporting of errors  
✅ **Process Monitoring**: Built-in monitoring and cleanup  
✅ **Easy to Use**: Simple command-line interface  
✅ **Reliable**: Tested and proven to work  

<!-- section_id: "fade9495-19cd-4743-baf2-c9d16877cd48" -->
## 📚 **Documentation References**

- **Terminal Hanging Solution**: `scripts/TERMINAL_HANGING_SOLUTION.md`
- **Cursor Agent Solution**: `scripts/CURSOR_AGENT_TERMINAL_HANGING_SOLUTION.md`
- **Tool Documentation**: Individual tool files in `scripts/`

---

**⚠️ CRITICAL REMINDER: Always use our robust script runner system instead of `run_terminal_cmd` for Python scripts to prevent hanging issues!**
