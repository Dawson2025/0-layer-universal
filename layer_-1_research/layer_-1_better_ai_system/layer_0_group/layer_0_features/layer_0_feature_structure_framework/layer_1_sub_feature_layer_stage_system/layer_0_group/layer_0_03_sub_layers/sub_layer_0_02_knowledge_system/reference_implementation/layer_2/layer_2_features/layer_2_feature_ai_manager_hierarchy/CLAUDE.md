# layer_2_feature_ai_manager_hierarchy

## Purpose
Defines the agnostic/specific pattern and AI tool configurations.

## Core Pattern

### Agnostic Source
- Location: `layer_N_00_ai_manager_system/agnostic/`
- Content: Tool-independent source of truth
- Files: init_prompt.md, context_rules.md, etc.

### Specific Implementation
- Location: `layer_N_00_ai_manager_system/specific/`
- Content: Tool-specific configurations
- Nesting: os → environment → coding_app → ai_app

## Nested Specificity
```
specific/
└── os/
    └── {wsl|linux|macos|windows}/
        └── environment/
            └── {local|cloud}/
                └── coding_app/
                    └── {cursor|vscode|terminal}/
                        └── ai_app/
                            └── {claude|codex|gemini}/
```

## Tool-Specific Files at Entity Root
- CLAUDE.md - Claude Code
- .claude/ - Claude Code folder
- .cursorrules - Cursor IDE
- AGENTS.md - OpenAI Codex
- GEMINI.md - Gemini CLI

## Components
- `layer_3_component_claude_code_config/` - Claude Code patterns
- `layer_3_component_cursor_config/` - Cursor patterns
- `layer_3_component_codex_config/` - Codex patterns
- `layer_3_component_gemini_config/` - Gemini patterns
