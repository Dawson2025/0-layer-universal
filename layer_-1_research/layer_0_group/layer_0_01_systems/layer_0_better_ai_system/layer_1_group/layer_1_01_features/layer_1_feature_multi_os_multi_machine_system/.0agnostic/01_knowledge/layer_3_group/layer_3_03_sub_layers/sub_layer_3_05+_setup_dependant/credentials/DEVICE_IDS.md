---
resource_id: "d3385f00-0c2b-4eea-aca1-59422210a6b8"
resource_type: "knowledge"
resource_name: "DEVICE_IDS"
---
# Syncthing Device IDs

This document contains the device IDs for all three systems in the multi-OS workspace sync.

<!-- section_id: "a31ae92b-fc73-4772-ba43-961ada9577c7" -->
## Device IDs

<!-- section_id: "d988ea8f-0d23-4b60-8ac8-6b2b83205aaa" -->
### WSL (Canonical Origin)
- **Device Name**: WSL-Dawson
- **Device ID**: `IF2WOGZ-RVSVKT3-RCRN3TT-6NDFXQX-KCCCFPW-ABIWRWT-3BFX37C-CDHKTAN`
- **Path**: `/home/dawson/dawson-workspace`
- **Status**: ✅ Active and syncing

<!-- section_id: "de25d928-77b8-4947-8d15-e32a8dbbbfc8" -->
### Windows
- **Device Name**: Win-Dawson
- **Device ID**: Check Windows Syncthing web UI (Actions → Show ID) and fill in here: __________________
- **Path**: `C:\Users\Dawson\dawson-workspace`
- **Status**: ✅ Active and syncing

<!-- section_id: "1de869b0-2f69-419a-89ae-58f0841a04cd" -->
### Ubuntu Desktop
- **Device Name**: Ubuntu-Dawson
- **Device ID**: ______________ (fill this in during Ubuntu setup - step 5.2)
- **Path**: `/home/dawson/dawson-workspace`
- **Status**: ⏳ Pending setup

<!-- section_id: "f68a4d87-5359-46b1-b36e-f45c21b2ab99" -->
## How to Find Your Device ID

<!-- section_id: "94391394-1c56-4bd0-9568-6f4df0e178ca" -->
### From Web UI
1. Open Syncthing web UI: http://localhost:8384
2. Click **Actions** (top right)
3. Click **Show ID**
4. Copy the device ID

<!-- section_id: "ab0888f2-8820-4dec-ab09-5dac01c03bc5" -->
### From Command Line
On Linux (WSL or Ubuntu):
```bash
syncthing --device-id
```

<!-- section_id: "cba3576b-ab48-4417-a576-063927a267d0" -->
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

<!-- section_id: "cf6c44cb-1972-4553-830d-45668da2fe57" -->
## Connection Status

All devices should show as **Connected** in the Syncthing web UI when they are online and on the same network (or have port 22000 accessible).

---

<!-- section_id: "cc406205-7120-4461-8395-a513e5883aca" -->
## SSH Keys

<!-- section_id: "7ad04ed2-a065-41aa-8969-84863dabfe65" -->
### Windows
- **Key Type**: ed25519
- **Public Key**: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINCwG5FmcXbdNrp+cldX8WLgCwCRc9OEd0xmtRlH60kn dawson-windows-git`
- **Private Key Location**: `~/.ssh/id_ed25519`

<!-- section_id: "8ad404a3-c202-4e3f-ac55-0aef3658e3a6" -->
### Linux Laptop
- **Key Type**: ed25519
- **Public Key**: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOsafGsGzpQ+h/kQx5DE16EJXj3FwlPdDwE0Gf8LBUSF dawson@github`

<!-- section_id: "d50515ed-e9be-47b6-9f89-19065be635a8" -->
### VPS (Hetzner)
- **Key Type**: ed25519
- **Public Key**: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w root@ubuntu-4gb-nbg1-1`

<!-- section_id: "22cb99b5-2800-44d5-b392-e499a88b9f95" -->
### iPhone (Termius)
- Check Termius app → Keychain → export public key

---

<!-- section_id: "e2ccac96-bab1-4ecf-badc-6c27895ea8f9" -->
## Tailscale IPs

| Device | Tailscale IP | Notes |
|--------|--------------|-------|
| VPS | 100.93.148.5 | Public IP: 46.224.184.10 |
| Linux Laptop | 100.73.84.89 | |
| iPhone | 100.75.210.27 | Client only |
| Windows | 100.91.229.9 | laptop-gf3b5qv4 |

---
Last updated: 2026-01-21
