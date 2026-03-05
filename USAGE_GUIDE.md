---
resource_id: "39c35059-9c1a-4d30-9ff4-f0991dfe8fc0"
resource_type: "document"
resource_name: "USAGE_GUIDE"
---
# Universal AI Context System - Usage Guide

This directory now follows the Layer + Stage framework (layers: universal/project/feature/component; stages: request_gathering → research → instructions → planning → design → development → testing → criticism → fixing → current_product → archives). Each layer has `layer_<N>_01_ai_manager_system/`, `layer_<N>_02_manager_handoff_documents/layer_<N>_00_to_universal|layer_<N>_01_to_specific/`, sub-layers under `layer_<N>_0X_sub_layers/sub_layer_<N>_XX_*`, and stages under `layer_<N>_99_stages/stage_<N>_XX_*` (each with `hand_off_documents/` and `ai_agent_system/`). Legacy `trickle_down_*` references remain below for historical context; prefer the layer paths for new work.

<!-- section_id: "de9cb5e1-07c2-4e3b-854b-fc19d546b29f" -->
## 🎯 Quick Start

1. **Copy the `0_layer_universal/` directory** to your project root (or desired location) if you need to vendor the framework
2. **Update the core prompt file**: Edit `0_basic_prompts_throughout/what_to_do_next.md`
3. **Add project-specific documentation** as needed
4. **Update file paths** to match your project structure

<!-- section_id: "1e6c22f2-6419-4ac0-a15a-3cbc83d9fdbd" -->
## 🏗️ Working with the AI Manager Hierarchy

This system implements the **AI Manager Hierarchy System** - an Agent OS architecture for coordinating AI work across layers and stages.

<!-- section_id: "9c9e05b9-c48d-439c-bb78-a4437b0067df" -->
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
2. **research** - Gather context and explore options
3. **instructions** - Define explicit requirements and constraints
4. **planning** - Break work into subtasks
5. **design** - Choose architectures and interfaces
6. **development** - Write code
7. **testing** - Verify functionality
8. **criticism** - Review against standards
9. **fixing** - Apply corrections
10. **current_product** - Ship the deliverable
11. **archives** - Document and close

**Handoffs (Communication):**
- Stages and layers communicate via **handoff documents** (JSON/Markdown)
- Each handoff contains: task, constraints, artifacts, subtasks, results, status
- Location: `hand_off_documents/incoming.json` and `outgoing.json` in each stage

<!-- section_id: "374c2655-b57a-42a0-a58d-7f4fdd01d780" -->
### Which Docs to Read First

**For AI Agents Starting Work:**
1. **Start**: `layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/universal_init_prompt.md` - Core initialization
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

<!-- section_id: "124bbcf9-2a94-4b94-b0a7-b054aeb4a2d2" -->
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

<!-- section_id: "3be08f40-e1dd-457f-a4e8-dbbb4d77ecd0" -->
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
See `layer_0/layer_0_02_manager_handoff_documents/layer_0_00_to_universal/handoff_schema.md`

<!-- section_id: "f0da42f2-5d27-441c-bd04-113bc2d58d2b" -->
### Tool Selection by Layer/Stage

- **L0-L2 Managers**: Claude Code (deep reasoning, cascading CLAUDE.md)
- **L3-L4 Workers**: Codex CLI (fast, atomic tasks, short sessions)
- **Request/Instructions**: Gemini CLI (long dialogues, research-heavy)
- **Criticism**: Claude Code (multi-file review, complex reasoning)
- **Interactive debugging**: Cursor IDE (human-in-the-loop)

<!-- section_id: "92a126b0-ebf9-42d2-8661-1fa946324b11" -->
### More Information

- **Complete Hierarchy Docs**: [`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/`](-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/)
- **Master Index**: [MASTER_DOCUMENTATION_INDEX.md](MASTER_DOCUMENTATION_INDEX.md#-canonical-agent-os-architecture---ai-manager-hierarchy-system)

<!-- section_id: "8e5e0cd3-fa01-4164-a0b2-5f3f7453415a" -->
## 📋 Step-by-Step Setup

<!-- section_id: "18f9c29b-2e4a-4633-b614-35add87c2d82" -->
### Step 1: Copy to Your Project

```bash
# From the location where 0_context currently exists
cp -r /path/to/0_layer_universal/0_context /path/to/your/project/docs/

# Or if you want it in your project root:
cp -r /path/to/0_layer_universal/0_context /path/to/your/project/
```

<!-- section_id: "7a7b3207-9444-48fc-a25d-ae056492f603" -->
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

<!-- section_id: "f1948c30-85e9-469e-b19a-fa3cffbaabaa" -->
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

<!-- section_id: "8602c137-c7a0-4a52-a2da-6b8519c5775a" -->
### Step 4: Update References

Search for and update these common patterns:

1. **Project paths**: Search for `/home/dawson/code/` and replace with your paths
2. **Project names**: Update any hardcoded project names
3. **Technology references**: Update technology stack references if different

<!-- section_id: "74c4b007-62d7-4d8f-81ca-0e005c021475" -->
## 📁 Directory Structure Overview

<!-- section_id: "ef2409d7-e09c-4608-a395-44c9e214654a" -->
### Universal Directories (Keep As-Is)
- `trickle_down_0_universal/`: Universal AI agent instructions
- `trickle_down_0.5_setup/`: Setup and configuration (customize as needed)
- `trickle_down_0.75_universal_tools/`: Universal tools documentation

<!-- section_id: "12acf433-9b2b-4bbb-9061-2b77b2a88628" -->
### Project-Specific Directories (Customize)
- `trickle_down_1_project/`: Your project's specific documentation
- `trickle_down_1.5_project_tools/`: Your project's tools
- `trickle_down_2_features/`: Your project's features
- `trickle_down_2_implementation/`: Implementation documentation
- `trickle_down_3_components/`: Component documentation
- `trickle_down_3_testing/`: Testing documentation

<!-- section_id: "05b453ab-4efe-4390-9d46-156d4e613145" -->
## 🎨 Customization Examples

<!-- section_id: "62262e4f-d53b-4c47-800d-12a3a20fc3d2" -->
### Example 1: React/Node.js Project

```markdown
### Technology Stack
- **Frontend**: React 18 + TypeScript + Vite
- **Backend**: Node.js + Express
- **Database**: PostgreSQL + Prisma ORM
- **Deployment**: Vercel (frontend), Railway (backend)
```

<!-- section_id: "fa562675-63d2-4055-8864-f484b5ae5998" -->
### Example 2: Python Django Project

```markdown
### Technology Stack
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: React (or template rendering)
- **Deployment**: Docker + AWS/GCP
```

<!-- section_id: "74833ac4-01c5-47a1-bc5d-0d55cc473e8c" -->
### Example 3: Mobile App Project

```markdown
### Technology Stack
- **Mobile**: React Native or Flutter
- **Backend**: Node.js or Python
- **Database**: Supabase or Firebase
- **Deployment**: App Store + Google Play
```

<!-- section_id: "ef98ec2c-1d0e-4047-be6c-6114ec2a2651" -->
## 📝 Documentation Organization

<!-- section_id: "2e5eae39-751f-4ec0-9c14-aa8d37545c5f" -->
### Follow the Trickle-Down Pattern

1. **0_instruction_docs/**: How-to guides, procedures, specifications
2. **1_status_progress_docs/**: Current status, progress reports
3. **2_archive_docs/**: Completed work, resolutions, historical records
4. **2_testing_docs/**: Testing documentation, test results

<!-- section_id: "65d5656c-6588-40cc-a09f-3b21ff9cb5de" -->
### Naming Conventions

Use this pattern for dated documentation:
- `YYYY-MM-DD_description.md` for daily documentation
- `DESCRIPTION_DATE.md` for major milestones
- `CATEGORY_description.md` for category-specific docs

<!-- section_id: "6fd51be9-a408-4d02-be60-0969b6b18e0d" -->
## ⚙️ Important Files to Know

<!-- section_id: "51b49145-03fa-44ce-8e4a-41dfb5c4fca5" -->
### Critical Files (Update These First)

1. **`0_basic_prompts_throughout/what_to_do_next.md`**
   - Primary instruction file for AI agents
   - Must be updated with your project details

2. **`README.md`**
   - Already universalized, customize as needed

3. **`MASTER_DOCUMENTATION_INDEX.md`**
   - Comprehensive index of all documentation
   - Update when adding new documentation

<!-- section_id: "ba6670b1-60cd-477f-90a1-e3b36ffc57ea" -->
### Reference Files (Review and Adapt)

1. **`TERMINAL_HANGING_FIX.md`**
   - Terminal execution protocol
   - Use as-is (universal)

2. **`trickle_down_0_universal/0_instruction_docs/cursor_terminal_issues.md`**
   - Cursor IDE terminal issues
   - Universal reference

<!-- section_id: "a254a21e-4da0-4faf-8e53-f180f726f316" -->
## 🚀 Using with AI Agents

<!-- section_id: "80e703ef-54c1-4bcb-a527-edb177ae7178" -->
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

<!-- section_id: "bcc25715-2fb5-4b2c-96a3-0d7dff14c035" -->
### For Multiple AI Agents:

This system is designed to work with:
- **Claude** (Anthropic)
- **ChatGPT** (OpenAI)
- **Cursor AI**
- **GitHub Copilot**
- Other MCP-compatible agents

<!-- section_id: "213e32db-c771-4c1b-9230-b65ddd4f15d0" -->
## 🔧 Advanced Customization

<!-- section_id: "71407611-3ecb-42b0-910f-e979bb2a09cd" -->
### Adding New Trickle-Down Levels

If you need additional organization levels:

1. Create new directory: `trickle_down_X_NAME/`
2. Mirror the standard structure:
   - `0_instruction_docs/`
   - `1_status_progress_docs/`
   - `2_archive_docs/`
3. Update `MASTER_DOCUMENTATION_INDEX.md`

<!-- section_id: "1c5d39c0-679a-43bf-8463-84080006f6d8" -->
### Creating Project-Specific Tools

Document custom tools in:
- `trickle_down_1.5_project_tools/0_instruction_docs/`

Include:
- Tool descriptions
- Usage examples
- Configuration guides
- Troubleshooting

<!-- section_id: "582f09c4-2eac-49dd-9531-b2e9aff44f2a" -->
## 📚 Best Practices

1. **Always update `what_to_do_next.md`** for each project
2. **Keep universal content** in `trickle_down_0_*` directories
3. **Archive old work** in `2_archive_docs/` or `3_archive_docs/`
4. **Document testing** in `2_testing_docs/` or `trickle_down_3_testing/`
5. **Maintain the index** in `MASTER_DOCUMENTATION_INDEX.md`

<!-- section_id: "8cbfcd06-bca8-4b63-84d2-88c894cc614e" -->
## ⚠️ Common Pitfalls

1. **Don't hardcode project paths** - Use relative paths or environment variables
2. **Don't delete universal documentation** - Keep trickle_down_0_* for reusability
3. **Don't skip the customization step** - Generic docs won't help without customization
4. **Don't ignore the master index** - Keep it updated as you add documentation

<!-- section_id: "27f62024-9d48-4eb3-b769-cf29aa59378d" -->
## 🎯 Next Steps

1. ✅ Copy `0_context` to your project
2. ✅ Update `0_basic_prompts_throughout/what_to_do_next.md`
3. ✅ Create project constitution in `trickle_down_1_project/0_instruction_docs/constitution.md`
4. ✅ Document your stack in `README.md`
5. ✅ Start documenting features in `trickle_down_2_features/`

---

**Need Help?** Review existing documentation in the trickle_down directories for examples and best practices.
