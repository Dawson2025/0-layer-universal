---
resource_id: "00e4bcaf-4273-4e64-b88a-a27d3b4354a0"
resource_type: "document"
resource_name: "INSTALL_CURSOR_EXTENSION.sync-conflict-20260126-102106-IF2WOGZ"
---
# Installing Cursor MCP Chrome Extension

## Found Extension

There IS a Cursor MCP extension, but it's **not on the Chrome Web Store** - it's on GitHub and needs to be installed manually.

**Repository**: https://github.com/sirvenis/cursor-mcp-extension

**Note**: This is a **community-developed** extension, not officially from Cursor. However, it may be what the `cursor-browser-extension` MCP server needs.

## Installation Steps

1. **The extension is already cloned** to `/tmp/cursor-mcp-extension`

2. **Open Chrome** and go to `chrome://extensions/`

3. **Enable Developer Mode** (toggle in top right)

4. **Click "Load unpacked"**

5. **Select the folder**: `/tmp/cursor-mcp-extension`

6. **The extension should install**

7. **Restart Cursor IDE**

## Important Notes

- According to Cursor's official docs, browser automation is "native" and doesn't require an extension
- However, the `cursor-browser-extension` MCP server shows "No server info found"
- This GitHub extension may or may not be what's needed
- It's community-developed, not official

## Alternative

Since Cursor docs say browser automation is native, the issue might be:
- Linux-specific path detection problems
- The cursor-browser-extension MCP server needing different configuration
- Using Playwright MCP tools directly instead

## Next Steps

After installing the extension:
1. Restart Cursor
2. Test browser tools
3. If it still doesn't work, we may need to use Playwright MCP tools directly

