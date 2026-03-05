---
resource_id: "b38ba758-3124-4b05-a9a0-b64e13856fad"
resource_type: "document"
resource_name: "TERMIUS_CROSS_DEVICE_SETUP"
---
# Termius Cross-Device SSH Setup

Full bidirectional SSH access between all machines using Termius.

---

<!-- section_id: "5859e27b-cc81-4d63-b74d-54ad21f6b1ff" -->
## Machines

| Machine | OS | IP/Hostname | SSH User |
|---------|-----|-------------|----------|
| VPS | Ubuntu 24.04 | 46.224.184.10 | root |
| Linux | Ubuntu | TBD (local network) | dawson |
| Windows | Windows 11 | TBD (local network) | dawson |

---

<!-- section_id: "4bd324df-29e6-4e96-9a3a-22070635e342" -->
## Connection Matrix

| From ↓ / To → | VPS | Linux | Windows |
|---------------|-----|-------|---------|
| **VPS** | - | ✅ Menu option 4 | ⏳ Need Windows SSH |
| **Linux** | ⏳ After fix | - | ⏳ Need Windows SSH |
| **Windows** | ✅ Done | ⏳ Need Linux IP | - |
| **iPhone** | ⏳ Sync from account | ⏳ Sync from account | ⏳ Need Windows SSH |

---

<!-- section_id: "56e99f3e-781c-45b0-b583-918a3d05e4d2" -->
## Setup Steps

<!-- section_id: "aa705eb7-f37c-4510-bf91-005a458bb250" -->
### 1. VPS (COMPLETE)
- IP: 46.224.184.10
- User: root
- Key: ~/.ssh/id_ed25519
- Hosts configured on: Windows ✅

<!-- section_id: "0a9cb3a6-06d2-4275-8c75-b3cdfa0656d4" -->
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

<!-- section_id: "fabadeb0-c3f2-484d-a444-03fdaded4e18" -->
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

<!-- section_id: "8515f318-4ac9-4b94-9bc6-50b7913adead" -->
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

<!-- section_id: "919a0418-3b16-43ec-9e9c-dff0aeb67edc" -->
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

<!-- section_id: "d1e044c3-6eaa-45b7-8998-a6404f77b7d4" -->
## Quick Reference

<!-- section_id: "605b4fbc-a4ee-4289-8f7b-f58c06e4fc77" -->
### From Any Device
```bash
ssh vps      # Connect to cloud server
ssh linux    # Connect to Linux machine
ssh windows  # Connect to Windows machine (if SSH enabled)
```

<!-- section_id: "141adfd8-c2b4-40ef-95b7-03535e9ecb41" -->
### Termius
- All hosts sync via account
- One-click connect from any device
- Works on Windows, Linux, iPhone, Android

---

<!-- section_id: "de9f806e-2bcc-4648-ae03-6c967cc88a34" -->
## Post-Fix Checklist

- [ ] Fix Linux login loop
- [ ] Get Linux IP and update configs
- [ ] Install Termius on Linux
- [ ] Sign in to Termius account on Linux
- [ ] Verify all connections work
- [ ] (Optional) Enable Windows SSH server
- [ ] (Optional) Add Windows host to all devices
