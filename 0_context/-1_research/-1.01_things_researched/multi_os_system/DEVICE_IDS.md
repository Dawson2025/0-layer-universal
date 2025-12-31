# Syncthing Device IDs

This document contains the device IDs for all three systems in the multi-OS workspace sync.

## Device IDs

### WSL (Canonical Origin)
- **Device Name**: WSL-Dawson
- **Device ID**: IF2WOGZ-RVSVKT3-RCRN3TT-6NDFXQX-KCCCFPW-ABIWRWT-3BFX37C-CDHKTAN
- **Path**: /home/dawson/dawson-workspace
- **Status**: ✅ Active and syncing

### Windows
- **Device Name**: Win-Dawson
- **Device ID**: Check Windows Syncthing web UI (Actions → Show ID) and fill in here
- **Path**: C:\Users\Dawson\dawson-workspace
- **Status**: ✅ Active and syncing

### Ubuntu Desktop
- **Device Name**: Ubuntu-Dawson
- **Device ID**: ______________ (fill this in during Ubuntu setup - step 5.2)
- **Path**: /home/dawson/dawson-workspace
- **Status**: ⏳ Pending setup

## How to Find Your Device ID

### From Web UI
1. Open Syncthing web UI: http://localhost:8384
2. Click **Actions** (top right)
3. Click **Show ID**
4. Copy the device ID

### From Command Line
On Linux (WSL or Ubuntu):
PKA5NY2-47573F4-SAHSF6Z-3UXFJCU-AEFHZKL-WKVIHVA-OBF4M2V-5P7AXAE

## Adding Devices

When setting up a new device, you need to:
1. Get the new device ID (see above)
2. On each existing device:
   - Open http://localhost:8384
   - Click **Add Remote Device**
   - Paste the new device ID
   - Give it a descriptive name (e.g., Ubuntu-Dawson)
   - Click **Save**
3. On the new device:
   - Accept any folder share requests
   - Set folder type to **Send & Receive**

## Connection Status

All devices should show as **Connected** in the Syncthing web UI when they are online and on the same network (or have port 22000 accessible).

---
Last updated: 2025-12-31
