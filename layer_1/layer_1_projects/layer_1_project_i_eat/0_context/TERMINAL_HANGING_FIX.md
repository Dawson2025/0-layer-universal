---
resource_id: "d9177760-6372-4762-ad0b-7e3882fb3780"
resource_type: "document"
resource_name: "TERMINAL_HANGING_FIX"
---
# Terminal Hanging Fix - Universal AI Agent Solution
*Critical Fix for Cursor Agent Terminal Hanging Issues*

<!-- section_id: "5595697e-3754-4a18-a6d1-b4ae3c774e82" -->
## 🚨 **PROBLEM SOLVED**

**Issue**: The `run_terminal_cmd` tool in Cursor has a known bug where it hangs indefinitely after executing Python scripts, even though the scripts complete successfully.

**Solution**: Use our robust script runner system instead of `run_terminal_cmd` for Python scripts.

<!-- section_id: "a27c2a70-1796-4d91-b742-da50a81408d8" -->
## 🔧 **IMMEDIATE SOLUTION**

<!-- section_id: "376e15a8-78a2-4466-b8b6-27862926afb4" -->
### **❌ NEVER USE:**
```python
run_terminal_cmd("python3 scripts/script_name.py")
```

<!-- section_id: "d202b3d5-aedb-4064-9f3d-52f60b6726c5" -->
### **✅ ALWAYS USE:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/script_name.py
```

<!-- section_id: "c3fb53df-ff24-465c-a54a-c5e897a813e4" -->
## 📋 **QUICK REFERENCE**

| What to run? | Use this command |
|--------------|------------------|
| **Python script** | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell command** | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Long process** | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Complex script** | `python3 scripts/robust_script_runner.py <script>` |

<!-- section_id: "97d6f682-4bc3-4489-a6f6-15655ef14676" -->
## 🎯 **COMMON EXAMPLES**

<!-- section_id: "fb1afb68-a14f-4bbc-aa1e-cdf94964c61f" -->
### **Verification Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/quick_verify.py
```

<!-- section_id: "4cf8b93b-de6f-4e70-9839-85b3f07a5bfd" -->
### **Setup Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/setup_environment.py
```

<!-- section_id: "96c33afa-e4e0-40c1-abb2-a8903c0b6ad3" -->
### **Test Scripts**
```bash
python3 scripts/terminal_wrapper.py --script scripts/test_auth_flow.py
```

<!-- section_id: "1c2344f8-9698-432b-b33d-c6ffcd110065" -->
## 📚 **COMPLETE DOCUMENTATION**

For detailed information, see:
- **Full Protocol**: `docs/0_context/0_universal_instructions/terminal-tool-replacement.md`
- **Quick Reference**: `docs/0_context/0_universal_instructions/terminal-quick-reference.md`
- **Implementation Details**: `scripts/TERMINAL_HANGING_SOLUTION.md`

<!-- section_id: "a73c30ba-e900-46e6-b1aa-2a0ee0742d6f" -->
## ✅ **BENEFITS**

- ✅ **No More Hanging**: Scripts complete properly
- ✅ **Real-time Output**: See output as it's generated
- ✅ **Timeout Protection**: Long-running scripts are terminated automatically
- ✅ **Error Handling**: Proper capture and reporting of errors
- ✅ **Process Monitoring**: Built-in monitoring and cleanup

---

**⚠️ CRITICAL: Always use our robust script runner system instead of `run_terminal_cmd` for Python scripts!**
