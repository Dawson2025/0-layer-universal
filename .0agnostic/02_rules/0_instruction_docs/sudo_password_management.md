---
resource_id: "322333ea-bebb-4f1b-a330-26aecf9d95bc"
resource_type: "rule"
resource_name: "sudo_password_management"
---
# Sudo Password Management - CRITICAL

<!-- section_id: "170ee7eb-c8d7-47a0-b3f9-2c390ee41aec" -->
## 🚨 **MANDATORY: Sudo Password Access for AI Agents**

<!-- section_id: "c7d32927-b7c3-4e6c-9697-e68e541903a9" -->
### **Why This Matters:**
- Enables installation of system packages (sqlite3, etc.)
- Allows system-level configuration changes
- Prevents terminal hanging on sudo prompts
- Essential for proper development environment setup

<!-- section_id: "370b192f-6903-4c95-bfd9-3db82be51ab0" -->
### **🔐 Password Storage Options:**

#### **Option 1: Environment Variable (Recommended)**
```bash
# Set in your shell profile (.bashrc, .zshrc, etc.)
export SUDO_PASSWORD="your_password_here"

# Or create a secure file
echo "your_password_here" > ~/.sudo_password
chmod 600 ~/.sudo_password
```

#### **Option 2: Secure File (Most Secure)**
```bash
# Create secure password file
echo "your_password_here" > ~/.ai_sudo_password
chmod 600 ~/.ai_sudo_password

# AI agents can read it when needed
cat ~/.ai_sudo_password | sudo -S command
```

#### **Option 3: Direct Input (Interactive)**
```bash
# AI agents can prompt for password when needed
echo "your_password_here" | sudo -S command
```

<!-- section_id: "5ed01d3c-3744-42b0-bc84-8aefc393616a" -->
### **🔧 Implementation for AI Agents:**

#### **Method 1: Environment Variable**
```bash
# Check if password is available
if [ -n "$SUDO_PASSWORD" ]; then
    echo "$SUDO_PASSWORD" | sudo -S command
else
    echo "❌ SUDO_PASSWORD not set"
fi
```

#### **Method 2: Secure File**
```bash
# Read password from secure file
if [ -f ~/.sudo_password ]; then
    cat ~/.sudo_password | sudo -S command
else
    echo "❌ Password file not found"
fi
```

#### **Method 3: Direct Input**
```bash
# Prompt for password (less secure)
echo "Please enter sudo password:" && read -s password && echo "$password" | sudo -S command
```

<!-- section_id: "d1e0046c-20ee-4601-aefa-05e978c4f7ab" -->
### **📋 Quick Setup Commands:**

#### **Automated Setup (Recommended):**
```bash
# Run the setup script (most secure)
./scripts/setup_sudo_password.sh
```

#### **Manual Setup:**
```bash
# Option 1: Set environment variable
echo 'export SUDO_PASSWORD="your_password_here"' >> ~/.bashrc
source ~/.bashrc

# Option 2: Create secure file
echo "your_password_here" > ~/.ai_sudo_password
chmod 600 ~/.ai_sudo_password

# Test access
echo "$SUDO_PASSWORD" | sudo -S whoami
# OR
cat ~/.ai_sudo_password | sudo -S whoami
```

#### **Using AI Helper Script:**
```bash
# Install packages
./scripts/ai_sudo_helper.sh install sqlite3

# Check if package is installed
./scripts/ai_sudo_helper.sh check sqlite3

# Run custom sudo commands
./scripts/ai_sudo_helper.sh run "systemctl restart nginx"
```

<!-- section_id: "4c9e435d-924f-4e8f-86e1-2e18c82bdf6b" -->
### **🎯 Benefits:**
- ✅ No terminal hanging on sudo prompts
- ✅ Automated system package installation
- ✅ Seamless development environment setup
- ✅ Consistent behavior across AI agents

<!-- section_id: "2175b0da-c0da-400d-9109-c8b041faa9c5" -->
### **⚠️ Security Notes:**
- Store password securely (600 permissions)
- Use environment variables in development only
- Consider using `sudo` with NOPASSWD for specific commands
- Never commit passwords to version control

**This protocol must be followed by ALL AI agents working on this project.**
