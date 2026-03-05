---
resource_id: "711c9d2c-637f-4024-8020-959aa47092a6"
resource_type: "document"
resource_name: "WSL_STABILITY_FIX"
---
# WSL2 "Catastrophic Failure" & Connection Fix

<!-- section_id: "7d34e707-ecbc-4e2a-978f-a28b2bf55abe" -->
## Problem
WSL2 instances may disconnect unexpectedly or fail to start with "Catastrophic failure" (Error code: `Wsl/Service/E_UNEXPECTED`) when accessed via VS Code / Cursor. This is often caused by the default idle timeout behavior which shuts down the VM after 60 seconds of inactivity (e.g., when the terminal is closed or during a reload).

<!-- section_id: "6a0ce087-3681-4d5f-8a95-79f03c3d0afb" -->
## Solution: Disable Idle Timeout
Configure WSL to stay running indefinitely and manage memory dynamically.

<!-- section_id: "672d9064-bca6-440a-a32c-760d508abffc" -->
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

<!-- section_id: "52742127-b5e5-47ff-bafe-20fa9e8bc37c" -->
### 2. Restart WSL
Apply the changes by shutting down WSL completely:

```powershell
wsl --shutdown
```

Then restart it by opening a new terminal.

<!-- section_id: "deb312c6-33bc-4f52-a30b-46543c9db54d" -->
## Verification
This ensures the WSL instance remains active even when no interactive shells are open, preventing connection drops during IDE reloads or background tasks.
