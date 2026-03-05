---
resource_id: "faaf2c36-ab52-4c6c-a89f-451f4c7eeda3"
resource_type: "document"
resource_name: "INSTALL_CURSOR_EXTENSION.sync-conflict-20260126-035815-IF2WOGZ"
---
# Installing Cursor MCP Chrome Extension

<!-- section_id: "e195fb36-b43d-4c27-80e1-41152753c2d0" -->
## Found Extension

There IS a Cursor MCP extension, but it's **not on the Chrome Web Store** - it's on GitHub and needs to be installed manually.

**Repository**: https://github.com/sirvenis/cursor-mcp-extension

**Note**: This is a **community-developed** extension, not officially from Cursor. However, it may be what the `cursor-browser-extension` MCP server needs.

<!-- section_id: "90f17b2a-491e-4a88-b885-2bb23fbadd52" -->
## Installation Steps

1. **The extension is already cloned** to `/tmp/cursor-mcp-extension`

2. **Open Chrome** and go to `chrome://extensions/`

3. **Enable Developer Mode** (toggle in top right)

4. **Click "Load unpacked"**

5. **Select the folder**: `/tmp/cursor-mcp-extension`

6. **The extension should install**

7. **Restart Cursor IDE**

<!-- section_id: "409d1525-782e-4777-9965-74434d00687b" -->
## Important Notes

- According to Cursor's official docs, browser automation is "native" and doesn't require an extension
- However, the `cursor-browser-extension` MCP server shows "No server info found"
- This GitHub extension may or may not be what's needed
- It's community-developed, not official

<!-- section_id: "01a1e507-d8bd-4a02-902c-04581e04f053" -->
## Alternative

Since Cursor docs say browser automation is native, the issue might be:
- Linux-specific path detection problems
- The cursor-browser-extension MCP server needing different configuration
- Using Playwright MCP tools directly instead

<!-- section_id: "f06e4235-82bb-4044-a031-5a41a10f826b" -->
## Next Steps

After installing the extension:
1. Restart Cursor
2. Test browser tools
3. If it still doesn't work, we may need to use Playwright MCP tools directly

