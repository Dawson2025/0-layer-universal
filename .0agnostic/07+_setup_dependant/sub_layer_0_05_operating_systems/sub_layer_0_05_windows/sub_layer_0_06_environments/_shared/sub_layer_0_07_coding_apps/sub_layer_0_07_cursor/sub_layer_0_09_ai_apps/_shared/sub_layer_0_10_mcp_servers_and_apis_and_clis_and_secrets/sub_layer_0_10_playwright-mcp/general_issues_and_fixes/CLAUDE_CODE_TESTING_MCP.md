---
resource_id: "1e1744be-3ab1-4d65-957a-6d2477cd1ed7"
resource_type: "document"
resource_name: "CLAUDE_CODE_TESTING_MCP"
---
# Testing Playwright MCP Server

<!-- section_id: "d9c2a34d-abaa-4424-8f3b-20cd9c21acf4" -->
## Prerequisites

✅ `.mcp.json` is at project root
✅ Configuration is correct
✅ Node.js and npx are installed

<!-- section_id: "8c0a0938-aaec-4e85-955b-cacc78d92189" -->
## How to Test

<!-- section_id: "f0f1e767-29e9-462f-aaa7-86f4f277d18d" -->
### Step 1: Restart Claude Code
MCP servers are loaded when the conversation starts. To test:
1. Save any current work
2. Start a **new conversation** in Claude Code
3. The MCP servers should load automatically

<!-- section_id: "e9a60a45-3c5c-404f-ae52-03aa34cf27ef" -->
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

<!-- section_id: "f8312ffe-a8a3-4eaf-9fb4-c02d980d9ab6" -->
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

<!-- section_id: "2c39cb07-eba2-4993-9f76-fd734c30d7fc" -->
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

<!-- section_id: "8d023699-960f-4d33-ba66-527fd620474b" -->
## Troubleshooting

<!-- section_id: "44d46e44-0448-49db-ae49-9611b5588762" -->
### MCP Server Not Loading
**Symptom**: Claude doesn't recognize browser/navigation commands

**Solutions**:
1. Check `.mcp.json` exists at project root (not in `.claude/`)
2. Verify JSON syntax is valid: `cat .mcp.json | python -m json.tool`
3. Restart Claude Code completely (not just new conversation)
4. Check Claude Code logs for errors

<!-- section_id: "04d44f00-8158-4902-b5aa-0983054bcdea" -->
### First Run is Slow
**Symptom**: First Playwright command takes 1-2 minutes

**Explanation**:
- Playwright downloads browsers on first run (~200MB)
- Subsequent runs use cached browsers (much faster)

**Solution**:
- Pre-install browsers: `npx playwright install`

<!-- section_id: "d1ddae67-adeb-4df2-9871-a5e2d6d93678" -->
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

<!-- section_id: "a4a1bf2e-d570-4afa-bd6e-7c6f9bc619c5" -->
### "Cannot find module" Error
**Symptom**: Error about missing @playwright/mcp

**Solution**:
```bash
# Clear npm cache
npm cache clean --force

# Test manual installation
npx @playwright/mcp@latest
```

<!-- section_id: "21589a1f-628e-42be-b3fe-124442de8bf5" -->
## Verification Checklist

- [ ] `.mcp.json` exists at project root
- [ ] JSON syntax is valid
- [ ] Node.js and npx are installed (`which npx`)
- [ ] Started a NEW conversation (not continuing old one)
- [ ] Claude Code was restarted if needed
- [ ] Browser automation commands work

<!-- section_id: "a6c6e7bb-fd8f-4013-938c-3333e8f5944e" -->
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

<!-- section_id: "e5652d3d-5ec4-4cda-9355-ecab3151fe4c" -->
## Example Commands

<!-- section_id: "b1a07899-da4c-4165-a746-fcec3f925929" -->
### Navigation
```
Go to localhost:5000
Navigate to the projects page
```

<!-- section_id: "407bbaac-5f60-422b-b8a6-1a572ec6be16" -->
### Form Interaction
```
Fill in the username field with "testuser" and password with "password123"
Click the login button
```

<!-- section_id: "8cd22578-ebc8-4f9b-ab88-46b146940a6f" -->
### Verification
```
Check if there's an error message displayed
Verify the page title is "Dashboard"
Look for a button labeled "Create New Project"
```

<!-- section_id: "91078abd-57cf-4c0f-aaf4-7597b1f5f854" -->
### Screenshots
```
Take a screenshot of the current page
Capture a screenshot of the mobile view at 375px width
```

<!-- section_id: "5a67a1f9-6164-448e-855a-6e10a0bcd373" -->
### Data Extraction
```
Get all the project names from the dashboard
List all the navigation menu items
```

<!-- section_id: "f131ded9-a1c9-442d-8eb7-c8ed005d5f2f" -->
## Common Use Cases for Lang-Trak

<!-- section_id: "8ad0e2d5-ab40-4ebb-8ebd-ceba491fea7f" -->
### Test User Registration
```
1. Navigate to localhost:5000/register
2. Fill in all registration fields
3. Submit the form
4. Verify successful registration or capture any errors
```

<!-- section_id: "f8cb8ee5-f9d9-446c-b343-8ea9a24fa87c" -->
### Test Project Creation
```
1. Log in to the application
2. Navigate to the projects page
3. Click "Create New Project"
4. Fill in project details
5. Verify the project appears in the list
```

<!-- section_id: "8f14e98a-2eed-40dd-8939-b8b980dc1069" -->
### Test Word Creation Workflow
```
1. Navigate to a project's word creation page
2. Test the syllable input workflow
3. Verify suggestions appear as expected
4. Test saving a new word
```

<!-- section_id: "7c5b52c7-b826-482e-b89d-e67610919823" -->
### Accessibility Audit
```
Navigate through all main pages and check for:
- Proper heading hierarchy (h1, h2, h3)
- ARIA labels on interactive elements
- Keyboard navigation support
- Semantic HTML usage
```

<!-- section_id: "b2c7d98d-3fc9-44bb-ba7e-ce09fc430fad" -->
## Success Indicators

✅ You see MCP server loading messages in Claude Code
✅ Browser automation commands are understood
✅ Playwright launches browsers and navigates pages
✅ Page content is analyzed and reported back
✅ Multi-step workflows execute successfully

<!-- section_id: "f6dac235-b429-4732-9df4-356d6a1f7aa2" -->
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
