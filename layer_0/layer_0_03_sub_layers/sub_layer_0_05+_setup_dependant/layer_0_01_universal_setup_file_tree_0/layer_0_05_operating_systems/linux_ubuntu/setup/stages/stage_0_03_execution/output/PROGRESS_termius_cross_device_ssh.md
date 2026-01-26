# Progress: Termius Cross-Device SSH Setup

**Layer**: 0 (Universal)
**Stage**: 0.03 Execution
**Created**: 2026-01-17
**Last Updated**: 2026-01-17
**Status**: In Progress

---

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

## Detailed Status

### Windows (COMPLETE)
- [x] Termius installed
- [x] SSH config updated with VPS and Linux hosts
- [x] VPS host imported into Termius
- [x] Connection to VPS verified
- [x] Menu command working

### iPhone (PENDING)
- [ ] Download Termius from App Store
- [ ] Sign in with Termius account
- [ ] Verify hosts synced
- [ ] Test VPS connection

### Linux (BLOCKED - waiting for login fix)
- [ ] Fix login loop first
- [ ] Install Termius via snap
- [ ] Sign in with same account
- [ ] Verify hosts synced
- [ ] Test connections

### VPS (COMPLETE)
- [x] SSH accessible from Windows
- [x] Menu with AI CLIs working
- [x] SSH key generated for Linux access
- [x] Menu option to SSH to Linux configured

---

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

## Next Steps

1. User downloads Termius on iPhone
2. User boots into Linux and gets IP
3. Fix login loop via VPS SSH
4. Install Termius on Linux
5. Update all configs with Linux IP
6. Verify all connections

---

## Blockers

| Blocker | Impact | Resolution |
|---------|--------|------------|
| Linux login loop | Can't set up Linux Termius | Fix via VPS SSH |
| Linux IP unknown | Can't complete SSH configs | Get IP after boot |
