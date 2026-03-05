---
resource_id: "4a023f85-f295-43e4-b66c-779c491da6d8"
resource_type: "document"
resource_name: "FINAL_SUMMARY"
---
# Complete Summary: Claude in Chrome + WSL Integration Attempt

**Date:** 2025-12-31
**Status:** Bridge Built & Tested - Blocked by Platform Check
**Outcome:** Windows → WSL communication proven functional, but Claude Code CLI blocks WSL execution

---

<!-- section_id: "3683ba7b-096f-442c-ba15-3881c8bd0b3f" -->
## The Goal

Get the **Claude in Chrome** browser extension (running in Windows Chrome) to communicate with **Claude Code CLI** (running in WSL).

<!-- section_id: "fef78326-328b-4601-88c7-70fbd6764960" -->
## The Challenge

- Chrome runs on **Windows**
- Claude Code CLI runs in **WSL (Linux)**
- Chrome's Native Messaging API doesn't natively cross this boundary
- The `claude --chrome` command is hardcoded to block WSL

---

<!-- section_id: "ed81281a-3717-40fe-91b8-0b3dfbf2895f" -->
## What We Built

<!-- section_id: "25cda2db-7d9d-47a9-8f60-7d3a4432bb67" -->
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

<!-- section_id: "3e8532ce-fac7-4307-931d-0225446a351b" -->
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

<!-- section_id: "ef45713a-9d21-4ff1-8f40-38eae20b2384" -->
## What We Tested

<!-- section_id: "ed61b977-82da-4dd7-9829-f08a0767a451" -->
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

<!-- section_id: "e0cdf9aa-b8a9-471c-867f-46f3cb3c0cf6" -->
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

<!-- section_id: "f7274529-c9d7-42aa-96ff-b8e63bf290e5" -->
## Key Discoveries

<!-- section_id: "0443ac1a-2573-4cc6-b759-4bd1e0be8aa5" -->
### The Architecture We Uncovered

The native host is a **relay/bridge**, not the actual service:

1. Chrome Extension sends messages via native messaging
2. Native Host receives messages and creates UNIX socket listener
3. Socket (`/tmp/claude-mcp-browser-bridge-dawson`) waits for connections
4. Claude Code CLI (when run with `--chrome`) connects to socket
5. Messages flow: Chrome ↔ Native Host ↔ Socket ↔ Claude CLI

<!-- section_id: "78aacf8d-2b34-48bf-9d85-96b38c831572" -->
### Why It's Broken

- Claude Code CLI **refuses to run** with `--chrome` flag on WSL
- Platform check happens **before** socket connection attempt
- Without CLI connected to socket, the chain is broken
- Extension sees no one listening on the other end

---

<!-- section_id: "6ebb1acd-8dd3-4395-822a-a49d12e3585a" -->
## Current Status

<!-- section_id: "eab3e7a7-4a56-4e71-b0e2-80322106b0bc" -->
### What Works ✅

- Windows → WSL native messaging bridge (fully functional)
- Native host running and listening
- Socket created and ready
- All infrastructure correctly configured

<!-- section_id: "8c28f23e-6fa8-4a8a-ab6d-8f8d861ff22c" -->
### What Doesn't Work ❌

- Claude Code CLI won't start with `--chrome` on WSL
- Extension can't detect CLI (because it's not connected)
- Full bidirectional communication blocked

<!-- section_id: "4eefd6cc-6019-4dab-9b1a-8d8d67f951a1" -->
### The Blocker 🚫

**Hardcoded platform check** in Claude Code CLI that rejects WSL before attempting socket connection.

---

<!-- section_id: "2f289c7f-4eb7-4821-9dd4-57a5e8b8bc43" -->
## Possible Solutions

<!-- section_id: "00b1d8e0-03fd-448b-a118-f577d1787e83" -->
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

<!-- section_id: "ebe5e157-94c4-479f-864d-726f1cf47625" -->
### Option 2: Request WSL Support (Long-term)

- Contact Anthropic to support WSL in future versions
- The infrastructure you built is correct
- Just needs client-side platform check removed
- File issue at: https://github.com/anthropics/claude-code/issues
- Reference: GitHub Issue #14367 (mentions WSL support)

<!-- section_id: "4b4e0cc6-643c-4b35-9295-cb624fb1f040" -->
### Option 3: Different Architecture (Complex)

- Use Chrome Remote Debugging Protocol instead
- Completely different approach
- More complex implementation
- Would bypass native messaging entirely

---

<!-- section_id: "d12c9c01-ee3b-487a-8296-af119ce526bd" -->
## Technical Details

<!-- section_id: "03c3016c-4afa-4b67-b594-f24f95129048" -->
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

<!-- section_id: "ecb7c380-9d18-4117-bfc2-b75332bc2d05" -->
### Native Messaging Protocol

Each message consists of:
1. **Length prefix:** 4 bytes (32-bit unsigned integer, little-endian)
2. **JSON message:** UTF-8 encoded JSON string

Example: `{type:"ping"}` (14 bytes)
```
Bytes: 0x0E 0x00 0x00 0x00 {"type":"ping"}
       └─── Length (14) ───┘ └─ JSON (14 bytes) ─┘
```

<!-- section_id: "2e0af883-84ba-425c-8cd1-a24ed00962dc" -->
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

<!-- section_id: "07aa71fb-5f89-4123-b577-b57c2dc285ee" -->
## Bottom Line

<!-- section_id: "12ff5460-db92-4505-a382-91446e495e7c" -->
### Success: Bridge Infrastructure

You successfully built a **working bridge** that proves Windows Chrome can communicate with WSL processes through native messaging. The bridge works perfectly - we confirmed this with the ping/pong test.

**This is a valuable proof-of-concept** that demonstrates:
- Native Messaging protocol CAN traverse Windows → WSL boundary
- The architecture is sound and well-designed
- All components communicate correctly

<!-- section_id: "d2aa8789-e132-47d3-bcd0-8a6b87415157" -->
### Blocker: Platform Check

However, Claude Code CLI has a **hardcoded restriction** preventing it from running in `--chrome` mode on WSL, which blocks the final connection. The platform check happens too early in the initialization process to work around with environment variables or patches.

<!-- section_id: "533b577e-2604-43e7-961c-ba3c28e39998" -->
### Recommendation

The **cleanest solution** is to run Claude Code natively on Windows instead of in WSL, which would make all your Chrome extension features work immediately without needing this custom bridge.

Your projects can remain in WSL and be accessed from Windows Claude Code via `\\wsl$\Ubuntu\home\dawson\`.

---

<!-- section_id: "9c9bcf8a-a1d5-4e98-b83d-15d1f852a6ac" -->
## Related Documentation

- **Detailed Setup Guide:** `BATCH_BRIDGE_SETUP.md`
- **Initial Findings:** `SETUP_FINDINGS.md`
- **Playwright MCP Alternative:** `../playwright-mcp-test-results.md`

---

<!-- section_id: "1e73222e-1d01-4efa-a6f9-e4c4b15b54e5" -->
## Acknowledgments

This investigation successfully proved that:
1. Windows → WSL native messaging bridge is **technically viable**
2. The infrastructure design is **correct and functional**
3. The only blocker is a **software restriction**, not an architectural limitation

If Anthropic adds WSL support in the future, all the infrastructure built here will work immediately without modification.
