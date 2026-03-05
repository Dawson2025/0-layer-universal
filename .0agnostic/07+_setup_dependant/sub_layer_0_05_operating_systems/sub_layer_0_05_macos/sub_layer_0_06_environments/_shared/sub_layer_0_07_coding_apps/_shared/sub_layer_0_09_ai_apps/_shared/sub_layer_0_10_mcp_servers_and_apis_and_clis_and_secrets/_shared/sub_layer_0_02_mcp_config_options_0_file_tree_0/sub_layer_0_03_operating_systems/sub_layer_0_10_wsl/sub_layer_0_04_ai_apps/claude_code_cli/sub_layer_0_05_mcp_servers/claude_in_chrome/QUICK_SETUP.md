---
resource_id: "aced8edc-cbee-4cee-8b0e-b79eba324146"
resource_type: "document"
resource_name: "QUICK_SETUP"
---
# Claude in Chrome WSL Bridge - Quick Setup

<!-- section_id: "be8dbdb7-92d0-42e6-893e-bff057598f82" -->
## TL;DR

Enable Claude in Chrome extension to talk to Claude Code CLI in WSL.

<!-- section_id: "6bc580ea-e542-48d6-acf0-39650361ed75" -->
## Prerequisites

- WSL2 with Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Chrome with Claude in Chrome extension installed
- PowerShell (Administrator access)

<!-- section_id: "1161aab7-26dc-490c-939d-4e6f0c4714eb" -->
## Setup (5 minutes)

<!-- section_id: "7493dcde-fc97-4189-9b38-df7514e97428" -->
### 1. WSL Wrapper (Already Created ✓)

The WSL wrapper script is already created at:
```
/home/dawson/bin/claude-chrome-host.sh
```

<!-- section_id: "18c54b43-d282-495c-8714-969d523f2476" -->
### 2. Windows Batch Script

**Run in PowerShell:**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"

@"
@echo off
wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
"@ | Out-File -FilePath "$env:USERPROFILE\bin\claude-chrome-host.bat" -Encoding ASCII
```

<!-- section_id: "dade6fe0-4d83-40d0-9f97-d5f37dbf50e4" -->
### 3. Get Extension ID

1. Open Chrome: `chrome://extensions/`
2. Enable "Developer mode"
3. Find "Claude in Chrome" → copy the ID (32 chars)

<!-- section_id: "2ebcf3da-7762-4c77-b262-84926fe54d6f" -->
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

<!-- section_id: "913ab273-4110-45ed-ba30-ac936ad7ee9d" -->
### 5. Restart Chrome

Close ALL Chrome windows and reopen.

<!-- section_id: "c6acfec8-6e8e-4704-b166-638015a590e6" -->
## Test It

Open Chrome extension and try using it. Check DevTools console for errors.

<!-- section_id: "3b5b3fcf-ba11-4457-925e-177ab563c593" -->
## Troubleshooting

<!-- section_id: "154393d8-96e2-4f18-bd91-ea1e45bfb8a2" -->
### "Native messaging host not found"

1. Check manifest exists:
   ```powershell
   Get-Content "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json"
   ```

2. Verify extension ID matches

3. Restart Chrome completely

<!-- section_id: "3f4bc3bd-3bfe-4b18-8467-f892850e4cc4" -->
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

<!-- section_id: "33c6e377-1ed4-4ce2-9ae3-8fb6e52a5a72" -->
## Files Created

| Location | File |
|----------|------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` |

<!-- section_id: "6f124f4b-5035-4942-856e-8f4bd5ff9352" -->
## Full Documentation

See `BATCH_BRIDGE_SETUP.md` for complete details, troubleshooting, and advanced configuration.

<!-- section_id: "831d55b7-fb4f-46ba-8e88-7f372cc54380" -->
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
