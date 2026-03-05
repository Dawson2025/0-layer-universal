---
resource_id: "f2dda20e-8da8-476c-b9c1-851487a7dd6f"
resource_type: "rule"
resource_name: "terminal-quick-reference"
---
# Terminal Tool Quick Reference
*Immediate Reference for AI Agents*

<!-- section_id: "0eeb70ad-f87f-4517-a6e8-ba474b5b30f2" -->
## 🚨 **CRITICAL: Use These Commands Instead of `run_terminal_cmd`**

<!-- section_id: "a45e27be-51e5-48eb-85f3-17d807cc1f89" -->
### **Python Scripts**
```bash
# Instead of: run_terminal_cmd("python3 scripts/script.py")
python3 scripts/terminal_wrapper.py --script scripts/script.py

# With arguments:
python3 scripts/terminal_wrapper.py --script scripts/script.py arg1 arg2

# With custom timeout:
python3 scripts/terminal_wrapper.py --script scripts/script.py --timeout 60
```

<!-- section_id: "ad26c334-86f0-45eb-b181-8b374503d347" -->
### **Shell Commands**
```bash
# Instead of: run_terminal_cmd("echo 'test'")
python3 scripts/terminal_wrapper.py "echo 'test'"

# Complex commands:
python3 scripts/terminal_wrapper.py "curl -s https://api.example.com | jq '.'"
```

<!-- section_id: "a335763b-5328-407f-bd7e-07398028e9d9" -->
### **Long-running Scripts**
```bash
# For scripts that might take a while:
python3 scripts/run_with_visibility.py scripts/long_script.py 300

# For complex monitoring:
python3 scripts/robust_script_runner.py scripts/complex_script.py
```

<!-- section_id: "146ac6f0-b721-43ea-b054-101f3f7d2964" -->
## ⚡ **Quick Decision Tree**

| What are you running? | Use this command |
|----------------------|------------------|
| **Python script** | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell command** | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Long process** | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Complex script** | `python3 scripts/robust_script_runner.py <script>` |
| **Simple echo/test** | `run_terminal_cmd("echo 'test'")` |

<!-- section_id: "53bc761b-3a33-4ab6-bf61-01df0f20b965" -->
## 🎯 **Common Examples**

<!-- section_id: "6ac9786d-93b3-4ff1-8730-4074b97be132" -->
### **Verification Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

<!-- section_id: "e920814c-1088-4a32-b203-ba81a57edcc0" -->
### **Setup Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py
```

<!-- section_id: "ddad4443-549f-47a8-8431-6f9cae4c5ddc" -->
### **Test Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/test_auth_flow.py
```

<!-- section_id: "fa33ce91-d75b-445b-a1e9-56366dd080e0" -->
### **Deployment Scripts**
```bash
python3 scripts/run_with_visibility.py scripts/deploy.py 600
```

<!-- section_id: "d94fb951-0359-4fb5-bc7f-f3ce8d65ef3f" -->
## ⚠️ **NEVER Use `run_terminal_cmd` For:**
- ❌ Python scripts (will hang)
- ❌ Interactive commands
- ❌ Long-running processes
- ❌ Scripts with complex output

<!-- section_id: "d651d2f1-dc81-4019-ae26-29ad9120861a" -->
## ✅ **ALWAYS Use Our Tools For:**
- ✅ Python script execution
- ✅ Complex shell commands
- ✅ Long-running processes
- ✅ Scripts requiring monitoring

---

**Remember: Our robust script runner prevents the terminal hanging issue completely!**
