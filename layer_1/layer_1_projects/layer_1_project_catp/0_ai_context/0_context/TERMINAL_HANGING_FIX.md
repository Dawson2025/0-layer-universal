---
resource_id: "d44b8490-b37f-4e7a-8c60-485d5c2a7625"
resource_type: "document"
resource_name: "TERMINAL_HANGING_FIX"
---
# Terminal Hanging Fix - Universal AI Agent Solution
*Critical Fix for Cursor Agent Terminal Hanging Issues*

<!-- section_id: "e3c8e68b-8e5a-406e-b437-0ac0e5ebd072" -->
## 🚨 **PROBLEM SOLVED**

**Issue**: The `run_terminal_cmd` tool in Cursor has a known bug where it hangs indefinitely after executing Python scripts, even though the scripts complete successfully.

**Solution**: Use our robust script runner system instead of `run_terminal_cmd` for Python scripts.

<!-- section_id: "a258d719-a0db-4485-abfc-37f9430a4d01" -->
## 🔧 **IMMEDIATE SOLUTION**

<!-- section_id: "7d812ecf-61e1-4128-a124-b6127eb0ca27" -->
### **❌ NEVER USE:**
```python
run_terminal_cmd("python3 scripts/script_name.py")
```

<!-- section_id: "292da10a-f5b1-4032-a306-f9b73a5940e7" -->
### **✅ ALWAYS USE:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/script_name.py
```

<!-- section_id: "4f5d08a8-b95a-457b-b174-59ed08d98c31" -->
## 📋 **QUICK REFERENCE**

| What to run? | Use this command |
|--------------|------------------|
| **Python script** | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell command** | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Long process** | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Complex script** | `python3 scripts/robust_script_runner.py <script>` |

<!-- section_id: "77835b08-2be4-4f8e-a7c0-662c098e3ba3" -->
## 🎯 **COMMON EXAMPLES**

<!-- section_id: "af2cd711-5b67-45ec-8aa9-7729f9975456" -->
### **Verification Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

<!-- section_id: "0d05e663-5db8-4ead-8616-1ed6d34d11d8" -->
### **Setup Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py
```

<!-- section_id: "bac7f8bb-2959-4a32-9ca1-5c1e9ccab27b" -->
### **Test Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/test_auth_flow.py
```

<!-- section_id: "585477af-11b6-4c6b-9f5c-23124bb9c939" -->
## 📚 **COMPLETE DOCUMENTATION**

For detailed information, see:
- **Full Protocol**: `docs/0_context/0_universal_instructions/terminal-tool-replacement.md`
- **Quick Reference**: `docs/0_context/0_universal_instructions/terminal-quick-reference.md`
- **Implementation Details**: `scripts/TERMINAL_HANGING_SOLUTION.md`

<!-- section_id: "d7871715-0d8e-44a2-9690-932f3ceb2538" -->
## ✅ **BENEFITS**

- ✅ **No More Hanging**: Scripts complete properly
- ✅ **Real-time Output**: See output as it's generated
- ✅ **Timeout Protection**: Long-running scripts are terminated automatically
- ✅ **Error Handling**: Proper capture and reporting of errors
- ✅ **Process Monitoring**: Built-in monitoring and cleanup

---

**⚠️ CRITICAL: Always use our robust script runner system instead of `run_terminal_cmd` for Python scripts!**
