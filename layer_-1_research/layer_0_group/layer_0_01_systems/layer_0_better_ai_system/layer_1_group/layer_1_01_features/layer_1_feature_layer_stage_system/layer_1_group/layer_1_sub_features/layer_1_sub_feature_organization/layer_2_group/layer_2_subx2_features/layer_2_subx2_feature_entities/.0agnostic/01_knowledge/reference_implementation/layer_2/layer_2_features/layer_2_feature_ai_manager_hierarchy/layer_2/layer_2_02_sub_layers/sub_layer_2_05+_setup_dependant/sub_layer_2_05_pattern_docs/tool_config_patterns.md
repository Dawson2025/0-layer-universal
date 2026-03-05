---
resource_id: "6220cbc8-2a38-49f5-a273-87466933ed11"
resource_type: "knowledge"
resource_name: "tool_config_patterns"
---
# Tool Configuration Patterns

<!-- section_id: "c1d23eff-70dc-4259-be31-4952550f39ca" -->
## Overview
Each AI coding tool has specific configuration files at the entity root.

<!-- section_id: "cdcc4dcd-a68e-4a50-b00a-034f9aaa1b58" -->
## Tool-Specific Files

<!-- section_id: "f0d16987-9477-4819-aa9c-d59d5b37ff06" -->
### Claude Code
- **File**: `CLAUDE.md`
- **Folder**: `.claude/`
- **Location**: Entity root
- **Component**: `layer_3_component_claude_code_config/`

<!-- section_id: "3ec9d00b-e9e5-4fa4-9dce-d3be5d3d1463" -->
### Cursor IDE
- **File**: `.cursorrules`
- **Location**: Entity root
- **Component**: `layer_3_component_cursor_config/`

<!-- section_id: "0a3713d2-aaa5-4ff5-8779-314f62940290" -->
### OpenAI Codex
- **File**: `AGENTS.md`
- **Location**: Entity root
- **Component**: `layer_3_component_codex_config/`

<!-- section_id: "fea75669-f5b0-4140-b4df-179c601b3772" -->
### Gemini CLI
- **File**: `GEMINI.md`
- **Location**: Entity root
- **Component**: `layer_3_component_gemini_config/`

<!-- section_id: "6cf57dde-9aa4-465d-9b4a-c1273d0bb95e" -->
## Resolution Order
1. Load agnostic source
2. Check for specific overrides based on current environment
3. Apply tool-specific configuration from entity root file
