---
resource_id: "cd0e6126-f0ef-45f9-bb29-f138ebe5fbbc"
resource_type: "document"
resource_name: "QUICK_SETUP"
---
# Claude in Chrome WSL Bridge - Quick Setup

<!-- section_id: "473d0172-8a75-4de6-a293-0c05fe7c597d" -->
## TL;DR

Enable Claude in Chrome extension to talk to Claude Code CLI in WSL.

<!-- section_id: "132eab92-e2de-4d59-ad2d-dbc2a813adcc" -->
## Prerequisites

- WSL2 with Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Chrome with Claude in Chrome extension installed
- PowerShell (Administrator access)

<!-- section_id: "0ff6a898-0221-4e24-a3dc-391afe29fd20" -->
## Setup (5 minutes)

<!-- section_id: "e58e7765-cff3-49ee-8bb7-7908f409cac1" -->
### 1. WSL Wrapper (Already Created ✓)

The WSL wrapper script is already created at:
```
/home/dawson/bin/claude-chrome-host.sh
```

<!-- section_id: "a340e087-c1ab-4cd1-b613-e0d4ede732a0" -->
### 2. Windows Batch Script

**Run in PowerShell:**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"

@"
@echo off
wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
"@ | Out-File -FilePath "$env:USERPROFILE\bin\claude-chrome-host.bat" -Encoding ASCII
```

<!-- section_id: "6476c4bb-b0a4-48ef-b4a6-436d8231e57a" -->
### 3. Get Extension ID

1. Open Chrome: `chrome://extensions/`
2. Enable "Developer mode"
3. Find "Claude in Chrome" → copy the ID (32 chars)

<!-- section_id: "202ff6d7-876e-4f7b-a4d1-8d6d9c3c4ba7" -->
### 4. Create Manifest

**Run in PowerShell (replace `YOUR_EXTENSION_ID`):**

```powershell
$extensionId = "YOUR_EXTENSION_ID"
$chromeDir = "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts"
New-Item -ItemType Directory -Force -Path $chromeDir

$batchPath = "$env:USERPROFILE\bin\claude-chrome-host.bat".Replace('\', '\\')

@"
{
  "name": "com.anthropic.claude.chrome",
  "description": "Claude in Chrome native messaging host",
  "path": "$batchPath",
  "type": "stdio",
  "allowed_origins": [
    "chrome-extension://$extensionId/"
  ]
}
"@ | Out-File -FilePath "$chromeDir\com.anthropic.claude.chrome.json" -Encoding UTF8
```

<!-- section_id: "52a1aac0-71f2-4e17-abe4-8cc9041c0368" -->
### 5. Restart Chrome

Close ALL Chrome windows and reopen.

<!-- section_id: "cb786664-912d-42a3-b937-ba7810be6bfd" -->
## Test It

Open Chrome extension and try using it. Check DevTools console for errors.

<!-- section_id: "1be7455e-0ecb-48f3-9582-a564fc110efb" -->
## Troubleshooting

<!-- section_id: "6a7e3123-03f9-4e1e-b310-efd2df6bac28" -->
### "Native messaging host not found"

1. Check manifest exists:
   ```powershell
   Get-Content "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json"
   ```

2. Verify extension ID matches

3. Restart Chrome completely

<!-- section_id: "fb5b80a4-912a-40e2-8291-26d1dfd67398" -->
### Enable Debug Logging

**Edit WSL wrapper:** `/home/dawson/bin/claude-chrome-host.sh`

```bash
#!/bin/bash
exec 2>> /home/dawson/claude-chrome-host.log
echo "[$(date)] Starting" >&2

NATIVE_HOST="/home/dawson/.claude/chrome/chrome-native-host"
exec "$NATIVE_HOST"
```

**View logs:**
```bash
tail -f ~/claude-chrome-host.log
```

<!-- section_id: "403c2a47-1393-4a68-b4d6-c49c308ad505" -->
## Files Created

| Location | File |
|----------|------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` |

<!-- section_id: "fd836c4d-d0b0-433f-a760-94d630f63960" -->
## Full Documentation

See `BATCH_BRIDGE_SETUP.md` for complete details, troubleshooting, and advanced configuration.

<!-- section_id: "780e5a36-ad05-47bd-be36-939328d433ee" -->
## Automated Setup

Save and run this PowerShell script for automated setup:

```powershell
# Get extension ID
$extensionId = Read-Host "Enter Claude in Chrome extension ID (from chrome://extensions)"

# Create batch script
$batchDir = "$env:USERPROFILE\bin"
New-Item -ItemType Directory -Force -Path $batchDir
@"
@echo off
wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
"@ | Out-File -FilePath "$batchDir\claude-chrome-host.bat" -Encoding ASCII

# Create manifest
$chromeDir = "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts"
New-Item -ItemType Directory -Force -Path $chromeDir
$batchPath = "$batchDir\claude-chrome-host.bat".Replace('\', '\\')
@"
{
  "name": "com.anthropic.claude.chrome",
  "description": "Claude in Chrome native messaging host",
  "path": "$batchPath",
  "type": "stdio",
  "allowed_origins": ["chrome-extension://$extensionId/"]
}
"@ | Out-File -FilePath "$chromeDir\com.anthropic.claude.chrome.json" -Encoding UTF8

Write-Host "Setup complete! Restart Chrome." -ForegroundColor Green
```
