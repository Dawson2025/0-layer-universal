---
resource_id: "160be65f-2171-4ac7-a729-9258b525e26f"
resource_type: "output"
resource_name: "00_overview"
---
# Context Propagation Through 0AGNOSTIC System

## Overview

This documentation describes how unified context (0AGNOSTIC.md and .0agnostic/) flows through the system and gets adapted for different contexts.

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

## Four Layers of Context

### 1. Core System (01_core_system/)
The canonical source of truth at every level. All context originates here:
- **01_knowledge/**: Domain knowledge, principles, documentation, resources
- **02_rules/**: Static (always-on) and dynamic (trigger-based) constraints
- **03_protocols/**: Step-by-step workflows and procedures
- **04_episodic_memory/**: Session history and accumulated learnings
- **05_handoff_documents/**: Communication across entities and stages

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

### 4. AI App-Specific Versions
Final versions tailored for specific AI applications (Claude, Cursor, Gemini, Codex, Aider, Copilot).

Documented in: `.1merge/` system (parallel structure)

## Key Principle

The same unified context flows through all four layers, being adapted at each step:
- **Core System**: What's true across all contexts
- **Setup-Dependent**: What's specific to this environment
- **Context Avenue**: How to represent it in this avenue
- **AI App-Specific**: How to use it in this specific AI app

This prevents duplication and ensures consistency across all tools and contexts.
