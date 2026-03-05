---
resource_id: "160be65f-2171-4ac7-a729-9258b525e26f"
resource_type: "output"
resource_name: "00_overview"
---
# Context Propagation Through 0AGNOSTIC System

<!-- section_id: "a9fe7f3f-01f5-40f2-b85a-2670bfe43529" -->
## Overview

This documentation describes how unified context (0AGNOSTIC.md and .0agnostic/) flows through the system and gets adapted for different contexts.

<!-- section_id: "ba9ce24b-034e-44a6-a561-8b82bf702a40" -->
## Propagation Flow

```
01_core_system/           Source of truth — unified context
  ↓
02_setup_dependent/       Environment-specific adaptations
  ↓
03_context_avenue_web/    Context avenue-specific versions
  ↓
.1merge system            AI app-specific final versions
(documented separately)
```

<!-- section_id: "f7fa62e6-eb98-4fb4-a236-73529ed75be4" -->
## Four Layers of Context

<!-- section_id: "5277f11c-a715-4d57-845c-7d7627b4bbcc" -->
### 1. Core System (01_core_system/)
The canonical source of truth at every level. All context originates here:
- **01_knowledge/**: Domain knowledge, principles, documentation, resources
- **02_rules/**: Static (always-on) and dynamic (trigger-based) constraints
- **03_protocols/**: Step-by-step workflows and procedures
- **04_episodic_memory/**: Session history and accumulated learnings
- **05_handoff_documents/**: Communication across entities and stages

<!-- section_id: "0e8227da-73e0-43fd-aeeb-a96923ac9e38" -->
### 2. Setup-Dependent (02_setup_dependent/)
Environment and configuration-specific context organized hierarchically:
- **01_os/**: Operating system specifics (Linux, macOS, Windows)
- **02_environment/**: Shell environment, PATH, system settings
- **03_coding_apps/**: IDEs and code editors (Cursor, Antigravity, NeoVim, VS Code, etc.)
- **04_ai_apps/**: AI services and CLI tools (Claude Code CLI, Codex CLI, Gemini CLI, Cursor Agent CLI, etc.)
- **05_plugins/**: Extensions for coding apps and AI apps (VS Code extensions, Cursor extensions, Claude plugins, etc.)
- **06_mcp_servers/**: Model Context Protocol server configurations
- **07_tools_and_apis/**: External tools, utilities, APIs
- **08_other_setup_specifics/**: Additional setup context

<!-- section_id: "2f202f3b-81ac-4a39-954e-9ae4fdcee1ef" -->
### 3. Context Avenue Web (03_context_avenue_web/)
Ports core system content into context avenue-specific formats:

**File-Based Avenues (01_file_based/)**:
- 01_aalang/ — AALang JSON-LD agent definitions
- 02_aalang_markdown_integration/ — Markdown summaries of AALang files
- 03_auto_memory/ — Persistent memory files
- 04_@import_references/ — Curated reference collections
- 05_skills/ — SKILL.md files for specialized tasks
- 06_agents/ — Agent stubs and definitions
- 07_path_specific_rules/ — Directory-scoped rules
- 08_hooks/ — Event-triggered scripts

**Data-Based Avenues (02_data_based/)**:
- 09_knowledge_graph/ — Structural model with typed relationships
- 10_relational_index/ — Tabular metadata across entities
- 11_vector_embeddings/ — Semantic similarity fingerprints
- 12_temporal_index/ — Time-series of events and changes
- 13_shimi_structures/ — Per-node optimization primitives

<!-- section_id: "679c8080-680f-4a46-86c0-e9908f609a41" -->
### 4. AI App-Specific Versions
Final versions tailored for specific AI applications (Claude, Cursor, Gemini, Codex, Aider, Copilot).

Documented in: `.1merge/` system (parallel structure)

<!-- section_id: "8badd440-e5cd-4ae5-9c6c-0d3424978e12" -->
## Key Principle

The same unified context flows through all four layers, being adapted at each step:
- **Core System**: What's true across all contexts
- **Setup-Dependent**: What's specific to this environment
- **Context Avenue**: How to represent it in this avenue
- **AI App-Specific**: How to use it in this specific AI app

This prevents duplication and ensures consistency across all tools and contexts.
