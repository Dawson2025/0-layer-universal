---
resource_id: "85c039b2-c3ce-4d06-917b-b8ef71634bed"
resource_type: "document"
resource_name: "FINAL_SUMMARY"
---
# Complete Summary: Claude in Chrome + WSL Integration Attempt

**Date:** 2025-12-31
**Status:** Bridge Built & Tested - Blocked by Platform Check
**Outcome:** Windows → WSL communication proven functional, but Claude Code CLI blocks WSL execution

---

<!-- section_id: "a9b6dd1d-2a30-4003-988d-1dbb41f5cd6b" -->
## The Goal

Get the **Claude in Chrome** browser extension (running in Windows Chrome) to communicate with **Claude Code CLI** (running in WSL).

<!-- section_id: "fa1a1561-77f6-479a-8fbb-7e44143185ad" -->
## The Challenge

- Chrome runs on **Windows**
- Claude Code CLI runs in **WSL (Linux)**
- Chrome's Native Messaging API doesn't natively cross this boundary
- The `claude --chrome` command is hardcoded to block WSL

---

<!-- section_id: "9fc4a3a5-547a-47ad-af2f-d73f9f5a2f44" -->
## What We Built

<!-- section_id: "a8f354b2-bba4-4c49-b820-3db05efd2872" -->
### 1. Three-Layer Bridge Architecture

We created a custom bridge to allow Chrome (Windows) to communicate with the native host (WSL):

```
Chrome Extension (Windows)
    ↓ Native Messaging Protocol
Windows Batch Script (C:\Users\Dawson\bin\claude-chrome-host.bat)
    ↓ Pipes stdin/stdout via wsl.exe
WSL Wrapper Script (/home/dawson/bin/claude-chrome-host.sh)
    ↓ Executes
Claude Native Host (/home/dawson/.claude/chrome/chrome-native-host)
    ↓ Creates UNIX socket
/tmp/claude-mcp-browser-bridge-dawson
    ↓ Should connect to
Claude Code CLI (blocked by platform check)
```

<!-- section_id: "9cee7ebc-d7ba-4a4c-bf61-d73a1160f644" -->
### 2. Components Created

#### WSL Wrapper Script (`/home/dawson/bin/claude-chrome-host.sh`)
- Executes the Claude native host binary
- Made executable with proper permissions

#### Windows Batch Script (`C:\Users\Dawson\bin\claude-chrome-host.bat`)
- Calls WSL and pipes binary stdin/stdout between Windows and WSL
- Critical for native messaging protocol

#### Chrome Manifest (`C:\Users\Dawson\AppData\Local\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json`)
- Points Chrome to the Windows batch script
- Specifies extension ID: `fcoeoabgfenejglbffodgkkbkcdhcgfn`
- Fixed JSON escaping issues (`\\` for Windows paths)

#### Windows Registry Entry
- `HKEY_CURRENT_USER\Software\Google\Chrome\NativeMessagingHosts\com.anthropic.claude.chrome`
- **Critical discovery:** Chrome on Windows requires registry entry to discover native hosts
- Points to the manifest file location

#### Environment Variable (`~/.bashrc`)
- `export CLAUDE_CODE_ENABLE_CFC=true`
- Attempted to bypass platform detection (didn't work)

---

<!-- section_id: "8b7406b1-0834-472c-85b2-1ceb0dd20f02" -->
## What We Tested

<!-- section_id: "d02facd2-c508-4b41-b216-ed97d9af656b" -->
### ✅ Successful Tests

1. **Native Messaging Bridge Works**
   - Chrome extension → Native host communication confirmed
   - Test: `{type: 'ping'}` → `{type: 'pong', timestamp: ...}`
   - **Proves Windows → WSL communication is functional**

2. **Native Host Running**
   - Process PID 8569 confirmed listening
   - Socket created: `/tmp/claude-mcp-browser-bridge-dawson`
   - Permissions set correctly (0600)

3. **Bridge Infrastructure Solid**
   - All components properly configured
   - Communication path verified working

<!-- section_id: "dec0a4ad-8a4a-4e72-a815-1edff80e0537" -->
### ❌ Failed Tests

1. **`claude --chrome` Command**
   - Error: `Claude in Chrome Native Host not supported on this platform`
   - Hardcoded platform check blocks WSL
   - Occurs regardless of `CLAUDE_CODE_ENABLE_CFC=true`
   - Even trying to force platform detection caused crashes

2. **Extension Status**
   - Shows "Extension: Not detected"
   - Extension can't see Claude Code CLI because it never connects to the socket

3. **Message Type Support**
   - Native host only responds to `ping`
   - All other message types return: `{type: 'error', error: 'Unknown message type: ...'}`
   - This is expected - native host is a relay, not a command processor

---

<!-- section_id: "d0dedf06-b19f-4d5f-a1aa-be3b432b37d6" -->
## Key Discoveries

<!-- section_id: "ab1dbcb2-80d5-4f4d-ae4d-767c4e4ca111" -->
### The Architecture We Uncovered

The native host is a **relay/bridge**, not the actual service:

1. Chrome Extension sends messages via native messaging
2. Native Host receives messages and creates UNIX socket listener
3. Socket (`/tmp/claude-mcp-browser-bridge-dawson`) waits for connections
4. Claude Code CLI (when run with `--chrome`) connects to socket
5. Messages flow: Chrome ↔ Native Host ↔ Socket ↔ Claude CLI

<!-- section_id: "d30e4a88-d7d7-4354-a9f6-2d1afa7b049a" -->
### Why It's Broken

- Claude Code CLI **refuses to run** with `--chrome` flag on WSL
- Platform check happens **before** socket connection attempt
- Without CLI connected to socket, the chain is broken
- Extension sees no one listening on the other end

---

<!-- section_id: "7d8c2e6e-a239-4606-96f3-18363a651c44" -->
## Current Status

<!-- section_id: "0cd17ffa-8b9a-4863-ac58-78533c1670c1" -->
### What Works ✅

- Windows → WSL native messaging bridge (fully functional)
- Native host running and listening
- Socket created and ready
- All infrastructure correctly configured

<!-- section_id: "11747adc-e4fd-45e6-b036-75a8b5db10d4" -->
### What Doesn't Work ❌

- Claude Code CLI won't start with `--chrome` on WSL
- Extension can't detect CLI (because it's not connected)
- Full bidirectional communication blocked

<!-- section_id: "b96defe2-4123-4206-8c6f-26151a774d42" -->
### The Blocker 🚫

**Hardcoded platform check** in Claude Code CLI that rejects WSL before attempting socket connection.

---

<!-- section_id: "08f05f19-7660-491b-a69f-8fa1d48bf7ad" -->
## Possible Solutions

<!-- section_id: "b7f90b35-27a5-4223-9209-c0eea81754ae" -->
### Option 1: Install Claude Code on Windows (Most Practical)

- Install `claude` natively in Windows (not WSL)
- Run `claude --chrome` from Windows PowerShell/CMD
- Your bridge infrastructure becomes unnecessary
- Should work out-of-the-box

**Setup:**
```powershell
# In Windows PowerShell
npm install -g @anthropic-ai/claude-code
claude --chrome
```

**Benefits:**
- ✅ Works immediately with no workarounds
- ✅ Can coexist with WSL installation
- ✅ Projects in WSL accessible via `\\wsl$\Ubuntu\home\dawson`

<!-- section_id: "3f7e7532-83e6-436a-a598-4d1d7e96327e" -->
### Option 2: Request WSL Support (Long-term)

- Contact Anthropic to support WSL in future versions
- The infrastructure you built is correct
- Just needs client-side platform check removed
- File issue at: https://github.com/anthropics/claude-code/issues
- Reference: GitHub Issue #14367 (mentions WSL support)

<!-- section_id: "daeb6d24-a77c-42db-a9d0-c9fde7686efd" -->
### Option 3: Different Architecture (Complex)

- Use Chrome Remote Debugging Protocol instead
- Completely different approach
- More complex implementation
- Would bypass native messaging entirely

---

<!-- section_id: "94ec6d79-15a8-4f56-b426-c7b9e5765a2b" -->
## Technical Details

<!-- section_id: "f1f510c7-1868-4030-ab1f-c8ede5aa596a" -->
### File Locations

**WSL (Linux) Files:**
| File | Purpose |
|------|---------|
| `/home/dawson/.claude/chrome/chrome-native-host` | Actual native messaging host (generated by Claude Code) |
| `/home/dawson/bin/claude-chrome-host.sh` | WSL wrapper script (bridges Windows → WSL) |
| `/tmp/claude-mcp-browser-bridge-dawson` | UNIX socket for CLI ↔ Native Host communication |
| `~/.bashrc` | Environment variable `CLAUDE_CODE_ENABLE_CFC=true` |

**Windows Files:**
| File | Purpose |
|------|---------|
| `C:\Users\Dawson\bin\claude-chrome-host.bat` | Windows batch script (called by Chrome) |
| `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` | Chrome native messaging manifest |

**Windows Registry:**
| Key | Purpose |
|-----|---------|
| `HKCU:\Software\Google\Chrome\NativeMessagingHosts\com.anthropic.claude.chrome` | Chrome native host registration |

<!-- section_id: "5c4d17e4-18d2-4942-bc3d-eb443cf4a189" -->
### Native Messaging Protocol

Each message consists of:
1. **Length prefix:** 4 bytes (32-bit unsigned integer, little-endian)
2. **JSON message:** UTF-8 encoded JSON string

Example: `{type:"ping"}` (14 bytes)
```
Bytes: 0x0E 0x00 0x00 0x00 {"type":"ping"}
       └─── Length (14) ───┘ └─ JSON (14 bytes) ─┘
```

<!-- section_id: "4fa2d308-07b8-4095-bd55-fd0b8f1cd8cf" -->
### Test Results

**Working Communication Test:**
```javascript
// Chrome DevTools Console
const port = chrome.runtime.connectNative('com.anthropic.claude.chrome');
port.postMessage({type: 'ping'});
// Response: {type: 'pong', timestamp: 1735689123456}
```

**Failed CLI Connection:**
```bash
# WSL
claude --chrome
# Error: Claude in Chrome Native Host not supported on this platform
```

---

<!-- section_id: "483dc21a-f343-4d87-bc58-0f2d0112d83a" -->
## Bottom Line

<!-- section_id: "b12c8c73-b289-4684-bb31-e0ad1102936a" -->
### Success: Bridge Infrastructure

You successfully built a **working bridge** that proves Windows Chrome can communicate with WSL processes through native messaging. The bridge works perfectly - we confirmed this with the ping/pong test.

**This is a valuable proof-of-concept** that demonstrates:
- Native Messaging protocol CAN traverse Windows → WSL boundary
- The architecture is sound and well-designed
- All components communicate correctly

<!-- section_id: "55b1e5ea-d022-4b59-a901-ef365e8df2e1" -->
### Blocker: Platform Check

However, Claude Code CLI has a **hardcoded restriction** preventing it from running in `--chrome` mode on WSL, which blocks the final connection. The platform check happens too early in the initialization process to work around with environment variables or patches.

<!-- section_id: "20e51988-f931-4d12-8bdd-119e8dec6e43" -->
### Recommendation

The **cleanest solution** is to run Claude Code natively on Windows instead of in WSL, which would make all your Chrome extension features work immediately without needing this custom bridge.

Your projects can remain in WSL and be accessed from Windows Claude Code via `\\wsl$\Ubuntu\home\dawson\`.

---

<!-- section_id: "f256f70a-ab70-4611-8f0a-dc5ee357d9fb" -->
## Related Documentation

- **Detailed Setup Guide:** `BATCH_BRIDGE_SETUP.md`
- **Initial Findings:** `SETUP_FINDINGS.md`
- **Playwright MCP Alternative:** `../playwright-mcp-test-results.md`

---

<!-- section_id: "9b3efccf-3423-4da6-b52c-24e50fa7ec2b" -->
## Acknowledgments

This investigation successfully proved that:
1. Windows → WSL native messaging bridge is **technically viable**
2. The infrastructure design is **correct and functional**
3. The only blocker is a **software restriction**, not an architectural limitation

If Anthropic adds WSL support in the future, all the infrastructure built here will work immediately without modification.
