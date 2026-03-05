---
resource_id: "a78dd884-9811-472a-92f9-13e9a8df1acd"
resource_type: "readme
document"
resource_name: "README"
---
# AI Apps and Tools

This level organizes setup documentation by AI application or tool.

<!-- section_id: "b007dd8a-149b-48c0-b9c3-c145fb87396b" -->
## Available AI Apps

- **_shared/** - Setup that works across all AI apps
- **claude_code_cli/** - Claude Code CLI setup
- **cursor_agent/** - Cursor AI Agent setup
- **codex_cli/** - OpenAI Codex CLI setup
- **gemini_cli/** - Google Gemini CLI setup

<!-- section_id: "57b0c111-aeb5-4e7f-8646-ea0e2b0f926d" -->
## How to Navigate

1. Choose your AI app directory
2. Navigate down to `0.10_mcp_servers_and_apis_and_secrets/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all AI apps

<!-- section_id: "47da2cc2-6c3b-4152-a148-a503a371caee" -->
## AI App-Specific Considerations

<!-- section_id: "d35756d8-8d93-4a9f-9321-9a7a1df0d470" -->
### Claude Code CLI
- Authentication with Anthropic API
- Configuration file location (`~/.claude/config.json`)
- MCP server setup via config
- Command-line usage patterns
- Context management

<!-- section_id: "8fa9f135-328a-4f89-8233-36b7267821b5" -->
### Cursor Agent
- Integrated with Cursor IDE
- Chat interface vs Composer
- MCP server integration
- API key management
- Model selection

<!-- section_id: "f51f2a1b-7236-44ee-b06c-d06f354fd86e" -->
### Codex CLI
- OpenAI API authentication
- Rate limits and token usage
- Code generation patterns
- Integration with development workflow

<!-- section_id: "c7b1878e-e2f8-47c7-bb40-91fec3fcea8b" -->
### Gemini CLI
- Google AI authentication
- Multi-modal capabilities
- Safety settings
- Model variants

<!-- section_id: "70c3508b-3862-41f8-8527-68a1b3f406a3" -->
## Links to Detailed Documentation

For detailed AI app setup, see:
- **sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/**
