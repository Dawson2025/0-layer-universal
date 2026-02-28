#!/bin/bash

# Setup script for OpenAI Codex CLI in Cursor environment
# This script ensures Node.js and Codex CLI are available in the current session

echo "Setting up Codex CLI environment..."

# Load nvm and Node.js
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# Verify installations
echo "Node.js version: $(node --version)"
echo "npm version: $(npm --version)"
echo "Codex CLI version: $(codex --version)"

# Check if OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo ""
    echo "⚠️  OPENAI_API_KEY environment variable is not set!"
    echo "To use Codex CLI, you need to:"
    echo "1. Get your API key from: https://platform.openai.com/settings/organization/api-keys"
    echo "2. Set it as an environment variable:"
    echo "   export OPENAI_API_KEY='your-api-key-here'"
    echo ""
    echo "You can add the export command to your ~/.bashrc file to make it persistent."
else
    echo "✅ OPENAI_API_KEY is set"
fi

echo ""
echo "🚀 Codex CLI is ready to use!"
echo "Try running: codex --help"
