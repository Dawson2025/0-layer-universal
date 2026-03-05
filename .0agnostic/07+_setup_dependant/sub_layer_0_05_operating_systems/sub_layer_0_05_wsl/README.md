---
resource_id: "b708923c-78e7-4949-9104-fc05236a7d14"
resource_type: "readme
document"
resource_name: "README"
---
# Windows Subsystem for Linux (WSL) Setup

Setup documentation specific to Windows Subsystem for Linux environments.

<!-- section_id: "568360f1-75c1-4f8a-8336-00ef1515296e" -->
## System Information

**Hardware:** Lenovo Yoga 9 Pro
**WSL Version:** WSL 2
**Distribution:** Ubuntu 24.04.3 LTS
**Kernel:** 6.6.87.2-microsoft-standard-WSL2

<!-- section_id: "562863f2-6886-4c89-ab2f-9fc115d3bfc2" -->
## WSL-Specific Considerations

<!-- section_id: "bfc06a8b-7632-40fc-83c9-f4255eeabd97" -->
### Hybrid Environment
- WSL runs Linux on top of Windows using Hyper-V virtualization
- Access Windows files via `/mnt/c/`, `/mnt/d/`, etc.
- Access Linux files from Windows via `\\wsl$\Ubuntu-24.04\`
- Environment variables and paths need translation between systems

<!-- section_id: "e010b46b-1e56-4424-b672-2d2183b93d7c" -->
### Networking
- WSL2 uses virtualized networking (NAT)
- IP address: 172.23.194.12 (dynamically assigned)
- localhost forwarding works between Windows and WSL

<!-- section_id: "4d8b9bdd-b3ad-43f2-9a45-3c4ee30e3313" -->
### File System
- Linux filesystem stored in virtual disk (ext4)
- Windows filesystem accessed through mount points
- Better performance when working within Linux filesystem
- Cross-filesystem operations can be slower

<!-- section_id: "b67fdc46-ddcd-42f2-b76e-0f673679b606" -->
## Common Issues and Solutions

<!-- section_id: "28ad5118-e8d3-4168-943f-dbebe740bed2" -->
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

<!-- section_id: "a34339b7-80b2-44c2-ac9e-c7698b87fb76" -->
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

<!-- section_id: "99602f55-a715-49a2-bafa-cb8346954ec0" -->
## WSL Commands Reference

<!-- section_id: "d97872fb-b8ed-4a8f-9e78-9750b070a8b9" -->
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

<!-- section_id: "cd1b2d4b-8562-45b7-b7dd-22371e990091" -->
### Version Management
```bash
# Check WSL version
wsl --version

# Update WSL
wsl --update

# Set WSL version for a distribution
wsl --set-version Ubuntu-24.04 2
```

<!-- section_id: "9caf0b5b-a325-4eeb-8323-296436cb444f" -->
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

<!-- section_id: "b6e69483-f568-4148-b430-bf9482552a29" -->
## Hardware-Specific Notes (Lenovo Yoga 9 Pro)

<!-- section_id: "6d63a4e2-aa23-47ca-9405-d50049c1da57" -->
### Working Configuration
- WSL 2 with Ubuntu 24.04.3 LTS
- Hyper-V and Virtual Machine Platform enabled
- Windows virtualization features working correctly

<!-- section_id: "6365d45a-4cb5-442c-874d-2634d57861d3" -->
### Known Issues
- vmcompute service can occasionally get stuck requiring system restart
- No specific hardware incompatibilities found

<!-- section_id: "1b7041e7-a1f0-4f97-86cb-b8f0132036fe" -->
### Performance
- System load: Minimal when idle (0.0)
- Memory usage: ~3% typical
- Disk usage: 4.1% of 1006.85GB allocated space

<!-- section_id: "fb1e23d2-2efa-4d39-a948-526b319b634f" -->
## Best Practices

<!-- section_id: "a73e73f4-c48c-43a2-80c6-40590f168f47" -->
### Daily Usage
1. Start WSL by simply running `wsl` in PowerShell or Windows Terminal
2. Access Windows files from `/mnt/c/` when needed
3. Keep project files in Linux filesystem for better performance
4. Use `wsl --shutdown` before major system updates

<!-- section_id: "33601ba6-1e85-4581-93ff-b6a08cf8114b" -->
### Troubleshooting Steps
1. Try `wsl --shutdown` and restart WSL
2. Check Windows services (vmcompute, vmms)
3. Update WSL with `wsl --update`
4. As last resort, restart the computer
5. Check Event Viewer (System logs) for vmcompute errors

<!-- section_id: "d925cd0e-094b-4cb6-82ea-26ebf7e3f432" -->
### Maintenance
- Keep Windows updated
- Keep WSL updated with `wsl --update`
- Keep Ubuntu updated with `sudo apt update && sudo apt upgrade`
- Monitor disk space in both Windows and WSL

<!-- section_id: "0b53efa0-93dd-47b3-b39c-3adba3640df4" -->
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

<!-- section_id: "ae236796-946b-43d5-996e-6c0d69dba9a2" -->
## Next Level

Navigate to `0.06_environments/` to continue setting up your environment.

<!-- section_id: "4c2b22ae-5853-4cc3-b449-d7fb8ae92bfe" -->
## Links to Detailed Documentation

For detailed WSL setup, see:
- [Microsoft WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/)
- [WSL GitHub Issues](https://github.com/microsoft/WSL/issues)
- **sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/WSL_SETUP.md** (if exists)
