---
resource_id: "00f0e3ee-2b85-44a7-9553-ee44c79cce00"
resource_type: "readme
rule"
resource_name: "README"
---
# Universal AI Agent Instructions
*Level 0: Instructions for ANY Project*

**Scope**: Universal (applies to all projects, not just Lang-Trak)
**Version**: 1.0
**Last Updated**: January 24, 2025

---

## 🎯 **Purpose**

This directory contains **universal instructions** for AI agents that apply to ANY software project, regardless of technology stack, domain, or size.

**📌 START HERE**: See `MASTER_DOCUMENTATION.md` for the comprehensive overview of all universal systems and agent-specific guides.

---

## 📚 **Core Universal Systems**

### **1. Universal Documentation System** 📘

**File**: `UNIVERSAL_DOCUMENTATION_SYSTEM.md`

**What it is**: Meta-documentation explaining how to organize documentation for any project

**Use it to**:
- Understand the trickle-down hierarchy
- Learn universal → project implementation pattern
- Create new universal systems
- Properly integrate systems across levels

**Key Concept**: Universal protocols + Project implementations = Complete systems

---

### **2. Testing Agent System** 🧪

**Universal Components**:
- `TESTING_AGENT_SYSTEM_README.md` - Complete overview
- `testing-agent-protocol.md` - Core testing protocol
- `testing-agent-instructions.md` - How to create tests (universal)
- `testing-agent-handoff-template.md` - Standard handoff format
- `testing-agent-report-template.md` - Standard report format

**What it is**: Separation of concerns between development and testing

**Use it to**:
- Understand Testing Agent role
- Learn handoff workflow
- Follow testing standards
- Create comprehensive tests

**Project Implementation**: See `trickle_down_1_project/0_instruction_docs/TESTING_AGENT_INTEGRATION.md`

---

### **3. Terminal Execution System** 💻

**Master Reference**: See `MASTER_DOCUMENTATION.md` for complete overview

**Universal Components**:
- `UNIVERSAL_TERMINAL_EXECUTION.md` - **Universal best practices** for all agents
- `CURSOR_TERMINAL_EXECUTION.md` - **Cursor-specific** terminal hanging solution
- `CURSOR_AGENT_GUIDE.md` - All Cursor-specific solutions
- `terminal-tool-replacement.md` - Complete terminal execution guide
- `when-to-use-terminal-wrapper.md` - Decision guide (when to use wrapper vs run_terminal_cmd)
- `why-&&-exit-works.md` - Technical explanation of `; exit` workaround
- `playwright-installation-confusion-analysis.md` - Root cause analysis
- `cursor_terminal_issues.md` - Cursor-specific terminal issues
- `terminal_execution_protocol.md` - Legacy protocol
- `terminal-quick-reference.md` - Quick reference guide
- `MASTER_TERMINAL_EXECUTION_REFERENCE.md` - Legacy (superseded by MASTER_DOCUMENTATION.md)

**What it is**: Best practices for terminal command execution in AI agents

**Use it to**:
- Follow universal terminal execution best practices
- Understand Cursor-specific terminal hanging issues (if using Cursor)
- Use proper tools for different command types (Node.js vs system commands)
- Execute commands safely with `; exit` workaround

**Key Rules**:
- **Universal**: Node.js commands → Use agent's terminal tool directly (with `; exit`)
- **Universal**: System commands → Use agent's terminal tool directly (with `; exit`)
- **Universal**: Always add `; exit` to prevent hanging on both success and failure
- **Cursor-Specific**: Python scripts → Use terminal wrapper (see CURSOR_TERMINAL_EXECUTION.md)

---

### **4. Manual Steps Automation** 🤖

**Universal Components**:
- `manual-steps-automation.md` - Protocol for automating manual steps

**What it is**: How AI agents should handle "manual steps" instructions

**Use it to**:
- Never ask users to do manual steps
- Automate browser interactions
- Use MCP tools for web interfaces
- Execute all steps programmatically

---

### **5. OAuth Production Setup** 🔐

**Universal Components**:
- `google_oauth_production_ready.md` - Production OAuth configuration

**What it is**: Universal OAuth setup procedures

**Use it to**:
- Configure OAuth for production
- Handle OAuth credentials securely
- Set up OAuth consent screens
- Manage OAuth redirects

---

### **6. Security Protocols** 🔒

**Universal Components**:
- `sudo_password_management.md` - Password management protocol

**What it is**: Security best practices for AI agents

**Use it to**:
- Handle sensitive credentials
- Manage sudo access
- Secure password storage
- Follow security protocols

---

### **7. Documentation Completion Protocol** 📝

**Universal Components**:
- `post-completion-documentation-protocol.md` - Documentation standards

**What it is**: How to document completed work

**Use it to**:
- Create completion reports
- Document decisions made
- Archive completed work
- Maintain documentation quality

---

## 🔄 **Universal → Project Pattern**

Every universal system follows this pattern:

### **Step 1: Universal (Level 0)**
Define the universal protocol that works for ANY project:
```
trickle_down_0_universal/0_instruction_docs/
└── [SYSTEM_NAME].md  ← Universal protocol
```

### **Step 2: Project Implementation (Level 1)**
Create project-specific implementation:
```
trickle_down_1_project/0_instruction_docs/
└── [SYSTEM_NAME]_INTEGRATION.md  ← How to use for THIS project
```

### **Step 3: Integration**
The integration guide explains:
- How to apply universal protocol to this project
- Project-specific requirements
- Where operational documents go
- Day-to-day usage

---

## 📊 **Directory Structure**

```
trickle_down_0_universal/
├── 0_instruction_docs/              ← You are here
│   ├── README.md                        ← This file
│   ├── UNIVERSAL_DOCUMENTATION_SYSTEM.md  ← Meta-documentation
│   │
│   ├── Testing Agent System/
│   │   ├── TESTING_AGENT_SYSTEM_README.md
│   │   ├── testing-agent-protocol.md
│   │   ├── testing-agent-instructions.md
│   │   ├── testing-agent-handoff-template.md
│   │   └── testing-agent-report-template.md
│   │
│   ├── Terminal Execution System/
│   │   ├── cursor_terminal_issues.md
│   │   ├── terminal_execution_protocol.md
│   │   ├── terminal-tool-replacement.md
│   │   └── terminal-quick-reference.md
│   │
│   └── Other Universal Systems/
│       ├── manual-steps-automation.md
│       ├── google_oauth_production_ready.md
│       ├── sudo_password_management.md
│       └── post-completion-documentation-protocol.md
│
├── 1_status_progress_docs/          ← Universal status (rare)
└── 3_archive_docs/                  ← Completed universal work
```

---

## 🎯 **For AI Agents**

### **When Starting Work**

1. **Read**: `../../../0_basic_prompts_throughout/what_to_do_next.md`
2. **Understand**: `UNIVERSAL_DOCUMENTATION_SYSTEM.md`
3. **Follow**: Relevant universal protocols from this directory
4. **Apply**: Project-specific integrations from Level 1

### **Which System to Use?**

| Task | Universal System | Project Integration |
|------|------------------|---------------------|
| Writing tests | `testing-agent-protocol.md` | `TESTING_AGENT_INTEGRATION.md` |
| Running commands | `terminal_execution_protocol.md` | (none needed) |
| Automating manual steps | `manual-steps-automation.md` | (none needed) |
| Setting up OAuth | `google_oauth_production_ready.md` | Project OAuth config |
| Managing passwords | `sudo_password_management.md` | (none needed) |
| Documenting work | `post-completion-documentation-protocol.md` | Project standards |

### **Creating New Systems**

If you need a new system:
1. Check if it's universal (applies to any project)
2. If yes, create universal protocol here
3. Create project integration in Level 1
4. Update MASTER_DOCUMENTATION_INDEX.md
5. Follow pattern in `UNIVERSAL_DOCUMENTATION_SYSTEM.md`

---

## 📝 **Quick Reference**

### **Finding Documentation**

```bash
# Universal systems (any project)
ls docs/0_context/trickle_down_0_universal/0_instruction_docs/

# Project implementations (Lang-Trak)
ls docs/0_context/trickle_down_1_project/0_instruction_docs/

# Integration guides
ls docs/0_context/trickle_down_1_project/0_instruction_docs/*INTEGRATION.md
```

### **Key Principles**

1. ✅ **Universal protocols** go in Level 0
2. ✅ **Project implementations** go in Level 1
3. ✅ **Integration guides** connect the two
4. ✅ **Pattern is consistent** across all systems
5. ✅ **Reusability** is a core goal

---

## 🔗 **Related Documentation**

### **Meta-Level**
- Core Instructions: `../../0_basic_prompts_throughout/what_to_do_next.md`
- Documentation System: `UNIVERSAL_DOCUMENTATION_SYSTEM.md`
- Master Index: `../../MASTER_DOCUMENTATION_INDEX.md`

### **Project-Level**
- Project Instructions: `../../trickle_down_1_project/0_instruction_docs/project_instructions.md`
- Project Constitution: `../../trickle_down_1_project/0_instruction_docs/constitution.md`
- Testing Integration: `../../trickle_down_1_project/0_instruction_docs/TESTING_AGENT_INTEGRATION.md`

### **Tools**
- Universal Tools: `../../trickle_down_0.75_universal_tools/0_instruction_docs/README.md`
- Project Tools: `../../trickle_down_1.5_project_tools/0_instruction_docs/README.md`

---

## ✅ **Summary**

This directory contains **universal protocols** that:
- Apply to ANY project
- Provide consistent patterns
- Are specialized by project implementations
- Enable reusability and maintainability

**Key Concept**: Universal → Project → Complete System

---

**Directory**: Level 0 Universal Instructions
**Scope**: Universal (all projects)
**Status**: Active
**Version**: 1.0
**Last Updated**: January 24, 2025
