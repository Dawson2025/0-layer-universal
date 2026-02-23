# Perplexity MCP Server Setup for Claude Code CLI

**Last Updated**: 2026-01-26

## Overview

The Perplexity MCP server provides web search and research capabilities through the Perplexity AI API.

## Configuration

### Config File Location
`~/.claude.json`

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

### Adding via CLI
You can also add the server using Claude Code's `/mcp` command or config menu.

## Getting an API Key

1. Go to https://www.perplexity.ai/settings/api
2. Add credits (API access requires credits, separate from Pro subscription)
   - Pro subscribers get $5/month in free credits
   - Otherwise, add payment method and purchase credits
3. Create an API Group (required before creating keys)
4. Click **"+ Create key"**
5. Copy the key immediately (shown only once)
6. Keys start with `pplx-`

## Available Tools

| Tool | Description |
|------|-------------|
| `mcp__perplexity__perplexity_ask` | General Q&A with web search |
| `mcp__perplexity__perplexity_search` | Web search with ranked results |
| `mcp__perplexity__perplexity_research` | Deep research with citations |
| `mcp__perplexity__perplexity_reason` | Reasoning tasks with sonar-reasoning-pro model |

## Troubleshooting

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

### MCP Server Not Responding

**Symptom**: Tools timeout or return no response

**Solution**:
1. Run `/mcp` in Claude Code to see server status
2. Click "Reconnect" on the perplexity server
3. If still failing, restart Claude Code entirely

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

## Shared Configuration

This MCP server uses the same API key as Gemini CLI. If you update the key, update both:
- `~/.claude.json` (Claude Code CLI)
- `~/.gemini/settings.json` (Gemini CLI)

## Related

- Canvas MCP: `../sub_layer_0_10_canvas-mcp/`
- Gemini CLI Perplexity setup: `../../sub_layer_0_09_gemini_cli/sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/sub_layer_0_10_perplexity-mcp/`
