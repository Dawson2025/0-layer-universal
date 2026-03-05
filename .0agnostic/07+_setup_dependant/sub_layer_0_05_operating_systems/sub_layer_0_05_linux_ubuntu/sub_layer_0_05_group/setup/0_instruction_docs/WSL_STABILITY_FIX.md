---
resource_id: "a6286f0b-6562-4e5e-9dfa-bd83ff07d7e3"
resource_type: "document"
resource_name: "WSL_STABILITY_FIX"
---
# WSL2 "Catastrophic Failure" & Connection Fix

<!-- section_id: "6d39893e-d47d-4cbf-8d5f-35260719b043" -->
## Problem
WSL2 instances may disconnect unexpectedly or fail to start with "Catastrophic failure" (Error code: `Wsl/Service/E_UNEXPECTED`) when accessed via VS Code / Cursor. This is often caused by the default idle timeout behavior which shuts down the VM after 60 seconds of inactivity (e.g., when the terminal is closed or during a reload).

<!-- section_id: "6ef2bad3-9843-41c4-876f-8073d27d0894" -->
## Solution: Disable Idle Timeout
Configure WSL to stay running indefinitely and manage memory dynamically.

<!-- section_id: "c88a8bec-e59d-4b73-8f62-8764f92f2572" -->
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

<!-- section_id: "d1fa6b62-e6b8-45d8-932a-8c5803909882" -->
### 2. Restart WSL
Apply the changes by shutting down WSL completely:

```powershell
wsl --shutdown
```

Then restart it by opening a new terminal.

<!-- section_id: "b02198f7-26c0-4996-aeef-ada3c29d5f61" -->
## Verification
This ensures the WSL instance remains active even when no interactive shells are open, preventing connection drops during IDE reloads or background tasks.
