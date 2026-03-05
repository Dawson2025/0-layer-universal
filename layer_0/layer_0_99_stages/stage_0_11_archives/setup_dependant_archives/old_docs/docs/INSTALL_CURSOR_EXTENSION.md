---
resource_id: "cd1712db-0110-4e4a-a689-3bb4231ca6a3"
resource_type: "document"
resource_name: "INSTALL_CURSOR_EXTENSION"
---
# Installing Cursor MCP Chrome Extension

<!-- section_id: "b1314ceb-9c00-469d-bfe1-7a9ba290dc6a" -->
## Found Extension

There IS a Cursor MCP extension, but it's **not on the Chrome Web Store** - it's on GitHub and needs to be installed manually.

**Repository**: https://github.com/sirvenis/cursor-mcp-extension

**Note**: This is a **community-developed** extension, not officially from Cursor. However, it may be what the `cursor-browser-extension` MCP server needs.

<!-- section_id: "8d0ac4c0-b8f0-4909-998c-adc056356b39" -->
## Installation Steps

1. **The extension is already cloned** to `/tmp/cursor-mcp-extension`

2. **Open Chrome** and go to `chrome://extensions/`

3. **Enable Developer Mode** (toggle in top right)

4. **Click "Load unpacked"**

5. **Select the folder**: `/tmp/cursor-mcp-extension`

6. **The extension should install**

7. **Restart Cursor IDE**

<!-- section_id: "3f5b7381-8a4b-422c-bc12-371803876a31" -->
## Important Notes

- According to Cursor's official docs, browser automation is "native" and doesn't require an extension
- However, the `cursor-browser-extension` MCP server shows "No server info found"
- This GitHub extension may or may not be what's needed
- It's community-developed, not official

<!-- section_id: "0ad3c3c4-d98e-4a4b-bcaf-34cd8a116e44" -->
## Alternative

Since Cursor docs say browser automation is native, the issue might be:
- Linux-specific path detection problems
- The cursor-browser-extension MCP server needing different configuration
- Using Playwright MCP tools directly instead

<!-- section_id: "a3d567f3-2371-4890-906a-29e86481a2df" -->
## Next Steps

After installing the extension:
1. Restart Cursor
2. Test browser tools
3. If it still doesn't work, we may need to use Playwright MCP tools directly

