---
resource_id: "d3385f00-0c2b-4eea-aca1-59422210a6b8"
resource_type: "knowledge"
resource_name: "DEVICE_IDS"
---
# Syncthing Device IDs

This document contains the device IDs for all three systems in the multi-OS workspace sync.

## Device IDs

### WSL (Canonical Origin)
- **Device Name**: WSL-Dawson
- **Device ID**: `IF2WOGZ-RVSVKT3-RCRN3TT-6NDFXQX-KCCCFPW-ABIWRWT-3BFX37C-CDHKTAN`
- **Path**: `/home/dawson/dawson-workspace`
- **Status**: ✅ Active and syncing

### Windows
- **Device Name**: Win-Dawson
- **Device ID**: Check Windows Syncthing web UI (Actions → Show ID) and fill in here: __________________
- **Path**: `C:\Users\Dawson\dawson-workspace`
- **Status**: ✅ Active and syncing

### Ubuntu Desktop
- **Device Name**: Ubuntu-Dawson
- **Device ID**: ______________ (fill this in during Ubuntu setup - step 5.2)
- **Path**: `/home/dawson/dawson-workspace`
- **Status**: ⏳ Pending setup

## How to Find Your Device ID

### From Web UI
1. Open Syncthing web UI: http://localhost:8384
2. Click **Actions** (top right)
3. Click **Show ID**
4. Copy the device ID

### From Command Line
On Linux (WSL or Ubuntu):
```bash
syncthing --device-id
```

## Adding Devices

When setting up a new device, you need to:
1. Get the new device's ID (see above)
2. On each existing device:
   - Open http://localhost:8384
   - Click **Add Remote Device**
   - Paste the new device ID
   - Give it a descriptive name (e.g., `Ubuntu-Dawson`)
   - Click **Save**
3. On the new device:
   - Accept any folder share requests
   - Set folder type to **Send & Receive**

## Connection Status

All devices should show as **Connected** in the Syncthing web UI when they are online and on the same network (or have port 22000 accessible).

---

## SSH Keys

### Windows
- **Key Type**: ed25519
- **Public Key**: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINCwG5FmcXbdNrp+cldX8WLgCwCRc9OEd0xmtRlH60kn dawson-windows-git`
- **Private Key Location**: `~/.ssh/id_ed25519`

### Linux Laptop
- **Key Type**: ed25519
- **Public Key**: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOsafGsGzpQ+h/kQx5DE16EJXj3FwlPdDwE0Gf8LBUSF dawson@github`

### VPS (Hetzner)
- **Key Type**: ed25519
- **Public Key**: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w root@ubuntu-4gb-nbg1-1`

### iPhone (Termius)
- Check Termius app → Keychain → export public key

---

## Tailscale IPs

| Device | Tailscale IP | Notes |
|--------|--------------|-------|
| VPS | 100.93.148.5 | Public IP: 46.224.184.10 |
| Linux Laptop | 100.73.84.89 | |
| iPhone | 100.75.210.27 | Client only |
| Windows | 100.91.229.9 | laptop-gf3b5qv4 |

---
Last updated: 2026-01-21
