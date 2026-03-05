---
resource_id: "dce1e194-4fb9-43f7-b6f7-4ca745406a31"
resource_type: "rule"
resource_name: "manual-steps-automation"
---
# Manual Steps Automation Protocol
*Universal AI Agent Manual Task Execution Rules*

<!-- section_id: "a3f35861-0330-427e-ab77-065de535dd5d" -->
## 🚨 **CRITICAL: AI Agents Must Execute Manual Steps**

**RULE**: When there are manual steps required to complete a task, the AI agent MUST execute them directly using available tools, NOT delegate them to the user.

<!-- section_id: "8cd58aee-ad97-4e29-b270-a9117b483067" -->
## 🔧 **Available Manual Step Execution Tools**

<!-- section_id: "e8f35698-d888-4010-9af5-b29fcfc51b14" -->
### **Browser Automation Tools**
- **Playwright MCP**: `mcp_playwright_browser_*` - Full browser automation
- **Chrome DevTools MCP**: `mcp_chrome-devtools_*` - Chrome-specific automation
- **Browser MCP**: `mcp_browser_browser_*` - General browser operations

<!-- section_id: "34be046d-652e-4e8a-97c8-5e8b3612e441" -->
### **Web Interface Interaction**
- **Navigate**: `mcp_browser_browser_navigate` - Go to URLs
- **Click**: `mcp_playwright_browser_click` - Click elements
- **Type**: `mcp_playwright_browser_type` - Fill forms
- **Select**: `mcp_playwright_browser_select_option` - Choose dropdown options
- **Wait**: `mcp_playwright_browser_wait_for` - Wait for elements/conditions

<!-- section_id: "9caf7904-30de-4485-b827-5beda06b595f" -->
### **Form Filling**
- **Single Field**: `mcp_playwright_browser_type` - Type into specific fields
- **Multiple Fields**: `mcp_playwright_browser_fill_form` - Fill entire forms
- **File Upload**: `mcp_playwright_browser_file_upload` - Upload files

<!-- section_id: "c155332e-280c-4ace-8cfd-94c5a4aded94" -->
## 📋 **Manual Step Execution Protocol**

<!-- section_id: "e5c500a9-f70c-46bb-a3dc-c62f784ff06c" -->
### **Step 1: Identify Manual Requirements**
- Analyze the task to identify manual steps
- Determine which tools are needed
- Plan the automation sequence

<!-- section_id: "675b929c-7eaa-4f75-b1c9-0d3ba5cb4cd9" -->
### **Step 2: Execute Browser Automation**
- Navigate to required URLs
- Interact with web interfaces
- Fill forms and configure settings
- Complete all required manual steps

<!-- section_id: "5622b99d-08ea-4d61-9fba-06acd3db361f" -->
### **Step 3: Verify Completion**
- Check that all steps were completed successfully
- Verify the expected outcome
- Run verification scripts to confirm

<!-- section_id: "e1819491-6a7b-4b81-8b4e-053713d14a5c" -->
## ⚠️ **Critical Rules**

<!-- section_id: "93563a54-bff0-4c0c-9f75-e9777e48fa86" -->
### **❌ NEVER:**
- Delegate manual steps to the user
- Provide instructions for user to follow
- Ask user to "click this" or "fill that"
- Create scripts that require user interaction

<!-- section_id: "22e8ffa6-c98b-4c4c-bfef-167140f1379a" -->
### **✅ ALWAYS:**
- Use browser automation tools directly
- Execute all manual steps yourself
- Complete the entire task end-to-end
- Verify results automatically

<!-- section_id: "72d98933-6cec-44bb-967d-4179863b02d6" -->
## 🎯 **Common Manual Step Scenarios**

<!-- section_id: "16562e3b-3563-4b8a-ae86-d02192c4aa10" -->
### **OAuth Consent Screen Setup**
- Navigate to Google Cloud Console
- Click "CONFIGURE CONSENT SCREEN"
- Fill in app details and contact information
- Configure scopes and test users
- Save and verify completion

<!-- section_id: "a2b31167-91fc-4107-9032-3ecf2aa21320" -->
### **Firebase Console Configuration**
- Navigate to Firebase Console
- Access authentication providers
- Enable Google Sign-In provider
- Configure provider settings
- Save changes

<!-- section_id: "7281f9e0-82e7-4ad4-9826-5520afe9c5c6" -->
### **API Key Management**
- Navigate to API credentials pages
- Generate or configure API keys
- Set permissions and restrictions
- Copy keys for use in applications

<!-- section_id: "a79570bf-6d6e-43d1-ab6f-453b6faf4280" -->
### **Service Configuration**
- Access service configuration pages
- Modify settings and parameters
- Enable/disable features
- Save and apply changes

<!-- section_id: "22be4069-7001-4b55-9dca-fcf2bf2406cf" -->
## 🛠️ **Tool Selection Guide**

| Task Type | Primary Tool | Fallback Tool |
|-----------|--------------|---------------|
| **General Browser** | `mcp_browser_browser_*` | `mcp_playwright_browser_*` |
| **Complex Forms** | `mcp_playwright_browser_*` | `mcp_chrome-devtools_*` |
| **File Uploads** | `mcp_playwright_browser_*` | `mcp_browser_browser_*` |
| **Chrome-specific** | `mcp_chrome-devtools_*` | `mcp_playwright_browser_*` |

<!-- section_id: "07be8b42-f9a3-4b6f-9c00-8f218acf6154" -->
## 📝 **Implementation Examples**

<!-- section_id: "d4bd076f-2bf8-4ec7-8570-65e6ffbafb61" -->
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

<!-- section_id: "63fb51b2-22df-4806-b472-8b15b7c4319e" -->
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

<!-- section_id: "afc204cd-b4a2-4b27-be83-14fc279381e2" -->
## 🔍 **Verification Protocol**

After completing manual steps:
1. **Run verification scripts** to confirm changes
2. **Check API responses** for expected results
3. **Test functionality** end-to-end
4. **Document completion** in TODO list

<!-- section_id: "cb10f6dc-0e4a-436f-bfb0-2d15e766ccdb" -->
## 📚 **Related Documentation**

- **Terminal Tool Replacement**: `terminal-tool-replacement.md`
- **Browser Automation Strategy**: `browser_automation_strategy.md`
- **Universal Instructions**: `universal_instructions.md`

---

**⚠️ CRITICAL REMINDER: AI agents must execute ALL manual steps directly using available tools. Never delegate manual tasks to users!**
