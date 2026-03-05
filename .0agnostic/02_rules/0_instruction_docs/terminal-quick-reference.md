---
resource_id: "f2dda20e-8da8-476c-b9c1-851487a7dd6f"
resource_type: "rule"
resource_name: "terminal-quick-reference"
---
# Terminal Tool Quick Reference
*Immediate Reference for AI Agents*

## 🚨 **CRITICAL: Use These Commands Instead of `run_terminal_cmd`**

### **Python Scripts**
```bash
# Instead of: run_terminal_cmd("python3 scripts/script.py")
python3 scripts/terminal_wrapper.py --script scripts/script.py

# With arguments:
python3 scripts/terminal_wrapper.py --script scripts/script.py arg1 arg2

# With custom timeout:
python3 scripts/terminal_wrapper.py --script scripts/script.py --timeout 60
```

### **Shell Commands**
```bash
# Instead of: run_terminal_cmd("echo 'test'")
python3 scripts/terminal_wrapper.py "echo 'test'"

# Complex commands:
python3 scripts/terminal_wrapper.py "curl -s https://api.example.com | jq '.'"
```

### **Long-running Scripts**
```bash
# For scripts that might take a while:
python3 scripts/run_with_visibility.py scripts/long_script.py 300

# For complex monitoring:
python3 scripts/robust_script_runner.py scripts/complex_script.py
```

## ⚡ **Quick Decision Tree**

| What are you running? | Use this command |
|----------------------|------------------|
| **Python script** | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell command** | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Long process** | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Complex script** | `python3 scripts/robust_script_runner.py <script>` |
| **Simple echo/test** | `run_terminal_cmd("echo 'test'")` |

## 🎯 **Common Examples**

### **Verification Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

### **Setup Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py
```

### **Test Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/test_auth_flow.py
```

### **Deployment Scripts**
```bash
python3 scripts/run_with_visibility.py scripts/deploy.py 600
```

## ⚠️ **NEVER Use `run_terminal_cmd` For:**
- ❌ Python scripts (will hang)
- ❌ Interactive commands
- ❌ Long-running processes
- ❌ Scripts with complex output

## ✅ **ALWAYS Use Our Tools For:**
- ✅ Python script execution
- ✅ Complex shell commands
- ✅ Long-running processes
- ✅ Scripts requiring monitoring

---

**Remember: Our robust script runner prevents the terminal hanging issue completely!**
