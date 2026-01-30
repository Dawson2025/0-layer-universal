# Canvas MCP Setup for Claude Code CLI in Cursor (Linux Ubuntu)

## Setup Status

**Note**: Canvas MCP servers are GitHub-based projects and require manual installation.
There is no npm package available.

---

## Installation Steps

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

## Getting Your Canvas API Token

1. Log into Canvas at https://byui.instructure.com
2. Go to **Account** (click your profile icon) > **Settings**
3. Scroll to **Approved Integrations**
4. Click **+ New Access Token**
5. Purpose: "Claude Code MCP"
6. Click **Generate Token**
7. **Copy the token immediately** - it won't be shown again!

---

## Verify Setup

After configuring your token:

```bash
# Check MCP servers
claude mcp list

# Expected output:
# canvas: npx -y canvas-mcp-server - ✓ Connected
```

---

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

## Troubleshooting

### Server shows "Disconnected" or "Error"
1. Verify your API token is correct
2. Check you can access Canvas at https://byui.instructure.com
3. Try regenerating your API token

### "401 Unauthorized"
- Your API token may have expired or been revoked
- Generate a new token in Canvas Settings

### Cannot see courses
- Check you're enrolled in active courses
- Semester may not have started yet

---

## Related Files

- Main install guide: `../../../_shared/0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/_shared/0.04_ai_apps/_shared/0.05_mcp_servers/canvas-mcp/INSTALL.md`
- Claude config: `~/.claude.json`
