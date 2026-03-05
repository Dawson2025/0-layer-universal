---
resource_id: "3d335b01-feef-4ca0-a598-dcaee78b716a"
resource_type: "knowledge"
resource_name: "DUAL_BOOT_TEST_INSTRUCTIONS"
---
# Dual Boot Sync Test Instructions

**Last Updated:** 2026-01-12 00:10 MST (from Windows)
**Status:** Awaiting Ubuntu verification of Windows → Ubuntu sync

---

<!-- section_id: "69204118-974f-4995-8635-3689ac063a0b" -->
## Current Verification Status

| Test | Direction | Status |
| :--- | :--- | :--- |
| Test 1 | Ubuntu → VPS → Windows | ✅ **VERIFIED** (2026-01-12) |
| Test 2 | Windows → VPS → Ubuntu | ⏳ **Pending** |

---

<!-- section_id: "14979c60-0665-42b1-afc4-662f86a0a7ad" -->
## Test Files

| File | Created | Location | Purpose |
| :--- | :--- | :--- | :--- |
| `SYNC_TEST_UBUNTU_TO_WINDOWS.md` | Ubuntu 2026-01-11 | dawson-workspace root | Verify Ubuntu → Windows |
| `SYNC_TEST_WINDOWS_TO_UBUNTU.md` | Windows 2026-01-12 | dawson-workspace root | Verify Windows → Ubuntu |

---

<!-- section_id: "c49e83b1-c72d-4c2d-9c92-3990efe0632d" -->
## FOR UBUNTU AGENTS: Complete Verification

When the user boots into Ubuntu, follow these steps:

<!-- section_id: "baae0194-7f2a-494e-a3f3-ab90d379e656" -->
### Quick Check (Run This First)

```bash
# One-liner to check if sync worked
[ -f ~/dawson-workspace/SYNC_TEST_WINDOWS_TO_UBUNTU.md ] && echo "✅ SYNC VERIFIED!" || echo "❌ File not found"
```

<!-- section_id: "c132d34e-1610-4fc6-aff0-077054569cf5" -->
### Step-by-Step Verification

#### 1. Ensure Syncthing is Running
```bash
systemctl --user status syncthing
# If not active, start it:
systemctl --user start syncthing
```

#### 2. Wait for Sync to Complete
Give Syncthing a minute to connect to VPS and sync. You can monitor:
```bash
# Watch Syncthing logs
journalctl --user -u syncthing -f
```

Or open the GUI at http://localhost:8384 and check:
- Hetzner-VPS shows connected (green)
- dawson-workspace shows "Up to Date"

#### 3. Verify the Test File Exists
```bash
ls -la ~/dawson-workspace/SYNC_TEST_WINDOWS_TO_UBUNTU.md
```

#### 4. Read the Test File
```bash
cat ~/dawson-workspace/SYNC_TEST_WINDOWS_TO_UBUNTU.md
```

**Expected content:**
- Created on Windows on 2026-01-12
- Contains sync test information
- Mentions "Windows → VPS → Ubuntu sync workflow"

#### 5. If File Exists: Update Documentation

Edit `STATUS.md` in this directory:
```bash
nano ~/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/multi_os_system/STATUS.md
```

Update:
1. Change "Windows → VPS → Ubuntu" row to: `✅ **VERIFIED WORKING** | 2026-01-12`
2. Add log entry: `- **2026-01-12 XX:XX:** ✅ Ubuntu verification complete. Windows → Ubuntu sync confirmed working.`

Then commit:
```bash
cd ~/dawson-workspace/code/0_layer_universal
git add -A
git commit -m "Verify Windows → Ubuntu sync working - bidirectional sync complete"
git push
```

---

<!-- section_id: "04730883-5aa9-4183-802e-500ddea98e34" -->
## Sync Flow Diagram

```
Test 1 (VERIFIED):
┌──────────┐         ┌─────────┐         ┌─────────┐
│  Ubuntu  │────────>│   VPS   │────────>│ Windows │
│ (Create) │  Sync   │ (Relay) │  Sync   │ (Read)  │
└──────────┘         └─────────┘         └─────────┘
     ✅                  ✅                  ✅

Test 2 (PENDING):
┌──────────┐         ┌─────────┐         ┌─────────┐
│ Windows  │────────>│   VPS   │────────>│ Ubuntu  │
│ (Create) │  Sync   │ (Relay) │  Sync   │ (Read)  │
└──────────┘         └─────────┘         └─────────┘
     ✅                  ✅                  ⏳
```

---

<!-- section_id: "ada850f2-77db-40c5-91a1-56e5fbc3f423" -->
## Troubleshooting

<!-- section_id: "e3c1f13d-5c44-4d9e-8991-e327cb51e04c" -->
### File doesn't appear after booting Ubuntu

1. **Check Syncthing is running:**
   ```bash
   systemctl --user status syncthing
   ```

2. **Check VPS connection:**
   ```bash
   curl -s http://localhost:8384/rest/system/connections 2>/dev/null | grep -o '"connected":[^,]*' | head -3
   ```

3. **Force a folder rescan:**
   ```bash
   curl -X POST "http://localhost:8384/rest/db/scan?folder=dawson-workspace"
   ```

4. **Check if file is on VPS:**
   ```bash
   ssh -i ~/.ssh/id_ed25519 root@46.224.184.10 "ls -la /root/sync/dawson-workspace/SYNC_TEST_WINDOWS_TO_UBUNTU.md"
   ```

5. **Check .stignore isn't blocking:**
   ```bash
   cat ~/dawson-workspace/.stignore | grep -i sync
   ```

<!-- section_id: "e884b4f6-766d-482a-9e68-a6655c44e838" -->
### Syncthing won't connect to VPS

1. Check internet connectivity
2. Verify VPS is reachable: `ping 46.224.184.10`
3. Check firewall allows port 22000
4. Verify device IDs are correct in Syncthing GUI

---

<!-- section_id: "75e1cc15-1186-4f39-a6c1-c158daa307ee" -->
## Success Criteria

When both tests pass:
- ✅ Ubuntu → VPS → Windows sync works automatically
- ✅ Windows → VPS → Ubuntu sync works automatically
- ✅ No manual intervention required
- ✅ Files appear within minutes of booting the other OS
- ✅ The multi-OS workspace sync project is COMPLETE

---

<!-- section_id: "c735565e-4e07-4e1d-b848-790bd3a9c069" -->
## What Happens Next

Once both directions are verified:
1. The dual boot sync system is fully operational
2. You can work on either OS and changes will sync via VPS
3. Consider setting up Syncthing to start automatically on boot (if not already)
4. Monitor Oracle Cloud ticket for potential free tier migration
