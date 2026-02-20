# iPhone Quick Guide - Fix Linux via VPS

**Purpose:** Fix Linux login loop using iPhone → VPS → Linux

---

## Step 1: Get an SSH App

**Recommended:** [Termius](https://apps.apple.com/app/termius/id549039908) (free)

**Alternatives:**
- Prompt 3 (paid, excellent)
- Blink Shell (paid)
- a]Shell (free)

---

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

## Quick Commands (if not using menu)

| Command | What it does |
|---------|--------------|
| `h` | Show help |
| `g "question"` | Ask Gemini |
| `c "question"` | Ask Claude |
| `cx "question"` | Ask Codex |
| `menu` | Open interactive menu |

---

## The Full Process

### Phase 1: Boot Linux
1. Turn on the Linux computer
2. Let it reach the login screen (loop is fine)
3. Press `Ctrl+Alt+F2` for text terminal
4. Login with your username/password
5. Run: `ip addr | grep inet`
6. Note the IP (e.g., `192.168.1.100`)

### Phase 2: From iPhone
1. Open Termius (or your SSH app)
2. Connect to `root@46.224.184.10`
3. Type `menu` and press Enter
4. Press `7` to set Linux IP
5. Enter the IP from step 6 above
6. Press `4` to SSH into Linux

### Phase 3: Fix Login Loop
Once connected to Linux (via VPS):
```bash
sudo rm -f ~/.Xauthority ~/.ICEauthority
sudo chown -R dawson:dawson /home/dawson
sudo chmod 1777 /tmp
sudo reboot
```

Or from the menu, press `5` to run the fix script automatically.

### Phase 4: Test
After Linux reboots, try logging in at the graphical screen.

---

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

## Troubleshooting

### Can't connect to VPS
- Check WiFi/cellular connection
- Verify IP: `46.224.184.10`
- Try password auth if key doesn't work

### Can't connect to Linux from VPS
- Make sure Linux SSH is running: `sudo systemctl start sshd`
- Check Linux IP is correct
- Check Linux firewall: `sudo ufw allow ssh`

### AI CLI not working
- Try reloading shell: `source ~/.bashrc`
- Check if credentials expired (they auto-refresh usually)

---

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
