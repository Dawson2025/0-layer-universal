---
resource_id: "537f85cb-1c8b-452a-84e2-f0bc8181f4d7"
resource_type: "document"
resource_name: "FULL_MESH_SSH_PLAN"
---
# Full Mesh SSH Connectivity Plan

**Goal**: Connect ALL devices to ALL other devices (where technically possible) using Termius

---

<!-- section_id: "f460e419-56a6-405a-a6a6-1b9b723952b4" -->
## Devices

| Device | OS | Can SSH OUT | Can Accept SSH IN |
|--------|-----|-------------|-------------------|
| VPS | Ubuntu 24.04 | ✅ Yes | ✅ Yes |
| Windows | Windows 11 | ✅ Yes | ✅ Yes (with OpenSSH Server) |
| Linux | Ubuntu | ✅ Yes | ✅ Yes |
| iPhone | iOS | ✅ Yes | ❌ No (iOS limitation) |

---

<!-- section_id: "fff91d58-bc94-43b7-a622-7cfd8c5b41d3" -->
## Full Connection Matrix

```
        TO →
FROM ↓   VPS    Windows   Linux   iPhone
─────────────────────────────────────────
VPS      -      ✅        ✅      ❌
Windows  ✅     -         ✅      ❌
Linux    ✅     ✅        -       ❌
iPhone   ✅     ✅        ✅      -
```

**Legend:**
- ✅ = Possible and planned
- ❌ = Not possible (iPhone can't accept incoming SSH)

---

<!-- section_id: "c18ea734-8957-4d0f-989c-00db96af689d" -->
## Connection Details

<!-- section_id: "8d48c686-6996-42fb-a42b-28fbc5b10199" -->
### 1. VPS (46.224.184.10)
**Can connect TO:**
- Windows (need Windows SSH server + IP)
- Linux (need Linux IP)

**Can accept FROM:**
- Windows ✅ (already working)
- Linux (after fix)
- iPhone (after Termius setup)

<!-- section_id: "193b5192-1244-41de-816e-3ceef48f31a4" -->
### 2. Windows
**Can connect TO:**
- VPS ✅ (already working)
- Linux (need Linux IP)

**Can accept FROM (requires OpenSSH Server):**
- VPS
- Linux
- iPhone

<!-- section_id: "71c4d5e5-5fd8-4e50-b132-93751d0d3836" -->
### 3. Linux
**Can connect TO:**
- VPS
- Windows (need Windows SSH server)

**Can accept FROM:**
- VPS (via menu)
- Windows
- iPhone

<!-- section_id: "230dc165-32d2-406c-b657-979d5783d123" -->
### 4. iPhone
**Can connect TO:**
- VPS
- Windows (need Windows SSH server)
- Linux

**Can accept FROM:**
- ❌ None (iOS doesn't support SSH server)

---

<!-- section_id: "a3eedd66-2873-4962-8350-e116c540341a" -->
## Implementation Phases

<!-- section_id: "6cba98c1-e20e-4f54-8f1e-1b407a88805f" -->
### Phase A: Current State (DONE)
- [x] Windows → VPS

<!-- section_id: "272f38e8-de36-40ff-a3a5-4884f90b9daf" -->
### Phase B: After Linux Fix
- [ ] VPS → Linux
- [ ] Windows → Linux
- [ ] iPhone → VPS
- [ ] iPhone → Linux
- [ ] Linux → VPS

<!-- section_id: "ec640fa9-c64c-4e4d-b07d-5a17fd706e5c" -->
### Phase C: Enable Windows SSH Server
- [ ] Enable OpenSSH Server on Windows
- [ ] Get Windows local IP
- [ ] VPS → Windows
- [ ] Linux → Windows
- [ ] iPhone → Windows

<!-- section_id: "fa97cd63-bfea-4299-a1b5-c3c8a9c2d3f1" -->
### Phase D: Termius Sync
- [ ] All hosts synced via Termius account
- [ ] One-click connections from any device

---

<!-- section_id: "bd93c097-5374-4735-9b36-6fe786eb6c6d" -->
## Setup Commands

<!-- section_id: "c5f11a4e-2a6c-4307-913d-5559bb396da9" -->
### Windows - Enable SSH Server
```powershell
# Run as Administrator
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# Get IP
ipconfig | findstr "IPv4"
```

<!-- section_id: "0b5c8d1b-c586-4361-9017-225b7501b525" -->
### Linux - Ensure SSH Server Running
```bash
sudo systemctl enable ssh
sudo systemctl start ssh

# Get IP
ip addr | grep "inet " | grep -v 127.0.0.1
```

<!-- section_id: "d2311fd2-4215-4da3-9d53-c80ee108d693" -->
### VPS - Already configured
```bash
menu  # Use interactive menu
```

---

<!-- section_id: "fa885609-8956-4746-879a-ed4ec1f55b65" -->
## SSH Config (for all machines)

```
# VPS - Hetzner Cloud
Host vps
    HostName 46.224.184.10
    User root
    IdentityFile ~/.ssh/id_ed25519

# Linux - Local machine
Host linux
    HostName <LINUX_IP>
    User dawson
    IdentityFile ~/.ssh/id_ed25519

# Windows - Local machine (after SSH server enabled)
Host windows
    HostName <WINDOWS_IP>
    User dawson
    IdentityFile ~/.ssh/id_ed25519
```

---

<!-- section_id: "07e71b35-0901-44f4-8dcd-d4c1e29b827d" -->
## Termius Hosts to Configure

| Host Name | Address | User | Devices That Need It |
|-----------|---------|------|---------------------|
| VPS | 46.224.184.10 | root | All |
| Linux | <LOCAL_IP> | dawson | VPS, Windows, iPhone |
| Windows | <LOCAL_IP> | dawson | VPS, Linux, iPhone |

**Sync Strategy**: Configure on Windows, sign into same Termius account on all devices → automatic sync

---

<!-- section_id: "500fa0e8-e9b0-41a4-aad8-5dce5224fd9c" -->
## Network Diagram

```
                    ┌─────────────┐
                    │   iPhone    │
                    │  (client)   │
                    └──────┬──────┘
                           │ SSH out only
                           ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Windows   │◄───►│     VPS     │◄───►│    Linux    │
│  (local)    │     │  (cloud)    │     │   (local)   │
└──────┬──────┘     └─────────────┘     └──────┬──────┘
       │                                        │
       └────────────────────────────────────────┘
                    Direct local connection
```

---

<!-- section_id: "a5ed46ac-c55e-4a0d-9a8d-a657b55ac5a2" -->
## Post-Setup Verification

From each device, test all possible connections:

**From VPS:**
```bash
ssh windows   # If Windows SSH enabled
ssh linux     # After Linux IP set
```

**From Windows:**
```bash
ssh vps       # ✅ Already working
ssh linux     # After Linux IP set
```

**From Linux:**
```bash
ssh vps
ssh windows   # If Windows SSH enabled
```

**From iPhone (Termius):**
- Tap VPS → Should connect
- Tap Linux → Should connect
- Tap Windows → Should connect (if SSH enabled)

---

<!-- section_id: "cfa35a67-1233-43c9-a290-c7fdc218fe34" -->
## Blockers

| Blocker | Impact | Resolution |
|---------|--------|------------|
| Linux login loop | Can't get Linux IP | Fix via VPS SSH |
| Windows SSH server | Can't SSH into Windows | Enable OpenSSH Server |
| iPhone SSH server | Can't SSH into iPhone | Not possible (iOS limitation) |
