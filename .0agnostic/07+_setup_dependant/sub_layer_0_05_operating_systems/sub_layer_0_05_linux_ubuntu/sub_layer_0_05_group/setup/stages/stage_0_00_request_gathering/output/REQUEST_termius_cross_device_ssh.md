---
resource_id: "7d840ec3-ed71-46b9-ae81-0734002e1392"
resource_type: "document"
resource_name: "REQUEST_termius_cross_device_ssh"
---
# Request: Termius Cross-Device SSH Setup

**Layer**: 0 (Universal)
**Stage**: 0.00 Request Gathering
**Created**: 2026-01-17
**Status**: In Progress
**Related**: REQUEST_fix_linux_login_loop_via_cloud_ssh.md

---

<!-- section_id: "fb6d45b6-e603-49a1-a54c-6b68117ad299" -->
## Request Summary

Set up bidirectional SSH access between all machines (Windows, Linux, VPS, iPhone) using Termius as the unified SSH client across all platforms.

---

<!-- section_id: "89477a7a-b7e3-42f7-bdb2-ad0ad4cc8362" -->
## Problem Statement

- Multiple machines need to connect to each other via SSH
- Need consistent SSH experience across Windows, Linux, and iPhone
- Want one-click connections from any device to any other device
- Configuration should sync automatically between devices

---

<!-- section_id: "e2959497-9904-44aa-9cf4-3bf91c5808cf" -->
## Machines Involved

| Machine | OS | Role | IP |
|---------|-----|------|-----|
| Windows PC | Windows 11 | Primary workstation | Local network |
| Linux PC | Ubuntu | Dual-boot on same machine | Local network |
| VPS | Ubuntu 24.04 | Cloud server (Hetzner) | 46.224.184.10 |
| iPhone | iOS | Mobile access | N/A (client only) |

---

<!-- section_id: "71390aa7-6cf3-4294-98be-42a891fa8e70" -->
## Requirements

<!-- section_id: "e561c1b3-a3b2-4ac9-a84e-c4d6a9f70063" -->
### Functional Requirements
1. SSH from any device to VPS
2. SSH from any device to Linux
3. SSH from any device to Windows (optional)
4. Termius installed on Windows, Linux, iPhone
5. Hosts sync via Termius account
6. SSH keys properly distributed

<!-- section_id: "4ad0eecb-ff75-473d-bc12-91feeef46c87" -->
### Non-Functional Requirements
- One-click connections
- Passwordless authentication (SSH keys)
- Consistent experience across platforms

---

<!-- section_id: "3a606b45-a817-4a4c-9f4b-c521a160a64c" -->
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

<!-- section_id: "d91aea00-fd50-49da-9d5d-19a5706b1b83" -->
## Progress Log

| Date | Update |
|------|--------|
| 2026-01-17 | Termius installed on Windows |
| 2026-01-17 | VPS host imported from SSH config |
| 2026-01-17 | Windows → VPS connection verified |
| 2026-01-17 | Cross-device documentation created |

---

<!-- section_id: "71523543-3ad8-4c43-880f-3bb6da303f5f" -->
## Related Documentation

- `TERMIUS_CROSS_DEVICE_SETUP.md` - Full setup guide
- `TERMIUS_LINUX_SETUP.md` - Linux installation steps
- `IPHONE_QUICK_GUIDE.md` - iPhone setup steps
