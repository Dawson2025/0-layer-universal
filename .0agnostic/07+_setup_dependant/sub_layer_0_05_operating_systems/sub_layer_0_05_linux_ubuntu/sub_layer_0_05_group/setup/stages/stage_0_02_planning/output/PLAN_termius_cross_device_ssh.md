---
resource_id: "be210830-5cea-483e-8587-9940831e3df4"
resource_type: "document"
resource_name: "PLAN_termius_cross_device_ssh"
---
# Plan: Termius Cross-Device SSH Setup

**Layer**: 0 (Universal)
**Stage**: 0.02 Planning
**Created**: 2026-01-17
**Related Request**: `REQUEST_termius_cross_device_ssh.md`
**Related Spec**: `SPEC_termius_cross_device_ssh.md`

---

## Execution Plan

### Phase 1: Windows Setup (COMPLETE)
- [x] Install Termius on Windows
- [x] Import SSH config with VPS host
- [x] Verify VPS connection
- [x] Test menu command

### Phase 2: iPhone Setup
- [ ] Download Termius from App Store
- [ ] Create Termius account (or sign in)
- [ ] Hosts sync automatically from Windows
- [ ] Test VPS connection from iPhone

### Phase 3: Fix Linux Login Loop
- [ ] Boot into Linux
- [ ] Get IP address via TTY
- [ ] SSH from VPS to Linux
- [ ] Run fix script
- [ ] Reboot and verify login works

### Phase 4: Linux Termius Setup
- [ ] Install Termius: `sudo snap install termius-app`
- [ ] Sign in with same Termius account
- [ ] Verify hosts synced (VPS should appear)
- [ ] Test VPS connection from Linux

### Phase 5: Update All Configs with Linux IP
- [ ] Get Linux IP: `ip addr`
- [ ] Update Windows SSH config
- [ ] Update VPS menu (option 6)
- [ ] Termius will sync Linux host to all devices

### Phase 6: Verify All Connections
- [ ] Windows → VPS ✅
- [ ] Windows → Linux
- [ ] iPhone → VPS
- [ ] iPhone → Linux
- [ ] Linux → VPS
- [ ] VPS → Linux ✅

### Phase 7: Optional - Windows SSH Server
- [ ] Enable OpenSSH Server on Windows
- [ ] Get Windows IP
- [ ] Add Windows host to SSH configs
- [ ] Test: VPS → Windows
- [ ] Test: Linux → Windows
- [ ] Test: iPhone → Windows

---

## Dependencies

```
Phase 1 (Windows) ✅ COMPLETE
    │
    ├──→ Phase 2 (iPhone) - Can do now
    │
    └──→ Phase 3 (Fix Linux) - Can do now
              │
              └──→ Phase 4 (Linux Termius)
                        │
                        └──→ Phase 5 (Update IPs)
                                  │
                                  └──→ Phase 6 (Verify)
                                            │
                                            └──→ Phase 7 (Optional Windows SSH)
```

---

## Time Estimate

| Phase | Duration |
|-------|----------|
| Phase 1 | ✅ Complete |
| Phase 2 | ~5 minutes |
| Phase 3 | ~10 minutes |
| Phase 4 | ~5 minutes |
| Phase 5 | ~5 minutes |
| Phase 6 | ~5 minutes |
| Phase 7 | ~10 minutes (optional) |

---

## Rollback Plan

If Termius sync fails:
1. Manually add hosts on each device
2. Use SSH config import as backup
3. Export/import hosts via file

If Windows SSH server causes issues:
1. Stop service: `Stop-Service sshd`
2. Disable: `Set-Service -Name sshd -StartupType 'Disabled'`

---

## Success Criteria

- [ ] Can SSH to VPS from any device with one click
- [ ] Can SSH to Linux from any device with one click
- [ ] Termius hosts stay in sync across all devices
- [ ] AI CLI tools accessible via VPS menu from any device
