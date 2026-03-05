---
resource_id: "db506af1-a554-4717-adda-e3c3b317539b"
resource_type: "document"
resource_name: "terminal_execution_protocol"
---
# Terminal Execution Protocol - CRITICAL

**See also**: [Cursor Terminal Issues - AI Agent Guidelines](cursor_terminal_issues.md) for comprehensive documentation of Cursor terminal problems and solutions.

<!-- section_id: "6ab3291b-c2b7-42b4-b2bb-1a6fd2372308" -->
## 🚨 **MANDATORY: Always Use (.venv) Prefix for Python Commands**

<!-- section_id: "9c58d00a-fa81-4f94-b416-ba471374cf2a" -->
### **Why This Matters:**
- Prevents terminal hanging issues with Python scripts
- Ensures virtual environment is properly activated
- Maintains consistent behavior across all AI interactions

<!-- section_id: "bfe02919-3560-4402-9de0-1c52fbc17765" -->
### **✅ CORRECT Usage:**
```bash
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 app.py
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 scripts/test.py
(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 -m pytest
```

<!-- section_id: "2f13d607-9b98-4f1e-af7a-1f0ecc2b1a81" -->
### **❌ INCORRECT Usage:**
```bash
dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 app.py  # Will hang!
dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$ python3 scripts/test.py  # Will hang!
```

<!-- section_id: "7ab5366b-a079-4157-b485-e4c29c6ac2ad" -->
### **🔧 Implementation:**
- **Always check** if the terminal prompt shows `(.venv)` before running Python commands
- **If not present**, run `source .venv/bin/activate` first
- **Then proceed** with Python commands
- **This applies to ALL AI agents** and sessions

<!-- section_id: "bc4963c4-f048-41d9-a587-37ce563bc299" -->
### **📋 Quick Reference:**
1. Check prompt: `(.venv) dawson@LAPTOP-GF3B5QV4:~/code/lang-trak-in-progress$`
2. If missing: `source .venv/bin/activate`
3. Run Python: `python3 script.py`
4. ✅ Success - no hanging!

<!-- section_id: "ee8b5cca-ee32-493b-8ac5-b24896b94ea9" -->
### **🎯 Benefits:**
- ✅ No terminal hanging
- ✅ Consistent Python environment
- ✅ Proper dependency resolution
- ✅ Reliable script execution

**This protocol must be followed by ALL AI agents working on this project.**
