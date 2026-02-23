# Perplexity MCP Server Setup for Gemini CLI

**Last Updated**: 2026-01-26

## Overview

The Perplexity MCP server provides web search and research capabilities through the Perplexity AI API.

## Configuration

### Config File Location
`~/.gemini/settings.json`

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
| `perplexity_ask` | General Q&A with web search |
| `perplexity_search` | Web search with ranked results |
| `perplexity_research` | Deep research with citations |
| `perplexity_reason` | Reasoning tasks with sonar-reasoning-pro model |

## Troubleshooting

### 401 Unauthorized Error

**Symptom**: API calls return `401 Authorization Required`

**Causes**:
1. **Credits exhausted** - Most common cause
2. **API key revoked or expired**
3. **Invalid API key format**

**Solution**:
1. Check your credit balance at https://www.perplexity.ai/settings/api
2. Add more credits if balance is $0
3. Verify the API key is correct and starts with `pplx-`
4. Regenerate key if necessary

**Note**: When credits run out, the API returns 401 (not a quota error). Once you add credits, the same key works again.

### "Tool execution denied by policy" Error

**Symptom**: Gemini CLI shows this error before retrying

**Cause**: Gemini's safety policies may block certain queries

**Solution**: Rephrase the query or use a different approach

### Rate Limiting

**Symptom**: "You have exhausted your capacity on this model"

**Cause**: Too many requests in a short time

**Solution**: Wait for quota reset (usually seconds to minutes)

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

## Related

- Canvas MCP: `../sub_layer_0_10_canvas-mcp/`
- Claude Code CLI setup: `../../sub_layer_0_09_claude_code_cli/sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/`
