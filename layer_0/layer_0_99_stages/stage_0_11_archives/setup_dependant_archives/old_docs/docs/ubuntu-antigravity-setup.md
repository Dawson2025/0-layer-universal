---
resource_id: "b40dfdd9-eead-4d67-88e5-3cbd957d7bee"
resource_type: "document"
resource_name: "ubuntu-antigravity-setup"
---
# Ubuntu Antigravity IDE Setup Guide

Complete guide for installing and configuring Google Antigravity IDE on native Ubuntu Linux systems.

<!-- section_id: "7cb7bf2a-f275-4542-902f-fefcc22ddc65" -->
## Prerequisites

- Ubuntu 20.04+ (24.04 recommended)
- Administrator access (sudo)
- Internet connection
- Desktop environment (GNOME, KDE, XFCE, etc.) with display server (X11 or Wayland)

<!-- section_id: "bc6511fd-fa5f-4f28-85e3-1ce1b84059d5" -->
## Environment Verification

Before starting, verify your Ubuntu environment:

```bash
# Check Ubuntu version
cat /etc/os-release | grep -E "^(NAME|VERSION)="
# Should show Ubuntu 20.04 or later

# Check display server
echo $XDG_SESSION_TYPE
# Should show: x11 or wayland

# Check if display is available
echo $DISPLAY
# Should show: :0 or :1 (for X11) or wayland-0 (for Wayland)

# Verify glibc version (required >= 2.28)
ldd --version | head -n 1
```

<!-- section_id: "1bb70088-5e9f-4f79-abb8-dd42b2cd1fa7" -->
## Step 1: Install Google Chrome

Chrome is required for Antigravity's authentication system and browser automation features.

<!-- section_id: "99df53eb-e797-49cb-9ec5-6b58c3ef2dfc" -->
### Check if Chrome is already installed

```bash
google-chrome --version
```

If not installed, follow these steps:

<!-- section_id: "99435ddc-cfbd-4e53-8b5b-6eb772681587" -->
### Install Chrome via apt repository

1. **Add Google's signing key**:
   ```bash
   wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
   ```

2. **Add Chrome repository**:
   ```bash
   echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
   ```

3. **Install Chrome**:
   ```bash
   sudo apt update
   sudo apt install google-chrome-stable -y
   ```

4. **Verify installation**:
   ```bash
   google-chrome --version
   ```

<!-- section_id: "319e41b2-a84f-4bdc-a7cc-9b7cf17c6b21" -->
### Alternative: Direct .deb Installation

If repository installation fails:

```bash
# Download the Chrome .deb package
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O ~/Downloads/google-chrome-stable_current_amd64.deb

# Install the package
sudo apt install ~/Downloads/google-chrome-stable_current_amd64.deb -y

# Verify installation
google-chrome --version
```

<!-- section_id: "3c8d0118-1422-47fa-848e-69a7bcb0101a" -->
## Step 2: Install Antigravity IDE

<!-- section_id: "7ffd6d15-142e-4caa-af4a-3d8a98315bdb" -->
### Add Antigravity Repository

1. **Create keyring directory**:
   ```bash
   sudo mkdir -p /etc/apt/keyrings
   ```

2. **Download and add repository signing key**:
   ```bash
   curl -fsSL https://us-central1-apt.pkg.dev/doc/repo-signing-key.gpg | \
     sudo gpg --dearmor -o /etc/apt/keyrings/antigravity-repo-key.gpg
   ```

3. **Add Antigravity repository** (IMPORTANT: Keep this as ONE line):
   ```bash
   echo "deb [signed-by=/etc/apt/keyrings/antigravity-repo-key.gpg] https://us-central1-apt.pkg.dev/projects/antigravity-auto-updater-dev/ antigravity-debian main" | sudo tee /etc/apt/sources.list.d/antigravity.list > /dev/null
   ```

4. **Update package cache**:
   ```bash
   sudo apt update
   ```

   You should see output like:
   ```
   Get:X https://us-central1-apt.pkg.dev/projects/antigravity-auto-updater-dev antigravity-debian InRelease
   ```

5. **Install Antigravity**:
   ```bash
   sudo apt install -y antigravity
   ```

   This will download approximately 154 MB and install 739 MB of files.

6. **Verify installation**:
   ```bash
   antigravity --version
   ```

<!-- section_id: "e71ba85c-97e1-4c36-8e37-b7102a895dfe" -->
### Troubleshooting Repository Issues

If you get a "Malformed entry" error:

1. **Remove the malformed repository file**:
   ```bash
   sudo rm /etc/apt/sources.list.d/antigravity.list
   ```

2. **Create a correctly formatted file**:
   ```bash
   cat > /tmp/antigravity.list << 'EOF'
   deb [signed-by=/etc/apt/keyrings/antigravity-repo-key.gpg] https://us-central1-apt.pkg.dev/projects/antigravity-auto-updater-dev/ antigravity-debian main
   EOF
   ```

3. **Copy to correct location**:
   ```bash
   sudo cp /tmp/antigravity.list /etc/apt/sources.list.d/antigravity.list
   ```

4. **Update and install**:
   ```bash
   sudo apt update
   sudo apt install -y antigravity
   ```

<!-- section_id: "42dd03ff-e0f1-4215-80ba-31f52e6b9106" -->
## Step 3: Configure Chrome for Authentication (Optional but Recommended)

While Antigravity can work without Chrome remote debugging on native Linux, enabling it provides better authentication integration and browser automation features.

<!-- section_id: "cacbe255-1cf1-4ec6-bfb8-10fb7a50bd69" -->
### Launch Chrome with Remote Debugging

1. **Kill any existing Chrome and Antigravity processes**:
   ```bash
   pkill -f antigravity-server
   pkill chrome
   sleep 2
   ```

2. **Start Chrome with remote debugging enabled**:
   ```bash
   google-chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check > /dev/null 2>&1 &
   ```

3. **Verify Chrome debugging port is accessible** (optional):
   ```bash
   curl -s http://127.0.0.1:9222/json/version
   ```

   **Note**: The debugging port may not be immediately accessible via HTTP, but this does not prevent Antigravity from working. Chrome uses the port internally for authentication flows. If the curl command fails, Antigravity should still launch and function correctly.

<!-- section_id: "0ddd8a61-3f60-456c-a999-63717f27510b" -->
### Alternative: Launch Chrome with Explicit User Profile

If the standard remote debugging launch doesn't work, try with an explicit user profile:

```bash
google-chrome --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug \
  --no-first-run \
  --no-default-browser-check > /dev/null 2>&1 &
```

<!-- section_id: "dc83b052-3aa2-4135-a170-17501836868f" -->
### Alternative: Use Chrome Normally

On native Linux, you can also use Chrome normally without remote debugging. Antigravity will attempt to use the default Chrome instance for authentication. However, remote debugging provides more reliable authentication flows.

<!-- section_id: "c01ed54c-e35b-4653-bb3b-00c57161d46b" -->
## Step 4: Launch Antigravity IDE

<!-- section_id: "c4db2b0c-3dd8-4fa5-9b4d-74cb8ae33b68" -->
### Basic Launch

```bash
antigravity .
```

This opens Antigravity in the current directory.

<!-- section_id: "82a4d691-c7d3-41da-b013-9bf09e0abaef" -->
### Open a Specific Project

```bash
antigravity ~/code/my-project
```

<!-- section_id: "51b52cd9-7984-4b63-b75c-d53f24937793" -->
### Launch from Applications Menu

After installation, Antigravity should appear in your applications menu:
- **GNOME**: Search for "Antigravity" in Activities overview
- **KDE**: Search for "Antigravity" in Application Launcher
- **XFCE**: Look in Applications > Development > Antigravity

<!-- section_id: "0da0249b-804e-4c1e-918f-c5ec083225e4" -->
### Create Desktop Shortcut (Optional)

Create desktop launchers for quick access. Two options are available:

#### Option 1: Basic Desktop Shortcut

Creates a simple launcher that opens Antigravity directly:

```bash
mkdir -p ~/.local/share/applications ~/Desktop
cat > ~/.local/share/applications/antigravity.desktop << 'EOF'
[Desktop Entry]
Name=Google Antigravity
Comment=Google Antigravity IDE
Exec=antigravity %F
Icon=antigravity
Type=Application
Categories=Development;IDE;
MimeType=inode/directory;
Terminal=false
StartupNotify=true
EOF

chmod +x ~/.local/share/applications/antigravity.desktop

# Copy to Desktop for easy access
cp ~/.local/share/applications/antigravity.desktop ~/Desktop/antigravity.desktop
chmod +x ~/Desktop/antigravity.desktop
```

#### Option 2: Desktop Shortcut with Chrome (Recommended)

Creates a launcher that uses the startup script with Chrome remote debugging:

```bash
mkdir -p ~/.local/share/applications ~/Desktop
cat > ~/.local/share/applications/antigravity-with-chrome.desktop << 'EOF'
[Desktop Entry]
Name=Google Antigravity (with Chrome)
Comment=Google Antigravity IDE with Chrome remote debugging
Exec=/home/dawson/start-antigravity.sh %F
Icon=antigravity
Type=Application
Categories=Development;IDE;
MimeType=inode/directory;
Terminal=false
StartupNotify=true
EOF

chmod +x ~/.local/share/applications/antigravity-with-chrome.desktop

# Copy to Desktop for easy access
cp ~/.local/share/applications/antigravity-with-chrome.desktop ~/Desktop/antigravity-with-chrome.desktop
chmod +x ~/Desktop/antigravity-with-chrome.desktop
```

**Note**: Replace `/home/dawson` with your actual home directory path if different.

#### Update Desktop Database (Optional)

After creating shortcuts, you may want to update the desktop database:

```bash
update-desktop-database ~/.local/share/applications
```

You can now launch Antigravity from:
- Your Desktop (double-click the shortcut)
- Your applications menu (search for "Antigravity")
- By dragging folders onto the shortcut to open that directory

<!-- section_id: "c2314733-57ad-43af-9ebe-dcca6bae9efd" -->
## Step 5: Sign In to Antigravity

1. Once Antigravity opens, click the **Sign In** button
2. A browser window should open for authentication
3. Sign in with your Google account
4. Grant necessary permissions
5. You should be redirected back to Antigravity, now signed in

<!-- section_id: "13c8ca74-0a91-46eb-acff-3e8d3ac15c1c" -->
### If Sign-In Button Doesn't Work

This usually means Chrome isn't properly configured for authentication:

1. **Verify Chrome is running**:
   ```bash
   ps aux | grep chrome | grep -v grep
   ```

2. **If Chrome isn't running, start it with remote debugging**:
   ```bash
   google-chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check > /dev/null 2>&1 &
   sleep 3
   ```

3. **Check if port 9222 is listening**:
   ```bash
   ss -tlnp | grep 9222
   ```

4. **Restart Antigravity**:
   ```bash
   pkill -f antigravity-server
   sleep 2
   antigravity .
   ```

<!-- section_id: "b0e8abf7-2f08-4c76-8f68-2925abdd4ac5" -->
## Complete Startup Script

Create a script to automate the startup process with Chrome remote debugging:

```bash
cat > ~/start-antigravity.sh << 'EOF'
#!/bin/bash

echo "Starting Antigravity IDE..."

# Kill existing processes
pkill -f antigravity-server 2>/dev/null
pkill chrome 2>/dev/null
sleep 2

# Start Chrome with remote debugging (optional but recommended)
echo "Launching Chrome with remote debugging..."
google-chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check > /dev/null 2>&1 &
sleep 3

# Start Antigravity
echo "Launching Antigravity IDE..."
antigravity "${1:-.}"
EOF

chmod +x ~/start-antigravity.sh
```

<!-- section_id: "41168cd5-5de5-4c95-ae37-310fd94782de" -->
### Usage

```bash
# Open current directory
~/start-antigravity.sh

# Open specific project
~/start-antigravity.sh ~/code/my-project
```

<!-- section_id: "fbaab8fc-b090-44bb-bcc5-92dcf96d6d10" -->
### Add to Shell Profile (Optional)

To make the script available system-wide:

```bash
# Add to PATH
echo 'export PATH="$HOME:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Now you can run `start-antigravity.sh` from anywhere.

<!-- section_id: "fb43f610-fd0c-494d-9621-fac14b6be338" -->
## Troubleshooting

<!-- section_id: "f4ad702c-a723-4eae-aa54-5099bd93064c" -->
### Display Issues

**Problem**: GUI doesn't appear or "cannot open display" error

**Solution**:
1. Verify you're logged into a desktop session (not SSH without X11 forwarding)
2. Check display server:
   ```bash
   echo $XDG_SESSION_TYPE
   echo $DISPLAY
   ```
3. For X11, ensure DISPLAY is set:
   ```bash
   export DISPLAY=:0
   echo 'export DISPLAY=:0' >> ~/.bashrc
   ```
4. For Wayland, ensure Wayland session is active (should work automatically)

<!-- section_id: "e3c56dd1-dac9-4b59-bd83-5f70349d0e94" -->
### Authentication Failures

**Problem**: Sign-in button does nothing or authentication fails

**Solution**:
1. Ensure Chrome is installed and accessible:
   ```bash
   google-chrome --version
   which google-chrome
   ```
2. Start Chrome with remote debugging enabled:
   ```bash
   google-chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check > /dev/null 2>&1 &
   ```
   Or with explicit user profile:
   ```bash
   google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug --no-first-run --no-default-browser-check > /dev/null 2>&1 &
   ```
3. Verify Chrome process is running:
   ```bash
   ps aux | grep "chrome.*remote-debugging-port=9222" | grep -v grep
   ```
   **Note**: The debugging port may not be accessible via HTTP (`curl` may fail), but this is normal and doesn't prevent Antigravity from working.
4. Restart Antigravity using the startup script

<!-- section_id: "569e0e72-cf17-462e-801e-551ff95c15ca" -->
### Repository Errors

**Problem**: "Malformed entry" or "cannot read list" errors

**Solution**:
- The repository line must be all on ONE line without newlines
- Use the troubleshooting steps in Step 2 to fix the repository file
- Ensure the GPG key was added correctly:
  ```bash
  ls -la /etc/apt/keyrings/antigravity-repo-key.gpg
  ```

**Problem**: Repository key name mismatch (e.g., `antigravity-repo-keys.gpg` vs `antigravity-repo-key.gpg`)

**Solution**:
- Check the key name in the repository file:
  ```bash
  cat /etc/apt/sources.list.d/antigravity.list
  ```
- Update the repository file to match the actual key name:
  ```bash
  sudo sed -i 's/antigravity-repo-keys\.gpg/antigravity-repo-key.gpg/g' /etc/apt/sources.list.d/antigravity.list
  ```
- Or create the key with the name the repository expects

<!-- section_id: "fecfc1ba-1b8c-4976-973e-6f4a66f850d1" -->
### Performance Issues

**Problem**: Antigravity is slow or unresponsive

**Solution**:
1. Check system resources:
   ```bash
   free -h
   df -h
   ```
2. Close unnecessary browser tabs in Chrome
3. Ensure sufficient RAM (4GB minimum, 8GB+ recommended)
4. Check if other heavy applications are running
5. Restart Antigravity and Chrome

<!-- section_id: "440e6f91-6117-4b96-ac9e-ee62e8b618b9" -->
### Missing Dependencies

**Problem**: Antigravity fails to launch with library errors

**Solution**:
1. Install missing dependencies:
   ```bash
   sudo apt update
   sudo apt install -f
   ```
2. Check for missing libraries:
   ```bash
   ldd $(which antigravity) | grep "not found"
   ```
3. Install specific missing libraries if identified

<!-- section_id: "4440cba7-af65-436d-a418-52080906024a" -->
## System Requirements

- **Ubuntu**: 20.04+ (24.04 recommended)
- **glibc**: >= 2.28
- **glibcxx**: >= 3.4.25
- **Desktop Environment**: GNOME, KDE, XFCE, or compatible
- **Display Server**: X11 or Wayland
- **RAM**: 4GB minimum, 8GB+ recommended
- **Disk Space**: ~1GB for Antigravity installation
- **Google Chrome**: Latest stable version

<!-- section_id: "6a89285c-a798-45ee-9f37-a2db796d9e83" -->
## Additional Resources

- [Google Antigravity Documentation](https://antigravity.google/docs)
- [Ubuntu Desktop Guide](https://help.ubuntu.com/lts/ubuntu-help/)
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)

<!-- section_id: "dfa7294d-4bb8-4c07-a724-f030534cc51a" -->
## Quick Reference

<!-- section_id: "08901c78-21fd-47bc-a1d5-ea84a5670568" -->
### Daily Startup
```bash
~/start-antigravity.sh ~/code/my-project
```

Or simply:
```bash
antigravity ~/code/my-project
```

<!-- section_id: "b233e632-68a3-423b-bde2-86b15df4b10d" -->
### Stop Everything
```bash
pkill -f antigravity-server
pkill chrome
```

<!-- section_id: "2faf9cc6-9861-4285-a9fa-baa9affd040f" -->
### Check Status
```bash
# Check if Antigravity is running
ps aux | grep antigravity-server | grep -v grep

# Check if Chrome debugging is active
curl -s http://127.0.0.1:9222/json/version
```

<!-- section_id: "2c6e81e9-de2a-4ecc-9d03-215c7de38a7c" -->
### Update Antigravity
```bash
sudo apt update
sudo apt upgrade antigravity
```

<!-- section_id: "8bcc2dc4-c929-4eb0-81cc-57660cbb4fcf" -->
### Uninstall Antigravity
```bash
sudo apt remove antigravity
sudo apt autoremove
```

---

**Last Updated**: November 25, 2025  
**Environment**: Native Ubuntu 24.04  
**Antigravity Version**: 1.11.5  
**Tested On**: Ubuntu 24.04 (Noble) with GNOME

