---
resource_id: "a0341d61-d018-4552-9a53-079a6657f52f"
resource_type: "document"
resource_name: "PLAN_full_mesh_ssh_connectivity"
---
# Full Mesh SSH Connectivity Plan

**Goal**: Connect ALL devices to ALL other devices (where technically possible) using Termius

---

<!-- section_id: "ee46349a-99d7-438e-9424-6054cf14ff28" -->
## Devices

| Device | OS | Can SSH OUT | Can Accept SSH IN |
|--------|-----|-------------|-------------------|
| VPS | Ubuntu 24.04 | ✅ Yes | ✅ Yes |
| Windows | Windows 11 | ✅ Yes | ✅ Yes (with OpenSSH Server) |
| Linux | Ubuntu | ✅ Yes | ✅ Yes |
| iPhone | iOS | ✅ Yes | ❌ No (iOS limitation) |

---

<!-- section_id: "11a3b855-85a3-48d6-a405-3bd6054b8d04" -->
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

<!-- section_id: "c501fe6f-1a90-42c0-b2ac-2dcb4ee8c30a" -->
## Connection Details

<!-- section_id: "add8cafe-857a-43da-805b-ba5ffdee582c" -->
### 1. VPS (46.224.184.10)
**Can connect TO:**
- Windows (need Windows SSH server + IP)
- Linux (need Linux IP)

**Can accept FROM:**
- Windows ✅ (already working)
- Linux (after fix)
- iPhone (after Termius setup)

<!-- section_id: "4c1d8d84-5bac-4561-a60f-5eb35bdd0898" -->
### 2. Windows
**Can connect TO:**
- VPS ✅ (already working)
- Linux (need Linux IP)

**Can accept FROM (requires OpenSSH Server):**
- VPS
- Linux
- iPhone

<!-- section_id: "890ece3f-8c6c-4967-9c08-b2ea072cc811" -->
### 3. Linux
**Can connect TO:**
- VPS
- Windows (need Windows SSH server)

**Can accept FROM:**
- VPS (via menu)
- Windows
- iPhone

<!-- section_id: "0d36e23c-41c0-4f16-b530-ac01521edba0" -->
### 4. iPhone
**Can connect TO:**
- VPS
- Windows (need Windows SSH server)
- Linux

**Can accept FROM:**
- ❌ None (iOS doesn't support SSH server)

---

<!-- section_id: "00017500-b197-4610-873e-eef4b96f0e21" -->
## Implementation Phases

<!-- section_id: "0d12d7c4-a91e-463b-8a3d-a090099bc3ff" -->
### Phase A: Current State (DONE)
- [x] Windows → VPS

<!-- section_id: "f4a2344d-cb37-4d6b-bb19-239c189e42a7" -->
### Phase B: After Linux Fix
- [ ] VPS → Linux
- [ ] Windows → Linux
- [ ] iPhone → VPS
- [ ] iPhone → Linux
- [ ] Linux → VPS

<!-- section_id: "6d26d497-a141-4723-8ece-ac18e5180bdb" -->
### Phase C: Enable Windows SSH Server
- [ ] Enable OpenSSH Server on Windows
- [ ] Get Windows local IP
- [ ] VPS → Windows
- [ ] Linux → Windows
- [ ] iPhone → Windows

<!-- section_id: "df17def4-3576-4bc0-b886-f6a87ffe2abc" -->
### Phase D: Termius Sync
- [ ] All hosts synced via Termius account
- [ ] One-click connections from any device

---

<!-- section_id: "3049647d-3826-4096-8c99-eee26576be35" -->
## Setup Commands

<!-- section_id: "5e403348-b01e-4ba1-9e3a-f92db40c2348" -->
### Windows - Enable SSH Server
```powershell
# Run as Administrator
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# Get IP
ipconfig | findstr "IPv4"
```

<!-- section_id: "b2343da9-6f49-420c-9ae1-3a06b7e8c834" -->
### Linux - Ensure SSH Server Running
```bash
sudo systemctl enable ssh
sudo systemctl start ssh

# Get IP
ip addr | grep "inet " | grep -v 127.0.0.1
```

<!-- section_id: "45fef02d-c40f-4ad8-9d97-763bba1dceef" -->
### VPS - Already configured
```bash
menu  # Use interactive menu
```

---

<!-- section_id: "e49b5345-18d1-481d-9a8c-4271e4267523" -->
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

<!-- section_id: "854c680f-a391-4a54-9f02-e0b8f132aefa" -->
## Termius Hosts to Configure

| Host Name | Address | User | Devices That Need It |
|-----------|---------|------|---------------------|
| VPS | 46.224.184.10 | root | All |
| Linux | <LOCAL_IP> | dawson | VPS, Windows, iPhone |
| Windows | <LOCAL_IP> | dawson | VPS, Linux, iPhone |

**Sync Strategy**: Configure on Windows, sign into same Termius account on all devices → automatic sync

---

<!-- section_id: "0cc79611-e4f9-4d63-95be-5b3dd715669c" -->
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

<!-- section_id: "caef5eb6-dd5b-4185-afde-ba1e41e04f25" -->
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

<!-- section_id: "16c97386-3904-472c-b922-6155cf017f0f" -->
## Blockers

| Blocker | Impact | Resolution |
|---------|--------|------------|
| Linux login loop | Can't get Linux IP | Fix via VPS SSH |
| Windows SSH server | Can't SSH into Windows | Enable OpenSSH Server |
| iPhone SSH server | Can't SSH into iPhone | Not possible (iOS limitation) |
