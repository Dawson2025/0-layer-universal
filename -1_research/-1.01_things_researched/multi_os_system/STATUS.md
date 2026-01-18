# Status: Multi-OS Workspace Sync

**Last Updated:** 2026-01-18 11:45 MST (from VPS)

---

## Current Session: Goals & Plan

### Request
Set up secure credential storage and Termius Desktop across devices (Linux laptop, Windows) for seamless SSH management with cloud sync.

### Goals
1. ✅ Set up `pass` (GPG-based password manager) on Linux laptop for secure credential storage
2. ✅ Store Termius credentials in pass
3. ✅ Log into Termius Desktop on Linux laptop (enables cloud sync with iPhone)
4. ⏳ Set up Termius on Windows (when booted)
5. ⏳ Complete Windows SSH mesh integration

### Why `pass` Instead of Alternatives?
| Option | Decision | Reason |
|:---|:---|:---|
| .env files | ❌ Rejected | Plaintext, security risk, not recommended in 2025+ |
| Google Secret Manager | ❌ Rejected | 6 secret version free limit, then $0.06/secret/month |
| pass (GPG) | ✅ Chosen | Free, unlimited secrets, encrypted, CLI-friendly |

### Current Execution Status

| Step | Status | Notes |
|:---|:---|:---|
| Install pass + gnupg | ✅ Done | `sudo apt install pass gnupg` |
| Generate GPG key | ✅ Done | ED25519, ID: `1F22130022A1BCF7628E34C9D9918BF45C6C47CB` |
| Initialize pass | ✅ Done | `~/.password-store/` created |
| Configure gpg-agent caching | ✅ Done | 8-hour cache (28800 seconds) |
| Configure pinentry-tty | ✅ Done | For SSH/headless access |
| Store Termius credentials | ✅ Done | `pass insert termius/email` and `termius/password` stored |
| Log into Termius Desktop | ✅ Done | Automated login via xdotool, hosts synced from iPhone |

### Commands to Complete Setup (from iPhone SSH)

```bash
# Store Termius email (will prompt for value twice)
pass insert termius/email

# Store Termius password (will prompt for value twice)
pass insert termius/password

# First use will ask for GPG passphrase, then cached for 8 hours
```

---

## Current System State

| Device | Status | Sync Mode | Connection | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Ubuntu (Native)** | 🟢 **ACTIVE** | Send & Receive | VPS via IPv6 TLS 1.3 | Currently running, sync verified |
| **Hetzner VPS** | 🟢 **Online** | Send & Receive | Always on | Relay server at 46.224.184.10 |
| **Windows/WSL** | ⏸️ Offline | Send & Receive | VPS via IPv6 | Will connect when booted |

## Architecture Overview

```
┌─────────────────┐                    ┌─────────────────┐
│  Ubuntu Native  │◄──── IPv6 TLS ────►│  Hetzner VPS    │
│  (Dual Boot)    │      1.3           │  46.224.184.10  │
│  CURRENTLY ON   │                    │  ALWAYS ON      │
└─────────────────┘                    └────────┬────────┘
                                               │
                                      IPv6 TLS 1.3
                                               │
                                       ┌────────▼────────┐
                                       │  Windows/WSL    │
                                       │  (Dual Boot)    │
                                       │  CURRENTLY OFF  │
                                       └─────────────────┘
```

**Key Constraint:** Ubuntu and Windows are on the SAME physical machine (dual boot). They can NEVER be online simultaneously. The VPS acts as a relay.

---

## Sync Verification Status

| Direction | Status | Verified Date |
| :--- | :--- | :--- |
| **Ubuntu → VPS → Windows** | ✅ **VERIFIED WORKING** | 2026-01-12 |
| **Windows → VPS → Ubuntu** | ✅ **VERIFIED WORKING** | 2026-01-11 |

---

## FOR UBUNTU AGENTS: PRIORITY TASK

**When you boot into Ubuntu, complete the following verification steps:**

### Step 1: Verify Syncthing is Running
```bash
# Check Syncthing status
systemctl --user status syncthing

# If not running, start it
systemctl --user start syncthing

# Open Syncthing GUI (optional)
xdg-open http://localhost:8384
```

### Step 2: Check VPS Connection
In the Syncthing GUI (http://localhost:8384):
- **Hetzner-VPS** should show as connected (green)
- **dawson-workspace** folder should show "Up to Date" after syncing

Or via command line:
```bash
# Check if connected to VPS
curl -s http://localhost:8384/rest/system/connections | grep -A5 "JTAFCHA"
```

### Step 3: Verify Windows Test File Synced

**THIS IS THE KEY VERIFICATION STEP**

```bash
# Check if the Windows test file exists
ls -la ~/dawson-workspace/SYNC_TEST_WINDOWS_TO_UBUNTU.md

# Read the file contents
cat ~/dawson-workspace/SYNC_TEST_WINDOWS_TO_UBUNTU.md
```

**Expected content:** A file created on Windows on 2026-01-12 with sync test information.

**If this file exists and is readable, the bidirectional dual boot sync is FULLY VERIFIED!**

### Step 4: Update This Documentation

After verifying the sync works, update this STATUS.md file:

1. Change the "Windows → VPS → Ubuntu" status to ✅ **VERIFIED WORKING**
2. Add the verification date
3. Update the Recent Log section
4. Commit and push changes:
```bash
cd ~/dawson-workspace/code/0_layer_universal
git add -A
git commit -m "Verify Windows → Ubuntu sync working"
git push
```

### Step 5: (Optional) Quick Verification Script
```bash
~/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/multi_os_system/ubuntu-quick-check.sh
```

---

## What's Working

### Syncthing Three-Way Sync
- **Ubuntu ↔ VPS:** ✅ Configured and tested
- **Windows ↔ VPS:** ✅ Connected and verified (2026-01-12)
- **Sync Folder:** `dawson-workspace` (only folder - "Default Folder" removed 2026-01-17)
- **Sync Status:** Complete, all devices connected

### SSH Access (Full Mesh)

| From | To | Status | Method |
| :--- | :--- | :--- | :--- |
| **VPS** | Linux | ✅ Working | `ssh linux` (via ~/.ssh/config) |
| **Linux** | VPS | ✅ Working | `ssh vps` (via ~/.ssh/config) |
| **iPhone** | VPS | ✅ Working | Termius + SSH key (2026-01-17) |
| **iPhone** | Linux | ✅ Working | Termius + SSH key (2026-01-17) |
| **Windows** | VPS | ✅ Working | `ssh -i ~/.ssh/id_ed25519 root@46.224.184.10` |

### SSH Key Architecture

Each device has its own SSH key pair. The public key is added to `~/.ssh/authorized_keys` on each server the device needs to access.

```
┌─────────────────────────────────────────────────────────────────┐
│                    SSH Key Distribution                          │
├─────────────────────────────────────────────────────────────────┤
│  Device        │ Key Location           │ Can Access            │
├─────────────────────────────────────────────────────────────────┤
│  iPhone        │ Termius Keychain       │ VPS ✅, Linux ✅       │
│  Ubuntu Laptop │ ~/.ssh/id_ed25519      │ VPS ✅, (Windows ⏳)   │
│  VPS           │ /root/.ssh/id_ed25519  │ Linux ✅, (Windows ⏳) │
│  Windows       │ ~/.ssh/id_ed25519      │ VPS ✅                 │
└─────────────────────────────────────────────────────────────────┘
```

**Principle:** One key per device, add public key to all target servers.

### Termius Setup (iPhone)

| Configuration | Status |
| :--- | :--- |
| Termius App | ✅ Installed |
| SSH Key (RSA 4096) | ✅ Imported to Keychain |
| VPS Host | ✅ Configured (SSH key auth) |
| Linux Host | ✅ Configured (SSH key auth) |

### Pass Password Manager (Linux Laptop)

| Component | Status | Details |
|:---|:---|:---|
| pass | ✅ Installed | v1.7.4-6 |
| gnupg | ✅ Installed | v2.4.4 |
| GPG Key | ✅ Created | ED25519, `1F22130022A1BCF7628E34C9D9918BF45C6C47CB` |
| Password Store | ✅ Initialized | `~/.password-store/` |
| gpg-agent caching | ✅ Configured | 8-hour TTL (28800 seconds) |
| pinentry-tty | ✅ Configured | For SSH/headless access |

**GPG Key Details:**
- **Type:** ED25519 (Curve 25519)
- **User ID:** `Dawson <2025computer2025@gmail.com>`
- **Key ID:** `1F22130022A1BCF7628E34C9D9918BF45C6C47CB`
- **Expiration:** Never

**Configuration Files:**
- `~/.gnupg/gpg-agent.conf`:
  ```
  pinentry-program /usr/bin/pinentry-tty
  default-cache-ttl 28800
  max-cache-ttl 28800
  allow-loopback-pinentry
  ```
- `~/.bashrc`: Added `export GPG_TTY=$(tty)`

**Usage:**
```bash
# Store a secret
pass insert service/credential

# Retrieve a secret
pass show service/credential

# List all secrets
pass ls

# First use requires GPG passphrase, then cached for 8 hours
```

### Termius CLI/API Status

| Option | Status | Notes |
| :--- | :--- | :--- |
| Termius CLI (Python) | ❌ Abandoned | Last updated Dec 2020, incompatible with new encryption |
| Termius API Bridge | 💰 Paid Only | Requires Team plan ($9.99/mo), Docker-based |
| Termius Web Version | ❌ None | No browser version exists - native apps only |
| Termius MCP Server | ❌ None | Does not exist |

**Conclusion:** Termius hosts must be added manually via the iPhone/desktop app. No free programmatic access available.

### Termius Desktop Automation (Linux)

| Capability | Status | Notes |
| :--- | :--- | :--- |
| Install Termius Desktop | ✅ Working | `sudo snap install termius-app` |
| Launch with remote debugging | ✅ Working | `termius-app --remote-debugging-port=9222` |
| SSH tunnel for CDP access | ✅ Working | `ssh -L 9222:localhost:9222 linux` |
| xdotool GUI automation | ✅ Working | Keyboard/mouse input, screenshots |
| Playwright MCP connection | ❌ Not supported | MCP server doesn't expose connectOverCDP |

**Status:** ✅ Termius Desktop logged in (2026-01-18). Hosts synced from iPhone:
- VPS (ssh, root)
- Laptop Linux Ubuntu (ssh, dawson)

**Note:** Automated login achieved via xdotool + pass. Credentials retrieved from `pass` and typed into GUI. Hosts now sync automatically with iPhone via Termius cloud.

**Useful xdotool commands for Termius automation:**
```bash
# Launch Termius with remote debugging (on Linux laptop)
DISPLAY=:0 termius-app --remote-debugging-port=9222 &

# Find Termius window ID
DISPLAY=:0 xdotool search --name 'Termius'

# Activate window and send keyboard input
DISPLAY=:0 xdotool windowactivate --sync <window_id>
DISPLAY=:0 xdotool key Tab Return

# Take screenshot of active window
DISPLAY=:0 scrot -u /tmp/screenshot.png
```

**From VPS (remote control via SSH):**
```bash
# SSH tunnel for CDP access
ssh -f -N -L 9222:localhost:9222 linux

# Execute xdotool commands remotely
ssh linux "DISPLAY=:0 xdotool windowactivate --sync 52428805 && DISPLAY=:0 xdotool key Tab"
```

### GUI Automation Learnings (xdotool via SSH)

**What Works:**
| Technique | Status | Notes |
|:---|:---|:---|
| `xdotool search --name` | ✅ Works | Find window IDs by name |
| `xdotool windowactivate` | ✅ Works | Bring window to focus |
| `xdotool type 'text'` | ✅ Works | Type text into focused field |
| `xdotool key Tab` | ✅ Works | Navigate between form fields |
| `xdotool key Return` | ✅ Works | Submit forms/click focused buttons |
| `scrot -u` | ✅ Works | Screenshot active window |
| Multi-step automation | ✅ Works | Chain commands with sleep delays |
| Retrieve secrets from `pass` | ✅ Works | `pass show service/credential` |
| Remote SSH control | ✅ Works | `ssh linux "DISPLAY=:0 xdotool ..."` |

**What Doesn't Work / Challenges:**
| Issue | Details | Workaround |
|:---|:---|:---|
| Tab order unpredictable | Different apps have inconsistent tab order | Trial and error, count tabs carefully |
| Enter key on forms | Enter may toggle visibility (eye icon) instead of submit | Use Tab to focus button first, then Enter |
| Google OAuth popups | Opens new browser window, harder to automate | Avoid Google SSO, use direct login |
| Window ID changes | New windows get new IDs after restart | Re-search with `xdotool search` |
| High-res screenshots | 2560x1600 screenshots cause API size limits | Use `scrot -q 20` for lower quality |
| No ImageMagick | `convert` not installed by default | Install with `sudo apt install imagemagick` |

**Reliable Automation Pattern:**
```bash
# 1. Launch app
ssh linux "DISPLAY=:0 nohup /snap/bin/termius-app > /tmp/app.log 2>&1 &"
sleep 4

# 2. Find and activate window
WID=$(ssh linux "DISPLAY=:0 xdotool search --name 'Termius' | tail -1")
ssh linux "DISPLAY=:0 xdotool windowactivate --sync $WID"

# 3. Get credentials from pass (must be unlocked first)
EMAIL=$(ssh linux "pass show termius/email")
PASSWORD=$(ssh linux "pass show termius/password")

# 4. Navigate and type (with delays)
ssh linux "DISPLAY=:0 xdotool type '$EMAIL'"
sleep 0.3
ssh linux "DISPLAY=:0 xdotool key Tab"  # Move to next field or button
sleep 0.3
ssh linux "DISPLAY=:0 xdotool key Return"  # Submit

# 5. Screenshot to verify state
ssh linux "DISPLAY=:0 scrot -q 20 /tmp/state.png"
scp linux:/tmp/state.png /tmp/state.png
```

**Key Lessons:**
1. Always verify GPG is unlocked before retrieving `pass` secrets (`pass show` requires passphrase on first use)
2. Use `--sync` with `windowactivate` to ensure window is focused before typing
3. Add `sleep 0.3` - `sleep 1` between actions to allow UI to update
4. Tab order varies - test manually first to determine correct tab count
5. Escape key can reset forms/close dialogs if something goes wrong
6. Restarting the app gives a clean state when automation gets stuck

### Test Files for Verification

| File | Created On | Status |
| :--- | :--- | :--- |
| `SYNC_TEST_UBUNTU_TO_WINDOWS.md` | Ubuntu (2026-01-11 14:11 MST) | ✅ Verified on Windows |
| `SYNC_TEST_WINDOWS_TO_UBUNTU.md` | Windows (2026-01-12 00:10 MST) | ✅ Verified on Ubuntu |

---

## Key Configuration Details

### Syncthing Device IDs
| Device | ID |
| :--- | :--- |
| Ubuntu | `7UVVQQS-O3463OC-GUTDI63-EWLX3SE-LRX4ZU3-MEOWA34-KSCMF6K-DR7GEAH` |
| Windows/WSL | `IF2WOGZ-RVSVKT3-RCRN3TT-6NDFXQX-KCCCFPW-ABIWRWT-3BFX37C-CDHKTAN` |
| Hetzner VPS | `JTAFCHA-VWKO4GU-W5N6GWM-GHAZC6Y-GCLT4VI-PWAXY45-UBCP3RJ-2ZPJWQR` |

### VPS Details
- **IP:** 46.224.184.10
- **IPv6:** 2a01:4f8:1c1a:885b::1
- **Tailscale IP:** 100.93.148.5
- **Syncthing GUI:** http://46.224.184.10:8384 (user: admin, pass: SyncthingVPS2026)
- **SSH:** `ssh -i ~/.ssh/id_ed25519 root@46.224.184.10` or `ssh vps` (from Linux)
- **Sync Folder on VPS:** `/root/sync/dawson-workspace`

### Tailscale Network

| Device | Tailscale IP | Status |
| :--- | :--- | :--- |
| Ubuntu Laptop | 100.73.84.89 | ✅ Connected |
| VPS | 100.93.148.5 | ✅ Connected |
| iPhone | 100.75.210.27 | ✅ Connected |

### Syncthing Ports
- 22000/TCP - Data transfer
- 21027/UDP - Local discovery
- 8384/TCP - Web GUI

---

## Recent Log

- **2026-01-18 11:45:** ✅ **Termius Desktop login complete!** Automated login via xdotool + pass. Hosts synced from iPhone (VPS, Laptop Linux Ubuntu visible). Documented GUI automation learnings.
- **2026-01-18 11:30:** ✅ User stored Termius credentials in pass (`termius/email`, `termius/password`). GPG passphrase entered via iPhone SSH to unlock gpg-agent.
- **2026-01-18 00:45:** ✅ Set up `pass` password manager on Linux laptop. GPG key generated (ED25519), pass initialized, gpg-agent configured for 8-hour caching.
- **2026-01-18 00:30:** 📚 Researched secure credential storage options. Compared .env files, Google Secret Manager, pass (GPG). Chose pass for unlimited free secrets with encryption.
- **2026-01-18 00:03:** ✅ Tested Termius Desktop automation on Linux laptop via xdotool. Successfully installed (snap), launched with CDP, automated GUI via keyboard/mouse. Requires manual login for cloud sync. Documented findings.
- **2026-01-17 23:30:** ✅ Investigated Termius CLI/API options. CLI abandoned (2020), API Bridge requires paid Team plan. Documented limitations. iPhone Termius fully configured (VPS + Linux hosts with SSH key auth).
- **2026-01-17 22:50:** ✅ iPhone Termius configured with SSH key auth for VPS. Generated RSA 4096 key, added to VPS and Linux authorized_keys. Documented SSH key architecture.
- **2026-01-17 21:15:** ✅ Set up SSH configs on VPS (`/home/dawson/.ssh/config`) and Linux (`~/.ssh/config`) for easy `ssh linux` and `ssh vps` commands. Copied SSH keys to dawson user on VPS.
- **2026-01-17 20:00:** ✅ Git pull from 0-universal-context repo. Linux Ubuntu setup stages now present (stage_0_00 through stage_0_03).
- **2026-01-17 19:00:** ✅ Authenticated GitHub CLI on VPS. Set up git for 0_layer_universal repo.
- **2026-01-17 12:30:** ✅ Integrated `0_ai_context` into `0_layer_universal`. Removed empty "Default Folder" from Syncthing. Cleaned up `/home/dawson/Sync`.
- **2026-01-17 11:48:** Syncthing running, connected to VPS. Login loop fix holding (LightDM).
- **2026-01-11 17:27:** ✅ **BIDIRECTIONAL SYNC FULLY VERIFIED!** Windows → Ubuntu sync confirmed working on Ubuntu boot.
- **2026-01-12 00:10:** ✅ Windows verification complete. Ubuntu → Windows sync confirmed working. Created reverse test file for Ubuntu verification.
- **2026-01-12 00:01:** Windows Syncthing started, connected to VPS via IPv6.
- **2026-01-11 16:45:** Documentation updated for Windows agent handoff.
- **2026-01-11 16:38:** ✅ Ubuntu SSH key added to VPS.
- **2026-01-11 14:11:** ✅ Dual boot test file created on Ubuntu and synced to VPS.
- **2026-01-11 14:03:** ✅ THREE-WAY SYNC OPERATIONAL! Ubuntu ↔ VPS ↔ Windows/WSL all configured.
- **2026-01-10:** Hetzner VPS created and configured as relay server.

---

## Completed Tasks

1. ✅ Create Hetzner VPS as relay server
2. ✅ Install and configure Syncthing on VPS
3. ✅ Connect Windows/WSL to VPS
4. ✅ Connect Ubuntu to VPS
5. ✅ Configure SSH access from both Ubuntu and Windows
6. ✅ Create Ubuntu → Windows test file
7. ✅ **Verify Ubuntu → Windows sync (2026-01-12)**
8. ✅ Create Windows → Ubuntu test file
9. ✅ **Fix Ubuntu login loop** - Switched from GDM3 to LightDM (2026-01-17)
10. ✅ **Integrate 0_ai_context into 0_layer_universal** (2026-01-17)
11. ✅ **Clean up Syncthing** - Removed empty "Default Folder" (2026-01-17)
12. ✅ **Set up SSH configs** - VPS and Linux now use `ssh linux` / `ssh vps` aliases (2026-01-17)
13. ✅ **iPhone Termius setup** - Installed app, imported SSH key, configured VPS host with key auth (2026-01-17)
14. ✅ **GitHub CLI on VPS** - Authenticated and configured git for 0_layer_universal (2026-01-17)
15. ✅ **iPhone Termius Linux host** - Configured with SSH key auth (2026-01-17)
16. ✅ **Termius CLI/API investigation** - CLI abandoned, API Bridge requires paid plan, no free programmatic access (2026-01-17)
17. ✅ **Termius Desktop automation test** - Installed on Linux (snap), tested xdotool GUI automation. Works but requires manual login for cloud sync (2026-01-18)
18. ✅ **Pass password manager setup** - Installed pass + gnupg, generated GPG key, initialized password store, configured gpg-agent for 8-hour caching (2026-01-18)
19. ✅ **Store Termius credentials in pass** - Stored `termius/email` and `termius/password` (2026-01-18)
20. ✅ **Termius Desktop login** - Automated login via xdotool + pass, hosts synced from iPhone cloud (2026-01-18)
21. ✅ **Document GUI automation learnings** - What works/doesn't work with xdotool via SSH (2026-01-18)

## Pending Tasks

### Windows Setup (When Booted)
1. ⏳ **Windows: Enable OpenSSH Server** - Required for full mesh SSH
2. ⏳ **Windows: Get Tailscale IP** - Need IP for SSH config and Termius
3. ⏳ **Add Windows to SSH mesh** - Add VPS, Linux, iPhone public keys to Windows authorized_keys
4. ⏳ **Set up Termius on Windows** - Already installed, needs login
5. ⏳ **Add Windows host to iPhone Termius** - Manual setup required

### Future
6. ⏳ **Monitor Oracle Cloud ticket** - May migrate to free tier if approved
7. ⏳ **Test full mesh connectivity** - All devices SSH to all others

---

## Troubleshooting

### Ubuntu: Syncthing not running
```bash
# Check status
systemctl --user status syncthing

# Start if needed
systemctl --user start syncthing

# Check logs
journalctl --user -u syncthing -f
```

### Ubuntu: Files not syncing
1. Check folder status in Syncthing GUI (http://localhost:8384)
2. Look for "Out of Sync" items
3. Check `.stignore` file for excluded patterns
4. Force rescan: `curl -X POST http://localhost:8384/rest/db/scan?folder=dawson-workspace`

### SSH connection issues
- Ensure using correct key: `~/.ssh/id_ed25519`
- VPS IP: 46.224.184.10
- Username: root

---

## Related Documentation

- [VPS_CREDENTIALS.md](./VPS_CREDENTIALS.md) - Full VPS access details
- [DUAL_BOOT_TEST_INSTRUCTIONS.md](./DUAL_BOOT_TEST_INSTRUCTIONS.md) - Testing procedure
- [README.md](./README.md) - Project overview
