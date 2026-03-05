---
resource_id: "5f5e5542-1f30-4a6a-ae1d-95e806623b2a"
resource_type: "document"
resource_name: "TROUBLESHOOTING"
---
# Tavily MCP Troubleshooting Guide

This guide covers common issues when using the Tavily MCP server with Claude Code CLI on Linux Ubuntu.

---

## API Key Issues

### Problem: "Invalid API Key" or "Unauthorized" Error

**Symptoms:**
- Server fails to start with authentication errors
- Searches return 401/403 status codes
- Error message mentions invalid credentials

**Solutions:**

1. **Verify API Key Format**
   ```bash
   # Check if TAVILY_API_KEY is set
   echo $TAVILY_API_KEY

   # Should output something like: tvly-xxxxxxxxxxxxxxxxxxxxxxxx
   ```

2. **Ensure Proper Export**
   ```bash
   # Add to ~/.bashrc or ~/.zshrc
   export TAVILY_API_KEY="tvly-your-actual-key-here"

   # Reload shell configuration
   source ~/.bashrc
   ```

3. **Check for Whitespace**
   ```bash
   # Verify no trailing whitespace
   echo -n "$TAVILY_API_KEY" | wc -c
   # Should match expected key length (typically 32+ characters)
   ```

4. **Verify Key in Tavily Dashboard**
   - Log into [https://tavily.com](https://tavily.com)
   - Navigate to API Keys section
   - Regenerate key if necessary

---

### Problem: API Key Not Found by MCP Server

**Symptoms:**
- Server starts but searches fail
- "TAVILY_API_KEY environment variable not set" error

**Solutions:**

1. **Check MCP Configuration**
   ```json
   {
     "mcpServers": {
       "tavily": {
         "command": "npx",
         "args": ["-y", "@tavily/mcp"],
         "env": {
           "TAVILY_API_KEY": "${TAVILY_API_KEY}"
         }
       }
     }
   }
   ```

2. **Use Direct Key (Not Recommended for Shared Configs)**
   ```json
   {
     "mcpServers": {
       "tavily": {
         "command": "npx",
         "args": ["-y", "@tavily/mcp"],
         "env": {
           "TAVILY_API_KEY": "tvly-your-key-here"
         }
       }
     }
   }
   ```

3. **Restart Claude Code CLI**
   ```bash
   # Environment changes require CLI restart
   claude  # Restart the CLI
   ```

---

## Rate Limiting

### Problem: "Rate Limit Exceeded" Error

**Symptoms:**
- Error code 429
- "Too many requests" message
- Searches stop working temporarily

**Solutions:**

1. **Check Your Tier Limits**
   | Tier | Rate Limit |
   |------|------------|
   | Free | 10 requests/minute |
   | Basic | 100 requests/minute |
   | Pro | 500 requests/minute |

2. **Implement Request Spacing**
   - Avoid rapid consecutive searches
   - Wait at least 6 seconds between searches on Free tier

3. **Monitor Usage**
   - Check your usage at [https://tavily.com/dashboard](https://tavily.com/dashboard)
   - Consider upgrading if consistently hitting limits

4. **Use Search Depth Strategically**
   - `basic` search uses fewer API credits
   - Reserve `advanced` for complex queries

---

### Problem: Monthly Quota Exhausted

**Symptoms:**
- All searches fail with quota errors
- Dashboard shows 100% usage

**Solutions:**

1. **Check Monthly Usage**
   - Log into Tavily dashboard
   - View current month's usage statistics

2. **Wait for Reset**
   - Free tier resets monthly
   - Check your billing cycle date

3. **Upgrade Plan**
   - Consider Basic tier for 10x more searches
   - Evaluate actual usage patterns first

---

## Search Result Problems

### Problem: Empty or No Results

**Symptoms:**
- Searches return empty arrays
- "No results found" for valid queries

**Solutions:**

1. **Simplify Query**
   ```
   # Too specific (may fail)
   "exact phrase that nobody wrote anywhere"

   # Better approach
   "general topic keywords"
   ```

2. **Check Domain Filters**
   - Remove `include_domains` to search all sites
   - Verify included domains actually have content

3. **Adjust Search Depth**
   - Try `advanced` depth for better coverage
   - `basic` may miss some sources

---

### Problem: Irrelevant Results

**Symptoms:**
- Results don't match query intent
- Low-quality sources returned

**Solutions:**

1. **Use Domain Filtering**
   ```json
   {
     "include_domains": ["github.com", "stackoverflow.com", "docs.python.org"]
   }
   ```

2. **Exclude Unwanted Sources**
   ```json
   {
     "exclude_domains": ["pinterest.com", "quora.com"]
   }
   ```

3. **Refine Query Terms**
   - Add specific technical terms
   - Include year for recent information

---

### Problem: Outdated Results

**Symptoms:**
- Search returns old articles
- Missing recent developments

**Solutions:**

1. **Use News Search for Recent Content**
   - `tavily_news_search` prioritizes recent articles
   - Set `days` parameter to limit time range

2. **Add Date Terms to Query**
   ```
   "topic 2024" or "topic latest"
   ```

3. **Use Advanced Search Depth**
   - More comprehensive indexing
   - Better at finding recent content

---

## Connection Issues

### Problem: Server Fails to Start

**Symptoms:**
- MCP server never connects
- Timeout errors

**Solutions:**

1. **Check npx Installation**
   ```bash
   which npx
   npx --version
   ```

2. **Verify Network Access**
   ```bash
   curl -I https://api.tavily.com
   ```

3. **Check Node.js Version**
   ```bash
   node --version
   # Requires Node.js 18+
   ```

4. **Clear npx Cache**
   ```bash
   npx cache clean --force
   ```

---

### Problem: Intermittent Failures

**Symptoms:**
- Sometimes works, sometimes fails
- Random timeout errors

**Solutions:**

1. **Check Network Stability**
   ```bash
   ping api.tavily.com
   ```

2. **Verify DNS Resolution**
   ```bash
   nslookup api.tavily.com
   ```

3. **Check System Resources**
   ```bash
   # Check memory
   free -h

   # Check CPU
   top
   ```

---

## MCP Configuration Issues

### Problem: Tavily Tool Not Available

**Symptoms:**
- `tavily_search` tool not listed
- "Unknown tool" errors

**Solutions:**

1. **Verify MCP Config Location**
   ```bash
   # User-level config
   cat ~/.config/mcp/mcp.json

   # Project-level config
   cat .mcp.json
   ```

2. **Check JSON Syntax**
   ```bash
   # Validate JSON
   cat ~/.config/mcp/mcp.json | python3 -m json.tool
   ```

3. **Restart After Changes**
   - Always restart Claude Code CLI after config changes

---

### Problem: Multiple MCP Server Conflicts

**Symptoms:**
- Tavily works inconsistently
- Other servers affected

**Solutions:**

1. **Check Server Names**
   - Ensure unique names for each server
   - Avoid duplicate entries

2. **Isolate Issue**
   - Temporarily disable other servers
   - Test Tavily alone

---

## Debugging Commands

### Check Environment

```bash
# Verify all relevant environment variables
env | grep -E "(TAVILY|NODE|PATH)"

# Test API key directly
curl -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -d '{"api_key": "'$TAVILY_API_KEY'", "query": "test"}'
```

### Check MCP Server Logs

```bash
# Run with verbose output
DEBUG=* npx -y @tavily/mcp
```

### Verify Package Installation

```bash
# Check if package can be fetched
npm view @tavily/mcp version
```

---

## Getting Help

If issues persist:

1. **Tavily Support**: Contact via [https://tavily.com/support](https://tavily.com/support)
2. **MCP Issues**: Check [MCP Protocol GitHub](https://github.com/anthropics/model-context-protocol)
3. **Claude Code CLI**: Refer to Anthropic documentation

---

## Quick Reference

| Issue | First Thing to Check |
|-------|---------------------|
| Auth errors | `echo $TAVILY_API_KEY` |
| Rate limits | Dashboard usage stats |
| No results | Remove domain filters |
| Server won't start | `npx --version` |
| Tool not found | MCP config JSON syntax |
