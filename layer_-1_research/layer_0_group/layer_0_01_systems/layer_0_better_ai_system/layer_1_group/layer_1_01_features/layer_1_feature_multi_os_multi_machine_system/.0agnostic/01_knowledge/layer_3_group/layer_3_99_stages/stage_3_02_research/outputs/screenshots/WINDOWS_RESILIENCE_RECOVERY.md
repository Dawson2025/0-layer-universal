---
resource_id: "93c1bde5-992c-4f87-a823-1b2408a6311c"
resource_type: "knowledge"
resource_name: "WINDOWS_RESILIENCE_RECOVERY"
---
# Windows Resilience & Remote Recovery System

**Created**: 2026-01-21
**Status**: ✅ IMPLEMENTED
**OS**: Windows 11

---

<!-- section_id: "ab4ac0ca-57ab-4c10-9d45-01d98513a0b3" -->
## Overview

This document describes a Murphy's Law resilient recovery system for the Windows laptop (dual boot with Linux). The goal is to ensure that **no matter what breaks**, you can always remotely access the system via SSH/RDP through Tailscale and fix it using Claude Code or other tools.

---

<!-- section_id: "be987c57-09da-48af-af68-71729604c2f5" -->
## Current State Assessment

| Component | Status | Notes |
|-----------|--------|-------|
| Tailscale | ✅ Running | Auto-starts, auto-restart on failure |
| OpenSSH Server | ✅ Running | Auto-starts, auto-restart on failure |
| RDP | ⚠️ Not configured | Optional - SSH is primary |
| Syncthing | ✅ Running | Via system tray |
| Claude Code | ✅ Installed | Available in PATH |

---

<!-- section_id: "5e57019d-e29e-4eed-ab8d-9b68acc0721a" -->
## System Configuration

| Setting | Value |
|---------|-------|
| OS | Windows 11 |
| Hostname | LAPTOP-GF3B5QV4 |
| Tailscale IP | 100.91.229.9 |
| Local IP | 10.200.164.45 (DHCP) |
| Username | Dawson |

---

<!-- section_id: "2910ab68-4fa4-49b4-b933-8177994976bd" -->
## Failure Modes & Solutions

<!-- section_id: "ecb81c2a-af05-4b24-9b18-c677900a24b4" -->
### Layer 1: Service Failures

| Failure | Solution | Status |
|---------|----------|--------|
| Tailscale crashes | Auto-restart via Windows Service Recovery | ✅ Configured |
| SSH crashes | Auto-restart via Windows Service Recovery | ✅ Configured |
| Syncthing crashes | Auto-restart via Task Scheduler | [ ] To configure |

<!-- section_id: "ee56558d-f4ac-41ac-b75c-10fc1a6e952a" -->
### Layer 2: Boot/Login Failures

| Failure | Solution | Status |
|---------|----------|--------|
| GUI login loop | SSH access still works via Tailscale | ✅ SSH working |
| BSOD on boot | Safe Mode with Networking + SSH | [ ] To test |
| User profile corrupted | RDP to other admin account | [ ] To set up |
| BitLocker issues | Recovery key backup | [ ] To document |

<!-- section_id: "a78e4c44-f8a7-45d4-8549-07d425e12ee9" -->
### Layer 3: Network Failures

| Failure | Solution | Status |
|---------|----------|--------|
| WiFi driver fails | Tailscale uses any available network | ✅ Implicit |
| Tailscale auth expires | Auto-renewal + SSH via local IP fallback | ✅ Working |
| Firewall blocks SSH | Configure Windows Firewall rules | ✅ Rule exists |

<!-- section_id: "d0cb4b01-dd86-4146-b083-95413618bba0" -->
### Layer 4: Hardware Level

| Failure | Solution | Status |
|---------|----------|--------|
| System hangs | No software watchdog on Windows | N/A |
| Disk errors | chkdsk auto-repair on boot | [x] Default |

---

<!-- section_id: "427a9f85-e4cf-4e54-9ad2-ebcf28eac9e3" -->
## Implementation Plan

<!-- section_id: "5a9f941b-2c8d-41be-8923-92e5f7b7b9f4" -->
### Phase 1: Install OpenSSH Server

```powershell
# Run as Administrator

# Check current state
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

# Install OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start and enable SSH service
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# Configure service recovery (restart on failure)
sc.exe failure sshd reset= 86400 actions= restart/5000/restart/10000/restart/30000
```

<!-- section_id: "e6076706-13bf-497c-93d6-b0035d7e90ab" -->
### Phase 2: Configure SSH Authentication

```powershell
# Allow key-based authentication
# Edit: C:\ProgramData\ssh\sshd_config

# Ensure these settings:
# PubkeyAuthentication yes
# PasswordAuthentication yes
# PermitUserEnvironment yes

# Copy authorized keys
mkdir C:\Users\Dawson\.ssh -Force
# Add public keys to C:\Users\Dawson\.ssh\authorized_keys

# Fix permissions (important for Windows SSH)
icacls "C:\Users\Dawson\.ssh" /inheritance:r
icacls "C:\Users\Dawson\.ssh" /grant "Dawson:(OI)(CI)F"
icacls "C:\Users\Dawson\.ssh" /grant "SYSTEM:(OI)(CI)F"

# Restart SSH
Restart-Service sshd
```

<!-- section_id: "a01cb615-3bd6-4ea0-8e47-b7501d6093ab" -->
### Phase 3: Configure Windows Firewall

```powershell
# Allow SSH through firewall (should be automatic but verify)
Get-NetFirewallRule -Name *ssh*

# If not present, add rule
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

# Allow Tailscale interface specifically
New-NetFirewallRule -Name "Tailscale SSH" -DisplayName "SSH via Tailscale" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22 -InterfaceAlias "Tailscale"
```

<!-- section_id: "09fd45ad-0826-4f47-aa1e-4eaa81222964" -->
### Phase 4: Configure Tailscale Service Recovery

```powershell
# Configure Tailscale to auto-restart on failure
sc.exe failure Tailscale reset= 86400 actions= restart/5000/restart/10000/restart/30000
```

<!-- section_id: "dc3649e2-b2e9-491f-8d69-02a74efee2ff" -->
### Phase 5: Configure Syncthing Auto-Start

```powershell
# Create scheduled task to start Syncthing at login
$action = New-ScheduledTaskAction -Execute "C:\Users\Dawson\AppData\Local\Microsoft\WinGet\Packages\Syncthing.Syncthing_Microsoft.Winget.Source_8wekyb3d8bbwe\syncthing-windows-amd64-v2.0.12\syncthing.exe" -Argument "--no-browser"
$trigger = New-ScheduledTaskTrigger -AtLogon -User "Dawson"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1)
Register-ScheduledTask -TaskName "Syncthing" -Action $action -Trigger $trigger -Settings $settings -User "Dawson" -RunLevel Highest
```

<!-- section_id: "3fdaac8b-5068-49fe-8fe3-baede89a4f30" -->
### Phase 6: Enable RDP (Backup Access Method)

```powershell
# Enable Remote Desktop
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0

# Allow through firewall
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

# Note: RDP uses port 3389
```

<!-- section_id: "123f5f4c-6bf4-4080-ab6c-6526f46f3f63" -->
### Phase 7: Create Recovery Admin Account

```powershell
# Create backup admin account for recovery
$Password = Read-Host -AsSecureString "Enter password for recovery account"
New-LocalUser -Name "RecoveryAdmin" -Password $Password -FullName "Recovery Administrator" -Description "Emergency recovery account"
Add-LocalGroupMember -Group "Administrators" -Member "RecoveryAdmin"
```

---

<!-- section_id: "71ddad13-708a-4613-bebb-90461e3ec428" -->
## Emergency Recovery Procedures

<!-- section_id: "6b10f965-cbee-4268-9d61-b0d5214a5af9" -->
### When GUI Breaks (Login Loop, etc.)

1. **From iPhone**: Open Termius
2. **Connect to VPS**: Use `tailscale_for_iphone_to_vps` connection
3. **On VPS**: SSH to Windows: `ssh dawson@100.91.229.9`
4. **On Windows**: Use PowerShell/CMD to diagnose
   - Check Event Viewer: `Get-EventLog -LogName System -Newest 50`
   - Check services: `Get-Service | Where-Object {$_.Status -eq 'Stopped'}`

<!-- section_id: "8ecddf35-1e2b-4b96-8c4c-cbc182a13448" -->
### When SSH via Tailscale Fails

1. Check Tailscale status from another device
2. Try RDP instead: `mstsc /v:100.91.229.9`
3. If on same network: Try local IP (10.200.164.x)
4. Boot to Safe Mode with Networking

<!-- section_id: "222f00ed-a665-437b-8dfc-ae3f14138461" -->
### When Everything Fails

1. Boot to Windows Recovery Environment
2. Use System Restore to previous working state
3. Boot to Safe Mode, disable problematic services
4. As last resort: Repair install from Windows USB

---

<!-- section_id: "7a96a176-4b28-4ebe-b5f9-1e0eef6d70d4" -->
## AI CLI Tools

| Tool | Command | Status |
|------|---------|--------|
| Claude Code | `claude` | ✅ Installed (npm global) |
| Other AI tools | TBD | Not installed |

<!-- section_id: "d4ea5ce3-ef73-4d17-834a-e8cc2489ad63" -->
### Claude Code Location
- Installation: `%APPDATA%\npm\node_modules\@anthropic-ai\claude-code`
- Command: Available in PATH

---

<!-- section_id: "780958f4-24d1-44fd-84fd-69d920adc5f6" -->
## Health Check Script

Save as `C:\Users\Dawson\scripts\windows-health-check.ps1`:

```powershell
# Windows Resilience Health Check
Write-Host "=== Windows Resilience Health Check ===" -ForegroundColor Cyan

# Check SSH
$ssh = Get-Service sshd -ErrorAction SilentlyContinue
if ($ssh -and $ssh.Status -eq 'Running') {
    Write-Host "[OK] SSH Server running" -ForegroundColor Green
} else {
    Write-Host "[FAIL] SSH Server not running" -ForegroundColor Red
}

# Check Tailscale
$tailscale = Get-Service Tailscale -ErrorAction SilentlyContinue
if ($tailscale -and $tailscale.Status -eq 'Running') {
    $ip = tailscale ip -4
    Write-Host "[OK] Tailscale running (IP: $ip)" -ForegroundColor Green
} else {
    Write-Host "[FAIL] Tailscale not running" -ForegroundColor Red
}

# Check Syncthing
$syncthing = Get-Process syncthing -ErrorAction SilentlyContinue
if ($syncthing) {
    Write-Host "[OK] Syncthing running" -ForegroundColor Green
} else {
    Write-Host "[WARN] Syncthing not running" -ForegroundColor Yellow
}

# Check firewall rules
$sshRule = Get-NetFirewallRule -Name *ssh* -ErrorAction SilentlyContinue
if ($sshRule) {
    Write-Host "[OK] SSH firewall rule exists" -ForegroundColor Green
} else {
    Write-Host "[WARN] SSH firewall rule not found" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== Network Connectivity ===" -ForegroundColor Cyan
Test-NetConnection -ComputerName 46.224.184.10 -Port 22 -WarningAction SilentlyContinue |
    Select-Object ComputerName, TcpTestSucceeded
```

---

<!-- section_id: "e4894d6e-0697-4e3a-9922-eea7971aa05a" -->
## Testing Checklist

- [x] SSH from localhost works (2026-01-21)
- [x] SSH from VPS to Windows via Tailscale IP (2026-01-21)
- [x] SSH from iPhone (via VPS) to Windows (same as above)
- [ ] RDP from VPS to Windows (if needed)
- [x] Tailscale auto-restart configured (2026-01-21)
- [x] SSH auto-restart configured (2026-01-21)
- [ ] Verify Syncthing starts on login
- [ ] Test Safe Mode with Networking access

---

<!-- section_id: "f7b8733a-2e23-46fd-8463-e007f76d99ff" -->
## Related Files

- `LINUX_RESILIENCE_RECOVERY.md` - Linux laptop recovery
- `VPS_RESILIENCE_RECOVERY.md` - VPS server recovery
- `STATUS.md` - Multi-OS workspace status
- `DEVICE_IDS.md` - Device identifiers and IPs
