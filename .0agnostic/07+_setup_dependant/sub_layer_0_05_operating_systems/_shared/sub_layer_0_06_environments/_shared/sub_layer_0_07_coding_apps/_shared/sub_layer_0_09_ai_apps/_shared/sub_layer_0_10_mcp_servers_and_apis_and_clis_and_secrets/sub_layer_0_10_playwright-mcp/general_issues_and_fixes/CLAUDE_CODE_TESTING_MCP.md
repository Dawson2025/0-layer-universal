---
resource_id: "872a12c8-8def-4827-84cc-67c9e65c90cc"
resource_type: "document"
resource_name: "CLAUDE_CODE_TESTING_MCP"
---
# Testing Playwright MCP Server

<!-- section_id: "8fefaeaf-bc89-4bec-93da-8657c59dc26a" -->
## Prerequisites

✅ `.mcp.json` is at project root
✅ Configuration is correct
✅ Node.js and npx are installed

<!-- section_id: "e9aaf7d7-888e-47e4-bd34-5acdb99bdf9e" -->
## How to Test

<!-- section_id: "3886f027-b440-4c1b-b4bc-91c8ab78ec25" -->
### Step 1: Restart Claude Code
MCP servers are loaded when the conversation starts. To test:
1. Save any current work
2. Start a **new conversation** in Claude Code
3. The MCP servers should load automatically

<!-- section_id: "09b48061-ca22-4da0-ae58-e3de4b8ecffb" -->
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

<!-- section_id: "93f3a2f4-e128-45dd-932d-3570c53cb0f7" -->
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

<!-- section_id: "5b027f98-2d34-44b0-a6ae-e9c9386cf1eb" -->
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

<!-- section_id: "148e7ff9-66ec-4734-b98a-b8fb49d32f69" -->
## Troubleshooting

<!-- section_id: "04764bf7-619a-42da-ba13-76af540e1f2e" -->
### MCP Server Not Loading
**Symptom**: Claude doesn't recognize browser/navigation commands

**Solutions**:
1. Check `.mcp.json` exists at project root (not in `.claude/`)
2. Verify JSON syntax is valid: `cat .mcp.json | python -m json.tool`
3. Restart Claude Code completely (not just new conversation)
4. Check Claude Code logs for errors

<!-- section_id: "e8bc310f-8cf6-4b37-8a6e-54599bca7a5b" -->
### First Run is Slow
**Symptom**: First Playwright command takes 1-2 minutes

**Explanation**:
- Playwright downloads browsers on first run (~200MB)
- Subsequent runs use cached browsers (much faster)

**Solution**:
- Pre-install browsers: `npx playwright install`

<!-- section_id: "1dd4bfc1-ec62-4faa-9bd7-4e5eb115b9ff" -->
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

<!-- section_id: "dac85de9-bdeb-4a32-895e-08437f928ffa" -->
### "Cannot find module" Error
**Symptom**: Error about missing @playwright/mcp

**Solution**:
```bash
# Clear npm cache
npm cache clean --force

# Test manual installation
npx @playwright/mcp@latest
```

<!-- section_id: "d491754a-9c49-4489-b393-4275e6c12b1d" -->
## Verification Checklist

- [ ] `.mcp.json` exists at project root
- [ ] JSON syntax is valid
- [ ] Node.js and npx are installed (`which npx`)
- [ ] Started a NEW conversation (not continuing old one)
- [ ] Claude Code was restarted if needed
- [ ] Browser automation commands work

<!-- section_id: "69e4fa37-8adb-49f7-858f-310c81e1fceb" -->
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

<!-- section_id: "c77e74b8-6539-4015-a363-71cc37f82676" -->
## Example Commands

<!-- section_id: "ddee703c-f789-400d-a836-ce7d26cf8e96" -->
### Navigation
```
Go to localhost:5000
Navigate to the projects page
```

<!-- section_id: "73d21d3b-af75-41a6-9511-7b30c45b5da5" -->
### Form Interaction
```
Fill in the username field with "testuser" and password with "password123"
Click the login button
```

<!-- section_id: "173e5ded-fba9-442b-ad88-a129e1aead07" -->
### Verification
```
Check if there's an error message displayed
Verify the page title is "Dashboard"
Look for a button labeled "Create New Project"
```

<!-- section_id: "257895f8-58c9-42a9-ba96-3a51eba27f4e" -->
### Screenshots
```
Take a screenshot of the current page
Capture a screenshot of the mobile view at 375px width
```

<!-- section_id: "7f279bb5-fcaf-4649-a0be-aa8ae1458d00" -->
### Data Extraction
```
Get all the project names from the dashboard
List all the navigation menu items
```

<!-- section_id: "7bf4ea1a-8c10-4fe4-ab87-e22a2aee2616" -->
## Common Use Cases for Lang-Trak

<!-- section_id: "7db10b94-3ca3-433b-bf7c-3388a6590655" -->
### Test User Registration
```
1. Navigate to localhost:5000/register
2. Fill in all registration fields
3. Submit the form
4. Verify successful registration or capture any errors
```

<!-- section_id: "0d0aec46-21e6-4ebb-b348-0df0841d75e1" -->
### Test Project Creation
```
1. Log in to the application
2. Navigate to the projects page
3. Click "Create New Project"
4. Fill in project details
5. Verify the project appears in the list
```

<!-- section_id: "56938af1-c869-4293-9ae8-45efa2454aa8" -->
### Test Word Creation Workflow
```
1. Navigate to a project's word creation page
2. Test the syllable input workflow
3. Verify suggestions appear as expected
4. Test saving a new word
```

<!-- section_id: "ca67ab49-e55b-4c2c-85bb-d79adc4d2468" -->
### Accessibility Audit
```
Navigate through all main pages and check for:
- Proper heading hierarchy (h1, h2, h3)
- ARIA labels on interactive elements
- Keyboard navigation support
- Semantic HTML usage
```

<!-- section_id: "f33adf9a-9e52-4828-8b67-e3716eb8cd84" -->
## Success Indicators

✅ You see MCP server loading messages in Claude Code
✅ Browser automation commands are understood
✅ Playwright launches browsers and navigates pages
✅ Page content is analyzed and reported back
✅ Multi-step workflows execute successfully

<!-- section_id: "26e8111b-376a-4703-bf5c-ab6db1453eb4" -->
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
