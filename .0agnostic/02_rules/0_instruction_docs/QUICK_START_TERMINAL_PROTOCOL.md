---
resource_id: "a6cbd651-10d3-45b1-a999-f51fd06d4da0"
resource_type: "rule"
resource_name: "QUICK_START_TERMINAL_PROTOCOL"
---
# Quick Start: Terminal Execution Protocol
*For ALL AI Agents - Read This First*

## 🚀 30-Second Summary

**Before running ANY terminal command, remember:**

1. **Python scripts** → Use wrapper: `python3 scripts/terminal_wrapper.py --script <script>`
2. **Node.js commands** → Use directly: `run_terminal_cmd("npx <command> ; exit")`
3. **System commands** → Use directly: `run_terminal_cmd("<command> ; exit")`
4. **Always add `; exit`** → Prevents hanging on both success and failure

## 📋 Decision Tree

```
Command Type?
├─ Python script → python3 scripts/terminal_wrapper.py --script <script>
├─ Node.js (npx/npm) → run_terminal_cmd("npx <command> ; exit")
├─ System (apt/wget/ls) → run_terminal_cmd("<command> ; exit")
└─ Complex → python3 scripts/terminal_wrapper.py "<command> ; exit"
```

## 📚 Full Documentation

**Complete Guide**: `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`  
**Discovery Guide**: `AGENT_DISCOVERY_GUIDE.md`  
**Detailed Guide**: `terminal-tool-replacement.md`

---

**This is a quick reference. For complete rules and explanations, see `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`**

