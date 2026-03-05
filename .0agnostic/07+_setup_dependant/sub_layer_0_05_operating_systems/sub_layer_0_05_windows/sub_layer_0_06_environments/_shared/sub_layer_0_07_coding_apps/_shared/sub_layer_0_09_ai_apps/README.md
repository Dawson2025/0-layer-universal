---
resource_id: "407b9036-9e97-4239-9172-bce6d96148fd"
resource_type: "readme
document"
resource_name: "README"
---
# AI Apps and Tools

This level organizes setup documentation by AI application or tool.

<!-- section_id: "eb9cfaba-d57f-4487-a35f-3a7a3cf1f98b" -->
## Available AI Apps

- **_shared/** - Setup that works across all AI apps
- **claude_code_cli/** - Claude Code CLI setup
- **cursor_agent/** - Cursor AI Agent setup
- **codex_cli/** - OpenAI Codex CLI setup
- **gemini_cli/** - Google Gemini CLI setup

<!-- section_id: "3b6d5a72-d0cc-4e13-a823-06b0b16a9ff0" -->
## How to Navigate

1. Choose your AI app directory
2. Navigate down to `0.10_mcp_servers_and_apis_and_secrets/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all AI apps

<!-- section_id: "8ccc73ec-b0e1-49f5-b70f-e097a8f1db73" -->
## AI App-Specific Considerations

<!-- section_id: "fe9156ca-10df-4411-88b3-82a305518496" -->
### Claude Code CLI
- Authentication with Anthropic API
- Configuration file location (`~/.claude/config.json`)
- MCP server setup via config
- Command-line usage patterns
- Context management

<!-- section_id: "47055c58-77bb-4488-9be5-adb18158ee72" -->
### Cursor Agent
- Integrated with Cursor IDE
- Chat interface vs Composer
- MCP server integration
- API key management
- Model selection

<!-- section_id: "e1b007c1-fc52-4265-9408-1a79c650bb54" -->
### Codex CLI
- OpenAI API authentication
- Rate limits and token usage
- Code generation patterns
- Integration with development workflow

<!-- section_id: "cc659475-ef91-4d8b-ab8a-d39e2975f16b" -->
### Gemini CLI
- Google AI authentication
- Multi-modal capabilities
- Safety settings
- Model variants

<!-- section_id: "acc3d55b-a024-4571-859c-8b365a95fc81" -->
## Links to Detailed Documentation

For detailed AI app setup, see:
- **sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/**
