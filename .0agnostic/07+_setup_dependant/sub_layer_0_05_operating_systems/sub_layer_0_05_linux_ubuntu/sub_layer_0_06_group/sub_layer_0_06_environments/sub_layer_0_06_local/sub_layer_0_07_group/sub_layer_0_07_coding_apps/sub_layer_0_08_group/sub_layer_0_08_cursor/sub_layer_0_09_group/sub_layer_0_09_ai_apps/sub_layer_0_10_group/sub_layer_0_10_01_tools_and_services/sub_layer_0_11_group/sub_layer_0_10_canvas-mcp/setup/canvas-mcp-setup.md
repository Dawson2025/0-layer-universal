---
resource_id: "3480c45b-2b84-44b5-9612-d147836ad362"
resource_type: "document"
resource_name: "canvas-mcp-setup"
---
# Canvas MCP Server Setup for Claude Code CLI

**Last Updated**: 2026-01-26

<!-- section_id: "fcd31eec-4c60-42c4-9650-13c3e2074479" -->
## Overview

The Canvas MCP server provides access to Canvas LMS features including courses, assignments, grades, discussions, and more.

<!-- section_id: "b74df804-f63e-4052-8dcf-8a885c154d9d" -->
## Configuration

<!-- section_id: "17182dac-fc10-4728-9ac4-3950add97fcd" -->
### Config File Location
`~/.claude.json`

<!-- section_id: "c6d71a50-db0e-47de-92fa-792bd4f624b1" -->
### Configuration Block
```json
{
  "mcpServers": {
    "canvas": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/dawson/mcp-servers/canvas-mcp-developer/dist/index.js"],
      "env": {
        "CANVAS_BASE_URL": "https://byui.instructure.com",
        "CANVAS_API_TOKEN": "YOUR_CANVAS_API_TOKEN"
      }
    }
  }
}
```

<!-- section_id: "423d16aa-c437-4ba6-95c5-b21f4319c05a" -->
### Server Locations

| CLI | Server Path |
|-----|-------------|
| Claude Code | `/home/dawson/mcp-servers/canvas-mcp-developer/` |
| Gemini CLI | `/home/dawson/mcp-servers/gemini-mcp-developer/` |

**Note**: These are separate server instances but use the same API token.

<!-- section_id: "0ca307cb-4373-4ed6-a6f7-7c75d9765224" -->
## Getting a Canvas API Token

1. Log in to your Canvas instance (e.g., https://byui.instructure.com)
2. Go to **Account** → **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Enter a purpose (e.g., "Claude Code MCP")
6. Set expiration (optional)
7. Click **Generate Token**
8. Copy the token immediately (shown only once)

<!-- section_id: "52a261e1-6b10-4a7b-992f-bed7db3b4709" -->
## Available Tools

<!-- section_id: "06880c7a-f92f-4f01-8d6a-a3cbb7400c19" -->
### Course Management
| Tool | Description |
|------|-------------|
| `canvas_course_list` | List enrolled courses |
| `canvas_course_get` | Get course details |
| `canvas_dashboard` | Comprehensive dashboard view |

<!-- section_id: "e4f325d2-96dc-4143-845e-9cdcf2dba5a2" -->
### Assignments & Grades
| Tool | Description |
|------|-------------|
| `canvas_assignment_list` | List assignments (with filters) |
| `canvas_assignment_get` | Get assignment details |
| `canvas_get_my_submission` | Get your submission for an assignment |
| `canvas_grades_overview` | View grades across all courses |
| `canvas_missing_submissions` | Find overdue/missing work |

<!-- section_id: "410e97b5-7580-4d9f-98c4-16cacdccc98e" -->
### Modules & Content
| Tool | Description |
|------|-------------|
| `canvas_module_list` | List course modules |
| `canvas_module_get` | Get module details |
| `canvas_module_items` | List items in a module |
| `canvas_module_progress` | Track module completion |

<!-- section_id: "9c02e447-ac3e-4ea0-9058-4f2378d82f97" -->
### Files & Discussions
| Tool | Description |
|------|-------------|
| `canvas_file_list` | List course files |
| `canvas_file_search` | Search for files |
| `canvas_discussion_list` | List discussions |
| `canvas_discussion_get` | Get discussion with replies |

<!-- section_id: "d7aeab61-ca2a-4326-870c-c375e406e77f" -->
### Planning & Communication
| Tool | Description |
|------|-------------|
| `canvas_planner_items` | Get upcoming items |
| `canvas_todo_list` | Get TODO items |
| `canvas_upcoming_events` | Get calendar events |
| `canvas_inbox_list` | List inbox messages |
| `canvas_announcement_list` | List announcements |

<!-- section_id: "db003afb-f200-4a9c-8c9f-c4613a553529" -->
## Troubleshooting

<!-- section_id: "e01288bb-9a22-4b7b-affe-a6b507a9c502" -->
### 401 Unauthorized Error

**Causes**:
1. **Token expired** - Canvas tokens can have expiration dates
2. **Token revoked** - Token was deleted in Canvas settings
3. **Wrong Canvas URL** - CANVAS_BASE_URL doesn't match your institution

**Solution**:
1. Check if token is still listed in Canvas Settings → Approved Integrations
2. Generate a new token if needed
3. Verify the base URL is correct for your institution

<!-- section_id: "03091a24-81f4-4001-abf5-cd4dcc80711c" -->
### File Downloads Failing

**Symptom**: `canvas_file_download` returns error

**Cause**: Canvas blocks file downloads with API tokens only; browser cookies required

**Solution**: Download files manually through the Canvas web interface

<!-- section_id: "1fdef53a-4ed1-4289-8740-bd11615d1fc0" -->
### MCP Server Not Starting

**Symptom**: Claude Code shows server as disconnected

**Solution**:
1. Verify the server is built:
   ```bash
   cd /home/dawson/mcp-servers/canvas-mcp-developer
   npm run build
   ```
2. Check that `dist/index.js` exists
3. Run `/mcp` in Claude Code and reconnect

<!-- section_id: "3069c8d1-4bcc-487a-bbaa-b883f7d0be02" -->
## Testing

Test the connection:
```bash
# In Claude Code, run:
mcp__canvas__canvas_profile
```

Expected: Your Canvas profile info (name, user ID)

<!-- section_id: "525faed6-13ee-4d95-9f30-4183e8a31b00" -->
## Shared Configuration

Both Claude Code and Gemini CLI use the same Canvas API token but different server instances:

| Config File | Server Path |
|-------------|-------------|
| `~/.claude.json` | `/home/dawson/mcp-servers/canvas-mcp-developer/` |
| `~/.gemini/settings.json` | `/home/dawson/mcp-servers/gemini-mcp-developer/` |

If you regenerate the token, update both config files.

<!-- section_id: "48e89d5c-7190-479b-bb22-03c017bac8f5" -->
## Related

- Perplexity MCP: `../sub_layer_0_10_perplexity-mcp/`
- Gemini CLI Canvas setup: `../../sub_layer_0_09_gemini_cli/sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/sub_layer_0_10_canvas-mcp/`
