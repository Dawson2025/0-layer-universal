#!/bin/bash
# resource_id: "be774b52-7ffb-40d2-9f61-3494c9f40974"
# resource_type: "script"
# resource_name: "cloud_server_setup_gemini"
# Gemini CLI Setup for Cloud Server
# Run this on your cloud server to set up Gemini CLI

echo "=== Setting up Gemini CLI ==="

# Set the API key
export GOOGLE_API_KEY="AIzaSyCoGDYmISEIK4PI-mQno4EhShL0Jp6RY2I"

# Add to bashrc for persistence
if ! grep -q "GOOGLE_API_KEY" ~/.bashrc; then
    echo 'export GOOGLE_API_KEY="AIzaSyCoGDYmISEIK4PI-mQno4EhShL0Jp6RY2I"' >> ~/.bashrc
    echo "Added GOOGLE_API_KEY to ~/.bashrc"
else
    echo "GOOGLE_API_KEY already in ~/.bashrc"
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "npm not found. Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# Install Gemini CLI
echo "Installing Gemini CLI..."
npm install -g @google/gemini-cli

# Verify installation
echo ""
echo "=== Verifying Installation ==="
gemini --version

# Test it
echo ""
echo "=== Testing Gemini CLI ==="
gemini "Say hello in 5 words"

echo ""
echo "=== Setup Complete ==="
echo "You can now use: gemini \"your prompt here\""
