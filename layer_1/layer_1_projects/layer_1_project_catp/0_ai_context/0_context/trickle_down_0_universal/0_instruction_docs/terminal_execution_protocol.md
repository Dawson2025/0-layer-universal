---
resource_id: "a624e9c7-f689-4864-bc9a-dcb32013126e"
resource_type: "document"
resource_name: "terminal_execution_protocol"
---
# Terminal Execution Protocol - CRITICAL

**See also**: [Cursor Terminal Issues - AI Agent Guidelines](cursor_terminal_issues.md) for comprehensive documentation of Cursor terminal problems and solutions.

<!-- section_id: "8ae7b5c0-8233-4976-820d-84f3cc84d0d5" -->
## 🚨 **MANDATORY: Always Use (.venv) Prefix for Python Commands**

<!-- section_id: "c01c61fd-c4ad-425d-99f9-6f1e40fc936d" -->
### **Why This Matters:**
- Prevents terminal hanging issues with Python scripts
- Ensures virtual environment is properly activated
- Maintains consistent behavior across all AI interactions

<!-- section_id: "730cdd05-ffa7-408e-914e-32167f588c81" -->
### **✅ CORRECT Usage:**
```bash
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 app.py
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 scripts/test.py
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 -m pytest
```

<!-- section_id: "bc00afb5-ab15-4f2a-9e2a-6712c7cf76ed" -->
### **❌ INCORRECT Usage:**
```bash
dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 app.py  # Will hang!
dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 scripts/test.py  # Will hang!
```

<!-- section_id: "85bda6ee-a485-4315-a11a-4c72bcc5a97d" -->
### **🔧 Implementation:**
- **Always check** if the terminal prompt shows `(.venv)` before running Python commands
- **If not present**, run `source .venv/bin/activate` first
- **Then proceed** with Python commands
- **This applies to ALL AI agents** and sessions

<!-- section_id: "c1cc2b13-982c-4c0d-baa2-82c0b39e5adb" -->
### **📋 Quick Reference:**
1. Check prompt: `(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$`
2. If missing: `source .venv/bin/activate`
3. Run Python: `python3 script.py`
4. ✅ Success - no hanging!

<!-- section_id: "f523d8e1-37a2-43b5-ba2a-5e9b851d7f44" -->
### **🎯 Benefits:**
- ✅ No terminal hanging
- ✅ Consistent Python environment
- ✅ Proper dependency resolution
- ✅ Reliable script execution

**This protocol must be followed by ALL AI agents working on this project.**
