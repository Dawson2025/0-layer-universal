---
resource_id: "09dbcca1-dc90-4495-ac2e-f89c9b49af56"
resource_type: "document"
resource_name: "LINUX_UBUNTU_AI_APPS_MCP_ISSUES"
---
# Linux/Ubuntu AI Apps & Tools MCP Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Apps & Tools Setup  
**Status**: Platform-specific limitations affecting AI apps and tools

<!-- section_id: "caf44b1d-3341-4f78-9108-70370f29e40a" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) functionality within AI applications and tools. These issues impact how AI apps like Cursor IDE, Claude Code, and other tools interact with MCP servers.

<!-- section_id: "2e319f46-871a-49ef-a746-73305d03840e" -->
## AI App-Specific MCP Issues

<!-- section_id: "251117bc-b70d-45db-8e70-fc6c5a018e5c" -->
### 1. Cursor IDE on Linux

**Issue**: Playwright MCP tools are not exposed to AI agents despite successful server connection.

**Details**: See `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`

**Impact**: 
- Browser automation limited to `mcp_browser_*` tools
- Playwright MCP's 22 tools unavailable
- Must use alternative browser MCP servers

<!-- section_id: "6ac45d8a-6adf-4c24-9c8c-7f112cc49f8a" -->
### 2. Claude Code CLI on Linux

**Issue**: MCP configuration uses CLI commands rather than config files, requiring different setup approach.

**Impact**:
- MCP servers must be added via CLI: `claude add-mcp-server`
- Configuration not in standard `~/.claude/mcp.json` location
- May require bash wrappers for NVM-dependent servers

**Solution**: Follow Claude Code-specific MCP setup documentation.

<!-- section_id: "ac95b361-ef1a-4b96-b4ac-2d546ca890a2" -->
### 3. Node.js/NVM Dependencies

**Issue**: AI apps may not have access to NVM environment when launching MCP servers.

**Impact**:
- MCP servers fail to find Node.js/npx
- Server startup failures
- Tools unavailable

**Solution**: Use bash wrappers in MCP configurations to load NVM:
```json
{
  "mcpServer": {
    "command": "bash",
    "args": [
      "-c",
      "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\" && npx -y @package/mcp-server"
    ]
  }
}
```

<!-- section_id: "2a4fe8ea-e441-4493-9200-1220e2ac1486" -->
## Platform-Specific Configuration Patterns

<!-- section_id: "8ce2a96a-d797-48c0-94ee-bcd120bbb3c5" -->
### Pattern 1: NVM-Dependent MCP Servers

**Use Case**: Any MCP server that requires Node.js via NVM

**Configuration**:
```json
{
  "command": "bash",
  "args": [
    "-c",
    "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\" && npx -y @package/mcp-server"
  ]
}
```

<!-- section_id: "cd6cd9dd-b910-4569-8c18-1bd489f45018" -->
### Pattern 2: Browser-Based MCP Servers

**Use Case**: Playwright, Browser MCP, Chrome DevTools MCP

**Configuration**:
```json
{
  "command": "bash",
  "args": [
    "-c",
    "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\" && npx -y @package/mcp-server --executable-path /absolute/path/to/browser"
  ],
  "env": {
    "PLAYWRIGHT_BROWSERS_PATH": "/home/user/.cache/ms-playwright"
  }
}
```

<!-- section_id: "a79758a3-1c0e-4311-9b9c-4f6971bb1e33" -->
### Pattern 3: System-Installed Tools

**Use Case**: MCP servers installed via system package manager

**Configuration**:
```json
{
  "command": "/usr/bin/mcp-server",
  "args": []
}
```

<!-- section_id: "1314067a-a299-43f0-8014-9fb46e966a56" -->
## AI App Configuration Locations

<!-- section_id: "c48a9777-1900-43f0-9318-ad1eb12a38b5" -->
### Cursor IDE
- **Config File**: `~/.cursor/mcp.json`
- **Logs**: `~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/`
- **Status**: Check Settings → Tools & MCP → Model Context Protocol

<!-- section_id: "e5fe9d9f-4944-4dde-80fe-8f789401771d" -->
### Claude Code
- **Config Method**: CLI commands (`claude add-mcp-server`)
- **Status**: Check via CLI or app interface

<!-- section_id: "4bf29c5f-2403-451d-8a5c-620f1fe9617f" -->
### Other AI Apps
- Check app-specific documentation for MCP configuration location
- May use `~/.config/<app>/mcp.json` or similar

<!-- section_id: "10a9fb82-bc77-4f32-b34e-a97ed6dc4f11" -->
## Verification Checklist

When setting up AI apps on Linux/Ubuntu:

- [ ] Node.js available via NVM (if using Node.js-based MCP servers)
- [ ] Browser paths explicitly configured (if using browser MCP servers)
- [ ] MCP config uses bash wrappers for NVM-dependent servers
- [ ] Environment variables set (PLAYWRIGHT_BROWSERS_PATH, DISPLAY, etc.)
- [ ] MCP servers start successfully (check logs)
- [ ] Tools are accessible to AI agents (test tool availability)
- [ ] Alternative tools identified if primary tools unavailable

<!-- section_id: "244edd5e-f7bc-49f6-8f98-7432cccbc913" -->
## Troubleshooting

<!-- section_id: "47540584-fd4f-49ae-91f4-2036a072b5a5" -->
### MCP Server Won't Start

1. Check Node.js availability:
   ```bash
   which node && node --version
   ```

2. Verify NVM is loaded in MCP process (use bash wrapper)

3. Check browser paths (if browser-based):
   ```bash
   ls -la /path/to/browser
   ```

<!-- section_id: "ab720883-d106-4c1d-9d57-7c3ab79acd5d" -->
### Tools Not Accessible

1. Verify server is connected (check logs)

2. Check tool naming convention (may differ on Linux)

3. Try alternative MCP server (e.g., Browser MCP instead of Playwright)

4. Restart AI app completely

<!-- section_id: "9a35d0c6-7784-4017-a3f6-f842ac9df0d1" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "522fec87-1d49-40ba-af19-1ef52d605c0e" -->
## References

- AI App Documentation: Check respective app documentation
- MCP Protocol: https://modelcontextprotocol.io
- GitHub Issues: Platform-specific MCP problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
