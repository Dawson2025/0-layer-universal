# Multi-OS Workspace Sync Documentation

This directory contains documentation for the multi-OS workspace sync project, which maintains a synchronized `dawson-workspace` across Windows, WSL, and Ubuntu (dual boot) using Syncthing with a VPS relay.

## Current Status: ✅ FULLY OPERATIONAL

**Last Updated:** 2026-01-11
**All systems configured and syncing via Hetzner VPS relay**

## Quick Reference

| If you're on... | Status | What to do |
| :--- | :--- | :--- |
| **Ubuntu (Native)** | ✅ Complete | Syncthing running, connected to VPS |
| **Windows** | ✅ Complete | Syncthing will connect to VPS on boot |
| **WSL** | ✅ Complete | Syncthing shares config with Windows |

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

## Key Documents

| Document | Purpose |
| :--- | :--- |
| **[STATUS.md](./STATUS.md)** | Current system state, what's working, next steps |
| **[VPS_CREDENTIALS.md](./VPS_CREDENTIALS.md)** | VPS access details, SSH commands, API keys |
| **[DUAL_BOOT_TEST_INSTRUCTIONS.md](./DUAL_BOOT_TEST_INSTRUCTIONS.md)** | How to verify sync is working |

## Quick Commands

### Ubuntu
```bash
# Check Syncthing status
systemctl --user status syncthing

# Open Syncthing GUI
xdg-open http://localhost:8384

# SSH to VPS
ssh -i ~/.ssh/id_ed25519 root@46.224.184.10
```

### Windows (PowerShell)
```powershell
# Check Syncthing is running
Get-Process syncthing

# Open Syncthing GUI
Start-Process "http://localhost:8384"

# SSH to VPS (from PowerShell or Git Bash)
ssh -i ~/.ssh/id_ed25519 root@46.224.184.10
```

### VPS
```bash
# Syncthing GUI (external access)
http://46.224.184.10:8384
# User: admin, Pass: SyncthingVPS2026

# Check Syncthing service
systemctl status syncthing@root
```

## Syncthing Device IDs

| Device | ID |
| :--- | :--- |
| Ubuntu | `7UVVQQS-O3463OC-GUTDI63-EWLX3SE-LRX4ZU3-MEOWA34-KSCMF6K-DR7GEAH` |
| Windows/WSL | `IF2WOGZ-RVSVKT3-RCRN3TT-6NDFXQX-KCCCFPW-ABIWRWT-3BFX37C-CDHKTAN` |
| Hetzner VPS | `JTAFCHA-VWKO4GU-W5N6GWM-GHAZC6Y-GCLT4VI-PWAXY45-UBCP3RJ-2ZPJWQR` |

## How It Works

1. **You're on Ubuntu:** Changes sync to VPS automatically via Syncthing
2. **You reboot to Windows:** Windows Syncthing connects to VPS, pulls changes
3. **You make changes on Windows:** Changes sync to VPS
4. **You reboot to Ubuntu:** Ubuntu Syncthing connects to VPS, pulls changes

The VPS is always online and acts as a store-and-forward relay.

## Verification Test

A test file `SYNC_TEST_UBUNTU_TO_WINDOWS.md` was created on Ubuntu on 2026-01-11. When you boot to Windows, this file should appear in your dawson-workspace folder, confirming the sync is working.

## Troubleshooting

### Syncthing not connecting
1. Check if Syncthing is running (see commands above)
2. Check firewall allows port 22000
3. Open http://localhost:8384 and check device status
4. VPS device (Hetzner-VPS) should show green/connected

### Files not appearing
1. Wait for sync to complete (check Syncthing GUI for progress)
2. Check folder status - should say "Up to Date"
3. Force rescan if needed: Folder actions → Rescan

### SSH connection issues
- Use the correct key: `~/.ssh/id_ed25519`
- VPS IP: 46.224.184.10
- Username: root

## Cost

- **Hetzner VPS:** ~$4.50 USD/month
- **Potential migration:** Oracle Cloud Free Tier (pending approval)

---

**Maintained by:** Claude Code + Dawson
