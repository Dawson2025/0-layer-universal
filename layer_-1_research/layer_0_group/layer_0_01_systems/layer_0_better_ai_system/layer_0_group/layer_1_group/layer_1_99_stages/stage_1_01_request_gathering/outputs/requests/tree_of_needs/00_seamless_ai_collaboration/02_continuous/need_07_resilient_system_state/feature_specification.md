# Feature Request: Full System Resilience

**Status**: Under Request Gathering
**Priority**: HIGH
**Related**: `need_06_universal_rules_and_cross_device_access`
**Project**: better_ai_system

---

## Overview

Make the entire 0_layer_universal AI system (universal rules, skills, memories, knowledge) accessible and usable by AI tools and applications **regardless of computer state, machine condition, or infrastructure failure**.

---

## What Is It?

A resilience infrastructure that ensures:

- ✓ **Layer 0 (Universal Rules)** always accessible
- ✓ **Layer 1 (Projects)** accessible from multiple locations
- ✓ **Layer -1 (Research)** recoverable even if primary storage fails
- ✓ AI tools can access system in **ANY state**:
  - Normal operation
  - Recovery mode
  - Corrupted filesystem
  - Boot failure
  - Offline/degraded
  - Multiple machines
  - Emergency situations

---

## Why?

### Current Risk
- 2.9GB AI system lives in one location
- If filesystem corrupts, system becomes inaccessible
- Universal rules (Layer 0) must ALWAYS be available
- Currently: Only Syncthing sync, no offline fallback

### Requirements That Demand This
From `need_06_universal_rules_and_cross_device_access`:
- Universal rules accessible to ANY user account
- Rules accessible from ANY filesystem location
- Rules accessible in EMERGENCY/RECOVERY mode
- Rules accessible from ANY machine (Syncthing synced)
- AI tools can access system from ANY of these

### Impact of Failure
- Can't access universal rules → AI tools can't operate
- Can't access project context → Projects blocked
- Can't access research → Development stalled
- Multi-machine: All machines blocked simultaneously

---

## Scope: 5 Phases

### Phase 0: Resolve Sync Conflicts (BLOCKING)
- 3,110 Syncthing conflict files currently exist
- Must resolve before implementing other phases
- Ensures correct versions backed up

### Phase 1: Recovery Partition (Weeks 2-3)
- Dedicated, bootable recovery partition
- Contains Layer 0 (universal rules) in read-only format
- Accessible if main filesystem fails
- **Result**: Layer 0 never inaccessible due to main drive failure

### Phase 2: A/B Redundancy (Weeks 3-4)
- Two complete copies of system (Partition A, Partition B)
- Automatic failover if one partition fails
- Syncthing keeps both synchronized
- **Result**: Automatic recovery without manual intervention

### Phase 3: External Immutable Backups (Weeks 4-5)
- Complete system copy to external USB (write-protected)
- Copy to cloud storage with Object Lock (S3)
- Monthly sync of changes
- **Result**: Full recovery possible even if both local partitions destroyed

### Phase 4: Live Boot USB (Weeks 5-6)
- Bootable recovery USB with full system pre-loaded
- Ubuntu minimal + all layers (0, 1, -1)
- Pre-cached for instant access
- **Result**: System bootable from USB if all local storage fails

### Phase 5: Network Recovery (Weeks 6-7, Optional)
- NFS/HTTP server with all layers accessible
- PXE boot fallback
- Cross-machine recovery
- **Result**: System accessible even if local storage offline

---

## Accessibility Matrix After Implementation

| System State | Layer 0 | Layer 1 | Layer -1 | Access Method |
|---|---|---|---|---|
| **Normal** | ✓ Fast | ✓ Fast | ✓ Fast | Synced local |
| **Main FS corrupted** | ✓ Fast | ✓ Fast | ✓ Fast | Recovery partition |
| **Both partitions fail** | ✓ Slow | ✓ Slow | ✓ Slow | Live boot USB |
| **All local storage offline** | ✓ Cached | ✓ Cached | ⚠ Limited | NFS network |
| **Completely offline** | ✓ USB | ✓ USB | ✓ USB | Pre-cached USB |

---

## Success Criteria

### Phase 0 Complete
- [ ] All 3,110 sync conflict files resolved
- [ ] Correct versions verified
- [ ] Git commit preserves cleanup
- [ ] `git status` shows clean

### Phase 1 Complete
- [ ] Recovery partition created
- [ ] Layer 0 copied (read-only)
- [ ] Bootable from recovery partition
- [ ] Access tested: PASS

### Phase 2 Complete
- [ ] Partition B created and synced
- [ ] Bootloader configured for failover
- [ ] Automatic failover tested: PASS
- [ ] Both partitions synchronized

### Phase 3 Complete
- [ ] External USB backup created
- [ ] Cloud backup with Object Lock enabled
- [ ] Restoration test: PASS
- [ ] Monthly sync automated

### Phase 4 Complete
- [ ] Live boot USB created
- [ ] All layers pre-loaded
- [ ] Boot test: PASS
- [ ] Can access system from USB

### Phase 5 Complete
- [ ] NFS server operational
- [ ] PXE boot configured
- [ ] Network recovery test: PASS
- [ ] Cross-machine access verified

### System Integration Complete
- [ ] AI tools configured for layered access
- [ ] Graceful degradation logic implemented
- [ ] Monitoring & alerting set up
- [ ] Recovery procedures documented
- [ ] Monthly validation tests automated

---

## Integration Points

### Syncthing (Existing)
- Maintains sync across machines
- Layer 0 changes synced immediately
- Layer 1 & -1 synced on schedule
- Continues to work with resilience layers

### Git (Existing)
- Version control for Layer 0 rules
- Full history preserved
- Rollback capability maintained
- Used for immutable backup versioning

### CLAUDE.md Cascade (Existing)
- AI tools load context from any accessible copy
- Fallback to earlier layers if current unavailable
- Works with recovery partitions & USB

### Hand-Off Documents (Existing)
- State persists in synced storage
- Survives across system states
- Enables AI tools to continue work

### Claude Code & Other AI Tools (NEW)
- Configured to use layered data access
- Query universal rules regardless of state
- Graceful degradation when layers unavailable
- Cross-machine access via Syncthing + network

---

## Risks & Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Sync conflicts during implementation | HIGH | Phase 0 resolves all conflicts first |
| Wrong versions backed up | HIGH | Audit + verify before Phase 1 |
| Recovery partition corrupts | MEDIUM | Weekly validation, 3+ copies |
| Both partitions fail simultaneously | LOW | External backup + network fallback |
| USB backup lost | LOW | Cloud backup with Object Lock |
| Network unavailable | MEDIUM | Pre-cached USB has full copy |
| AI tools can't handle degraded mode | MEDIUM | Implement layer-aware query logic |
| Recovery procedures untested | MEDIUM | Monthly recovery test automation |

---

## Resource Requirements

### Storage
- Recovery partition: 10-20GB
- USB backup: 32GB (3.5x for expansion)
- Cloud backup: First 5GB, then incremental
- Network NFS: 20GB (optional)

### Time
- Phase 0: 2-4 hours (one-time)
- Phase 1: 4-6 hours (one-time)
- Phase 2: 2-3 hours (one-time)
- Phase 3: 3-4 hours (one-time)
- Phase 4: 2-3 hours (one-time)
- Phase 5: 2-4 hours (one-time, optional)
- **Total**: 15-27 hours initial, then ~1 hour/month maintenance

### Tools
- Existing: Git, Syncthing, Linux standard tools
- New: None required, all using standard Linux tools
- Optional: Cloud storage (S3) for backup

---

## Timeline

```
Week 1:    Phase 0 (Sync conflict resolution) - BLOCKING
Week 2-3:  Phase 1 (Recovery partition)
Week 3-4:  Phase 2 (A/B redundancy)
Week 4-5:  Phase 3 (Immutable backups)
Week 5-6:  Phase 4 (Live boot USB)
Week 6-7:  Phase 5 (Network recovery, optional)
Week 7+:   Testing, validation, documentation
```

---

## Design Documents

See `RESILIENCE_SYSTEM_STAGING_PLAN.md` for detailed breakdown of how this feature flows through all 11 implementation stages.

---

## Next Steps

1. **Stage 01 (This stage)**: Clarify requirements ← YOU ARE HERE
2. **Stage 02**: Research resilience approaches
3. **Stage 03**: Define implementation procedures
4. **Stage 04**: Design system architecture
5. **Stage 05**: Create implementation plan
6. **Stage 06**: Build each phase
7. **Stage 07**: Test all scenarios
8. **Stage 08**: Critique and improve
9. **Stage 09**: Fix issues
10. **Stage 10**: Final working system
11. **Stage 11**: Archive & lessons learned

---

## Related Documents

- [`RESILIENCE_READINESS_ASSESSMENT.md`](../../../RESILIENCE_READINESS_ASSESSMENT.md): Current system analysis
- [`RESILIENCE_SYSTEM_STAGING_PLAN.md`](../RESILIENCE_SYSTEM_STAGING_PLAN.md): How to document through stages
- [`need_06_universal_rules_and_cross_device_access`](../need_06_universal_rules_and_cross_device_access/): Related requirement
- [`existing_infrastructure.md`](../../overview/existing_infrastructure.md): Current Syncthing system
