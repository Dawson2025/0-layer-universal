---
resource_id: "177fb315-a398-43c5-9db8-8b950f06de16"
resource_type: "readme_document"
resource_name: "README"
---
# Claude in Chrome MCP Server

<!-- section_id: "11e96073-88cd-4faf-a721-74354e3c91af" -->
## Overview

Claude in Chrome is a Model Context Protocol (MCP) server that enables AI-assisted browser automation through the Claude browser extension. It provides a bridge between Claude Code CLI and Chrome, allowing AI agents to read web pages, interact with page elements, capture screenshots, execute JavaScript, and perform complex browser automation tasks.

This MCP server transforms Claude into a capable browser automation assistant that can navigate websites, fill forms, extract content, and interact with web applications on your behalf.

<!-- section_id: "c17e52d5-9c2f-4aed-8871-1e53b5b7f355" -->
## Features

<!-- section_id: "5bafd2fb-628f-4865-8553-e883b61e2dd7" -->
### Page Reading and Analysis
- **Accessibility Tree Snapshots**: Capture the complete accessibility structure of any web page
- **Text Extraction**: Extract raw text content prioritizing article and main content areas
- **Element Finding**: Locate elements using natural language queries (e.g., "search bar", "login button")
- **Console Monitoring**: Read browser console messages for debugging and monitoring

<!-- section_id: "3610614e-9940-44dd-9f6e-28a6c0f5f97f" -->
### Browser Interaction
- **Navigation**: Navigate to URLs, go forward/back in browser history
- **Mouse Actions**: Click, double-click, right-click, hover, drag-and-drop
- **Keyboard Input**: Type text, press keys, use keyboard shortcuts
- **Form Handling**: Fill form fields, select options, upload files
- **Scrolling**: Scroll pages and scroll elements into view

<!-- section_id: "ecb73770-6861-498f-994a-98055e8af6dc" -->
### Visual Capture
- **Screenshots**: Capture full page or viewport screenshots
- **Zoom Regions**: Capture specific regions for detailed inspection
- **GIF Recording**: Record browser sessions as animated GIFs with action overlays

<!-- section_id: "f29c21a0-852f-45fb-80ea-4f8cba4afa3b" -->
### Advanced Capabilities
- **JavaScript Execution**: Run custom JavaScript in page context
- **Network Monitoring**: Monitor XHR, Fetch, and other network requests
- **Tab Management**: Create, select, and manage browser tabs
- **Window Resizing**: Resize browser windows for responsive testing
- **Shortcut Execution**: Execute predefined shortcuts and workflows

<!-- section_id: "05b58efd-8626-4f9c-a73b-b8895e8a8200" -->
## Quick Start

<!-- section_id: "5675bca8-384f-4e2a-b371-313318a5453c" -->
### 1. Install the Claude Browser Extension

1. Open Chrome and navigate to the Chrome Web Store
2. Search for "Claude" or visit the official Claude extension page
3. Click "Add to Chrome" to install the extension
4. Pin the extension to your toolbar for easy access
5. Sign in with your Anthropic account

<!-- section_id: "a98d6c67-79ca-4373-8545-9c7d332b9c9e" -->
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

<!-- section_id: "c47dbe3b-f10e-490a-8121-328276cc3c78" -->
### 3. Restart Claude Code CLI

After configuration, restart your Claude Code CLI session:

```bash
# Close existing session and start fresh
claude
```

<!-- section_id: "6d6f664e-3c36-48f0-955f-0bc7a4959b95" -->
### 4. Verify Connection

In your Claude Code session, the browser tools should now be available:

```
# Example: Get tab context
mcp__claude-in-chrome__tabs_context_mcp
```

<!-- section_id: "5f8e112c-6300-42f2-92e7-3e79c8351dfa" -->
## Prerequisites

<!-- section_id: "05a2717b-bb73-476a-addd-6668868fdf2d" -->
### Required Software

| Component | Version | Purpose |
|-----------|---------|---------|
| Google Chrome | Latest stable | Browser for automation |
| Claude Extension | Latest | Bridge between Claude and Chrome |
| Node.js | 18+ | Runtime for MCP servers |
| Python | 3.7+ | Setup scripts |
| Claude Code CLI | Latest | AI agent interface |

<!-- section_id: "b2b95b29-26db-479f-948f-ae8d3d239dd9" -->
### System Requirements

- **Operating System**: Linux (Ubuntu 22.04+), macOS, or Windows with WSL2
- **Display Server**: X11 or Wayland (WSLg supported)
- **Memory**: 4GB+ RAM recommended for browser automation
- **Network**: Active internet connection for extension communication

<!-- section_id: "15c43646-97db-455d-946b-de2c9f9924d0" -->
### Browser Extension Setup

1. **Extension Installation**: Install from Chrome Web Store
2. **Permissions**: Grant necessary permissions when prompted
3. **Authentication**: Sign in to the extension with your Anthropic credentials
4. **Tab Group**: The extension creates an "MCP" tab group for managed tabs

<!-- section_id: "b1d668e8-cd4b-4192-b128-73828bed3791" -->
## Architecture

```
+-------------------+     +----------------------+     +------------------+
|  Claude Code CLI  | <-> |  MCP Server Bridge   | <-> |  Chrome Browser  |
+-------------------+     +----------------------+     +------------------+
        |                          |                          |
        v                          v                          v
  User Commands           Protocol Messages           DOM/Page Actions
```

<!-- section_id: "23443566-0849-4317-a615-3eea22312423" -->
### Communication Flow

1. User issues command in Claude Code CLI
2. Claude invokes MCP tool function
3. MCP server translates to browser action
4. Chrome extension executes action
5. Results return through the chain

<!-- section_id: "dcdab8f0-d9ba-4573-99db-fd09abbcaa51" -->
## Available Tools

<!-- section_id: "2104d531-afd5-4d9f-9fe0-4e5f8d890042" -->
### Tab Management
- `tabs_context_mcp` - Get tab context and available tab IDs
- `tabs_create_mcp` - Create new tabs in the MCP group

<!-- section_id: "2c07d95d-ec6b-4aa2-a37e-132558e99eea" -->
### Page Interaction
- `read_page` - Get accessibility tree of current page
- `find` - Find elements using natural language
- `computer` - Mouse/keyboard actions (click, type, scroll, etc.)
- `navigate` - Navigate to URLs or history navigation
- `form_input` - Set form field values

<!-- section_id: "5579259a-5518-4159-8263-bf329cf35242" -->
### Content Extraction
- `get_page_text` - Extract text content from page
- `javascript_tool` - Execute JavaScript in page context

<!-- section_id: "bef62d03-7024-4499-84f0-efc0234cfd4b" -->
### Monitoring
- `read_console_messages` - Read browser console output
- `read_network_requests` - Monitor network activity

<!-- section_id: "490ef62b-261e-4747-ad4c-9c709ca2d69c" -->
### Visual
- `gif_creator` - Record and export GIF animations
- `upload_image` - Upload screenshots to file inputs
- `resize_window` - Change browser window dimensions

<!-- section_id: "c3c45f0f-647f-468e-88e1-1ead52df6b45" -->
### Automation
- `shortcuts_list` - List available shortcuts/workflows
- `shortcuts_execute` - Run predefined shortcuts
- `update_plan` - Present action plan for user approval

<!-- section_id: "83365cf8-32cf-4861-ba6e-fe384be50c2d" -->
## Configuration Files

<!-- section_id: "c9ebbe03-eb12-48bd-9361-6684974a29d4" -->
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

<!-- section_id: "9b64cdd0-9c1f-4699-a4db-a13d0675d8c6" -->
### Environment Variables

The following environment variables are automatically configured:

| Variable | Description |
|----------|-------------|
| `PLAYWRIGHT_BROWSERS_PATH` | Path to browser binaries |
| `HOME` | User home directory |
| `DISPLAY` | X11 display for headed mode |
| `WAYLAND_DISPLAY` | Wayland display (WSLg) |
| `XDG_RUNTIME_DIR` | Runtime directory (WSLg) |

<!-- section_id: "a05b2337-c40d-4c9f-9a6e-d685df1c9f5a" -->
## Concurrent Browser Usage

When using multiple AI tools (Codex CLI, Claude Code CLI, Gemini CLI) simultaneously, each tool needs its own isolated browser configuration to prevent conflicts.

<!-- section_id: "ac6e68dc-12f7-4cfe-8593-6e868a6a5884" -->
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

<!-- section_id: "c6abc268-79c1-4821-bbd7-254f15c03df3" -->
## Usage Examples

<!-- section_id: "671f4367-d5ab-4b27-9218-22d7f8cdc59d" -->
### Basic Navigation

```python
# Get tab context first
tabs_context_mcp(createIfEmpty=True)

# Navigate to a website
navigate(url="https://example.com", tabId=123)

# Take a screenshot
computer(action="screenshot", tabId=123)
```

<!-- section_id: "75f28238-1e8a-4f5f-81c2-c4f43c1eebd5" -->
### Form Interaction

```python
# Find the search input
find(query="search bar", tabId=123)

# Type in the search field
form_input(ref="ref_1", value="search query", tabId=123)

# Click submit button
computer(action="left_click", ref="ref_2", tabId=123)
```

<!-- section_id: "422301e3-a56a-4fdf-a82e-985fd7e88cb3" -->
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

<!-- section_id: "6e65d71c-c99d-4cf7-8a9c-b0c329fe3bc4" -->
## Related Documentation

- `setup/README.md` - MCP server automation system details
- `setup/CONCURRENT_BROWSER_SETUP.md` - Multi-tool browser setup guide
- `setup/TROUBLESHOOTING.md` - Common issues and solutions
- `0.13_protocols/` - Workflow protocols for common tasks

<!-- section_id: "3e591c78-29ab-4483-a68c-67bb881fea7e" -->
## Support

For issues specific to the Claude browser extension, refer to Anthropic's official documentation. For MCP server configuration issues, see the troubleshooting guide in `setup/TROUBLESHOOTING.md`.

---

**Last Updated**: 2026-01-13
**MCP Server Version**: Compatible with Claude Code CLI
**Status**: Active
