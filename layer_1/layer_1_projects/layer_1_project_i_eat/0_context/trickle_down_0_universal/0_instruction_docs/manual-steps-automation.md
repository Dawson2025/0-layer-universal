---
resource_id: "be72ce16-30e8-4685-9e80-505f5f7d893b"
resource_type: "document"
resource_name: "manual-steps-automation"
---
# Manual Steps Automation Protocol
*Universal AI Agent Manual Task Execution Rules*

<!-- section_id: "4a3522f1-6121-47c7-82f2-40a3602f8e9a" -->
## 🚨 **CRITICAL: AI Agents Must Execute Manual Steps**

**RULE**: When there are manual steps required to complete a task, the AI agent MUST execute them directly using available tools, NOT delegate them to the user.

<!-- section_id: "8d5fc690-627f-49a4-92e4-41b487f15849" -->
## 🔧 **Available Manual Step Execution Tools**

<!-- section_id: "23d18673-8eea-40f5-9482-5c2420dbdbd0" -->
### **Browser Automation Tools**
- **Playwright MCP**: `mcp_playwright_browser_*` - Full browser automation
- **Chrome DevTools MCP**: `mcp_chrome-devtools_*` - Chrome-specific automation
- **Browser MCP**: `mcp_browser_browser_*` - General browser operations

<!-- section_id: "93d5fdcb-0b9d-4bb4-b328-d08389532ea5" -->
### **Web Interface Interaction**
- **Navigate**: `mcp_browser_browser_navigate` - Go to URLs
- **Click**: `mcp_playwright_browser_click` - Click elements
- **Type**: `mcp_playwright_browser_type` - Fill forms
- **Select**: `mcp_playwright_browser_select_option` - Choose dropdown options
- **Wait**: `mcp_playwright_browser_wait_for` - Wait for elements/conditions

<!-- section_id: "f2e4dfba-b1ba-46ca-9709-99a030631ec8" -->
### **Form Filling**
- **Single Field**: `mcp_playwright_browser_type` - Type into specific fields
- **Multiple Fields**: `mcp_playwright_browser_fill_form` - Fill entire forms
- **File Upload**: `mcp_playwright_browser_file_upload` - Upload files

<!-- section_id: "95c17c2a-9448-4ca9-87b3-fc10121947d5" -->
## 📋 **Manual Step Execution Protocol**

<!-- section_id: "64a23d73-cf38-4b0b-9b14-13da0a8253da" -->
### **Step 1: Identify Manual Requirements**
- Analyze the task to identify manual steps
- Determine which tools are needed
- Plan the automation sequence

<!-- section_id: "5f5da626-b57a-4708-a807-05662e522f31" -->
### **Step 2: Execute Browser Automation**
- Navigate to required URLs
- Interact with web interfaces
- Fill forms and configure settings
- Complete all required manual steps

<!-- section_id: "53605174-f7f6-4256-b190-3ed6a4e87fa7" -->
### **Step 3: Verify Completion**
- Check that all steps were completed successfully
- Verify the expected outcome
- Run verification scripts to confirm

<!-- section_id: "f7947401-35db-4378-864f-a4a6c2e4a285" -->
## ⚠️ **Critical Rules**

<!-- section_id: "0bda7657-b8bd-4dbd-9fee-21499d403d32" -->
### **❌ NEVER:**
- Delegate manual steps to the user
- Provide instructions for user to follow
- Ask user to "click this" or "fill that"
- Create scripts that require user interaction

<!-- section_id: "64efb02b-5fd2-4e20-8deb-23eab2125e59" -->
### **✅ ALWAYS:**
- Use browser automation tools directly
- Execute all manual steps yourself
- Complete the entire task end-to-end
- Verify results automatically

<!-- section_id: "0f8fcb95-d467-4cc1-8810-dfb0d82e33ac" -->
## 🎯 **Common Manual Step Scenarios**

<!-- section_id: "7f8954b2-6d90-4653-a006-f38fcd621472" -->
### **OAuth Consent Screen Setup**
- Navigate to Google Cloud Console
- Click "CONFIGURE CONSENT SCREEN"
- Fill in app details and contact information
- Configure scopes and test users
- Save and verify completion

<!-- section_id: "8dabdf60-e674-4cb8-b6bc-04b5d0e273d8" -->
### **Firebase Console Configuration**
- Navigate to Firebase Console
- Access authentication providers
- Enable Google Sign-In provider
- Configure provider settings
- Save changes

<!-- section_id: "9f2f074c-9aef-44c8-a1c1-ca2df7718541" -->
### **API Key Management**
- Navigate to API credentials pages
- Generate or configure API keys
- Set permissions and restrictions
- Copy keys for use in applications

<!-- section_id: "62d1bb7b-764e-4e73-a2e5-2f81b603545d" -->
### **Service Configuration**
- Access service configuration pages
- Modify settings and parameters
- Enable/disable features
- Save and apply changes

<!-- section_id: "50d874c8-2f18-423d-90be-2fef348fec05" -->
## 🛠️ **Tool Selection Guide**

| Task Type | Primary Tool | Fallback Tool |
|-----------|--------------|---------------|
| **General Browser** | `mcp_browser_browser_*` | `mcp_playwright_browser_*` |
| **Complex Forms** | `mcp_playwright_browser_*` | `mcp_chrome-devtools_*` |
| **File Uploads** | `mcp_playwright_browser_*` | `mcp_browser_browser_*` |
| **Chrome-specific** | `mcp_chrome-devtools_*` | `mcp_playwright_browser_*` |

<!-- section_id: "f7222c01-08a2-4139-bbe6-750cc427efd8" -->
## 📝 **Implementation Examples**

<!-- section_id: "d72484d2-16a6-4c5b-8616-6595fcf65a6e" -->
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

<!-- section_id: "07d86b05-2efb-4dbe-ad38-48e12fbb2017" -->
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

<!-- section_id: "cf39d3aa-4948-4c23-b4bd-fb8c0f03ac54" -->
## 🔍 **Verification Protocol**

After completing manual steps:
1. **Run verification scripts** to confirm changes
2. **Check API responses** for expected results
3. **Test functionality** end-to-end
4. **Document completion** in TODO list

<!-- section_id: "865dce36-878d-4225-8950-0bc53ef704a4" -->
## 📚 **Related Documentation**

- **Terminal Tool Replacement**: `terminal-tool-replacement.md`
- **Browser Automation Strategy**: `browser_automation_strategy.md`
- **Universal Instructions**: `universal_instructions.md`

---

**⚠️ CRITICAL REMINDER: AI agents must execute ALL manual steps directly using available tools. Never delegate manual tasks to users!**
