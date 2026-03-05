---
resource_id: "c46e0cc8-8fe3-444b-821e-8bdb6573a4a8"
resource_type: "document"
resource_name: "ubuntu-antigravity-setup.sync-conflict-20260126-035814-IF2WOGZ"
---
# Ubuntu Antigravity IDE Setup Guide

Complete guide for installing and configuring Google Antigravity IDE on native Ubuntu Linux systems.

## Prerequisites

- Ubuntu 20.04+ (24.04 recommended)
- Administrator access (sudo)
- Internet connection
- Desktop environment (GNOME, KDE, XFCE, etc.) with display server (X11 or Wayland)

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

## Step 1: Install Google Chrome

Chrome is required for Antigravity's authentication system and browser automation features.

### Check if Chrome is already installed

```bash
google-chrome --version
```

If not installed, follow these steps:

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

## Step 2: Install Antigravity IDE

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

## Step 3: Configure Chrome for Authentication (Optional but Recommended)

While Antigravity can work without Chrome remote debugging on native Linux, enabling it provides better authentication integration and browser automation features.

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

### Alternative: Launch Chrome with Explicit User Profile

If the standard remote debugging launch doesn't work, try with an explicit user profile:

```bash
google-chrome --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug \
  --no-first-run \
  --no-default-browser-check > /dev/null 2>&1 &
```

### Alternative: Use Chrome Normally

On native Linux, you can also use Chrome normally without remote debugging. Antigravity will attempt to use the default Chrome instance for authentication. However, remote debugging provides more reliable authentication flows.

## Step 4: Launch Antigravity IDE

### Basic Launch

```bash
antigravity .
```

This opens Antigravity in the current directory.

### Open a Specific Project

```bash
antigravity ~/code/my-project
```

### Launch from Applications Menu

After installation, Antigravity should appear in your applications menu:
- **GNOME**: Search for "Antigravity" in Activities overview
- **KDE**: Search for "Antigravity" in Application Launcher
- **XFCE**: Look in Applications > Development > Antigravity

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

## Step 5: Sign In to Antigravity

1. Once Antigravity opens, click the **Sign In** button
2. A browser window should open for authentication
3. Sign in with your Google account
4. Grant necessary permissions
5. You should be redirected back to Antigravity, now signed in

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

### Usage

```bash
# Open current directory
~/start-antigravity.sh

# Open specific project
~/start-antigravity.sh ~/code/my-project
```

### Add to Shell Profile (Optional)

To make the script available system-wide:

```bash
# Add to PATH
echo 'export PATH="$HOME:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Now you can run `start-antigravity.sh` from anywhere.

## Troubleshooting

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

## System Requirements

- **Ubuntu**: 20.04+ (24.04 recommended)
- **glibc**: >= 2.28
- **glibcxx**: >= 3.4.25
- **Desktop Environment**: GNOME, KDE, XFCE, or compatible
- **Display Server**: X11 or Wayland
- **RAM**: 4GB minimum, 8GB+ recommended
- **Disk Space**: ~1GB for Antigravity installation
- **Google Chrome**: Latest stable version

## Additional Resources

- [Google Antigravity Documentation](https://antigravity.google/docs)
- [Ubuntu Desktop Guide](https://help.ubuntu.com/lts/ubuntu-help/)
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)

## Quick Reference

### Daily Startup
```bash
~/start-antigravity.sh ~/code/my-project
```

Or simply:
```bash
antigravity ~/code/my-project
```

### Stop Everything
```bash
pkill -f antigravity-server
pkill chrome
```

### Check Status
```bash
# Check if Antigravity is running
ps aux | grep antigravity-server | grep -v grep

# Check if Chrome debugging is active
curl -s http://127.0.0.1:9222/json/version
```

### Update Antigravity
```bash
sudo apt update
sudo apt upgrade antigravity
```

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

