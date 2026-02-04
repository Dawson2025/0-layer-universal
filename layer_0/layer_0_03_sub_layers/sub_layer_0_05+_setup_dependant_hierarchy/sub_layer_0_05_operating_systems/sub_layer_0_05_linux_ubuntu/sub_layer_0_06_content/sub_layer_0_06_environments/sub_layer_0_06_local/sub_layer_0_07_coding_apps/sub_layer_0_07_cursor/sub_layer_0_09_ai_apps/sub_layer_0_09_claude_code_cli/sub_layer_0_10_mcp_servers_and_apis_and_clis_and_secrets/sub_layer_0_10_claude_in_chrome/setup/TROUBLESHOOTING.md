# Claude in Chrome - Troubleshooting Guide

This document covers common issues encountered when using the Claude in Chrome MCP server and their solutions.

## Table of Contents

1. [Extension Not Detected](#extension-not-detected)
2. [Communication Errors](#communication-errors)
3. [Permission Problems](#permission-problems)
4. [Browser Issues](#browser-issues)
5. [MCP Configuration Issues](#mcp-configuration-issues)
6. [WSL-Specific Issues](#wsl-specific-issues)
7. [Concurrent Browser Conflicts](#concurrent-browser-conflicts)

---

## Extension Not Detected

### Symptom
Claude Code CLI cannot communicate with the browser, tools return errors like "No tab context found" or "Extension not responding".

### Causes and Solutions

#### Extension Not Installed
**Solution**: Install the Claude browser extension from Chrome Web Store.

1. Open Chrome browser
2. Navigate to Chrome Web Store
3. Search for "Claude" extension
4. Click "Add to Chrome"
5. Confirm installation
6. Pin the extension to your toolbar

#### Extension Disabled
**Solution**: Enable the extension in Chrome settings.

```
chrome://extensions/
```

1. Find the Claude extension
2. Toggle the switch to enable it
3. Refresh any open tabs

#### Extension Not Authenticated
**Solution**: Sign in to the extension.

1. Click the Claude extension icon in toolbar
2. Sign in with your Anthropic credentials
3. Complete any verification steps
4. Wait for the extension to initialize

#### Tab Group Not Created
**Solution**: Initialize the MCP tab group.

```python
# In Claude Code CLI, run:
mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=True)
```

This creates a new window with an MCP tab group if none exists.

#### Browser Not Running
**Solution**: Ensure Chrome is running with the extension active.

```bash
# Start Chrome (Linux)
google-chrome &

# Or Chromium
chromium-browser &
```

---

## Communication Errors

### Symptom
Tools timeout, return "Connection refused", or fail with network errors.

### Causes and Solutions

#### MCP Server Not Started
**Solution**: Verify the MCP server is running.

```bash
# Check for running MCP processes
ps aux | grep mcp

# Check for node processes related to playwright/browser
ps aux | grep playwright
ps aux | grep chromium
```

#### Firewall Blocking Connection
**Solution**: Check firewall rules.

```bash
# Check if port is being blocked (if using remote debugging)
sudo ufw status

# Allow localhost connections
sudo ufw allow from 127.0.0.1
```

#### Extension Crashed
**Solution**: Restart the extension.

1. Navigate to `chrome://extensions/`
2. Find Claude extension
3. Click the reload button (circular arrow)
4. Close and reopen Claude Code CLI

#### Stale Tab Reference
**Solution**: Get fresh tab context.

```python
# Always get fresh tab context before operations
mcp__claude-in-chrome__tabs_context_mcp()
```

The `tabId` values can become stale if tabs are closed or the browser restarts.

---

## Permission Problems

### Symptom
Tools fail with "Permission denied" or security-related errors.

### Causes and Solutions

#### Extension Permissions Not Granted
**Solution**: Grant required permissions.

1. Click the extension icon
2. Click "Settings" or gear icon
3. Review and grant all requested permissions
4. Especially ensure "Read and change all your data on all websites" is enabled for full functionality

#### Content Security Policy Blocking
**Solution**: Some websites block extension scripts via CSP.

This is a website-level restriction. Workarounds:
- Use headless mode for restricted sites
- Access the site through different methods
- Check if the site has an API alternative

#### File Upload Restrictions
**Solution**: Ensure proper file paths.

```python
# Use absolute paths for file uploads
upload_image(imageId="screenshot_id",
             ref="ref_1",
             tabId=123)
```

#### Cross-Origin Restrictions
**Solution**: The extension can only interact with tabs in its managed group.

Always use `tabs_context_mcp` first to ensure you're working with managed tabs.

---

## Browser Issues

### Symptom
Browser crashes, doesn't open, or displays incorrectly.

### Causes and Solutions

#### Browser Not Installed
**Solution**: Install Chromium browsers via Playwright.

```bash
# Install Playwright browsers
npx playwright install chromium

# Verify installation
ls ~/.cache/ms-playwright/
```

#### Browser Executable Not Found
**Solution**: Update the browser path in configuration.

```bash
# Run the MCP manager to regenerate configs
python3 setup/scripts/mcp_manager.py --scope user
```

The script auto-detects the newest Chromium version.

#### Browser Profile Corrupted
**Solution**: Clear the browser profile.

```bash
# Remove existing profile
rm -rf ~/.cache/ms-playwright/mcp-chromium-*

# Restart Claude Code CLI
# The profile will be recreated automatically
```

#### Display Issues (Headed Mode)
**Solution**: Verify display settings.

```bash
# Check DISPLAY variable
echo $DISPLAY

# Should output something like ":0" or ":1"

# If empty, set it
export DISPLAY=:0
```

---

## MCP Configuration Issues

### Symptom
MCP tools are not available or configuration errors appear.

### Causes and Solutions

#### Configuration File Missing
**Solution**: Regenerate the configuration.

```bash
# Run setup script
python3 setup/scripts/mcp_manager.py --scope user

# Restart Claude Code CLI
```

#### Invalid JSON Configuration
**Solution**: Validate and fix the configuration file.

```bash
# Check the config file
cat ~/.config/mcp/mcp.json | python3 -m json.tool

# If errors, regenerate
python3 setup/scripts/mcp_manager.py --scope user
```

#### Environment Variables Not Set
**Solution**: Ensure environment variables are in the wrapper scripts.

The wrapper scripts at `~/.config/mcp/servers/` should contain:

```bash
export PLAYWRIGHT_BROWSERS_PATH="/home/user/.cache/ms-playwright"
export HOME="/home/user"
export DISPLAY=":0"
```

If missing, regenerate with:

```bash
python3 setup/scripts/mcp_manager.py --scope user
```

#### npx Not Found
**Solution**: Install Node.js and npm.

```bash
# Using NVM (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install --lts

# Verify
which npx
npx --version
```

---

## WSL-Specific Issues

### Symptom
Browser crashes immediately on WSL, graphical issues, or display not working.

### Causes and Solutions

#### WSLg Not Configured
**Solution**: Verify WSLg is working.

```bash
# Check if WSLg paths exist
ls /mnt/wslg/runtime-dir

# If not present, update WSL
# In Windows PowerShell (admin):
wsl --update
```

#### Wayland/Ozone Not Enabled
**Solution**: Ensure browser uses Wayland on WSLg.

The configuration should include:

```json
{
  "browser": {
    "launchOptions": {
      "args": [
        "--ozone-platform=wayland",
        "--enable-features=UseOzonePlatform"
      ]
    }
  }
}
```

Regenerate config:

```bash
python3 setup/scripts/mcp_manager.py --scope user
```

#### X11 Fallback Issues
**Solution**: Try X11 mode instead of Wayland.

```bash
# Remove Wayland flags from config manually
# Or set DISPLAY and unset WAYLAND_DISPLAY
export DISPLAY=:0
unset WAYLAND_DISPLAY
```

#### Missing Dependencies
**Solution**: Install WSL GUI dependencies.

```bash
# Update packages
sudo apt update

# Install common dependencies
sudo apt install -y \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libxkbcommon0 \
    libasound2
```

---

## Concurrent Browser Conflicts

### Symptom
"Browser is already in use" error when running multiple AI tools.

### Causes and Solutions

#### Shared Browser Instance
**Solution**: Set up tool-specific browser configurations.

```bash
# Navigate to setup directory
cd setup/scripts

# Set up concurrent configs
python3 mcp_concurrent_browser.py setup

# Apply to Codex (if using)
python3 mcp_concurrent_browser.py apply-codex

# Verify
python3 mcp_concurrent_browser.py status
```

#### Leftover Browser Processes
**Solution**: Kill stale browser processes.

```bash
# Find and kill playwright processes
pkill -f playwright

# Kill chromium processes
pkill -f chromium

# Restart Claude Code CLI
```

#### Profile Directory Locked
**Solution**: Remove lock files or use isolated profiles.

```bash
# Remove lock files
rm -f ~/.cache/ms-playwright/mcp-chromium-*/SingletonLock
rm -f ~/.cache/ms-playwright/mcp-chromium-*/SingletonSocket

# Or use the concurrent browser setup for isolated profiles
python3 setup/scripts/mcp_concurrent_browser.py setup
```

#### Configuration Not Applied
**Solution**: Restart all AI CLI tools after configuration changes.

1. Close all instances of Claude Code CLI, Codex CLI, etc.
2. Wait a few seconds for processes to terminate
3. Reopen the AI tools
4. Verify configuration with `status` command

---

## Diagnostic Commands

### Check MCP Server Status

```bash
# List running MCP processes
ps aux | grep -E "(mcp|playwright|chromium)"

# Check MCP configuration
cat ~/.config/mcp/mcp.json | python3 -m json.tool

# Verify Playwright browsers
ls -la ~/.cache/ms-playwright/

# Check wrapper scripts
ls -la ~/.config/mcp/servers/
```

### Test Browser Manually

```bash
# Test Chromium directly
~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome --headless --dump-dom https://example.com

# Test with Playwright
npx playwright screenshot https://example.com screenshot.png
```

### Check Extension Connection

In Chrome DevTools (F12):

```javascript
// Check extension context
console.log(chrome.runtime.id);
```

---

## Getting Help

### Log Files

Check these locations for error logs:

```
/tmp/mcp-chrome.log          # Chrome DevTools MCP log
~/.config/mcp/logs/          # General MCP logs (if configured)
~/.cache/ms-playwright/      # Playwright cache and crash dumps
```

### Report Issues

When reporting issues, include:

1. Operating system and version
2. Chrome version (`chrome://version`)
3. Extension version
4. Error messages (complete text)
5. Steps to reproduce
6. Output of diagnostic commands above

---

**Last Updated**: 2026-01-13
