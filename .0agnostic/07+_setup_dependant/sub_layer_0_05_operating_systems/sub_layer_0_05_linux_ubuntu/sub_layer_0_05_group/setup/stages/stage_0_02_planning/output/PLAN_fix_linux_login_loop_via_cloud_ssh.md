---
resource_id: "7aced408-c814-4a01-9f38-5bf14d23fdcd"
resource_type: "document"
resource_name: "PLAN_fix_linux_login_loop_via_cloud_ssh"
---
# Plan: Fix Linux Login Loop via Cloud Server SSH

**Layer**: 0 (Universal)
**Stage**: 0.02 Planning
**Created**: 2026-01-17
**Related Request**: `REQUEST_fix_linux_login_loop_via_cloud_ssh.md`
**Related Spec**: `SPEC_fix_linux_login_loop_via_cloud_ssh.md`

---

<!-- section_id: "8f699b2e-c3fd-46d1-b336-042794d44cc0" -->
## Execution Plan

<!-- section_id: "b3cf1a29-27d8-4406-bde9-a6ce1fe977b0" -->
### Phase 1: Cloud Server Setup (From Phone)

**Duration**: ~5 minutes
**Prerequisites**: Phone with SSH client, cloud server access

#### Step 1.1: Connect to Cloud Server
```bash
ssh user@cloud-server-address
```

#### Step 1.2: Navigate to Synced Folder
```bash
cd ~/dawson-workspace/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/0.02_operating_systems/linux_ubuntu/setup/trickle_down_0.5_setup/0_instruction_docs/setup/
```

#### Step 1.3: Run AI CLI Setup
```bash
chmod +x cloud_server_ai_cli_master_setup.sh
./cloud_server_ai_cli_master_setup.sh
```

#### Step 1.4: Reload Shell
```bash
source ~/.bashrc
```

#### Step 1.5: Verify Gemini Works
```bash
gemini "Say hello"
```

---

<!-- section_id: "de8745ca-7b26-47e6-b7c6-411d083321c2" -->
### Phase 2: Boot Linux & Get SSH Access

**Duration**: ~3 minutes
**Prerequisites**: Physical access to Linux machine (or remote KVM)

#### Step 2.1: Boot Into Linux
- Start the Linux system
- Let it reach the login screen (login loop is fine)

#### Step 2.2: Get TTY Access (if needed)
- Press `Ctrl+Alt+F2` to get text console
- Login with username and password

#### Step 2.3: Ensure SSH is Running
```bash
sudo systemctl status sshd
# If not running:
sudo systemctl start sshd
```

#### Step 2.4: Get IP Address
```bash
ip addr | grep "inet " | grep -v 127.0.0.1
```
Note the IP address (e.g., 192.168.1.xxx)

---

<!-- section_id: "db74f49f-6064-4438-80c6-17bf0b773584" -->
### Phase 3: SSH from Cloud Server to Linux

**Duration**: ~1 minute

#### Step 3.1: From Cloud Server, Connect to Linux
```bash
ssh dawson@<linux-ip-address>
```

#### Step 3.2: Verify Connection
```bash
whoami
pwd
```

---

<!-- section_id: "96c6a844-1411-48b2-beb2-e2d0ceb87009" -->
### Phase 4: Fix Login Loop

**Duration**: ~5 minutes

#### Step 4.1: Run Diagnostic
```bash
# Check disk space
df -h

# Check home directory permissions
ls -la /home/dawson

# Check for corrupt files
ls -la /home/dawson/.Xauthority
ls -la /home/dawson/.ICEauthority
```

#### Step 4.2: Apply Quick Fixes
```bash
# Remove corrupt auth files
rm -f /home/dawson/.Xauthority
rm -f /home/dawson/.ICEauthority

# Fix permissions
sudo chown -R dawson:dawson /home/dawson
chmod 755 /home/dawson

# Fix /tmp
sudo chmod 1777 /tmp
```

#### Step 4.3: Or Run the Fix Script
```bash
cd ~/dawson-workspace/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/0.02_operating_systems/linux_ubuntu/setup/trickle_down_0.5_setup/0_instruction_docs/setup/

chmod +x fix_linux_login_loop.sh
sudo ./fix_linux_login_loop.sh
```

---

<!-- section_id: "192413d7-664a-42a8-8d6d-a483a1ac560e" -->
### Phase 5: Verify Fix

**Duration**: ~2 minutes

#### Step 5.1: Reboot Linux
```bash
sudo reboot
```

#### Step 5.2: Test Graphical Login
- Wait for system to boot
- Try logging in at the graphical login screen
- Should now enter desktop environment

---

<!-- section_id: "e512e565-347f-455f-9d32-d40001eaee1f" -->
## Contingency Plans

<!-- section_id: "6abf6103-17ce-4260-b3e6-20d90b180c74" -->
### If SSH Connection Fails
1. Use TTY directly on Linux machine (Ctrl+Alt+F2)
2. Run fix commands manually
3. Check firewall: `sudo ufw allow ssh`

<!-- section_id: "a51674bb-7776-41d1-ae52-6903c00bcd6a" -->
### If Quick Fixes Don't Work
1. Check Xorg logs: `cat /var/log/Xorg.0.log | grep -i error`
2. Reinstall display manager: `sudo apt install --reinstall gdm3`
3. Check GPU drivers: `ubuntu-drivers devices`

<!-- section_id: "da32bd3f-3910-4cdd-9a0a-85b32de08349" -->
### If Syncthing Not Working
Copy script content manually or run commands directly

---

<!-- section_id: "3723e0c0-2c82-47b1-8ac2-e42b4e5422f7" -->
## AI Assistance Commands

While connected to cloud server, use AI to help troubleshoot:

```bash
# Ask Gemini for help
gemini "My Linux Ubuntu has a login loop. I've removed .Xauthority but it still doesn't work. What else should I check?"

# Interactive Claude session
claude
> Help me diagnose a Linux login loop. The Xorg.0.log shows: [paste error]
```

---

<!-- section_id: "cae4493f-89c9-4b83-a782-3886e31f3a21" -->
## Success Criteria

- [ ] Phase 1: AI CLIs working on cloud server
- [ ] Phase 2: SSH running on Linux, IP address known
- [ ] Phase 3: Can SSH from cloud server to Linux
- [ ] Phase 4: Fix commands executed
- [ ] Phase 5: Can login to Linux desktop

---

<!-- section_id: "bacc4d0a-eab5-4cd8-8d0a-838ab5b677e1" -->
## Rollback Plan

If fixes cause more issues:
1. Boot into recovery mode
2. Mount filesystem
3. Restore from backup if available
4. Or reinstall desktop environment: `sudo apt install ubuntu-desktop`

---

<!-- section_id: "7b3b463c-27cd-452a-9c60-35f8e12aac57" -->
## Post-Fix: Git Repo Filename Fix

The git repo has files with `*` in names which Windows can't handle. Once Linux is working, fix this by replacing `*` with `x`:

```bash
cd ~/dawson-workspace/code/0_ai_context

# Find files with * in their names
find . -name "*\**" 2>/dev/null

# Rename them - replace * with x
# Example:
git mv "path/to/layer_3_subx2_projects" "path/to/layer_3_subx2_projects"

# Or use this one-liner to find and rename all:
find . -name "*\**" -exec bash -c 'newname="${1//\*/x}"; git mv "$1" "$newname"' _ {} \;

# Commit and push
git add -A
git commit -m "Replace * with x in filenames for Windows compatibility"
git push
```

Then on Windows, `git pull` will work properly.
