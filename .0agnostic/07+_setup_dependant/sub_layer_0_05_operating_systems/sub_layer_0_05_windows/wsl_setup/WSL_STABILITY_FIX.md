---
resource_id: "285e4edc-bdef-4aee-aded-f21e25f2c167"
resource_type: "document"
resource_name: "WSL_STABILITY_FIX"
---
# WSL2 "Catastrophic Failure" & Connection Fix

<!-- section_id: "98869a2c-14aa-4c2b-8b92-eed69682a7cd" -->
## Problem
WSL2 instances may disconnect unexpectedly or fail to start with "Catastrophic failure" (Error code: `Wsl/Service/E_UNEXPECTED`) when accessed via VS Code / Cursor. This is often caused by the default idle timeout behavior which shuts down the VM after 60 seconds of inactivity (e.g., when the terminal is closed or during a reload).

<!-- section_id: "399e7fd2-2ad1-4167-8879-db67e2bff126" -->
## Solution: Disable Idle Timeout
Configure WSL to stay running indefinitely and manage memory dynamically.

<!-- section_id: "90eba924-20fb-44ea-948b-a0a174c44559" -->
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

<!-- section_id: "687e4a65-0b5b-4a0f-adfd-cad04e9f8b2d" -->
### 2. Restart WSL
Apply the changes by shutting down WSL completely:

```powershell
wsl --shutdown
```

Then restart it by opening a new terminal.

<!-- section_id: "6a3fc21a-9d98-46de-8f99-efac07333ffe" -->
## Verification
This ensures the WSL instance remains active even when no interactive shells are open, preventing connection drops during IDE reloads or background tasks.
