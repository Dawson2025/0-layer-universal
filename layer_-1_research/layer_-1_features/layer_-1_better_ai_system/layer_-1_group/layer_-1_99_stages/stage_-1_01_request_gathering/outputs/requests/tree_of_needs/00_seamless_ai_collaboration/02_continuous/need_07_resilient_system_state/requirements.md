# Need: Resilient System State & Data Accessibility

**Branch**: [02_continuous](../)
**Question**: "Will my AI system survive storage failures and corrupted filesystems?"
**Related Needs**: need_06_universal_rules_and_cross_device_access, need_02_session_resilient
**Related Feature**: feature_resilience_system.md

---

## Definition

The AI system (universal rules, skills, memories, knowledge) must survive **catastrophic failures** and remain accessible from **multiple independent locations**, ensuring that:

- Universal rules (Layer 0) never become inaccessible
- System continues functioning even if main storage corrupts
- Recovery is automatic without manual intervention
- Data is protected against data loss scenarios

---

## Why This Matters

- **Criticality**: If universal rules become inaccessible, entire AI system fails
- **Data Loss Prevention**: 2.9GB of AI system could be lost without redundancy
- **Uptime**: System should continue even during storage failure
- **Safety**: Universal rules guide all AI behavior - they MUST always be available
- **User Trust**: Users need confidence system won't lose their data

---

## Requirements

### Multi-Location Storage

- MUST store complete Layer 0 (universal rules) in ≥3 independent locations
- MUST store Layers 1 and -1 in ≥2 independent locations
- MUST maintain bit-for-bit identical copies across locations
- MUST verify checksums on all copies regularly

### Automatic Failover

- MUST detect when primary storage location becomes unavailable
- MUST automatically use next available location (no user intervention)
- MUST preserve complete system state during failover
- MUST recover from failures without data loss

### Recovery Partition

- MUST have dedicated recovery partition separate from main filesystem
- MUST contain full Layer 0 (universal rules) in immutable form
- MUST be bootable independent of main partition
- MUST be accessible even if main filesystem corrupted
- MUST be regularly synchronized with primary system

### A/B Redundancy

- MUST maintain two complete copies of system (Partition A, Partition B)
- MUST keep copies synchronized automatically
- MUST allow seamless failover if one partition fails
- MUST support automatic recovery and resync

### External Immutable Backup

- MUST backup all layers to external storage (USB, cloud)
- MUST use write-protection/immutability (can't be modified after creation)
- MUST store with version history (can recover to any point in time)
- MUST encrypt sensitive data
- MUST verify integrity regularly

### Live Boot Recovery

- MUST provide bootable recovery media (USB)
- MUST contain full system pre-cached
- MUST be bootable even if all local storage failed
- MUST provide complete system access from boot media

### Network Recovery (Optional)

- SHOULD have network-accessible recovery systems
- SHOULD support PXE/network boot fallback
- SHOULD allow system restoration over network
- SHOULD work across multiple machines

### Verification & Monitoring

- MUST verify all copies match regularly (checksums)
- MUST alert if copies diverge
- MUST detect data corruption immediately
- MUST have automated validation procedures
- MUST support manual verification procedures

### Recovery Procedures

- MUST document recovery procedures for each failure scenario
- MUST test recovery procedures regularly (monthly minimum)
- MUST have automated recovery tests
- MUST track recovery time objectives (RTO) and recovery point objectives (RPO)

---

## Acceptance Criteria

- [ ] Layer 0 stored in ≥3 independent locations
- [ ] Recovery partition created and bootable
- [ ] A/B redundancy implemented and tested
- [ ] External backups with immutability verified
- [ ] Live boot USB created and tested
- [ ] Automatic failover tested: works without user intervention
- [ ] Recovery procedures documented
- [ ] Recovery procedures tested monthly
- [ ] All copies verified to be identical
- [ ] Checksums validate after each sync

---

## Implementation Phases

See feature_resilience_system.md for detailed phases:
- Phase 0: Resolve sync conflicts (prerequisite)
- Phase 1: Recovery partition
- Phase 2: A/B redundancy
- Phase 3: External backups
- Phase 4: Live boot USB
- Phase 5: Network recovery (optional)

---

## Related Needs

- `need_02_session_resilient`: State must persist across system states
- `need_06_universal_rules_and_cross_device_access`: Rules must be universally accessible
- `need_03_failure_recoverable`: System recovers gracefully from failure
- `need_05_cross_platform`: Recovery works across platforms

---

## Open Questions

1. How often should recovery be tested? (Monthly? Weekly?)
2. What RTO is acceptable? (Recovery time objective)
3. What RPO is acceptable? (Recovery point objective)
4. Should network recovery be implemented or just optional?
5. How far back should version history go? (All time? 1 year? 3 months?)

