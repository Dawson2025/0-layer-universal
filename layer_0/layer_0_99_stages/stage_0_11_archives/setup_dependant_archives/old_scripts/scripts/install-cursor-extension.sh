#!/bin/bash
# Script to help install Cursor browser extension

echo "=========================================="
echo "Installing Cursor Browser Extension"
echo "=========================================="
echo ""

# Try to find Chrome
CHROME_PATH=""
if command -v google-chrome &> /dev/null; then
    CHROME_PATH="google-chrome"
elif command -v chromium-browser &> /dev/null; then
    CHROME_PATH="chromium-browser"
elif command -v chromium &> /dev/null; then
    CHROME_PATH="chromium"
fi

if [ -z "$CHROME_PATH" ]; then
    echo "❌ Chrome/Chromium not found in PATH"
    echo "Please install Chrome or Chromium first"
    exit 1
fi

echo "✓ Found browser: $CHROME_PATH"
echo ""
echo "Opening Chrome extensions page..."
echo "Please follow these steps:"
echo "1. Enable 'Developer mode' (toggle in top right)"
echo "2. Search for 'Cursor' in Chrome Web Store"
echo "3. Install the official Cursor browser extension"
echo "4. Restart Cursor IDE"
echo ""

# Open Chrome to extensions page
$CHROME_PATH "chrome://extensions/" > /dev/null 2>&1 &

echo "Chrome should now be open to the extensions page."
echo "After installing the extension, restart Cursor IDE."

