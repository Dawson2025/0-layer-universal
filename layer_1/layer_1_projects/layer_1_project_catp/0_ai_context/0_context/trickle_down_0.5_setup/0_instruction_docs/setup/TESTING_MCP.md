---
resource_id: "978f1534-10f8-40af-bceb-14f77534bf91"
resource_type: "document"
resource_name: "TESTING_MCP"
---
# Testing Playwright MCP Server

<!-- section_id: "f108dfc3-eb2a-4694-93ca-1a03c43f4a17" -->
## Prerequisites

✅ `.mcp.json` is at project root
✅ Configuration is correct
✅ Node.js and npx are installed

<!-- section_id: "3cb41167-23b3-4593-af18-34c8f1b2fc0f" -->
## How to Test

<!-- section_id: "d3ce6919-f708-448a-abbb-b1a9e05f785b" -->
### Step 1: Restart Claude Code
MCP servers are loaded when the conversation starts. To test:
1. Save any current work
2. Start a **new conversation** in Claude Code
3. The MCP servers should load automatically

<!-- section_id: "6303f497-a774-4a97-b197-c98c9b46d716" -->
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

<!-- section_id: "7ac4a93f-20ab-4f6f-b78b-0879be900a29" -->
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

<!-- section_id: "9680e091-ad19-47bd-ba1f-457155ff6182" -->
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

<!-- section_id: "8e2b4445-b23d-4ea6-8ad3-6f9e4bf3c021" -->
## Troubleshooting

<!-- section_id: "d65e64ef-bf9c-4dce-9bbb-03116420127d" -->
### MCP Server Not Loading
**Symptom**: Claude doesn't recognize browser/navigation commands

**Solutions**:
1. Check `.mcp.json` exists at project root (not in `.claude/`)
2. Verify JSON syntax is valid: `cat .mcp.json | python -m json.tool`
3. Restart Claude Code completely (not just new conversation)
4. Check Claude Code logs for errors

<!-- section_id: "c651c60e-9ca0-4727-a27c-070ac4828f95" -->
### First Run is Slow
**Symptom**: First Playwright command takes 1-2 minutes

**Explanation**:
- Playwright downloads browsers on first run (~200MB)
- Subsequent runs use cached browsers (much faster)

**Solution**:
- Pre-install browsers: `npx playwright install`

<!-- section_id: "4414da7a-9d06-44e9-a6ea-5a8349869631" -->
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

<!-- section_id: "284aa9a3-0da1-4e0f-8439-f26c2403bf90" -->
### "Cannot find module" Error
**Symptom**: Error about missing @playwright/mcp

**Solution**:
```bash
# Clear npm cache
npm cache clean --force

# Test manual installation
npx @playwright/mcp@latest
```

<!-- section_id: "a14043f4-3190-4584-8b07-444f825f4f6f" -->
## Verification Checklist

- [ ] `.mcp.json` exists at project root
- [ ] JSON syntax is valid
- [ ] Node.js and npx are installed (`which npx`)
- [ ] Started a NEW conversation (not continuing old one)
- [ ] Claude Code was restarted if needed
- [ ] Browser automation commands work

<!-- section_id: "5929c94f-fac1-4081-b71a-d44042af6c23" -->
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

<!-- section_id: "8d4ef03e-c1bc-4ad4-b949-cab51494a8d8" -->
## Example Commands

<!-- section_id: "6406bbef-d1fa-4c15-9813-daa1068a2d84" -->
### Navigation
```
Go to localhost:5000
Navigate to the projects page
```

<!-- section_id: "f0036a6d-fb16-43a4-b874-a7fa98650377" -->
### Form Interaction
```
Fill in the username field with "testuser" and password with "password123"
Click the login button
```

<!-- section_id: "0c4085ce-59f0-424b-9813-b7307f3d8a8a" -->
### Verification
```
Check if there's an error message displayed
Verify the page title is "Dashboard"
Look for a button labeled "Create New Project"
```

<!-- section_id: "ad76f07a-0dcd-4dff-b012-2dd7c75587f6" -->
### Screenshots
```
Take a screenshot of the current page
Capture a screenshot of the mobile view at 375px width
```

<!-- section_id: "c7a2d588-b427-4f78-addb-5df7ee0ad583" -->
### Data Extraction
```
Get all the project names from the dashboard
List all the navigation menu items
```

<!-- section_id: "550fdca8-7bd8-40c8-8fc6-ffd83f0c868c" -->
## Common Use Cases for Lang-Trak

<!-- section_id: "d2927949-3bc5-4b5d-ac03-20babf60347d" -->
### Test User Registration
```
1. Navigate to localhost:5000/register
2. Fill in all registration fields
3. Submit the form
4. Verify successful registration or capture any errors
```

<!-- section_id: "b3968256-5155-410f-85aa-4858d030353e" -->
### Test Project Creation
```
1. Log in to the application
2. Navigate to the projects page
3. Click "Create New Project"
4. Fill in project details
5. Verify the project appears in the list
```

<!-- section_id: "24ed53bf-6b7c-4eb2-a5f0-b21d078eaaef" -->
### Test Word Creation Workflow
```
1. Navigate to a project's word creation page
2. Test the syllable input workflow
3. Verify suggestions appear as expected
4. Test saving a new word
```

<!-- section_id: "0e5db0b3-9e83-4d7c-a446-d63423e9384d" -->
### Accessibility Audit
```
Navigate through all main pages and check for:
- Proper heading hierarchy (h1, h2, h3)
- ARIA labels on interactive elements
- Keyboard navigation support
- Semantic HTML usage
```

<!-- section_id: "165c913c-0a38-4bdd-aa69-0fdea7a5ace4" -->
## Success Indicators

✅ You see MCP server loading messages in Claude Code
✅ Browser automation commands are understood
✅ Playwright launches browsers and navigates pages
✅ Page content is analyzed and reported back
✅ Multi-step workflows execute successfully

<!-- section_id: "d87399e8-dc5a-4107-8bd0-645a971586d0" -->
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
