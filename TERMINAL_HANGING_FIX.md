---
resource_id: "5204d76a-8614-4d65-9a2c-7f3ff82c407d"
resource_type: "document"
resource_name: "TERMINAL_HANGING_FIX"
---
# Terminal Hanging Fix - Universal AI Agent Solution
*Critical Fix for Cursor Agent Terminal Hanging Issues*

<!-- section_id: "da458e5b-df4b-4504-bae5-958f24500f30" -->
## 🚨 **PROBLEM SOLVED**

**Issue**: The `run_terminal_cmd` tool in Cursor has a known bug where it hangs indefinitely after executing Python scripts, even though the scripts complete successfully.

**Solution**: Use our robust script runner system instead of `run_terminal_cmd` for Python scripts.

<!-- section_id: "e360564f-6d07-48f7-a35d-99d8bd5dd1d1" -->
## 🔧 **IMMEDIATE SOLUTION**

<!-- section_id: "d8122234-445d-400a-aa95-121b6cf35b9c" -->
### **❌ NEVER USE:**
```python
run_terminal_cmd("python3 scripts/script_name.py")
```

<!-- section_id: "c7306c26-3fbb-475c-aab8-3b5b7da1d95a" -->
### **✅ ALWAYS USE:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/script_name.py
```

<!-- section_id: "0047aa12-8fcb-4de2-be40-e1a45b6633eb" -->
## 📋 **QUICK REFERENCE**

| What to run? | Use this command |
|--------------|------------------|
| **Python script** | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell command** | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Long process** | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Complex script** | `python3 scripts/robust_script_runner.py <script>` |

<!-- section_id: "084eb89e-fc1f-45dd-acc7-eb2c65894271" -->
## 🎯 **COMMON EXAMPLES**

<!-- section_id: "60b9c247-06a1-4f97-91de-183fe4663bd5" -->
### **Verification Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

<!-- section_id: "0ce0a672-6b8b-4d10-b26a-ed7462280c50" -->
### **Setup Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py
```

<!-- section_id: "32af2063-943d-4551-bfcd-e95c6cd12621" -->
### **Test Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/test_auth_flow.py
```

<!-- section_id: "c4b740f8-49db-4935-917f-29e9b328308e" -->
## 📚 **COMPLETE DOCUMENTATION**

For detailed information, see:
- **Full Protocol**: `docs/0_context/0_universal_instructions/terminal-tool-replacement.md`
- **Quick Reference**: `docs/0_context/0_universal_instructions/terminal-quick-reference.md`
- **Implementation Details**: `scripts/TERMINAL_HANGING_SOLUTION.md`

<!-- section_id: "8ae0de5b-3eb2-453e-a4c0-d787a49f4173" -->
## ✅ **BENEFITS**

- ✅ **No More Hanging**: Scripts complete properly
- ✅ **Real-time Output**: See output as it's generated
- ✅ **Timeout Protection**: Long-running scripts are terminated automatically
- ✅ **Error Handling**: Proper capture and reporting of errors
- ✅ **Process Monitoring**: Built-in monitoring and cleanup

---

**⚠️ CRITICAL: Always use our robust script runner system instead of `run_terminal_cmd` for Python scripts!**
