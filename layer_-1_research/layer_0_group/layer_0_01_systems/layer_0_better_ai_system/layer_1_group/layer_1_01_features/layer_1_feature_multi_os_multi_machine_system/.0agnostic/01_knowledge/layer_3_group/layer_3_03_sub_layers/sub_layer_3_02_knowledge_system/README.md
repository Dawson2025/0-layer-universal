---
resource_id: "076467ee-21b7-4440-862d-d6b856aa416e"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Multi-OS Workspace Sync Documentation

This directory contains documentation for the multi-OS workspace sync project, which maintains a synchronized `dawson-workspace` across Windows, WSL, and Ubuntu (dual boot) using Syncthing with a VPS relay.

<!-- section_id: "372f21ff-5c66-48b5-93e0-433489df4581" -->
## Current Status: ✅ FULLY OPERATIONAL

**Last Updated:** 2026-01-21
**All systems configured and syncing via Hetzner VPS relay**
**Windows & VPS resilience implemented with auto-recovery**

<!-- section_id: "2442a8c6-251c-49bb-b3e6-360541d494ba" -->
### Verification Progress
| Direction | Status |
| :--- | :--- |
| Ubuntu → VPS → Windows | ✅ Verified |
| Windows → VPS → Ubuntu | ✅ Verified |

<!-- section_id: "e1faee7a-b567-4791-abe8-ae9fbad316ab" -->
## Quick Reference

| If you're on... | Status | What to do |
| :--- | :--- | :--- |
| **Ubuntu (Native)** | ✅ Verified | Syncthing connected to VPS, sync working |
| **Windows** | ✅ Verified | Syncthing connected to VPS, sync working |
| **WSL** | ✅ Complete | Syncthing shares config with Windows |

<!-- section_id: "1671aba0-c689-4dfe-8f18-156224cb2095" -->
## Architecture

```
┌─────────────────┐                    ┌─────────────────┐
│  Ubuntu Native  │◄──── IPv6 TLS ────►│  Hetzner VPS    │
│  (Dual Boot)    │      1.3           │  46.224.184.10  │
└─────────────────┘                    │  ALWAYS ON      │
                                       └────────┬────────┘
                                                │
                                       IPv6 TLS 1.3
                                                │
                                       ┌────────▼────────┐
                                       │  Windows/WSL    │
                                       │  (Dual Boot)    │
                                       └─────────────────┘
```

**Key Point:** Ubuntu and Windows are dual boot on the SAME machine. They can never be online together. The VPS relays changes between them.

<!-- section_id: "e010edf5-9ce8-47ed-9e10-b9db17fcd57f" -->
## Key Documents

| Document | Purpose |
| :--- | :--- |
| **[STATUS.md](./STATUS.md)** | Current system state, what's working, next steps |
| **[VPS_CREDENTIALS.md](./VPS_CREDENTIALS.md)** | VPS access details, SSH commands, API keys |
| **[DUAL_BOOT_TEST_INSTRUCTIONS.md](./DUAL_BOOT_TEST_INSTRUCTIONS.md)** | How to verify sync is working |
| **[WINDOWS_RESILIENCE_RECOVERY.md](./WINDOWS_RESILIENCE_RECOVERY.md)** | Windows SSH setup, auto-recovery, remote access |
| **[VPS_RESILIENCE_RECOVERY.md](./VPS_RESILIENCE_RECOVERY.md)** | VPS hardening, fail2ban, auto-restart configs |
| **[LINUX_RESILIENCE_RECOVERY.md](./LINUX_RESILIENCE_RECOVERY.md)** | Ubuntu recovery procedures |

<!-- section_id: "8b6c1f0f-0f44-449b-b92c-ea25898d0939" -->
## Quick Commands

<!-- section_id: "82ad9cc7-71a1-4bce-bd22-ea36aa7b804a" -->
### Ubuntu
```bash
# Check Syncthing status
systemctl --user status syncthing

# Open Syncthing GUI
xdg-open http://localhost:8384

# SSH to VPS
ssh -i ~/.ssh/id_ed25519 root@46.224.184.10
```

<!-- section_id: "30a66175-6ea8-43cb-ac52-7cc08bad0e2e" -->
### Windows (PowerShell)
```powershell
# Check Syncthing is running
Get-Process syncthing

# Open Syncthing GUI
Start-Process "http://localhost:8384"

# SSH to VPS (from PowerShell or Git Bash)
ssh -i ~/.ssh/id_ed25519 root@46.224.184.10
```

<!-- section_id: "1a32260d-19cb-4477-9c9a-eeed2c5d2fe1" -->
### VPS
```bash
# Syncthing GUI (external access)
http://46.224.184.10:8384
# User: admin, Pass: SyncthingVPS2026

# Check Syncthing service
systemctl status syncthing@root
```

<!-- section_id: "cb2303b8-a20a-43f5-a754-980fbdc8268e" -->
## Syncthing Device IDs

| Device | ID |
| :--- | :--- |
| Ubuntu | `7UVVQQS-O3463OC-GUTDI63-EWLX3SE-LRX4ZU3-MEOWA34-KSCMF6K-DR7GEAH` |
| Windows/WSL | `IF2WOGZ-RVSVKT3-RCRN3TT-6NDFXQX-KCCCFPW-ABIWRWT-3BFX37C-CDHKTAN` |
| Hetzner VPS | `JTAFCHA-VWKO4GU-W5N6GWM-GHAZC6Y-GCLT4VI-PWAXY45-UBCP3RJ-2ZPJWQR` |

<!-- section_id: "90697796-7c8f-4150-90f5-135fd4932d99" -->
## How It Works

1. **You're on Ubuntu:** Changes sync to VPS automatically via Syncthing
2. **You reboot to Windows:** Windows Syncthing connects to VPS, pulls changes
3. **You make changes on Windows:** Changes sync to VPS
4. **You reboot to Ubuntu:** Ubuntu Syncthing connects to VPS, pulls changes

The VPS is always online and acts as a store-and-forward relay.

<!-- section_id: "0c6e524f-6d5a-47f8-a752-00df08a8059d" -->
## Auto-Start & Real-Time Sync Configuration

All systems are configured for automatic startup and real-time file synchronization:

| Setting | Windows | VPS | Ubuntu |
| :--- | :--- | :--- | :--- |
| **Auto-start on boot** | ✅ Registry Run key | ✅ systemd enabled | ✅ systemd --user |
| **File watcher (real-time)** | ✅ Enabled | ✅ Enabled | ✅ Enabled |
| **Backup rescan interval** | 1 hour | 1 hour | 1 hour |
| **Service auto-restart** | ✅ Configured | ✅ Configured | ✅ Configured |

<!-- section_id: "f1855d69-9528-4269-9fef-3c800a448b46" -->
### How Real-Time Sync Works
- **File watcher** monitors the filesystem for changes and triggers sync within seconds
- **Backup rescan** runs hourly to catch any changes the watcher might miss
- **Auto-restart** ensures Syncthing restarts automatically if it crashes

<!-- section_id: "36ed7399-c539-45f6-abe2-1b44266a45d5" -->
### Windows Auto-Start Location
```
HKCU:\Software\Microsoft\Windows\CurrentVersion\Run\Syncthing
```

<!-- section_id: "4f1200c3-2cf9-412e-9a72-441da9643259" -->
### VPS/Ubuntu Service
```bash
# Check status
systemctl status syncthing@root    # VPS
systemctl --user status syncthing  # Ubuntu
```

<!-- section_id: "17eb0dd7-ba2b-4108-bde4-fb8a3ea283d9" -->
## Verification Test

A test file `SYNC_TEST_UBUNTU_TO_WINDOWS.md` was created on Ubuntu on 2026-01-11. When you boot to Windows, this file should appear in your dawson-workspace folder, confirming the sync is working.

<!-- section_id: "815ca80f-d21a-4652-b825-53c1c2924ce8" -->
## Troubleshooting

<!-- section_id: "243a923d-72df-492d-a805-9d7c8889c2dc" -->
### Syncthing not connecting
1. Check if Syncthing is running (see commands above)
2. Check firewall allows port 22000
3. Open http://localhost:8384 and check device status
4. VPS device (Hetzner-VPS) should show green/connected

<!-- section_id: "4c44322f-acd7-4b17-87cd-f5c33f53a88d" -->
### Files not appearing
1. Wait for sync to complete (check Syncthing GUI for progress)
2. Check folder status - should say "Up to Date"
3. Force rescan if needed: Folder actions → Rescan

<!-- section_id: "5e8b97bd-c252-4aad-a2f0-fbbb324dd419" -->
### SSH connection issues
- Use the correct key: `~/.ssh/id_ed25519`
- VPS IP: 46.224.184.10
- Username: root

<!-- section_id: "9c172243-8b11-4a00-bb0e-381df499c827" -->
## Cost

- **Hetzner VPS:** ~$4.50 USD/month
- **Potential migration:** Oracle Cloud Free Tier (pending approval)

---

**Maintained by:** Claude Code + Dawson
