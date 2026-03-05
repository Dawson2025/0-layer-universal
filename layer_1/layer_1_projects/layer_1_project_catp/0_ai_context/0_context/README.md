---
resource_id: "d05ebd73-e508-4cb6-acdb-1dd5ed149a13"
resource_type: "readme
document"
resource_name: "README"
---
# AI Agent Context System
*Universal Trickle-Down Documentation for AI Coding Agents*

## 🚨 **CRITICAL: Terminal Hanging Fix**

**IMPORTANT**: Before using any terminal commands, read the terminal hanging fix:
- **Quick Fix**: `TERMINAL_HANGING_FIX.md` - Immediate solution
- **Full Protocol**: `trickle_down_0_universal/0_instruction_docs/terminal-tool-replacement.md`
- **Quick Reference**: `trickle_down_0_universal/0_instruction_docs/terminal-quick-reference.md`

## 🚨 **CRITICAL: Manual Steps Execution**

**IMPORTANT**: AI agents must execute ALL manual steps directly using available tools:
- **Manual Steps Protocol**: `trickle_down_0_universal/0_instruction_docs/manual-steps-automation.md`
- **Browser Automation**: Use MCP tools for web interface interaction
- **No Delegation**: Never ask users to perform manual steps

## 📁 **Directory Structure**

### **trickle_down_0_universal/**
Universal instructions for all AI agents
- `0_instruction_docs/` - How-to guides, protocols, and procedures
- `1_status_progress_docs/` - Current status and progress reports
- `2_archive_docs/` - Completed work and resolutions
- **Key universal lessons inside `0_instruction_docs/`:**
  - `browser_management_policy.md` and `browser_opening_rule.md` - Keep automation browsers open and use Playwright MCP by default
  - `universal_instructions.md` - Fundamental mindset, analysis, and execution rules for any AI agent
  - `trickle-down-0.0-ai-coding-systems/` - Framework for selecting an AI coding system (Spec Kit, BMAD, AFD, etc.)
  - `agent-patterns/assignment-*.md` - Two-agent planning/execution workflow template for multi-step tasks
  - `cursor_terminal_issues.md` - Cursor IDE output corruption diagnosis plus verified workarounds (preview box toggle, wrapper usage, logging pattern)
  - `canvas_submission_protocol.md` - Required evidence files, upload steps, and integrity rules for Canvas submissions (auto-generated logs only)

### **trickle_down_0.5_setup/**
Setup and configuration systems
- `0_instruction_docs/` - Setup guides and configuration procedures
- `1_status_progress_docs/` - Setup status and progress
- `2_archive_docs/` - Completed setup documentation

### **trickle_down_0.75_universal_tools/**
Universal tools and utilities
- `0_instruction_docs/` - Tool usage guides and procedures
- `1_status_progress_docs/` - Tool development status
- `2_archive_docs/` - Completed tool implementations

### **trickle_down_1_project/**
Project-specific documentation
- `0_instruction_docs/` - Project constitution and standards
- `1_status_progress_docs/` - Project status and progress
- `2_archive_docs/` - Project completion documentation
- `2_testing_docs/` - Testing documentation

### **trickle_down_1.5_project_tools/**
Project-specific tools and implementations
- `0_instruction_docs/` - Tool specifications and usage
- `1_status_progress_docs/` - Tool development status
- `2_archive_docs/` - Completed tool implementations

### **trickle_down_2_features/**
Feature-specific documentation
- `0_instruction_docs/` - Feature specifications and guides
- `1_status_progress_docs/` - Feature development status
- `2_archive_docs/` - Completed feature implementations
- `2_testing_docs/` - Testing documentation

### **trickle_down_2_implementation/**
Implementation-specific documentation
- Contains detailed implementation guides and completed implementations

### **trickle_down_3_components/**
Component-specific documentation
- `0_instruction_docs/` - Component specifications and guides
- `1_status_progress_docs/` - Component development status
- `2_archive_docs/` - Completed component implementations

### **trickle_down_3_testing/**
Testing-specific documentation
- Contains testing guides, test results, and bug reports

## 📦 Integrated Project Imports

- All project-level trickle-down content from `trickle_down_1_project/0_instruction_docs` now lives under the main numbered directories in `integrated_from_projects/<project_name>/`.
- When you need a constitution, environment guide, or tooling spec, follow the path `trickle_down_<level>/0_instruction_docs/integrated_from_projects/catp__0_ai_context/...`.
- Run the `/init` loader at the start of a session so Cursor refreshes paths after this restructure.
- Update any personal snippets or scripts that referenced the removed nested `trickle-down-*` directories.

## 🚀 **Quick Start for AI Agents**

1. **Read Terminal Fix**: `TERMINAL_HANGING_FIX.md`
2. **Read Project Overview**: `0_basic_prompts_throughout/what_to_do_next.md` (update the path in this file to point to your project)
3. **Read Environments Guide**: `trickle_down_1_project/0_instruction_docs/ENVIRONMENTS_AND_INTEGRATIONS.md` (if exists)
4. **Read Project Constitution**: `trickle_down_1_project/0_instruction_docs/constitution.md` (if exists)
5. **Initialize**: Follow `trickle_down_0_universal/0_instruction_docs/initialization/init-command.md` (if exists)
6. **Use Proper Tools**: Always use `terminal_wrapper.py` for Python scripts

## 🔧 **Customization for Your Project**

To adapt this context system for your project:

1. **Update `0_basic_prompts_throughout/what_to_do_next.md`**:
   - Replace project-specific paths
   - Update project overview
   - Add your project's technology stack
   - Define current priorities

2. **Add Project-Specific Documentation**:
   - Create `trickle_down_1_project/0_instruction_docs/project_constitution.md` for your project standards
   - Add project-specific tools to `trickle_down_1.5_project_tools/`
   - Document features in `trickle_down_2_features/`
   - Add component docs to `trickle_down_3_components/`

3. **Configure Your Stack**:
   - Update setup documentation in `trickle_down_0.5_setup/`
   - Add environment-specific configurations
   - Document deployment procedures

## ⚠️ **Critical Rules**

- **NEVER** use `run_terminal_cmd` for Python scripts (hangs)
- **ALWAYS** use `python3 scripts/terminal_wrapper.py --script <script>` for Python scripts
- **FOLLOW** the initialization protocol for proper context loading
- **READ** terminal execution protocol before executing commands

## 📚 **Documentation Hierarchy**

This directory follows the Trickle-Down documentation pattern:
- **0_universal_instructions**: Universal rules for all AI agents
- **0.5_setup**: Setup and configuration systems
- **0.75_universal_tools**: Universal tools and utilities
- **1_project**: Project-specific documentation
- **2_features**: Feature-specific documentation
- **3_components**: Component-specific documentation

---

**Remember: Always use the robust script runner system to prevent terminal hanging issues!**
