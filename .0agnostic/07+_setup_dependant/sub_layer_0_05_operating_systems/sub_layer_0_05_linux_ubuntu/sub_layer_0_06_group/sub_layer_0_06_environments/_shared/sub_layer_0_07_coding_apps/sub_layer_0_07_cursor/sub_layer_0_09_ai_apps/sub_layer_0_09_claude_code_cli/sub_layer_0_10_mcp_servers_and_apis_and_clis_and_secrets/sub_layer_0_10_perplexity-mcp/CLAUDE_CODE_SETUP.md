---
resource_id: "9c8d52db-3f74-4ea8-930f-45f4c5e1fda0"
resource_type: "document"
resource_name: "CLAUDE_CODE_SETUP"
---
# Perplexity MCP Setup for Claude Code CLI in Cursor (Linux Ubuntu)

<!-- section_id: "513d0b16-fde7-4421-94fa-e536a6f24780" -->
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

<!-- section_id: "54609548-3671-40f6-b417-4ee3cb1fa3e4" -->
## Required: Configure Your Perplexity API Key

You need to replace `PLACEHOLDER_SET_IN_ENV` with your actual Perplexity API key.

<!-- section_id: "d4f9c470-2176-4494-9b9a-f562b2657c54" -->
### Option 1: Edit the config file directly
```bash
# Open the config file
nano ~/.claude.json

# Find the line with PERPLEXITY_API_KEY and replace PLACEHOLDER_SET_IN_ENV with your actual key
```

<!-- section_id: "f633050f-d6e7-40c3-bc49-79a8c678466b" -->
### Option 2: Use claude mcp command
```bash
# Remove the placeholder config
claude mcp remove perplexity -s user

# Re-add with your actual key
claude mcp add perplexity -s user \
  -e PERPLEXITY_API_KEY=pplx-YOUR_ACTUAL_KEY_HERE \
  -- npx -y @perplexity-ai/mcp-server
```

<!-- section_id: "e2f247bb-dc96-4b57-998c-5b1f559e9b26" -->
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

<!-- section_id: "bcc5a679-d330-47b6-b252-7471d9af8381" -->
## Getting Your Perplexity API Key

1. Go to https://www.perplexity.ai/settings/api
2. Log into your Perplexity account (or create one)
3. Generate a new API key
4. Copy the key (starts with `pplx-`)

**Note**: API usage is billed separately from Perplexity Pro subscription.

---

<!-- section_id: "38a0a6e8-8f92-4f11-a921-6fc8105621d4" -->
## Verify Setup

After configuring your key:

```bash
# Check MCP servers
claude mcp list

# Expected output:
# perplexity: npx -y @perplexity-ai/mcp-server - ✓ Connected
```

---

<!-- section_id: "2e6d9997-bb0f-4719-95a7-f3ece5d37a3d" -->
## Available Perplexity Tools

Once connected, you'll have access to:
- **perplexity_search** - Web search with AI summarization and citations
- **perplexity_research** - Deep research on complex topics

---

<!-- section_id: "b756da6c-9ac7-4f65-b3ec-dc037ec6b78a" -->
## Usage Examples

In Claude Code CLI, you can now use Perplexity for research:

```
"Search Perplexity for the latest Canvas LMS API changes"
"Use Perplexity to research best practices for MCP server development"
"Ask Perplexity about Node.js 22 features"
```

---

<!-- section_id: "b77f9d8e-ea9a-4495-be07-b7aae9c4064a" -->
## Troubleshooting

<!-- section_id: "b0557070-9199-4ecb-947e-d66c7f558e4d" -->
### Server shows "Disconnected" or "Error"
1. Verify your API key is correct (should start with `pplx-`)
2. Check you have API access enabled on your Perplexity account
3. Try regenerating your API key

<!-- section_id: "fd7e28a4-93d0-4bc3-a4da-220671419b9e" -->
### "401 Unauthorized"
- Your API key may be invalid or revoked
- Generate a new key at https://www.perplexity.ai/settings/api

<!-- section_id: "30ed7a5d-a785-4c9b-809a-21113ed76f2e" -->
### Rate Limiting
- Perplexity API has usage limits
- Wait a few minutes and retry
- Consider upgrading your API plan

---

<!-- section_id: "94f44b2a-a4a9-4b72-bfb9-79a1228f3ce8" -->
## Related Files

- Main install guide: `../../../_shared/0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/_shared/0.04_ai_apps/_shared/0.05_mcp_servers/perplexity-mcp/INSTALL.md`
- Claude config: `~/.claude.json`
