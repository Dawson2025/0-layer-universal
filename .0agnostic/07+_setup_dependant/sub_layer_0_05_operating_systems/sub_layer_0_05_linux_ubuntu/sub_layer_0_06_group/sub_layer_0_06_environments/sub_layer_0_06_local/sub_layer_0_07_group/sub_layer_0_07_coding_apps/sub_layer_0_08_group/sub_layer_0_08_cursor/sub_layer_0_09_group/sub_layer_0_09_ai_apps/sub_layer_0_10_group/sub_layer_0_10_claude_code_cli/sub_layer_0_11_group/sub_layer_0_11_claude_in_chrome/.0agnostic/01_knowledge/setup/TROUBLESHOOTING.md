---
resource_id: "6db1b04b-3a38-499b-99a2-8b55031d4e3c"
resource_type: "knowledge"
resource_name: "TROUBLESHOOTING"
---
# Claude in Chrome - Troubleshooting Guide

This document covers common issues encountered when using the Claude in Chrome MCP server and their solutions.

<!-- section_id: "1c8ca828-5066-4dc2-88ae-da4dc472cc56" -->
## Table of Contents

1. [Extension Not Detected](#extension-not-detected)
2. [Communication Errors](#communication-errors)
3. [Permission Problems](#permission-problems)
4. [Browser Issues](#browser-issues)
5. [MCP Configuration Issues](#mcp-configuration-issues)
6. [WSL-Specific Issues](#wsl-specific-issues)
7. [Concurrent Browser Conflicts](#concurrent-browser-conflicts)

---

<!-- section_id: "8bdb1be2-dc3a-4d2c-b352-ca4a24e37b34" -->
## Extension Not Detected

<!-- section_id: "dc48f6da-bd27-43ce-8c4c-d8dd405fc5dc" -->
### Symptom
Claude Code CLI cannot communicate with the browser, tools return errors like "No tab context found" or "Extension not responding".

<!-- section_id: "5988ab80-64a2-46a9-b8dc-bbe3b244a87a" -->
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

<!-- section_id: "db06e42a-603c-4084-b715-7364b8c53c22" -->
## Communication Errors

<!-- section_id: "a5a4c224-4636-4d87-bf62-e8e016ecdf5d" -->
### Symptom
Tools timeout, return "Connection refused", or fail with network errors.

<!-- section_id: "c1217c86-f6e1-42c1-823a-b18de6821cd7" -->
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

<!-- section_id: "398f4e4e-1703-414f-86db-c0127ab84f88" -->
## Permission Problems

<!-- section_id: "426cd60d-1d6c-4126-81dc-4cb580cb6a44" -->
### Symptom
Tools fail with "Permission denied" or security-related errors.

<!-- section_id: "c1f3797d-2036-4472-8973-7419f1b2dad5" -->
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

<!-- section_id: "f11085da-a0d2-4525-8fdb-c29a1296accf" -->
## Browser Issues

<!-- section_id: "d97b7fe1-c959-48cb-9490-4d6340c4a971" -->
### Symptom
Browser crashes, doesn't open, or displays incorrectly.

<!-- section_id: "7d70213f-f56b-4472-8642-a24992c63487" -->
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

<!-- section_id: "68158186-836c-45c6-af60-285b8ac60d48" -->
## MCP Configuration Issues

<!-- section_id: "8ff8c180-024e-4f3e-8be0-f59ba02943e2" -->
### Symptom
MCP tools are not available or configuration errors appear.

<!-- section_id: "a7d91ab2-140e-4711-84c3-bc61a9b7a6ed" -->
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

<!-- section_id: "c41170b6-8842-4317-af2f-1946bf209211" -->
## WSL-Specific Issues

<!-- section_id: "87c2107c-f548-4ce9-8d45-44793289020c" -->
### Symptom
Browser crashes immediately on WSL, graphical issues, or display not working.

<!-- section_id: "7217221a-cdb2-4403-af6d-5fb641e0cc81" -->
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

<!-- section_id: "848ebdbf-b0f3-40cf-b942-0b5e2d66bd8c" -->
## Concurrent Browser Conflicts

<!-- section_id: "980520e1-458c-473e-a7b1-6bee02eb70fb" -->
### Symptom
"Browser is already in use" error when running multiple AI tools.

<!-- section_id: "23395a25-156f-4e85-9e6b-3ed1f05c11cc" -->
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

<!-- section_id: "9c82c14a-0e1a-4c73-acb0-bd843381d2ed" -->
## Diagnostic Commands

<!-- section_id: "5c6a63e0-0b9b-4e57-a692-74c5d8860fed" -->
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

<!-- section_id: "4bd186de-3af6-47c4-93e9-83081a70cc99" -->
### Test Browser Manually

```bash
# Test Chromium directly
~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome --headless --dump-dom https://example.com

# Test with Playwright
npx playwright screenshot https://example.com screenshot.png
```

<!-- section_id: "5a443a60-a4f5-4c4a-9f1f-05ef3f57f7a5" -->
### Check Extension Connection

In Chrome DevTools (F12):

```javascript
// Check extension context
console.log(chrome.runtime.id);
```

---

<!-- section_id: "218476ec-132b-4096-9ebf-e07a9f30fc38" -->
## Getting Help

<!-- section_id: "b7707424-93ee-4dbe-93ac-0d912fe105d4" -->
### Log Files

Check these locations for error logs:

```
/tmp/mcp-chrome.log          # Chrome DevTools MCP log
~/.config/mcp/logs/          # General MCP logs (if configured)
~/.cache/ms-playwright/      # Playwright cache and crash dumps
```

<!-- section_id: "5d65000d-bf57-452e-836c-719286b3bb85" -->
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
