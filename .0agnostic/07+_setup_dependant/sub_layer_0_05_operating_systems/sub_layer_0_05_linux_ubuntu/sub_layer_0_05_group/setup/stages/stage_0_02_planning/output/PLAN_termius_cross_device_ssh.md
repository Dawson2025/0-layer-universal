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

<!-- section_id: "be067e3d-093f-4944-a8d1-613aa7ea2796" -->
## Execution Plan

<!-- section_id: "bf68e90f-ad68-445f-94d7-5b7619cdedab" -->
### Phase 1: Windows Setup (COMPLETE)
- [x] Install Termius on Windows
- [x] Import SSH config with VPS host
- [x] Verify VPS connection
- [x] Test menu command

<!-- section_id: "32bd06e0-c855-43a8-a9ee-98d18a2071b1" -->
### Phase 2: iPhone Setup
- [ ] Download Termius from App Store
- [ ] Create Termius account (or sign in)
- [ ] Hosts sync automatically from Windows
- [ ] Test VPS connection from iPhone

<!-- section_id: "9ffd4733-8dff-4fcc-a995-b917e920d66d" -->
### Phase 3: Fix Linux Login Loop
- [ ] Boot into Linux
- [ ] Get IP address via TTY
- [ ] SSH from VPS to Linux
- [ ] Run fix script
- [ ] Reboot and verify login works

<!-- section_id: "cc648b3b-7fa0-4304-82a5-29cc965c49a3" -->
### Phase 4: Linux Termius Setup
- [ ] Install Termius: `sudo snap install termius-app`
- [ ] Sign in with same Termius account
- [ ] Verify hosts synced (VPS should appear)
- [ ] Test VPS connection from Linux

<!-- section_id: "b87fe310-5517-4f25-9a85-752bebcb129b" -->
### Phase 5: Update All Configs with Linux IP
- [ ] Get Linux IP: `ip addr`
- [ ] Update Windows SSH config
- [ ] Update VPS menu (option 6)
- [ ] Termius will sync Linux host to all devices

<!-- section_id: "7201008a-bf08-48eb-96ed-c4025c78ffb1" -->
### Phase 6: Verify All Connections
- [ ] Windows → VPS ✅
- [ ] Windows → Linux
- [ ] iPhone → VPS
- [ ] iPhone → Linux
- [ ] Linux → VPS
- [ ] VPS → Linux ✅

<!-- section_id: "ce7023b8-1ba0-42c6-857c-cb543292e2cc" -->
### Phase 7: Optional - Windows SSH Server
- [ ] Enable OpenSSH Server on Windows
- [ ] Get Windows IP
- [ ] Add Windows host to SSH configs
- [ ] Test: VPS → Windows
- [ ] Test: Linux → Windows
- [ ] Test: iPhone → Windows

---

<!-- section_id: "fe92890e-e0ed-40ff-84e5-0958c79c1381" -->
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

<!-- section_id: "cedeeb80-608a-4c51-8fdc-561d04053abd" -->
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

<!-- section_id: "1592a78f-0d9d-4fcb-a40a-00b3a414adc2" -->
## Rollback Plan

If Termius sync fails:
1. Manually add hosts on each device
2. Use SSH config import as backup
3. Export/import hosts via file

If Windows SSH server causes issues:
1. Stop service: `Stop-Service sshd`
2. Disable: `Set-Service -Name sshd -StartupType 'Disabled'`

---

<!-- section_id: "cdaebc6e-e42f-4a4b-994a-da9c39d7bf78" -->
## Success Criteria

- [ ] Can SSH to VPS from any device with one click
- [ ] Can SSH to Linux from any device with one click
- [ ] Termius hosts stay in sync across all devices
- [ ] AI CLI tools accessible via VPS menu from any device
