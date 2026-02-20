# Spec: Full Mesh SSH Connectivity

**Layer**: 0 (Universal)
**Stage**: 0.01 Instructions
**Created**: 2026-01-17

---

## Overview

Full bidirectional SSH connectivity between all devices using Termius as the unified client.

---

## Device Capabilities

| Device | OS | SSH Client | SSH Server | Termius |
|--------|-----|------------|------------|---------|
| VPS | Ubuntu 24.04 | ✅ Built-in | ✅ Built-in | N/A (CLI only) |
| Windows | Windows 11 | ✅ Termius | ✅ OpenSSH Server (install) | ✅ Desktop app |
| Linux | Ubuntu | ✅ Termius | ✅ Built-in | ✅ Snap/Flatpak |
| iPhone | iOS | ✅ Termius | ❌ Not possible | ✅ App Store |

---

## Connection Matrix

| From \ To | VPS | Windows | Linux | iPhone |
|-----------|-----|---------|-------|--------|
| **VPS** | - | ✅ | ✅ | ❌ |
| **Windows** | ✅ | - | ✅ | ❌ |
| **Linux** | ✅ | ✅ | - | ❌ |
| **iPhone** | ✅ | ✅ | ✅ | - |

**Total connections**: 9 possible out of 12 (iPhone can't accept incoming)

---

## Network Topology

```
        CLOUD                    LOCAL NETWORK
    ┌───────────┐            ┌─────────────────────┐
    │    VPS    │            │  Windows ◄──► Linux │
    │ 46.224.   │◄──────────►│                     │
    │ 184.10    │            │         ▲           │
    └─────┬─────┘            └─────────┼───────────┘
          │                            │
          │         ┌──────────────────┘
          │         │
          ▼         ▼
    ┌───────────────────┐
    │      iPhone       │
    │   (client only)   │
    └───────────────────┘
```

---

## Technical Requirements

### VPS (46.224.184.10)
- SSH server: ✅ Running (port 22)
- User: root
- Auth: SSH key (Ed25519)
- Firewall: Allow SSH

### Windows
- SSH server: **Must install** OpenSSH Server
- User: dawson
- Auth: SSH key
- Firewall: Allow port 22
- IP: Local network (192.168.x.x or similar)

### Linux
- SSH server: ✅ Built-in (openssh-server)
- User: dawson
- Auth: SSH key
- IP: Local network (192.168.x.x or similar)

### iPhone
- Termius app from App Store
- SSH keys imported or synced via account
- Can only initiate connections (no server)

---

## SSH Key Distribution

**Primary key**: `~/.ssh/id_ed25519` (Ed25519)

| Machine | Has Private Key | Public Key Locations |
|---------|----------------|---------------------|
| Windows | ✅ | VPS authorized_keys, Linux authorized_keys |
| Linux | ✅ (copy from Windows) | VPS authorized_keys, Windows authorized_keys |
| VPS | ✅ (generated) | Linux authorized_keys, Windows authorized_keys |
| iPhone | ✅ (import via Termius) | N/A (client only) |

---

## SSH Config Specification

All machines should have this config in `~/.ssh/config`:

```
Host vps
    HostName 46.224.184.10
    User root
    IdentityFile ~/.ssh/id_ed25519

Host linux
    HostName <LINUX_LOCAL_IP>
    User dawson
    IdentityFile ~/.ssh/id_ed25519

Host windows
    HostName <WINDOWS_LOCAL_IP>
    User dawson
    IdentityFile ~/.ssh/id_ed25519
```

---

## Termius Configuration

### Account Sync
- All devices use same Termius account
- Hosts automatically sync
- Keys stored in encrypted vault

### Hosts to Create
| Host | Address | Port | User | Key |
|------|---------|------|------|-----|
| VPS | 46.224.184.10 | 22 | root | id_ed25519 |
| Linux | TBD | 22 | dawson | id_ed25519 |
| Windows | TBD | 22 | dawson | id_ed25519 |

---

## Windows OpenSSH Server Spec

### Installation
```powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

### Configuration
- Service: sshd
- Port: 22
- Auth: Public key
- Shell: PowerShell or cmd

### Firewall Rule
```powershell
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

---

## Verification Tests

After setup, verify each connection:

```bash
# From VPS
ssh dawson@<LINUX_IP>     # Should work
ssh dawson@<WINDOWS_IP>   # Should work (after OpenSSH)

# From Windows
ssh vps                   # Should work (already done)
ssh linux                 # Should work (after IP set)

# From Linux
ssh vps                   # Should work
ssh windows               # Should work (after OpenSSH)

# From iPhone (via Termius)
# Tap each host - should connect
```

---

## Dependencies

```
Phase A (done): Windows → VPS
    │
    ├── Phase B: Fix Linux login loop
    │       │
    │       └── Get Linux IP
    │           │
    │           ├── VPS → Linux
    │           ├── Windows → Linux
    │           ├── iPhone → Linux
    │           └── Linux → VPS
    │
    └── Phase C: Enable Windows SSH
            │
            ├── VPS → Windows
            ├── Linux → Windows
            └── iPhone → Windows
```
