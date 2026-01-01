# Universal AI Context System - Usage Guide

This directory now follows the Layer + Stage framework (layers: universal/project/feature/component; stages: instructions → planning → design → development → testing → criticism → fixing → archives). Each layer has `<N>.00_ai_manager_system/`, `<N>.01_manager_handoff_documents/<N>.00_to_universal|<N>.01_to_specific/`, slots under `layer_<N>_*/*02_sub_layers/sub_layer_<N.xx>_*`, and stages under `*.99_stages/stage_<N.xx>_*` (each with `hand_off_documents/` and `ai_agent_system/`). Legacy `trickle_down_*` references remain below for historical context; prefer the layer paths for new work.

## 🎯 Quick Start

1. **Copy the entire `0_context` directory** to your project root (or desired location)
2. **Update the core prompt file**: Edit `0_basic_prompts_throughout/what_to_do_next.md`
3. **Add project-specific documentation** as needed
4. **Update file paths** to match your project structure

## 🏗️ Working with the AI Manager Hierarchy

This system implements the **AI Manager Hierarchy System** - an Agent OS architecture for coordinating AI work across layers and stages.

### Understanding the Hierarchy

**Layers (Abstraction Levels):**
- **L0 (Universal)**: Global rules, tools, and standards that apply everywhere
- **L1 (Project)**: Project-specific constraints, architecture, and tech stack
- **L2 (Feature)**: Individual features within the project (auth, payments, reporting)
- **L3 (Component)**: Concrete implementation units (LoginForm, PaymentGateway)
- **L4+ (Sub-component)**: Optional deeper splits for parallelism

**Stages (Chronological Pipeline):**
Each layer moves work through stages:
1. **request** - Clarify what needs to be done
2. **instructions** - Define explicit requirements and constraints
3. **planning** - Break work into subtasks
4. **design** - Choose architectures and interfaces
5. **implementation** - Write code
6. **testing** - Verify functionality
7. **criticism** - Review against standards
8. **fixing** - Apply corrections
9. **archiving** - Document and close

**Handoffs (Communication):**
- Stages and layers communicate via **handoff documents** (JSON/Markdown)
- Each handoff contains: task, constraints, artifacts, subtasks, results, status
- Location: `hand_off_documents/incoming.json` and `outgoing.json` in each stage

### Which Docs to Read First

**For AI Agents Starting Work:**
1. **Start**: `layer_0_universal/.../universal_init_prompt.md` - Core initialization
2. **Overview**: `SYSTEM_OVERVIEW.md` - Understand layer + stage structure
3. **Hierarchy**: [`-1_research/.../overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`](-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md) - Agent OS architecture
4. **Layer Context**: Load appropriate L0 → L1 → L2 → L3 context for your task
5. **Stage Handoff**: Read `hand_off_documents/incoming.json` in your current stage

**For Specific Tasks:**
- **Manager role** (coordinating work): Read `supervisor_patterns.md` and `framework_orchestration.md`
- **Worker role** (executing tasks): Read `cli_recursion_syntax.md` and stage-specific `ai_agent_system/`
- **Tool selection**: Read `model_selection_strategy.md` and `tools_and_context_systems.md`
- **Parallel work**: Read `parallel_execution.md`
- **Production deployment**: Read `production_deployment.md`, `observability_and_logging.md`, `safety_and_governance.md`

### Which Layers/Stages to Touch

**When to work at each layer:**
- **L0**: Only when changing universal rules that affect ALL projects
- **L1**: When adding/modifying project-wide constraints, architecture, or standards
- **L2**: When implementing new features or modifying feature-level logic
- **L3**: Most common - implementing specific components or fixing bugs
- **L4+**: When parallelizing component work or managing sub-components

**Stage transitions:**
- Start in `request` or `instructions` for new work
- Jump to `implementation` if requirements are clear
- Always pass through `testing` and `criticism` before completing
- End in `archiving` to document completed work

### Handoff Documents

**Structure:**
```json
{
  "schemaVersion": "1.0.0",
  "id": "handoff-l2-auth-impl",
  "layer": 2,
  "stage": "implementation",
  "from": "layer_2/auth/planning",
  "to": "layer_2/auth/implementation",
  "task": "Implement login component",
  "constraints": ["TypeScript", "React", "Accessibility"],
  "artifacts": {
    "files": ["src/components/LoginForm.tsx"]
  },
  "status": "pending"
}
```

**Location:**
- Read: `<layer>/<stage>/hand_off_documents/incoming.json`
- Write: `<layer>/<stage>/hand_off_documents/outgoing.json`

**For detailed handoff specification:**
See `layer_0_universal/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md` (to be created)

### Tool Selection by Layer/Stage

- **L0-L2 Managers**: Claude Code (deep reasoning, cascading CLAUDE.md)
- **L3-L4 Workers**: Codex CLI (fast, atomic tasks, short sessions)
- **Request/Instructions**: Gemini CLI (long dialogues, research-heavy)
- **Criticism**: Claude Code (multi-file review, complex reasoning)
- **Interactive debugging**: Cursor IDE (human-in-the-loop)

### More Information

- **Complete Hierarchy Docs**: [`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/`](-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/)
- **Master Index**: [MASTER_DOCUMENTATION_INDEX.md](MASTER_DOCUMENTATION_INDEX.md#-canonical-agent-os-architecture---ai-manager-hierarchy-system)

## 📋 Step-by-Step Setup

### Step 1: Copy to Your Project

```bash
# From the location where 0_context currently exists
cp -r /path/to/0_ai_context/0_context /path/to/your/project/docs/

# Or if you want it in your project root:
cp -r /path/to/0_ai_context/0_context /path/to/your/project/
```

### Step 2: Customize Core Prompt

Edit `0_basic_prompts_throughout/what_to_do_next.md`:

1. **Update the project path**:
   - Replace `/PATH/TO/YOUR/PROJECT/0_context` with your actual path
   
2. **Update project overview**:
   - Replace "Your Project Name" with your actual project name
   - Describe what your project does
   - List key features
   
3. **Define technology stack**:
   - List your frontend technology
   - List your backend technology
   - Specify your database solution
   - Mention deployment platform
   
4. **Set current priorities**:
   - Define high priority tasks
   - Define medium priority tasks
   - Define low priority tasks
   
5. **Update project status**:
   - Describe current development stage
   - List technology stack
   - Specify target platform
   - Mention next milestone

### Step 3: Add Project-Specific Documentation

Create or update files in these directories as needed:

#### `trickle_down_1_project/0_instruction_docs/`
- **constitution.md**: Project-specific coding standards, guidelines, and best practices
- **ENVIRONMENTS_AND_INTEGRATIONS.md**: Environment setup, integrations, and configurations
- **README.md**: Project-specific overview and quick start guide

#### `trickle_down_1.5_project_tools/0_instruction_docs/`
- Add project-specific tools and scripts documentation
- Document custom configurations
- Add integration guides

#### `trickle_down_2_features/0_instruction_docs/`
- Document feature specifications
- Add feature implementation guides
- Create feature testing documentation

#### `trickle_down_3_components/0_instruction_docs/`
- Document component specifications
- Add implementation guides
- Create component documentation

### Step 4: Update References

Search for and update these common patterns:

1. **Project paths**: Search for `/home/dawson/dawson-workspace/code/` and replace with your paths
2. **Project names**: Update any hardcoded project names
3. **Technology references**: Update technology stack references if different

## 📁 Directory Structure Overview

### Universal Directories (Keep As-Is)
- `trickle_down_0_universal/`: Universal AI agent instructions
- `trickle_down_0.5_setup/`: Setup and configuration (customize as needed)
- `trickle_down_0.75_universal_tools/`: Universal tools documentation

### Project-Specific Directories (Customize)
- `trickle_down_1_project/`: Your project's specific documentation
- `trickle_down_1.5_project_tools/`: Your project's tools
- `trickle_down_2_features/`: Your project's features
- `trickle_down_2_implementation/`: Implementation documentation
- `trickle_down_3_components/`: Component documentation
- `trickle_down_3_testing/`: Testing documentation

## 🎨 Customization Examples

### Example 1: React/Node.js Project

```markdown
### Technology Stack
- **Frontend**: React 18 + TypeScript + Vite
- **Backend**: Node.js + Express
- **Database**: PostgreSQL + Prisma ORM
- **Deployment**: Vercel (frontend), Railway (backend)
```

### Example 2: Python Django Project

```markdown
### Technology Stack
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: React (or template rendering)
- **Deployment**: Docker + AWS/GCP
```

### Example 3: Mobile App Project

```markdown
### Technology Stack
- **Mobile**: React Native or Flutter
- **Backend**: Node.js or Python
- **Database**: Supabase or Firebase
- **Deployment**: App Store + Google Play
```

## 📝 Documentation Organization

### Follow the Trickle-Down Pattern

1. **0_instruction_docs/**: How-to guides, procedures, specifications
2. **1_status_progress_docs/**: Current status, progress reports
3. **2_archive_docs/**: Completed work, resolutions, historical records
4. **2_testing_docs/**: Testing documentation, test results

### Naming Conventions

Use this pattern for dated documentation:
- `YYYY-MM-DD_description.md` for daily documentation
- `DESCRIPTION_DATE.md` for major milestones
- `CATEGORY_description.md` for category-specific docs

## ⚙️ Important Files to Know

### Critical Files (Update These First)

1. **`0_basic_prompts_throughout/what_to_do_next.md`**
   - Primary instruction file for AI agents
   - Must be updated with your project details

2. **`README.md`**
   - Already universalized, customize as needed

3. **`MASTER_DOCUMENTATION_INDEX.md`**
   - Comprehensive index of all documentation
   - Update when adding new documentation

### Reference Files (Review and Adapt)

1. **`TERMINAL_HANGING_FIX.md`**
   - Terminal execution protocol
   - Use as-is (universal)

2. **`trickle_down_0_universal/0_instruction_docs/cursor_terminal_issues.md`**
   - Cursor IDE terminal issues
   - Universal reference

## 🚀 Using with AI Agents

### For Claude/ChatGPT/Cursor AI:

Point the AI to this directory:
```
/path/to/your/project/docs/0_context
```

The AI will:
1. Read the `what_to_do_next.md` file first
2. Follow the trickle-down documentation structure
3. Use universal instructions when appropriate
4. Apply project-specific documentation when available

### For Multiple AI Agents:

This system is designed to work with:
- **Claude** (Anthropic)
- **ChatGPT** (OpenAI)
- **Cursor AI**
- **GitHub Copilot**
- Other MCP-compatible agents

## 🔧 Advanced Customization

### Adding New Trickle-Down Levels

If you need additional organization levels:

1. Create new directory: `trickle_down_X_NAME/`
2. Mirror the standard structure:
   - `0_instruction_docs/`
   - `1_status_progress_docs/`
   - `2_archive_docs/`
3. Update `MASTER_DOCUMENTATION_INDEX.md`

### Creating Project-Specific Tools

Document custom tools in:
- `trickle_down_1.5_project_tools/0_instruction_docs/`

Include:
- Tool descriptions
- Usage examples
- Configuration guides
- Troubleshooting

## 📚 Best Practices

1. **Always update `what_to_do_next.md`** for each project
2. **Keep universal content** in `trickle_down_0_*` directories
3. **Archive old work** in `2_archive_docs/` or `3_archive_docs/`
4. **Document testing** in `2_testing_docs/` or `trickle_down_3_testing/`
5. **Maintain the index** in `MASTER_DOCUMENTATION_INDEX.md`

## ⚠️ Common Pitfalls

1. **Don't hardcode project paths** - Use relative paths or environment variables
2. **Don't delete universal documentation** - Keep trickle_down_0_* for reusability
3. **Don't skip the customization step** - Generic docs won't help without customization
4. **Don't ignore the master index** - Keep it updated as you add documentation

## 🎯 Next Steps

1. ✅ Copy `0_context` to your project
2. ✅ Update `0_basic_prompts_throughout/what_to_do_next.md`
3. ✅ Create project constitution in `trickle_down_1_project/0_instruction_docs/constitution.md`
4. ✅ Document your stack in `README.md`
5. ✅ Start documenting features in `trickle_down_2_features/`

---

**Need Help?** Review existing documentation in the trickle_down directories for examples and best practices.
