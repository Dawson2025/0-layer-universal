---
resource_id: "b3342c75-129d-4f81-a16c-c5765b107bc5"
resource_type: "readme
knowledge"
resource_name: "README"
---
# sub_layer_2.05-2.14_setup - Sub-Project Setup Sublayer

**Sublayer Range**: 2.05 through 2.14
**Purpose**: Consolidated setup documentation covering all setup dimensions for this sub-project

---

## Overview

This sublayer consolidates all setup documentation for sublayers 2.05 through 2.14:

- **2.05** - Operating System Setup
- **2.06** - Environment Setup
- **2.07** - Coding App Setup
- **2.08** - Apps/Browsers/Extensions Setup
- **2.09** - AI Apps/Tools Setup
- **2.10** - MCP Servers and Tools Setup
- **2.11** - AI Models
- **2.12** - Sub-Project Tools
- **2.13** - Sub-Project Protocols
- **2.14** - Agent Setup

All setup documentation is organized in a single **hierarchical file tree structure**.

---

## Primary Navigation: Sub-Project Setup File Tree

**Main entry point**: `2.01_sub_project_setup_file_tree/`

This file tree provides hierarchical navigation across all 10 setup dimensions:

```
OS → Environment → Coding App → Apps/Browsers → AI App → MCP Server → AI Model → Tools → Protocols → Agent Setup
```

### Quick Start

```bash
# Navigate to the file tree
cd 2.01_sub_project_setup_file_tree/

# Navigate to your specific setup
cd 2.05_operating_systems/<your_os>/
cd 2.06_environments/<your_env>/
cd 2.07_coding_apps/<your_app>/
# Continue navigating down...
```

---

## Structure

```
sub_layer_2.05-2.14_setup_dependant_sub_layers/
└── 2.01_sub_project_setup_file_tree/
    └── 2.05_operating_systems/
        └── <os>/ or _shared/
            └── 2.06_environments/
                └── <env>/ or _shared/
                    └── 2.07_coding_apps/
                        └── <app>/ or _shared/
                            └── 2.08_apps_browsers/
                                └── <browser>/ or _shared/
                                    └── 2.09_ai_apps/
                                        └── <ai_app>/ or _shared/
                                            ├── 2.10_mcp_servers_and_apis_and_clis_and_secrets/
                                            ├── 2.11_ai_models/
                                            ├── 2.12_tools/
                                            ├── 2.13_protocols/
                                            ├── 2.14_agent_setup/
                                            └── setup/
```

### Using `_shared/` Directories

- `_shared/` directories contain documentation that applies across all options at that level
- Use specific directories (e.g., `linux_ubuntu/`, `cursor/`) for OS/app-specific setup
- Documentation cascades down: shared configs at higher levels apply to all children

---

## Sublayer Mapping

| Sublayer | Directory | Purpose |
|----------|-----------|---------|
| 2.05 | `2.05_operating_systems/` | OS-specific setup |
| 2.06 | `2.06_environments/` | Environment setup (local, remote, etc.) |
| 2.07 | `2.07_coding_apps/` | IDE/editor setup |
| 2.08 | `2.08_apps_browsers/` | Browser and app extensions |
| 2.09 | `2.09_ai_apps/` | AI CLI tools setup |
| 2.10 | `2.10_mcp_servers.../` | MCP server configuration |
| 2.11 | `2.11_ai_models/` | AI model configuration |
| 2.12 | `2.12_tools/` | Sub-project tools |
| 2.13 | `2.13_protocols/` | Sub-project protocols |
| 2.14 | `2.14_agent_setup/` | Agent configuration |

---

## Relationship to Universal Context

This structure mirrors the universal context's `sub_layer_0_05-0.014_setup_dependant_sub_layers/`. The numbering aligns:

| Universal | Sub-Project | Purpose |
|-----------|-------------|---------|
| 0.05 | 2.05 | OS Setup |
| 0.06 | 2.06 | Environment Setup |
| 0.07 | 2.07 | Coding App Setup |
| 0.08 | 2.08 | Apps/Browsers Setup |
| 0.09 | 2.09 | AI Apps Setup |
| 0.10 | 2.10 | MCP Servers Setup |
| 0.11 | 2.11 | AI Models |
| 0.12 | 2.12 | Tools |
| 0.13 | 2.13 | Protocols |
| 0.14 | 2.14 | Agent Setup |
