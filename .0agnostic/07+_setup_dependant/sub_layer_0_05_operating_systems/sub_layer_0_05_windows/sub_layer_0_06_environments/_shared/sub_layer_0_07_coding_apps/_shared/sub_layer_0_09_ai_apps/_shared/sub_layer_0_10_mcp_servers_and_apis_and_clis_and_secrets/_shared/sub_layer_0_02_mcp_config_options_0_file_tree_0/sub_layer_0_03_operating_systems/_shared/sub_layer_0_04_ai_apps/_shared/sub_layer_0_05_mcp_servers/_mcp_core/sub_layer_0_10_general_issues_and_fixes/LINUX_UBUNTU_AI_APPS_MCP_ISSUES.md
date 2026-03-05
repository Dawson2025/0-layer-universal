---
resource_id: "02545fc1-8e13-4cfb-bfcd-22eb0f41ae62"
resource_type: "document"
resource_name: "LINUX_UBUNTU_AI_APPS_MCP_ISSUES"
---
# Linux/Ubuntu AI Apps & Tools MCP Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Apps & Tools Setup  
**Status**: Platform-specific limitations affecting AI apps and tools

<!-- section_id: "da3ff5b7-c9c2-4dab-8189-5a6189026d6a" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) functionality within AI applications and tools. These issues impact how AI apps like Cursor IDE, Claude Code, and other tools interact with MCP servers.

<!-- section_id: "63854789-8800-468a-ab14-a6ca5888aa74" -->
## AI App-Specific MCP Issues

<!-- section_id: "c6a631ad-f917-4d8c-ac33-c4583fc45b06" -->
### 1. Cursor IDE on Linux

**Issue**: Playwright MCP tools are not exposed to AI agents despite successful server connection.

**Details**: See `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`

**Impact**: 
- Browser automation limited to `mcp_browser_*` tools
- Playwright MCP's 22 tools unavailable
- Must use alternative browser MCP servers

<!-- section_id: "204ac04d-cddb-4901-82d4-999107b9a79d" -->
### 2. Claude Code CLI on Linux

**Issue**: MCP configuration uses CLI commands rather than config files, requiring different setup approach.

**Impact**:
- MCP servers must be added via CLI: `claude add-mcp-server`
- Configuration not in standard `~/.claude/mcp.json` location
- May require bash wrappers for NVM-dependent servers

**Solution**: Follow Claude Code-specific MCP setup documentation.

<!-- section_id: "fe16a0df-a10a-403c-894c-0b000e33276d" -->
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

<!-- section_id: "83e0b06b-61a5-417b-b49b-628392848d37" -->
## Platform-Specific Configuration Patterns

<!-- section_id: "1c31a387-d65c-4fc8-adae-d1b114d90a7e" -->
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

<!-- section_id: "d0faace6-6114-41eb-a2e1-dd5f54964af5" -->
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

<!-- section_id: "db0d9aba-fc8b-475d-a275-c34abf2929f2" -->
### Pattern 3: System-Installed Tools

**Use Case**: MCP servers installed via system package manager

**Configuration**:
```json
{
  "command": "/usr/bin/mcp-server",
  "args": []
}
```

<!-- section_id: "b1550934-21af-48d5-b475-841884d93479" -->
## AI App Configuration Locations

<!-- section_id: "f3cf4482-5298-47f8-9809-d627e7fef7fe" -->
### Cursor IDE
- **Config File**: `~/.cursor/mcp.json`
- **Logs**: `~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/`
- **Status**: Check Settings → Tools & MCP → Model Context Protocol

<!-- section_id: "8e350703-0ee0-4330-a8d5-6010eb65458e" -->
### Claude Code
- **Config Method**: CLI commands (`claude add-mcp-server`)
- **Status**: Check via CLI or app interface

<!-- section_id: "a7d2b0f3-96fe-4d98-9ab7-6e7773b782cb" -->
### Other AI Apps
- Check app-specific documentation for MCP configuration location
- May use `~/.config/<app>/mcp.json` or similar

<!-- section_id: "54474e90-019b-41f3-8417-0a737c2e0e37" -->
## Verification Checklist

When setting up AI apps on Linux/Ubuntu:

- [ ] Node.js available via NVM (if using Node.js-based MCP servers)
- [ ] Browser paths explicitly configured (if using browser MCP servers)
- [ ] MCP config uses bash wrappers for NVM-dependent servers
- [ ] Environment variables set (PLAYWRIGHT_BROWSERS_PATH, DISPLAY, etc.)
- [ ] MCP servers start successfully (check logs)
- [ ] Tools are accessible to AI agents (test tool availability)
- [ ] Alternative tools identified if primary tools unavailable

<!-- section_id: "9997a242-faab-4d1c-81c0-a3b21197f724" -->
## Troubleshooting

<!-- section_id: "75493b3f-c49a-476f-89f3-7787b9bf57b1" -->
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

<!-- section_id: "fedff1dd-ea37-4377-a931-f903cc9e6d38" -->
### Tools Not Accessible

1. Verify server is connected (check logs)

2. Check tool naming convention (may differ on Linux)

3. Try alternative MCP server (e.g., Browser MCP instead of Playwright)

4. Restart AI app completely

<!-- section_id: "a3c72f17-1524-4f05-9178-2ba6cfef91a6" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "fb5cc604-e4a8-4b5c-ad4e-1045d6215286" -->
## References

- AI App Documentation: Check respective app documentation
- MCP Protocol: https://modelcontextprotocol.io
- GitHub Issues: Platform-specific MCP problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
