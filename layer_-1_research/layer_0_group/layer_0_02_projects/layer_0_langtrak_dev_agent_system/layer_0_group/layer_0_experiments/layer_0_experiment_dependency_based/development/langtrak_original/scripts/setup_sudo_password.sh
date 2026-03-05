#!/bin/bash
# resource_id: "882443b8-a5c6-488a-8669-508e0a010821"
# resource_type: "script"
# resource_name: "setup_sudo_password"
# Setup script for sudo password management
# This creates a secure password file that won't be committed to git

echo "🔐 Setting up sudo password management for AI agents..."

# Create secure password file
read -s -p "Enter your sudo password: " password
echo
echo "$password" > ~/.ai_sudo_password
chmod 600 ~/.ai_sudo_password

echo "✅ Password stored securely in ~/.ai_sudo_password"

# Test the setup
echo "🧪 Testing sudo access..."
if echo "$password" | sudo -S whoami > /dev/null 2>&1; then
    echo "✅ Sudo access working correctly"
else
    echo "❌ Sudo access failed - please check your password"
    exit 1
fi

# Create environment variable option
echo "📝 Setting up environment variable option..."
echo "export SUDO_PASSWORD=\"$password\"" >> ~/.bashrc
echo "✅ Added SUDO_PASSWORD to ~/.bashrc"

echo ""
echo "🎉 Setup complete! AI agents can now use:"
echo "   Method 1: cat ~/.ai_sudo_password | sudo -S command"
echo "   Method 2: echo \$SUDO_PASSWORD | sudo -S command"
echo ""
echo "⚠️  Security note: ~/.ai_sudo_password is not tracked by git"
