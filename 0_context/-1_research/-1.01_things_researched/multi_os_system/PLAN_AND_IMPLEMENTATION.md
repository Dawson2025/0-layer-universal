# Multi-OS Workspace Sync Plan + Implementation

## Plan Summary

Goal: Maintain a canonical WSL workspace that syncs bidirectionally across Windows 11, WSL2, and Native Ubuntu (Dual Boot) on a single laptop.

### Core Strategic Pivot (2026-01-09)
Because Windows/WSL and Native Ubuntu share the same hardware (Dual Boot), they are never online at the same time. **Direct peer-to-peer sync is physically impossible.**

**New Architectural Pattern:**
- **Triple Replica:** Local working copies on Windows (NTFS), WSL (ext4), and Ubuntu (ext4).
- **Relay Bridge:** Use a 3rd "Always On" device (Phone, VPS, or NAS) as a Syncthing relay to store changes during reboots.
- **Dependency Exclusion:** Strict exclusion of build/dependency folders (`node_modules`, `.venv`) from the sync fabric.

## Current System Status (2026-01-09)

| Environment | OS | Status | Connection |
| :--- | :--- | :--- | :--- |
| **WSL2** | Ubuntu 24.04 | ✅ Running | Connected to Windows |
| **Host** | Windows 11 | ✅ Running | Connected to WSL |
| **Native** | Ubuntu Desktop | ⏸️ Offline | **Dual Boot - Requires Relay** |

### Recent Implementation (2026-01-09)
- **Windows Recovery:** Discovered `syncthing.exe` service was down on the host. Restarted process and verified firewall rules. WSL ↔ Windows sync restored.
- **IP Correction:** Documentation previously listed `10.200.164.40` as Ubuntu; this has been corrected to the **Windows Host** IP.
- **Architecture Validation:** Research confirmed that Dual Boot requires a Store-and-Forward relay for seamless "pick up where you left off" workflows.

## Remaining Implementation Steps

### Phase 1: The Relay (URGENT)
1.  **Identify Relay Device:** Choose a 3rd device (e.g., Android Phone with Syncthing, or a VPS).
2.  **Add Relay to Cluster:** Add the Relay Device ID to Windows, WSL, and Ubuntu.
3.  **Establish Data Bridge:** 
    - Windows/WSL syncs to Relay.
    - Reboot.
    - Ubuntu pulls from Relay.

### Phase 2: Performance & Hygiene
1.  **Update `.stignore`:** Ensure `(?d)` prefix is added to allow deletion of ignored directories.
2.  **Verify Sync Speed:** Confirm that excluding `node_modules` keeps the reboot-sync window under 30 seconds.

### Phase 3: Final Verification
1.  **3-Way Test:**
    - Edit file in Windows.
    - Verify sync to Relay.
    - Reboot to Ubuntu.
    - Verify file appears in Ubuntu.

## Documentation
- Detailed Status: `SYNC_STATUS_2026-01-09.md`
- Research Results: `1 I am a software engineer looking for the optimal.md` (Perplexity Research)
- Troubleshooting: `ubuntu-quick-check.sh`