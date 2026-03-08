---
resource_id: "ea4644e4-9479-4e8d-9041-9627d32e5d07"
resource_type: "readme_document"
resource_name: "README"
---
# AI Apps and Tools

This level organizes setup documentation by AI application or tool.

<!-- section_id: "9663714c-3c0d-4ae6-aa78-5572a8133ecd" -->
## Available AI Apps

- **_shared/** - Setup that works across all AI apps
- **claude_code_cli/** - Claude Code CLI setup
- **cursor_agent/** - Cursor AI Agent setup
- **codex_cli/** - OpenAI Codex CLI setup
- **gemini_cli/** - Google Gemini CLI setup

<!-- section_id: "dbd74642-9b65-4f27-ae84-d93588667ad3" -->
## How to Navigate

1. Choose your AI app directory
2. Navigate down to `0.10_mcp_servers_and_apis_and_secrets/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all AI apps

<!-- section_id: "2fc07528-68e4-44d7-a16b-355ac5b687e6" -->
## AI App-Specific Considerations

<!-- section_id: "6fa93506-1d74-419e-9991-59adfc9aecca" -->
### Claude Code CLI
- Authentication with Anthropic API
- Configuration file location (`~/.claude/config.json`)
- MCP server setup via config
- Command-line usage patterns
- Context management

<!-- section_id: "b944f579-670f-4f94-a274-e04dc3a4d21a" -->
### Cursor Agent
- Integrated with Cursor IDE
- Chat interface vs Composer
- MCP server integration
- API key management
- Model selection

<!-- section_id: "d37406dd-2f3b-4b5f-831d-0296f6ce3ccb" -->
### Codex CLI
- OpenAI API authentication
- Rate limits and token usage
- Code generation patterns
- Integration with development workflow

<!-- section_id: "3cf0445f-9b6d-4303-92c4-2493aaa7eddf" -->
### Gemini CLI
- Google AI authentication
- Multi-modal capabilities
- Safety settings
- Model variants

<!-- section_id: "02c695d2-ce49-49c8-a38c-43b7409072a3" -->
## Links to Detailed Documentation

For detailed AI app setup, see:
- **sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/**
