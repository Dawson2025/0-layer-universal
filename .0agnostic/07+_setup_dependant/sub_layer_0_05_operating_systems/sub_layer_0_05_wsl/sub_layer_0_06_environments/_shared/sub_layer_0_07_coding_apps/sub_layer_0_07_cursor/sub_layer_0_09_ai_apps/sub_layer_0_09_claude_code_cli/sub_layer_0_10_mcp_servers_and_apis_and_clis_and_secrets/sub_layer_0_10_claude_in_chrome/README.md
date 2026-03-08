---
resource_id: "86ebae61-d57f-44cf-b521-2ecb28a5cb9d"
resource_type: "readme_document"
resource_name: "README"
---
# Claude in Chrome Extension Integration

This directory contains setup and configuration for integrating the **Claude in Chrome** browser extension with **Claude Code CLI** running in WSL.

<!-- section_id: "4cf3d7ab-d638-4a63-8ea6-0861f69d7760" -->
## Documentation

- **[QUICK_SETUP.md](QUICK_SETUP.md)** - Fast 5-minute setup guide (start here!)
- **[BATCH_BRIDGE_SETUP.md](BATCH_BRIDGE_SETUP.md)** - Complete detailed guide with troubleshooting
- **[SETUP_FINDINGS.md](SETUP_FINDINGS.md)** - Research and findings about the integration

<!-- section_id: "7a3acfb0-3a54-4f85-967e-1201c57fd3e7" -->
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

<!-- section_id: "b1e2e958-6831-4d31-b8de-d28a7f70a02c" -->
## Quick Start

1. Make sure WSL wrapper exists: `/home/dawson/bin/claude-chrome-host.sh` ✓ (already created)
2. Follow **[QUICK_SETUP.md](QUICK_SETUP.md)** to create Windows components
3. Restart Chrome
4. Test the extension

<!-- section_id: "1624416d-ba9d-4ba4-a148-a0f7b3ddf077" -->
## Status

- ✓ WSL wrapper script created and executable
- ✓ Native messaging host verified (`~/.claude/chrome/chrome-native-host`)
- ⏳ Windows batch script (needs manual creation - see QUICK_SETUP.md)
- ⏳ Native messaging manifest (needs manual creation - see QUICK_SETUP.md)
- ⏳ Extension ID configuration (needs user's extension ID)

<!-- section_id: "a163d92a-1edc-4612-a1fd-5aa28cd80528" -->
## Key Files

| Location | File | Status |
|----------|------|--------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` | ✓ Created |
| WSL | `/home/dawson/.claude/chrome/chrome-native-host` | ✓ Exists |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` | ⏳ Create manually |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` | ⏳ Create manually |

<!-- section_id: "d84b1256-a240-40e5-9d4b-52f2fade5f3b" -->
## Support

- See [BATCH_BRIDGE_SETUP.md](BATCH_BRIDGE_SETUP.md) for detailed troubleshooting
- Check Claude Code issues: https://github.com/anthropics/claude-code/issues
- Chrome Native Messaging docs: https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging

<!-- section_id: "77152d5e-bc7d-4307-8dd8-8103aa78b488" -->
## Version

Last updated: 2025-12-30
Claude Code version: 2.0.76
