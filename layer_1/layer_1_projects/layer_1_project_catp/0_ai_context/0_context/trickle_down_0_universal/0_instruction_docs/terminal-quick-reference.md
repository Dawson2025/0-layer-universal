---
resource_id: "eef97fb3-45c0-4ee3-93ef-6617225d3caf"
resource_type: "document"
resource_name: "terminal-quick-reference"
---
# Terminal Tool Quick Reference
*Immediate Reference for AI Agents*

<!-- section_id: "ad45ad06-9478-41dd-9de0-c72f63adfd79" -->
## 🚨 **CRITICAL: Use These Commands Instead of `run_terminal_cmd`**

<!-- section_id: "4f889776-b64b-487c-99af-7c297e6e9774" -->
### **Python Scripts**
```bash
# Instead of: run_terminal_cmd("python3 scripts/script.py")
python3 scripts/terminal_wrapper.py --script scripts/script.py

# With arguments:
python3 scripts/terminal_wrapper.py --script scripts/script.py arg1 arg2

# With custom timeout:
python3 scripts/terminal_wrapper.py --script scripts/script.py --timeout 60
```

<!-- section_id: "e7e88355-bc96-4f8f-b010-f487f11b754c" -->
### **Shell Commands**
```bash
# Instead of: run_terminal_cmd("echo 'test'")
python3 scripts/terminal_wrapper.py "echo 'test'"

# Complex commands:
python3 scripts/terminal_wrapper.py "curl -s https://api.example.com | jq '.'"
```

<!-- section_id: "9b836000-98d3-4c1a-9e64-0ceb5c35f8e9" -->
### **Long-running Scripts**
```bash
# For scripts that might take a while:
python3 scripts/run_with_visibility.py scripts/long_script.py 300

# For complex monitoring:
python3 scripts/robust_script_runner.py scripts/complex_script.py
```

<!-- section_id: "f69c3c86-efc5-4114-9629-4b48af45463f" -->
## ⚡ **Quick Decision Tree**

| What are you running? | Use this command |
|----------------------|------------------|
| **Python script** | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell command** | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Long process** | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Complex script** | `python3 scripts/robust_script_runner.py <script>` |
| **Simple echo/test** | `run_terminal_cmd("echo 'test'")` |

<!-- section_id: "3152d3a7-876e-4506-9418-76898db36c94" -->
## 🎯 **Common Examples**

<!-- section_id: "3881ccb6-d860-4a11-ae81-efb1da66f1a4" -->
### **Verification Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

<!-- section_id: "707d2107-67df-473f-b719-46500d084185" -->
### **Setup Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py
```

<!-- section_id: "3bdf3273-e5e0-48ea-bad3-7390933e574f" -->
### **Test Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/test_auth_flow.py
```

<!-- section_id: "85c5de9c-0a5e-4d33-9adf-3825d4d1c63d" -->
### **Deployment Scripts**
```bash
python3 scripts/run_with_visibility.py scripts/deploy.py 600
```

<!-- section_id: "db767907-9a7d-49ea-bd41-21162f35dbc9" -->
## ⚠️ **NEVER Use `run_terminal_cmd` For:**
- ❌ Python scripts (will hang)
- ❌ Interactive commands
- ❌ Long-running processes
- ❌ Scripts with complex output

<!-- section_id: "f762a0a0-4e86-4021-b97a-4649df947c66" -->
## ✅ **ALWAYS Use Our Tools For:**
- ✅ Python script execution
- ✅ Complex shell commands
- ✅ Long-running processes
- ✅ Scripts requiring monitoring

---

**Remember: Our robust script runner prevents the terminal hanging issue completely!**
