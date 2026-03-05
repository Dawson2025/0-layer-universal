---
resource_id: "d35c571d-5de4-451f-81df-3ab9585ccce3"
resource_type: "document"
resource_name: "github_browser_automation"
---
# GitHub Browser Automation Protocol (Playwright MCP)

## Overview

This protocol defines standard procedures for automating GitHub operations via the Playwright MCP server. These operations should be used when CLI tools (like `gh`) are unavailable or when browser-based interaction is required.

## Pre-Requisites

1. Playwright MCP server must be running and accessible
2. User must be logged into GitHub in the browser session
3. Browser instance must be available (not in use by another process)

## Handling Browser Conflicts

If you encounter "Browser is already in use" errors:

```bash
# Kill any running Playwright MCP chrome instances
pkill -f "chrome.*mcp-chrome" || pkill -f "chromium.*mcp" || echo "No matching processes found"
```

Then retry the browser operation.

---

## Protocol 1: Creating a New GitHub Repository

### Steps

1. **Navigate to new repo page**
   ```
   mcp__playwright__browser_navigate → https://github.com/new
   ```

2. **Select owner** (if multiple accounts/orgs available)
   - Click "Choose an owner" button
   - Select the appropriate owner from dropdown

3. **Enter repository name**
   - Type in the "Repository name" textbox
   - Follow naming conventions (see git_repository_creation_rule.md)

4. **Set visibility to PRIVATE** (MANDATORY by default)
   - Look for "Public" button in Configuration section
   - Click to open visibility options
   - Select "Private" option

   **CRITICAL**: All repos must be PRIVATE unless explicitly told otherwise.

5. **Optional configurations**
   - Add README: Toggle if needed
   - Add .gitignore: Select appropriate template
   - Add license: Select if needed

6. **Create repository**
   - Click "Create repository" button
   - Wait for redirect to new repo page
   - Verify "Private" badge appears on repo page

### Verification

After creation, confirm:
- URL matches expected pattern: `https://github.com/{owner}/{repo-name}`
- "Private" badge is visible
- Clone URL is available

---

## Protocol 2: Changing Repository Visibility

### Making a Repository Private

1. **Navigate to settings**
   ```
   mcp__playwright__browser_navigate → https://github.com/{owner}/{repo}/settings
   ```

2. **Scroll to Danger Zone**
   - Scroll down the page until "Danger Zone" section is visible

3. **Click Change visibility**
   - Click "Change visibility" button
   - Select "Change to private" from dropdown

4. **Confirm the change**
   - Click "I want to make this repository private"
   - Click "I have read and understand these effects"
   - Click "Make this repository private"

5. **Verify**
   - Page should refresh
   - Lock icon should appear next to repo name
   - Danger Zone should now show "This repository is currently private"

### Making a Repository Public

**WARNING**: Only do this when explicitly instructed by user.

Follow same steps but select "Change to public" instead.

---

## Protocol 3: Renaming a Repository

1. **Navigate to settings**
   ```
   mcp__playwright__browser_navigate → https://github.com/{owner}/{repo}/settings
   ```

2. **Find Repository name field**
   - Located at top of General settings
   - Clear existing name and enter new name

3. **Click Rename**
   - Click the "Rename" button
   - Confirm the rename if prompted

4. **Update local remotes**
   After renaming, update local git config:
   ```bash
   git remote set-url origin https://github.com/{owner}/{new-name}.git
   ```

---

## Protocol 4: Managing Collaborators/Access

1. **Navigate to access settings**
   ```
   mcp__playwright__browser_navigate → https://github.com/{owner}/{repo}/settings/access
   ```

2. **Add collaborators**
   - Click "Add people" or "Invite collaborators"
   - Search by username or email
   - Select permission level

**NOTE**: Modifying access controls requires explicit user permission per safety rules.

---

## Protocol 5: Creating/Managing Releases

1. **Navigate to releases**
   ```
   mcp__playwright__browser_navigate → https://github.com/{owner}/{repo}/releases/new
   ```

2. **Fill release details**
   - Choose/create a tag
   - Set release title
   - Add description
   - Attach binaries if needed

3. **Publish**
   - Click "Publish release" (or "Save draft")

---

## Common Element References

When using Playwright, these are typical element patterns:

| Action | Element Pattern |
|--------|-----------------|
| Owner dropdown | `button "Choose an owner"` |
| Repo name input | `textbox "Repository name"` |
| Visibility button | `button "Public"` or `button "Private"` |
| Create repo button | `button "Create repository"` |
| Settings navigation | `link "Settings"` |
| Danger zone buttons | Look for red-styled buttons |

---

## Error Handling

### Browser Not Responding
```bash
pkill -f "chrome.*mcp-chrome"
# Then retry operation
```

### Authentication Required
If GitHub requires re-authentication:
1. Inform user that authentication is needed
2. Wait for user to complete 2FA/password
3. Continue with operation

### Rate Limiting
If GitHub shows rate limit errors:
1. Wait 60 seconds
2. Retry operation
3. If persistent, inform user

---

## Best Practices

1. **Always verify repo exists before operations** - Check if repo already exists to avoid duplicates
2. **Private by default** - Never create public repos unless explicitly instructed
3. **Take snapshots** - Use `browser_snapshot` to verify page state before critical actions
4. **Handle modals carefully** - GitHub often uses multi-step confirmation modals
5. **Clean up browser** - Close browser sessions when done to free resources

---

**Last Updated**: 2026-01-12
**Applies To**: Playwright MCP Server for Claude Code CLI
