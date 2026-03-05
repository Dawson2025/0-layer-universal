---
resource_id: "20b4ac31-3b15-469f-97a6-8c9721de448a"
resource_type: "document"
resource_name: "ubuntu-linux-setup.sync-conflict-20260126-035814-IF2WOGZ"
---
# Ubuntu Linux Setup Guide

This guide documents the setup process for Ubuntu Linux systems, including essential tools and applications.

## Prerequisites

- Ubuntu 24.04 (Noble) or later
- Administrator (sudo) access
- Internet connection

## Initial System Setup

### 1. Configure Passwordless Sudo (Optional but Recommended for Automation)

For AI-assisted development and automation, passwordless sudo can be configured:

```bash
# Create sudoers configuration file
echo "dawson ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/dawson-nopasswd

# Set correct permissions
sudo chmod 0440 /etc/sudoers.d/dawson-nopasswd

# Validate configuration
sudo visudo -c
```

**Security Note**: This is recommended for personal development machines. For production systems, use more restrictive sudoers rules.

### 2. Install Essential Tools

#### Git
```bash
sudo apt update
sudo apt install git -y
```

#### Curl
```bash
sudo apt install curl -y
```

## System Configuration

### Trackpad Sensitivity (GNOME)

For Ubuntu systems using GNOME desktop environment, you can adjust trackpad cursor speed to make the cursor move faster with less finger movement.

#### Check Current Speed

```bash
gsettings get org.gnome.desktop.peripherals.touchpad speed
```

The value ranges from `-1.0` (slowest) to `1.0` (fastest), with `0.0` as neutral.

#### Adjust Cursor Speed

**Increase sensitivity** (cursor moves faster):
```bash
# Moderate increase
gsettings set org.gnome.desktop.peripherals.touchpad speed 0.5

# Higher sensitivity
gsettings set org.gnome.desktop.peripherals.touchpad speed 0.7

# Maximum sensitivity
gsettings set org.gnome.desktop.peripherals.touchpad speed 1.0
```

**Decrease sensitivity** (cursor moves slower):
```bash
gsettings set org.gnome.desktop.peripherals.touchpad speed 0.3
```

**Note**: This setting controls **cursor movement speed only**, not scrolling speed. Changes persist across reboots.

#### GUI Method

Alternatively, use GNOME Settings:
1. Open **Settings**
2. Navigate to **Mouse & Touchpad**
3. Adjust the **Pointer Speed** slider under the Touchpad section

#### Identify Your Trackpad Device

To see your trackpad information:
```bash
xinput list
```

To view detailed trackpad properties:
```bash
xinput list-props <device-id>
```

Replace `<device-id>` with the ID number from `xinput list` output.

## Application Installations

### Google Chrome

#### Method 1: Direct .deb Installation (Recommended)

1. Download the Chrome .deb package:
   ```bash
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O ~/Downloads/google-chrome-stable_current_amd64.deb
   ```

2. Install the package:
   ```bash
   sudo apt install ~/Downloads/google-chrome-stable_current_amd64.deb -y
   ```

3. Verify installation:
   ```bash
   google-chrome --version
   ```

#### Method 2: Repository Installation

1. Add Google's signing key:
   ```bash
   wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
   ```

2. Add the repository:
   ```bash
   echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
   ```

3. Install Chrome:
   ```bash
   sudo apt update
   sudo apt install google-chrome-stable -y
   ```

### Google Antigravity IDE

Google Antigravity IDE is available as a native Linux application via apt repository for Ubuntu/Debian-based systems.

#### Prerequisites

- Ubuntu 20.04+ (glibc >= 2.28, glibcxx >= 3.4.25)
- Google Chrome installed (for authentication and browser automation features)
- X11 display server configured (for WSL2 users)

#### Installation for Ubuntu/Debian (deb-based distributions)

1. **Create keyring directory** (if it doesn't exist):
   ```bash
   sudo mkdir -p /etc/apt/keyrings
   ```

2. **Add the Antigravity repository signing key**:
   ```bash
   curl -fsSL https://us-central1-apt.pkg.dev/doc/repo-signing-key.gpg | \
     sudo gpg --dearmor -o /etc/apt/keyrings/antigravity-repo-key.gpg
   ```

3. **Add the Antigravity repository to apt sources**:
   ```bash
   echo "deb [signed-by=/etc/apt/keyrings/antigravity-repo-key.gpg] https://us-central1-apt.pkg.dev/projects/antigravity-auto-updater-dev/ antigravity-debian main" | \
     sudo tee /etc/apt/sources.list.d/antigravity.list > /dev/null
   ```

4. **Update package cache**:
   ```bash
   sudo apt update
   ```

5. **Install Antigravity IDE**:
   ```bash
   sudo apt install -y antigravity
   ```

6. **Verify installation**:
   ```bash
   antigravity --version
   ```

#### WSL2-Specific Setup

If you're running in WSL2, Antigravity requires Chrome with remote debugging enabled for proper authentication:

1. **Kill any existing Antigravity and Chrome processes**:
   ```bash
   pkill -f antigravity-server
   pkill chrome
   sleep 2
   ```

2. **Launch Chrome with remote debugging**:
   ```bash
   google-chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check > /dev/null 2>&1 &
   ```

3. **Launch Antigravity**:
   ```bash
   export DONT_PROMPT_WSL_INSTALL=1
   antigravity .
   ```

   The `DONT_PROMPT_WSL_INSTALL=1` environment variable suppresses the warning about using WSL.

#### Launching Antigravity

**Open current directory**:
```bash
antigravity .
```

**Open a specific project folder**:
```bash
antigravity ~/code/my-project
```

**Open with WSL prompt suppressed**:
```bash
export DONT_PROMPT_WSL_INSTALL=1
antigravity ~/code/my-project
```

#### Troubleshooting

**Sign-in button not working in WSL2**:
- Ensure Chrome is running with remote debugging enabled (port 9222)
- Check that `DISPLAY` environment variable is set (should be `:0` for WSL2 with X11)
- Verify Chrome can be accessed at `http://127.0.0.1:9222`

**Authentication issues**:
- Launch Chrome first with `--remote-debugging-port=9222` flag
- Then launch Antigravity
- The IDE needs to connect to Chrome for OAuth authentication flows

**Display/GUI not showing**:
- For WSL2 users, ensure X11 forwarding is configured
- Install an X server on Windows (like VcXsrv or Windows 11 built-in WSLg)
- Verify `echo $DISPLAY` returns a value (typically `:0`)

#### Alternative Installation: RPM-based distributions

For Red Hat, Fedora, SUSE, etc.:

1. **Add the repository**:
   ```bash
   sudo tee /etc/yum.repos.d/antigravity.repo << EOL
   [antigravity-rpm]
   name=Antigravity RPM Repository
   baseurl=https://us-central1-yum.pkg.dev/projects/antigravity-auto-updater-dev/antigravity-rpm
   enabled=1
   gpgcheck=0
   EOL
   ```

2. **Update cache and install**:
   ```bash
   sudo dnf makecache
   sudo dnf install antigravity
   ```

## Project Directory Structure

### Recommended Location for Coding Projects

Store coding projects in `~/code`:

```bash
mkdir -p ~/code
```

This follows Linux conventions and keeps projects organized.

### Repository Setup

#### Clone Context Repositories

```bash
cd ~/code

# Clone universal context repository
git clone git@github.com:Dawson2025/0-universal-context.git

# Clone setup hub repository
git clone git@github.com:Dawson2025/setup-hub.git
```

#### SSH Key Setup for GitHub

1. Generate SSH key (if not already done):
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

2. Display public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

3. Add to GitHub:
   - Go to https://github.com/settings/keys
   - Click "New SSH key"
   - Paste the public key
   - Select "Authentication Key" as the key type

4. Test connection:
   ```bash
   ssh -T git@github.com
   ```

## Troubleshooting

### APT Repository Issues

If you encounter malformed repository errors:

1. Remove the problematic repository file:
   ```bash
   sudo rm /etc/apt/sources.list.d/problematic-repo.list
   ```

2. Update package lists:
   ```bash
   sudo apt update
   ```

### Empty GPG Key Files

If a GPG key file is 0 bytes:

1. Remove the empty key file:
   ```bash
   sudo rm /etc/apt/keyrings/empty-key.gpg
   ```

2. Re-download and add the key:
   ```bash
   curl -fsSL <key-url> | sudo gpg --dearmor -o /etc/apt/keyrings/key-name.gpg
   ```

### Command Not Found Errors

If you get "command not found" errors:

1. Update package lists:
   ```bash
   sudo apt update
   ```

2. Install the missing package:
   ```bash
   sudo apt install <package-name> -y
   ```

## Next Steps

- [ ] Complete Antigravity IDE installation
- [ ] Set up development environment (Node.js, Python, etc.)
- [ ] Configure IDE and editor preferences
- [ ] Set up version control workflows
- [ ] Document additional tools and utilities

## Related Documentation

- [Codex on Windows + VS Code](codex-windows-vscode.md) - Windows/WSL setup guide
- [Codex VS Code Manual Tasks](codex-vscode-manual-tests.md) - Manual verification checklist

---

**Last Updated**: November 25, 2025
**Ubuntu Version**: 24.04 (Noble)
**Antigravity Version**: 1.11.5

