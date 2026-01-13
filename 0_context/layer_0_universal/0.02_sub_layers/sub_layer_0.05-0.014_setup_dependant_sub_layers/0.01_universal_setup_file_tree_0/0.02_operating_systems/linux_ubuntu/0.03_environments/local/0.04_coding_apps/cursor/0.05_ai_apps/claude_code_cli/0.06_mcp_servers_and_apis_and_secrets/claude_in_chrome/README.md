# Claude in Chrome MCP Server

## Overview

Claude in Chrome is a Model Context Protocol (MCP) server that enables AI-assisted browser automation through the Claude browser extension. It provides a bridge between Claude Code CLI and Chrome, allowing AI agents to read web pages, interact with page elements, capture screenshots, execute JavaScript, and perform complex browser automation tasks.

This MCP server transforms Claude into a capable browser automation assistant that can navigate websites, fill forms, extract content, and interact with web applications on your behalf.

## Features

### Page Reading and Analysis
- **Accessibility Tree Snapshots**: Capture the complete accessibility structure of any web page
- **Text Extraction**: Extract raw text content prioritizing article and main content areas
- **Element Finding**: Locate elements using natural language queries (e.g., "search bar", "login button")
- **Console Monitoring**: Read browser console messages for debugging and monitoring

### Browser Interaction
- **Navigation**: Navigate to URLs, go forward/back in browser history
- **Mouse Actions**: Click, double-click, right-click, hover, drag-and-drop
- **Keyboard Input**: Type text, press keys, use keyboard shortcuts
- **Form Handling**: Fill form fields, select options, upload files
- **Scrolling**: Scroll pages and scroll elements into view

### Visual Capture
- **Screenshots**: Capture full page or viewport screenshots
- **Zoom Regions**: Capture specific regions for detailed inspection
- **GIF Recording**: Record browser sessions as animated GIFs with action overlays

### Advanced Capabilities
- **JavaScript Execution**: Run custom JavaScript in page context
- **Network Monitoring**: Monitor XHR, Fetch, and other network requests
- **Tab Management**: Create, select, and manage browser tabs
- **Window Resizing**: Resize browser windows for responsive testing
- **Shortcut Execution**: Execute predefined shortcuts and workflows

## Quick Start

### 1. Install the Claude Browser Extension

1. Open Chrome and navigate to the Chrome Web Store
2. Search for "Claude" or visit the official Claude extension page
3. Click "Add to Chrome" to install the extension
4. Pin the extension to your toolbar for easy access
5. Sign in with your Anthropic account

### 2. Configure MCP Server

Run the MCP manager script to set up the server configuration:

```bash
# Navigate to the setup scripts directory
cd setup/scripts

# Set up MCP servers at user level (recommended)
python3 mcp_manager.py --scope user

# Or for project-level setup
python3 mcp_manager.py --scope project
```

### 3. Restart Claude Code CLI

After configuration, restart your Claude Code CLI session:

```bash
# Close existing session and start fresh
claude
```

### 4. Verify Connection

In your Claude Code session, the browser tools should now be available:

```
# Example: Get tab context
mcp__claude-in-chrome__tabs_context_mcp
```

## Prerequisites

### Required Software

| Component | Version | Purpose |
|-----------|---------|---------|
| Google Chrome | Latest stable | Browser for automation |
| Claude Extension | Latest | Bridge between Claude and Chrome |
| Node.js | 18+ | Runtime for MCP servers |
| Python | 3.7+ | Setup scripts |
| Claude Code CLI | Latest | AI agent interface |

### System Requirements

- **Operating System**: Linux (Ubuntu 22.04+), macOS, or Windows with WSL2
- **Display Server**: X11 or Wayland (WSLg supported)
- **Memory**: 4GB+ RAM recommended for browser automation
- **Network**: Active internet connection for extension communication

### Browser Extension Setup

1. **Extension Installation**: Install from Chrome Web Store
2. **Permissions**: Grant necessary permissions when prompted
3. **Authentication**: Sign in to the extension with your Anthropic credentials
4. **Tab Group**: The extension creates an "MCP" tab group for managed tabs

## Architecture

```
+-------------------+     +----------------------+     +------------------+
|  Claude Code CLI  | <-> |  MCP Server Bridge   | <-> |  Chrome Browser  |
+-------------------+     +----------------------+     +------------------+
        |                          |                          |
        v                          v                          v
  User Commands           Protocol Messages           DOM/Page Actions
```

### Communication Flow

1. User issues command in Claude Code CLI
2. Claude invokes MCP tool function
3. MCP server translates to browser action
4. Chrome extension executes action
5. Results return through the chain

## Available Tools

### Tab Management
- `tabs_context_mcp` - Get tab context and available tab IDs
- `tabs_create_mcp` - Create new tabs in the MCP group

### Page Interaction
- `read_page` - Get accessibility tree of current page
- `find` - Find elements using natural language
- `computer` - Mouse/keyboard actions (click, type, scroll, etc.)
- `navigate` - Navigate to URLs or history navigation
- `form_input` - Set form field values

### Content Extraction
- `get_page_text` - Extract text content from page
- `javascript_tool` - Execute JavaScript in page context

### Monitoring
- `read_console_messages` - Read browser console output
- `read_network_requests` - Monitor network activity

### Visual
- `gif_creator` - Record and export GIF animations
- `upload_image` - Upload screenshots to file inputs
- `resize_window` - Change browser window dimensions

### Automation
- `shortcuts_list` - List available shortcuts/workflows
- `shortcuts_execute` - Run predefined shortcuts
- `update_plan` - Present action plan for user approval

## Configuration Files

### MCP Configuration Location

```
~/.config/mcp/
├── mcp.json              # Main MCP server configuration
├── servers/              # Generated wrapper scripts
│   ├── mcp-playwright-generic.sh
│   ├── mcp-browser-generic.sh
│   └── ...
└── configs/
    └── playwright.json   # Playwright-specific config
```

### Environment Variables

The following environment variables are automatically configured:

| Variable | Description |
|----------|-------------|
| `PLAYWRIGHT_BROWSERS_PATH` | Path to browser binaries |
| `HOME` | User home directory |
| `DISPLAY` | X11 display for headed mode |
| `WAYLAND_DISPLAY` | Wayland display (WSLg) |
| `XDG_RUNTIME_DIR` | Runtime directory (WSLg) |

## Concurrent Browser Usage

When using multiple AI tools (Codex CLI, Claude Code CLI, Gemini CLI) simultaneously, each tool needs its own isolated browser configuration to prevent conflicts.

### Setup Concurrent Browsers

```bash
# Navigate to setup scripts
cd setup/scripts

# Set up OS-specific concurrent configs
python3 mcp_concurrent_browser.py setup

# Apply Codex-specific config (if using Codex)
python3 mcp_concurrent_browser.py apply-codex

# Verify setup
python3 mcp_concurrent_browser.py status
```

See `setup/CONCURRENT_BROWSER_SETUP.md` for detailed concurrent browser documentation.

## Usage Examples

### Basic Navigation

```python
# Get tab context first
tabs_context_mcp(createIfEmpty=True)

# Navigate to a website
navigate(url="https://example.com", tabId=123)

# Take a screenshot
computer(action="screenshot", tabId=123)
```

### Form Interaction

```python
# Find the search input
find(query="search bar", tabId=123)

# Type in the search field
form_input(ref="ref_1", value="search query", tabId=123)

# Click submit button
computer(action="left_click", ref="ref_2", tabId=123)
```

### Content Extraction

```python
# Get page text content
get_page_text(tabId=123)

# Read accessibility tree
read_page(tabId=123, filter="interactive")

# Execute JavaScript
javascript_tool(action="javascript_exec",
                text="document.title",
                tabId=123)
```

## Related Documentation

- `setup/README.md` - MCP server automation system details
- `setup/CONCURRENT_BROWSER_SETUP.md` - Multi-tool browser setup guide
- `setup/TROUBLESHOOTING.md` - Common issues and solutions
- `0.08_protocols/` - Workflow protocols for common tasks

## Support

For issues specific to the Claude browser extension, refer to Anthropic's official documentation. For MCP server configuration issues, see the troubleshooting guide in `setup/TROUBLESHOOTING.md`.

---

**Last Updated**: 2026-01-13
**MCP Server Version**: Compatible with Claude Code CLI
**Status**: Active
