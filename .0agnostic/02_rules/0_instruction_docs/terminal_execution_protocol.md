---
resource_id: "24acb567-dbe9-4783-a89a-0c7602c9245c"
resource_type: "rule"
resource_name: "terminal_execution_protocol"
---
# Terminal Execution Protocol - CRITICAL

**See also**: [Cursor Terminal Issues - AI Agent Guidelines](cursor_terminal_issues.md) for comprehensive documentation of Cursor terminal problems and solutions.

<!-- section_id: "df52668e-c819-4d21-a38e-916d075e8fdd" -->
## 🚨 **MANDATORY: Always Use (.venv) Prefix for Python Commands**

<!-- section_id: "4edb71e2-7714-4a56-ac72-0033102c236b" -->
### **Why This Matters:**
- Prevents terminal hanging issues with Python scripts
- Ensures virtual environment is properly activated
- Maintains consistent behavior across all AI interactions

<!-- section_id: "a26c547b-3423-4197-b45d-a07e9bebc2d4" -->
### **✅ CORRECT Usage:**
```bash
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 app.py
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 scripts/test.py
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 -m pytest
```

<!-- section_id: "ad56323b-5f3e-4a28-9e59-e8314180abd2" -->
### **❌ INCORRECT Usage:**
```bash
dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 app.py  # Will hang!
dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 scripts/test.py  # Will hang!
```

<!-- section_id: "53d96940-5ef0-4cc8-9788-fdb23d8fc6e9" -->
### **🔧 Implementation:**
- **Always check** if the terminal prompt shows `(.venv)` before running Python commands
- **If not present**, run `source .venv/bin/activate` first
- **Then proceed** with Python commands
- **This applies to ALL AI agents** and sessions

<!-- section_id: "6a4dbc5b-2c20-4276-8fb8-5bf7d52329b1" -->
### **📋 Quick Reference:**
1. Check prompt: `(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$`
2. If missing: `source .venv/bin/activate`
3. Run Python: `python3 script.py`
4. ✅ Success - no hanging!

<!-- section_id: "ba7ee053-cea7-474c-b65c-f62c7daaebdd" -->
### **🎯 Benefits:**
- ✅ No terminal hanging
- ✅ Consistent Python environment
- ✅ Proper dependency resolution
- ✅ Reliable script execution

**This protocol must be followed by ALL AI agents working on this project.**
