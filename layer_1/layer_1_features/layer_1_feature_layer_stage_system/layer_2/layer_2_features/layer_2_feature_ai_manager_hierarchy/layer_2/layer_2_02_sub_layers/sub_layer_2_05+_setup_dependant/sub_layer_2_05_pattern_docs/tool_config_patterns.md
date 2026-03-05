---
resource_id: "1bcee1da-1edb-4ee5-92f6-b29c49cc2f86"
resource_type: "document"
resource_name: "tool_config_patterns"
---
# Tool Configuration Patterns

<!-- section_id: "50eb3c60-cd7d-418e-aec1-c9f4705e5bb1" -->
## Overview
Each AI coding tool has specific configuration files at the entity root.

<!-- section_id: "dcd729c1-4703-4d30-8f99-5d88c2044210" -->
## Tool-Specific Files

<!-- section_id: "f176f240-9392-4070-af7f-226e5b687927" -->
### Claude Code
- **File**: `CLAUDE.md`
- **Folder**: `.claude/`
- **Location**: Entity root
- **Component**: `layer_3_component_claude_code_config/`

<!-- section_id: "6f4b89ac-268a-47e7-8ec0-3249e547465b" -->
### Cursor IDE
- **File**: `.cursorrules`
- **Location**: Entity root
- **Component**: `layer_3_component_cursor_config/`

<!-- section_id: "959774ef-b14b-4178-ac00-43e7991b1ab6" -->
### OpenAI Codex
- **File**: `AGENTS.md`
- **Location**: Entity root
- **Component**: `layer_3_component_codex_config/`

<!-- section_id: "129291b6-f84c-44a3-a0d7-e988058d77dd" -->
### Gemini CLI
- **File**: `GEMINI.md`
- **Location**: Entity root
- **Component**: `layer_3_component_gemini_config/`

<!-- section_id: "c77e5b4e-afae-4a2e-80ec-7784dd6f9860" -->
## Resolution Order
1. Load agnostic source
2. Check for specific overrides based on current environment
3. Apply tool-specific configuration from entity root file
