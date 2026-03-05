---
resource_id: "ed402f07-02f5-4bd8-9ff8-aba4cd877662"
resource_type: "document"
resource_name: "IPHONE_QUICK_GUIDE"
---
# iPhone Quick Guide - Fix Linux via VPS

**Purpose:** Fix Linux login loop using iPhone → VPS → Linux

---

<!-- section_id: "a17bc2d7-1235-4df4-a758-5f80cc8a3c11" -->
## Step 1: Get an SSH App

**Recommended:** [Termius](https://apps.apple.com/app/termius/id549039908) (free)

**Alternatives:**
- Prompt 3 (paid, excellent)
- Blink Shell (paid)
- a]Shell (free)

---

<!-- section_id: "e4485914-4bc2-46bd-8d90-7bdd34bcd868" -->
## Step 2: Configure SSH Connection

In your SSH app, create a new host:

| Field | Value |
|-------|-------|
| Host | `46.224.184.10` |
| Port | `22` |
| Username | `root` |
| Auth | SSH Key (copy from Windows) or Password |

**To get SSH key for iPhone:**
On Windows, run this and copy the output to your iPhone:
```
cat ~/.ssh/id_ed25519
```

---

<!-- section_id: "03261bff-52a0-41f2-b76f-54f77f3d8c51" -->
## Step 3: Connect and Use Menu

Once connected, just type:
```
menu
```

You'll see:
```
================================
   VPS Quick Menu (for phone)
================================

  1) Ask Gemini
  2) Ask Claude
  3) Ask Codex
  4) SSH to Linux
  5) Run Linux fix script
  6) Check Syncthing status
  7) Set Linux IP
  q) Quit

Choice:
```

---

<!-- section_id: "7da3c158-f494-403b-b2c1-ab19cd10ffbc" -->
## Quick Commands (if not using menu)

| Command | What it does |
|---------|--------------|
| `h` | Show help |
| `g "question"` | Ask Gemini |
| `c "question"` | Ask Claude |
| `cx "question"` | Ask Codex |
| `menu` | Open interactive menu |

---

<!-- section_id: "af2310d8-5a47-4e2b-8331-198b58e3f1a0" -->
## The Full Process

<!-- section_id: "c02fe06e-bb29-42b4-b997-4d6e28e49fb4" -->
### Phase 1: Boot Linux
1. Turn on the Linux computer
2. Let it reach the login screen (loop is fine)
3. Press `Ctrl+Alt+F2` for text terminal
4. Login with your username/password
5. Run: `ip addr | grep inet`
6. Note the IP (e.g., `192.168.1.100`)

<!-- section_id: "7a906789-41e3-4876-ab9c-bd9ac268a5cd" -->
### Phase 2: From iPhone
1. Open Termius (or your SSH app)
2. Connect to `root@46.224.184.10`
3. Type `menu` and press Enter
4. Press `7` to set Linux IP
5. Enter the IP from step 6 above
6. Press `4` to SSH into Linux

<!-- section_id: "6c7606df-6011-4937-8bbe-558706024fab" -->
### Phase 3: Fix Login Loop
Once connected to Linux (via VPS):
```bash
sudo rm -f ~/.Xauthority ~/.ICEauthority
sudo chown -R dawson:dawson /home/dawson
sudo chmod 1777 /tmp
sudo reboot
```

Or from the menu, press `5` to run the fix script automatically.

<!-- section_id: "c0f6c236-c3a0-4231-8e53-76280c40f0ae" -->
### Phase 4: Test
After Linux reboots, try logging in at the graphical screen.

---

<!-- section_id: "152fffda-2c7a-4446-abd4-431c2468b1cd" -->
## If You Need AI Help

From the VPS (after `menu`):
- Press `1` for Gemini
- Press `2` for Claude
- Press `3` for Codex

Example prompts:
- "My Linux login loop persists after removing .Xauthority. What else should I check?"
- "How do I check Xorg logs for errors?"
- "What causes Ubuntu login loops?"

---

<!-- section_id: "c5aafdd5-8362-4976-ade2-91bade221898" -->
## Troubleshooting

<!-- section_id: "dd662ac3-01af-4930-b7b1-b2ba43723e6a" -->
### Can't connect to VPS
- Check WiFi/cellular connection
- Verify IP: `46.224.184.10`
- Try password auth if key doesn't work

<!-- section_id: "f288ee59-f9c5-4bf3-bca2-4b7b7ba593d6" -->
### Can't connect to Linux from VPS
- Make sure Linux SSH is running: `sudo systemctl start sshd`
- Check Linux IP is correct
- Check Linux firewall: `sudo ufw allow ssh`

<!-- section_id: "83a4ce3b-2a4e-46c6-9776-9f17850b3465" -->
### AI CLI not working
- Try reloading shell: `source ~/.bashrc`
- Check if credentials expired (they auto-refresh usually)

---

<!-- section_id: "50a4a36d-a743-4f2d-a588-e776ee7b2d4d" -->
## Copy-Paste Commands

**SSH to VPS (for apps that support URL schemes):**
```
ssh://root@46.224.184.10
```

**One-liner to start menu:**
```
menu
```

**One-liner to fix Linux (after SSH to Linux):**
```
sudo rm -f ~/.Xauthority ~/.ICEauthority && sudo chown -R $USER:$USER ~ && sudo reboot
```

---

<!-- section_id: "de14078f-5152-4029-ac62-b18d80b22be3" -->
## Bonus: Enable Passwordless SSH from VPS

After fixing Linux, run this once to allow future SSH without password:

```bash
# On Linux, in the synced folder:
cd ~/dawson-workspace/.../setup/
./add_vps_key_to_linux.sh
```

Or manually:
```bash
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w root@ubuntu-4gb-nbg1-1" >> ~/.ssh/authorized_keys
```

---

<!-- section_id: "53fbd038-5b73-41f6-ab06-954fca17fc76" -->
## Summary: What You Need to Do

| Step | Where | Action |
|------|-------|--------|
| 1 | Linux | Boot, Ctrl+Alt+F2, get IP |
| 2 | iPhone | SSH to VPS: `ssh root@46.224.184.10` |
| 3 | iPhone | Type `menu`, press 6, enter Linux IP |
| 4 | iPhone | Press 4 to SSH to Linux |
| 5 | iPhone | Run fix commands, reboot |
| 6 | Linux | Test graphical login |

**Total phone typing: ~20 keystrokes** (after initial SSH app setup)
