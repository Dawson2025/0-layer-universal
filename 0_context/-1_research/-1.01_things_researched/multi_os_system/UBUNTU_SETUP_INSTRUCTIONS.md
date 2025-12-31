# Ubuntu Desktop Setup Instructions

## Overview
This guide will complete the multi-OS workspace sync by setting up the Ubuntu desktop portion. WSL and Windows are already configured and syncing successfully.

## Prerequisites Check
Before starting, verify you're on the Ubuntu desktop machine:
\\ash
# Should show Ubuntu
lsb_release -a

# Should show your username
whoami  # Expected: dawson
\
## Step 1: Pull Latest Changes from GitHub

\\ash
# Navigate to your code directory (if it exists, otherwise skip)
cd ~/code/0_ai_context/0_context/-1_research/-1.01_things_researched/multi_os_system 2>/dev/null || echo 'Will create workspace first'

# If the directory exists, pull latest
git pull 2>/dev/null || echo 'Will set up via Syncthing instead'
\
## Step 2: Create Workspace Directory Structure

\\ash
# Create the canonical workspace root
mkdir -p ~/dawson-workspace

# Create all subdirectories
cd ~/dawson-workspace
mkdir -p code agents ai-mcp data docs dotfiles java mcp-servers mcp-setup scripts templates uploads videos

# Verify structure
ls -la ~/dawson-workspace/
\
## Step 3: Install Syncthing

\\ash
# Add Syncthing repository
sudo curl -o /usr/share/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg
echo 'deb [signed-by=/usr/share/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable' | sudo tee /etc/apt/sources.list.d/syncthing.list

# Update and install
sudo apt update
sudo apt install syncthing

# Verify installation
syncthing --version
\
## Step 4: Configure Syncthing to Start Automatically

\\ash
# Enable and start Syncthing service for your user
systemctl --user enable syncthing.service
systemctl --user start syncthing.service

# Check status
systemctl --user status syncthing.service

# Syncthing web UI should now be available at:
# http://localhost:8384
\
## Step 5: Configure Syncthing Devices and Folder

### 5.1 Get Device IDs from WSL/Windows
You'll need the device IDs from your other machines. See DEVICE_IDS.md in this directory for the complete list.

### 5.2 Add Devices in Syncthing Web UI
1. Open http://localhost:8384 in your browser
2. Click **Actions** → **Show ID** to see your Ubuntu device ID
3. **Copy this ID** - you'll need to add it to WSL and Windows
4. Click **Add Remote Device**
5. Add both WSL and Windows devices using IDs from DEVICE_IDS.md
6. Click **Save** for each

### 5.3 Add Ubuntu Device to WSL and Windows
This step will need to be done when you switch back to WSL/Windows, or you can do it remotely if you have network access.

**On WSL**:
- Open http://localhost:8384
- Add Remote Device with Ubuntu's device ID (which you copied in step 5.2)
- Name it: \Ubuntu-Dawson
**On Windows**:
- Open http://localhost:8384  
- Add Remote Device with Ubuntu's device ID
- Name it: \Ubuntu-Dawson
### 5.4 Accept Folder Share
After devices are connected:
1. You should see a notification about a new folder share: \dawson-workspace2. Click **Add**
3. Set folder path to: \/home/dawson/dawson-workspace4. Set folder type to: **Send & Receive**
5. Click **Save**

### 5.5 Enable File Versioning
1. In the folder settings for \dawson-workspace2. Go to **File Versioning** tab
3. Select: **Staggered File Versioning**
4. Set **Maximum Age**: \1209600\ (14 days, matching WSL/Windows)
5. Click **Save**

## Step 6: Verify Sync is Working

\\ash
# Wait a few moments for initial sync, then check
ls -la ~/dawson-workspace/

# You should see files syncing from WSL/Windows, including:
# - SYNC_TEST.md (the test file)
# - README.md, WORKSPACE_STRUCTURE.md
# - code/, agents/, ai-mcp/, etc. with content

# Check the test file
cat ~/dawson-workspace/SYNC_TEST.md

# Create a test from Ubuntu
echo 'Ubuntu sync verification - 12/31/2025 07:45:32' >> ~/dawson-workspace/SYNC_TEST.md

# Wait 10 seconds, then check on WSL/Windows to verify it synced
\
## Step 7: Install Dotfiles

\\ash
# The dotfiles directory should sync from WSL/Windows
# OR clone fresh from GitHub:
cd ~/dawson-workspace
git clone https://github.com/Dawson2025/dotfiles.git

# Run the installer
cd dotfiles
./install.sh

# Reload your shell
source ~/.bashrc
\
## Step 8: Verify Git Setup

\\ash
# Check git config
git config --global user.name
git config --global user.email

# If not set, configure:
git config --global user.name 'Your Name'
git config --global user.email 'your.email@example.com'

# Set up SSH key for GitHub (if needed)
ssh-keygen -t ed25519 -C 'your.email@example.com'
cat ~/.ssh/id_ed25519.pub
# Add this to GitHub: https://github.com/settings/keys
\
## Step 9: Final Verification

\\ash
# Check workspace structure
tree -L 2 ~/dawson-workspace/ 2>/dev/null || ls -la ~/dawson-workspace/

# Verify Syncthing status
systemctl --user status syncthing.service

# Check sync status in web UI
# Open http://localhost:8384
# All three devices should show 'Up to Date'

# Test three-way sync
echo 'Final Ubuntu verification - 12/31/2025 07:45:32' > ~/dawson-workspace/ubuntu-test.txt
# Check on WSL and Windows after a few seconds to confirm sync
\
## Step 10: Update Documentation

\\ash
# Mark Ubuntu setup as complete in the status document
cd ~/dawson-workspace/code/0_ai_context/0_context/-1_research/-1.01_things_researched/multi_os_system

# Edit PLAN_AND_IMPLEMENTATION.md to add Ubuntu completion status
# Then commit and push
git add .
git commit -m 'docs: Mark Ubuntu desktop setup as complete'
git push
\
## Troubleshooting

### Syncthing not starting
\\ash
# Check logs
journalctl --user -u syncthing.service -f
\
### Devices not connecting
- Ensure all three machines are on the same network or can reach each other
- Check firewall settings (port 22000 for Syncthing)
- Verify device IDs are correct

### Files not syncing
- Check .stignore file in ~/dawson-workspace/.stignore
- Verify folder is set to 'Send & Receive' on all devices
- Check Syncthing web UI for errors

## Success Criteria

✅ Ubuntu workspace exists at \/home/dawson/dawson-workspace✅ Syncthing running and enabled at startup  
✅ All three devices connected (WSL, Windows, Ubuntu)
✅ Folder \dawson-workspace\ shared and syncing
✅ Test files sync in all directions
✅ Dotfiles installed and shell configured
✅ Git configured with proper credentials

## Next Steps After Completion

Once Ubuntu is set up:
- You can work on any of the three systems
- Changes will sync automatically within seconds
- Use Git for version control of code projects
- Use Syncthing for file sync and backup
- Dotfiles keep your shell environment consistent

---
**Setup completed on**: 2025-12-31
**Ubuntu device ID**: 7UVVQQS-O3463OC-GUTDI63-EWLX3SE-LRX4ZU3-MEOWA34-KSCMF6K-DR7GEAH
