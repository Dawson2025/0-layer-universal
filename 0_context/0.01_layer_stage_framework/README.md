# Layer + Stage Framework

This repository uses two orthogonal systems to manage AI context and workflows. Numbering is zero-padded (two digits after the decimal) for lexicographic stability (e.g., 1.01, 1.10, 1.12).

**This framework implements the [Ideal AI Manager Hierarchy System](../code/0_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md), the canonical Agent OS architecture for all AI work in this repository.**

- **Layer System (specificity)**: from universal -> project -> feature -> component -> sub-component (optional). Lower numbers are more universal and are prerequisites for higher numbers. Each layer uses the **layer grouping pattern**: entity internals live in `layer_N/` (containing `layer_N_00_ai_manager_system/`, `layer_N_01_manager_handoff_documents/`, `layer_N_02_sub_layers/`, `layer_N_99_stages/`), while nested content lives in `layer_N+1/` as a sibling folder.
  - **L0 (Universal)**: Global rules, tools, and standards that apply everywhere (e.g., TypeScript by default, security-first practices, testing expectations)
  - **L1 (Project)**: Project-specific constraints, architecture, and tech stack (e.g., e-commerce platform, ALEKS automation)
  - **L2 (Feature)**: Individual features within the project (e.g., auth-system, shopping-cart, reporting-dashboard)
  - **L3 (Component)**: Concrete implementation units (e.g., LoginForm, PaymentGateway, GradeCalculator)
  - **L4+ (Sub-component)**: Optional deeper splits for parallelism or complexity management (e.g., login/form-ui, login/validation, login/api-handler)

  Example universal 0.x band inside `layer_0/layer_0_02_sub_layers/`: 0.01 basic prompts, 0.02 SE knowledge, 0.03 principles, 0.04 rules, 0.05 OS setup, 0.06 coding app setup, 0.07 apps/browsers/extensions, 0.08 AI apps/tools, 0.09 MCP servers and tools setup, 0.10 AI models, 0.11 universal tools, 0.12 agent setup. Project (1.x), feature (2.x), and component (3.x) bands mirror the same pattern with their own numbering (e.g., 1.01-1.12).

- **Stage System (chronology)**: inside every layer, stages are located in `layer_N/layer_N_99_stages/` and are named `stage_L.xx_*` (e.g., universal uses stage_0.00-stage_0.08, project uses stage_1.00-stage_1.08, etc.) covering the complete chronological pipeline:
  1. **request** (stage_0.00_request_gathering) - Clarify what needs to be done
  2. **instructions** - Define explicit requirements and constraints
  3. **planning** - Break work into subtasks with dependencies
  4. **design** - Choose architectures, interfaces, and data flows
  5. **implementation** - Write code, modify modules, create configs
  6. **testing** - Verify functionality, run tests, collect results
  7. **criticism** - Review against standards and quality criteria
  8. **fixing** - Apply corrections, refactor, re-run tests
  9. **archiving** - Document and close completed work

  Each stage folder contains `hand_off_documents/` and `ai_agent_system/` subfolders for structured handoffs and agent configs.

## Layer Grouping Pattern

The framework uses a **layer grouping convention** where each entity has two sibling folders at its root:

```
layer_N_<type>_<name>/
├── layer_N/                              # This entity's internals
│   ├── layer_N_00_ai_manager_system/
│   ├── layer_N_01_manager_handoff_documents/
│   │   ├── layer_N_00_to_universal/
│   │   └── layer_N_01_to_specific/
│   ├── layer_N_02_sub_layers/
│   │   └── sub_layer_N.xx.../
│   └── layer_N_99_stages/
│       └── status_N.json
└── layer_N+1/                            # Nested content (siblings!)
    ├── layer_N+1_sub*X_projects/         # Always present for projects
    ├── layer_N+1_features/               # Always present for projects
    └── layer_N+1_components/             # Always present for projects
```

**Key Points:**
- `layer_N/` groups the entity's **own internals** (ai_manager, handoffs, sub_layers, stages)
- `layer_N+1/` groups **nested content** (sub-projects, features, components)
- These two folders are **SIBLINGS** at the entity root, not nested within each other
- Every project-type entity **always has all three folders** in `layer_N+1/`: sub*X_projects, features, components

## Purpose (how context management works)
- **Deterministic navigation**: Each layer has numbered slots in `layer_N/layer_N_02_sub_layers/` and stages in `layer_N/layer_N_99_stages/`. Agents address work as (Layer, Stage) to load only what's needed instead of fuzzy search.
- **Dependency clarity**: Higher layers depend on lower ones (e.g., models -> tools -> OS; features -> project architecture -> universal rules). The AI setup dependency chain is particularly important: 0.08 AI apps/tools -> 0.09 MCP servers -> 0.10 AI models -> 0.11 universal tools -> 0.12 agent setup.
- **Handoff & audit**: The manager system (`layer_N/layer_N_00_ai_manager_system/`) + handoff hub (`layer_N/layer_N_01_manager_handoff_documents/layer_N_00_to_universal/` and `layer_N_01_to_specific/`) + stage handoff folders allow clean up/downstream communication; stages and per-layer status files support handoffs, progress tracking, and archival for replay/debug. This is the spine of the context management system.

## AI Setup Dependency Chain (Universal Layer 0.08-0.11)

The universal layer includes a critical dependency chain for AI agent setup:

### 0.08 AI Apps/Tools Setup
- **Purpose**: Installation and configuration of AI applications and CLI tools (Cursor IDE, Claude Code, etc.)
- **Dependencies**: None (foundational)
- **Output**: Configured AI applications ready for MCP and model integration

### 0.09 MCP Servers and Tools Setup
- **Purpose**: Model Context Protocol (MCP) server setup and configuration
- **Dependencies**: **0.08** (MCP servers are configured within specific AI apps/tools)
- **Output**: Configured MCP servers providing capabilities (browser automation, documentation, search, etc.)
- **App-Specific**: MCP configuration is app-specific (e.g., `~/.cursor/mcp.json` for Cursor, `~/.claude/mcp.json` for Claude Code)

### 0.10 AI Models
- **Purpose**: Approved AI models and usage guidance
- **Dependencies**: **0.08** (models are accessed through AI apps/tools)
- **Output**: Model selection guidance and approved model list
- **Model Types**: Primary models, fallback models, model-specific capabilities

### 0.11 Universal Tools
- **Purpose**: Cross-project scripts, utilities, and universal tools
- **Dependencies**: **0.08** (tools may require AI apps), **0.09** (some tools may use MCP servers)
- **Output**: Universal tools available for agents to use
- **Key Features**:
  - **Browser Automation**: Tools for browser automation and testing
  - **Development Frameworks**: AI development frameworks and methodologies
  - **Platform Tools**: Version control, database integration, orchestration tools
  - **Cross-Cutting Utilities**: Scripts and utilities usable across all projects

### 0.12 Agent Setup
- **Purpose**: Agent configuration and setup for AI applications
- **Dependencies**: **0.08** (agents run within AI apps/tools), **0.09** (agents use MCP servers), **0.10** (agents require models), **0.11** (agents use universal tools)
- **Output**: Configured agents with model fallbacks, MCP integration, and tool access
- **Key Features**:
  - **Model Fallback Strategy**: Agents configured with primary models and ordered fallback models
  - **MCP Integration**: Agent instructions for using specific MCP servers and capabilities
  - **Tool Access**: Agents configured to use universal tools and project-specific tools
  - **App-Specific Configurations**: Agent setups tailored to specific AI applications
  - **Model-Specific Instructions**: Instructions that vary by model capabilities

### Dependency Flow
```
0.08 AI Apps/Tools Setup
    | (provides: AI application environment)
0.09 MCP Servers and Tools Setup
    | (provides: MCP capabilities)
0.10 AI Models
    | (provides: Model selection)
0.11 Universal Tools
    | (provides: Cross-cutting tools and utilities)
0.12 Agent Setup
    | (provides: Configured agents ready for work)
```

### Agent Configuration Example
An agent setup in 0.12 might specify:
- **Primary Model**: Claude Sonnet 4.5
- **Fallback Order**: Claude Sonnet 4.0 -> GPT-4 -> Claude Haiku
- **MCP Servers**: Browser automation (Playwright), Documentation (Context7)
- **Available Tools**: Universal tools from 0.11 (browser automation, development frameworks, etc.)
- **App Context**: Cursor IDE with specific workspace settings
- **Model-Specific Instructions**: Instructions that adapt based on which model is active

## Design Rationale

This Layer + Stage Framework is derived from the **Ideal AI Manager Hierarchy System**, which provides the complete architectural foundation for organizing AI work across abstraction layers and chronological stages.

**Core Architecture Documentation:**
- **Overview**: [`-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`](../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md) - Summary of the Agent OS concept
- **Architecture**: [`architecture.md`](../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md) - Deep dive on layers, stages, agents, handoffs, supervisors, and parallelism
- **Tools & Context**: [`tools_and_context_systems.md`](../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md) - How Claude Code, Codex CLI, Gemini CLI, and Cursor IDE work within the hierarchy
- **OS Variants**: [`os_and_quartets.md`](../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md) - OS-specific layouts and context file variants

**Key Architectural Principles:**
- **Layers cascade constraints**: Universal (L0) rules flow down through Project (L1), Feature (L2), and Component (L3+) layers
- **Stages form pipelines**: Work moves through request -> instructions -> planning -> design -> implementation -> testing -> criticism -> fixing -> archiving
- **Managers coordinate, workers execute**: Managers decompose tasks and spawn workers; workers perform bounded work and exit
- **Handoffs enable communication**: Structured JSON/Markdown documents pass state between layers and stages
- **Tools specialize by role**: Claude Code for managers/criticism, Codex CLI for atomic workers, Gemini CLI for research/planning, Cursor IDE for interactive work
- **OS-aware context**: Each layer/stage can include `os/<os-id>/` directories for OS-specific instructions

## Templates here
This folder contains templates to scaffold layers:
- `0_universal_template/`
- `1_project_template/`
- `2_feature_template/`
- `3_component_template/`

Each template includes:
- The `layer_N/` folder containing manager folders (`layer_N_00_ai_manager_system/`) plus handoff hub (`layer_N_01_manager_handoff_documents/layer_N_00_to_universal/` and `layer_N_01_to_specific/`).
- Numbered slots for that layer (e.g., project 1.01-1.12, feature 2.01-2.12, component 3.01-3.12) stored as `sub_layer_<slot>/` inside `layer_N/layer_N_02_sub_layers/`.
- A `layer_N/layer_N_99_stages/` folder with stage subfolders named `stage_L.xx_*` and a `status_template.json`. Every stage folder already contains `hand_off_documents/` and `ai_agent_system/` directories (with `.gitkeep`) so agents have a canonical drop-point.
- The `layer_N+1/` folder (for project templates) containing `layer_N+1_features/`, `layer_N+1_components/`, and `layer_N+1_sub_projects/`.

## How to instantiate for a real context
1) Copy the appropriate template to your context repo and rename (e.g., `layer_0_universal`, `layer_1_project`, `layer_2_feature_X`, `layer_3_component_Y`).
2) Populate the numbered slots in `layer_N/layer_N_02_sub_layers/` with your actual content. Use lower numbers for more foundational items. Legacy material can live in a `legacy_import/` subfolder while you reorganize.
3) File artifacts by Stage inside `layer_N/layer_N_99_stages/` and keep the per-layer `status*.json` updated.
4) The manager/worker agents navigate by Layer + Stage (e.g., `layer_2_feature_checkout/layer_2/layer_2_99_stages/stage_2.04_development/`) to load, work, and record status.
5) For inter-layer coordination, use the manager folders: drop upward reports in `layer_N/layer_N_01_manager_handoff_documents/layer_N_00_to_universal/` and downward/context packets in `layer_N/layer_N_01_manager_handoff_documents/layer_N_01_to_specific/`.

### Instantiating Workflow Features

When a Layer 2 Feature is a "Workflow Feature" (e.g., `layer_2_feature_2.17_2_workflow_feature_2_applied_programming_automation`), it requires a specific internal structure to manage the creation and execution of workflows.

**Required Internal Structure:**

1.  **`layer_2/layer_2_02_sub_layers/sub_layer_2.03_workflow_creation/`**:
    *   This folder contains the context, tools, and processes for creating *other* workflows.
    *   It **MUST** follow the standard Layer 2 Feature structure internally:
        *   `layer_2_00_ai_manager_system/`
        *   `layer_2_01_manager_handoff_documents/`
            *   `layer_2_00_to_universal/`
            *   `layer_2_01_to_specific/`
        *   `layer_2_02_sub_layers/` (for its own sub-layers)
        *   `layer_2_99_stages/` (for its own stages, following `stage_2.xx_*` naming)

2.  **`layer_2/layer_2_02_sub_layers/sub_layer_2.04_workflows/`**:
    *   This folder contains the actual instances of the workflows being managed by this feature.
    *   Each specific workflow instance within this folder (e.g., `workflow_1_applied_programming_module_completion`) **MUST** follow its own Layer 2 structure:
        *   `layer_2_02_sub_layers/` (for its own sub-layers)
        *   `layer_2_99_stages/` (for its own stages, following `stage_2.xx_*` naming)

3.  **`layer_2/layer_2_02_sub_layers/sub_layer_2.05_results/`**:
    *   This folder stores the aggregated results or outputs generated by the executed workflows.


## How the context file system works
- **Traversal:** A session loads from the outside in (layer_0 -> layer_1 -> layer_2 -> layer_3) and within each layer moves through the applicable stage folder. This keeps context scoped and deterministic.
- **Handoffs:** Every stage folder contains `hand_off_documents/` (for briefs, decisions, outputs) and `ai_agent_system/` (runbooks/configs for the stage owner agent). This is the canonical place for intra-agent transfers.
- **Status:** Each `status*.json` in `layer_N/layer_N_99_stages/` records the active stage and per-stage state so a manager agent can route work, unblock, or archive consistently.
- **Agent roles:** Each layer has a manager agent for that layer. The universal manager coordinates all project managers; each project manager coordinates all feature managers for that project; each feature manager coordinates all component managers for that feature. Within a layer, there is one stage agent per stage (instructions, planning, design, development, testing, criticism, fixing, archives), and each stage agent reports to that layer's manager. Upward reports go to `layer_N/layer_N_01_manager_handoff_documents/layer_N_00_to_universal/`; downstream/context packets go to `layer_N/layer_N_01_manager_handoff_documents/layer_N_01_to_specific/`.

## Agent system
- **Hierarchy:** Universal manager -> Project managers -> Feature managers -> Component managers. Each manager oversees all stage agents in its own layer and the manager agents of the immediately more specific layer.
- **Stage agents:** One per stage per layer (instructions, planning, design, development, testing, criticism, fixing, archives). They execute work for that layer/stage and report to their layer's manager.
- **Communication paths:** Upward reports/rollups: `layer_N/layer_N_01_manager_handoff_documents/layer_N_00_to_universal/` (to managers of broader layers). Downstream/context packets: `layer_N/layer_N_01_manager_handoff_documents/layer_N_01_to_specific/` (to managers of more specific layers). Stage-level handoffs live inside each `stage_<N.xx>_*` folder under `hand_off_documents/` and `ai_agent_system/`.
- **Routing:** Managers decide which stage agent to activate, collect results, and escalate or delegate via the handoff folders; status files in `layer_N/layer_N_99_stages/` keep `current_stage` and per-stage states in sync.

## How it works with sessions
- At session start, load the universal layer (`layer_0_universal`), then the relevant project (`layer_1_*`), feature (`layer_2_*`), and component (`layer_3_*`) layers as needed.
- Within each layer, operate in the current Stage (instructions/design/development/testing/criticism/fixing/archives) and update status on exit.

## Status tracking
- Each layer's `layer_N/layer_N_99_stages/status*.json` tracks `current_stage` and per-stage state (`not_started | in_progress | blocked | done`).
- This enables dashboards and automated routing for agents.

## Why this structure
- Mirrors hierarchical memory best practices: scoped layers + typed, chronological stages.
- Git-friendly, human-readable, deterministic; complements search/RAG rather than replacing it.
- Scales across universal/project/feature/component without changing the mental model.
- Layer grouping (`layer_N/` for internals, `layer_N+1/` for nested content) provides clear visual separation.
