---
resource_id: "40b64312-a9e8-462f-bbdb-a0ca819136ee"
resource_type: "document"
resource_name: "CLAUDE_CODE_SETUP"
---
# Canvas MCP Setup for Claude Code CLI in Cursor (Linux Ubuntu)

<!-- section_id: "316daec3-1135-4d8f-862b-78d88a7d0bbb" -->
## Setup Status

**Note**: Canvas MCP servers are GitHub-based projects and require manual installation.
There is no npm package available.

---

<!-- section_id: "4ddf0d12-ca8a-4a23-b1bd-6949420e576c" -->
## Installation Steps

<!-- section_id: "d0870157-cc66-4b5f-9e63-9ca2618978fd" -->
### Step 1: Clone the Canvas MCP Server

Choose one of these options:

**Option A: Student-focused (Recommended for BYUI students)**
```bash
cd ~/mcp-servers
git clone https://github.com/Shigakuresama/canvas-mcp-developer.git
cd canvas-mcp-developer
npm install
npm run build
```

**Option B: Full-featured (Read/Write access)**
```bash
cd ~/mcp-servers
git clone https://github.com/DMontgomery40/mcp-canvas-lms.git
cd mcp-canvas-lms
npm install
npm run build
```

<!-- section_id: "77d8d1e3-3b07-4e3c-9d13-c4c5d5a3595a" -->
### Step 2: Add to Claude Code CLI

```bash
claude mcp add canvas -s user \
  -e CANVAS_BASE_URL=https://byui.instructure.com \
  -e CANVAS_API_TOKEN=YOUR_ACTUAL_TOKEN_HERE \
  -- node ~/mcp-servers/canvas-mcp-developer/build/index.js
```

Or for the full-featured version:
```bash
claude mcp add canvas -s user \
  -e CANVAS_BASE_URL=https://byui.instructure.com \
  -e CANVAS_API_TOKEN=YOUR_ACTUAL_TOKEN_HERE \
  -- node ~/mcp-servers/mcp-canvas-lms/build/index.js
```

<!-- section_id: "0cda9eec-0029-4b43-a830-85176a085ca2" -->
### Step 3: Using Environment Variables (Recommended for security)

Set in your shell profile (`~/.bashrc` or `~/.zshrc`):
```bash
export CANVAS_API_TOKEN="YOUR_ACTUAL_TOKEN_HERE"
```

Then add to Claude Code:
```bash
source ~/.bashrc
claude mcp add canvas -s user \
  -e CANVAS_BASE_URL=https://byui.instructure.com \
  -e CANVAS_API_TOKEN=$CANVAS_API_TOKEN \
  -- node ~/mcp-servers/canvas-mcp-developer/build/index.js
```

---

<!-- section_id: "a192a1f8-c420-4904-913c-9bc01690fd31" -->
## Getting Your Canvas API Token

1. Log into Canvas at https://byui.instructure.com
2. Go to **Account** (click your profile icon) > **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Purpose: "Claude Code MCP"
6. Click **Generate Token**
7. **Copy the token immediately** - it won't be shown again!

---

<!-- section_id: "b0a8a52a-6899-406d-af59-d51e47d156af" -->
## Verify Setup

After configuring your token:

```bash
# Check MCP servers
claude mcp list

# Expected output:
# canvas: npx -y canvas-mcp-server - ✓ Connected
```

---

<!-- section_id: "b6b4f0f0-30c6-47f0-b9d9-98bfbfcdbbbe" -->
## Available Canvas Tools

Once connected, you'll have access to:
- List courses
- View assignments
- Read announcements
- Check grades
- View discussion posts
- Access course files
- Read quiz questions (after starting quiz)
- Save quiz answers (draft mode)

---

<!-- section_id: "7890f17e-f7fa-4462-8030-7ee3e25b78ee" -->
## Troubleshooting

<!-- section_id: "ec39c504-022a-4bd7-8030-11a3e65da19f" -->
### Server shows "Disconnected" or "Error"
1. Verify your API token is correct
2. Check you can access Canvas at https://byui.instructure.com
3. Try regenerating your API token

<!-- section_id: "3675808d-950a-481a-84f9-917f24921a88" -->
### "401 Unauthorized"
- Your API token may have expired or been revoked
- Generate a new token in Canvas Settings

<!-- section_id: "0e28f8a2-d2b0-4556-a8a8-fa6ce45f0fa7" -->
### Cannot see courses
- Check you're enrolled in active courses
- Semester may not have started yet

---

<!-- section_id: "e2c95629-1121-458b-9925-195281833db8" -->
## Related Files

- Main install guide: `../../../_shared/0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/_shared/0.04_ai_apps/_shared/0.05_mcp_servers/canvas-mcp/INSTALL.md`
- Claude config: `~/.claude.json`
