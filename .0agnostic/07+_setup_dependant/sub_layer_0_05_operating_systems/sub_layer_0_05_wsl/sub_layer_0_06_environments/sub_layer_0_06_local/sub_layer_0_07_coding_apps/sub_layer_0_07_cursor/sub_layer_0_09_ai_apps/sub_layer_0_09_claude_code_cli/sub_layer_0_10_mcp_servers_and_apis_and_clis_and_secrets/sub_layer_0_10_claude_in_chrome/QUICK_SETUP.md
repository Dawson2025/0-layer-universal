---
resource_id: "06b27870-b833-4d2c-befa-9cca77908759"
resource_type: "document"
resource_name: "QUICK_SETUP"
---
# Claude in Chrome WSL Bridge - Quick Setup

## TL;DR

Enable Claude in Chrome extension to talk to Claude Code CLI in WSL.

## Prerequisites

- WSL2 with Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Chrome with Claude in Chrome extension installed
- PowerShell (Administrator access)

## Setup (5 minutes)

### 1. WSL Wrapper (Already Created ✓)

The WSL wrapper script is already created at:
```
/home/dawson/bin/claude-chrome-host.sh
```

### 2. Windows Batch Script

**Run in PowerShell:**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"

@"
@echo off
wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
"@ | Out-File -FilePath "$env:USERPROFILE\bin\claude-chrome-host.bat" -Encoding ASCII
```

### 3. Get Extension ID

1. Open Chrome: `chrome://extensions/`
2. Enable "Developer mode"
3. Find "Claude in Chrome" → copy the ID (32 chars)

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

### 5. Restart Chrome

Close ALL Chrome windows and reopen.

## Test It

Open Chrome extension and try using it. Check DevTools console for errors.

## Troubleshooting

### "Native messaging host not found"

1. Check manifest exists:
   ```powershell
   Get-Content "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json"
   ```

2. Verify extension ID matches

3. Restart Chrome completely

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

## Files Created

| Location | File |
|----------|------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` |

## Full Documentation

See `BATCH_BRIDGE_SETUP.md` for complete details, troubleshooting, and advanced configuration.

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
