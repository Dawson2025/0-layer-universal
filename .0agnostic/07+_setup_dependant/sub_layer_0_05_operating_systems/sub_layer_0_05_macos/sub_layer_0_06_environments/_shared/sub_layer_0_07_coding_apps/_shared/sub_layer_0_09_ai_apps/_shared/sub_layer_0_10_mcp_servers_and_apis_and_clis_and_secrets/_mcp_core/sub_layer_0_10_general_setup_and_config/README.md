---
resource_id: "1d9a1d9e-3903-43c4-8c37-4d23a27afdb1"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Core Issues - General Setup and Configuration

This directory documents **core MCP server issues** that affect multiple MCP servers across different configurations.

<!-- section_id: "9f053dcc-e6cf-4c64-83bc-d4ac8cb124e4" -->
## Environment
- **OS**: All operating systems (_shared)
- **Environment**: All environments (_shared)
- **Coding App**: All coding apps (_shared)
- **AI App**: All AI apps (_shared)
- **Scope**: Core MCP issues affecting multiple servers

<!-- section_id: "1670e281-d594-47f2-bcee-1e7f0b6d78e5" -->
## Common MCP Server Issues

<!-- section_id: "29dc9e9f-109e-4e02-b427-6342d8f9177f" -->
### 1. Tool Exposure Issues

**Issue**: MCP server connects successfully but tools are NOT exposed to the AI agent

**Symptoms**:
- Server shows as "Connected" in AI app settings
- Server logs show successful initialization
- Tools with prefix `mcp__<server>__*` are NOT available to AI
- AI says "I don't have access to that tool"

**Affected platforms**:
- Cursor IDE on Linux, Windows, WSL (versions 2.0.77+)
- May affect other AI apps with MCP integration

**Root cause**:
- AI app fails to expose server tools to the agent
- This is an AI app bug, NOT an MCP server bug
- Server-side everything works correctly

**Solutions**:
1. **Verify tools are supposed to be exposed**:
   - Check MCP server documentation for expected tool names
   - Verify server initialization logs show tools loaded

2. **Try alternative MCP servers**:
   - If using `playwright-mcp`, try `@agent-infra/mcp-server-browser` instead
   - Browser-mcp works reliably when Playwright MCP fails

3. **Check AI app version**:
   - Update to latest version (may fix the bug)
   - Or downgrade to version before the bug was introduced

4. **Report to AI app developers**:
   - This is an AI app issue, not MCP server issue
   - Provide detailed reproduction steps

<!-- section_id: "9230e179-e8d2-45fd-8c4c-f36f1b56b185" -->
### 2. Environment Variable Issues

**Issue**: MCP server cannot access required environment variables

**Symptoms**:
- Server fails to start
- Errors about missing API keys or configuration
- "Environment variable X not found" errors

**Common causes**:
- AI app doesn't inherit shell environment
- `.env` files not loaded
- Variables defined in shell rc files not available

**Solutions**:

1. **Set env vars in MCP config**:
   ```json
   {
     "mcpServers": {
       "my-server": {
         "command": "node",
         "args": ["server.js"],
         "env": {
           "API_KEY": "your-api-key-here",
           "OTHER_VAR": "value"
         }
       }
     }
   }
   ```

2. **Load from .env file** (if supported):
   ```json
   {
     "mcpServers": {
       "my-server": {
         "command": "node",
         "args": ["-r", "dotenv/config", "server.js"],
         "env": {
           "DOTENV_CONFIG_PATH": "/path/to/.env"
         }
       }
     }
   }
   ```

3. **Use absolute paths for env files**:
   - Relative paths may not work
   - Always use full absolute paths

<!-- section_id: "6a51316e-3f55-4a48-ba95-795aae3def0e" -->
### 3. Node.js / NVM Path Issues

**Issue**: MCP server cannot find Node.js or specific Node version from NVM

**Symptoms**:
- "node: command not found"
- "npm: command not found"
- Server uses system Node instead of NVM version

**Common causes**:
- AI app doesn't source NVM initialization scripts
- PATH doesn't include NVM directories
- Interactive shell initialization not run

**Solutions**:

1. **Use bash wrapper for NVM** (Linux/macOS/WSL):
   ```json
   {
     "mcpServers": {
       "my-server": {
         "command": "bash",
         "args": [
           "-i",
           "-c",
           "npx my-mcp-server"
         ]
       }
     }
   }
   ```

2. **Use absolute path to Node**:
   ```json
   {
     "mcpServers": {
       "my-server": {
         "command": "/home/user/.nvm/versions/node/v20.0.0/bin/node",
         "args": ["server.js"]
       }
     }
   }
   ```

3. **Set PATH explicitly**:
   ```json
   {
     "mcpServers": {
       "my-server": {
         "command": "node",
         "args": ["server.js"],
         "env": {
           "PATH": "/home/user/.nvm/versions/node/v20.0.0/bin:${PATH}"
         }
       }
     }
   }
   ```

<!-- section_id: "0ea4111f-910c-46f8-a1cf-0a0ceb45c486" -->
### 4. Server Timeout and Connection Issues

**Issue**: MCP server times out or fails to connect

**Symptoms**:
- "Connection timeout" errors
- Server appears to hang during startup
- Intermittent connection failures

**Common causes**:
- Server initialization takes too long
- Network/firewall blocking connections
- Server crashes during startup

**Solutions**:

1. **Increase timeout** (if AI app supports it):
   ```json
   {
     "mcpServers": {
       "my-server": {
         "command": "node",
         "args": ["server.js"],
         "timeout": 30000
       }
     }
   }
   ```

2. **Check server logs**:
   - Look for startup errors
   - Verify server actually starts successfully
   - Check for missing dependencies

3. **Test server independently**:
   - Run server command manually in terminal
   - Verify it starts without errors
   - Check it responds to test requests

<!-- section_id: "fb249d34-c384-49a3-8ea4-1bdca371bbc9" -->
### 5. Configuration File Syntax Issues

**Issue**: MCP configuration file has syntax errors

**Symptoms**:
- MCP servers don't load at all
- AI app shows parsing errors
- Some servers load, others don't

**Common causes**:
- Invalid JSON syntax (trailing commas, missing quotes)
- Incorrect escaping in paths (especially Windows)
- Missing required fields

**Solutions**:

1. **Validate JSON**:
   ```bash
   # Use a JSON validator
   cat config.json | python -m json.tool
   # Or use online validator
   ```

2. **Common syntax errors**:
   ```json
   // ❌ WRONG - trailing comma
   {
     "mcpServers": {
       "server1": {...},
       "server2": {...},  // <- trailing comma breaks JSON
     }
   }

   // ✅ CORRECT - no trailing comma
   {
     "mcpServers": {
       "server1": {...},
       "server2": {...}
     }
   }
   ```

3. **Escape backslashes in Windows paths**:
   ```json
   // ❌ WRONG
   "command": "C:\Program Files\nodejs\node.exe"

   // ✅ CORRECT
   "command": "C:\\Program Files\\nodejs\\node.exe"
   // OR
   "command": "C:/Program Files/nodejs/node.exe"
   ```

<!-- section_id: "6b7f7efa-d462-487a-8992-afcdb6c31cba" -->
## Testing MCP Server Setup

<!-- section_id: "f030198f-3fc8-407a-96d0-ff577fc0f9a2" -->
### Verification Checklist

- [ ] Server appears as "Connected" in AI app settings
- [ ] Server logs show successful initialization (if logs available)
- [ ] Tools are exposed to AI agent (test by asking AI to use a tool)
- [ ] Environment variables are accessible (check server logs)
- [ ] No timeout or connection errors
- [ ] Configuration JSON is valid

<!-- section_id: "3910f76e-71d3-4730-939e-a28beea597bd" -->
### Debugging Steps

1. **Check AI app settings**: Verify server is configured and connected
2. **Check server logs**: Look for startup errors or warnings
3. **Test manually**: Run server command in terminal to verify it works
4. **Simplify config**: Start with minimal configuration, add complexity gradually
5. **Check permissions**: Ensure server executable has correct permissions
6. **Verify paths**: All paths (commands, files, directories) must be absolute or correct relative paths

<!-- section_id: "ba6b9f91-fa7a-4d52-81a9-519847b16046" -->
## Links to Detailed Documentation

For server-specific issues, see:
- **0.10_mcp_servers_and_apis_and_secrets/browser-mcp/general_setup_and_config/**
- **0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/general_setup_and_config/**
- **0.10_mcp_servers_and_apis_and_secrets/chrome-devtools-mcp/general_setup_and_config/**
- **sub_layer_0_10_mcp_servers_and_tools_setup/** for comprehensive MCP documentation

For AI app-specific issues, see:
- **0.09_ai_apps/claude_code_cli/** for Claude Code CLI
- **0.09_ai_apps/cursor_agent/** for Cursor Agent
- **sub_layer_0_09_ai_apps_tools_setup/** for detailed AI app documentation

For OS-specific issues, see:
- **0.05_operating_systems/linux_ubuntu/** for Linux-specific MCP issues
- **0.05_operating_systems/macos/** for macOS-specific MCP issues
- **0.05_operating_systems/windows/** for Windows-specific MCP issues
- **0.05_operating_systems/wsl/** for WSL-specific MCP issues
