---
resource_id: "9ecf1d20-3f00-44e3-a550-f83e2a66855c"
resource_type: "document"
resource_name: "CLAUDE_CODE_TESTING_MCP"
---
# Testing Playwright MCP Server

<!-- section_id: "e540bd13-02fa-4d28-a8b6-84001f105b0e" -->
## Prerequisites

✅ `.mcp.json` is at project root
✅ Configuration is correct
✅ Node.js and npx are installed

<!-- section_id: "ee7dcf59-943f-4441-beeb-21b6ba46429a" -->
## How to Test

<!-- section_id: "5e64a7a3-b965-42ae-98a4-282af20d23f6" -->
### Step 1: Restart Claude Code
MCP servers are loaded when the conversation starts. To test:
1. Save any current work
2. Start a **new conversation** in Claude Code
3. The MCP servers should load automatically

<!-- section_id: "7a5fad7a-65d5-47a2-9417-6d913c7289b9" -->
### Step 2: Simple Test
In the new conversation, try:

```
Navigate to google.com and tell me what you see
```

Expected behavior:
- Claude Code should invoke the Playwright MCP server
- Browser will launch (headless mode)
- Page content will be analyzed
- Response with page title and description

<!-- section_id: "7692b3b8-ad15-4a18-8add-1b22b5f25873" -->
### Step 3: Test with Local App
Start your Flask app and test:

```bash
# Terminal 1: Start the app
source .venv/bin/activate
python app.py
```

Then in Claude Code:
```
Navigate to localhost:5000 and describe the login page structure
```

<!-- section_id: "74413115-459b-4587-9c5b-f3ccad44a1e1" -->
### Step 4: Advanced Tests

#### Test Authentication Flow
```
1. Navigate to localhost:5000/login
2. Fill in the login form with test credentials
3. Click the submit button
4. Tell me what page loads next
```

#### Test Responsive Design
```
Navigate to localhost:5000 with a 375px wide viewport and check if the mobile menu appears
```

#### Test Accessibility
```
Navigate to the dashboard page and check for proper ARIA labels and semantic HTML
```

<!-- section_id: "0ac8a0f7-531b-4035-9194-8357ed545108" -->
## Troubleshooting

<!-- section_id: "5b3a4623-9aa4-4797-8cd6-1170e20bbad1" -->
### MCP Server Not Loading
**Symptom**: Claude doesn't recognize browser/navigation commands

**Solutions**:
1. Check `.mcp.json` exists at project root (not in `.claude/`)
2. Verify JSON syntax is valid: `cat .mcp.json | python -m json.tool`
3. Restart Claude Code completely (not just new conversation)
4. Check Claude Code logs for errors

<!-- section_id: "1eff2d4d-38b3-476d-bdc7-337674fdfe40" -->
### First Run is Slow
**Symptom**: First Playwright command takes 1-2 minutes

**Explanation**:
- Playwright downloads browsers on first run (~200MB)
- Subsequent runs use cached browsers (much faster)

**Solution**:
- Pre-install browsers: `npx playwright install`

<!-- section_id: "e6a63a61-01a2-4804-b77f-a45293c681ee" -->
### Browser Not Launching
**Symptom**: Errors about missing browser or dependencies

**Solutions**:
```bash
# Install Playwright browsers
npx playwright install

# Install system dependencies (Linux)
npx playwright install-deps

# Check installation
npx @playwright/mcp@latest --help
```

<!-- section_id: "0afded6d-442f-46e0-92c9-a6e1aba7ce9c" -->
### "Cannot find module" Error
**Symptom**: Error about missing @playwright/mcp

**Solution**:
```bash
# Clear npm cache
npm cache clean --force

# Test manual installation
npx @playwright/mcp@latest
```

<!-- section_id: "07d3ea96-5587-4568-862a-e99137885ea7" -->
## Verification Checklist

- [ ] `.mcp.json` exists at project root
- [ ] JSON syntax is valid
- [ ] Node.js and npx are installed (`which npx`)
- [ ] Started a NEW conversation (not continuing old one)
- [ ] Claude Code was restarted if needed
- [ ] Browser automation commands work

<!-- section_id: "a0410780-00de-41d5-a150-56c9a992f2fe" -->
## Expected Capabilities

Once working, you can ask Claude to:
- ✅ Navigate to any URL
- ✅ Click buttons and links
- ✅ Fill out forms
- ✅ Take screenshots
- ✅ Check page structure and accessibility
- ✅ Test responsive design at different viewports
- ✅ Extract data from pages
- ✅ Verify text content and elements
- ✅ Test multi-step workflows (login → navigate → action)

<!-- section_id: "ab4b0ad8-5210-49ab-a4ab-041041d7c005" -->
## Example Commands

<!-- section_id: "64b5015a-efb1-4c21-8f3e-89cd7a726b83" -->
### Navigation
```
Go to localhost:5000
Navigate to the projects page
```

<!-- section_id: "5952c30b-2142-485b-9a00-23b870a8ffe9" -->
### Form Interaction
```
Fill in the username field with "testuser" and password with "password123"
Click the login button
```

<!-- section_id: "0a01fbb5-2ea0-4016-99ed-cff98a467102" -->
### Verification
```
Check if there's an error message displayed
Verify the page title is "Dashboard"
Look for a button labeled "Create New Project"
```

<!-- section_id: "a3937e49-5913-4ca1-a45e-2bcd36efd9c7" -->
### Screenshots
```
Take a screenshot of the current page
Capture a screenshot of the mobile view at 375px width
```

<!-- section_id: "60f1c3ee-f716-4d6f-ae44-6ef0e2826b84" -->
### Data Extraction
```
Get all the project names from the dashboard
List all the navigation menu items
```

<!-- section_id: "6422919c-2f2b-40b1-8e55-0090efad591f" -->
## Common Use Cases for Lang-Trak

<!-- section_id: "35240ec6-5933-45c8-9e02-2e349d33485e" -->
### Test User Registration
```
1. Navigate to localhost:5000/register
2. Fill in all registration fields
3. Submit the form
4. Verify successful registration or capture any errors
```

<!-- section_id: "8623752c-c0aa-4791-804b-f6e600314cc3" -->
### Test Project Creation
```
1. Log in to the application
2. Navigate to the projects page
3. Click "Create New Project"
4. Fill in project details
5. Verify the project appears in the list
```

<!-- section_id: "5ba7c5d2-be16-4494-b8a5-acfbbcd5665b" -->
### Test Word Creation Workflow
```
1. Navigate to a project's word creation page
2. Test the syllable input workflow
3. Verify suggestions appear as expected
4. Test saving a new word
```

<!-- section_id: "86a1ab8a-e139-4175-a495-60fdc5798c59" -->
### Accessibility Audit
```
Navigate through all main pages and check for:
- Proper heading hierarchy (h1, h2, h3)
- ARIA labels on interactive elements
- Keyboard navigation support
- Semantic HTML usage
```

<!-- section_id: "7240fe18-09d3-4af4-bbb7-9fcb7e708218" -->
## Success Indicators

✅ You see MCP server loading messages in Claude Code
✅ Browser automation commands are understood
✅ Playwright launches browsers and navigates pages
✅ Page content is analyzed and reported back
✅ Multi-step workflows execute successfully

<!-- section_id: "42504b34-3a39-465d-bed8-786a076b5575" -->
## If Still Not Working

1. Check Claude Code version (needs MCP support)
2. Look for `.mcp.json` syntax errors
3. Verify npx can run: `npx --version`
4. Try manual MCP invocation: `npx @playwright/mcp@latest`
5. Check Claude Code settings/preferences for MCP configuration
6. Consult [docs/setup/MCP_SERVER_SETUP.md](MCP_SERVER_SETUP.md) for detailed setup

---

**Last Updated**: October 16, 2025
**Status**: Configuration complete, ready for testing in new conversation
