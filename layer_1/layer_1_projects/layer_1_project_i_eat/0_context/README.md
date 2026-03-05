---
resource_id: "46b6d922-21cf-4bff-be6b-33e0a77556e6"
resource_type: "readme
document"
resource_name: "README"
---
# 0_context - I-Eat University Food Delivery Platform
*Trickle-Down Documentation for AI Coding Agents*

<!-- section_id: "8f4b0689-d10c-493a-a3c3-22b96f824e1d" -->
## 🚨 **CRITICAL: Terminal Hanging Fix**

**IMPORTANT**: Before using any terminal commands, read the terminal hanging fix:
- **Quick Fix**: `TERMINAL_HANGING_FIX.md` - Immediate solution
- **Full Protocol**: `trickle_down_0_universal/0_instruction_docs/terminal-tool-replacement.md`
- **Quick Reference**: `trickle_down_0_universal/0_instruction_docs/terminal-quick-reference.md`

<!-- section_id: "4cc6b387-c726-448e-81fb-b8ee382d9b7d" -->
## 🚨 **CRITICAL: Manual Steps Execution**

**IMPORTANT**: AI agents must execute ALL manual steps directly using available tools:
- **Manual Steps Protocol**: `trickle_down_0_universal/0_instruction_docs/manual-steps-automation.md`
- **Browser Automation**: Use MCP tools for web interface interaction
- **No Delegation**: Never ask users to perform manual steps

<!-- section_id: "05665365-0cae-437b-a668-8b8a55cf6c9e" -->
## 🍕 **I-Eat Project Overview**

**I-Eat** is a university-focused food delivery platform that connects students with food delivery services on campus. The platform features:

- **Student Users**: Order food, earn points from teachers, track deliveries
- **Delivery Drivers**: Accept orders, navigate campus locations, complete deliveries
- **Points System**: Teachers award points to students for academic performance
- **Campus Integration**: Specialized for university dorms, classrooms, and campus locations

<!-- section_id: "acc646cd-3c11-4214-8b89-762e5e49644f" -->
### Technology Stack
- **Frontend**: React 19.1.1 + Vite 7.1.7
- **Backend**: Supabase (Authentication, Database, Real-time)
- **Mobile**: React Native (planned)
- **Deployment**: Vercel (web), App Store/Google Play (mobile)

<!-- section_id: "dfe091c2-14ef-4239-8576-02aa8a25ff09" -->
## 📁 **Directory Structure**

<!-- section_id: "5c080d66-ecb0-4c05-98e5-f9207d3d5537" -->
### **trickle_down_0_universal/**
Universal instructions for all AI agents
- `0_instruction_docs/` - How-to guides, protocols, and procedures
- `1_status_progress_docs/` - Current status and progress reports
- `2_archive_docs/` - Completed work and resolutions

<!-- section_id: "a9114a16-d644-4617-b146-15a7952367c8" -->
### **trickle_down_0.5_setup/**
Setup and configuration systems
- `0_instruction_docs/` - Setup guides and configuration procedures
- `1_status_progress_docs/` - Setup status and progress
- `2_archive_docs/` - Completed setup documentation

<!-- section_id: "96a5d7a8-8fdb-44a8-95f1-2d797b264f44" -->
### **trickle_down_0.75_universal_tools/**
Universal tools and utilities
- `0_instruction_docs/` - Tool usage guides and procedures
- `1_status_progress_docs/` - Tool development status
- `2_archive_docs/` - Completed tool implementations

<!-- section_id: "95f3518d-69bb-48af-b5d0-8efa2f84d670" -->
### **trickle_down_1_project/**
Project-specific documentation
- `0_instruction_docs/` - Project constitution and standards
- `1_status_progress_docs/` - Project status and progress
- `2_archive_docs/` - Project completion documentation

<!-- section_id: "bbb28514-d8ac-4cbe-9876-fe31aee82ae7" -->
### **trickle_down_1.5_project_tools/**
Project-specific tools and implementations
- `0_instruction_docs/` - Tool specifications and usage
- `1_status_progress_docs/` - Tool development status
- `2_archive_docs/` - Completed tool implementations

<!-- section_id: "7656fc13-002e-4c82-b256-68d590d51bd8" -->
### **trickle_down_2_features/**
Feature-specific documentation
- `0_instruction_docs/` - Feature specifications and guides
- `1_status_progress_docs/` - Feature development status
- `2_archive_docs/` - Completed feature implementations

<!-- section_id: "e6136182-10be-46ab-ad3a-310f368250d1" -->
### **trickle_down_3_components/**
Component-specific documentation
- `0_instruction_docs/` - Component specifications and guides
- `1_status_progress_docs/` - Component development status
- `2_archive_docs/` - Completed component implementations

<!-- section_id: "789a5202-d226-4ab4-a157-7012835d3d5c" -->
## 📦 Integrated Project Imports

- Project-layer trickle-down docs are consolidated under `integrated_from_projects/I-eat-repo/...` inside each primary numbered directory.
- Use the `trickle_down_<level>/0_instruction_docs/integrated_from_projects/` paths to reach constitutions, environment setup, and tooling references.
- Run `/init` at the beginning of a session so Cursor reloads the flattened layout.
- Adjust any personal automations or notes that pointed at the deprecated nested `trickle-down-*` folders.

<!-- section_id: "351f2f45-fa61-47b1-9825-835b510c9fb5" -->
## 🚀 **Quick Start for AI Agents**

1. **Read Terminal Fix**: `TERMINAL_HANGING_FIX.md`
2. **Read Project Overview**: `0_basic_prompts_throughout/what_to_do_next.md`
3. **Read Environments Guide**: `trickle_down_1_project/0_instruction_docs/ENVIRONMENTS_AND_INTEGRATIONS.md`
4. **Read Project Constitution**: `trickle_down_1_project/0_instruction_docs/constitution.md`
5. **Initialize**: Follow `trickle_down_0_universal/0_instruction_docs/initialization/init-command.md`
6. **Use Proper Tools**: Always use `terminal_wrapper.py` for Python scripts

<!-- section_id: "b21940cb-ba92-4892-8db2-a760a68ec01e" -->
## 🍕 **I-Eat Development Quick Start**

<!-- section_id: "21957a79-40df-4088-abaa-75b375bac571" -->
### Start Development Server
```bash
cd website
npm install
npm run dev
```

<!-- section_id: "b91a9e08-23c8-495e-b8ea-bae450a07612" -->
### Key Development Commands
- **Start Dev Server**: `npm run dev` (runs on http://localhost:5173)
- **Build for Production**: `npm run build`
- **Run Tests**: `npm run test`
- **Lint Code**: `npm run lint`

<!-- section_id: "86087d7b-da9a-42cb-b960-2a3de1571a21" -->
### Project Structure
- **Frontend**: `website/src/` - React application
- **Backend**: Supabase - Authentication and database
- **Documentation**: `0_context/` - Project documentation

<!-- section_id: "811c4c37-5a9a-49ea-b313-87016c91c6ab" -->
## ⚠️ **Critical Rules**

- **NEVER** use `run_terminal_cmd` for Python scripts (hangs)
- **ALWAYS** use `python3 scripts/terminal_wrapper.py --script <script>` for Python scripts
- **FOLLOW** the initialization protocol for proper context loading

<!-- section_id: "6045091a-d62a-4385-96d4-1ca2d94e91b0" -->
## 📚 **Documentation Hierarchy**

This directory follows the Trickle-Down documentation pattern:
- **0_universal_instructions**: Universal rules for all AI agents
- **0.5_setup**: Setup and configuration systems
- **0.75_universal_tools**: Universal tools and utilities
- **1_trickle_down**: Project-specific documentation
- **2_features**: Feature-specific documentation

---

**Remember: Always use the robust script runner system to prevent terminal hanging issues!**
