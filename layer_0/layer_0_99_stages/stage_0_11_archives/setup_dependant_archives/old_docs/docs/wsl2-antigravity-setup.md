---
resource_id: "21c73dce-cdbb-45f3-a694-244d928bef48"
resource_type: "document"
resource_name: "wsl2-antigravity-setup"
---
# WSL2 Antigravity IDE Setup Guide

Complete guide for installing and configuring Google Antigravity IDE on Windows Subsystem for Linux 2 (WSL2).

<!-- section_id: "1549dc74-7baf-4219-9b23-ccb21beb41f1" -->
## Prerequisites

- Windows 10/11 with WSL2 enabled
- Ubuntu 24.04 running in WSL2
- Administrator access (sudo)
- Internet connection

<!-- section_id: "2ebc7226-1be8-409f-a7c8-d19ced7cf6fc" -->
## Environment Verification

Before starting, verify your WSL2 environment:

```bash
# Check WSL kernel version
uname -r
# Should show something like: 6.6.87.2-microsoft-standard-WSL2

# Check Ubuntu version
cat /etc/os-release | grep -E "^(NAME|VERSION)="
# Should show Ubuntu 24.04

# Check DISPLAY environment variable (for X11)
echo $DISPLAY
# Should show: :0
```

<!-- section_id: "0f0710e8-ad31-4f3f-a833-07e2ca7f9b86" -->
## Step 1: Install Google Chrome

Chrome is required for Antigravity's authentication system and browser automation features.

<!-- section_id: "1b8c2ada-6a3e-4050-8c16-bd4342e9ff32" -->
### Check if Chrome is already installed

```bash
google-chrome --version
```

If not installed, follow these steps:

<!-- section_id: "3c6c9000-089c-45a5-9d2c-9036db8c1cbf" -->
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

<!-- section_id: "cb8ec94e-35ad-411f-968b-4e44a56eef3d" -->
## Step 2: Install Antigravity IDE

<!-- section_id: "1726eb0e-9811-43a7-b7dc-501ea8795cdf" -->
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

<!-- section_id: "68254e38-0ae8-431f-8861-27ee347f0ae1" -->
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

<!-- section_id: "44e48167-eaa9-4682-943d-369f0139dd90" -->
## Step 3: Configure Chrome for WSL2 Authentication

Antigravity requires Chrome to be running with remote debugging enabled for proper authentication in WSL2.

<!-- section_id: "1a7eb252-372e-4d15-8676-670b0933ac7d" -->
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

<!-- section_id: "2c195e86-9d09-461c-8b7f-683cde69d5fa" -->
## Step 4: Launch Antigravity IDE

<!-- section_id: "f8f5f25b-2692-4c4b-bb23-7c3bb09172cb" -->
### Basic Launch

```bash
export DONT_PROMPT_WSL_INSTALL=1
antigravity .
```

The `DONT_PROMPT_WSL_INSTALL=1` environment variable suppresses the WSL warning message.

<!-- section_id: "87c1a72b-3691-4217-be4d-7f9edbfcafc8" -->
### Open a Specific Project

```bash
export DONT_PROMPT_WSL_INSTALL=1
antigravity ~/code/my-project
```

<!-- section_id: "f3ac264e-0777-4d75-a873-bc4a6e11536d" -->
### Add to Shell Profile (Optional)

To avoid typing the export command every time:

```bash
echo 'export DONT_PROMPT_WSL_INSTALL=1' >> ~/.bashrc
source ~/.bashrc
```

Now you can simply run:
```bash
antigravity .
```

<!-- section_id: "e87a4300-4629-4e76-9adc-d217b057f2ec" -->
## Step 5: Sign In to Antigravity

1. Once Antigravity opens, click the **Sign In** button
2. A browser window should open for authentication
3. Sign in with your Google account
4. Grant necessary permissions
5. You should be redirected back to Antigravity, now signed in

<!-- section_id: "661ecd31-76ec-4a53-b2a5-81a38c8fb53a" -->
### If Sign-In Button Doesn't Work

This usually means Chrome remote debugging isn't connected:

1. **Verify Chrome is running with debugging**:
   ```bash
   ps aux | grep chrome | grep "remote-debugging-port=9222"
   ```

2. **Check if port 9222 is listening**:
   ```bash
   ss -tlnp | grep 9222
   ```

3. **Restart both Chrome and Antigravity**:
   ```bash
   pkill -f antigravity-server
   pkill chrome
   sleep 2
   google-chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check > /dev/null 2>&1 &
   sleep 3
   export DONT_PROMPT_WSL_INSTALL=1
   antigravity .
   ```

<!-- section_id: "3e1acd95-d76d-4720-86f3-bc5aa88816d4" -->
## Complete Startup Script

Create a script to automate the startup process:

```bash
cat > ~/start-antigravity.sh << 'EOF'
#!/bin/bash

echo "Starting Antigravity IDE for WSL2..."

# Kill existing processes
pkill -f antigravity-server 2>/dev/null
pkill chrome 2>/dev/null
sleep 2

# Start Chrome with remote debugging
echo "Launching Chrome with remote debugging..."
google-chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check > /dev/null 2>&1 &
sleep 3

# Start Antigravity
echo "Launching Antigravity IDE..."
export DONT_PROMPT_WSL_INSTALL=1
antigravity "${1:-.}"
EOF

chmod +x ~/start-antigravity.sh
```

<!-- section_id: "c44eec0c-94b2-4a21-9df0-b3d0ac2078c8" -->
### Usage

```bash
# Open current directory
~/start-antigravity.sh

# Open specific project
~/start-antigravity.sh ~/code/my-project
```

<!-- section_id: "09198b05-ab3c-48df-9258-441fb2770632" -->
## Troubleshooting

<!-- section_id: "194d135b-ea89-40c0-899e-85ba8f04490c" -->
### Display Issues

**Problem**: GUI doesn't appear or "cannot open display" error

**Solution**:
1. Verify X11 server is running on Windows (VcXsrv, X410, or Windows 11 WSLg)
2. Check DISPLAY variable:
   ```bash
   echo $DISPLAY
   ```
3. If empty, set it:
   ```bash
   export DISPLAY=:0
   echo 'export DISPLAY=:0' >> ~/.bashrc
   ```

<!-- section_id: "fad2ab40-d2b8-435c-a88b-3089f1d4f77f" -->
### Authentication Failures

**Problem**: Sign-in button does nothing or authentication fails

**Solution**:
1. Ensure Chrome is running with `--remote-debugging-port=9222`
2. Check Chrome DevTools is accessible at `http://127.0.0.1:9222`
3. Restart both Chrome and Antigravity using the startup script above

<!-- section_id: "84fbaf2c-cd97-43dc-b892-abad786c1f31" -->
### Repository Errors

**Problem**: "Malformed entry" or "cannot read list" errors

**Solution**:
- The repository line must be all on ONE line without newlines
- Use the troubleshooting steps in Step 2 to fix the repository file

<!-- section_id: "22b71d02-44fd-44e0-8ea8-bc34e3c66114" -->
### Performance Issues

**Problem**: Antigravity is slow or unresponsive

**Solution**:
1. Check WSL2 memory allocation in `.wslconfig` (Windows side)
2. Close unnecessary browser tabs in Chrome
3. Ensure your project is in WSL2 filesystem (`/home/...`), not Windows (`/mnt/c/...`)

<!-- section_id: "e284f3ce-1cb8-4389-bf4f-f6d298043781" -->
## System Requirements

- **WSL2**: Kernel 5.10+
- **Ubuntu**: 20.04+ (24.04 recommended)
- **glibc**: >= 2.28
- **glibcxx**: >= 3.4.25
- **RAM**: 4GB minimum, 8GB+ recommended
- **Disk Space**: ~1GB for Antigravity installation

<!-- section_id: "a7799a69-e00d-458d-9acf-442e16b48b07" -->
## Additional Resources

- [Google Antigravity Documentation](https://antigravity.google/docs)
- [WSL2 Official Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)

<!-- section_id: "624dfacb-0674-4c16-8bcb-d8d513e1cee7" -->
## Quick Reference

<!-- section_id: "5fbd3379-eca0-42a9-98ec-1bc8163067d1" -->
### Daily Startup
```bash
~/start-antigravity.sh ~/code/my-project
```

<!-- section_id: "931b9a0b-cd59-49b9-ae9d-80172136fa40" -->
### Stop Everything
```bash
pkill -f antigravity-server
pkill chrome
```

<!-- section_id: "88dd9d57-dbe9-45e8-b93e-decb61f11290" -->
### Check Status
```bash
# Check if Antigravity is running
ps aux | grep antigravity-server | grep -v grep

# Check if Chrome debugging is active
curl -s http://127.0.0.1:9222/json/version
```

<!-- section_id: "c30d6d13-04d2-42a2-8a97-cd718359d146" -->
### Update Antigravity
```bash
sudo apt update
sudo apt upgrade antigravity
```

---

**Last Updated**: November 25, 2025
**Environment**: WSL2 Ubuntu 24.04
**Antigravity Version**: 1.11.5
**Tested On**: Windows 11 with WSL2
