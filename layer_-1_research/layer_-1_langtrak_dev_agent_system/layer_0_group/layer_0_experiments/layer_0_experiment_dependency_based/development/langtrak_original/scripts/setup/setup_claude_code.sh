#!/bin/bash

# Setup script for Claude Code CLI
# This loads the Node.js environment and makes the claude command available

echo "🚀 Setting up Claude Code CLI environment..."

# Load nvm and Node.js
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# Verify installations
echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"
echo "✅ Claude Code version: $(claude --version)"

echo ""
echo "🎉 Claude Code CLI is ready to use!"
echo ""
echo "📖 Available commands:"
echo "  claude              - Start interactive mode"
echo "  claude 'task'       - Run a one-time task"
echo "  claude -c           - Continue most recent conversation"
echo "  claude -r           - Resume a previous conversation"
echo "  claude commit       - Create a git commit"
echo ""
echo "💡 Type 'claude' to start, or 'claude --help' for more options"
