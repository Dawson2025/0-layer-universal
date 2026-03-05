---
resource_id: "9c8d52db-3f74-4ea8-930f-45f4c5e1fda0"
resource_type: "document"
resource_name: "CLAUDE_CODE_SETUP"
---
# Perplexity MCP Setup for Claude Code CLI in Cursor (Linux Ubuntu)

## Current Setup Status

The Perplexity MCP server has been added to your Claude Code CLI user configuration.

**Configuration file**: `~/.claude.json`

**Current configuration**:
```json
"mcpServers": {
  "perplexity": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@perplexity-ai/mcp-server"],
    "env": {
      "PERPLEXITY_API_KEY": "PLACEHOLDER_SET_IN_ENV"
    }
  }
}
```

---

## Required: Configure Your Perplexity API Key

You need to replace `PLACEHOLDER_SET_IN_ENV` with your actual Perplexity API key.

### Option 1: Edit the config file directly
```bash
# Open the config file
nano ~/.claude.json

# Find the line with PERPLEXITY_API_KEY and replace PLACEHOLDER_SET_IN_ENV with your actual key
```

### Option 2: Use claude mcp command
```bash
# Remove the placeholder config
claude mcp remove perplexity -s user

# Re-add with your actual key
claude mcp add perplexity -s user \
  -e PERPLEXITY_API_KEY=pplx-YOUR_ACTUAL_KEY_HERE \
  -- npx -y @perplexity-ai/mcp-server
```

### Option 3: Use environment variables (Recommended for security)

Set in your shell profile (`~/.bashrc` or `~/.zshrc`):
```bash
export PERPLEXITY_API_KEY="pplx-YOUR_ACTUAL_KEY_HERE"
```

Then update the config to reference the env var:
```json
"env": {
  "PERPLEXITY_API_KEY": "${PERPLEXITY_API_KEY}"
}
```

---

## Getting Your Perplexity API Key

1. Go to https://www.perplexity.ai/settings/api
2. Log into your Perplexity account (or create one)
3. Generate a new API key
4. Copy the key (starts with `pplx-`)

**Note**: API usage is billed separately from Perplexity Pro subscription.

---

## Verify Setup

After configuring your key:

```bash
# Check MCP servers
claude mcp list

# Expected output:
# perplexity: npx -y @perplexity-ai/mcp-server - ✓ Connected
```

---

## Available Perplexity Tools

Once connected, you'll have access to:
- **perplexity_search** - Web search with AI summarization and citations
- **perplexity_research** - Deep research on complex topics

---

## Usage Examples

In Claude Code CLI, you can now use Perplexity for research:

```
"Search Perplexity for the latest Canvas LMS API changes"
"Use Perplexity to research best practices for MCP server development"
"Ask Perplexity about Node.js 22 features"
```

---

## Troubleshooting

### Server shows "Disconnected" or "Error"
1. Verify your API key is correct (should start with `pplx-`)
2. Check you have API access enabled on your Perplexity account
3. Try regenerating your API key

### "401 Unauthorized"
- Your API key may be invalid or revoked
- Generate a new key at https://www.perplexity.ai/settings/api

### Rate Limiting
- Perplexity API has usage limits
- Wait a few minutes and retry
- Consider upgrading your API plan

---

## Related Files

- Main install guide: `../../../_shared/0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/_shared/0.04_ai_apps/_shared/0.05_mcp_servers/perplexity-mcp/INSTALL.md`
- Claude config: `~/.claude.json`
