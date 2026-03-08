---
resource_id: "255e1bd3-90c5-4498-a3be-85b1951709e0"
resource_type: "readme_document"
resource_name: "README"
---
# Claude in Chrome Extension Integration

This directory contains setup and configuration for integrating the **Claude in Chrome** browser extension with **Claude Code CLI** running in WSL.

<!-- section_id: "9cc11d89-3b95-491a-92f9-046a5ce1a25a" -->
## Documentation

- **[QUICK_SETUP.md](QUICK_SETUP.md)** - Fast 5-minute setup guide (start here!)
- **[BATCH_BRIDGE_SETUP.md](BATCH_BRIDGE_SETUP.md)** - Complete detailed guide with troubleshooting
- **[SETUP_FINDINGS.md](SETUP_FINDINGS.md)** - Research and findings about the integration

<!-- section_id: "cc513de5-0fc3-41de-b6f6-71fcd5770cf2" -->
## What This Does

Enables the Chrome extension running on Windows to communicate with Claude Code CLI running in WSL via a Native Messaging bridge.

```
Chrome Extension (Windows)
        ↓
Windows Batch Script
        ↓
WSL Bash Wrapper
        ↓
Claude Code Native Host
        ↓
Claude Code CLI (WSL)
```

<!-- section_id: "b115b834-9328-40bf-a257-0557193a7b2d" -->
## Quick Start

1. Make sure WSL wrapper exists: `/home/dawson/bin/claude-chrome-host.sh` ✓ (already created)
2. Follow **[QUICK_SETUP.md](QUICK_SETUP.md)** to create Windows components
3. Restart Chrome
4. Test the extension

<!-- section_id: "889a351d-468a-4bc8-ae6f-9dec909af5c1" -->
## Status

- ✓ WSL wrapper script created and executable
- ✓ Native messaging host verified (`~/.claude/chrome/chrome-native-host`)
- ⏳ Windows batch script (needs manual creation - see QUICK_SETUP.md)
- ⏳ Native messaging manifest (needs manual creation - see QUICK_SETUP.md)
- ⏳ Extension ID configuration (needs user's extension ID)

<!-- section_id: "1492d474-223c-46a6-80f5-e8bc5def2339" -->
## Key Files

| Location | File | Status |
|----------|------|--------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` | ✓ Created |
| WSL | `/home/dawson/.claude/chrome/chrome-native-host` | ✓ Exists |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` | ⏳ Create manually |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` | ⏳ Create manually |

<!-- section_id: "0a556391-2f15-4af0-b176-e981d4a1cb9e" -->
## Support

- See [BATCH_BRIDGE_SETUP.md](BATCH_BRIDGE_SETUP.md) for detailed troubleshooting
- Check Claude Code issues: https://github.com/anthropics/claude-code/issues
- Chrome Native Messaging docs: https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging

<!-- section_id: "5ee52f26-ddec-46fd-b136-ba377c104a86" -->
## Version

Last updated: 2025-12-30
Claude Code version: 2.0.76
