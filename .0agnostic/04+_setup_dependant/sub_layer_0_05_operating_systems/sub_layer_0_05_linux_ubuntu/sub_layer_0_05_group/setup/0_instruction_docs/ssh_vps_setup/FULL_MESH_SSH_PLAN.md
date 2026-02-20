# Full Mesh SSH Connectivity Plan

**Goal**: Connect ALL devices to ALL other devices (where technically possible) using Termius

---

## Devices

| Device | OS | Can SSH OUT | Can Accept SSH IN |
|--------|-----|-------------|-------------------|
| VPS | Ubuntu 24.04 | ✅ Yes | ✅ Yes |
| Windows | Windows 11 | ✅ Yes | ✅ Yes (with OpenSSH Server) |
| Linux | Ubuntu | ✅ Yes | ✅ Yes |
| iPhone | iOS | ✅ Yes | ❌ No (iOS limitation) |

---

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

## Connection Details

### 1. VPS (46.224.184.10)
**Can connect TO:**
- Windows (need Windows SSH server + IP)
- Linux (need Linux IP)

**Can accept FROM:**
- Windows ✅ (already working)
- Linux (after fix)
- iPhone (after Termius setup)

### 2. Windows
**Can connect TO:**
- VPS ✅ (already working)
- Linux (need Linux IP)

**Can accept FROM (requires OpenSSH Server):**
- VPS
- Linux
- iPhone

### 3. Linux
**Can connect TO:**
- VPS
- Windows (need Windows SSH server)

**Can accept FROM:**
- VPS (via menu)
- Windows
- iPhone

### 4. iPhone
**Can connect TO:**
- VPS
- Windows (need Windows SSH server)
- Linux

**Can accept FROM:**
- ❌ None (iOS doesn't support SSH server)

---

## Implementation Phases

### Phase A: Current State (DONE)
- [x] Windows → VPS

### Phase B: After Linux Fix
- [ ] VPS → Linux
- [ ] Windows → Linux
- [ ] iPhone → VPS
- [ ] iPhone → Linux
- [ ] Linux → VPS

### Phase C: Enable Windows SSH Server
- [ ] Enable OpenSSH Server on Windows
- [ ] Get Windows local IP
- [ ] VPS → Windows
- [ ] Linux → Windows
- [ ] iPhone → Windows

### Phase D: Termius Sync
- [ ] All hosts synced via Termius account
- [ ] One-click connections from any device

---

## Setup Commands

### Windows - Enable SSH Server
```powershell
# Run as Administrator
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# Get IP
ipconfig | findstr "IPv4"
```

### Linux - Ensure SSH Server Running
```bash
sudo systemctl enable ssh
sudo systemctl start ssh

# Get IP
ip addr | grep "inet " | grep -v 127.0.0.1
```

### VPS - Already configured
```bash
menu  # Use interactive menu
```

---

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

## Termius Hosts to Configure

| Host Name | Address | User | Devices That Need It |
|-----------|---------|------|---------------------|
| VPS | 46.224.184.10 | root | All |
| Linux | <LOCAL_IP> | dawson | VPS, Windows, iPhone |
| Windows | <LOCAL_IP> | dawson | VPS, Linux, iPhone |

**Sync Strategy**: Configure on Windows, sign into same Termius account on all devices → automatic sync

---

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

## Blockers

| Blocker | Impact | Resolution |
|---------|--------|------------|
| Linux login loop | Can't get Linux IP | Fix via VPS SSH |
| Windows SSH server | Can't SSH into Windows | Enable OpenSSH Server |
| iPhone SSH server | Can't SSH into iPhone | Not possible (iOS limitation) |
