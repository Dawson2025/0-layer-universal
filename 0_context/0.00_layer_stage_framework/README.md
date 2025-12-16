# Layer + Stage Framework

This repository uses two orthogonal systems to manage AI context and workflows. Numbering is zero-padded (two digits after the decimal) for lexicographic stability (e.g., 1.01, 1.10, 1.12).

- **Layer System (specificity)**: from universal → project → feature → component. Lower numbers are more universal and are prerequisites for higher numbers. Each layer starts with a manager system (`<N>.00_ai_manager_system/`), a manager handoff hub (`<N>.01_manager_handoff_documents/` with `<N>.00_to_universal/` and `<N>.01_to_specific/`), then its slots live inside `<N>.02_sub_layers/` with directories prefixed `sub_layer_`. Example universal 0.x band inside `0.02_sub_layers/`: 0.01 basic prompts, 0.02 SE knowledge, 0.03 principles, 0.04 rules, 0.05 OS setup, 0.06 coding app setup, 0.07 apps/browsers/extensions, 0.08 AI apps/tools, 0.09 MCP servers and tools setup, 0.10 AI models, 0.11 universal tools, 0.12 agent setup. Project (1.x), feature (2.x), and component (3.x) bands mirror the same pattern with their own numbering (e.g., 1.01–1.12).
- **Stage System (chronology)**: inside every layer, stages mirror the layer prefix and are named `stage_L.xx_*` (e.g., universal uses stage_0.01–stage_0.08, project uses stage_1.01–stage_1.08, etc.) covering: instructions, planning, design, development, testing, criticism, fixing, archives. Each stage folder contains `hand_off_documents/` and `ai_agent_system/` subfolders for structured handoffs and agent configs.

## Purpose (how context management works)
- **Deterministic navigation**: Each layer has numbered slots and a `*.99_stages` folder. Agents address work as (Layer, Stage) to load only what's needed instead of fuzzy search.
- **Dependency clarity**: Higher layers depend on lower ones (e.g., models → tools → OS; features → project architecture → universal rules). The AI setup dependency chain is particularly important: 0.08 AI apps/tools → 0.09 MCP servers → 0.10 AI models → 0.11 universal tools → 0.12 agent setup.
- **Handoff & audit**: The manager system (`<N>.00_ai_manager_system/`) + handoff hub (`<N>.01_manager_handoff_documents/<N>.00_to_universal|<N>.01_to_specific/`) + stage handoff folders allow clean up/downstream communication; stages and per-layer status files support handoffs, progress tracking, and archival for replay/debug. This is the spine of the context management system.

## AI Setup Dependency Chain (Universal Layer 0.08–0.11)

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
    ↓ (provides: AI application environment)
0.09 MCP Servers and Tools Setup
    ↓ (provides: MCP capabilities)
0.10 AI Models
    ↓ (provides: Model selection)
0.11 Universal Tools
    ↓ (provides: Cross-cutting tools and utilities)
0.12 Agent Setup
    ↓ (provides: Configured agents ready for work)
```

### Agent Configuration Example
An agent setup in 0.12 might specify:
- **Primary Model**: Claude Sonnet 4.5
- **Fallback Order**: Claude Sonnet 4.0 → GPT-4 → Claude Haiku
- **MCP Servers**: Browser automation (Playwright), Documentation (Context7)
- **Available Tools**: Universal tools from 0.11 (browser automation, development frameworks, etc.)
- **App Context**: Cursor IDE with specific workspace settings
- **Model-Specific Instructions**: Instructions that adapt based on which model is active

## Templates here
This folder contains templates to scaffold layers:
- `0_universal_template/`
- `1_project_template/`
- `2_feature_template/`
- `3_component_template/`

Each template includes:
- Manager folders (`<N>.00_ai_manager_system/`) plus handoff hub (`<N>.01_manager_handoff_documents/<N>.00_to_universal/` and `<N>.01_to_specific/`).
- Numbered slots for that layer (e.g., project 1.01–1.12, feature 2.01–2.12, component 3.01–3.12) stored as `sub_layer_<slot>/` inside `*.02_sub_layers/`.
- A `*.99_stages/` folder with stage subfolders named `stage_L.xx_*` and a `status_template.json`. Every stage folder already contains `hand_off_documents/` and `ai_agent_system/` directories (with `.gitkeep`) so agents have a canonical drop-point.
- The template itself already includes the `*.02_sub_layers/` directory and the stage folders to mirror the live layout.

## How to instantiate for a real context
1) Copy the appropriate template to your context repo and rename (e.g., `layer_0_universal`, `layer_1_project`, `layer_2_feature_X`, `layer_3_component_Y`).
2) Populate the numbered slots with your actual content. Use lower numbers for more foundational items. Legacy material can live in a `legacy_import/` subfolder while you reorganize.
3) File artifacts by Stage inside `*.99_stages/` and keep the per-layer `status*.json` updated.
4) The manager/worker agents navigate by Layer + Stage (e.g., `layer_2_feature_checkout` + `stage_2.04_development`) to load, work, and record status.
5) For inter-layer coordination, use the manager folders: drop upward reports in `<N>.01_manager_handoff_documents/<N>.00_to_universal/` and downward/context packets in `<N>.01_manager_handoff_documents/<N>.01_to_specific/`.

### Instantiating Workflow Features

When a Layer 2 Feature is a "Workflow Feature" (e.g., `layer_2_feature_2.17_2_workflow_feature_2_applied_programming_automation`), it requires a specific internal structure to manage the creation and execution of workflows.

**Required Internal Structure:**

1.  **`2.03_workflow_creation/`**:
    *   This folder contains the context, tools, and processes for creating *other* workflows.
    *   It **MUST** follow the standard Layer 2 Feature structure internally:
        *   `2.00_ai_manager_system/`
        *   `2.01_manager_handoff_documents/`
            *   `2.00_to_universal/`
            *   `2.01_to_specific/`
        *   `2.02_sub_layers/` (for its own sub-layers)
        *   `2.99_stages/` (for its own stages, following `stage_2.xx_*` naming)

2.  **`2.04_workflows/`**:
    *   This folder contains the actual instances of the workflows being managed by this feature.
    *   Each specific workflow instance within this folder (e.g., `workflow_1_applied_programming_module_completion`) **MUST** follow its own Layer 2 structure:
        *   `2.02_sub_layers/` (for its own sub-layers)
        *   `2.99_stages/` (for its own stages, following `stage_2.xx_*` naming)

3.  **`2.05_results/`**:
    *   This folder stores the aggregated results or outputs generated by the executed workflows.


## How the context file system works
- **Traversal:** A session loads from the outside in (layer_0 → layer_1 → layer_2 → layer_3) and within each layer moves through the applicable stage folder. This keeps context scoped and deterministic.
- **Handoffs:** Every stage folder contains `hand_off_documents/` (for briefs, decisions, outputs) and `ai_agent_system/` (runbooks/configs for the stage owner agent). This is the canonical place for intra-agent transfers.
- **Status:** Each `status*.json` records the active stage and per-stage state so a manager agent can route work, unblock, or archive consistently.
- **Agent roles:** Each layer has a manager agent for that layer. The universal manager coordinates all project managers; each project manager coordinates all feature managers for that project; each feature manager coordinates all component managers for that feature. Within a layer, there is one stage agent per stage (instructions, planning, design, development, testing, criticism, fixing, archives), and each stage agent reports to that layer’s manager. Upward reports go to `<N>.01_manager_handoff_documents/<N>.00_to_universal/`; downstream/context packets go to `<N>.01_manager_handoff_documents/<N>.01_to_specific/`.

## Agent system
- **Hierarchy:** Universal manager → Project managers → Feature managers → Component managers. Each manager oversees all stage agents in its own layer and the manager agents of the immediately more specific layer.
- **Stage agents:** One per stage per layer (instructions, planning, design, development, testing, criticism, fixing, archives). They execute work for that layer/stage and report to their layer’s manager.
- **Communication paths:** Upward reports/rollups: `<N>.01_manager_handoff_documents/<N>.00_to_universal/` (to managers of broader layers). Downstream/context packets: `<N>.01_manager_handoff_documents/<N>.01_to_specific/` (to managers of more specific layers). Stage-level handoffs live inside each `stage_<N.xx>_*` folder under `hand_off_documents/` and `ai_agent_system/`.
- **Routing:** Managers decide which stage agent to activate, collect results, and escalate or delegate via the handoff folders; status files in `*.99_stages/` keep `current_stage` and per-stage states in sync.

## How it works with sessions
- At session start, load the universal layer (`layer_0_universal`), then the relevant project (`layer_1_*`), feature (`layer_2_*`), and component (`layer_3_*`) layers as needed.
- Within each layer, operate in the current Stage (instructions/design/development/testing/criticism/fixing/archives) and update status on exit.

## Status tracking
- Each layer’s `*.99_stages/status*.json` tracks `current_stage` and per-stage state (`not_started | in_progress | blocked | done`).
- This enables dashboards and automated routing for agents.

## Why this structure
- Mirrors hierarchical memory best practices: scoped layers + typed, chronological stages.
- Git-friendly, human-readable, deterministic; complements search/RAG rather than replacing it.
- Scales across universal/project/feature/component without changing the mental model.
