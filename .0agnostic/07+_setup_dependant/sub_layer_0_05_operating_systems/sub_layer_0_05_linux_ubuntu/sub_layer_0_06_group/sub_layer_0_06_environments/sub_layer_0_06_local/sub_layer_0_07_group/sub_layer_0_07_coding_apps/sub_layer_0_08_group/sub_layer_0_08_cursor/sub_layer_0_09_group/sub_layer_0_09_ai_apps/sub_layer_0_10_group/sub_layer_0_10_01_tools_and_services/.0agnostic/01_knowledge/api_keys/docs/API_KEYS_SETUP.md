---
resource_id: "893b5967-31aa-46ad-8301-12e7a97d82ab"
resource_type: "knowledge"
resource_name: "API_KEYS_SETUP"
---
# MCP Servers API Keys Setup Guide

This document explains how to securely manage API keys for MCP servers without exposing them in version control.

---

<!-- section_id: "acefee47-bf28-476b-ae07-c3f947776979" -->
## Required API Keys

<!-- section_id: "775b6f10-b249-4c59-b49f-6f41403f5d15" -->
### 1. TAVILY_API_KEY
**Service:** Tavily AI Search API
**Purpose:** Web search capabilities for AI agents

**How to obtain:**
1. Visit [https://tavily.com](https://tavily.com)
2. Sign up for an account
3. Navigate to your dashboard
4. Copy your API key from the API Keys section

<!-- section_id: "289bf9ae-1f24-4f52-a572-b5c4ede22c6f" -->
### 2. CONTEXT7_API_KEY
**Service:** Context7 MCP Server
**Purpose:** Library documentation and code context retrieval

**How to obtain:**
1. Visit [https://context7.com](https://context7.com) or the Context7 GitHub repository
2. Follow the registration/API key generation process
3. Copy your API key

<!-- section_id: "a1c45a44-0391-4b7e-9fa7-f627aa84f75d" -->
### 3. CONTEXT7_API_URL
**Service:** Context7 API Endpoint
**Purpose:** Base URL for Context7 API requests

**Default value:** Usually provided during Context7 setup (e.g., `https://api.context7.com`)

---

<!-- section_id: "329e153c-683d-4f86-82e3-7fc11bfad566" -->
## Secure Storage Methods

<!-- section_id: "6dd78d2d-096f-47a6-8a9f-1da4af2b7422" -->
### Method 1: Environment Variables (Recommended)

#### Option A: Shell Profile (~/.bashrc or ~/.zshrc)
Add to your shell profile:
```bash
# MCP Server API Keys
export TAVILY_API_KEY="your-tavily-api-key-here"
export CONTEXT7_API_KEY="your-context7-api-key-here"
export CONTEXT7_API_URL="https://api.context7.com"
```

Then reload:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

#### Option B: Dedicated Secrets File (.secrets.sh pattern)

1. Create a secrets file (NOT tracked by git):
```bash
# Create in your home directory or project root
touch ~/.secrets/mcp_keys.sh
chmod 600 ~/.secrets/mcp_keys.sh
```

2. Add your keys to `~/.secrets/mcp_keys.sh`:
```bash
#!/bin/bash
# MCP Server API Keys - DO NOT COMMIT THIS FILE

export TAVILY_API_KEY="your-tavily-api-key-here"
export CONTEXT7_API_KEY="your-context7-api-key-here"
export CONTEXT7_API_URL="https://api.context7.com"
```

3. Source in your shell profile:
```bash
# Add to ~/.bashrc or ~/.zshrc
if [ -f ~/.secrets/mcp_keys.sh ]; then
    source ~/.secrets/mcp_keys.sh
fi
```

<!-- section_id: "10c01edf-8a24-478c-8d21-b76df8ece32e" -->
### Method 2: Local Config Files

Use the template pattern with local overrides:

1. **config.template.json** - Tracked by git, shows structure with placeholders
2. **config.local.json** - NOT tracked by git, contains actual keys

---

<!-- section_id: "f56b45eb-9a06-4444-8805-8c0762e3c495" -->
## Template Pattern Explanation

<!-- section_id: "2bd93ac4-bfab-43ed-8f65-d642b3ed51ea" -->
### How It Works

```
config.template.json  (committed to repo)
        |
        v
    Copy & rename
        |
        v
config.local.json    (gitignored, contains real keys)
```

<!-- section_id: "0d4ecccd-8ff7-4d2b-a568-6eb2d1f73176" -->
### Files Overview

| File | Git Status | Purpose |
|------|------------|---------|
| `config.template.json` | Tracked | Shows required structure, uses `${VAR}` placeholders |
| `config.local.json` | Ignored | Your actual configuration with real keys |
| `.secrets/` | Ignored | Directory for any secret files |

<!-- section_id: "84189e89-251b-4ce2-a9b6-a9a595dbdc91" -->
### Setup Steps

1. Copy the template:
```bash
cp config.template.json config.local.json
```

2. Edit `config.local.json` and replace placeholders with actual values:
```json
{
  "tavily": {
    "api_key": "tvly-actual-key-here"
  },
  "context7": {
    "api_key": "ctx7-actual-key-here",
    "api_url": "https://api.context7.com"
  }
}
```

3. Your application reads from `config.local.json` or environment variables

<!-- section_id: "aa6363ab-0b89-4144-96fa-3fc41b11ab57" -->
### Environment Variable Substitution

Some tools support automatic environment variable substitution. The template uses `${VAR_NAME}` syntax:

```json
{
  "tavily": {
    "api_key": "${TAVILY_API_KEY}"
  }
}
```

If your MCP server supports this, you can use the template directly after setting environment variables.

---

<!-- section_id: "30c88b0c-786d-4525-8615-16f0a4c778aa" -->
## Security Best Practices

1. **Never commit secrets** - Always verify `.gitignore` is working
2. **Use environment variables** - Preferred for production and CI/CD
3. **Restrict file permissions** - Use `chmod 600` for secret files
4. **Rotate keys regularly** - Update keys periodically
5. **Use different keys per environment** - Dev, staging, production should have separate keys
6. **Audit access** - Check who has access to your API dashboards

---

<!-- section_id: "b0ab14a6-d4f2-483c-923b-bb689dcfc399" -->
## Verification

<!-- section_id: "195afa73-307f-4a2b-b4b6-ccfbcb2f2b5c" -->
### Check Environment Variables
```bash
# Verify keys are set (shows if set, not the actual value)
echo "TAVILY_API_KEY: ${TAVILY_API_KEY:+SET}"
echo "CONTEXT7_API_KEY: ${CONTEXT7_API_KEY:+SET}"
echo "CONTEXT7_API_URL: ${CONTEXT7_API_URL:+SET}"
```

<!-- section_id: "c46cce71-42f1-4dbc-8273-c652bd217fe8" -->
### Check Git Status
```bash
# Ensure local config is not tracked
git status --ignored | grep -E "config\.local|\.secrets"
```

---

<!-- section_id: "f797db85-2885-4e1e-8b01-72807fad0c6f" -->
## Troubleshooting

<!-- section_id: "239ae71e-b486-4781-93a6-5bebe820d963" -->
### Keys Not Loading
- Ensure you've sourced your shell profile: `source ~/.bashrc`
- Check for typos in variable names
- Verify file permissions on secrets files

<!-- section_id: "66243cc6-8f52-4c94-86a7-61bb2c5d7c47" -->
### Git Tracking Local Files
- Verify `.gitignore` entries are correct
- If already tracked, remove from git: `git rm --cached config.local.json`

<!-- section_id: "22de4a37-9cdd-42d9-8dc9-109c780609a8" -->
### API Key Invalid
- Verify the key is copied correctly (no extra spaces)
- Check if the key has expired or been revoked
- Ensure you're using the correct key for the environment
