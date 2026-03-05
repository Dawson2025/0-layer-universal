---
resource_id: "1575cd72-f97c-4201-bf79-19b8d8972497"
resource_type: "document"
resource_name: "INSTALL"
---
# Perplexity MCP Server Installation Guide

## Overview
The Perplexity MCP Server is the **official** MCP server from Perplexity AI, providing AI-powered web search and research capabilities directly to your AI coding assistant.

**Repository**: [perplexityai/modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)
**npm Package**: `@perplexity-ai/mcp-server`

---

## Features

- Official Perplexity AI integration (~95% feature parity with web interface)
- Access to all Perplexity models (Sonar, etc.)
- Real-time web search with citations
- Structured research responses
- Same quality as the Perplexity web interface

---

## Prerequisites

### 1. Get Your Perplexity API Key
1. Go to [Perplexity API Settings](https://www.perplexity.ai/settings/api)
2. Create or log into your Perplexity account
3. Generate a new API key
4. Copy the key (starts with `pplx-`)

### 2. API Pricing Note
- Perplexity API usage is billed separately from Perplexity Pro subscription
- Check current pricing at [Perplexity API Pricing](https://docs.perplexity.ai/guides/pricing)

---

## Installation by OS & Tool

### For Claude Code CLI (Linux/Ubuntu)

**Method 1: Using claude mcp add (Recommended)**
```bash
claude mcp add perplexity -s user -- npx -y @perplexity-ai/mcp-server
```

Then set the environment variable:
```bash
export PERPLEXITY_API_KEY="pplx-your-api-key-here"
```

Or add to your shell profile (`~/.bashrc` or `~/.zshrc`):
```bash
echo 'export PERPLEXITY_API_KEY="pplx-your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Method 2: Manual Configuration**
Add to `~/.claude.json`:
```json
{
  "mcpServers": {
    "perplexity": {
      "command": "npx",
      "args": ["-y", "@perplexity-ai/mcp-server"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-api-key-here"
      }
    }
  }
}
```

### For Cursor IDE (Linux/Ubuntu)

Add to Cursor MCP settings:
```json
{
  "mcpServers": {
    "perplexity": {
      "command": "npx",
      "args": ["-y", "@perplexity-ai/mcp-server"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-api-key-here"
      }
    }
  }
}
```

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `PERPLEXITY_API_KEY` | Your Perplexity API key (starts with `pplx-`) | Yes |

---

## Available Tools

The Perplexity MCP server provides:

1. **perplexity_search** - Perform web searches with AI-powered summarization
   - Returns structured responses with citations
   - Supports follow-up questions in context

2. **perplexity_research** - Deep research on complex topics
   - Multi-step research with source verification
   - Comprehensive analysis with citations

---

## Verification

Test your setup:
```bash
# Check MCP server is running
claude mcp list

# Should show perplexity server connected
```

---

## MCP Server vs Web Interface

| Feature | MCP Server | Web Interface |
|---------|------------|---------------|
| Search Quality | Same | Same |
| Models Available | All Sonar models | All models |
| Citations | Yes | Yes |
| Follow-up Context | Yes | Yes |
| Image Generation | No | Yes |
| Collections/Spaces | No | Yes |
| Cost | API billing | Subscription |

The MCP server provides approximately 95% feature parity with the web interface, missing primarily the visual/collection features.

---

## Security Notes

- **Never commit your API key** to version control
- Store the key in environment variables or secure credential storage
- API keys can be revoked in your Perplexity settings if compromised
- API usage is metered and billed - monitor your usage

---

## Troubleshooting

### "401 Unauthorized" Error
- Verify your API key is correct (should start with `pplx-`)
- Check the key hasn't been revoked
- Ensure you have API access enabled on your account

### Server Won't Start
- Ensure Node.js is installed (`node --version`)
- Check the environment variable is set: `echo $PERPLEXITY_API_KEY`
- Try running manually: `PERPLEXITY_API_KEY=your-key npx @perplexity-ai/mcp-server`

### Rate Limiting
- Perplexity API has rate limits
- If you hit limits, wait and retry
- Consider upgrading your API plan for higher limits

---

## Related Documentation

- [Perplexity API Documentation](https://docs.perplexity.ai/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
