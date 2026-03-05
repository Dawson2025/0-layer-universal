---
resource_id: "10a69b32-e214-4005-8ce8-c44570ffbcb7"
resource_type: "document"
resource_name: "perplexity-mcp-setup"
---
# Perplexity MCP Server Setup for Claude Code CLI

**Last Updated**: 2026-01-26

<!-- section_id: "23fe880d-5f90-4709-a1fa-e36988ffd550" -->
## Overview

The Perplexity MCP server provides web search and research capabilities through the Perplexity AI API.

<!-- section_id: "2c6e7784-cd0a-4579-9b2c-3072e01ded0d" -->
## Configuration

<!-- section_id: "e0622301-3afb-4dec-a056-6fb684facc99" -->
### Config File Location
`~/.claude.json`

<!-- section_id: "fd3768a4-07de-4f36-8489-2d2b51104286" -->
### Configuration Block
```json
{
  "mcpServers": {
    "perplexity": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@perplexity-ai/mcp-server"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-YOUR_API_KEY_HERE"
      }
    }
  }
}
```

<!-- section_id: "69b3f020-6356-4030-a116-e5cfc42f8c73" -->
### Adding via CLI
You can also add the server using Claude Code's `/mcp` command or config menu.

<!-- section_id: "b4f3bd5d-74b7-43f5-a660-d8a64eb6b7b4" -->
## Getting an API Key

1. Go to https://www.perplexity.ai/settings/api
2. Add credits (API access requires credits, separate from Pro subscription)
   - Pro subscribers get $5/month in free credits
   - Otherwise, add payment method and purchase credits
3. Create an API Group (required before creating keys)
4. Click **"+ Create key"**
5. Copy the key immediately (shown only once)
6. Keys start with `pplx-`

<!-- section_id: "37ae4ee8-2d08-4d0f-a0da-862588587d34" -->
## Available Tools

| Tool | Description |
|------|-------------|
| `mcp__perplexity__perplexity_ask` | General Q&A with web search |
| `mcp__perplexity__perplexity_search` | Web search with ranked results |
| `mcp__perplexity__perplexity_research` | Deep research with citations |
| `mcp__perplexity__perplexity_reason` | Reasoning tasks with sonar-reasoning-pro model |

<!-- section_id: "e6885ee7-85e8-4c78-8171-77a0cc50694d" -->
## Troubleshooting

<!-- section_id: "a3b20513-917b-4fe9-8a91-ee06776e3946" -->
### 401 Unauthorized Error

**Symptom**: API calls return `401 Authorization Required` with Cloudflare HTML

**Causes**:
1. **Credits exhausted** - Most common cause
2. **API key revoked or expired**
3. **Invalid API key format**

**Solution**:
1. Check your credit balance at https://www.perplexity.ai/settings/api
2. Add more credits if balance is $0
3. Verify the API key is correct and starts with `pplx-`
4. Regenerate key if necessary

**Important**: When credits run out, the API returns 401 (not a quota error). Once you add credits, the same key works again immediately.

<!-- section_id: "16f6d322-b028-46fe-a313-97335b232147" -->
### MCP Server Not Responding

**Symptom**: Tools timeout or return no response

**Solution**:
1. Run `/mcp` in Claude Code to see server status
2. Click "Reconnect" on the perplexity server
3. If still failing, restart Claude Code entirely

<!-- section_id: "75c2595e-8579-4e41-a709-d28bd04daf7b" -->
### Multiple Server Instances

**Symptom**: Inconsistent behavior, some queries work and others fail

**Cause**: Multiple MCP server processes running (e.g., one from Gemini CLI, one from Claude Code)

**Solution**:
```bash
# Check running processes
ps aux | grep perplexity

# Kill stale processes if needed
kill <PID>

# Restart Claude Code
```

<!-- section_id: "16112d89-e82c-4d08-950a-48d7f738d5d0" -->
## Testing

Test the API key directly:
```bash
curl -X POST "https://api.perplexity.ai/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "sonar", "messages": [{"role": "user", "content": "Hello"}]}'
```

Expected: JSON response with completion
Error: HTML with "401 Authorization Required" = invalid key or no credits

<!-- section_id: "6dc4f892-d995-413b-94b8-c081da128d0e" -->
## Shared Configuration

This MCP server uses the same API key as Gemini CLI. If you update the key, update both:
- `~/.claude.json` (Claude Code CLI)
- `~/.gemini/settings.json` (Gemini CLI)

<!-- section_id: "8c6e0086-4083-44d5-a68e-e10e5bcec3fb" -->
## Related

- Canvas MCP: `../sub_layer_0_10_canvas-mcp/`
- Gemini CLI Perplexity setup: `../../sub_layer_0_09_gemini_cli/sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/sub_layer_0_10_perplexity-mcp/`
