---
resource_id: "eb9531ad-3f7a-4edb-8419-530eea3840d3"
resource_type: "document"
resource_name: "terminal-quick-reference"
---
# Terminal Tool Quick Reference
*Immediate Reference for AI Agents*

<!-- section_id: "643a48be-0d08-462d-87cd-dd737ae5c5c7" -->
## 🚨 **CRITICAL: Use These Commands Instead of `run_terminal_cmd`**

<!-- section_id: "0ffcccbc-7368-4176-8aaf-c32e3a48443a" -->
### **Python Scripts**
```bash
# Instead of: run_terminal_cmd("python3 scripts/script.py")
python3 scripts/terminal_wrapper.py --script scripts/script.py

# With arguments:
python3 scripts/terminal_wrapper.py --script scripts/script.py arg1 arg2

# With custom timeout:
python3 scripts/terminal_wrapper.py --script scripts/script.py --timeout 60
```

<!-- section_id: "eeb11acd-d243-4fda-bf3e-376eec103ac2" -->
### **Shell Commands**
```bash
# Instead of: run_terminal_cmd("echo 'test'")
python3 scripts/terminal_wrapper.py "echo 'test'"

# Complex commands:
python3 scripts/terminal_wrapper.py "curl -s https://api.example.com | jq '.'"
```

<!-- section_id: "5e10e85a-b9c5-4296-a899-b8ca65c329ba" -->
### **Long-running Scripts**
```bash
# For scripts that might take a while:
python3 scripts/run_with_visibility.py scripts/long_script.py 300

# For complex monitoring:
python3 scripts/robust_script_runner.py scripts/complex_script.py
```

<!-- section_id: "cbfe0003-52e9-4e03-a8e0-89736e30776f" -->
## ⚡ **Quick Decision Tree**

| What are you running? | Use this command |
|----------------------|------------------|
| **Python script** | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell command** | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Long process** | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Complex script** | `python3 scripts/robust_script_runner.py <script>` |
| **Simple echo/test** | `run_terminal_cmd("echo 'test'")` |

<!-- section_id: "bfdc41da-6867-49b0-8f07-5c13e6679e1c" -->
## 🎯 **Common Examples**

<!-- section_id: "618a23c3-8838-4314-9b06-17b274ae8abf" -->
### **Verification Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

<!-- section_id: "97fac706-224e-4741-8876-511a051a7773" -->
### **Setup Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py
```

<!-- section_id: "e7620400-33ec-4c33-b2d0-d7429acb0189" -->
### **Test Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/test_auth_flow.py
```

<!-- section_id: "1a1701da-35e4-472f-bd80-086519e8c309" -->
### **Deployment Scripts**
```bash
python3 scripts/run_with_visibility.py scripts/deploy.py 600
```

<!-- section_id: "21281b46-704b-49d3-b0e9-955f62304ce2" -->
## ⚠️ **NEVER Use `run_terminal_cmd` For:**
- ❌ Python scripts (will hang)
- ❌ Interactive commands
- ❌ Long-running processes
- ❌ Scripts with complex output

<!-- section_id: "09386c37-ca0d-45eb-b185-0ec4b4b27b0c" -->
## ✅ **ALWAYS Use Our Tools For:**
- ✅ Python script execution
- ✅ Complex shell commands
- ✅ Long-running processes
- ✅ Scripts requiring monitoring

---

**Remember: Our robust script runner prevents the terminal hanging issue completely!**
