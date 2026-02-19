# Request: Termius Cross-Device SSH Setup

**Layer**: 0 (Universal)
**Stage**: 0.00 Request Gathering
**Created**: 2026-01-17
**Status**: In Progress
**Related**: REQUEST_fix_linux_login_loop_via_cloud_ssh.md

---

## Request Summary

Set up bidirectional SSH access between all machines (Windows, Linux, VPS, iPhone) using Termius as the unified SSH client across all platforms.

---

## Problem Statement

- Multiple machines need to connect to each other via SSH
- Need consistent SSH experience across Windows, Linux, and iPhone
- Want one-click connections from any device to any other device
- Configuration should sync automatically between devices

---

## Machines Involved

| Machine | OS | Role | IP |
|---------|-----|------|-----|
| Windows PC | Windows 11 | Primary workstation | Local network |
| Linux PC | Ubuntu | Dual-boot on same machine | Local network |
| VPS | Ubuntu 24.04 | Cloud server (Hetzner) | 46.224.184.10 |
| iPhone | iOS | Mobile access | N/A (client only) |

---

## Requirements

### Functional Requirements
1. SSH from any device to VPS
2. SSH from any device to Linux
3. SSH from any device to Windows (optional)
4. Termius installed on Windows, Linux, iPhone
5. Hosts sync via Termius account
6. SSH keys properly distributed

### Non-Functional Requirements
- One-click connections
- Passwordless authentication (SSH keys)
- Consistent experience across platforms

---

## Acceptance Criteria

- [x] Termius installed on Windows
- [x] VPS host configured in Termius (Windows)
- [x] Windows → VPS connection working
- [ ] Termius installed on iPhone
- [ ] iPhone → VPS connection working
- [ ] Linux login loop fixed
- [ ] Termius installed on Linux
- [ ] Linux → VPS connection working
- [ ] VPS → Linux connection working
- [ ] All hosts synced via Termius account
- [ ] (Optional) Windows SSH server enabled
- [ ] (Optional) All devices can SSH to Windows

---

## Progress Log

| Date | Update |
|------|--------|
| 2026-01-17 | Termius installed on Windows |
| 2026-01-17 | VPS host imported from SSH config |
| 2026-01-17 | Windows → VPS connection verified |
| 2026-01-17 | Cross-device documentation created |

---

## Related Documentation

- `TERMIUS_CROSS_DEVICE_SETUP.md` - Full setup guide
- `TERMIUS_LINUX_SETUP.md` - Linux installation steps
- `IPHONE_QUICK_GUIDE.md` - iPhone setup steps
