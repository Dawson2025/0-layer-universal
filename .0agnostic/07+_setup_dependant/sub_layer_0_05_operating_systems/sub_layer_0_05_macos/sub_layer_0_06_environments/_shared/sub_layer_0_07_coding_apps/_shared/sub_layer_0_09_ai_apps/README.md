---
resource_id: "0a9947e1-27b3-45b3-8b13-05171f3206d8"
resource_type: "readme
document"
resource_name: "README"
---
# AI Apps and Tools

This level organizes setup documentation by AI application or tool.

<!-- section_id: "d85a4673-ea7b-4d07-b0ba-a134a44b818e" -->
## Available AI Apps

- **_shared/** - Setup that works across all AI apps
- **claude_code_cli/** - Claude Code CLI setup
- **cursor_agent/** - Cursor AI Agent setup
- **codex_cli/** - OpenAI Codex CLI setup
- **gemini_cli/** - Google Gemini CLI setup

<!-- section_id: "ee305f5f-3c52-49ff-aeb3-22efe9fd4578" -->
## How to Navigate

1. Choose your AI app directory
2. Navigate down to `0.10_mcp_servers_and_apis_and_secrets/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all AI apps

<!-- section_id: "7b2622bb-3dd8-4496-a434-77e45aa7b755" -->
## AI App-Specific Considerations

<!-- section_id: "4e23fed4-c42a-40fe-8b42-0e10b47dc084" -->
### Claude Code CLI
- Authentication with Anthropic API
- Configuration file location (`~/.claude/config.json`)
- MCP server setup via config
- Command-line usage patterns
- Context management

<!-- section_id: "aa12c294-27f2-484b-ac17-214b6074a876" -->
### Cursor Agent
- Integrated with Cursor IDE
- Chat interface vs Composer
- MCP server integration
- API key management
- Model selection

<!-- section_id: "fffa6750-677a-4c9c-8fbb-610ccc843c17" -->
### Codex CLI
- OpenAI API authentication
- Rate limits and token usage
- Code generation patterns
- Integration with development workflow

<!-- section_id: "731de619-0b70-4696-b7c7-4c8d3ad6effc" -->
### Gemini CLI
- Google AI authentication
- Multi-modal capabilities
- Safety settings
- Model variants

<!-- section_id: "bed8c0ea-ce27-4fc4-8bb6-6ab6b4610177" -->
## Links to Detailed Documentation

For detailed AI app setup, see:
- **sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/**
