---
resource_id: "0426c24c-d1ef-4d04-bdd5-052aefe7aded"
resource_type: "knowledge"
resource_name: "TERMIUS_SSH_ARCHITECTURE"
---
# Termius SSH Architecture

**Created**: 2026-01-21
**Status**: In Progress

---

## Overview

SSH key-based authentication setup across all devices using Termius, with both direct IP and Tailscale connectivity options.

---

## Devices & Keys

Each device has its own SSH key:

| Device | Key Name | Key Type | Status |
|--------|----------|----------|--------|
| Windows Laptop | laptop-windows-key | ED25519 | ✅ In Termius |
| Linux Laptop | laptop-linux-key | ED25519 | ❌ Pending (laptop offline) |
| iPhone | iphone-key | RSA | ✅ In Termius |
| VPS | vps-key | ED25519 | ✅ In Termius |

---

## IP Addresses

| Device | Direct IP | Tailscale IP |
|--------|-----------|--------------|
| VPS | 46.224.184.10 | 100.93.148.5 |
| Windows Laptop | N/A (no public IP) | 100.91.229.9 |
| Linux Laptop | N/A (no public IP) | 100.73.84.89 |
| iPhone | N/A | 100.75.210.27 |

---

## Group Architecture

### Direct Connection Groups
For connections over public internet (only VPS has public IP):

| Group | Key Used | Hosts |
|-------|----------|-------|
| for_laptop_windows | laptop-windows-key | vps (46.224.184.10) |
| for_laptop_linux | laptop-linux-key | vps (46.224.184.10) |
| for_iphone | iphone-key | vps (46.224.184.10) |
| for_vps | vps-key | *(empty - laptops have no public IP)* |

### Tailscale Groups
For connections over Tailscale mesh network:

| Group | Key Used | Hosts |
|-------|----------|-------|
| tailscale_for_laptop_windows | laptop-windows-key | vps (100.93.148.5), laptop-linux (100.73.84.89) |
| tailscale_for_laptop_linux | laptop-linux-key | vps (100.93.148.5), laptop-windows (100.91.229.9) |
| tailscale_for_iphone | iphone-key | vps (100.93.148.5), laptop-linux (100.73.84.89), laptop-windows (100.91.229.9) |
| tailscale_for_vps | vps-key | laptop-linux (100.73.84.89), laptop-windows (100.91.229.9) |

---

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

## Detailed Host Configuration

### Group: for_laptop_windows
*Hosts that Windows laptop connects to via direct IP*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 46.224.184.10 | 22 | dawson | laptop-windows-key |

### Group: tailscale_for_laptop_windows
*Hosts that Windows laptop connects to via Tailscale*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 100.93.148.5 | 22 | dawson | laptop-windows-key |
| laptop-linux | 100.73.84.89 | 22 | dawson | laptop-windows-key |

### Group: for_laptop_linux
*Hosts that Linux laptop connects to via direct IP*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 46.224.184.10 | 22 | dawson | laptop-linux-key |

### Group: tailscale_for_laptop_linux
*Hosts that Linux laptop connects to via Tailscale*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 100.93.148.5 | 22 | dawson | laptop-linux-key |
| laptop-windows | 100.91.229.9 | 22 | dawson | laptop-linux-key |

### Group: for_iphone
*Hosts that iPhone connects to via direct IP*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 46.224.184.10 | 22 | dawson | iphone-key |

### Group: tailscale_for_iphone
*Hosts that iPhone connects to via Tailscale*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| vps | 100.93.148.5 | 22 | dawson | iphone-key |
| laptop-linux | 100.73.84.89 | 22 | dawson | iphone-key |
| laptop-windows | 100.91.229.9 | 22 | dawson | iphone-key |

### Group: for_vps
*Hosts that VPS connects to (Tailscale only - no direct IP possible)*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| laptop-linux | 100.73.84.89 | 22 | dawson | vps-key |
| laptop-windows | 100.91.229.9 | 22 | dawson | vps-key |

### Group: tailscale_for_vps
*Same as for_vps (VPS can only reach laptops via Tailscale)*

| Host Label | Address | Port | User | Key |
|------------|---------|------|------|-----|
| laptop-linux | 100.73.84.89 | 22 | dawson | vps-key |
| laptop-windows | 100.91.229.9 | 22 | dawson | vps-key |

---

## authorized_keys Configuration

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

## Setup Status

### Termius Keychain
- [x] laptop-windows-key (ED25519)
- [x] iphone-key (RSA)
- [x] vps-key (ED25519)
- [ ] laptop-linux-key (ED25519) - *pending: laptop offline*

### authorized_keys Files
- [x] VPS /home/dawson/.ssh/authorized_keys - has windows + iphone keys
- [x] Windows ~/.ssh/authorized_keys - has vps + iphone keys
- [ ] Linux ~/.ssh/authorized_keys - *pending: laptop offline*

### Termius Groups & Hosts
- [ ] for_laptop_windows
- [ ] tailscale_for_laptop_windows
- [ ] for_laptop_linux
- [ ] tailscale_for_laptop_linux
- [ ] for_iphone
- [ ] tailscale_for_iphone
- [ ] for_vps / tailscale_for_vps

---

## Pending Tasks

1. **Get laptop-linux-key** - Need to boot Linux laptop and retrieve `~/.ssh/id_ed25519`
2. **Add laptop-linux-key to Termius** - Import to Keychain
3. **Set up Linux authorized_keys** - Add vps, windows, iphone keys
4. **Create all Termius groups and hosts** - Manual setup in Termius
5. **Test all connections** - Verify SSH works in both directions

---

## Related Files

- `DEVICE_IDS.md` - Device identifiers and IPs
- `VPS_CREDENTIALS.md` - VPS connection details
- `STATUS.md` - Overall multi-OS status
