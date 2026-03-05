---
resource_id: "151a0189-cd3f-494e-9a6a-13126ec972fd"
resource_type: "rule"
resource_name: "CURSOR_AGENT_GUIDE"
---
# Cursor Agent Guide
*All Cursor-Specific Solutions and Workarounds*

<!-- section_id: "66bc52c7-154c-4b71-8594-e5ef46252147" -->
## Purpose

This document provides **all Cursor-specific solutions** for issues that don't apply to other AI agents. For universal rules that apply to all agents, see `MASTER_DOCUMENTATION.md`.

<!-- section_id: "b5b9a47f-c638-4add-835d-f080672391af" -->
## Location

**Universal Location**: `0_context/trickle_down_0_universal/0_instruction_docs/CURSOR_AGENT_GUIDE.md`

**Referenced by**: `MASTER_DOCUMENTATION.md`

---

<!-- section_id: "a05727dd-db1a-409b-b4bd-91cf68e6d1c6" -->
## Master Documentation Reference

**MANDATORY**: See `MASTER_DOCUMENTATION.md` for:
- Universal rules that apply to all agents
- Documentation standards
- Testing protocols
- General terminal execution best practices

**This guide** contains only Cursor-specific solutions.

---

<!-- section_id: "9daacfac-74aa-4a12-9440-7f84e52c055e" -->
## Cursor-Specific Solutions

<!-- section_id: "f7c5c9ce-fefd-4925-a169-c565cd9f32f7" -->
### 1. Terminal Execution Issues

**See**: `CURSOR_TERMINAL_EXECUTION.md` for complete Cursor terminal solutions.

**Quick Summary**:
- **Terminal Hanging**: Cursor has a known bug where `run_terminal_cmd` hangs on Python scripts
- **Solution**: Use `python3 scripts/terminal_wrapper.py --script <script>` for Python scripts
- **Workaround**: Always add `; exit` to commands to prevent hanging on failure
- **Node.js/System Commands**: Can use `run_terminal_cmd` directly (with `; exit`)

**Key Rules**:
- Python scripts → Always use terminal wrapper
- Node.js commands → Use `run_terminal_cmd("npx <command> ; exit")` directly
- System commands → Use `run_terminal_cmd("<command> ; exit")` directly
- Always add `; exit` to prevent hanging on both success and failure

<!-- section_id: "3d067672-433c-4535-bd32-471b41275f8a" -->
### 2. Other Cursor-Specific Issues

(Add other Cursor-specific solutions here as they are discovered)

---

<!-- section_id: "ee8b07f0-8265-4169-9cb0-9050a062dba0" -->
## Quick Reference

<!-- section_id: "d05bc217-8c76-4063-9100-2211d3773377" -->
### Terminal Execution
- **Python scripts**: `python3 scripts/terminal_wrapper.py --script <script>`
- **Node.js commands**: `run_terminal_cmd("npx <command> ; exit")`
- **System commands**: `run_terminal_cmd("<command> ; exit")`
- **Always add `; exit`** to prevent hanging

---

<!-- section_id: "076436f1-f7e2-4d93-8c9d-00349af87ed3" -->
## Related Documentation

- **Master Documentation**: `MASTER_DOCUMENTATION.md` - Universal rules for all agents
- **Cursor Terminal Execution**: `CURSOR_TERMINAL_EXECUTION.md` - Complete terminal solutions
- **Universal Terminal Execution**: `UNIVERSAL_TERMINAL_EXECUTION.md` - Universal best practices
- **Cursor Terminal Issues**: `cursor_terminal_issues.md` - Detailed Cursor issues

---

<!-- section_id: "f94c15f0-a321-4620-bdcf-524976f65e4c" -->
## For Cursor User Rules

If you're adding this to Cursor Settings → Rules for AI, reference:
- `MASTER_DOCUMENTATION.md` for universal rules
- `CURSOR_AGENT_GUIDE.md` for Cursor-specific solutions

---

**Status**: Cursor-Specific (does not apply to other agents)  
**Last Updated**: November 15, 2025  
**Version**: 1.0  
**Purpose**: All Cursor-specific solutions and workarounds

