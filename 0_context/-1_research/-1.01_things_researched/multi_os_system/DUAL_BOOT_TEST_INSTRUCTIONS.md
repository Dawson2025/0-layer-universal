# Dual Boot Sync Test Instructions

**Date:** 2026-01-11 14:11 MST
**Status:** Ready to test Windows → VPS → Ubuntu sync

## What We Just Did (Ubuntu Side)

1. ✅ Opened Syncthing GUI at http://localhost:8384
2. ✅ Verified connection to Hetzner-VPS (IPv6 TLS 1.3)
3. ✅ Created test file: `SYNC_TEST_UBUNTU_TO_WINDOWS.md`
4. ✅ Verified file synced to VPS (confirmed via VPS API)

## Test File Location

**File:** `SYNC_TEST_UBUNTU_TO_WINDOWS.md`
- **Ubuntu path:** `/home/dawson/dawson-workspace/SYNC_TEST_UBUNTU_TO_WINDOWS.md`
- **VPS path:** `/root/sync/dawson-workspace/SYNC_TEST_UBUNTU_TO_WINDOWS.md`
- **Windows path (expected):** `C:\Users\<username>\dawson-workspace\SYNC_TEST_UBUNTU_TO_WINDOWS.md`
- **Size:** 1,013 bytes
- **Status:** ✅ Already on VPS

## Next Steps: Reboot to Windows

When you reboot to Windows, follow these steps:

### 1. Verify Syncthing is Running
```powershell
# Check if Syncthing process is running
Get-Process syncthing

# Open Syncthing GUI
Start-Process "http://localhost:8384"
```

### 2. Check VPS Connection
In the Syncthing GUI:
- Look for "Hetzner-VPS" under Remote Devices
- Should show green checkmark (connected)
- Check that it says "Up to Date" or "Syncing"

### 3. Verify Test File Appears
Open File Explorer and navigate to:
```
C:\Users\<username>\dawson-workspace\
```

Look for the file:
```
SYNC_TEST_UBUNTU_TO_WINDOWS.md
```

If you can see and open this file, the dual boot sync is working! ✅

### 4. Create a Reverse Test (Optional)

To test Windows → Ubuntu sync:

1. Create a new file in Windows: `SYNC_TEST_WINDOWS_TO_UBUNTU.md`
2. Add some content with timestamp
3. Wait for it to sync to VPS (watch Syncthing GUI)
4. Reboot back to Ubuntu
5. Check if file appears in `/home/dawson/dawson-workspace/`

## Expected Sync Flow

```
┌──────────┐         ┌─────────┐         ┌─────────┐
│  Ubuntu  │────────>│   VPS   │────────>│ Windows │
│ (Create) │  Upload │ (Relay) │Download │ (Read)  │
└──────────┘         └─────────┘         └─────────┘
     │                                         │
     │             Dual Boot System            │
     │          (Never online together)        │
     └─────────────────────────────────────────┘
```

## Troubleshooting

### If file doesn't appear in Windows:

1. **Check Syncthing is running:**
   - Open Task Manager → Look for "syncthing.exe"
   - If not running, start it manually

2. **Check VPS connection:**
   - Open http://localhost:8384
   - Remote Devices → Hetzner-VPS should be green
   - If disconnected, check internet connection

3. **Check folder status:**
   - In Syncthing GUI, click on "dawson-workspace" folder
   - Should show "Up to Date" or "Syncing"
   - If paused, click Resume

4. **Force rescan:**
   - In Syncthing GUI, folder actions → Rescan
   - Or click "Rescan All" button

5. **Check firewall:**
   - Ensure Windows Firewall allows Syncthing
   - Port 22000 should be allowed

## Success Criteria

✅ Syncthing connects to VPS automatically on Windows boot
✅ Test file appears in Windows dawson-workspace folder
✅ File content matches what was created in Ubuntu
✅ No manual intervention required (automatic sync)

## Current Sync Status (at time of test creation)

**Ubuntu:**
- Connection: VPS via IPv6 TLS 1.3 ✓
- Download rate: 2.66 MiB/s
- Overall sync: 60% complete (initial large sync still in progress)
- Test file: Uploaded to VPS ✓

**VPS:**
- Ubuntu device: Connected ✓
- Windows device: Will connect when Windows boots
- Test file: Present on VPS ✓

**Windows:**
- Status: Not running (Ubuntu is currently active)
- Expected: Will connect when booted

---

**Last Updated:** 2026-01-11 14:11 MST (from Ubuntu)
