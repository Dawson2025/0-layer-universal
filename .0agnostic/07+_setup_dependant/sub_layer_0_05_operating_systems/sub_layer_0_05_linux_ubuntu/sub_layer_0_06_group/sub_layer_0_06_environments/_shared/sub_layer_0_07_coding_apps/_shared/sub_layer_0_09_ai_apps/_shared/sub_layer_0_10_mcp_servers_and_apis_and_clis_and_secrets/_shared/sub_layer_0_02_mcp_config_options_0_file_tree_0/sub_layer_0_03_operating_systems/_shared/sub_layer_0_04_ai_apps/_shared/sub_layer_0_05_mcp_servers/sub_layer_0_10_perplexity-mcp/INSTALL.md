---
resource_id: "1575cd72-f97c-4201-bf79-19b8d8972497"
resource_type: "document"
resource_name: "INSTALL"
---
# Perplexity MCP Server Installation Guide

<!-- section_id: "eafa455b-afdb-42e9-80d9-da9f738aa620" -->
## Overview
The Perplexity MCP Server is the **official** MCP server from Perplexity AI, providing AI-powered web search and research capabilities directly to your AI coding assistant.

**Repository**: [perplexityai/modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)
**npm Package**: `@perplexity-ai/mcp-server`

---

<!-- section_id: "91a63ad4-e01a-498a-b995-d86d9d87512e" -->
## Features

- Official Perplexity AI integration (~95% feature parity with web interface)
- Access to all Perplexity models (Sonar, etc.)
- Real-time web search with citations
- Structured research responses
- Same quality as the Perplexity web interface

---

<!-- section_id: "8c58193a-06fe-44b9-9a7f-a5e753711407" -->
## Prerequisites

<!-- section_id: "141be3b7-85fa-40c3-a8f8-d604a0b62454" -->
### 1. Get Your Perplexity API Key
1. Go to [Perplexity API Settings](https://www.perplexity.ai/settings/api)
2. Create or log into your Perplexity account
3. Generate a new API key
4. Copy the key (starts with `pplx-`)

<!-- section_id: "dc278ebf-763d-4917-ba46-9fd6476a8b7f" -->
### 2. API Pricing Note
- Perplexity API usage is billed separately from Perplexity Pro subscription
- Check current pricing at [Perplexity API Pricing](https://docs.perplexity.ai/guides/pricing)

---

<!-- section_id: "a8093a8b-3cb0-46c3-8ce4-ff0fb1852f9e" -->
## Installation by OS & Tool

<!-- section_id: "bd0f6b01-cd9c-498b-a136-84710233044a" -->
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

<!-- section_id: "fc8194a1-e73a-46d4-8e29-1bfb7fc614f4" -->
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

<!-- section_id: "d3718d95-6222-4244-a9c2-ee6313a5b5b7" -->
## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `PERPLEXITY_API_KEY` | Your Perplexity API key (starts with `pplx-`) | Yes |

---

<!-- section_id: "9b3fa3cc-2a87-475d-b034-00a53642ff11" -->
## Available Tools

The Perplexity MCP server provides:

1. **perplexity_search** - Perform web searches with AI-powered summarization
   - Returns structured responses with citations
   - Supports follow-up questions in context

2. **perplexity_research** - Deep research on complex topics
   - Multi-step research with source verification
   - Comprehensive analysis with citations

---

<!-- section_id: "2cd0f0bc-f8cc-47d7-bca3-2a2596798abf" -->
## Verification

Test your setup:
```bash
# Check MCP server is running
claude mcp list

# Should show perplexity server connected
```

---

<!-- section_id: "c4388920-193d-43b8-9cdf-40d3f7710c1d" -->
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

<!-- section_id: "7300e4c1-e0ab-45b2-81c5-b7c54b0052b4" -->
## Security Notes

- **Never commit your API key** to version control
- Store the key in environment variables or secure credential storage
- API keys can be revoked in your Perplexity settings if compromised
- API usage is metered and billed - monitor your usage

---

<!-- section_id: "613959dd-4bee-454d-8df5-2994627ea41e" -->
## Troubleshooting

<!-- section_id: "728948f5-5098-4d6d-b33f-b79f98d6acb0" -->
### "401 Unauthorized" Error
- Verify your API key is correct (should start with `pplx-`)
- Check the key hasn't been revoked
- Ensure you have API access enabled on your account

<!-- section_id: "8888ed81-f49a-4e8f-885e-bf741740a240" -->
### Server Won't Start
- Ensure Node.js is installed (`node --version`)
- Check the environment variable is set: `echo $PERPLEXITY_API_KEY`
- Try running manually: `PERPLEXITY_API_KEY=your-key npx @perplexity-ai/mcp-server`

<!-- section_id: "011dba56-6195-4aaf-80e9-6ab2e8154a0c" -->
### Rate Limiting
- Perplexity API has rate limits
- If you hit limits, wait and retry
- Consider upgrading your API plan for higher limits

---

<!-- section_id: "6216c9fd-d32c-48a2-81d6-1ee2a9983324" -->
## Related Documentation

- [Perplexity API Documentation](https://docs.perplexity.ai/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
