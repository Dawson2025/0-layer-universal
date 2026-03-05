---
resource_id: "7ddaa2ee-7d8d-43e7-8e7b-18df9ad54a23"
resource_type: "document"
resource_name: "manual-steps-automation"
---
# Manual Steps Automation Protocol
*Universal AI Agent Manual Task Execution Rules*

<!-- section_id: "042c1eb5-22dd-4c0b-8485-a94a12dc0b2d" -->
## 🚨 **CRITICAL: AI Agents Must Execute Manual Steps**

**RULE**: When there are manual steps required to complete a task, the AI agent MUST execute them directly using available tools, NOT delegate them to the user.

<!-- section_id: "ad1b6782-e52c-4f8c-990a-a1fc0cb18543" -->
## 🔧 **Available Manual Step Execution Tools**

<!-- section_id: "aa19d802-5117-462d-bc09-3c7daaf6e3b2" -->
### **Browser Automation Tools**
- **Playwright MCP**: `mcp_playwright_browser_*` - Full browser automation
- **Chrome DevTools MCP**: `mcp_chrome-devtools_*` - Chrome-specific automation
- **Browser MCP**: `mcp_browser_browser_*` - General browser operations

<!-- section_id: "2937b34d-220d-4e2c-becf-3ab90e621a82" -->
### **Web Interface Interaction**
- **Navigate**: `mcp_browser_browser_navigate` - Go to URLs
- **Click**: `mcp_playwright_browser_click` - Click elements
- **Type**: `mcp_playwright_browser_type` - Fill forms
- **Select**: `mcp_playwright_browser_select_option` - Choose dropdown options
- **Wait**: `mcp_playwright_browser_wait_for` - Wait for elements/conditions

<!-- section_id: "a1a2b26c-2941-4154-91e0-b0debd815cdd" -->
### **Form Filling**
- **Single Field**: `mcp_playwright_browser_type` - Type into specific fields
- **Multiple Fields**: `mcp_playwright_browser_fill_form` - Fill entire forms
- **File Upload**: `mcp_playwright_browser_file_upload` - Upload files

<!-- section_id: "6d782416-676f-4d3d-8ffb-66d4a32e5785" -->
## 📋 **Manual Step Execution Protocol**

<!-- section_id: "4c2d5e64-457c-4713-8377-51db8785c9cd" -->
### **Step 1: Identify Manual Requirements**
- Analyze the task to identify manual steps
- Determine which tools are needed
- Plan the automation sequence

<!-- section_id: "9face242-0827-43b4-8743-ae5bc206d9ab" -->
### **Step 2: Execute Browser Automation**
- Navigate to required URLs
- Interact with web interfaces
- Fill forms and configure settings
- Complete all required manual steps

<!-- section_id: "7c0568fa-6d8b-45ad-8009-6cc0f3429fb2" -->
### **Step 3: Verify Completion**
- Check that all steps were completed successfully
- Verify the expected outcome
- Run verification scripts to confirm

<!-- section_id: "62cf4d84-17b2-4e3c-a2aa-89671b1e729c" -->
## ⚠️ **Critical Rules**

<!-- section_id: "33fb53b7-309f-41d8-a959-03c1a0e3bf70" -->
### **❌ NEVER:**
- Delegate manual steps to the user
- Provide instructions for user to follow
- Ask user to "click this" or "fill that"
- Create scripts that require user interaction

<!-- section_id: "e651ddb8-e77a-48d9-8fb9-75875aeea654" -->
### **✅ ALWAYS:**
- Use browser automation tools directly
- Execute all manual steps yourself
- Complete the entire task end-to-end
- Verify results automatically

<!-- section_id: "2780e161-268c-480d-85fa-c225eeed30b8" -->
## 🎯 **Common Manual Step Scenarios**

<!-- section_id: "70a6e4df-d3b5-463f-a783-6e9e6d6cedee" -->
### **OAuth Consent Screen Setup**
- Navigate to Google Cloud Console
- Click "CONFIGURE CONSENT SCREEN"
- Fill in app details and contact information
- Configure scopes and test users
- Save and verify completion

<!-- section_id: "7eb9aeea-7c5a-4fa4-afa9-8dedeec26a1f" -->
### **Firebase Console Configuration**
- Navigate to Firebase Console
- Access authentication providers
- Enable Google Sign-In provider
- Configure provider settings
- Save changes

<!-- section_id: "83b919ae-3799-4fa5-90a6-4a87fd13f633" -->
### **API Key Management**
- Navigate to API credentials pages
- Generate or configure API keys
- Set permissions and restrictions
- Copy keys for use in applications

<!-- section_id: "f066fd24-09d2-4a86-96cb-20578cb93d16" -->
### **Service Configuration**
- Access service configuration pages
- Modify settings and parameters
- Enable/disable features
- Save and apply changes

<!-- section_id: "ad5b5d8c-7c78-4cf2-8b50-3a1b404141ce" -->
## 🛠️ **Tool Selection Guide**

| Task Type | Primary Tool | Fallback Tool |
|-----------|--------------|---------------|
| **General Browser** | `mcp_browser_browser_*` | `mcp_playwright_browser_*` |
| **Complex Forms** | `mcp_playwright_browser_*` | `mcp_chrome-devtools_*` |
| **File Uploads** | `mcp_playwright_browser_*` | `mcp_browser_browser_*` |
| **Chrome-specific** | `mcp_chrome-devtools_*` | `mcp_playwright_browser_*` |

<!-- section_id: "3b292ca0-5464-4155-9936-fcce204c70da" -->
## 📝 **Implementation Examples**

<!-- section_id: "407b7711-bd67-4cbc-8bb1-193ecc19b941" -->
### **Example 1: OAuth Consent Screen Setup**
```python
# Navigate to OAuth consent screen
mcp_browser_browser_navigate(url="https://console.cloud.google.com/apis/credentials/consent?project=lang-trak-dev")

# Click configure consent screen
mcp_playwright_browser_click(element="CONFIGURE CONSENT SCREEN button")

# Fill in app details
mcp_playwright_browser_type(element="App name field", text="Lang Trak Dev")
mcp_playwright_browser_type(element="Support email field", text="2025computer2025@gmail.com")

# Save and continue
mcp_playwright_browser_click(element="Save button")
```

<!-- section_id: "688ef478-71db-4252-bb0b-68dfbd93dc8f" -->
### **Example 2: Firebase Provider Configuration**
```python
# Navigate to Firebase Console
mcp_browser_browser_navigate(url="https://console.firebase.google.com/u/1/project/lang-trak-dev/authentication/providers")

# Click on Google provider
mcp_playwright_browser_click(element="Google provider row")

# Enable the provider
mcp_playwright_browser_click(element="Enable switch")

# Fill support email
mcp_playwright_browser_type(element="Support email field", text="2025computer2025@gmail.com")

# Save changes
mcp_playwright_browser_click(element="Save button")
```

<!-- section_id: "0fa7b8a5-e554-4a53-ba31-dfc66aecbe78" -->
## 🔍 **Verification Protocol**

After completing manual steps:
1. **Run verification scripts** to confirm changes
2. **Check API responses** for expected results
3. **Test functionality** end-to-end
4. **Document completion** in TODO list

<!-- section_id: "47e5c13a-772c-45cb-87f7-035272468edb" -->
## 📚 **Related Documentation**

- **Terminal Tool Replacement**: `terminal-tool-replacement.md`
- **Browser Automation Strategy**: `browser_automation_strategy.md`
- **Universal Instructions**: `universal_instructions.md`

---

**⚠️ CRITICAL REMINDER: AI agents must execute ALL manual steps directly using available tools. Never delegate manual tasks to users!**
