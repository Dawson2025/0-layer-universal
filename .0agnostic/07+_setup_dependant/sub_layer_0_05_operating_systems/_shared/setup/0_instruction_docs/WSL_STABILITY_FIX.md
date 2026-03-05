---
resource_id: "4a6d0cc8-6252-4d69-bc8a-3cb22e4569ca"
resource_type: "document"
resource_name: "WSL_STABILITY_FIX"
---
# WSL2 "Catastrophic Failure" & Connection Fix

<!-- section_id: "de471d46-16e4-45e0-b1d4-fcbef90a82ef" -->
## Problem
WSL2 instances may disconnect unexpectedly or fail to start with "Catastrophic failure" (Error code: `Wsl/Service/E_UNEXPECTED`) when accessed via VS Code / Cursor. This is often caused by the default idle timeout behavior which shuts down the VM after 60 seconds of inactivity (e.g., when the terminal is closed or during a reload).

<!-- section_id: "7704e80c-3a69-4888-80ef-ea2e4330a019" -->
## Solution: Disable Idle Timeout
Configure WSL to stay running indefinitely and manage memory dynamically.

<!-- section_id: "e2ca0407-eb5e-4c92-a643-d5ec194bbf82" -->
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

<!-- section_id: "63952229-9269-4e9e-b675-6cc37ef52833" -->
### 2. Restart WSL
Apply the changes by shutting down WSL completely:

```powershell
wsl --shutdown
```

Then restart it by opening a new terminal.

<!-- section_id: "115d1984-d0fb-4287-a26c-3d334ef64a84" -->
## Verification
This ensures the WSL instance remains active even when no interactive shells are open, preventing connection drops during IDE reloads or background tasks.
