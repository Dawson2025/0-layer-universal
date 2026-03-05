---
resource_id: "1bcee1da-1edb-4ee5-92f6-b29c49cc2f86"
resource_type: "document"
resource_name: "tool_config_patterns"
---
# Tool Configuration Patterns

## Overview
Each AI coding tool has specific configuration files at the entity root.

## Tool-Specific Files

### Claude Code
- **File**: `CLAUDE.md`
- **Folder**: `.claude/`
- **Location**: Entity root
- **Component**: `layer_3_component_claude_code_config/`

### Cursor IDE
- **File**: `.cursorrules`
- **Location**: Entity root
- **Component**: `layer_3_component_cursor_config/`

### OpenAI Codex
- **File**: `AGENTS.md`
- **Location**: Entity root
- **Component**: `layer_3_component_codex_config/`

### Gemini CLI
- **File**: `GEMINI.md`
- **Location**: Entity root
- **Component**: `layer_3_component_gemini_config/`

## Resolution Order
1. Load agnostic source
2. Check for specific overrides based on current environment
3. Apply tool-specific configuration from entity root file
