#!/bin/bash

# Script to set up OpenAI API key for Codex CLI

echo "Setting up OpenAI API key..."
echo "Please enter your OpenAI API key (it should start with 'sk-'):"
read -s API_KEY

if [[ $API_KEY == sk-* ]]; then
    # Set for current session
    export OPENAI_API_KEY="$API_KEY"
    
    # Add to .bashrc for persistence
    if ! grep -q "OPENAI_API_KEY" ~/.bashrc; then
        echo "" >> ~/.bashrc
        echo "# OpenAI API Key for Codex CLI" >> ~/.bashrc
        echo "export OPENAI_API_KEY='$API_KEY'" >> ~/.bashrc
        echo "✅ API key added to ~/.bashrc for future sessions"
    else
        echo "⚠️  API key already exists in ~/.bashrc - you may want to update it manually"
    fi
    
    echo "✅ API key set successfully!"
    echo "Loading Codex environment..."
    
    # Load the Codex environment
    source .codex_alias
    
    echo "🚀 Ready to use Codex CLI!"
    echo "Try: codex --help"
    
else
    echo "❌ Invalid API key format. OpenAI API keys should start with 'sk-'"
    exit 1
fi
