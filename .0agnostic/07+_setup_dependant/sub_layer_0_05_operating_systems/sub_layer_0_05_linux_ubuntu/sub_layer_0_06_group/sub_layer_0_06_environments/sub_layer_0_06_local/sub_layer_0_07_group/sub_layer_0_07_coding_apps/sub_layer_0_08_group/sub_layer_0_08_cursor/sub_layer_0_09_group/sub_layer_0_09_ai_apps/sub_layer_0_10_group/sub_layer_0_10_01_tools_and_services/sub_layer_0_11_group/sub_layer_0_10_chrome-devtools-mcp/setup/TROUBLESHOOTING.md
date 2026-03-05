---
resource_id: "17ad9741-c425-49be-91fb-dddcb04f172a"
resource_type: "document"
resource_name: "TROUBLESHOOTING"
---
# Chrome DevTools MCP Troubleshooting Guide

This guide covers common issues when using the Chrome DevTools MCP server on Linux/Ubuntu with Claude Code CLI.

## Table of Contents

- [Chrome Connection Issues](#chrome-connection-issues)
- [DevTools Protocol Errors](#devtools-protocol-errors)
- [Port Configuration Problems](#port-configuration-problems)
- [MCP Server Startup Issues](#mcp-server-startup-issues)
- [Permission and Access Issues](#permission-and-access-issues)
- [Diagnostic Commands](#diagnostic-commands)

---

## Chrome Connection Issues

### Error: "Cannot connect to browser"

**Symptoms:**
- MCP server fails to establish connection
- "Connection refused" errors in logs
- Tools return connection timeout errors

**Causes and Solutions:**

1. **Chrome not running with remote debugging enabled**

   ```bash
   # Check if Chrome is running with debugging port
   lsof -i :9222

   # If empty, start Chrome with debugging:
   google-chrome --remote-debugging-port=9222
   ```

2. **Chrome started without the correct flag**

   ```bash
   # Kill existing Chrome instances
   pkill -f google-chrome

   # Restart with remote debugging
   google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
   ```

3. **Wrong URL format in configuration**

   Ensure `--browserUrl` uses the correct format:
   ```json
   "--browserUrl", "http://127.0.0.1:9222"
   ```

   NOT:
   ```json
   "--browserUrl", "ws://127.0.0.1:9222"  // Wrong protocol
   "--browserUrl", "localhost:9222"        // Missing protocol
   ```

### Error: "WebSocket connection failed"

**Symptoms:**
- Initial HTTP connection succeeds but WebSocket upgrade fails
- Intermittent connection drops

**Solutions:**

1. **Verify WebSocket endpoint availability**

   ```bash
   # Get available debugging endpoints
   curl -s http://127.0.0.1:9222/json/version

   # List all available targets
   curl -s http://127.0.0.1:9222/json/list
   ```

2. **Check for WebSocket conflicts**

   Another tool may have an active DevTools connection:
   ```bash
   # Check what's connected to Chrome debugging
   ss -tlnp | grep 9222
   ```

3. **Only one DevTools client per page**

   Close Chrome DevTools GUI if open - only one client can connect to a debugging target at a time.

### Error: "No debugging targets available"

**Symptoms:**
- Connection succeeds but no pages found
- Empty target list

**Solutions:**

1. **Open at least one tab in Chrome**

   ```bash
   # Start Chrome and navigate to a page
   google-chrome --remote-debugging-port=9222 https://example.com
   ```

2. **Check target list**

   ```bash
   curl -s http://127.0.0.1:9222/json/list | jq '.'
   ```

---

## DevTools Protocol Errors

### Error: "Method not found"

**Symptoms:**
- Specific CDP method calls fail
- "Unknown method" or "Method not supported"

**Causes and Solutions:**

1. **Chrome version mismatch**

   Some CDP methods require specific Chrome versions:
   ```bash
   # Check Chrome version
   google-chrome --version

   # Verify CDP protocol version
   curl -s http://127.0.0.1:9222/json/protocol | jq '.version'
   ```

2. **Method requires specific domain to be enabled**

   Many CDP methods require enabling their domain first:
   - Network methods require `Network.enable`
   - DOM methods require `DOM.enable`
   - Console methods require `Runtime.enable`

### Error: "Target closed"

**Symptoms:**
- Commands fail mid-execution
- "Target has been closed" errors

**Solutions:**

1. **Page navigated away or closed**

   Re-attach to a new target after page navigation:
   ```bash
   # Get updated target list
   curl -s http://127.0.0.1:9222/json/list
   ```

2. **Browser crashed or restarted**

   Check if Chrome is still running:
   ```bash
   pgrep -f "google-chrome.*remote-debugging"
   ```

### Error: "Cannot find execution context"

**Symptoms:**
- JavaScript evaluation fails
- Runtime methods return context errors

**Solutions:**

1. **Page not fully loaded**

   Wait for page load before executing JavaScript.

2. **Frame context changed**

   After navigation, execution contexts are invalidated. Re-enable Runtime domain:
   ```
   Runtime.enable
   ```

---

## Port Configuration Problems

### Error: "Port already in use"

**Symptoms:**
- Chrome fails to start with debugging
- "Address already in use" error

**Solutions:**

1. **Find and kill process using port**

   ```bash
   # Find what's using port 9222
   sudo lsof -i :9222

   # Or using ss
   ss -tlnp | grep 9222

   # Kill the process
   kill -9 <PID>
   ```

2. **Use alternative port**

   ```bash
   # Start Chrome on different port
   google-chrome --remote-debugging-port=9223
   ```

   Update MCP configuration:
   ```json
   "--browserUrl", "http://127.0.0.1:9223"
   ```

### Error: "Connection refused on localhost"

**Symptoms:**
- Cannot connect to 127.0.0.1:9222
- Works with explicit IP but not localhost

**Solutions:**

1. **IPv6 vs IPv4 binding issue**

   ```bash
   # Check if bound to IPv4
   ss -tlnp | grep 9222

   # Try explicit IPv4
   curl http://127.0.0.1:9222/json/version

   # Try IPv6
   curl http://[::1]:9222/json/version
   ```

2. **Firewall blocking localhost**

   ```bash
   # Check iptables rules
   sudo iptables -L -n | grep 9222

   # Allow localhost connections
   sudo iptables -A INPUT -i lo -j ACCEPT
   ```

### Port Not Accessible from MCP Server

**Symptoms:**
- Manual curl works but MCP server cannot connect
- Different user contexts

**Solutions:**

1. **Ensure same user context**

   The MCP server runs as the same user that started the AI agent. Verify Chrome is also running as that user.

2. **Check network namespaces**

   In containerized environments, ensure port is accessible:
   ```bash
   # From container/namespace
   curl http://host.docker.internal:9222/json/version
   ```

---

## MCP Server Startup Issues

### Error: "MCP server failed to start"

**Symptoms:**
- AI agent cannot list chrome-devtools tools
- Server process exits immediately

**Solutions:**

1. **Check server logs**

   ```bash
   # View MCP chrome-devtools log
   cat /tmp/mcp-chrome.log

   # Follow log in real-time
   tail -f /tmp/mcp-chrome.log
   ```

2. **Verify npx availability**

   ```bash
   # Check npx path
   which npx

   # Verify it can run chrome-devtools-mcp
   npx -y chrome-devtools-mcp@latest --help
   ```

3. **Check wrapper script**

   ```bash
   # View generated wrapper
   cat ~/.config/mcp/servers/mcp-chrome-devtools-generic.sh

   # Test wrapper directly
   ~/.config/mcp/servers/mcp-chrome-devtools-generic.sh
   ```

### Error: "Package not found" or "npm error"

**Symptoms:**
- npx fails to download chrome-devtools-mcp
- Network or registry errors

**Solutions:**

1. **Clear npm cache**

   ```bash
   npm cache clean --force
   ```

2. **Check npm registry access**

   ```bash
   npm ping
   ```

3. **Install package globally as fallback**

   ```bash
   npm install -g chrome-devtools-mcp
   ```

---

## Permission and Access Issues

### Error: "Permission denied" accessing Chrome

**Symptoms:**
- Cannot start Chrome with debugging
- Sandbox errors

**Solutions:**

1. **Sandbox issues on Linux**

   ```bash
   # Run without sandbox (less secure, for debugging only)
   google-chrome --remote-debugging-port=9222 --no-sandbox
   ```

2. **User data directory permissions**

   ```bash
   # Use a fresh user data directory
   google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug-$(whoami)
   ```

### Error: "Cannot write to log file"

**Symptoms:**
- MCP server starts but cannot write logs
- Missing diagnostic information

**Solutions:**

1. **Check log directory permissions**

   ```bash
   # Verify /tmp is writable
   touch /tmp/test-write && rm /tmp/test-write

   # Create log file explicitly
   touch /tmp/mcp-chrome.log
   ```

2. **Use alternative log location**

   Update configuration:
   ```json
   "--logFile", "/home/YOUR_USER/.local/log/mcp-chrome.log"
   ```

---

## Diagnostic Commands

### Quick Health Check

```bash
#!/bin/bash
# chrome-devtools-health-check.sh

echo "=== Chrome DevTools MCP Health Check ==="

# Check Chrome running with debugging
echo -n "Chrome with debugging: "
if pgrep -f "chrome.*remote-debugging-port" > /dev/null; then
    echo "RUNNING"
else
    echo "NOT RUNNING"
fi

# Check port availability
echo -n "Port 9222 status: "
if lsof -i :9222 > /dev/null 2>&1; then
    echo "IN USE"
else
    echo "AVAILABLE"
fi

# Check DevTools endpoint
echo -n "DevTools endpoint: "
if curl -s --connect-timeout 2 http://127.0.0.1:9222/json/version > /dev/null; then
    echo "ACCESSIBLE"
    echo "  Version: $(curl -s http://127.0.0.1:9222/json/version | jq -r '.Browser')"
else
    echo "NOT ACCESSIBLE"
fi

# Check available targets
echo -n "Debugging targets: "
TARGETS=$(curl -s http://127.0.0.1:9222/json/list 2>/dev/null | jq 'length')
if [ -n "$TARGETS" ]; then
    echo "$TARGETS available"
else
    echo "0 (or unreachable)"
fi

# Check MCP wrapper
echo -n "MCP wrapper: "
WRAPPER="$HOME/.config/mcp/servers/mcp-chrome-devtools-generic.sh"
if [ -x "$WRAPPER" ]; then
    echo "EXISTS and EXECUTABLE"
else
    echo "MISSING or NOT EXECUTABLE"
fi

# Check log file
echo -n "Log file: "
LOG="/tmp/mcp-chrome.log"
if [ -f "$LOG" ]; then
    echo "EXISTS ($(wc -l < $LOG) lines)"
else
    echo "NOT FOUND"
fi
```

### View Recent Log Entries

```bash
# Last 50 log entries
tail -n 50 /tmp/mcp-chrome.log

# Filter for errors
grep -i "error\|fail\|exception" /tmp/mcp-chrome.log
```

### Test CDP Connection Manually

```bash
# Get WebSocket URL for first page
WS_URL=$(curl -s http://127.0.0.1:9222/json/list | jq -r '.[0].webSocketDebuggerUrl')
echo "WebSocket URL: $WS_URL"

# Test with websocat (if installed)
# echo '{"id":1,"method":"Runtime.evaluate","params":{"expression":"1+1"}}' | websocat "$WS_URL"
```

### Full System Information

```bash
echo "=== System Information ==="
echo "OS: $(lsb_release -d | cut -f2)"
echo "Kernel: $(uname -r)"
echo "Node: $(node --version)"
echo "NPM: $(npm --version)"
echo "Chrome: $(google-chrome --version 2>/dev/null || echo 'Not found')"
echo "User: $(whoami)"
echo "Home: $HOME"
```

---

## Getting Help

If issues persist after trying these solutions:

1. **Collect diagnostic information**
   ```bash
   # Run health check script
   bash chrome-devtools-health-check.sh > diagnostics.txt

   # Include log file
   cat /tmp/mcp-chrome.log >> diagnostics.txt
   ```

2. **Check for known issues**
   - Review chrome-devtools-mcp package issues on npm/GitHub

3. **Verify MCP configuration**
   ```bash
   cat ~/.config/mcp/mcp.json | jq '.mcpServers["chrome-devtools"]'
   ```

---

**Last Updated**: 2025-01-13
**Environment**: Linux Ubuntu / Local / Cursor / Claude Code CLI
