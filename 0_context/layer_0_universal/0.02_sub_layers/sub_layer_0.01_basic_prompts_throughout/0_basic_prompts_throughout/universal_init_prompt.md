# Universal Session Initialization - Navigation Hub

**Purpose:** This is the entry point for ALL new AI assistant sessions. It directs you to the right documentation based on your current task.

---

## 🚀 Quick Start (3 Steps)

### 0. Sync Before Anything Else
For every relevant repo (universal + any project/assignment you will touch in this session):
```bash
git pull
git status
```
Do this at the start of the chat/session before any other action.

### 1. Discover Your Location & Read the Master Index

**First, find where you are:**
- This file's location = `<universal_context_root>/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`
- Master Index location = `<universal_context_root>/0_context/MASTER_DOCUMENTATION_INDEX.md`

**Expected directory structure (Layer System):**
```
<parent_directory>/
├── 0_ai_context/                    # Universal context repo
│   └── 0_context/
│       ├── MASTER_DOCUMENTATION_INDEX.md
│       ├── SYSTEM_OVERVIEW.md
│       ├── USAGE_GUIDE.md
│       ├── 0.00_layer_stage_framework/   # Templates
│       └── layer_0_universal/            # Universal layer (content)
│           ├── 0.00_ai_manager_system/
│           ├── 0.01_manager_handoff_documents/
│           │   ├── 0.00_to_universal/
│           │   └── 0.01_to_specific/
│           ├── 0.02_sub_layers/          # All universal slots live here
│           │   ├── sub_layer_0.01_basic_prompts_throughout/
│           │   │   └── 0_basic_prompts_throughout/
│           │   │       └── universal_init_prompt.md  ← You are here
│           │   ├── sub_layer_0.02_software_engineering_knowledge_system/
│           │   ├── sub_layer_0.03_universal_principles/
│           │   ├── sub_layer_0.04_universal_rules/
│           │   ├── sub_layer_0.05_os_setup/
│           │   ├── sub_layer_0.06_coding_app_setup/
│           │   ├── sub_layer_0.07_apps_browsers_extensions_setup/
│           │   ├── sub_layer_0.08_ai_apps_tools_setup/
│           │   ├── sub_layer_0.09_mcp_servers_and_tools_setup/
│           │   ├── sub_layer_0.10_ai_models/
│           │   ├── sub_layer_0.11_universal_tools/
│           │   └── sub_layer_0.12_agent_setup/
│           └── 0.99_stages/
└── <project_name>/                  # Project-specific context repo
    └── 0_context/
        └── 0_context/
            └── 0_basic_prompts_throughout/
                └── project_init_prompt.md
```

**Read the Master Index NOW:**
```bash
# From this file's directory:
cd ../../../..
cat MASTER_DOCUMENTATION_INDEX.md
```

This is your map of the entire universal documentation system.

### 2. Discover & Read Project-Specific Init Prompt

**How to find it:**
1. Your universal context is at `<parent>/0_ai_context/0_context/`
2. Project contexts are siblings: `<parent>/<project_name>/0_context/`
3. Look for: `<parent>/<project_name>/0_context/0_context/0_basic_prompts_throughout/project_init_prompt.md`

**Discovery command:**
```bash
# From universal context root, list all potential project repos:
cd ../../  # Go to parent directory
ls -d */0_context/0_context/0_basic_prompts_throughout/project_init_prompt.md 2>/dev/null | grep -v "0_ai_context"
```

**If project init prompt EXISTS:** Read and follow it immediately.

**If project init prompt DOES NOT EXIST:**
1. Notify the user:
   ```
   ⚠️ No project initialization prompt found.

   Searched in: <parent>/<project_dirs>/0_context/0_context/0_basic_prompts_throughout/

   I can help create one. Would you like me to generate a project_init_prompt.md file?
   ```

2. If user agrees, use template in Section 7

### 3. Load Core Universal Documentation

**All paths relative to `<universal_context_root>/0_context/`:**

#### Critical (Read First):
- `SYSTEM_OVERVIEW.md` - Visual guide to the documentation system
- `USAGE_GUIDE.md` - How to navigate and use the system

#### Essential Universal Protocols:
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/cursor_terminal_issues.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/ai_agent_documentation_rule.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`

### 4. Load the Context Management System (Layer + Stage + Agents)
- **Layer System:** universal (0) → project (1) → feature (2) → component (3). Each layer has:
  - `<N>.00_ai_manager_system/` (manager agent home)
  - `<N>.01_manager_handoff_documents/` (`<N>.00_to_universal/`, `<N>.01_to_specific/`)
  - `<N>.02_sub_layers/` (slots, e.g., `sub_layer_0.01_basic_prompts_throughout`)
  - `<N>.99_stages/` (stage folders with `hand_off_documents/` and `ai_agent_system/`)
- **Stage System:** instructions, planning, design, development, testing, criticism, fixing, archives. One stage agent per stage per layer.
- **Agent hierarchy:** universal manager oversees project managers; project managers oversee feature managers; feature managers oversee component managers; stage agents report to their layer’s manager. Upstream reports: `<N>.00_to_universal/`; downstream/context: `<N>.01_to_specific/`.
- **Registry:** see `0.00_layer_stage_framework/agent_registry_template.md` to register managers/stage agents for discovery.

### 5. Summaries must keep entrypoints
When summarizing context for any session, you must explicitly retain:
- A reference to this universal init prompt (`layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`) with an instruction to follow it.
- A reference to the active project init prompt (e.g., `<project>/0_context/0_context/0_basic_prompts_throughout/project_init_prompt.md` or its Layer/Stage location) with an instruction to follow it.
Do not remove these references during summarization; they are required navigation anchors.

---

## 📚 Documentation Reference by Task

**All paths relative to `<universal_context_root>/0_context/`**

### Layer + Stage Framework Templates
- Templates for universal/project/feature/component layers: `0.00_layer_stage_framework/`
- Stage folders (0.01–0.08) and status templates live under each `*.99_stages/`
- Read `0.00_layer_stage_framework/README.md` for how to copy/rename/populate per project
- Live universal layer (actual content): `layer_0_universal/0.02_sub_layers/`

### For Git Operations
**Read before making commits:**
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

### For Terminal Commands
**Read before executing commands:**
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/cursor_terminal_issues.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/terminal_execution_protocol.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/terminal-quick-reference.md`

### For Browser Automation
**Read before opening browsers:**
- `layer_0_universal/0.02_sub_layers/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/browser_management_policy.md`
- `layer_0_universal/0.02_sub_layers/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/browser_opening_rule.md`
- `layer_0_universal/0.02_sub_layers/sub_layer_0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md`

### For Testing
**Read when creating or running tests:**
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/TESTING_AGENT_SYSTEM_README.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/testing-agent-protocol.md`
- `layer_0_universal/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/testing-agent-instructions.md`

### For MCP Tools
**Read when using Model Context Protocol servers:**
- `layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/README.md`
- `layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_SYSTEM_GUIDE.md`
- `layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/MCP_CONFIGURATION_GUIDE.md`

### For Claude Code Specific
**Read when using Claude Code CLI:**
- `layer_0_universal/0.02_sub_layers/sub_layer_0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md`
- `layer_0_universal/0.02_sub_layers/sub_layer_0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/QUICK_START.md`
- `layer_0_universal/0.02_sub_layers/sub_layer_0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/WHAT_ACTUALLY_WORKS.md`

### For Database Operations (Supabase)
**MANDATORY - Read before any database work:**
- `layer_0_universal/0.02_sub_layers/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/supabase_javascript_integration_rule.md`
- `layer_0_universal/0.02_sub_layers/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/supabase_javascript_quick_reference.md`

### For OAuth/Security Setup
**Read when implementing authentication:**
- `layer_0_universal/0.02_sub_layers/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/google_oauth_production_ready.md`
- `layer_0_universal/0.02_sub_layers/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/sudo_password_management.md`

---

## 🔍 Finding Project-Specific Documentation

**Project context repos are siblings to universal context:**

```
<parent_directory>/
├── 0_ai_context/                           # Universal (you are here)
└── <project_name>/0_context/               # Project-specific
    └── 0_context/
        ├── MASTER_DOCUMENTATION_INDEX.md   # Start here for project docs
        ├── layer_1_project/
        ├── layer_2_features/
        └── layer_3_components/
```

**To navigate from universal to project:**
```bash
# From <universal_context_root>/0_context/
cd ../../<project_name>/0_context/0_context/
```

---

## ⚙️ Session Initialization Checklist

- [ ] Identified universal context root directory
- [ ] Read `MASTER_DOCUMENTATION_INDEX.md` (universal)
- [ ] Discovered project context directory (sibling to universal)
- [ ] Read project init prompt (if exists)
- [ ] Read `SYSTEM_OVERVIEW.md` and `USAGE_GUIDE.md`
- [ ] Loaded task-specific universal documentation
- [ ] Checked git branch in working repository
- [ ] Synced repositories (start-of-session pull for every relevant repo)
- [ ] Reviewed current task context
- [ ] Asked clarifying questions if unclear

---

## 🔄 Mandatory Sync & Context Update Policy (Every Session/Response)

**At start of every chat/session (before work):**
```bash
# From each relevant repo (universal, project, assignment):
git pull
git status
```

**Before ending every response:**
1. Update context/docs with any new decisions/findings (follow `context_update_rule.md`).
2. Stage and commit your changes in the active repo:
   ```bash
   git add .
   git commit -m "<short description>" || true  # skip if nothing to commit
   ```
3. Push to your fork to sync cloud/local:
   ```bash
   git push || true  # skip if nothing to push
   ```
4. Confirm clean status:
   ```bash
   git status
   ```

**Notes:**
- This applies to every response in every session/chat. Do not close a response until context/docs are updated and git state is synced (or explicitly note no changes to commit).
- Use project init prompt for branch rules (e.g., `personal-version` vs `main`).
- Never push to upstream; push to your fork remotes.
- If multiple repos are active (universal + project + assignment), repeat the end-of-response sync for each touched repo.

---

## 🗺️ Directory Discovery Commands

### Find Universal Context Root
```bash
# If you know this file's location:
cd "$(dirname "$(find ~ -name universal_init_prompt.md -path "*/0_ai_context/*" | head -1)")"
cd ../..  # Now at <universal_context_root>/0_context/
```

### Find All Project Contexts
```bash
# From <universal_context_root>/0_context/:
cd ../../
find . -maxdepth 2 -type d -name "0_context" | grep -v "0_ai_context"
```

### Find Project Init Prompts
```bash
# From parent directory:
find . -path "*/0_context/0_context/0_basic_prompts_throughout/project_init_prompt.md" \
  | grep -v "0_ai_context"
```

---

## 📋 Project Init Prompt Template

If generating a new project init prompt, use this structure:

```markdown
# [Project Name] - Project Initialization

## 🔍 Repository Discovery

### Universal Context Location
**Relative path from project context:** `../../0_ai_context/0_context/`

```bash
# Verify universal context exists:
ls ../../0_ai_context/0_context/MASTER_DOCUMENTATION_INDEX.md
```

### Project Context Location
**You are here:** `<parent>/<project_name>/0_context/0_context/`

### Working Repository Location
**Document where your actual work/code repository is:**
- Could be: `<parent>/<project_name>/<work_repo>/`
- Or elsewhere: Document the pattern

## 1. Repository Structure
- List all relevant repositories (context + working repos)
- Show how they relate spatially
- Include git remotes (origin, upstream, etc.)

## 2. Critical Project Rules
- Branch to use
- Environment setup requirements
- Language-specific considerations

## 3. Session Initialization Sequence
- Commands to run at session start (use relative paths)
- Context files to read (relative to project context root)
- Verification steps

## 4. Documentation Map
**All paths relative to `<project_context_root>/0_context/`:**
- `MASTER_DOCUMENTATION_INDEX.md`
- `trickle_down_1_project/0_instruction_docs/...`
- etc.

## 5. Reference Documentation by Task
- Link to project-specific docs (relative paths)
- Reference universal docs: `../../0_ai_context/0_context/...`
- Quick reference commands

## 6. Troubleshooting
- Common issues and solutions
- Where to find help
```

---

## 🎯 Path Resolution Strategy

### Universal Documentation References
**Always relative to:** `<universal_context_root>/0_context/`

Example: `trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`

### Project Documentation References
**Always relative to:** `<project_context_root>/0_context/`

Example: `trickle_down_1_project/0_instruction_docs/constitution.md`

### Cross-References (Project → Universal)
**Use relative path:** `../../0_ai_context/0_context/<path>`

Example from project context:
```bash
# Read universal git rules:
cat ../../0_ai_context/0_context/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md
```

---

## 🎯 Remember

1. **Paths are portable** - All references are relative to known roots
2. **Universal and project are siblings** - Navigate with `../../<name>/`
3. **Master indices are your maps** - Start there when lost
4. **Task-based navigation** - Load only what you need
5. **Ask when uncertain** - Clarify directory structure if confused

---

**Location Pattern:** `<parent>/0_ai_context/0_context/0_basic_prompts_throughout/`
**Last Updated:** 2025-01-26
**Version:** 2.1 (Portable Paths)
