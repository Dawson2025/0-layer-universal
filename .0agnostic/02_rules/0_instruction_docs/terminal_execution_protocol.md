---
resource_id: "24acb567-dbe9-4783-a89a-0c7602c9245c"
resource_type: "rule"
resource_name: "terminal_execution_protocol"
---
# Terminal Execution Protocol - CRITICAL

**See also**: [Cursor Terminal Issues - AI Agent Guidelines](cursor_terminal_issues.md) for comprehensive documentation of Cursor terminal problems and solutions.

## 🚨 **MANDATORY: Always Use (.venv) Prefix for Python Commands**

### **Why This Matters:**
- Prevents terminal hanging issues with Python scripts
- Ensures virtual environment is properly activated
- Maintains consistent behavior across all AI interactions

### **✅ CORRECT Usage:**
```bash
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 app.py
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 scripts/test.py
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 -m pytest
```

### **❌ INCORRECT Usage:**
```bash
dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 app.py  # Will hang!
dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 scripts/test.py  # Will hang!
```

### **🔧 Implementation:**
- **Always check** if the terminal prompt shows `(.venv)` before running Python commands
- **If not present**, run `source .venv/bin/activate` first
- **Then proceed** with Python commands
- **This applies to ALL AI agents** and sessions

### **📋 Quick Reference:**
1. Check prompt: `(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$`
2. If missing: `source .venv/bin/activate`
3. Run Python: `python3 script.py`
4. ✅ Success - no hanging!

### **🎯 Benefits:**
- ✅ No terminal hanging
- ✅ Consistent Python environment
- ✅ Proper dependency resolution
- ✅ Reliable script execution

**This protocol must be followed by ALL AI agents working on this project.**
