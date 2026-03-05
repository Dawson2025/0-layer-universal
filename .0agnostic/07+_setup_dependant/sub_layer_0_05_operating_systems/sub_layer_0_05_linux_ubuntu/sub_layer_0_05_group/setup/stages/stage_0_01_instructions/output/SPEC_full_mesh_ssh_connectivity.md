---
resource_id: "fa5a9074-d42e-4e76-9043-f46c4aa7d2fb"
resource_type: "document"
resource_name: "SPEC_full_mesh_ssh_connectivity"
---
# Spec: Full Mesh SSH Connectivity

**Layer**: 0 (Universal)
**Stage**: 0.01 Instructions
**Created**: 2026-01-17

---

<!-- section_id: "9805669e-f786-4f11-878d-b8afb5ca497b" -->
## Overview

Full bidirectional SSH connectivity between all devices using Termius as the unified client.

---

<!-- section_id: "444d1441-5f0b-4648-9d8f-66b5cff77199" -->
## Device Capabilities

| Device | OS | SSH Client | SSH Server | Termius |
|--------|-----|------------|------------|---------|
| VPS | Ubuntu 24.04 | ✅ Built-in | ✅ Built-in | N/A (CLI only) |
| Windows | Windows 11 | ✅ Termius | ✅ OpenSSH Server (install) | ✅ Desktop app |
| Linux | Ubuntu | ✅ Termius | ✅ Built-in | ✅ Snap/Flatpak |
| iPhone | iOS | ✅ Termius | ❌ Not possible | ✅ App Store |

---

<!-- section_id: "7a3c68d2-525b-4c1c-98d4-fa93d6422455" -->
## Connection Matrix

| From \ To | VPS | Windows | Linux | iPhone |
|-----------|-----|---------|-------|--------|
| **VPS** | - | ✅ | ✅ | ❌ |
| **Windows** | ✅ | - | ✅ | ❌ |
| **Linux** | ✅ | ✅ | - | ❌ |
| **iPhone** | ✅ | ✅ | ✅ | - |

**Total connections**: 9 possible out of 12 (iPhone can't accept incoming)

---

<!-- section_id: "b56e8551-bda1-446d-90bb-84365f383412" -->
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

<!-- section_id: "104a9938-e130-43bc-beee-9a98c1296c04" -->
## Technical Requirements

<!-- section_id: "0e666b2a-bb4c-4408-ac03-69535fb0b1c8" -->
### VPS (46.224.184.10)
- SSH server: ✅ Running (port 22)
- User: root
- Auth: SSH key (Ed25519)
- Firewall: Allow SSH

<!-- section_id: "4165bcbc-b744-4eb5-8b91-dfffd28573d2" -->
### Windows
- SSH server: **Must install** OpenSSH Server
- User: dawson
- Auth: SSH key
- Firewall: Allow port 22
- IP: Local network (192.168.x.x or similar)

<!-- section_id: "8b7b8894-e462-4bac-9b90-59fea3f9e28b" -->
### Linux
- SSH server: ✅ Built-in (openssh-server)
- User: dawson
- Auth: SSH key
- IP: Local network (192.168.x.x or similar)

<!-- section_id: "95715d85-1ce5-4fe9-a02e-6751e51176bf" -->
### iPhone
- Termius app from App Store
- SSH keys imported or synced via account
- Can only initiate connections (no server)

---

<!-- section_id: "742b925b-78b1-4c2e-92f9-35a966943d6e" -->
## SSH Key Distribution

**Primary key**: `~/.ssh/id_ed25519` (Ed25519)

| Machine | Has Private Key | Public Key Locations |
|---------|----------------|---------------------|
| Windows | ✅ | VPS authorized_keys, Linux authorized_keys |
| Linux | ✅ (copy from Windows) | VPS authorized_keys, Windows authorized_keys |
| VPS | ✅ (generated) | Linux authorized_keys, Windows authorized_keys |
| iPhone | ✅ (import via Termius) | N/A (client only) |

---

<!-- section_id: "407afe19-f08d-4f95-b95e-86e33a445d37" -->
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

<!-- section_id: "72374d48-2d02-4f76-9b3c-c1fc4e0d21e0" -->
## Termius Configuration

<!-- section_id: "627be7e9-fe1e-43e7-89d8-7e9b30966135" -->
### Account Sync
- All devices use same Termius account
- Hosts automatically sync
- Keys stored in encrypted vault

<!-- section_id: "391fa336-e876-41bc-87e3-389e97f77744" -->
### Hosts to Create
| Host | Address | Port | User | Key |
|------|---------|------|------|-----|
| VPS | 46.224.184.10 | 22 | root | id_ed25519 |
| Linux | TBD | 22 | dawson | id_ed25519 |
| Windows | TBD | 22 | dawson | id_ed25519 |

---

<!-- section_id: "6c5dad46-021d-4c28-b8d2-631624cc7e11" -->
## Windows OpenSSH Server Spec

<!-- section_id: "295b90c2-9a78-41fb-b886-0a10bd9c1397" -->
### Installation
```powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

<!-- section_id: "0a5324ee-f0e4-4394-a997-5f404aaeaf0a" -->
### Configuration
- Service: sshd
- Port: 22
- Auth: Public key
- Shell: PowerShell or cmd

<!-- section_id: "adfa8bc5-d3cd-4c20-bf2e-57e7b2931d52" -->
### Firewall Rule
```powershell
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

---

<!-- section_id: "78030da8-eea5-41f8-85ae-fac6c84c1ddf" -->
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

<!-- section_id: "19735e4a-3693-40c0-8783-479f1b002417" -->
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
