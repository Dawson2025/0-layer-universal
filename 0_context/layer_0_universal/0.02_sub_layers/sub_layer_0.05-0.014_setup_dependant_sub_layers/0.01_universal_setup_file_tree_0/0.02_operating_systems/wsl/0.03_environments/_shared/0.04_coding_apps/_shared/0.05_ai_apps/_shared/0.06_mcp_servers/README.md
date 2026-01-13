# MCP Servers

This level organizes setup documentation by Model Context Protocol (MCP) server.

## Available MCP Servers

- **_shared/** - Setup that works across all MCP servers
- **_mcp_core/** - Core MCP issues that affect multiple servers
- **browser-mcp/** - Browser automation MCP server (@agent-infra/mcp-server-browser)
- **playwright-mcp/** - Playwright-based browser automation
- **chrome-devtools-mcp/** - Chrome DevTools Protocol MCP server
- **tavily-mcp/** - Tavily search API MCP server
- **context7-mcp/** - Context7 knowledge base MCP server

## How to Navigate

1. Choose your MCP server directory
2. Navigate to `general_setup_and_config/` for setup instructions
3. Use `_mcp_core/` for cross-server MCP issues
4. Use `_shared/` when the setup applies to all MCP servers

## MCP Server Categories

### Browser Automation
- **browser-mcp** - Works on all platforms including Linux
- **playwright-mcp** - Platform-specific issues (especially Linux/WSL)
- **chrome-devtools-mcp** - Chrome-specific automation

### Search and Knowledge
- **tavily-mcp** - Web search API integration
- **context7-mcp** - Knowledge base and context management

### Core MCP Issues (_mcp_core)
- Tool exposure issues (tools not showing up in AI apps)
- Environment variable handling
- Node.js/NVM path issues
- Server timeout and connection problems
- Configuration file syntax
- Platform-specific bugs

## MCP Setup Checklist

For each MCP server you set up:
1. Install the server package (npm, pip, etc.)
2. Configure in your AI app's config file
3. Set up any required API keys or credentials
4. Test the server connection
5. Verify tools are exposed to the AI
6. Document any issues in `general_setup_and_config/`

## Links to Detailed Documentation

For detailed MCP server setup, see:
- **sub_layer_0.10_mcp_servers_and_tools_setup/0.01_core-system/README.md**
- **sub_layer_0.10_mcp_servers_and_tools_setup/0.02_mcp_config_options_0_file_tree_0/** (alternative organization)

## Platform-Specific Notes

### Linux/Ubuntu
- Playwright MCP tools may not work in Cursor IDE (known bug)
- Use browser-mcp instead for Linux environments
- WSLg may be required for headed browser automation

### macOS
- Most MCP servers work out of the box
- May need to allow browser automation in System Preferences

### Windows/WSL
- Path translation between Windows and Linux
- NVM requires bash wrapper in MCP config
- Display server (WSLg) needed for headed browsers
