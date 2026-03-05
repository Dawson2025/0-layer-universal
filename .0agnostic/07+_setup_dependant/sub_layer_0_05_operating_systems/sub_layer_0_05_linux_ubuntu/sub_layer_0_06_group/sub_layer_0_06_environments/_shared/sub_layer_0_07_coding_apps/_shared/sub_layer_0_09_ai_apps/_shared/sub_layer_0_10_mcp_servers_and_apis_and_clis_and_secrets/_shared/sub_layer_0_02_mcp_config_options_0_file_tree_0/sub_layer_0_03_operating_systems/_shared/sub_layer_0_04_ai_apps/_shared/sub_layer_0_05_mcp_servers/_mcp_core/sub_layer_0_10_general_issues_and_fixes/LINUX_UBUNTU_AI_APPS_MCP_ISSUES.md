---
resource_id: "dbae9587-899c-47b8-bec9-ec9f22802208"
resource_type: "document"
resource_name: "LINUX_UBUNTU_AI_APPS_MCP_ISSUES"
---
# Linux/Ubuntu AI Apps & Tools MCP Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Apps & Tools Setup  
**Status**: Platform-specific limitations affecting AI apps and tools

<!-- section_id: "3cad30d0-d513-4382-aae6-0f9c99c3332c" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) functionality within AI applications and tools. These issues impact how AI apps like Cursor IDE, Claude Code, and other tools interact with MCP servers.

<!-- section_id: "3eb31801-737a-472d-8c3b-78778aa0bc78" -->
## AI App-Specific MCP Issues

<!-- section_id: "6b6dc4a6-8830-40ef-88a1-9d97a8e4267e" -->
### 1. Cursor IDE on Linux

**Issue**: Playwright MCP tools are not exposed to AI agents despite successful server connection.

**Details**: See `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`

**Impact**: 
- Browser automation limited to `mcp_browser_*` tools
- Playwright MCP's 22 tools unavailable
- Must use alternative browser MCP servers

<!-- section_id: "9caee959-fb94-49cc-9c5f-094b5232237d" -->
### 2. Claude Code CLI on Linux

**Issue**: MCP configuration uses CLI commands rather than config files, requiring different setup approach.

**Impact**:
- MCP servers must be added via CLI: `claude add-mcp-server`
- Configuration not in standard `~/.claude/mcp.json` location
- May require bash wrappers for NVM-dependent servers

**Solution**: Follow Claude Code-specific MCP setup documentation.

<!-- section_id: "6015b8d6-1021-4e1d-b567-d6c22e0e6ad6" -->
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

<!-- section_id: "df2c302d-49df-4d33-aec9-215674d51128" -->
## Platform-Specific Configuration Patterns

<!-- section_id: "b0c3bfb2-27d5-4cdb-a273-9ffa891a7411" -->
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

<!-- section_id: "b4df0e93-335f-48ae-8bd3-1e020a01f175" -->
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

<!-- section_id: "ebeef3fc-76f2-4a6a-80b7-25c0e7987783" -->
### Pattern 3: System-Installed Tools

**Use Case**: MCP servers installed via system package manager

**Configuration**:
```json
{
  "command": "/usr/bin/mcp-server",
  "args": []
}
```

<!-- section_id: "7e378dd4-391b-48fc-86b6-85935b454a32" -->
## AI App Configuration Locations

<!-- section_id: "74043d74-c126-4580-b2f3-70a286ca62be" -->
### Cursor IDE
- **Config File**: `~/.cursor/mcp.json`
- **Logs**: `~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/`
- **Status**: Check Settings → Tools & MCP → Model Context Protocol

<!-- section_id: "31603e48-924f-49b9-8253-949799bd4507" -->
### Claude Code
- **Config Method**: CLI commands (`claude add-mcp-server`)
- **Status**: Check via CLI or app interface

<!-- section_id: "b458a7c5-abc1-4b24-9ca4-5b40f84de0f3" -->
### Other AI Apps
- Check app-specific documentation for MCP configuration location
- May use `~/.config/<app>/mcp.json` or similar

<!-- section_id: "a6d6d097-f7ef-4cc9-b948-820c3dab80f3" -->
## Verification Checklist

When setting up AI apps on Linux/Ubuntu:

- [ ] Node.js available via NVM (if using Node.js-based MCP servers)
- [ ] Browser paths explicitly configured (if using browser MCP servers)
- [ ] MCP config uses bash wrappers for NVM-dependent servers
- [ ] Environment variables set (PLAYWRIGHT_BROWSERS_PATH, DISPLAY, etc.)
- [ ] MCP servers start successfully (check logs)
- [ ] Tools are accessible to AI agents (test tool availability)
- [ ] Alternative tools identified if primary tools unavailable

<!-- section_id: "4ee4b279-3e7b-4702-ae19-05bb6a94755c" -->
## Troubleshooting

<!-- section_id: "0131baab-adf2-4093-a468-1309a2162b7c" -->
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

<!-- section_id: "ade314ce-e017-49c0-b65c-db295295db64" -->
### Tools Not Accessible

1. Verify server is connected (check logs)

2. Check tool naming convention (may differ on Linux)

3. Try alternative MCP server (e.g., Browser MCP instead of Playwright)

4. Restart AI app completely

<!-- section_id: "55f8b68f-04b5-4a71-ad1b-e8adae80de28" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "f2ca3187-79fd-44ed-921e-c400b59ae1de" -->
## References

- AI App Documentation: Check respective app documentation
- MCP Protocol: https://modelcontextprotocol.io
- GitHub Issues: Platform-specific MCP problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
