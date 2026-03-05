---
resource_id: "8b76045a-8dc4-41dd-9471-e7066c688eb5"
resource_type: "document"
resource_name: "LINUX_UBUNTU_AI_APPS_MCP_ISSUES"
---
# Linux/Ubuntu AI Apps & Tools MCP Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Apps & Tools Setup  
**Status**: Platform-specific limitations affecting AI apps and tools

## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) functionality within AI applications and tools. These issues impact how AI apps like Cursor IDE, Claude Code, and other tools interact with MCP servers.

## AI App-Specific MCP Issues

### 1. Cursor IDE on Linux

**Issue**: Playwright MCP tools are not exposed to AI agents despite successful server connection.

**Details**: See `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`

**Impact**: 
- Browser automation limited to `mcp_browser_*` tools
- Playwright MCP's 22 tools unavailable
- Must use alternative browser MCP servers

### 2. Claude Code CLI on Linux

**Issue**: MCP configuration uses CLI commands rather than config files, requiring different setup approach.

**Impact**:
- MCP servers must be added via CLI: `claude add-mcp-server`
- Configuration not in standard `~/.claude/mcp.json` location
- May require bash wrappers for NVM-dependent servers

**Solution**: Follow Claude Code-specific MCP setup documentation.

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

## Platform-Specific Configuration Patterns

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

### Pattern 3: System-Installed Tools

**Use Case**: MCP servers installed via system package manager

**Configuration**:
```json
{
  "command": "/usr/bin/mcp-server",
  "args": []
}
```

## AI App Configuration Locations

### Cursor IDE
- **Config File**: `~/.cursor/mcp.json`
- **Logs**: `~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/`
- **Status**: Check Settings → Tools & MCP → Model Context Protocol

### Claude Code
- **Config Method**: CLI commands (`claude add-mcp-server`)
- **Status**: Check via CLI or app interface

### Other AI Apps
- Check app-specific documentation for MCP configuration location
- May use `~/.config/<app>/mcp.json` or similar

## Verification Checklist

When setting up AI apps on Linux/Ubuntu:

- [ ] Node.js available via NVM (if using Node.js-based MCP servers)
- [ ] Browser paths explicitly configured (if using browser MCP servers)
- [ ] MCP config uses bash wrappers for NVM-dependent servers
- [ ] Environment variables set (PLAYWRIGHT_BROWSERS_PATH, DISPLAY, etc.)
- [ ] MCP servers start successfully (check logs)
- [ ] Tools are accessible to AI agents (test tool availability)
- [ ] Alternative tools identified if primary tools unavailable

## Troubleshooting

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

### Tools Not Accessible

1. Verify server is connected (check logs)

2. Check tool naming convention (may differ on Linux)

3. Try alternative MCP server (e.g., Browser MCP instead of Playwright)

4. Restart AI app completely

## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`

## References

- AI App Documentation: Check respective app documentation
- MCP Protocol: https://modelcontextprotocol.io
- GitHub Issues: Platform-specific MCP problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
