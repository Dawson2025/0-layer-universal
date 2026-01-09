# Status: Multi-OS Workspace Sync

## System Health (2026-01-09)

| Device | Status | Sync Mode | Notes |
| :--- | :--- | :--- | :--- |
| **WSL** | 🟢 Running | Send & Receive | Canonical source |
| **Windows** | 🟢 Running | Send & Receive | 1,022 "failed" items (ignored dirs) |
| **Ubuntu** | 🟡 Running | Send & Receive | **Connectivity Issue - Disconnected** |

## Critical Issue: Ubuntu Connection Failure

The Ubuntu device (`7UVVQQS...`) is online and local configuration is correct, but it cannot see the WSL device (`IF2WOGZ...`).

**Reported by Ubuntu Agent (2026-01-09):**
- Syncthing service is active.
- Device ID is correct.
- Folder path is correct.
- **Problem:** Connection status to WSL is "Disconnected" (Never seen).

## Instructions for WSL Agent

When you start in WSL, your **priority #1** is to establish the connection to Ubuntu.

### 1. Check WSL Syncthing Status
```bash
systemctl --user status syncthing
```

### 2. Verify Ubuntu Device is Added on WSL
Open the web UI (`http://localhost:8384`) or use the API:
```bash
API_KEY=$(cat ~/.config/syncthing/config.xml | grep -oP '(?<=<apikey>)[^<]+')
curl -s -X GET -H "X-API-Key: $API_KEY" http://localhost:8384/rest/config/devices | grep "7UVVQQS"
```

### 3. If missing, Add Ubuntu Device
Run the helper script (if available on your local disk):
```bash
cd ~/dawson-workspace
./add-ubuntu-to-wsl-syncthing.sh
```

### 4. If added but disconnected, Debug Network
- Ensure both are on the same local network or Global Discovery is enabled.
- Check firewall on Windows/WSL for port 22000 (TCP/UDP).
- Try adding the Ubuntu IP address manually in WSL Syncthing device settings if dynamic discovery fails.

## Pending Verification (After Connection)
1. Verify `dawson-workspace` folder starts syncing (expect ~1.5GB).
2. Confirm 100% completion.
3. Perform Three-Way Sync Test (see `NEXT_STEPS.md`).