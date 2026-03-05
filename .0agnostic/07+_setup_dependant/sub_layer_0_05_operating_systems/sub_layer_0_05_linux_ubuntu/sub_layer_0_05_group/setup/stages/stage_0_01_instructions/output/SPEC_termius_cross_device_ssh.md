---
resource_id: "84c5c6e5-5e49-4fde-81d1-4d014de22402"
resource_type: "document"
resource_name: "SPEC_termius_cross_device_ssh"
---
# Spec: Termius Cross-Device SSH Setup

**Layer**: 0 (Universal)
**Stage**: 0.01 Instructions
**Created**: 2026-01-17
**Related Request**: `REQUEST_termius_cross_device_ssh.md`

---

<!-- section_id: "3e2a8636-4f2c-4b77-bdf0-6a2d5749dd33" -->
## Technical Specification

<!-- section_id: "0a6d6a65-ff01-4540-a67f-1f03ee1340d1" -->
### SSH Key Distribution

**Primary Key**: `~/.ssh/id_ed25519` (Ed25519)

| Machine | Has Key | In authorized_keys |
|---------|---------|-------------------|
| Windows | ✅ Yes | N/A (client) |
| Linux | ✅ Yes | VPS key added |
| VPS | ✅ Generated | Windows key added |

<!-- section_id: "a67f4591-12bc-484a-aec8-7d88ea0856a5" -->
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

<!-- section_id: "ff81bebe-9c71-4f86-ad91-c433f34f4472" -->
## Termius Configuration

<!-- section_id: "3cd630ed-36f5-4417-a7b9-2e7ccd2af296" -->
### Account Sync
- All devices use same Termius account
- Hosts automatically sync between devices
- Keys can be stored in Termius vault (encrypted)

<!-- section_id: "42dae111-6652-4da0-a6de-173885d04ab8" -->
### Hosts to Configure

| Host Name | Address | User | Key |
|-----------|---------|------|-----|
| VPS | 46.224.184.10 | root | id_ed25519 |
| Linux | TBD | dawson | id_ed25519 |
| Windows | TBD (optional) | dawson | id_ed25519 |

---

<!-- section_id: "2150e6c7-bdb8-4106-8104-ff3fbb9fb772" -->
## Installation Commands

<!-- section_id: "1563050a-e5e2-48eb-b8e9-2f9ae6405328" -->
### Windows
- Download from termius.com ✅ Done

<!-- section_id: "8c287eda-d88b-458d-8021-0840f84a61e3" -->
### Linux
```bash
sudo snap install termius-app
# OR
flatpak install flathub com.termius.Termius
```

<!-- section_id: "b49950f4-dc5b-4b27-b7ab-d297980b45d0" -->
### iPhone
- App Store: "Termius - SSH Client"

---

<!-- section_id: "68ffb591-579d-4db5-aa1f-81539bc4db96" -->
## Connection Matrix

<!-- section_id: "35e04579-740b-49b4-837e-2df6cf826f72" -->
### Required Connections
```
Windows ──→ VPS      ✅ Complete
Windows ──→ Linux    ⏳ Need Linux IP
iPhone  ──→ VPS      ⏳ Install Termius
iPhone  ──→ Linux    ⏳ Install Termius + Linux IP
Linux   ──→ VPS      ⏳ After login fix
VPS     ──→ Linux    ✅ Menu configured
```

<!-- section_id: "5ef74c43-0120-473a-a2fd-c7361cc3d58b" -->
### Optional Connections (Windows SSH Server)
```
VPS     ──→ Windows  ⏳ Enable Windows SSH
Linux   ──→ Windows  ⏳ Enable Windows SSH
iPhone  ──→ Windows  ⏳ Enable Windows SSH
```

---

<!-- section_id: "c2f8f670-67e5-456c-a968-2863e15cad56" -->
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

<!-- section_id: "6ef61af9-8f2b-4863-abfe-b1a4f63c05d3" -->
## Verification Tests

<!-- section_id: "7fd562e2-bd7d-4a33-9568-f1eeca9658a6" -->
### From Windows
```bash
ssh vps        # Should connect to VPS
ssh linux      # Should connect to Linux (after IP set)
```

<!-- section_id: "17a1fe09-4635-4f07-8ae7-09005f5a3f45" -->
### From VPS
```bash
ssh dawson@<LINUX_IP>    # Should connect to Linux
```

<!-- section_id: "18e83e72-3a85-4f2a-a6d7-09641af6fb7a" -->
### From Linux
```bash
ssh vps        # Should connect to VPS
```

<!-- section_id: "a5513132-f4cb-41ec-9cab-885361f48487" -->
### From iPhone
- Open Termius → Tap VPS → Should connect
- Open Termius → Tap Linux → Should connect

---

<!-- section_id: "c0dbe09d-5beb-47e7-9a0d-3ffddbac0e46" -->
## Security Considerations

1. SSH keys only (no password auth)
2. Keys stored locally, not in cloud (unless using Termius vault)
3. VPS firewall configured for SSH only
4. Local network machines only accessible on LAN
