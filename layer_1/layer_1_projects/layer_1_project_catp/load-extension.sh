#!/bin/bash
# Script to launch Chrome with the extension loaded

EXTENSION_PATH="/home/dawson/dawson-workspace/code/catp/task-timer-frontend"
CANVAS_URL="https://byui.instructure.com/courses/123456/assignments/789012"

echo "🚀 Loading Canvas Assignment Timer Extension..."
echo ""
echo "Extension path: $EXTENSION_PATH"
echo "Target URL: $CANVAS_URL"
echo ""

# Convert WSL path to Windows path
WIN_PATH=$(wslpath -w "$EXTENSION_PATH")
echo "Windows path: $WIN_PATH"
echo ""

# Launch Chrome with extension loaded (Windows command from WSL)
echo "Launching Chrome with extension..."
cmd.exe /c start chrome.exe --load-extension="$WIN_PATH" --new-window "$CANVAS_URL"

echo ""
echo "✅ Chrome should open with:"
echo "   1. Extension loaded from: task-timer-frontend/"
echo "   2. Navigated to Canvas assignment page"
echo ""
echo "If you see errors about Chrome being already open:"
echo "   - Close all Chrome windows first"
echo "   - Or load extension manually:"
echo "     1. Open chrome://extensions/"
echo "     2. Enable 'Developer mode'"
echo "     3. Click 'Load unpacked'"
echo "     4. Select: $WIN_PATH"




