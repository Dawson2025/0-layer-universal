---
resource_id: "0426c24c-d1ef-4d04-bdd5-052aefe7aded"
resource_type: "knowledge"
resource_name: "TERMIUS_SSH_ARCHITECTURE"
---
# Termius SSH Architecture

**Created**: 2026-01-21
**Status**: In Progress

---

<!-- section_id: "0a1955a1-f4fe-493c-92a3-1343ec654b77" -->
## Overview

SSH key-based authentication setup across all devices using Termius, with both direct IP and Tailscale connectivity options.

---

<!-- section_id: "fdcdd08c-e233-468f-a6d2-8a97c37dda70" -->
## Devices & Keys

Each device has its own SSH key:

| Device | Key Name | Key Type | Status |
|--------|----------|----------|--------|
| Windows Laptop | laptop-windows-key | ED25519 | ✅ In Termius |
| Linux Laptop | laptop-linux-key | ED25519 | ❌ Pending (laptop offline) |
| iPhone | iphone-key | RSA | ✅ In Termius |
| VPS | vps-key | ED25519 | ✅ In Termius |

---

<!-- section_id: "3829036c-6c4f-4600-ba36-0610679a6dc7" -->
## IP Addresses

| Device | Direct IP | Tailscale IP |
|--------|-----------|--------------|
| VPS | 46.224.184.10 | 100.93.148.5 |
| Windows Laptop | N/A (no public IP) | 100.91.229.9 |
| Linux Laptop | N/A (no public IP) | 100.73.84.89 |
| iPhone | N/A | 100.75.210.27 |

---

<!-- section_id: "ad5d373f-0fe4-40cb-b19d-47346f52008c" -->
## Group Architecture

<!-- section_id: "5d33159c-6458-404d-bd67-0c3f7e292c9c" -->
### Direct Connection Groups
For connections over public internet (only VPS has public IP):

| Group | Key Used | Hosts |
|-------|----------|-------|
| for_laptop_windows | laptop-windows-key | vps (46.224.184.10) |
| for_laptop_linux | laptop-linux-key | vps (46.224.184.10) |
| for_iphone | iphone-key | vps (46.224.184.10) |
| for_vps | vps-key | *(empty - laptops have no public IP)* |

<!-- section_id: "44566c14-0d99-4c1e-9180-1bfaa528a959" -->
### Tailscale Groups
For connections over Tailscale mesh network:

| Group | Key Used | Hosts |
|-------|----------|-------|
| tailscale_for_laptop_windows | laptop-windows-key | vps (100.93.148.5), laptop-linux (100.73.84.89) |
| tailscale_for_laptop_linux | laptop-linux-key | vps (100.93.148.5), laptop-windows (100.91.229.9) |
| tailscale_for_iphone | iphone-key | vps (100.93.148.5), laptop-linux (100.73.84.89), laptop-windows (100.91.229.9) |
| tailscale_for_vps | vps-key | laptop-linux (100.73.84.89), laptop-windows (100.91.229.9) |

---

<!-- section_id: "9f10126c-00a2-4d9c-9c2d-5ad123e1015a" -->
## Connection Diagram

```
                         DIRECT IP
                    ┌─────────────────┐
                    │      VPS        │
                    │  46.224.184.10  │
                    │  100.93.148.5   │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
   ┌───────────┐       ┌───────────┐       ┌───────────┐
   │  laptop   │◄─────►│  laptop   │       │  iPhone   │
   │  windows  │       │  linux    │       │           │
   │100.91.229.9│      │100.73.84.89│      │100.75.210.27│
   └───────────┘       └───────────┘       └───────────┘
         ▲                   ▲                   │
         │                   │                   │
         └───────────────────┴───────────────────┘
                    TAILSCALE MESH
              (all can reach all via Tailscale)
```

---

<!-- section_id: "8730f882-10f0-48df-8499-036ed8252271" -->
## Detailed Host Configuration

<!-- section_id: "a7f4597b-e351-48a0-923f-eefdb9629a3f" -->
### Group: for_laptop_windows
*Hosts that Windows laptop connects to via direct IP*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 46.224.184.10 | 22 | dawson | laptop-windows-key |

<!-- section_id: "b25d15a8-1a33-43cd-b30f-4bdb42d2187c" -->
### Group: tailscale_for_laptop_windows
*Hosts that Windows laptop connects to via Tailscale*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 100.93.148.5 | 22 | dawson | laptop-windows-key |
| laptop-linux | 100.73.84.89 | 22 | dawson | laptop-windows-key |

<!-- section_id: "d3c5289f-61fb-41ae-a5ff-15233f3f463a" -->
### Group: for_laptop_linux
*Hosts that Linux laptop connects to via direct IP*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 46.224.184.10 | 22 | dawson | laptop-linux-key |

<!-- section_id: "78c7d877-5a12-445f-a5fc-1a9477cfe506" -->
### Group: tailscale_for_laptop_linux
*Hosts that Linux laptop connects to via Tailscale*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 100.93.148.5 | 22 | dawson | laptop-linux-key |
| laptop-windows | 100.91.229.9 | 22 | dawson | laptop-linux-key |

<!-- section_id: "d11c6021-6d81-49b2-a4b1-9a5c5d114cdd" -->
### Group: for_iphone
*Hosts that iPhone connects to via direct IP*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 46.224.184.10 | 22 | dawson | iphone-key |

<!-- section_id: "b380c115-1f0b-46b3-92aa-6ab2c2fd5193" -->
### Group: tailscale_for_iphone
*Hosts that iPhone connects to via Tailscale*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 100.93.148.5 | 22 | dawson | iphone-key |
| laptop-linux | 100.73.84.89 | 22 | dawson | iphone-key |
| laptop-windows | 100.91.229.9 | 22 | dawson | iphone-key |

<!-- section_id: "0d4d6c22-3928-4869-9919-72cfc2e4c17e" -->
### Group: for_vps
*Hosts that VPS connects to (Tailscale only - no direct IP possible)*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| laptop-linux | 100.73.84.89 | 22 | dawson | vps-key |
| laptop-windows | 100.91.229.9 | 22 | dawson | vps-key |

<!-- section_id: "ec8fc12e-fe08-46e5-9e44-3e494e2649ec" -->
### Group: tailscale_for_vps
*Same as for_vps (VPS can only reach laptops via Tailscale)*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| laptop-linux | 100.73.84.89 | 22 | dawson | vps-key |
| laptop-windows | 100.91.229.9 | 22 | dawson | vps-key |

---

<!-- section_id: "db2efdcd-79c3-40bd-9509-044c9813329f" -->
## authorized_keys Configuration

<!-- section_id: "c49f033c-799c-49d5-a4ed-d2ea8778c302" -->
### VPS (/home/dawson/.ssh/authorized_keys)
```
# Windows laptop key
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINCwG5FmcXbdNrp+cldX8WLgCwCRc9OEd0xmtRlH60kn laptop-windows-key

# Linux laptop key (add when available)
# ssh-ed25519 AAAA... laptop-linux-key

# iPhone keys
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPZEOa5zt0Xt1EaMQVfRp1Mn+2SQ0fuV+embyGwVHIl+ iPhone-Termius
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKKWgc07svKyAFNl1HsXJIYbeWJDiCxyWPh2Mu1Izw2a iPhone-Termius
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ... iPhone-Termius
```

<!-- section_id: "2561bfc2-b570-4093-a74c-92631883697f" -->
### Windows Laptop (~/.ssh/authorized_keys)
```
# VPS key
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w vps-key

# Linux laptop key (add when available)
# ssh-ed25519 AAAA... laptop-linux-key

# iPhone keys
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPZEOa5zt0Xt1EaMQVfRp1Mn+2SQ0fuV+embyGwVHIl+ iPhone-Termius
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKKWgc07svKyAFNl1HsXJIYbeWJDiCxyWPh2Mu1Izw2a iPhone-Termius
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ... iPhone-Termius
```

<!-- section_id: "84a64a92-5051-4455-b3e8-0d4f9d7bcdd8" -->
### Linux Laptop (~/.ssh/authorized_keys)
```
# VPS key
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w vps-key

# Windows laptop key
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINCwG5FmcXbdNrp+cldX8WLgCwCRc9OEd0xmtRlH60kn laptop-windows-key

# iPhone keys
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPZEOa5zt0Xt1EaMQVfRp1Mn+2SQ0fuV+embyGwVHIl+ iPhone-Termius
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKKWgc07svKyAFNl1HsXJIYbeWJDiCxyWPh2Mu1Izw2a iPhone-Termius
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ... iPhone-Termius
```

---

<!-- section_id: "3ab57318-d0e8-4f68-bfb9-d2442c742c9a" -->
## Setup Status

<!-- section_id: "1023de38-60db-4b95-8e9e-0194a15f5a85" -->
### Termius Keychain
- [x] laptop-windows-key (ED25519)
- [x] iphone-key (RSA)
- [x] vps-key (ED25519)
- [ ] laptop-linux-key (ED25519) - *pending: laptop offline*

<!-- section_id: "dafd57f6-b286-49c7-804c-0bdd5a4fbf5e" -->
### authorized_keys Files
- [x] VPS /home/dawson/.ssh/authorized_keys - has windows + iphone keys
- [x] Windows ~/.ssh/authorized_keys - has vps + iphone keys
- [ ] Linux ~/.ssh/authorized_keys - *pending: laptop offline*

<!-- section_id: "e5c9cc5a-1bf4-4937-9436-337ee5fca550" -->
### Termius Groups & Hosts
- [ ] for_laptop_windows
- [ ] tailscale_for_laptop_windows
- [ ] for_laptop_linux
- [ ] tailscale_for_laptop_linux
- [ ] for_iphone
- [ ] tailscale_for_iphone
- [ ] for_vps / tailscale_for_vps

---

<!-- section_id: "e105beec-b0f6-4427-bd55-ade68d5804c6" -->
## Pending Tasks

1. **Get laptop-linux-key** - Need to boot Linux laptop and retrieve `~/.ssh/id_ed25519`
2. **Add laptop-linux-key to Termius** - Import to Keychain
3. **Set up Linux authorized_keys** - Add vps, windows, iphone keys
4. **Create all Termius groups and hosts** - Manual setup in Termius
5. **Test all connections** - Verify SSH works in both directions

---

<!-- section_id: "449e62f3-18c8-458d-9938-c6bcea815a7e" -->
## Related Files

- `DEVICE_IDS.md` - Device identifiers and IPs
- `VPS_CREDENTIALS.md` - VPS connection details
- `STATUS.md` - Overall multi-OS status
