---
resource_id: "1d1ed4c0-98ec-4a31-b5a2-bbdcb75712eb"
resource_type: "document"
resource_name: "WSL_STABILITY_FIX"
---
# WSL2 "Catastrophic Failure" & Connection Fix

## Problem
WSL2 instances may disconnect unexpectedly or fail to start with "Catastrophic failure" (Error code: `Wsl/Service/E_UNEXPECTED`) when accessed via VS Code / Cursor. This is often caused by the default idle timeout behavior which shuts down the VM after 60 seconds of inactivity (e.g., when the terminal is closed or during a reload).

## Solution: Disable Idle Timeout
Configure WSL to stay running indefinitely and manage memory dynamically.

### 1. Create/Edit `.wslconfig`
Create or edit the file at `%USERPROFILE%\.wslconfig` (Windows path, e.g., `C:\Users\YourUser\.wslconfig`).

**Add the following configuration:**

```ini
[wsl2]
# Disable automatic shutdown (default is 60000ms / 60s)
vmIdleTimeout=-1

[experimental]
# Gradually reclaim unused memory instead of shutting down
autoMemoryReclaim=gradual
```

### 2. Restart WSL
Apply the changes by shutting down WSL completely:

```powershell
wsl --shutdown
```

Then restart it by opening a new terminal.

## Verification
This ensures the WSL instance remains active even when no interactive shells are open, preventing connection drops during IDE reloads or background tasks.
