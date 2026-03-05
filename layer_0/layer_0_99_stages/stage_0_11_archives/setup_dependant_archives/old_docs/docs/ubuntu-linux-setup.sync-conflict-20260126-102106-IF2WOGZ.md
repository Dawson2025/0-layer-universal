---
resource_id: "16fe91d9-6510-480e-8c55-69b9e96c126c"
resource_type: "document"
resource_name: "ubuntu-linux-setup.sync-conflict-20260126-102106-IF2WOGZ"
---
# Ubuntu Linux Setup Guide

This guide documents the setup process for Ubuntu Linux systems, including essential tools and applications.

<!-- section_id: "d9bc6e57-69ca-4975-823d-a693fbe1b543" -->
## Prerequisites

- Ubuntu 24.04 (Noble) or later
- Administrator (sudo) access
- Internet connection

<!-- section_id: "1cffa26a-b8db-4b70-891d-772e055be395" -->
## Initial System Setup

<!-- section_id: "fcdb5a01-4c2e-4763-a699-9e61ed516690" -->
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

<!-- section_id: "1739922c-449e-4bdc-afbc-8d0a15cdca52" -->
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

<!-- section_id: "7a99b44c-5d18-446a-99af-62e0e9d26ebe" -->
## System Configuration

<!-- section_id: "84c86a2b-3b63-4ca4-91f2-260500cf08f7" -->
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

<!-- section_id: "329e6543-7fe3-43bd-893c-0c043de5f3c8" -->
## Application Installations

<!-- section_id: "ccbf7cbb-7ec5-4a49-bf50-81d96e54bd7f" -->
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

<!-- section_id: "4b52ad92-2d3f-418d-8424-0f2067670689" -->
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

<!-- section_id: "99ee4bc5-4409-4d44-a254-86f8fe328e53" -->
## Project Directory Structure

<!-- section_id: "9b00c1a4-bb4a-455b-b18f-82971a3e9527" -->
### Recommended Location for Coding Projects

Store coding projects in `~/code`:

```bash
mkdir -p ~/code
```

This follows Linux conventions and keeps projects organized.

<!-- section_id: "73df38df-8577-4aca-b6f9-a8e2760ade76" -->
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

<!-- section_id: "536f4c3d-8ace-47ce-94e6-c1d89db7d9d0" -->
## Troubleshooting

<!-- section_id: "1df0708f-9a10-4b6b-9a56-8d21f40881ec" -->
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

<!-- section_id: "bc318351-6266-4a83-8d0a-6049952d6e22" -->
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

<!-- section_id: "9d989de7-0050-4a25-9714-b04d7a032414" -->
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

<!-- section_id: "2ecb5dfc-57d7-4a0e-9c94-1f7bad368525" -->
## Next Steps

- [ ] Complete Antigravity IDE installation
- [ ] Set up development environment (Node.js, Python, etc.)
- [ ] Configure IDE and editor preferences
- [ ] Set up version control workflows
- [ ] Document additional tools and utilities

<!-- section_id: "55f4eb07-2644-4cb1-81c8-70a9c59a5e42" -->
## Related Documentation

- [Codex on Windows + VS Code](codex-windows-vscode.md) - Windows/WSL setup guide
- [Codex VS Code Manual Tasks](codex-vscode-manual-tests.md) - Manual verification checklist

---

**Last Updated**: November 25, 2025
**Ubuntu Version**: 24.04 (Noble)
**Antigravity Version**: 1.11.5

