---
resource_id: "56c56eaf-7f99-459b-bed6-1786ce1c3863"
resource_type: "document"
resource_name: "QUICK_SETUP"
---
# Claude in Chrome WSL Bridge - Quick Setup

<!-- section_id: "fe276dd8-515f-4670-a78f-6b01c01a27cd" -->
## TL;DR

Enable Claude in Chrome extension to talk to Claude Code CLI in WSL.

<!-- section_id: "5389186c-bc2b-4bfa-bcae-8d74a976c105" -->
## Prerequisites

- WSL2 with Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Chrome with Claude in Chrome extension installed
- PowerShell (Administrator access)

<!-- section_id: "7c3b92c7-da05-4c7c-98f0-919dd5eed23b" -->
## Setup (5 minutes)

<!-- section_id: "9de61690-2169-461c-885c-bece8f1c106c" -->
### 1. WSL Wrapper (Already Created ✓)

The WSL wrapper script is already created at:
```
/home/dawson/bin/claude-chrome-host.sh
```

<!-- section_id: "c4d17c85-cb3f-46d2-80cd-7f7d99e7d3e3" -->
### 2. Windows Batch Script

**Run in PowerShell:**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"

@"
@echo off
wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
"@ | Out-File -FilePath "$env:USERPROFILE\bin\claude-chrome-host.bat" -Encoding ASCII
```

<!-- section_id: "3fdd0393-6ab4-4f4a-8e98-0202e88adbc7" -->
### 3. Get Extension ID

1. Open Chrome: `chrome://extensions/`
2. Enable "Developer mode"
3. Find "Claude in Chrome" → copy the ID (32 chars)

<!-- section_id: "9691901b-d97d-4472-9069-1ccb3bc3fff7" -->
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

<!-- section_id: "4c3e8a85-4e6b-4786-9ec3-3bae85ba2474" -->
### 5. Restart Chrome

Close ALL Chrome windows and reopen.

<!-- section_id: "03062459-651d-4054-8ffb-e0eb6d5937d7" -->
## Test It

Open Chrome extension and try using it. Check DevTools console for errors.

<!-- section_id: "96de0852-eeb7-465c-9da8-deefbb758dfb" -->
## Troubleshooting

<!-- section_id: "4767addd-97be-4676-9d92-58877b1d3de0" -->
### "Native messaging host not found"

1. Check manifest exists:
   ```powershell
   Get-Content "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json"
   ```

2. Verify extension ID matches

3. Restart Chrome completely

<!-- section_id: "471febd8-70a7-4e25-a40f-b8d06fa9b3ff" -->
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

<!-- section_id: "14fb5f0d-81d2-4720-ad8c-3c06ed13e633" -->
## Files Created

| Location | File |
|----------|------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` |

<!-- section_id: "2bfca8e1-233e-4312-a340-0b18cdbc8d9c" -->
## Full Documentation

See `BATCH_BRIDGE_SETUP.md` for complete details, troubleshooting, and advanced configuration.

<!-- section_id: "a6a2251b-b2b2-409c-9a42-4d93b0f5e5eb" -->
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
