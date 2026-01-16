# Cursor Agent Guide
*All Cursor-Specific Solutions and Workarounds*

## Purpose

This document provides **all Cursor-specific solutions** for issues that don't apply to other AI agents. For universal rules that apply to all agents, see `MASTER_DOCUMENTATION.md`.

## Location

**Universal Location**: `0_context/trickle_down_0_universal/0_instruction_docs/CURSOR_AGENT_GUIDE.md`

**Referenced by**: `MASTER_DOCUMENTATION.md`

---

## Master Documentation Reference

**MANDATORY**: See `MASTER_DOCUMENTATION.md` for:
- Universal rules that apply to all agents
- Documentation standards
- Testing protocols
- General terminal execution best practices

**This guide** contains only Cursor-specific solutions.

---

## Cursor-Specific Solutions

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

### 2. Other Cursor-Specific Issues

(Add other Cursor-specific solutions here as they are discovered)

---

## Quick Reference

### Terminal Execution
- **Python scripts**: `python3 scripts/terminal_wrapper.py --script <script>`
- **Node.js commands**: `run_terminal_cmd("npx <command> ; exit")`
- **System commands**: `run_terminal_cmd("<command> ; exit")`
- **Always add `; exit`** to prevent hanging

---

## Related Documentation

- **Master Documentation**: `MASTER_DOCUMENTATION.md` - Universal rules for all agents
- **Cursor Terminal Execution**: `CURSOR_TERMINAL_EXECUTION.md` - Complete terminal solutions
- **Universal Terminal Execution**: `UNIVERSAL_TERMINAL_EXECUTION.md` - Universal best practices
- **Cursor Terminal Issues**: `cursor_terminal_issues.md` - Detailed Cursor issues

---

## For Cursor User Rules

If you're adding this to Cursor Settings → Rules for AI, reference:
- `MASTER_DOCUMENTATION.md` for universal rules
- `CURSOR_AGENT_GUIDE.md` for Cursor-specific solutions

---

**Status**: Cursor-Specific (does not apply to other agents)  
**Last Updated**: November 15, 2025  
**Version**: 1.0  
**Purpose**: All Cursor-specific solutions and workarounds

