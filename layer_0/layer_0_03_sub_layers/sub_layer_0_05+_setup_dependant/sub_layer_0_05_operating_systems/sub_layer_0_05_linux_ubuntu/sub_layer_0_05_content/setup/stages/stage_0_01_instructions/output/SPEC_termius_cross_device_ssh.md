# Spec: Termius Cross-Device SSH Setup

**Layer**: 0 (Universal)
**Stage**: 0.01 Instructions
**Created**: 2026-01-17
**Related Request**: `REQUEST_termius_cross_device_ssh.md`

---

## Technical Specification

### SSH Key Distribution

**Primary Key**: `~/.ssh/id_ed25519` (Ed25519)

| Machine | Has Key | In authorized_keys |
|---------|---------|-------------------|
| Windows | ✅ Yes | N/A (client) |
| Linux | ✅ Yes | VPS key added |
| VPS | ✅ Generated | Windows key added |

### SSH Config (All Machines)

```
Host vps
    HostName 46.224.184.10
    User root
    IdentityFile ~/.ssh/id_ed25519

Host linux
    HostName <LINUX_IP>
    User dawson
    IdentityFile ~/.ssh/id_ed25519

Host windows
    HostName <WINDOWS_IP>
    User dawson
    IdentityFile ~/.ssh/id_ed25519
```

---

## Termius Configuration

### Account Sync
- All devices use same Termius account
- Hosts automatically sync between devices
- Keys can be stored in Termius vault (encrypted)

### Hosts to Configure

| Host Name | Address | User | Key |
|-----------|---------|------|-----|
| VPS | 46.224.184.10 | root | id_ed25519 |
| Linux | TBD | dawson | id_ed25519 |
| Windows | TBD (optional) | dawson | id_ed25519 |

---

## Installation Commands

### Windows
- Download from termius.com ✅ Done

### Linux
```bash
sudo snap install termius-app
# OR
flatpak install flathub com.termius.Termius
```

### iPhone
- App Store: "Termius - SSH Client"

---

## Connection Matrix

### Required Connections
```
Windows ──→ VPS      ✅ Complete
Windows ──→ Linux    ⏳ Need Linux IP
iPhone  ──→ VPS      ⏳ Install Termius
iPhone  ──→ Linux    ⏳ Install Termius + Linux IP
Linux   ──→ VPS      ⏳ After login fix
VPS     ──→ Linux    ✅ Menu configured
```

### Optional Connections (Windows SSH Server)
```
VPS     ──→ Windows  ⏳ Enable Windows SSH
Linux   ──→ Windows  ⏳ Enable Windows SSH
iPhone  ──→ Windows  ⏳ Enable Windows SSH
```

---

## Windows SSH Server Setup (Optional)

```powershell
# Run as Administrator
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# Allow through firewall
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

---

## Verification Tests

### From Windows
```bash
ssh vps        # Should connect to VPS
ssh linux      # Should connect to Linux (after IP set)
```

### From VPS
```bash
ssh dawson@<LINUX_IP>    # Should connect to Linux
```

### From Linux
```bash
ssh vps        # Should connect to VPS
```

### From iPhone
- Open Termius → Tap VPS → Should connect
- Open Termius → Tap Linux → Should connect

---

## Security Considerations

1. SSH keys only (no password auth)
2. Keys stored locally, not in cloud (unless using Termius vault)
3. VPS firewall configured for SSH only
4. Local network machines only accessible on LAN
