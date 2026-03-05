---
resource_id: "a206faeb-48e2-4c26-ab8c-3492dc2eff72"
resource_type: "readme
document"
resource_name: "README"
---
# AI Apps and Tools

This level organizes setup documentation by AI application or tool.

<!-- section_id: "ad57c698-5822-4333-8624-104455a39458" -->
## Available AI Apps

- **_shared/** - Setup that works across all AI apps
- **claude_code_cli/** - Claude Code CLI setup
- **cursor_agent/** - Cursor AI Agent setup
- **codex_cli/** - OpenAI Codex CLI setup
- **gemini_cli/** - Google Gemini CLI setup

<!-- section_id: "8ead542e-130e-4cd1-aefd-cb873a399f85" -->
## How to Navigate

1. Choose your AI app directory
2. Navigate down to `0.10_mcp_servers_and_apis_and_secrets/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all AI apps

<!-- section_id: "7cacef0a-5317-4c06-819b-90b5b8c78809" -->
## AI App-Specific Considerations

<!-- section_id: "d5bd2d0d-6837-43bd-9ac5-d5500f155577" -->
### Claude Code CLI
- Authentication with Anthropic API
- Configuration file location (`~/.claude/config.json`)
- MCP server setup via config
- Command-line usage patterns
- Context management

<!-- section_id: "a62e4929-d0cb-49ff-b1b4-400ffb0549da" -->
### Cursor Agent
- Integrated with Cursor IDE
- Chat interface vs Composer
- MCP server integration
- API key management
- Model selection

<!-- section_id: "e9418732-eff7-4e0e-b3f6-326aed979d6d" -->
### Codex CLI
- OpenAI API authentication
- Rate limits and token usage
- Code generation patterns
- Integration with development workflow

<!-- section_id: "b62d5d6e-e792-4128-b7c0-af517c06fd46" -->
### Gemini CLI
- Google AI authentication
- Multi-modal capabilities
- Safety settings
- Model variants

<!-- section_id: "9fdd093e-7c47-4baf-8f74-b1f302dbbf5f" -->
## Links to Detailed Documentation

For detailed AI app setup, see:
- **sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/**
