---
resource_id: "94c911a5-216f-43c2-8b8c-3db7beb0d432"
resource_type: "knowledge"
resource_name: "WINDOWS_RESILIENCE_RECOVERY"
---
# Windows Resilience & Remote Recovery System

**Created**: 2026-01-21
**Status**: ✅ IMPLEMENTED
**OS**: Windows 11

---

## Overview

This document describes a Murphy's Law resilient recovery system for the Windows laptop (dual boot with Linux). The goal is to ensure that **no matter what breaks**, you can always remotely access the system via SSH/RDP through Tailscale and fix it using Claude Code or other tools.

---

## Current State Assessment

| Component | Status | Notes |
|-----------|--------|-------|
| Tailscale | ✅ Running | Auto-starts, auto-restart on failure |
| OpenSSH Server | ✅ Running | Auto-starts, auto-restart on failure |
| RDP | ⚠️ Not configured | Optional - SSH is primary |
| Syncthing | ✅ Running | Via system tray |
| Claude Code | ✅ Installed | Available in PATH |

---

## System Configuration

| Setting | Value |
|---------|-------|
| OS | Windows 11 |
| Hostname | LAPTOP-GF3B5QV4 |
| Tailscale IP | 100.91.229.9 |
| Local IP | 10.200.164.45 (DHCP) |
| Username | Dawson |

---

## Failure Modes & Solutions

### Layer 1: Service Failures

| Failure | Solution | Status |
|---------|----------|--------|
| Tailscale crashes | Auto-restart via Windows Service Recovery | ✅ Configured |
| SSH crashes | Auto-restart via Windows Service Recovery | ✅ Configured |
| Syncthing crashes | Auto-restart via Task Scheduler | [ ] To configure |

### Layer 2: Boot/Login Failures

| Failure | Solution | Status |
|---------|----------|--------|
| GUI login loop | SSH access still works via Tailscale | ✅ SSH working |
| BSOD on boot | Safe Mode with Networking + SSH | [ ] To test |
| User profile corrupted | RDP to other admin account | [ ] To set up |
| BitLocker issues | Recovery key backup | [ ] To document |

### Layer 3: Network Failures

| Failure | Solution | Status |
|---------|----------|--------|
| WiFi driver fails | Tailscale uses any available network | ✅ Implicit |
| Tailscale auth expires | Auto-renewal + SSH via local IP fallback | ✅ Working |
| Firewall blocks SSH | Configure Windows Firewall rules | ✅ Rule exists |

### Layer 4: Hardware Level

| Failure | Solution | Status |
|---------|----------|--------|
| System hangs | No software watchdog on Windows | N/A |
| Disk errors | chkdsk auto-repair on boot | [x] Default |

---

## Implementation Plan

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

### Phase 3: Configure Windows Firewall

```powershell
# Allow SSH through firewall (should be automatic but verify)
Get-NetFirewallRule -Name *ssh*

# If not present, add rule
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

# Allow Tailscale interface specifically
New-NetFirewallRule -Name "Tailscale SSH" -DisplayName "SSH via Tailscale" -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22 -InterfaceAlias "Tailscale"
```

### Phase 4: Configure Tailscale Service Recovery

```powershell
# Configure Tailscale to auto-restart on failure
sc.exe failure Tailscale reset= 86400 actions= restart/5000/restart/10000/restart/30000
```

### Phase 5: Configure Syncthing Auto-Start

```powershell
# Create scheduled task to start Syncthing at login
$action = New-ScheduledTaskAction -Execute "C:\Users\Dawson\AppData\Local\Microsoft\WinGet\Packages\Syncthing.Syncthing_Microsoft.Winget.Source_8wekyb3d8bbwe\syncthing-windows-amd64-v2.0.12\syncthing.exe" -Argument "--no-browser"
$trigger = New-ScheduledTaskTrigger -AtLogon -User "Dawson"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1)
Register-ScheduledTask -TaskName "Syncthing" -Action $action -Trigger $trigger -Settings $settings -User "Dawson" -RunLevel Highest
```

### Phase 6: Enable RDP (Backup Access Method)

```powershell
# Enable Remote Desktop
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0

# Allow through firewall
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

# Note: RDP uses port 3389
```

### Phase 7: Create Recovery Admin Account

```powershell
# Create backup admin account for recovery
$Password = Read-Host -AsSecureString "Enter password for recovery account"
New-LocalUser -Name "RecoveryAdmin" -Password $Password -FullName "Recovery Administrator" -Description "Emergency recovery account"
Add-LocalGroupMember -Group "Administrators" -Member "RecoveryAdmin"
```

---

## Emergency Recovery Procedures

### When GUI Breaks (Login Loop, etc.)

1. **From iPhone**: Open Termius
2. **Connect to VPS**: Use `tailscale_for_iphone_to_vps` connection
3. **On VPS**: SSH to Windows: `ssh dawson@100.91.229.9`
4. **On Windows**: Use PowerShell/CMD to diagnose
   - Check Event Viewer: `Get-EventLog -LogName System -Newest 50`
   - Check services: `Get-Service | Where-Object {$_.Status -eq 'Stopped'}`

### When SSH via Tailscale Fails

1. Check Tailscale status from another device
2. Try RDP instead: `mstsc /v:100.91.229.9`
3. If on same network: Try local IP (10.200.164.x)
4. Boot to Safe Mode with Networking

### When Everything Fails

1. Boot to Windows Recovery Environment
2. Use System Restore to previous working state
3. Boot to Safe Mode, disable problematic services
4. As last resort: Repair install from Windows USB

---

## AI CLI Tools

| Tool | Command | Status |
|------|---------|--------|
| Claude Code | `claude` | ✅ Installed (npm global) |
| Other AI tools | TBD | Not installed |

### Claude Code Location
- Installation: `%APPDATA%\npm\node_modules\@anthropic-ai\claude-code`
- Command: Available in PATH

---

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

## Related Files

- `LINUX_RESILIENCE_RECOVERY.md` - Linux laptop recovery
- `VPS_RESILIENCE_RECOVERY.md` - VPS server recovery
- `STATUS.md` - Multi-OS workspace status
- `DEVICE_IDS.md` - Device identifiers and IPs
