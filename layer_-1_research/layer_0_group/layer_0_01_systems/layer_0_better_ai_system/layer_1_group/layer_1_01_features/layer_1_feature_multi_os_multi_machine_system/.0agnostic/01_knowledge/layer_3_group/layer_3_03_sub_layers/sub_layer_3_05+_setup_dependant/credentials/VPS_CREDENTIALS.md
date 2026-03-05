---
resource_id: "bfa2b378-20ec-438e-bf3a-3dfd04f22c7c"
resource_type: "knowledge"
resource_name: "VPS_CREDENTIALS"
---
# VPS Credentials and Access Information

**Date:** 2026-01-11
**Server:** Hetzner CX23 VPS

## Server Details

**Hostname:** ubuntu-4gb-nbg1-1
**IP Address:** 46.224.184.10
**IPv6 Address:** 2a01:4f8:1c1a:885b::1
**Location:** Nuremberg, Germany (eu-central)
**OS:** Ubuntu 24.04 LTS

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

## Syncthing Web GUI

**URL:** http://46.224.184.10:8384
**Username:** `admin`
**Password:** `SyncthingVPS2026`

**Note:** GUI authentication is configured. Access from external IPs requires username and password.

## Syncthing Configuration

**Device ID:** JTAFCHA-VWKO4GU-W5N6GWM-GHAZC6Y-GCLT4VI-PWAXY45-UBCP3RJ-2ZPJWQR
**API Key:** cQMo4c5GFeRUQXhe7QrQZyFQDxZktW24
**Version:** 1.30.0
**Service:** syncthing@root.service (systemd)
**Config Path:** /root/.local/state/syncthing/config.xml
**Sync Folder:** /root/sync/dawson-workspace

## Firewall Ports

**Open Ports:**
- 22/TCP - SSH
- 22000/TCP - Syncthing data transfer
- 21027/UDP - Syncthing local discovery
- 8384/TCP - Syncthing Web GUI

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

## Connected Devices

### Windows (LAPTOP-GF3B5QV4)
- **Device ID:** IF2WOGZ-RVSVKT3-RCRN3TT-6NDFXQX-KCCCFPW-ABIWRWT-3BFX37C-CDHKTAN
- **Connection:** IPv6, TLS 1.3
- **Shared Folder:** dawson-workspace

### Ubuntu (Ubuntu-Dawson)
- **Device ID:** 7UVVQQS-O3463OC-GUTDI63-EWLX3SE-LRX4ZU3-MEOWA34-KSCMF6K-DR7GEAH
- **Status:** ✅ Connected via IPv6 TLS 1.3
- **Connection:** tcp-server (2a01:4f8:1c1a:885b::1)
- **Shared Folder:** dawson-workspace (active, syncing)

### WSL (WSL-Dawson)
- **Device ID:** PKA5NY2-47573F4-SAHSF6Z-3UXFJCU-AEFHZKL-WKVIHVA-OBF4M2V-5P7AXAE
- **Connection:** Local (Windows host)

## Cost

**Monthly:** €4.09 (~$4.50 USD)
- Server (CX23): €3.49/month
- IPv4 Address: €0.60/month

**Annual:** ~$54 USD

## Backup & Migration

**Oracle Cloud Free Tier:** Support ticket pending (48-hour response)
- If approved: Can migrate to $0/month free tier
- Migration: Re-provision on Oracle, reconfigure Syncthing, decommission Hetzner

## Security Notes

- ✅ SSH key authentication enabled (password-less)
- ✅ Root password changed from default
- ✅ Syncthing GUI authentication configured
- ✅ TLS 1.3 encryption for all Syncthing connections
- ⚠️ ufw firewall rules added but not enabled
- ⚠️ Consider enabling ufw after testing complete

## Hetzner Console Access

**URL:** https://console.hetzner.com/projects/13012420/servers
**Email:** dawsonpacker2025@gmail.com

---

**⚠️ IMPORTANT: Keep this file secure. Contains sensitive access credentials.**
