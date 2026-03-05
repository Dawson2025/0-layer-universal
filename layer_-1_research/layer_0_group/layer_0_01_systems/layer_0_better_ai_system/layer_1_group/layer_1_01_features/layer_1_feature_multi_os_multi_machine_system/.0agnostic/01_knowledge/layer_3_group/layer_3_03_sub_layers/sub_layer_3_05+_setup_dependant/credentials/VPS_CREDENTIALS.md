---
resource_id: "bfa2b378-20ec-438e-bf3a-3dfd04f22c7c"
resource_type: "knowledge"
resource_name: "VPS_CREDENTIALS"
---
# VPS Credentials and Access Information

**Date:** 2026-01-11
**Server:** Hetzner CX23 VPS

<!-- section_id: "8cacee3f-fbac-4c81-a5d7-13d9a915588b" -->
## Server Details

**Hostname:** ubuntu-4gb-nbg1-1
**IP Address:** 46.224.184.10
**IPv6 Address:** 2a01:4f8:1c1a:885b::1
**Location:** Nuremberg, Germany (eu-central)
**OS:** Ubuntu 24.04 LTS

<!-- section_id: "6bd8df22-a431-4326-9328-60288c778a31" -->
## SSH Access

**Username:** root
**Authentication:** SSH key (ed25519)

**From Windows/WSL:**
- **Key Location:** `~/.ssh/id_ed25519`
- **Public Key:** `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINCwG5FmcXbdNrp+cldX8WLgCwCRc9OEd0xmtRlH60kn dawson-windows-git`

**From Ubuntu (Native):**
- **Key Location:** `~/.ssh/id_ed25519`
- **Public Key:** `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOsafGsGzpQ+h/kQx5DE16EJXj3FwlPdDwE0Gf8LBUSF dawson@github`
- **Status:** ✅ Working (added 2026-01-11)

**Connect:**
```bash
ssh -i ~/.ssh/id_ed25519 root@46.224.184.10
```

<!-- section_id: "fc776ae5-7daf-4d09-a9a6-fc6529c4d45b" -->
## Syncthing Web GUI

**URL:** http://46.224.184.10:8384
**Username:** `admin`
**Password:** `SyncthingVPS2026`

**Note:** GUI authentication is configured. Access from external IPs requires username and password.

<!-- section_id: "b23d4716-adf7-49b1-be3e-a3af72e94869" -->
## Syncthing Configuration

**Device ID:** JTAFCHA-VWKO4GU-W5N6GWM-GHAZC6Y-GCLT4VI-PWAXY45-UBCP3RJ-2ZPJWQR
**API Key:** cQMo4c5GFeRUQXhe7QrQZyFQDxZktW24
**Version:** 1.30.0
**Service:** syncthing@root.service (systemd)
**Config Path:** /root/.local/state/syncthing/config.xml
**Sync Folder:** /root/sync/dawson-workspace

<!-- section_id: "12f27c0a-bef4-4f13-8c61-50c276d91068" -->
## Firewall Ports

**Open Ports:**
- 22/TCP - SSH
- 22000/TCP - Syncthing data transfer
- 21027/UDP - Syncthing local discovery
- 8384/TCP - Syncthing Web GUI

<!-- section_id: "ec7912d0-d5ee-4242-83a7-17cf190e79f3" -->
## Syncthing Service Commands

```bash
# Check status
systemctl status syncthing@root

# View logs
journalctl -u syncthing@root -f

# Restart service
systemctl restart syncthing@root

# Stop service
systemctl stop syncthing@root

# Start service
systemctl start syncthing@root
```

<!-- section_id: "7bd94536-2029-4040-aa81-e8b5f6b79dcc" -->
## Connected Devices

<!-- section_id: "0aeeac53-8889-4111-94d7-2cfad30ae931" -->
### Windows (LAPTOP-GF3B5QV4)
- **Device ID:** IF2WOGZ-RVSVKT3-RCRN3TT-6NDFXQX-KCCCFPW-ABIWRWT-3BFX37C-CDHKTAN
- **Connection:** IPv6, TLS 1.3
- **Shared Folder:** dawson-workspace

<!-- section_id: "9f390dc9-f936-4f7e-bf2a-344d3d88375f" -->
### Ubuntu (Ubuntu-Dawson)
- **Device ID:** 7UVVQQS-O3463OC-GUTDI63-EWLX3SE-LRX4ZU3-MEOWA34-KSCMF6K-DR7GEAH
- **Status:** ✅ Connected via IPv6 TLS 1.3
- **Connection:** tcp-server (2a01:4f8:1c1a:885b::1)
- **Shared Folder:** dawson-workspace (active, syncing)

<!-- section_id: "6e138572-bf58-4bb0-a944-b78ca843af6a" -->
### WSL (WSL-Dawson)
- **Device ID:** PKA5NY2-47573F4-SAHSF6Z-3UXFJCU-AEFHZKL-WKVIHVA-OBF4M2V-5P7AXAE
- **Connection:** Local (Windows host)

<!-- section_id: "85239f48-bf3c-4c51-b21f-cb43e3481049" -->
## Cost

**Monthly:** €4.09 (~$4.50 USD)
- Server (CX23): €3.49/month
- IPv4 Address: €0.60/month

**Annual:** ~$54 USD

<!-- section_id: "39b6ae43-837a-48fe-b290-9fbd09a0f106" -->
## Backup & Migration

**Oracle Cloud Free Tier:** Support ticket pending (48-hour response)
- If approved: Can migrate to $0/month free tier
- Migration: Re-provision on Oracle, reconfigure Syncthing, decommission Hetzner

<!-- section_id: "86d378e5-1033-469a-9b9a-407f7809eaed" -->
## Security Notes

- ✅ SSH key authentication enabled (password-less)
- ✅ Root password changed from default
- ✅ Syncthing GUI authentication configured
- ✅ TLS 1.3 encryption for all Syncthing connections
- ⚠️ ufw firewall rules added but not enabled
- ⚠️ Consider enabling ufw after testing complete

<!-- section_id: "eb46d90b-47d9-48fd-bb71-b9c673e7bda0" -->
## Hetzner Console Access

**URL:** https://console.hetzner.com/projects/13012420/servers
**Email:** dawsonpacker2025@gmail.com

---

**⚠️ IMPORTANT: Keep this file secure. Contains sensitive access credentials.**
