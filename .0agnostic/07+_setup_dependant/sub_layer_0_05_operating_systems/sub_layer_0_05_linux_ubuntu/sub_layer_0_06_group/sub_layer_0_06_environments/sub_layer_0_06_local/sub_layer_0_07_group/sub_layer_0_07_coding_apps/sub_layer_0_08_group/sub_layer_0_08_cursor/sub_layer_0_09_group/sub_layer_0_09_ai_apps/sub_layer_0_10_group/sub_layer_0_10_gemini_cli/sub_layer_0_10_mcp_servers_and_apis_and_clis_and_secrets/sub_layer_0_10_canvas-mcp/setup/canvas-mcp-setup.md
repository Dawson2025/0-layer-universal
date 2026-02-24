# Canvas MCP Server Setup for Gemini CLI

**Last Updated**: 2026-01-26

## Overview

The Canvas MCP server provides access to Canvas LMS features including courses, assignments, grades, discussions, and more.

## Configuration

### Config File Location
`~/.gemini/settings.json`

### Configuration Block
```json
{
  "mcpServers": {
    "canvas": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/dawson/mcp-servers/gemini-mcp-developer/dist/index.js"],
      "env": {
        "CANVAS_BASE_URL": "https://byui.instructure.com",
        "CANVAS_API_TOKEN": "YOUR_CANVAS_API_TOKEN"
      }
    }
  }
}
```

### Server Locations

| CLI | Server Path |
|-----|-------------|
| Gemini CLI | `/home/dawson/mcp-servers/gemini-mcp-developer/` |
| Claude Code | `/home/dawson/mcp-servers/canvas-mcp-developer/` |

**Note**: These are separate server instances but use the same API token.

## Getting a Canvas API Token

1. Log in to your Canvas instance (e.g., https://byui.instructure.com)
2. Go to **Account** → **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Enter a purpose (e.g., "Gemini CLI MCP")
6. Set expiration (optional)
7. Click **Generate Token**
8. Copy the token immediately (shown only once)

## Available Tools

### Course Management
- `canvas_course_list` - List enrolled courses
- `canvas_course_get` - Get course details
- `canvas_dashboard` - Comprehensive dashboard view

### Assignments & Grades
- `canvas_assignment_list` - List assignments (with filters)
- `canvas_assignment_get` - Get assignment details
- `canvas_get_my_submission` - Get your submission
- `canvas_grades_overview` - View grades across courses
- `canvas_missing_submissions` - Find overdue work

### Modules & Content
- `canvas_module_list` - List course modules
- `canvas_module_get` - Get module details
- `canvas_file_list` - List course files
- `canvas_discussion_list` - List discussions

### Planning & Communication
- `canvas_planner_items` - Get upcoming items
- `canvas_todo_list` - Get TODO items
- `canvas_inbox_list` - List inbox messages
- `canvas_announcement_list` - List announcements

## Troubleshooting

### 401 Unauthorized Error

**Causes**:
1. **Token expired** - Canvas tokens can have expiration dates
2. **Token revoked** - Token was deleted in Canvas settings
3. **Wrong Canvas URL** - CANVAS_BASE_URL doesn't match your institution

**Solution**:
1. Check if token is still listed in Canvas Settings → Approved Integrations
2. Generate a new token if needed
3. Verify the base URL is correct for your institution

### Server Not Starting

**Solution**:
1. Verify the server is built:
   ```bash
   cd /home/dawson/mcp-servers/gemini-mcp-developer
   npm run build
   ```
2. Check that `dist/index.js` exists

## Building the Server

```bash
cd /home/dawson/mcp-servers/gemini-mcp-developer
npm install
npm run build
```

## Shared Configuration

Both Gemini CLI and Claude Code use the same Canvas API token but different server instances:

| Config File | Server Path |
|-------------|-------------|
| `~/.gemini/settings.json` | `/home/dawson/mcp-servers/gemini-mcp-developer/` |
| `~/.claude.json` | `/home/dawson/mcp-servers/canvas-mcp-developer/` |

If you regenerate the token, update both config files.

## Related

- Perplexity MCP: `../sub_layer_0_10_perplexity-mcp/`
- Claude Code CLI Canvas setup: `../../sub_layer_0_09_claude_code_cli/sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/sub_layer_0_10_canvas-mcp/`
