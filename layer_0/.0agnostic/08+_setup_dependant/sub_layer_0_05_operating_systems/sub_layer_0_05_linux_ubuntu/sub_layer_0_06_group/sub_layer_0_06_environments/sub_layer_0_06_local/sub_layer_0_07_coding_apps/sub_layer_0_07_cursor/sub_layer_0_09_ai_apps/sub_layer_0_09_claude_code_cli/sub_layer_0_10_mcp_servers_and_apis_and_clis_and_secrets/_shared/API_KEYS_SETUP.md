# MCP Servers API Keys Setup Guide

This document explains how to securely manage API keys for MCP servers without exposing them in version control.

---

## Required API Keys

### 1. TAVILY_API_KEY
**Service:** Tavily AI Search API
**Purpose:** Web search capabilities for AI agents

**How to obtain:**
1. Visit [https://tavily.com](https://tavily.com)
2. Sign up for an account
3. Navigate to your dashboard
4. Copy your API key from the API Keys section

### 2. CONTEXT7_API_KEY
**Service:** Context7 MCP Server
**Purpose:** Library documentation and code context retrieval

**How to obtain:**
1. Visit [https://context7.com](https://context7.com) or the Context7 GitHub repository
2. Follow the registration/API key generation process
3. Copy your API key

### 3. CONTEXT7_API_URL
**Service:** Context7 API Endpoint
**Purpose:** Base URL for Context7 API requests

**Default value:** Usually provided during Context7 setup (e.g., `https://api.context7.com`)

---

## Secure Storage Methods

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

### Method 2: Local Config Files

Use the template pattern with local overrides:

1. **config.template.json** - Tracked by git, shows structure with placeholders
2. **config.local.json** - NOT tracked by git, contains actual keys

---

## Template Pattern Explanation

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

### Files Overview

| File | Git Status | Purpose |
|------|------------|---------|
| `config.template.json` | Tracked | Shows required structure, uses `${VAR}` placeholders |
| `config.local.json` | Ignored | Your actual configuration with real keys |
| `.secrets/` | Ignored | Directory for any secret files |

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

## Security Best Practices

1. **Never commit secrets** - Always verify `.gitignore` is working
2. **Use environment variables** - Preferred for production and CI/CD
3. **Restrict file permissions** - Use `chmod 600` for secret files
4. **Rotate keys regularly** - Update keys periodically
5. **Use different keys per environment** - Dev, staging, production should have separate keys
6. **Audit access** - Check who has access to your API dashboards

---

## Verification

### Check Environment Variables
```bash
# Verify keys are set (shows if set, not the actual value)
echo "TAVILY_API_KEY: ${TAVILY_API_KEY:+SET}"
echo "CONTEXT7_API_KEY: ${CONTEXT7_API_KEY:+SET}"
echo "CONTEXT7_API_URL: ${CONTEXT7_API_URL:+SET}"
```

### Check Git Status
```bash
# Ensure local config is not tracked
git status --ignored | grep -E "config\.local|\.secrets"
```

---

## Troubleshooting

### Keys Not Loading
- Ensure you've sourced your shell profile: `source ~/.bashrc`
- Check for typos in variable names
- Verify file permissions on secrets files

### Git Tracking Local Files
- Verify `.gitignore` entries are correct
- If already tracked, remove from git: `git rm --cached config.local.json`

### API Key Invalid
- Verify the key is copied correctly (no extra spaces)
- Check if the key has expired or been revoked
- Ensure you're using the correct key for the environment
