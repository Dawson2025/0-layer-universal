# Status: Multi-OS Workspace Sync

**Last Updated:** 2026-01-11 16:45 MST (from Ubuntu)

## Current System State

| Device | Status | Sync Mode | Connection | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Ubuntu (Native)** | 🟢 **ACTIVE** | Send & Receive | VPS via IPv6 TLS 1.3 | Currently running, sync complete |
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

## What's Working

### Syncthing Three-Way Sync
- **Ubuntu ↔ VPS:** ✅ Connected and syncing
- **Windows ↔ VPS:** ✅ Configured (will connect when Windows boots)
- **Sync Folder:** `dawson-workspace` (~1.5 GB, 50,000+ files)
- **Sync Status:** Complete on Ubuntu side

### SSH Access to VPS
- **From Ubuntu:** ✅ Working (`ssh -i ~/.ssh/id_ed25519 root@46.224.184.10`)
- **From Windows:** ✅ Working (`ssh -i ~/.ssh/id_ed25519 root@46.224.184.10`)

### Test File for Verification
A test file was created on Ubuntu to verify the dual boot sync:
- **File:** `SYNC_TEST_UBUNTU_TO_WINDOWS.md`
- **Location:** Root of dawson-workspace folder
- **Status:** ✅ Synced to VPS, waiting for Windows to pick it up

---

## FOR WINDOWS AGENTS: What To Do When Booted

When the user boots into Windows, the following should happen automatically:

### 1. Verify Syncthing Connection
```powershell
# Check Syncthing is running
Get-Process syncthing

# Or open the Web GUI
Start-Process "http://localhost:8384"
```

In the Syncthing GUI:
- **Hetzner-VPS** should show as connected (green)
- **dawson-workspace** folder should show "Up to Date" after syncing

### 2. Verify Test File Synced
Check if this file exists:
```
C:\Users\<username>\dawson-workspace\SYNC_TEST_UBUNTU_TO_WINDOWS.md
```

If this file exists and is readable, the dual boot sync is working!

### 3. (Optional) Create Reverse Test
To verify Windows → Ubuntu sync:
1. Create a file: `SYNC_TEST_WINDOWS_TO_UBUNTU.md` in dawson-workspace
2. Wait for it to sync to VPS (check Syncthing GUI)
3. When user reboots to Ubuntu, the file should appear

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
- **Syncthing GUI:** http://46.224.184.10:8384 (user: admin, pass: SyncthingVPS2026)
- **SSH:** `ssh -i ~/.ssh/id_ed25519 root@46.224.184.10`
- **Sync Folder on VPS:** `/root/sync/dawson-workspace`

### Syncthing Ports
- 22000/TCP - Data transfer
- 21027/UDP - Local discovery
- 8384/TCP - Web GUI

---

## Recent Log

- **2026-01-11 16:45:** Documentation updated for Windows agent handoff.
- **2026-01-11 16:38:** ✅ Ubuntu SSH key added to VPS. Can now SSH directly from Ubuntu to VPS.
- **2026-01-11 14:11:** ✅ Dual boot test file created and synced to VPS. Ready for Windows verification.
- **2026-01-11 14:03:** ✅ THREE-WAY SYNC OPERATIONAL! Ubuntu ↔ VPS ↔ Windows/WSL all configured.
- **2026-01-11 14:00:** Ubuntu connected to VPS via Syncthing REST API.
- **2026-01-11:** Windows/WSL connected to VPS. Initial sync complete.
- **2026-01-10:** Hetzner VPS created and configured as relay server.

---

## Completed Tasks

1. ✅ Create Hetzner VPS as relay server
2. ✅ Install and configure Syncthing on VPS
3. ✅ Connect Windows/WSL to VPS
4. ✅ Connect Ubuntu to VPS
5. ✅ Configure SSH access from both Ubuntu and Windows
6. ✅ Create test file for dual boot verification
7. ✅ Update documentation for agent handoff

## Pending Tasks

1. ⏳ **Verify Windows sync** - User needs to boot to Windows and confirm test file appears
2. ⏳ **Create Windows → Ubuntu test** - Optional reverse test
3. ⏳ **Monitor Oracle Cloud ticket** - May migrate to free tier if approved

---

## Troubleshooting

### Syncthing not connecting on Windows
1. Check if Syncthing service is running: `Get-Process syncthing`
2. Check Windows Firewall allows port 22000
3. Open GUI at http://localhost:8384 and check device status

### Files not syncing
1. Check folder status in Syncthing GUI
2. Look for "Out of Sync" items
3. Check `.stignore` file for excluded patterns
4. Force rescan: Folder actions → Rescan

### SSH connection issues
- Ensure using correct key: `~/.ssh/id_ed25519`
- VPS IP: 46.224.184.10
- Username: root

---

## Related Documentation

- [VPS_CREDENTIALS.md](./VPS_CREDENTIALS.md) - Full VPS access details
- [DUAL_BOOT_TEST_INSTRUCTIONS.md](./DUAL_BOOT_TEST_INSTRUCTIONS.md) - Testing procedure
- [README.md](./README.md) - Project overview
