---
resource_id: "bcb8755c-4d81-458c-bf67-6fa233d46e09"
resource_type: "knowledge"
resource_name: "UBUNTU_SETUP_INSTRUCTIONS"
---
# Ubuntu Desktop Setup Instructions

<!-- section_id: "ba5fcdcc-8e6b-4ebe-a658-e4fcf1ad7508" -->
## Overview
This guide will complete the multi-OS workspace sync by setting up the Ubuntu desktop portion. WSL and Windows are already configured and syncing successfully.

<!-- section_id: "bfcb23d1-fa1f-493e-aaea-1eb55e16e01f" -->
## Prerequisites Check
Before starting, verify you're on the Ubuntu desktop machine:
\\ash
# Should show Ubuntu
lsb_release -a

# Should show your username
whoami  # Expected: dawson
\
<!-- section_id: "26fdab4c-50c3-4085-bfd4-983a71b57c17" -->
## Step 1: Pull Latest Changes from GitHub

\\ash
# Navigate to your code directory (if it exists, otherwise skip)
cd ~/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/multi_os_system 2>/dev/null || echo 'Will create workspace first'

# If the directory exists, pull latest
git pull 2>/dev/null || echo 'Will set up via Syncthing instead'
\
<!-- section_id: "98dbaeaf-a66c-4730-a078-b98fda80aa90" -->
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
<!-- section_id: "19601f4e-9ffa-4177-9ebb-dfd954885441" -->
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
<!-- section_id: "0f222986-82e4-4560-b4c0-895d0a3cf8ab" -->
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
<!-- section_id: "da63ad04-7f9a-469e-8ce8-6ab73de86594" -->
## Step 5: Configure Syncthing Devices and Folder

<!-- section_id: "04f23d82-0f19-45dd-9e4b-ed4cf5fe8ca2" -->
### 5.1 Get Device IDs from WSL/Windows
You'll need the device IDs from your other machines. See DEVICE_IDS.md in this directory for the complete list.

<!-- section_id: "6b460c95-1a08-4f7d-822b-47777ed814ba" -->
### 5.2 Add Devices in Syncthing Web UI
1. Open http://localhost:8384 in your browser
2. Click **Actions** → **Show ID** to see your Ubuntu device ID
3. **Copy this ID** - you'll need to add it to WSL and Windows
4. Click **Add Remote Device**
5. Add both WSL and Windows devices using IDs from DEVICE_IDS.md
6. Click **Save** for each

<!-- section_id: "06be1892-1d3a-4c59-bb34-79f319e4901b" -->
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
<!-- section_id: "ee7a76a0-77f4-4339-9e75-f518376754f6" -->
### 5.4 Accept Folder Share
After devices are connected:
1. You should see a notification about a new folder share: \dawson-workspace2. Click **Add**
3. Set folder path to: \/home/dawson/dawson-workspace4. Set folder type to: **Send & Receive**
5. Click **Save**

<!-- section_id: "7ac9ae64-8ff9-4c35-8a01-d6ba3605de62" -->
### 5.5 Enable File Versioning
1. In the folder settings for \dawson-workspace2. Go to **File Versioning** tab
3. Select: **Staggered File Versioning**
4. Set **Maximum Age**: \1209600\ (14 days, matching WSL/Windows)
5. Click **Save**

<!-- section_id: "b223fedd-5c94-4163-a3aa-a9ee740cce26" -->
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
<!-- section_id: "8d483764-e44c-4970-b1c1-98e9dea460fb" -->
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
<!-- section_id: "591efef6-2e11-4b8a-b4bc-57db0be868b9" -->
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
<!-- section_id: "3443bbc3-b096-4123-a623-4625149ebf4f" -->
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
<!-- section_id: "88ad2bbd-3b33-4f5e-bced-17222bf39f1a" -->
## Step 10: Update Documentation

\\ash
# Mark Ubuntu setup as complete in the status document
cd ~/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/multi_os_system

# Edit PLAN_AND_IMPLEMENTATION.md to add Ubuntu completion status
# Then commit and push
git add .
git commit -m 'docs: Mark Ubuntu desktop setup as complete'
git push
\
<!-- section_id: "c80be925-c075-401e-b8ac-b313b2a32ce4" -->
## Troubleshooting

<!-- section_id: "a3b57de4-cad6-46de-b987-0baf5738b3d3" -->
### Syncthing not starting
\\ash
# Check logs
journalctl --user -u syncthing.service -f
\
<!-- section_id: "78843737-10f1-44e2-b18f-fd3278cb0c6b" -->
### Devices not connecting
- Ensure all three machines are on the same network or can reach each other
- Check firewall settings (port 22000 for Syncthing)
- Verify device IDs are correct

<!-- section_id: "068d0116-4ba0-41a1-8af5-03e570c17a2b" -->
### Files not syncing
- Check .stignore file in ~/dawson-workspace/.stignore
- Verify folder is set to 'Send & Receive' on all devices
- Check Syncthing web UI for errors

<!-- section_id: "51f22786-1bca-4557-99ea-5827f2bdbf10" -->
## Success Criteria

✅ Ubuntu workspace exists at \/home/dawson/dawson-workspace✅ Syncthing running and enabled at startup  
✅ All three devices connected (WSL, Windows, Ubuntu)
✅ Folder \dawson-workspace\ shared and syncing
✅ Test files sync in all directions
✅ Dotfiles installed and shell configured
✅ Git configured with proper credentials

<!-- section_id: "bca310b6-718c-4ef1-8ece-c4c048f11b90" -->
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
