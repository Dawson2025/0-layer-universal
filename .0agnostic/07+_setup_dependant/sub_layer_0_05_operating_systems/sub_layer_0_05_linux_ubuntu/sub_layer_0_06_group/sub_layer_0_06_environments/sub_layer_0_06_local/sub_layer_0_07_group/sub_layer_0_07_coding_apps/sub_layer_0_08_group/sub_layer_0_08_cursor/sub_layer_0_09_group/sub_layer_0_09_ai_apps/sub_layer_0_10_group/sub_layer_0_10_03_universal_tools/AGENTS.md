# AutoGen Agent Context



## Identity

**Entity**: Universal Tools
**Sub-Layer**: 0.10
**Type**: Feature (shared across all AI apps)
**Feature Number**: 03 (third in sequence — shared dev tools that work across any AI app)
**Scope**: Shared development tools usable by any AI app, independent of specific AI platform

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → **Universal Tools (10)**

## Key Behaviors

- Contains tools like docx_ai_tool and other cross-platform development utilities
- Children are individual tool entities in `sub_layer_0_11_group/`
- Tools here must be AI-app-agnostic — if a tool only works with one AI app, it belongs in that app's entity
- Each child tool entity contains its own documentation, configuration, and usage patterns
- Tool dependencies and compatibility tracked in knowledge base

## Delegation Contract

**Children** (level 11): Individual tool entities (docx_ai_tool, etc.)
**Parent** (level 09): AI Apps Category
**Siblings**: 01_tools_and_services, 02_ai_models, 04_protocols, 05_agent_setup (features), claude_code_cli, codex_cli, cursor_agent, gemini_cli (further_specificity)

## Inputs

- Tool source code and documentation
- Configuration templates
- Dependency requirements

## Outputs

- Organized tool documentation accessible to all AI apps
- Configuration patterns and usage guides
- Tool compatibility matrices


## Current Status

- **Stage**: Active (created 2026-02-25 from content migration)
- **Structure**: Full canonical entity with .0agnostic/, stages directory, children group
- **Content**: Tools migrated from Claude Code CLI sub_layer_0_12_universal_tools/
- **Children**: docx_ai_tool and other shared tools in sub_layer_0_11_group/


## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
