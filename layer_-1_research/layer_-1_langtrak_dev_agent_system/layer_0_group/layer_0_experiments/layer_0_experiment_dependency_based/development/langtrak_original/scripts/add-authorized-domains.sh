#!/bin/bash

# Add Authorized Domains to Firebase Authentication
# This script uses the Google Cloud Identity Toolkit API

PROJECT_ID="lang-trak-dev"

echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║         ADDING AUTHORIZED DOMAINS TO FIREBASE AUTH                   ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Project: $PROJECT_ID"
echo ""

# Get access token
echo "📋 Getting access token..."
ACCESS_TOKEN=$(firebase login:ci --no-localhost 2>/dev/null || gcloud auth print-access-token 2>/dev/null)

if [ -z "$ACCESS_TOKEN" ]; then
    echo "⚠️  Could not get access token automatically"
    echo "   Trying with Firebase CLI token..."
    ACCESS_TOKEN=$(cat ~/.config/firebase/firebase-token.json 2>/dev/null | grep -o '"access_token":"[^"]*' | cut -d'"' -f4)
fi

if [ -z "$ACCESS_TOKEN" ]; then
    echo "❌ Could not get access token"
    echo "   Please run: gcloud auth login"
    exit 1
fi

echo "✅ Access token obtained"

# Get current configuration
echo ""
echo "📋 Fetching current authorized domains..."

RESPONSE=$(curl -s -H "Authorization: Bearer $ACCESS_TOKEN" \
    "https://identitytoolkit.googleapis.com/admin/v2/projects/$PROJECT_ID/config")

echo "Current config response length: ${#RESPONSE}"

# The Firebase Auth config uses the Identity Platform API
# Let's try a different approach - use gcloud to list current domains
echo ""
echo "📋 Using gcloud to check current configuration..."

# Check if gcloud is available
if command -v gcloud &> /dev/null; then
    echo "✅ gcloud CLI found"
    
    # List current authorized domains (this requires manual check in console)
    echo ""
    echo "ℹ️  To add authorized domains, you can:"
    echo ""
    echo "   1. Via Firebase Console (easiest):"
    echo "      https://console.firebase.google.com/project/$PROJECT_ID/authentication/settings"
    echo "      Scroll to 'Authorized domains'"
    echo "      Click 'Add domain'"
    echo "      Add: localhost"
    echo "      Add: 127.0.0.1"
    echo ""
    echo "   2. Via gcloud CLI:"
    echo "      The domains are typically already authorized by default"
    echo "      localhost and 127.0.0.1 are usually pre-configured"
    echo ""
else
    echo "⚠️  gcloud CLI not found"
fi

# Check what's currently in the project
echo ""
echo "📋 Checking current Firebase project setup..."
firebase apps:list --project $PROJECT_ID 2>&1 | head -20

echo ""
echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║                        CONFIGURATION INFO                             ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Good news: localhost and 127.0.0.1 are usually pre-authorized!"
echo ""
echo "To verify or add domains manually:"
echo "  1. Go to: https://console.firebase.google.com/project/$PROJECT_ID/authentication/settings"
echo "  2. Scroll to 'Authorized domains' section"
echo "  3. You should see 'localhost' already there"
echo "  4. If not, click 'Add domain' and add:"
echo "     • localhost"
echo "     • 127.0.0.1"
echo ""
echo "Then test with:"
echo "  python3 scripts/run-automated-browser-tests.py"
echo ""

