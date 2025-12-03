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

**Read the Context Management Framework:**
```bash
# From universal context root:
cat 0.00_layer_stage_framework/README.md
```

This explains how the layer + stage system works, how to maintain documentation, and how the agent hierarchy operates. **CRITICAL** for understanding how to navigate and update the context system.

**Read the Navigation and Execution Workflow:**
After understanding the framework, read **Section 4.7** of this file for the step-by-step workflow on:
- How to interpret user prompts
- How to load context layers (universal → project → feature → component)
- How to gather relevant sub-layer content
- How to choose and load the appropriate stage
- How to execute work and update status

**This workflow (Section 4.7) is your guide for every user request.**

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

**CRITICAL:** Read `0.00_layer_stage_framework/README.md` for complete system documentation.

#### 4.1 Understanding the Layer System (Specificity Hierarchy)

The layer system organizes context by specificity, from universal to specific:

- **Layer 0 (Universal)**: Applies to all projects. Contains universal rules, principles, OS setup, AI tools, models, etc.
- **Layer 1 (Project)**: Project-specific context. Depends on Layer 0.
- **Layer 2 (Feature)**: Feature-specific context within a project. Depends on Layers 0 and 1.
- **Layer 3 (Component)**: Component-specific context within a feature. Depends on Layers 0, 1, and 2.

**Each layer follows this structure:**
```
layer_<N>_<name>/
├── <N>.00_ai_manager_system/          # Manager agent home for this layer
├── <N>.01_manager_handoff_documents/  # Inter-layer communication hub
│   ├── <N>.00_to_universal/          # Upward reports (to broader layers)
│   └── <N>.01_to_specific/           # Downstream context (to more specific layers)
├── <N>.02_sub_layers/                # Numbered content slots
│   ├── sub_layer_<N>.01_basic_prompts_throughout/
│   ├── sub_layer_<N>.02_software_engineering_knowledge_system/
│   ├── sub_layer_<N>.03_universal_principles/
│   ├── ... (numbered slots 0.01-0.12 for universal, 1.01-1.12 for project, etc.)
│   └── sub_layer_<N>.12_agent_setup/
└── <N>.99_stages/                    # Chronological workflow stages
    ├── stage_<N>.01_instructions/
    ├── stage_<N>.02_planning/
    ├── stage_<N>.03_design/
    ├── stage_<N>.04_development/
    ├── stage_<N>.05_testing/
    ├── stage_<N>.06_criticism/
    ├── stage_<N>.07_fixing/
    ├── stage_<N>.08_archives/
    └── status_<N>.json                # Tracks current stage and per-stage state
```

**Key Principles:**
- **Numbering**: Zero-padded two digits (e.g., 0.01, 0.10, 0.12) for lexicographic stability
- **Dependency Flow**: Lower-numbered layers are prerequisites for higher-numbered layers
- **Deterministic Navigation**: Agents address work as (Layer, Stage) to load only what's needed

#### 4.2 Understanding the Stage System (Chronological Workflow)

Within each layer, stages represent the chronological workflow:

1. **stage_<N>.01_instructions** - Initial requirements and instructions
2. **stage_<N>.02_planning** - Planning and architecture decisions
3. **stage_<N>.03_design** - Design specifications
4. **stage_<N>.04_development** - Active development work
5. **stage_<N>.05_testing** - Testing and validation
6. **stage_<N>.06_criticism** - Review and critique
7. **stage_<N>.07_fixing** - Bug fixes and corrections
8. **stage_<N>.08_archives** - Completed/archived work

**Each stage folder contains:**
```
stage_<N>.xx_<name>/
├── hand_off_documents/    # Briefs, decisions, outputs for agent handoffs
└── ai_agent_system/      # Runbooks/configs for the stage owner agent
```

**Status Tracking:**
- Each layer's `status_<N>.json` tracks `current_stage` and per-stage state
- States: `not_started | in_progress | blocked | done`
- Enables dashboards and automated routing for agents

#### 4.3 How Layers and Stages Work Together

**Navigation Pattern:**
- Load from outside in: `layer_0 → layer_1 → layer_2 → layer_3`
- Within each layer, operate in the current Stage
- Update status on exit

**Session Workflow:**
1. At session start, load universal layer (`layer_0_universal`)
2. Load relevant project (`layer_1_*`), feature (`layer_2_*`), component (`layer_3_*`) as needed
3. Within each layer, operate in the current Stage
4. Update `status_<N>.json` on exit

**Example Navigation:**
```
Working on feature checkout in project ecommerce:
- Load: layer_0_universal (universal rules)
- Load: layer_1_project_ecommerce (project context)
- Load: layer_2_feature_checkout (feature context)
- Operate in: stage_2.04_development (current stage)
- Update: status_2.json when done
```

#### 4.4 Understanding the Agent Hierarchy

**Manager Agents (Hierarchical):**
- **Universal Manager (Layer 0)**: Oversees all project managers
- **Project Managers (Layer 1)**: Each project has one manager; oversees feature managers for that project
- **Feature Managers (Layer 2)**: Each feature has one manager; oversees component managers for that feature
- **Component Managers (Layer 3)**: Each component has one manager

**Stage Agents (Per Layer):**
- One stage agent per stage per layer (8 stage agents per layer)
- Each stage agent reports to its layer's manager
- Stage agents execute work for their (Layer, Stage) combination

**Communication Paths:**
- **Upward Reports**: `<N>.01_manager_handoff_documents/<N>.00_to_universal/`
  - Reports from more specific layers to broader layers
  - Example: Project manager reports to universal manager
- **Downstream Context**: `<N>.01_manager_handoff_documents/<N>.01_to_specific/`
  - Context packets from broader layers to more specific layers
  - Example: Universal manager provides context to project managers
- **Stage Handoffs**: Inside each `stage_<N>.xx_*/hand_off_documents/` and `ai_agent_system/`
  - Intra-agent transfers within a stage

**Agent Routing:**
- Managers decide which stage agent to activate
- Managers collect results and escalate/delegate via handoff folders
- Status files in `*.99_stages/` keep `current_stage` and per-stage states in sync

#### 4.5 Agent Registry System

**Purpose:** Register manager and stage agents so the universal manager can discover and call them.

**Location:** `0.00_layer_stage_framework/agent_registry_template.md`

**Required Information for Each Agent:**
- `layer`: `0|1|2|3`
- `name`: Human-friendly label (e.g., `universal_manager`, `project_checkout_manager`)
- `manager_path`: Path to manager folder (e.g., `layer_1_project/1.00_ai_manager_system/`)
- `handoff_up`: Path to `<N>.00_to_universal/` (null for universal layer)
- `handoff_down`: Path to `<N>.01_to_specific/`
- `stages_root`: Path to `<N>.99_stages/`
- `stage_agents`: List of stage agent entries with stage id and location
- `invoke_notes`: How to call the manager/stage agents (CLI/API prompt patterns)

**Agent Configuration Considerations:**
- **Model Selection**: Specify primary models and fallback order (see `sub_layer_0.12_agent_setup`)
- **MCP Integration**: Dependencies on MCP servers (see `sub_layer_0.09_mcp_servers_and_tools_setup`)
- **Tool Access**: Universal tools available (see `sub_layer_0.11_universal_tools`)
- **App Context**: AI application context (see `sub_layer_0.08_ai_apps_tools_setup`)

**Usage:**
1. Copy `agent_registry_template.md` to your repo (e.g., `agent_registry.yaml`)
2. Ensure AI setup layers (0.08–0.12) are configured before registering agents
3. Fill entries for every manager agent you will use
4. Specify model fallbacks and MCP dependencies in `invoke_notes`
5. Keep it near top-level context (e.g., next to `MASTER_DOCUMENTATION_INDEX.md`)

#### 4.6 How to Maintain and Update Documentation

**Documentation Update Workflow:**
1. **Identify the Correct Layer**: Determine if content is universal (0), project (1), feature (2), or component (3)
2. **Identify the Correct Slot**: Use numbered slots (e.g., 0.01 for basic prompts, 0.04 for rules, 0.11 for tools)
3. **Update in Place**: Edit files directly in their slot location
4. **Stage Artifacts**: File artifacts by Stage inside `*.99_stages/`
5. **Update Status**: Keep per-layer `status_<N>.json` updated
6. **Commit Changes**: Follow git commit rules (see Section 3.6)

**When Creating New Content:**
- **New Layer**: Copy template from `0.00_layer_stage_framework/` (e.g., `1_project_template/`)
- **New Sub-layer Slot**: Create `sub_layer_<N>.xx_<name>/` inside `<N>.02_sub_layers/`
- **New Stage**: Stages are pre-created in templates; use existing `stage_<N>.xx_*/` folders
- **Legacy Material**: Can live in `legacy_import/` subfolder while reorganizing

**Documentation Organization Principles:**
- **Deterministic Navigation**: Each layer has numbered slots and stages
- **Dependency Clarity**: Higher layers depend on lower ones
- **Handoff & Audit**: Manager system + handoff hub + stage handoff folders enable clean communication
- **Git-Friendly**: Structure is human-readable and version-control friendly

**Updating Master Documentation:**
- Update `MASTER_DOCUMENTATION_INDEX.md` when adding new major sections
- Update `SYSTEM_OVERVIEW.md` when structure changes
- Update this `universal_init_prompt.md` when navigation patterns change

#### 4.7 How to Navigate the System and Execute User Requests

**This is the core workflow for using the context management system. Follow these steps for every user request.**

##### Step 1: Interpret the User's Prompt

**Analyze the user's request to determine:**
- **What** they want to accomplish (the task/goal)
- **Where** it applies (which project, feature, component)
- **What type** of work it is (new feature, bug fix, documentation, setup, etc.)
- **What scope** it requires (universal only, project-specific, feature-specific, component-specific)

**Questions to ask yourself:**
- Does this affect multiple projects? → Universal layer (0)
- Is this project-specific? → Project layer (1)
- Is this feature-specific? → Feature layer (2)
- Is this component-specific? → Component layer (3)
- What stage of work is this? (instructions, planning, design, development, testing, criticism, fixing, archives)

**Example Analysis:**
```
User: "Add a checkout feature to the ecommerce project"

Interpretation:
- Task: Create new feature
- Location: ecommerce project, checkout feature
- Layers needed: 0 (universal), 1 (project_ecommerce), 2 (feature_checkout)
- Stage: Likely starting at stage_2.01_instructions or stage_2.02_planning
- Sub-layers needed: 
  - Universal: 0.01 (prompts), 0.03 (principles), 0.04 (rules), 0.11 (tools)
  - Project: 1.01 (prompts), 1.03 (principles), 1.04 (rules)
  - Feature: 2.01 (prompts), 2.02 (SE knowledge), 2.03 (principles)
```

##### Step 2: Load Context Layers (Outside-In)

**Always start from universal and work down to specific layers.**

**2.1 Load Universal Layer (Layer 0) - REQUIRED**
```bash
# From universal context root:
cd 0_context/layer_0_universal/
```

**Load these universal sub-layers first (foundational):**
- `sub_layer_0.01_basic_prompts_throughout/` - This file and navigation patterns
- `sub_layer_0.03_universal_principles/` - Universal principles that apply everywhere
- `sub_layer_0.04_universal_rules/` - Universal rules (git, terminal, documentation, etc.)

**Then load task-specific universal sub-layers:**
- **For development work**: `sub_layer_0.02_software_engineering_knowledge_system/`, `sub_layer_0.11_universal_tools/`
- **For setup/configuration**: `sub_layer_0.05_os_setup/`, `sub_layer_0.06_coding_app_setup/`, `sub_layer_0.08_ai_apps_tools_setup/`
- **For AI/agent work**: `sub_layer_0.09_mcp_servers_and_tools_setup/`, `sub_layer_0.10_ai_models/`, `sub_layer_0.12_agent_setup/`

**2.2 Load Project Layer (Layer 1) - If project-specific**
```bash
# Navigate to project context (sibling to universal):
cd ../../<project_name>/0_context/0_context/layer_1_project/
```

**Load project sub-layers:**
- `sub_layer_1.01_basic_prompts_throughout/` - Project init prompt
- `sub_layer_1.03_project_principles/` - Project-specific principles
- `sub_layer_1.04_project_rules/` - Project-specific rules
- Task-specific sub-layers as needed

**2.3 Load Feature Layer (Layer 2) - If feature-specific**
```bash
# From project context:
cd ../layer_2_features/layer_2_feature_<name>/
```

**Load feature sub-layers:**
- `sub_layer_2.01_basic_prompts_throughout/` - Feature context
- `sub_layer_2.02_feature_knowledge/` - Feature-specific knowledge
- `sub_layer_2.03_feature_principles/` - Feature-specific principles
- Task-specific sub-layers as needed

**2.4 Load Component Layer (Layer 3) - If component-specific**
```bash
# From feature context:
cd ../layer_3_components/layer_3_component_<name>/
```

**Load component sub-layers as needed for the specific component.**

##### Step 3: Gather Relevant Sub-layer Content

**Within each loaded layer, identify which sub-layer slots contain relevant information:**

**Universal Sub-layer Guide:**
- `0.01` - Basic prompts and navigation (always load)
- `0.02` - Software engineering knowledge (for development)
- `0.03` - Universal principles (always load)
- `0.04` - Universal rules (always load - git, terminal, documentation)
- `0.05` - OS setup (for system configuration)
- `0.06` - Coding app setup (for IDE/editor work)
- `0.07` - Apps/browsers/extensions (for browser work)
- `0.08` - AI apps/tools setup (for AI tool configuration)
- `0.09` - MCP servers and tools (for MCP work)
- `0.10` - AI models (for model selection)
- `0.11` - Universal tools (for tool usage)
- `0.12` - Agent setup (for agent configuration)

**Project/Feature/Component Sub-layers:**
- Mirror the universal pattern (1.01-1.12, 2.01-2.12, 3.01-3.12)
- Load based on what's relevant to the task

**How to Gather Content:**
1. **Read README files** in each relevant sub-layer directory
2. **Check `0_instruction_docs/`** folders for specific guidance
3. **Review `trickle_down_*` folders** for layer-specific content
4. **Look for task-specific documentation** (e.g., `browser-automation/` for browser work)

**Example Content Gathering:**
```
Task: "Fix a bug in the checkout feature"

Universal (Layer 0):
- sub_layer_0.01/ - Navigation patterns
- sub_layer_0.04/ - Git commit rules, testing rules
- sub_layer_0.11/ - Testing tools, debugging tools

Project (Layer 1):
- sub_layer_1.04/ - Project-specific testing rules
- sub_layer_1.11/ - Project-specific tools

Feature (Layer 2):
- sub_layer_2.02/ - Feature knowledge (checkout flow)
- Check stage_2.07_fixing/ for existing fix attempts
```

##### Step 4: Determine and Load the Appropriate Stage

**Check the current stage status:**
```bash
# From the relevant layer directory:
cat <N>.99_stages/status_<N>.json
```

**Stage Selection Logic:**
- **New work/feature**: Start at `stage_<N>.01_instructions` or `stage_<N>.02_planning`
- **Continuing work**: Check `status_<N>.json` for `current_stage`
- **Bug fixes**: Use `stage_<N>.07_fixing`
- **Testing**: Use `stage_<N>.05_testing`
- **Review/critique**: Use `stage_<N>.06_criticism`
- **Archiving**: Use `stage_<N>.08_archives`

**Load Stage Context:**
```bash
# Navigate to the appropriate stage:
cd <N>.99_stages/stage_<N>.xx_<name>/

# Read handoff documents:
cat hand_off_documents/*.md

# Check agent system configs:
cat ai_agent_system/*.md
```

**Stage Folder Contents:**
- `hand_off_documents/` - Previous decisions, briefs, outputs from this stage
- `ai_agent_system/` - Runbooks and configs for the stage agent
- These help you understand what's already been done and what's needed

##### Step 5: Execute the Work

**5.1 Review Loaded Context**
- Verify you have all necessary layers loaded
- Confirm you understand the task scope
- Check for any blocking issues or dependencies

**5.2 Follow Layer-Specific Rules**
- Apply universal rules from Layer 0 (git, terminal, documentation)
- Apply project-specific rules from Layer 1
- Apply feature/component-specific rules from Layer 2/3

**5.3 Execute the Task**
- Use the appropriate tools (from `sub_layer_0.11_universal_tools/` or project-specific tools)
- Follow principles from loaded sub-layers
- Make decisions consistent with the context hierarchy

**5.4 Document and Update Status**
- Update relevant documentation in the appropriate sub-layers
- Create/update handoff documents in the current stage folder
- Update `status_<N>.json` to reflect progress:
  ```json
  {
    "current_stage": "stage_<N>.04_development",
    "stages": {
      "stage_<N>.01_instructions": "done",
      "stage_<N>.02_planning": "done",
      "stage_<N>.03_design": "done",
      "stage_<N>.04_development": "in_progress",
      ...
    }
  }
  ```

**5.5 Commit and Sync**
- Follow git commit rules (see Section 3.6)
- Commit changes to the appropriate repository
- Push to sync cloud/local

##### Step 6: Navigation Commands Reference

**Find Universal Context Root:**
```bash
# If you know this file's location:
cd "$(dirname "$(find ~ -name universal_init_prompt.md -path "*/0_ai_context/*" | head -1)")"
cd ../../..  # Now at <universal_context_root>/0_context/
```

**Navigate Between Layers:**
```bash
# Universal to Project:
cd ../../<project_name>/0_context/0_context/

# Project to Feature:
cd layer_2_features/layer_2_feature_<name>/

# Feature to Component:
cd layer_3_components/layer_3_component_<name>/
```

**Find Project Context:**
```bash
# From universal context root:
cd ../../
find . -maxdepth 2 -type d -name "0_context" | grep -v "0_ai_context"
```

**List Available Layers:**
```bash
# List projects:
ls -d */0_context/0_context/layer_1_*/

# List features in a project:
ls -d <project>/0_context/0_context/layer_2_features/layer_2_*/

# List components in a feature:
ls -d <project>/0_context/0_context/layer_2_features/layer_2_*/layer_3_components/layer_3_*/
```

##### Complete Workflow Example

**User Request:** "Add user authentication to the ecommerce project"

**Step 1: Interpret**
- Task: New feature (authentication)
- Location: ecommerce project
- Layers: 0 (universal), 1 (project_ecommerce), 2 (feature_auth)
- Stage: Start at `stage_2.01_instructions`
- Sub-layers: 0.01, 0.03, 0.04, 0.11; 1.01, 1.03, 1.04; 2.01, 2.02, 2.03

**Step 2: Load Layers**
```bash
# Load universal
cd ~/code/0_ai_context/0_context/layer_0_universal/
# Read: sub_layer_0.01/, sub_layer_0.03/, sub_layer_0.04/, sub_layer_0.11/

# Load project
cd ../../ecommerce/0_context/0_context/layer_1_project/
# Read: sub_layer_1.01/, sub_layer_1.03/, sub_layer_1.04/

# Load/create feature
cd ../layer_2_features/layer_2_feature_auth/
# Read: sub_layer_2.01/, sub_layer_2.02/, sub_layer_2.03/
```

**Step 3: Gather Content**
- Universal rules (git, testing, security principles)
- Project architecture and patterns
- Feature requirements and design

**Step 4: Determine Stage**
```bash
# Check if feature exists and current stage
cat 2.99_stages/status_2.json
# If new, start at stage_2.01_instructions
cd 2.99_stages/stage_2.01_instructions/
```

**Step 5: Execute**
- Follow universal and project rules
- Create authentication feature
- Update documentation
- Update status_2.json

**Step 6: Commit**
- Commit changes following git rules
- Push to sync

### 5. Summaries must keep entrypoints
When summarizing context for any session, you must explicitly retain:
- A reference to this universal init prompt (`layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`) with an instruction to follow it.
- A reference to the active project init prompt (e.g., `<project>/0_context/0_context/0_basic_prompts_throughout/project_init_prompt.md` or its Layer/Stage location) with an instruction to follow it.
Do not remove these references during summarization; they are required navigation anchors.

---

## 📚 Documentation Reference by Task

**All paths relative to `<universal_context_root>/0_context/`**

### Layer + Stage Framework Templates
**MANDATORY READING for context management:**
- **`0.00_layer_stage_framework/README.md`** - Complete documentation of the layer + stage system, how context management works, how to maintain documentation, and how the agent hierarchy operates
- **`0.00_layer_stage_framework/agent_registry_template.md`** - How to register manager and stage agents for discovery

**Templates and Structure:**
- Templates for universal/project/feature/component layers: `0.00_layer_stage_framework/`
- Stage folders (0.01–0.08) and status templates live under each `*.99_stages/`
- Live universal layer (actual content): `layer_0_universal/0.02_sub_layers/`

**Key Concepts (see Section 4 for details):**
- Layer System: universal (0) → project (1) → feature (2) → component (3)
- Stage System: instructions → planning → design → development → testing → criticism → fixing → archives
- Agent Hierarchy: Universal Manager → Project Managers → Feature Managers → Component Managers
- Stage Agents: One per stage per layer, reporting to their layer's manager

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

**⚠️ Linux/Ubuntu Note**: Browser MCP tools have platform-specific issues. See MCP Tools section above for Linux limitations.

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

**⚠️ CRITICAL: Linux/Ubuntu-Specific MCP Issues**
**MANDATORY - Read if running on Linux/Ubuntu:**
- `layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_MCP_SETUP_EXPERIENCE.md` - **Read Lesson 1 first!**

**Key Linux/Ubuntu Limitations:**
1. **Playwright MCP Tools**: Server connects and reports tools, but Cursor IDE on Linux does NOT expose them to AI agents. Tools registered but not accessible.
2. **Browser Path Detection**: Always fails on Linux - must use explicit `--executable-path` in MCP config.
3. **NVM/Node.js**: Requires bash wrapper to load NVM in MCP server processes.
4. **Tool Naming**: May differ from Windows/macOS documentation.

**Workaround**: Use `mcp_browser_*` tools from `@agent-infra/mcp-server-browser` instead of Playwright MCP on Linux.

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
- [ ] **Read `0.00_layer_stage_framework/README.md`** (context management system)
- [ ] **Read `0.00_layer_stage_framework/agent_registry_template.md`** (agent hierarchy)
- [ ] Discovered project context directory (sibling to universal)
- [ ] Read project init prompt (if exists)
- [ ] Read `SYSTEM_OVERVIEW.md` and `USAGE_GUIDE.md`
- [ ] Loaded task-specific universal documentation
- [ ] Understood layer + stage system (Section 4.1-4.6)
- [ ] **Read and understood navigation/execution workflow (Section 4.7)**
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
