---
resource_id: "949bb0e1-dfd0-4c23-8b98-bb10c1db7d7c"
resource_type: "document"
resource_name: "LINUX_UBUNTU_AI_APPS_MCP_ISSUES"
---
# Linux/Ubuntu AI Apps & Tools MCP Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Apps & Tools Setup  
**Status**: Platform-specific limitations affecting AI apps and tools

<!-- section_id: "9126f621-1b3d-4b01-b2a3-05f5d47eaa44" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect MCP (Model Context Protocol) functionality within AI applications and tools. These issues impact how AI apps like Cursor IDE, Claude Code, and other tools interact with MCP servers.

<!-- section_id: "9b7d00af-3d7b-4bdb-ab05-d93769fdefbe" -->
## AI App-Specific MCP Issues

<!-- section_id: "6fe0d720-9422-4cca-9ea1-e28c7f20ce20" -->
### 1. Cursor IDE on Linux

**Issue**: Playwright MCP tools are not exposed to AI agents despite successful server connection.

**Details**: See `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`

**Impact**: 
- Browser automation limited to `mcp_browser_*` tools
- Playwright MCP's 22 tools unavailable
- Must use alternative browser MCP servers

<!-- section_id: "3422c401-7f30-45d0-a9df-0a727dcbed47" -->
### 2. Claude Code CLI on Linux

**Issue**: MCP configuration uses CLI commands rather than config files, requiring different setup approach.

**Impact**:
- MCP servers must be added via CLI: `claude add-mcp-server`
- Configuration not in standard `~/.claude/mcp.json` location
- May require bash wrappers for NVM-dependent servers

**Solution**: Follow Claude Code-specific MCP setup documentation.

<!-- section_id: "ac88722a-175f-48da-be79-745b7c52caa8" -->
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

<!-- section_id: "991d1397-e564-45e4-9b21-9979dae19bb8" -->
## Platform-Specific Configuration Patterns

<!-- section_id: "bb627969-fac1-45aa-9e4a-5e1d1579d986" -->
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

<!-- section_id: "5c9b9ba5-ce42-496b-a608-8874eeb435e4" -->
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

<!-- section_id: "4aee2317-ab73-46ef-b5fd-497f8250f75e" -->
### Pattern 3: System-Installed Tools

**Use Case**: MCP servers installed via system package manager

**Configuration**:
```json
{
  "command": "/usr/bin/mcp-server",
  "args": []
}
```

<!-- section_id: "077fecf7-43b9-4532-b3c1-becf26820567" -->
## AI App Configuration Locations

<!-- section_id: "0455f161-ceed-4938-8ca5-6afe022a1e5e" -->
### Cursor IDE
- **Config File**: `~/.cursor/mcp.json`
- **Logs**: `~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/`
- **Status**: Check Settings → Tools & MCP → Model Context Protocol

<!-- section_id: "4bf9b9bd-e901-437b-9de3-cfd1507bcf5f" -->
### Claude Code
- **Config Method**: CLI commands (`claude add-mcp-server`)
- **Status**: Check via CLI or app interface

<!-- section_id: "9054f2fd-6a78-493e-872a-f82617f1d515" -->
### Other AI Apps
- Check app-specific documentation for MCP configuration location
- May use `~/.config/<app>/mcp.json` or similar

<!-- section_id: "321016fd-2fc9-435d-bd22-8631b27ec91a" -->
## Verification Checklist

When setting up AI apps on Linux/Ubuntu:

- [ ] Node.js available via NVM (if using Node.js-based MCP servers)
- [ ] Browser paths explicitly configured (if using browser MCP servers)
- [ ] MCP config uses bash wrappers for NVM-dependent servers
- [ ] Environment variables set (PLAYWRIGHT_BROWSERS_PATH, DISPLAY, etc.)
- [ ] MCP servers start successfully (check logs)
- [ ] Tools are accessible to AI agents (test tool availability)
- [ ] Alternative tools identified if primary tools unavailable

<!-- section_id: "2723c133-a7ac-49c1-9b05-ecf4ecc5191b" -->
## Troubleshooting

<!-- section_id: "8fe94b0b-0427-4f5e-b4e4-c0ff8c7f6902" -->
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

<!-- section_id: "045afe15-3df2-41af-9997-d92689d58e79" -->
### Tools Not Accessible

1. Verify server is connected (check logs)

2. Check tool naming convention (may differ on Linux)

3. Try alternative MCP server (e.g., Browser MCP instead of Playwright)

4. Restart AI app completely

<!-- section_id: "8bc9293e-803f-4c00-ab2e-0b4bc98639f5" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "ba18bc9a-2878-447b-8c0d-5cda088628a0" -->
## References

- AI App Documentation: Check respective app documentation
- MCP Protocol: https://modelcontextprotocol.io
- GitHub Issues: Platform-specific MCP problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
