ok, I want # Universal Session Initialization - Navigation Hub

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

**Quick Reference for Common Situations:**
**Section 4.8** provides a quick lookup guide mapping common situations to specific context locations. Use it when you need to quickly find where to get context for:
- Development tasks (coding, debugging, testing)
- Setup tasks (OS, IDE, AI tools, MCP servers)
- Git operations
- Terminal commands
- Browser automation
- Database work
- Documentation tasks
- And more...

**Bookmark Section 4.8 for quick reference during work.**

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

**Then load the active stage agent system:**
- For each layer you touch (project/feature/component), enter the current stage folder (e.g., `.../1.99_stages/stage_1.xx_*` or `2.99_stages/stage_2.xx_*`) and open `ai_agent_system/README.md`.
- Follow the init prompts listed there (this universal init + the project init) so every agent session is anchored to both universal and project context.

### 2.1 MCP / Tooling Context (OS + App aware)
If the task involves MCP servers/tools (browser automation, web-search, etc.), load the MCP sublayer and pick your OS + AI app:
- Universal MCP hub:
  - `0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/`
- OS-specific runbooks:
  - `.../sub_layer_0.09_mcp_servers_and_tools_setup/0.01_operating_system/<os>/`
- App-specific runbooks:
  - `.../sub_layer_0.09_mcp_servers_and_tools_setup/0.02_ai_apps/<ai_app>/`

This is where you confirm “headed vs headless” requirements, WSLg env vars, and which MCP server is recommended for the current CLI.

**If project init prompt DOES NOT EXIST:**
1. Notify the user:
   ```
   ⚠️ No project initialization prompt found.

   Searched in: <parent>/<project_dirs>/0_context/0_context/0_basic_prompts_throughout/

   I can help create one. Would you like me to generate a project_init_prompt.md file?
   ```

2. If user agrees, use template in Section 7

**⚠️ CRITICAL PROJECT STRUCTURE REQUIREMENT:**
**Before working on any project, verify it has proper instantiation and organization:**
1. **Check for proper layer structure**: Project must have `layer_1_project/` with proper sub-layers (1.00-1.12) and stages (1.99_stages/)
2. **Check for templates**: If missing, project should be instantiated from `0_ai_context/0_context/0.00_layer_stage_framework/1_project_template/`
3. **Verify organization**: Project structure must match the universal context organization pattern
4. **If structure is missing or incomplete**: You MUST notify the user and help set it up before proceeding with work

See Section 4.9 for detailed project structure requirements and instantiation process.

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
├── docs/                 # Persistent stage notes (checklists, criticism/fix logs)
├── hand_off_documents/    # Briefs, decisions, outputs for agent handoffs
└── ai_agent_system/      # Runbooks/configs for the stage owner agent
```

**Stage logging rule (critical):**
- Store **criticism** in `stage_<N>.06_criticism/docs/` and **fixes** in `stage_<N>.07_fixing/docs/` for the relevant layer/workflow.
- Do not embed workflow-specific criticism/fix content inside init prompts; init prompts should only describe *where* to record it.

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

##### Step 1: Interpret the User's Prompt and Outline Stages

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

**CRITICAL: Outline the stages that will be carried out BEFORE proceeding:**
- Identify which stages are needed for this task
- Determine the starting stage
- Determine the sequence of stages
- Present this outline to the user (or in your internal plan)

**Example Analysis:**
```
User: "Add a checkout feature to the ecommerce project"

Interpretation:
- Task: Create new feature
- Location: ecommerce project, checkout feature
- Layers needed: 0 (universal), 1 (project_ecommerce), 2 (feature_checkout)
- Sub-layers needed: 
  - Universal: 0.01 (prompts), 0.03 (principles), 0.04 (rules), 0.11 (tools)
  - Project: 1.01 (prompts), 1.03 (principles), 1.04 (rules)
  - Feature: 2.01 (prompts), 2.02 (SE knowledge), 2.03 (principles)

Stages to be carried out (at Layer 2 - Feature level):
1. stage_2.01_instructions - Gather requirements and initial instructions
2. stage_2.02_planning - Plan the checkout feature architecture
3. stage_2.03_design - Design the checkout flow and components
4. stage_2.04_development - Implement the checkout feature
5. stage_2.05_testing - Test the checkout feature
6. stage_2.06_criticism - Review and critique the implementation
7. stage_2.07_fixing - Fix any issues found
8. stage_2.08_archives - Archive completed work

Starting stage: stage_2.01_instructions
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

**CRITICAL: Check if project exists before loading:**
```bash
# Check if project context exists:
if [ ! -d "../../<project_name>/0_context/0_context/layer_1_project/" ]; then
  echo "⚠️ Project '<project_name>' does not exist or is not properly instantiated"
  echo "I can help create it. Would you like me to:"
  echo "  1. Create the project structure from template?"
  echo "  2. Set up layer_1_project with all required sub-layers and stages?"
  # STOP and wait for user confirmation
fi
```

**If project is missing:**
1. **STOP** - Do not proceed until project structure exists
2. **NOTIFY** - Inform user that the project doesn't exist or isn't properly instantiated
3. **OFFER** - Offer to create the project structure using the template (see Section 4.9)
4. **WAIT** - Wait for user confirmation before creating structure
5. **CREATE** - If confirmed, follow instantiation process in Section 4.9

**If project exists, navigate and load:**
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

**CRITICAL: Check if feature exists before loading:**
```bash
# From project context, check if feature exists:
if [ ! -d "../layer_2_features/layer_2_feature_<name>/" ]; then
  echo "⚠️ Feature '<name>' does not exist in project '<project_name>'"
  echo "I can help create it. Would you like me to:"
  echo "  1. Create the feature structure from template?"
  echo "  2. Set up layer_2_feature_<name> with all required sub-layers and stages?"
  # STOP and wait for user confirmation
fi
```

**If feature is missing:**
1. **STOP** - Do not proceed until feature structure exists
2. **NOTIFY** - Inform user that the feature doesn't exist
3. **OFFER** - Offer to create the feature structure using the template:
   - Copy from: `0_ai_context/0_context/0.00_layer_stage_framework/2_feature_template/`
   - To: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/`
4. **WAIT** - Wait for user confirmation before creating structure
5. **CREATE** - If confirmed, create feature structure following template pattern

**If feature exists, navigate and load:**
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

**CRITICAL: Check if component exists before loading:**
```bash
# From feature context, check if component exists:
if [ ! -d "../layer_3_components/layer_3_component_<name>/" ]; then
  echo "⚠️ Component '<name>' does not exist in feature '<feature_name>'"
  echo "I can help create it. Would you like me to:"
  echo "  1. Create the component structure from template?"
  echo "  2. Set up layer_3_component_<name> with all required sub-layers and stages?"
  # STOP and wait for user confirmation
fi
```

**If component is missing:**
1. **STOP** - Do not proceed until component structure exists
2. **NOTIFY** - Inform user that the component doesn't exist
3. **OFFER** - Offer to create the component structure using the template:
   - Copy from: `0_ai_context/0_context/0.00_layer_stage_framework/3_component_template/`
   - To: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/layer_3_components/layer_3_component_<name>/`
4. **WAIT** - Wait for user confirmation before creating structure
5. **CREATE** - If confirmed, create component structure following template pattern

**If component exists, navigate and load:**
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

##### Step 4: Outline Stages and Determine Appropriate Level

**CRITICAL: Before executing, outline all stages that will be carried out at the appropriate layer level.**

**4.1 Check Current Stage Status:**
```bash
# From the relevant layer directory:
cat <N>.99_stages/status_<N>.json
```

**4.2 Determine Which Layer Level to Work At:**
- **Universal work** (affects all projects): Work at Layer 0 level
- **Project work** (affects entire project): Work at Layer 1 level
- **Feature work** (affects specific feature): Work at Layer 2 level
- **Component work** (affects specific component): Work at Layer 3 level

**4.3 Outline the Stages That Will Be Carried Out:**

**Present a clear outline of stages before proceeding. Example:**
```
For task: "Add checkout feature to ecommerce project"

Working at: Layer 2 (Feature level) - layer_2_feature_checkout

Stages to be carried out:
1. stage_2.01_instructions - Gather requirements and initial instructions
2. stage_2.02_planning - Plan checkout feature architecture
3. stage_2.03_design - Design checkout flow and components
4. stage_2.04_development - Implement checkout feature
5. stage_2.05_testing - Test checkout feature
6. stage_2.06_criticism - Review and critique implementation
7. stage_2.07_fixing - Fix any issues found
8. stage_2.08_archives - Archive completed work

Starting at: stage_2.01_instructions
Current status: All stages marked as "not_started"
```

**4.4 Stage Selection Logic:**
- **New work/feature**: Start at `stage_<N>.01_instructions` or `stage_<N>.02_planning`
- **Continuing work**: Check `status_<N>.json` for `current_stage`
- **Bug fixes**: Use `stage_<N>.07_fixing`
- **Testing**: Use `stage_<N>.05_testing`
- **Review/critique**: Use `stage_<N>.06_criticism`
- **Archiving**: Use `stage_<N>.08_archives`

**4.5 Load Stage Context:**
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

**4.6 Confirm Stage Outline with User (if needed):**
- If the task is complex or ambiguous, present the stage outline to the user
- Get confirmation that the outlined stages match their expectations
- Adjust the outline based on user feedback before proceeding

##### Step 5: Execute the Work at the Appropriate Level

**CRITICAL: Execute work at the layer level determined in Step 4.2, following the stages outlined in Step 4.3.**

**5.1 Review Loaded Context**
- Verify you have all necessary layers loaded (universal → project → feature → component)
- Confirm you understand the task scope
- Verify you're working at the correct layer level
- Check for any blocking issues or dependencies
- Ensure all required project/feature/component structures exist (from Step 2)

**5.2 Follow Layer-Specific Rules**
- Apply universal rules from Layer 0 (git, terminal, documentation)
- Apply project-specific rules from Layer 1 (if working at project level or below)
- Apply feature-specific rules from Layer 2 (if working at feature level or below)
- Apply component-specific rules from Layer 3 (if working at component level)

**5.3 Execute the Task at the Appropriate Level**

**Work at the layer level determined in Step 4:**
- **Layer 0 (Universal)**: Work affects all projects - execute in `layer_0_universal/<N>.99_stages/stage_0.xx_*/`
- **Layer 1 (Project)**: Work affects entire project - execute in `layer_1_project/1.99_stages/stage_1.xx_*/`
- **Layer 2 (Feature)**: Work affects specific feature - execute in `layer_2_feature_<name>/2.99_stages/stage_2.xx_*/`
- **Layer 3 (Component)**: Work affects specific component - execute in `layer_3_component_<name>/3.99_stages/stage_3.xx_*/`

**Follow the outlined stages from Step 4.3:**
- Execute each stage in sequence
- Complete one stage before moving to the next
- Update status after each stage completion
- Use stage-specific tools and documentation

**Execution Guidelines:**
- Use the appropriate tools (from `sub_layer_0.11_universal_tools/` or project/feature-specific tools)
- Follow principles from loaded sub-layers at the working level
- Make decisions consistent with the context hierarchy
- Create artifacts in the appropriate stage folder at the working level

**5.4 Document and Update Status at the Working Level**

**Update documentation in the appropriate sub-layers at the working level:**
- If working at Layer 1: Update `layer_1_project/1.02_sub_layers/sub_layer_1.xx_*/`
- If working at Layer 2: Update `layer_2_feature_<name>/2.02_sub_layers/sub_layer_2.xx_*/`
- If working at Layer 3: Update `layer_3_component_<name>/3.02_sub_layers/sub_layer_3.xx_*/`

**Create/update handoff documents in the current stage folder:**
- Place in: `<N>.99_stages/stage_<N>.xx_*/hand_off_documents/`
- Document decisions, outputs, and context for next stage

**Update `status_<N>.json` at the working level to reflect progress:**
```json
{
  "current_stage": "stage_<N>.04_development",
  "stages": {
    "stage_<N>.01_instructions": "done",
    "stage_<N>.02_planning": "done",
    "stage_<N>.03_design": "done",
    "stage_<N>.04_development": "in_progress",
    "stage_<N>.05_testing": "not_started",
    "stage_<N>.06_criticism": "not_started",
    "stage_<N>.07_fixing": "not_started",
    "stage_<N>.08_archives": "not_started"
  }
}
```

**5.5 Commit and Sync**
- Follow git commit rules (see Section 3.6)
- Commit changes to the appropriate repository (universal, project, or both)
- Push to sync cloud/local
- Update status files reflect the current state

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

**Step 1: Interpret and Outline Stages**
- Task: New feature (authentication)
- Location: ecommerce project
- Layers: 0 (universal), 1 (project_ecommerce), 2 (feature_auth)
- Sub-layers: 0.01, 0.03, 0.04, 0.11; 1.01, 1.03, 1.04; 2.01, 2.02, 2.03

**Stages to be carried out (at Layer 2 - Feature level):**
1. stage_2.01_instructions - Gather authentication requirements
2. stage_2.02_planning - Plan authentication architecture
3. stage_2.03_design - Design authentication flow and components
4. stage_2.04_development - Implement authentication feature
5. stage_2.05_testing - Test authentication feature
6. stage_2.06_criticism - Review and critique implementation
7. stage_2.07_fixing - Fix any issues found
8. stage_2.08_archives - Archive completed work

**Starting stage:** stage_2.01_instructions

**Step 2: Load Layers (Check for Missing Structure)**
```bash
# Load universal (always exists)
cd ~/code/0_ai_context/0_context/layer_0_universal/
# Read: sub_layer_0.01/, sub_layer_0.03/, sub_layer_0.04/, sub_layer_0.11/

# Check if project exists
if [ ! -d "../../ecommerce/0_context/0_context/layer_1_project/" ]; then
  echo "⚠️ Project 'ecommerce' does not exist or is not properly instantiated"
  echo "I can help create it. Would you like me to set up the project structure?"
  # STOP and wait for user confirmation
  # If confirmed, follow Section 4.9 instantiation process
fi

# Load project (after verification)
cd ../../ecommerce/0_context/0_context/layer_1_project/
# Read: sub_layer_1.01/, sub_layer_1.03/, sub_layer_1.04/

# Check if feature exists
if [ ! -d "../layer_2_features/layer_2_feature_auth/" ]; then
  echo "⚠️ Feature 'auth' does not exist in project 'ecommerce'"
  echo "I can help create it. Would you like me to:"
  echo "  1. Create the feature structure from template?"
  echo "  2. Set up layer_2_feature_auth with all required sub-layers and stages?"
  # STOP and wait for user confirmation
  # If confirmed, copy from 2_feature_template/
fi

# Load/create feature (after verification or creation)
cd ../layer_2_features/layer_2_feature_auth/
# Read: sub_layer_2.01/, sub_layer_2.02/, sub_layer_2.03/
```

**Step 3: Gather Content**
- Universal rules (git, testing, security principles)
- Project architecture and patterns
- Feature requirements and design

**Step 4: Outline Stages and Determine Level**
```bash
# Check current stage status
cat 2.99_stages/status_2.json

# Working at: Layer 2 (Feature level) - layer_2_feature_auth
# Stages outlined in Step 1
# Starting at: stage_2.01_instructions

cd 2.99_stages/stage_2.01_instructions/
```

**Step 5: Execute at Layer 2 Level**
- Follow universal and project rules
- Execute work in `layer_2_feature_auth/2.99_stages/stage_2.xx_*/`
- Create authentication feature
- Update documentation in `layer_2_feature_auth/2.02_sub_layers/sub_layer_2.xx_*/`
- Update status_2.json at Layer 2 level:
  ```json
  {
    "current_stage": "stage_2.01_instructions",
    "stages": {
      "stage_2.01_instructions": "in_progress",
      "stage_2.02_planning": "not_started",
      ...
    }
  }
  ```

**Step 6: Commit**
- Commit changes following git rules
- Push to sync
- Status files updated at Layer 2 level

#### 4.8 Quick Reference: Where to Find Context for Common Situations

**Use this as a quick lookup guide when you need to know where to find context for specific situations.**

**All paths are relative to `<universal_context_root>/0_context/`**

##### Development & Coding Tasks

**Starting a new feature:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/` (this file)
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.02_software_engineering_knowledge_system/` (SE knowledge)
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.03_universal_principles/` (principles)
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/` (rules)
- Project: `<project>/0_context/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.02_project_se_knowledge/`
- Feature: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/2.99_stages/stage_2.01_instructions/`

**Writing code:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.02_software_engineering_knowledge_system/`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.11_universal_tools/` (development tools)
- Project: `<project>/0_context/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.02_project_se_knowledge/`
- Feature: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/2.02_sub_layers/sub_layer_2.02_feature_knowledge/`
- Stage: Check `2.99_stages/status_2.json` for current stage, then load `stage_2.04_development/`

**Debugging/Fixing bugs:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/` (testing rules)
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.11_universal_tools/` (debugging tools)
- Feature: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/2.99_stages/stage_2.07_fixing/`
- Check: `2.99_stages/stage_2.07_fixing/hand_off_documents/` for previous fix attempts

**Testing:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/TESTING_AGENT_SYSTEM_README.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.11_universal_tools/` (testing tools)
- Feature: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/2.99_stages/stage_2.05_testing/`

##### Setup & Configuration Tasks

**OS/System setup:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.05_os_setup/`
- Check: `sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/` for OS-specific guides

**IDE/Editor setup:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.06_coding_app_setup/`
- Check: `sub_layer_0.06_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/` for IDE-specific guides

**Browser/Extension setup:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.07_apps_browsers_extensions_setup/`

**AI Apps/Tools setup:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.08_ai_apps_tools_setup/`
- Check: `sub_layer_0.08_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/` for app-specific guides

**MCP Servers setup:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/`
- Check: `sub_layer_0.09_mcp_servers_and_tools_setup/trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/`
- **Linux/Ubuntu users**: Read `BROWSER_MCP_SETUP_EXPERIENCE.md` first!

**AI Models configuration:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.10_ai_models/`
- Check: `sub_layer_0.10_ai_models/trickle_down_0.5_setup/0_instruction_docs/` for model access issues

**Agent setup:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.12_agent_setup/`
- Registry: `0.00_layer_stage_framework/agent_registry_template.md`

##### Git & Version Control

**Making commits:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

**Syncing repos:**
- Always start with: `git pull` and `git status` in each relevant repo
- See Section 0 (Quick Start) for sync workflow

##### Terminal & Command Execution

**Running terminal commands:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/cursor_terminal_issues.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/terminal_execution_protocol.md`
- **Python scripts**: Use `python3 scripts/terminal_wrapper.py --script <script_path>`

##### Browser Automation

**Browser automation tasks:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/browser_management_policy.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/browser_opening_rule.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.11_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/`

**MCP Browser tools (Linux/Ubuntu):**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/BROWSER_MCP_SETUP_EXPERIENCE.md`
- **CRITICAL**: Read Lesson 1 first! Playwright MCP tools don't work on Linux in Cursor IDE.

##### Database Operations

**Supabase/Database work:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/supabase_javascript_integration_rule.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/supabase_javascript_quick_reference.md`

##### Authentication & Security

**OAuth/Security setup:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/google_oauth_production_ready.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/sudo_password_management.md`

##### Documentation Tasks

**Updating documentation:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/ai_agent_documentation_rule.md`
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`
- See Section 4.6 for documentation maintenance workflow

**Finding project documentation:**
- Project: `<project>/0_context/0_context/MASTER_DOCUMENTATION_INDEX.md`
- Project: `<project>/0_context/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts_throughout/` (project init prompt)

##### Planning & Design Tasks

**Planning a new feature:**
- Universal: `layer_0_universal/0.02_sub_layers/sub_layer_0.03_universal_principles/`
- Project: `<project>/0_context/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.03_project_principles/`
- Feature: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/2.99_stages/stage_2.02_planning/`

**Design work:**
- Feature: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/2.99_stages/stage_2.03_design/`
- Check: `stage_2.03_design/hand_off_documents/` for design decisions

##### Review & Critique

**Code review/critique:**
- Feature: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/2.99_stages/stage_2.06_criticism/`
- Check: `stage_2.06_criticism/hand_off_documents/` for review notes

##### Agent & Manager Tasks

**Registering agents:**
- Template: `0.00_layer_stage_framework/agent_registry_template.md`
- Agent setup: `layer_0_universal/0.02_sub_layers/sub_layer_0.12_agent_setup/`

**Manager handoffs:**
- Upward reports: `<N>.01_manager_handoff_documents/<N>.00_to_universal/`
- Downstream context: `<N>.01_manager_handoff_documents/<N>.01_to_specific/`
- Stage handoffs: `<N>.99_stages/stage_<N>.xx_*/hand_off_documents/`

##### Finding Current Status

**Check what stage work is in:**
- Feature: `<project>/0_context/0_context/layer_2_features/layer_2_feature_<name>/2.99_stages/status_2.json`
- Project: `<project>/0_context/0_context/layer_1_project/1.99_stages/status_1.json`

**Find previous work/decisions:**
- Check: `<N>.99_stages/stage_<N>.xx_*/hand_off_documents/` for previous decisions
- Check: `<N>.99_stages/stage_<N>.08_archives/` for completed work

##### Platform-Specific Issues

**Linux/Ubuntu issues:**
- MCP: `layer_0_universal/0.02_sub_layers/sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- Cursor IDE: `layer_0_universal/0.02_sub_layers/sub_layer_0.06_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- AI Apps: `layer_0_universal/0.02_sub_layers/sub_layer_0.08_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- Models: `layer_0_universal/0.02_sub_layers/sub_layer_0.10_ai_models/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md`
- Tools: `layer_0_universal/0.02_sub_layers/sub_layer_0.11_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/LINUX_UBUNTU_TOOL_ACCESS_ISSUES.md`

##### Quick Decision Tree

**"I need to..."**

- **...write code** → `sub_layer_0.02_software_engineering_knowledge_system/` + `sub_layer_0.11_universal_tools/` + project/feature SE knowledge
- **...run a terminal command** → `sub_layer_0.04_universal_rules/.../UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- **...make a git commit** → `sub_layer_0.04_universal_rules/.../git_commit_rule.md`
- **...set up something** → `sub_layer_0.05_os_setup/` through `sub_layer_0.12_agent_setup/` (depending on what)
- **...use browser automation** → `sub_layer_0.11_universal_tools/.../browser-automation/` + MCP tools docs
- **...work on a feature** → Load layers 0 → 1 → 2, check `2.99_stages/status_2.json` for current stage
- **...find project rules** → `<project>/0_context/0_context/layer_1_project/1.02_sub_layers/sub_layer_1.04_project_rules/`
- **...understand the system** → `0.00_layer_stage_framework/README.md` + Section 4 of this file
- **...navigate the system** → Section 4.7 of this file (navigation workflow)

#### 4.9 Project Structure Requirements and Instantiation

**MANDATORY RULE: Any project being worked on MUST have proper instantiation and organization as laid out in the universal context repository.**

##### Required Project Structure

**A properly instantiated project must have:**

1. **Project Context Root**: `<parent>/<project_name>/0_context/0_context/`

2. **Layer 1 (Project Layer)**: `layer_1_project/` with complete structure:
   ```
   layer_1_project/
   ├── 1.00_ai_manager_system/          # Manager agent home
   ├── 1.01_manager_handoff_documents/  # Inter-layer communication
   │   ├── 1.00_to_universal/          # Upward reports
   │   └── 1.01_to_specific/           # Downstream context
   ├── 1.02_sub_layers/                 # Numbered content slots
   │   ├── sub_layer_1.01_basic_prompts_throughout/
   │   ├── sub_layer_1.02_project_se_knowledge/
   │   ├── sub_layer_1.03_project_principles/
   │   ├── sub_layer_1.04_project_rules/
   │   ├── sub_layer_1.05_project_os_setup/
   │   ├── sub_layer_1.06_project_coding_app_setup/
   │   ├── sub_layer_1.07_project_apps_browsers_extensions_setup/
   │   ├── sub_layer_1.08_project_ai_apps_tools_setup/
   │   ├── sub_layer_1.09_project_mcp_servers_and_tools_setup/
   │   ├── sub_layer_1.10_project_ai_models/
   │   ├── sub_layer_1.11_project_tools/
   │   └── sub_layer_1.12_project_agent_setup/
   └── 1.99_stages/                     # Chronological workflow stages
       ├── stage_1.01_instructions/
       ├── stage_1.02_planning/
       ├── stage_1.03_design/
       ├── stage_1.04_development/
       ├── stage_1.05_testing/
       ├── stage_1.06_criticism/
       ├── stage_1.07_fixing/
       ├── stage_1.08_archives/
       └── status_1.json                # Tracks current stage and per-stage state
   ```

3. **Project Init Prompt**: `<project>/0_context/0_context/0_basic_prompts_throughout/project_init_prompt.md`
   - Or located in: `layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts_throughout/`

4. **Master Documentation Index**: `<project>/0_context/0_context/MASTER_DOCUMENTATION_INDEX.md`

5. **Optional but Recommended**:
   - `layer_2_features/` - For feature-specific layers
   - `layer_3_components/` - For component-specific layers

##### Verification Checklist

**Before starting work on any project, verify:**

- [ ] Project has `0_context/0_context/` directory structure
- [ ] Project has `layer_1_project/` directory
- [ ] `layer_1_project/` has `1.00_ai_manager_system/` directory
- [ ] `layer_1_project/` has `1.01_manager_handoff_documents/` with `1.00_to_universal/` and `1.01_to_specific/`
- [ ] `layer_1_project/` has `1.02_sub_layers/` directory
- [ ] `layer_1_project/` has `1.99_stages/` directory with all 8 stage folders
- [ ] `layer_1_project/1.99_stages/status_1.json` exists
- [ ] Project init prompt exists (either in `0_basic_prompts_throughout/` or `sub_layer_1.01_basic_prompts_throughout/`)
- [ ] Project structure mirrors universal context organization pattern

##### Instantiation Process

**If a project is missing proper structure, you MUST help set it up:**

**Step 1: Identify Missing Structure**
```bash
# From project context root:
cd <project>/0_context/0_context/

# Check for layer_1_project:
ls -d layer_1_project/ 2>/dev/null || echo "MISSING: layer_1_project/"

# Check for required subdirectories:
[ -d "layer_1_project/1.02_sub_layers" ] || echo "MISSING: 1.02_sub_layers/"
[ -d "layer_1_project/1.99_stages" ] || echo "MISSING: 1.99_stages/"
```

**Step 2: Copy Template from Universal Context**
```bash
# From universal context root:
cd <parent>/0_ai_context/0_context/0.00_layer_stage_framework/

# Copy project template to project context:
cp -r 1_project_template/ <parent>/<project>/0_context/0_context/layer_1_project/
```

**Step 3: Rename and Customize**
```bash
# From project context root:
cd <project>/0_context/0_context/layer_1_project/

# The template should already have correct numbering (1.00, 1.01, etc.)
# Customize sub-layer content as needed
# Populate project-specific content in sub_layers
```

**Step 4: Create Project Init Prompt**
- Use template from Section 7 of this file
- Place in: `<project>/0_context/0_context/0_basic_prompts_throughout/project_init_prompt.md`
- Or in: `layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts_throughout/`

**Step 5: Create Master Documentation Index**
- Create: `<project>/0_context/0_context/MASTER_DOCUMENTATION_INDEX.md`
- Reference universal index structure
- Document project-specific documentation locations

**Step 6: Initialize Status File**
```bash
# Create status_1.json:
cat > layer_1_project/1.99_stages/status_1.json << 'EOF'
{
  "current_stage": "stage_1.01_instructions",
  "stages": {
    "stage_1.01_instructions": "not_started",
    "stage_1.02_planning": "not_started",
    "stage_1.03_design": "not_started",
    "stage_1.04_development": "not_started",
    "stage_1.05_testing": "not_started",
    "stage_1.06_criticism": "not_started",
    "stage_1.07_fixing": "not_started",
    "stage_1.08_archives": "not_started"
  }
}
EOF
```

**Step 7: Verify Structure**
- Run verification checklist above
- Ensure all required directories exist
- Ensure all required files exist

##### When to Enforce This Rule

**You MUST check and enforce this rule when:**

1. **Starting work on a new project** - Verify structure exists before proceeding
2. **User requests work on a project** - Check structure as part of Step 2 (Discover Project)
3. **Project context seems incomplete** - Verify all required components exist
4. **Navigating to project layers** - Ensure structure matches expected pattern

**If structure is missing:**
1. **STOP** - Do not proceed with work until structure is in place
2. **NOTIFY** - Inform user that project needs proper instantiation
3. **OFFER HELP** - Offer to set up the structure using the instantiation process
4. **WAIT** - Wait for user confirmation before creating structure

##### Benefits of Proper Structure

**Projects with proper structure enable:**
- Deterministic navigation (agents know where to find context)
- Proper layer hierarchy (project depends on universal)
- Stage-based workflow tracking
- Manager/agent system integration
- Clean handoff documents and communication
- Status tracking and progress monitoring
- Consistent documentation organization

**Projects without proper structure:**
- Cannot leverage the context management system
- Make navigation and context loading difficult
- Prevent proper agent hierarchy integration
- Block stage-based workflow tracking
- Create maintenance and organization problems

##### Template Location

**Project template is located at:**
```
<universal_context_root>/0_context/0.00_layer_stage_framework/1_project_template/
```

**Template includes:**
- Complete `layer_1_project/` structure
- All required sub-layers (1.01-1.12)
- All required stages (1.01-1.08)
- Manager system folders
- Handoff document folders
- Status template

**See also:**
- `0.00_layer_stage_framework/README.md` - How to instantiate layers
- Section 4.6 - How to maintain and update documentation

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
**Read when using Model Context Protocol servers or troubleshooting issues:**
- `layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/trickle_down_0.75_universal_tools/0_instruction_docs/mcp-tools/README.md` - **Start here for an overview of MCP setup, automation, and specific OS/AI tool documentation.**

### For ALEKS Mathematics Input (Critical!)

**When entering mathematical expressions with exponents in ALEKS:**

- **Use the Exponent button** to insert exponents in the equation editor
- **CRITICAL: After entering the exponent, ALWAYS press the right arrow key (→)** to exit the exponent space
- **Without the right arrow**, subsequent characters will be entered as part of the exponent or in the wrong location
- Example: To enter "x^2 + 3x - 14":
  1. Type "x"
  2. Click Exponent button
  3. Type "2"
  4. **Press right arrow (→) to exit exponent**
  5. Type "+ 3x - 14"
- This applies to all ALEKS math editor interactions with exponents

### ALEKS Math Input Helper Functions (Playwright)

**Use these reusable Playwright functions when automating ALEKS math expression entry:**

#### 1. Enter Fraction (numerator/denominator)

```javascript
// Enters a fraction using ALEKS Fraction button
async function enterFraction(page, numerator, denominator) {
  // Click Fraction button
  await page.getByRole('button', { name: 'Fraction' }).first().click();
  await page.waitForTimeout(150);

  // Type numerator
  await page.keyboard.type(numerator);
  await page.waitForTimeout(100);

  // Tab to denominator
  await page.keyboard.press('Tab');
  await page.waitForTimeout(100);

  // Type denominator
  await page.keyboard.type(denominator);
  await page.waitForTimeout(200);
}
```

#### 2. Enter Exponent (with critical right arrow)
```javascript
// Enters a single exponent with right arrow exit (CRITICAL)
async function enterExponent(page, base, exponent) {
  // Type base variable
  await page.keyboard.type(base);
  await page.waitForTimeout(100);

  // Click Exponent button
  await page.getByRole('button', { name: 'Exponent' }).click();
  await page.waitForTimeout(150);

  // Type exponent
  await page.keyboard.type(exponent);
  await page.waitForTimeout(100);

  // CRITICAL: Press right arrow to exit exponent space
  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(100);
}
```

#### 3. Enter Square Root
```javascript
// Enters content under a square root
async function enterSquareRoot(page, content) {
  // Click Square root button
  await page.getByRole('button', { name: 'Square root' }).click();
  await page.waitForTimeout(150);

  // Type content under square root
  await page.keyboard.type(content);
  await page.waitForTimeout(200);
}
```

#### 4. Enter Polynomial with Exponents
```javascript
// Enters polynomial like x^2 + 3x - 14 with correct exponent handling
async function enterPolynomial(page, terms) {
  // terms = [{base: 'x', exp: '2'}, {op: '+', coef: '3', var: 'x'}, {op: '-', num: '14'}]

  for (const term of terms) {
    if (term.base && term.exp) {
      // Term with exponent
      await enterExponent(page, term.base, term.exp);
    } else if (term.coef && term.var) {
      // Coefficient and variable
      await page.keyboard.type(term.op || '');
      await page.keyboard.type(term.coef);
      await page.keyboard.type(term.var);
      await page.waitForTimeout(100);
    } else if (term.num) {
      // Just a number
      await page.keyboard.type(term.op || '');
      await page.keyboard.type(term.num);
      await page.waitForTimeout(100);
    }
  }
}
```

#### 5. Fill Answer Field with Complex Expression
```javascript
// Main handler for filling an ALEKS answer field with expression
async function fillALEKSAnswer(page, fieldRef, expressionType, expressionData) {
  // Focus on the field
  const field = await page.locator(`[ref="${fieldRef}"]`);
  await field.focus();
  await page.waitForTimeout(300);

  switch(expressionType) {
    case 'fraction':
      await enterFraction(page, expressionData.numerator, expressionData.denominator);
      break;
    case 'exponent':
      await enterExponent(page, expressionData.base, expressionData.exponent);
      break;
    case 'sqrt':
      await enterSquareRoot(page, expressionData.content);
      break;
    case 'polynomial':
      await enterPolynomial(page, expressionData.terms);
      break;
    case 'sqrt-polynomial':
      await enterSquareRoot(page, expressionData.polynomialContent);
      break;
  }
}
```

#### 6. Enter Domain Intervals with Union Notation (CRITICAL!)

**When entering domain intervals with union notation (e.g., (-∞, -1) ∪ (-1, ∞)):**

**The PROCEDURE (MUST FOLLOW THIS ORDER):**
1. **Click the parentheses/brackets button** for the first interval (e.g., "Left paren comma right paren")
2. **Fill it out**, pressing Tab between the two numbers/symbols you're inputting
3. **Once complete, press the RIGHT ARROW KEY** - This exits the cursor OUT of the parentheses (CRITICAL!)
4. **Click the union button**
5. **Click the parentheses/brackets button** for the second interval
6. **Fill that one too** (Tab between numbers)

**Example: Entering (-∞, -1) ∪ (-1, ∞):**
- Click "Left paren comma right paren" button
- Click "Negative infinity" button (for -∞)
- Press Tab
- Type "-1"
- **Press RIGHT ARROW KEY** (EXIT THE PARENTHESES - this is critical!)
- Click "Union" button
- Click "Left paren comma right paren" button
- Type "-1"
- Press Tab
- Click "Infinity" button (for ∞)

**Why the right arrow key is critical:** Without pressing the right arrow to exit each interval, the ALEKS parser doesn't properly close the parentheses and the next element (union or additional interval) won't format correctly.

```javascript
// Helper function for entering domain with union
async function enterDomainWithUnion(page, interval1, interval2, button1Type, button2Type) {
  // interval1 = {value1: '-∞', value2: '-1'} with button type (e.g., 'Left paren comma right paren')
  // interval2 = {value1: '-1', value2: '∞'} with button type (e.g., 'Left paren comma right paren')

  // First interval
  const btn1 = await page.locator(`button[aria-label="${button1Type}"]`);
  await btn1.click({ force: true });
  await page.waitForTimeout(200);

  // Handle special symbols for interval1.value1
  if (interval1.value1 === '-∞') {
    const negInfBtn = await page.locator('button[aria-label="Negative infinity"]');
    await negInfBtn.click({ force: true });
  } else {
    await page.keyboard.type(interval1.value1);
  }
  await page.waitForTimeout(100);

  // Tab to next field
  await page.keyboard.press('Tab');
  await page.waitForTimeout(100);

  // Enter second value
  await page.keyboard.type(interval1.value2);
  await page.waitForTimeout(100);

  // CRITICAL: Exit the parentheses with right arrow
  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(200);

  // Union button
  const unionBtn = await page.locator('button[aria-label="Union"]');
  await unionBtn.click({ force: true });
  await page.waitForTimeout(300);

  // Second interval
  const btn2 = await page.locator(`button[aria-label="${button2Type}"]`);
  await btn2.click({ force: true });
  await page.waitForTimeout(200);

  // Enter first value
  await page.keyboard.type(interval2.value1);
  await page.waitForTimeout(100);

  // Tab to next field
  await page.keyboard.press('Tab');
  await page.waitForTimeout(100);

  // Handle special symbols for interval2.value2
  if (interval2.value2 === '∞') {
    const infBtn = await page.locator('button[aria-label="Infinity"]');
    await infBtn.click({ force: true });
  } else {
    await page.keyboard.type(interval2.value2);
  }
  await page.waitForTimeout(200);
}
```

**Usage Example:**
```javascript
// Enter f(5/x) = (20 + 3x)/(25 + 2x)
await fillALEKSAnswer(page, 'e1503', 'fraction', {
  numerator: '20+3x',
  denominator: '25+2x'
});

// Enter g(x-3) = √(x² - 14x + 33)
// First, click Square root, then type with exponent handling:
await page.getByRole('button', { name: 'Square root' }).click();
await page.waitForTimeout(150);
await enterExponent(page, 'x', '2');
await page.keyboard.type('-14x+33');

// Enter domain with union: (-∞, -1) ∪ (-1, ∞)
await enterDomainWithUnion(page,
  { value1: '-∞', value2: '-1' },
  { value1: '-1', value2: '∞' },
  'Left paren comma right paren',
  'Left paren comma right paren'
);
```

### Key Cursor IDE MCP Limitations (Affects Linux, Windows, WSL)


1. **Playwright MCP Tools**: Server connects and reports tools, but Cursor IDE (v2.0.77+) fails to expose them to AI agents on Linux, Windows, and WSL. This is a Cursor IDE bug, not specific to Linux.
2. **Browser Path Detection**: Always fails on Linux - must use explicit `--executable-path` in MCP config.
3. **NVM/Node.js**: Requires bash wrapper to load NVM in MCP server processes (especially on Linux).
4. **Tool Naming**: May differ from Windows/macOS documentation.

**Workaround**: Use `mcp_browser_*` tools from `@agent-infra/mcp-server-browser` instead of Playwright MCP on Linux/WSL.

### For Lesson Plan Development (Graphing)
**IMPORTANT: Read before creating lesson plans with interactive graphs:**
- `layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/0_basic_prompts_throughout/lesson-plan-graphing-best-practices.md` (when created)
- **Key lesson learned**: Use simple public shareable Desmos graph URLs instead of state-encoded parameter URLs
  - State parameters are unreliable and format inconsistently across browsers
  - Public shareable URLs (`https://www.desmos.com/calculator/GRAPHID`) are stable and work consistently
  - For future lesson plans: Provide simple shareable graph links or guide students to create graphs themselves
  - See project context for detailed notes in `precalc/0_context/0_context/0_context/layer_1_project/1.02_sub_layers/lesson_plans/FUTURE_LESSON_PLAN_NOTES.md`

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
- [ ] **Familiarized with quick reference guide (Section 4.8)** - bookmark for later use
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
