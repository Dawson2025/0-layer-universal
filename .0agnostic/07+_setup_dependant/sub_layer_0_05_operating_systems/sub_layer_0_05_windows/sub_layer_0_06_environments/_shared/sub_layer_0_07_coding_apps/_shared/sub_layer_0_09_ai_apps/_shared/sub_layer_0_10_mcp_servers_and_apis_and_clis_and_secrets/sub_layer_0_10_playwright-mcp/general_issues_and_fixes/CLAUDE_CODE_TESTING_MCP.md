---
resource_id: "3020fcc0-6351-43a6-aed7-eb44f1615084"
resource_type: "document"
resource_name: "CLAUDE_CODE_TESTING_MCP"
---
# Testing Playwright MCP Server

<!-- section_id: "a9c3c47d-4574-4ce5-97a1-e9c773e08476" -->
## Prerequisites

✅ `.mcp.json` is at project root
✅ Configuration is correct
✅ Node.js and npx are installed

<!-- section_id: "e43c0e69-15bc-46b8-99c7-2e1da7682229" -->
## How to Test

<!-- section_id: "90a79c52-3201-4a3b-800d-6b8dc76293ef" -->
### Step 1: Restart Claude Code
MCP servers are loaded when the conversation starts. To test:
1. Save any current work
2. Start a **new conversation** in Claude Code
3. The MCP servers should load automatically

<!-- section_id: "220aebfc-14ec-46fe-ac43-94d114019c74" -->
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

<!-- section_id: "1e17e183-d327-48fb-abed-a774923d763f" -->
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

<!-- section_id: "da190a85-0079-429f-9985-3a3b8322c5af" -->
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

<!-- section_id: "6f72c841-dfdc-493a-824d-9f6499755dc5" -->
## Troubleshooting

<!-- section_id: "6d08be3c-907d-4ebb-8fea-c0c358b61ba8" -->
### MCP Server Not Loading
**Symptom**: Claude doesn't recognize browser/navigation commands

**Solutions**:
1. Check `.mcp.json` exists at project root (not in `.claude/`)
2. Verify JSON syntax is valid: `cat .mcp.json | python -m json.tool`
3. Restart Claude Code completely (not just new conversation)
4. Check Claude Code logs for errors

<!-- section_id: "cedce1ba-d65b-4a5a-819c-105e859ea09c" -->
### First Run is Slow
**Symptom**: First Playwright command takes 1-2 minutes

**Explanation**:
- Playwright downloads browsers on first run (~200MB)
- Subsequent runs use cached browsers (much faster)

**Solution**:
- Pre-install browsers: `npx playwright install`

<!-- section_id: "c1ede874-2062-40f8-818b-9209989b9864" -->
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

<!-- section_id: "4cca7a97-8209-4e9b-864a-f66ee2000415" -->
### "Cannot find module" Error
**Symptom**: Error about missing @playwright/mcp

**Solution**:
```bash
# Clear npm cache
npm cache clean --force

# Test manual installation
npx @playwright/mcp@latest
```

<!-- section_id: "18c89665-da29-4e8e-974e-a3fe3008577b" -->
## Verification Checklist

- [ ] `.mcp.json` exists at project root
- [ ] JSON syntax is valid
- [ ] Node.js and npx are installed (`which npx`)
- [ ] Started a NEW conversation (not continuing old one)
- [ ] Claude Code was restarted if needed
- [ ] Browser automation commands work

<!-- section_id: "aa3ac4ed-c870-482a-957d-b61624c74c88" -->
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

<!-- section_id: "0e19014a-df2a-4a38-96c1-c2dca479f7f8" -->
## Example Commands

<!-- section_id: "9ef1aa92-b027-429a-b8e2-e19fb052faea" -->
### Navigation
```
Go to localhost:5000
Navigate to the projects page
```

<!-- section_id: "3eb378b8-b654-4e25-bc48-f508d333e3ca" -->
### Form Interaction
```
Fill in the username field with "testuser" and password with "password123"
Click the login button
```

<!-- section_id: "8688bffa-2305-486c-94ae-cce79de481d0" -->
### Verification
```
Check if there's an error message displayed
Verify the page title is "Dashboard"
Look for a button labeled "Create New Project"
```

<!-- section_id: "7fd41eb3-c43f-4a45-873f-ad0e26e9d490" -->
### Screenshots
```
Take a screenshot of the current page
Capture a screenshot of the mobile view at 375px width
```

<!-- section_id: "e0f0b23a-8447-4670-9838-d2c2a3f193be" -->
### Data Extraction
```
Get all the project names from the dashboard
List all the navigation menu items
```

<!-- section_id: "4335e57c-c620-4257-b167-4071756fb151" -->
## Common Use Cases for Lang-Trak

<!-- section_id: "041e9b3a-f075-4fde-bea4-cf40d84485fe" -->
### Test User Registration
```
1. Navigate to localhost:5000/register
2. Fill in all registration fields
3. Submit the form
4. Verify successful registration or capture any errors
```

<!-- section_id: "70dbc948-b934-4443-91a1-2c7bfa34041f" -->
### Test Project Creation
```
1. Log in to the application
2. Navigate to the projects page
3. Click "Create New Project"
4. Fill in project details
5. Verify the project appears in the list
```

<!-- section_id: "a5dfd723-a347-4757-a310-62c656cc58fb" -->
### Test Word Creation Workflow
```
1. Navigate to a project's word creation page
2. Test the syllable input workflow
3. Verify suggestions appear as expected
4. Test saving a new word
```

<!-- section_id: "629fa71a-bc3e-4608-a228-9aff35377a73" -->
### Accessibility Audit
```
Navigate through all main pages and check for:
- Proper heading hierarchy (h1, h2, h3)
- ARIA labels on interactive elements
- Keyboard navigation support
- Semantic HTML usage
```

<!-- section_id: "91ff5932-790c-4bf2-bec1-d8d9f3e26034" -->
## Success Indicators

✅ You see MCP server loading messages in Claude Code
✅ Browser automation commands are understood
✅ Playwright launches browsers and navigates pages
✅ Page content is analyzed and reported back
✅ Multi-step workflows execute successfully

<!-- section_id: "deb5ef95-e1d9-461c-85da-e80b264b5ff4" -->
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
