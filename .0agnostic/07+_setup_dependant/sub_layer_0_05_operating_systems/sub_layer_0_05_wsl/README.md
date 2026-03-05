---
resource_id: "b708923c-78e7-4949-9104-fc05236a7d14"
resource_type: "readme
document"
resource_name: "README"
---
# Windows Subsystem for Linux (WSL) Setup

Setup documentation specific to Windows Subsystem for Linux environments.

## System Information

**Hardware:** Lenovo Yoga 9 Pro
**WSL Version:** WSL 2
**Distribution:** Ubuntu 24.04.3 LTS
**Kernel:** 6.6.87.2-microsoft-standard-WSL2

## WSL-Specific Considerations

### Hybrid Environment
- WSL runs Linux on top of Windows using Hyper-V virtualization
- Access Windows files via `/mnt/c/`, `/mnt/d/`, etc.
- Access Linux files from Windows via `\\wsl$\Ubuntu-24.04\`
- Environment variables and paths need translation between systems

### Networking
- WSL2 uses virtualized networking (NAT)
- IP address: 172.23.194.12 (dynamically assigned)
- localhost forwarding works between Windows and WSL

### File System
- Linux filesystem stored in virtual disk (ext4)
- Windows filesystem accessed through mount points
- Better performance when working within Linux filesystem
- Cross-filesystem operations can be slower

## Common Issues and Solutions

### "Catastrophic failure" Error

**Error Message:**
```
Catastrophic failure
Error code: Wsl/Service/E_UNEXPECTED
```

**Cause:**
This error occurs when the `vmcompute` service (Hyper-V Host Compute Service) becomes stuck or fails to start properly. This is the underlying service that manages WSL's virtualization.

**Solution:**
1. **Restart the computer** - This is the most reliable fix
   ```powershell
   Restart-Computer -Force
   ```

**Attempted fixes that may not work:**
- Restarting the vmcompute service (often hangs)
- Running `wsl --shutdown` (may hang if service is stuck)
- Killing WSL processes manually
- Updating WSL with `wsl --update`

**Prevention:**
- Keep Windows and WSL updated
- Avoid force-terminating WSL instances when possible
- Properly shutdown WSL with `wsl --shutdown` before system updates

### Service Management

**Key Windows Services for WSL:**
- `vmcompute` - Hyper-V Host Compute Service (critical)
- `vmms` - Hyper-V Virtual Machine Management Service
- `LxssManager` - May not be present on all systems

**Check WSL Status:**
```powershell
wsl --list --verbose
wsl --status
```

**Shutdown WSL:**
```bash
wsl --shutdown
```

**Update WSL:**
```bash
wsl --update
```

## WSL Commands Reference

### Distribution Management
```bash
# List installed distributions
wsl --list --verbose

# Set default distribution
wsl --set-default Ubuntu-24.04

# Unregister a distribution (deletes all data!)
wsl --unregister Ubuntu-24.04

# Install a new distribution
wsl --install -d Ubuntu-24.04
```

### Version Management
```bash
# Check WSL version
wsl --version

# Update WSL
wsl --update

# Set WSL version for a distribution
wsl --set-version Ubuntu-24.04 2
```

### System Operations
```bash
# Shutdown all WSL instances
wsl --shutdown

# Terminate specific distribution
wsl --terminate Ubuntu-24.04

# Run command in WSL
wsl <command>

# Run as specific user
wsl -u root
```

## Hardware-Specific Notes (Lenovo Yoga 9 Pro)

### Working Configuration
- WSL 2 with Ubuntu 24.04.3 LTS
- Hyper-V and Virtual Machine Platform enabled
- Windows virtualization features working correctly

### Known Issues
- vmcompute service can occasionally get stuck requiring system restart
- No specific hardware incompatibilities found

### Performance
- System load: Minimal when idle (0.0)
- Memory usage: ~3% typical
- Disk usage: 4.1% of 1006.85GB allocated space

## Best Practices

### Daily Usage
1. Start WSL by simply running `wsl` in PowerShell or Windows Terminal
2. Access Windows files from `/mnt/c/` when needed
3. Keep project files in Linux filesystem for better performance
4. Use `wsl --shutdown` before major system updates

### Troubleshooting Steps
1. Try `wsl --shutdown` and restart WSL
2. Check Windows services (vmcompute, vmms)
3. Update WSL with `wsl --update`
4. As last resort, restart the computer
5. Check Event Viewer (System logs) for vmcompute errors

### Maintenance
- Keep Windows updated
- Keep WSL updated with `wsl --update`
- Keep Ubuntu updated with `sudo apt update && sudo apt upgrade`
- Monitor disk space in both Windows and WSL

## System Messages

When first logging in, you may see:
```
System information as of [date/time]

  System load:  0.0                 Processes:             10
  Usage of /:   4.1% of 1006.85GB   Users logged in:       0
  Memory usage: 3%                  IPv4 address for eth0: 172.23.194.12
  Swap usage:   0%
```

To disable the daily message, create:
```bash
touch ~/.hushlogin
```

## Next Level

Navigate to `0.06_environments/` to continue setting up your environment.

## Links to Detailed Documentation

For detailed WSL setup, see:
- [Microsoft WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/)
- [WSL GitHub Issues](https://github.com/microsoft/WSL/issues)
- **sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/WSL_SETUP.md** (if exists)
