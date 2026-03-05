---
resource_id: "cb660b8d-7531-448b-9bc7-1fed52992be2"
resource_type: "document"
resource_name: "WSL_STABILITY_FIX"
---
# WSL2 "Catastrophic Failure" & Connection Fix

<!-- section_id: "da79084a-36a2-496d-8fa1-2b470e517b8d" -->
## Problem
WSL2 instances may disconnect unexpectedly or fail to start with "Catastrophic failure" (Error code: `Wsl/Service/E_UNEXPECTED`) when accessed via VS Code / Cursor. This is often caused by the default idle timeout behavior which shuts down the VM after 60 seconds of inactivity (e.g., when the terminal is closed or during a reload).

<!-- section_id: "a6bdce80-481f-4f48-9f2d-d834ff01da11" -->
## Solution: Disable Idle Timeout
Configure WSL to stay running indefinitely and manage memory dynamically.

<!-- section_id: "5c2d6767-a2a8-49d1-8eba-2583917b27d2" -->
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

<!-- section_id: "92e954d4-ebc5-459c-8658-709e63011394" -->
### 2. Restart WSL
Apply the changes by shutting down WSL completely:

```powershell
wsl --shutdown
```

Then restart it by opening a new terminal.

<!-- section_id: "13152bb9-389a-42a5-9071-f051da699a9b" -->
## Verification
This ensures the WSL instance remains active even when no interactive shells are open, preventing connection drops during IDE reloads or background tasks.
