---
resource_id: "b38ba758-3124-4b05-a9a0-b64e13856fad"
resource_type: "document"
resource_name: "TERMIUS_CROSS_DEVICE_SETUP"
---
# Termius Cross-Device SSH Setup

Full bidirectional SSH access between all machines using Termius.

---

## Machines

| Machine | OS | IP/Hostname | SSH User |
|---------|-----|-------------|----------|
| VPS | Ubuntu 24.04 | 46.224.184.10 | root |
| Linux | Ubuntu | TBD (local network) | dawson |
| Windows | Windows 11 | TBD (local network) | dawson |

---

## Connection Matrix

| From ↓ / To → | VPS | Linux | Windows |
|---------------|-----|-------|---------|
| **VPS** | - | ✅ Menu option 4 | ⏳ Need Windows SSH |
| **Linux** | ⏳ After fix | - | ⏳ Need Windows SSH |
| **Windows** | ✅ Done | ⏳ Need Linux IP | - |
| **iPhone** | ⏳ Sync from account | ⏳ Sync from account | ⏳ Need Windows SSH |

---

## Setup Steps

### 1. VPS (COMPLETE)
- IP: 46.224.184.10
- User: root
- Key: ~/.ssh/id_ed25519
- Hosts configured on: Windows ✅

### 2. Linux (AFTER LOGIN FIX)

**On Linux:**
```bash
# Get IP address
ip addr | grep "inet " | grep -v 127.0.0.1

# Ensure SSH server is running
sudo systemctl enable ssh
sudo systemctl start ssh

# Add VPS public key for passwordless access FROM VPS
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w root@ubuntu-4gb-nbg1-1" >> ~/.ssh/authorized_keys
```

**On Windows (update SSH config):**
```bash
# Edit ~/.ssh/config and replace LINUX_IP_HERE with actual IP
```

**On VPS (already done):**
- Menu option 6: Set Linux IP
- Menu option 4: SSH to Linux

### 3. Windows SSH Server (OPTIONAL - for incoming connections)

**Enable OpenSSH Server on Windows:**
```powershell
# Run as Administrator
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
```

**Get Windows IP:**
```powershell
ipconfig | findstr "IPv4"
```

**Add to other machines' SSH config:**
```
Host windows
    HostName WINDOWS_IP_HERE
    User dawson
    IdentityFile ~/.ssh/id_ed25519
```

---

## Termius Sync Strategy

Using **Termius Account** (recommended):
1. Create hosts on Windows
2. Sign in on all devices with same account
3. All hosts automatically sync!

**Hosts to create in Termius:**
- VPS (46.224.184.10) ✅ Done
- Linux (IP TBD)
- Windows (IP TBD, if SSH server enabled)

---

## SSH Config Template (for all machines)

```
Host vps
    HostName 46.224.184.10
    User root
    IdentityFile ~/.ssh/id_ed25519

Host linux
    HostName LINUX_IP_HERE
    User dawson
    IdentityFile ~/.ssh/id_ed25519

Host windows
    HostName WINDOWS_IP_HERE
    User dawson
    IdentityFile ~/.ssh/id_ed25519
```

---

## Quick Reference

### From Any Device
```bash
ssh vps      # Connect to cloud server
ssh linux    # Connect to Linux machine
ssh windows  # Connect to Windows machine (if SSH enabled)
```

### Termius
- All hosts sync via account
- One-click connect from any device
- Works on Windows, Linux, iPhone, Android

---

## Post-Fix Checklist

- [ ] Fix Linux login loop
- [ ] Get Linux IP and update configs
- [ ] Install Termius on Linux
- [ ] Sign in to Termius account on Linux
- [ ] Verify all connections work
- [ ] (Optional) Enable Windows SSH server
- [ ] (Optional) Add Windows host to all devices
