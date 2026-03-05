---
resource_id: "83a024c8-886d-4c97-8bff-ff7d62cd4437"
resource_type: "document"
resource_name: "PROGRESS_termius_cross_device_ssh"
---
# Progress: Termius Cross-Device SSH Setup

**Layer**: 0 (Universal)
**Stage**: 0.03 Execution
**Created**: 2026-01-17
**Last Updated**: 2026-01-17
**Status**: In Progress

---

<!-- section_id: "fc1cf668-1eb3-42f9-881e-6874abb1654c" -->
## Overall Progress

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1: Windows | ✅ COMPLETE | Termius installed, VPS connected |
| Phase 2: iPhone | ⏳ PENDING | User to download app |
| Phase 3: Fix Linux | ⏳ PENDING | Blocked by login loop |
| Phase 4: Linux Termius | ⏳ PENDING | After login fix |
| Phase 5: Update IPs | ⏳ PENDING | After Linux IP known |
| Phase 6: Verify All | ⏳ PENDING | After all setup |
| Phase 7: Windows SSH | ⏳ OPTIONAL | User to decide |

---

<!-- section_id: "ace75650-3c8f-42d3-af55-fd7e21dcb6c4" -->
## Detailed Status

<!-- section_id: "497695e2-91e2-4d33-8247-7e1bbbb59835" -->
### Windows (COMPLETE)
- [x] Termius installed
- [x] SSH config updated with VPS and Linux hosts
- [x] VPS host imported into Termius
- [x] Connection to VPS verified
- [x] Menu command working

<!-- section_id: "d4009c9e-846a-4b3b-88bc-8114deef69b4" -->
### iPhone (PENDING)
- [ ] Download Termius from App Store
- [ ] Sign in with Termius account
- [ ] Verify hosts synced
- [ ] Test VPS connection

<!-- section_id: "f24339d7-cf81-4978-a4d1-d3501df10baa" -->
### Linux (BLOCKED - waiting for login fix)
- [ ] Fix login loop first
- [ ] Install Termius via snap
- [ ] Sign in with same account
- [ ] Verify hosts synced
- [ ] Test connections

<!-- section_id: "31a3d254-59d9-478e-8c58-10511b11196a" -->
### VPS (COMPLETE)
- [x] SSH accessible from Windows
- [x] Menu with AI CLIs working
- [x] SSH key generated for Linux access
- [x] Menu option to SSH to Linux configured

---

<!-- section_id: "4787d2d1-c63d-49f0-a5c8-10ccd4ebc5cf" -->
## Connection Status

| Connection | Status | Tested |
|------------|--------|--------|
| Windows → VPS | ✅ Working | Yes |
| Windows → Linux | ⏳ Need IP | No |
| iPhone → VPS | ⏳ Pending | No |
| iPhone → Linux | ⏳ Pending | No |
| Linux → VPS | ⏳ Pending | No |
| VPS → Linux | ⏳ Need IP | No |

---

<!-- section_id: "91543a71-d7aa-46c0-8ed8-cf98c1038dc3" -->
## Next Steps

1. User downloads Termius on iPhone
2. User boots into Linux and gets IP
3. Fix login loop via VPS SSH
4. Install Termius on Linux
5. Update all configs with Linux IP
6. Verify all connections

---

<!-- section_id: "2a4584e5-3371-439b-9652-f00da3150796" -->
## Blockers

| Blocker | Impact | Resolution |
|---------|--------|------------|
| Linux login loop | Can't set up Linux Termius | Fix via VPS SSH |
| Linux IP unknown | Can't complete SSH configs | Get IP after boot |
