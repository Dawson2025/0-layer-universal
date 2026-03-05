---
resource_id: "d44b8490-b37f-4e7a-8c60-485d5c2a7625"
resource_type: "document"
resource_name: "TERMINAL_HANGING_FIX"
---
# Terminal Hanging Fix - Universal AI Agent Solution
*Critical Fix for Cursor Agent Terminal Hanging Issues*

## 🚨 **PROBLEM SOLVED**

**Issue**: The `run_terminal_cmd` tool in Cursor has a known bug where it hangs indefinitely after executing Python scripts, even though the scripts complete successfully.

**Solution**: Use our robust script runner system instead of `run_terminal_cmd` for Python scripts.

## 🔧 **IMMEDIATE SOLUTION**

### **❌ NEVER USE:**
```python
run_terminal_cmd("python3 scripts/script_name.py")
```

### **✅ ALWAYS USE:**
```bash
python3 scripts/terminal_wrapper.py --script scripts/script_name.py
```

## 📋 **QUICK REFERENCE**

| What to run? | Use this command |
|--------------|------------------|
| **Python script** | `python3 scripts/terminal_wrapper.py --script <script>` |
| **Shell command** | `python3 scripts/terminal_wrapper.py "<command>"` |
| **Long process** | `python3 scripts/run_with_visibility.py <script> <timeout>` |
| **Complex script** | `python3 scripts/robust_script_runner.py <script>` |

## 🎯 **COMMON EXAMPLES**

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

## 📚 **COMPLETE DOCUMENTATION**

For detailed information, see:
- **Full Protocol**: `docs/0_context/0_universal_instructions/terminal-tool-replacement.md`
- **Quick Reference**: `docs/0_context/0_universal_instructions/terminal-quick-reference.md`
- **Implementation Details**: `scripts/TERMINAL_HANGING_SOLUTION.md`

## ✅ **BENEFITS**

- ✅ **No More Hanging**: Scripts complete properly
- ✅ **Real-time Output**: See output as it's generated
- ✅ **Timeout Protection**: Long-running scripts are terminated automatically
- ✅ **Error Handling**: Proper capture and reporting of errors
- ✅ **Process Monitoring**: Built-in monitoring and cleanup

---

**⚠️ CRITICAL: Always use our robust script runner system instead of `run_terminal_cmd` for Python scripts!**
