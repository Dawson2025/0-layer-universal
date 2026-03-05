#!/bin/bash
# resource_id: "eb2e5547-c668-4644-96b5-448f9b5f02d3"
# resource_type: "script"
# resource_name: "install-cursor-browser-extension.sync-conflict-20260126-035820-IF2WOGZ"
# Script to help install Cursor browser extension

echo "=========================================="
echo "Cursor Browser Extension Installation"
echo "=========================================="
echo ""
echo "The cursor-browser-extension MCP server requires the Cursor browser extension"
echo "to be installed in Chrome/Chromium."
echo ""
echo "To install:"
echo "1. Open Google Chrome or Chromium"
echo "2. Go to: chrome://extensions/"
echo "3. Enable 'Developer mode' (toggle in top right)"
echo "4. Search for 'Cursor' in the Chrome Web Store"
echo "5. Install the official Cursor browser extension"
echo "6. Restart Cursor IDE"
echo ""
echo "Alternatively, you can use the Playwright MCP server or the"
echo "@agent-infra/mcp-server-browser which are already configured."
echo ""
echo "Current MCP configuration:"
cat ~/.cursor/mcp.json | python3 -m json.tool 2>/dev/null || cat ~/.cursor/mcp.json


