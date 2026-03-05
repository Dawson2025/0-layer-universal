---
resource_id: "73c2c9d1-a596-4cd2-a9df-cc7cbff08759"
resource_type: "document"
resource_name: "WHAT_ACTUALLY_WORKS"
---
# What Actually Works: Bypass Permissions Mode
*Lessons Learned from Real-World Testing*

<!-- section_id: "6bf28f81-3b3b-47d6-aa03-12d064b0b62f" -->
## TL;DR - The Working Configuration

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "allow": [
      "WebSearch",
      "WebFetch(domain:*)",
      "Read(/**)",
      "Edit(**)",
      "Write(**)",
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(npx:*)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(mkdir:*)",
      "Bash(rm:*)",
      "Bash(cp:*)",
      "Bash(mv:*)"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm -rf :*)",
      "Bash(git push --force origin main)",
      "Bash(git push --force origin master)",
      "Edit(.env*)"
    ]
  }
}
```

<!-- section_id: "82dc389f-8306-434f-9b82-955eb74df92f" -->
## The Problem with Old Documentation

<!-- section_id: "4f97ec16-c9eb-4ba1-8cf9-f37c6759b197" -->
### ❌ What DOESN'T Work

Many guides (including earlier versions of our own documentation) suggest:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

**This is WRONG** for several reasons:

1. **Invalid Schema Value**: The `disableBypassPermissionsMode` field only accepts `"disable"` as a value, not `false`
2. **No UI Toggle**: This approach doesn't show the Shift+Tab bypass mode indicator
3. **Doesn't Auto-Enable**: Even if the schema accepted it, bypass mode wouldn't automatically activate

<!-- section_id: "14e698cd-1921-4c7c-bb69-6467da911208" -->
### The Truth About `disableBypassPermissionsMode`

According to the actual Claude Code schema:

| Setting | Value | Effect |
|---------|-------|--------|
| `disableBypassPermissionsMode` | `"disable"` | ✅ Valid - Prevents bypass mode from being activated |
| `disableBypassPermissionsMode` | `false` | ❌ Invalid - Schema validation fails |
| `disableBypassPermissionsMode` | Not set | ⚠️ Allows bypass but doesn't enable it or show toggle |

<!-- section_id: "756a6bc0-3d62-4ce1-84c3-cc58942b5ea9" -->
## ✅ What Actually Works

<!-- section_id: "a977533d-8e6a-475a-93f3-1db226dc2296" -->
### The Magic Combination

To enable bypass permissions mode AND show the Shift+Tab toggle, you need:

1. **`defaultMode: "bypassPermissions"`** - This is the KEY setting
2. **Comprehensive `allow` rules** - List all operations you want to permit
3. **Strategic `deny` rules** - Block dangerous operations

<!-- section_id: "437034d6-7c3c-448a-a709-ffdb1d82163a" -->
### Why This Works

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",  // ← Shows Shift+Tab toggle and enables bypass
    "allow": [                            // ← Grants broad permissions
      "Read(/**)",
      "Edit(**)",
      "Write(**)"
      // ... etc
    ],
    "deny": [                             // ← Blocks dangerous operations
      "Bash(rm -rf /)"
      // ... etc
    ]
  }
}
```

**What each part does:**

- **`defaultMode: "bypassPermissions"`**
  - Automatically enables bypass mode on startup
  - Shows the visual Shift+Tab toggle indicator in the UI
  - Allows toggling between bypass/normal modes

- **`allow` array**
  - Whitelist approach - explicitly permit operations
  - Works alongside bypass mode for fine-grained control
  - Essential for comprehensive autonomous operation

- **`deny` array**
  - Blacklist approach - explicitly block dangerous operations
  - Overrides both bypass mode and allow rules
  - Safety net against destructive commands

<!-- section_id: "884ff1dc-c71f-4d27-b3eb-161857e05a26" -->
## Real-World Tested Configurations

<!-- section_id: "7e2efdfb-2eb0-4b05-902f-f8f0fb4fb8a7" -->
### Configuration 1: I-eat-repo (This Project)

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "allow": [
      "WebSearch",
      "WebFetch(domain:*)",
      "Read(/**)",
      "Edit(**)",
      "Write(**)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(find:*)",
      "Bash(grep:*)",
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(npx:*)",
      "Bash(node:*)",
      "Bash(mkdir:*)",
      "Bash(touch:*)",
      "Bash(cp:*)",
      "Bash(mv:*)",
      "Bash(rm:*)",
      "Bash(chmod:*)",
      "mcp__context7__resolve-library-id",
      "mcp__context7__get-library-docs",
      "mcp__playwright__browser_navigate",
      "mcp__chrome-devtools__take_snapshot",
      "mcp__browser__browser_navigate"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm -rf :*)",
      "Bash(git push --force origin main)",
      "Bash(git push --force origin master)",
      "Edit(.env*)",
      "Bash(DROP TABLE:*)"
    ]
  },
  "enabledMcpjsonServers": [
    "playwright",
    "context7",
    "chrome-devtools",
    "browser",
    "web-search"
  ]
}
```

**Result**: ✅ Works perfectly
- Shift+Tab toggle appears
- Bypass mode active on startup
- All common operations work without prompts
- Dangerous operations still blocked

<!-- section_id: "73a870a5-ce79-438e-bbd8-2127a12c1f8b" -->
### Configuration 2: Lang-trak-in-progress (Comparison)

```json
{
  "permissions": {
    "allow": [
      "WebSearch",
      "WebFetch(domain:*)",
      "Read(/**)",
      // ... extensive list of 60+ allowed operations
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo:*)"
    ]
  }
}
```

**Result**: ✅ Also works
- Doesn't use `defaultMode` but has extensive `allow` list
- Functions like bypass mode due to comprehensive permissions
- May not show Shift+Tab toggle as prominently

<!-- section_id: "87815257-9e79-4d05-9c35-8637852a6d4d" -->
## The Shift+Tab Toggle Mystery Solved

<!-- section_id: "e6dc8251-5f37-4a69-9bc6-bbdf45bcda28" -->
### What Makes the Toggle Appear?

The Shift+Tab toggle indicator appears when:

1. ✅ `defaultMode: "bypassPermissions"` is set in settings
2. ✅ Claude Code is restarted after settings change
3. ✅ No enterprise policy is blocking bypass mode

<!-- section_id: "70747ff5-28b9-422a-8a5c-d068c6ed9ad1" -->
### What DOESN'T Show the Toggle?

1. ❌ Only having extensive `allow` rules without `defaultMode`
2. ❌ Using `disableBypassPermissionsMode: false` (invalid)
3. ❌ Command-line `--dangerously-skip-permissions` flag (works but no persistent toggle)

<!-- section_id: "f02c67ee-ab40-4fac-8b9e-776c516393a4" -->
## Comparison Table

| Approach | Shows Toggle? | Auto-Enables Bypass? | Valid Schema? |
|----------|---------------|----------------------|---------------|
| `defaultMode: "bypassPermissions"` | ✅ Yes | ✅ Yes | ✅ Yes |
| `disableBypassPermissionsMode: false` | ❌ No | ❌ No | ❌ No (invalid) |
| Extensive `allow` list only | ⚠️ Maybe | ⚠️ Partial | ✅ Yes |
| `--dangerously-skip-permissions` flag | ❌ No | ✅ Yes | ✅ Yes |
| Nothing (omit field) | ❌ No | ❌ No | ✅ Yes |

<!-- section_id: "df42a292-c98f-40bd-848d-3b7bbfc0cb33" -->
## Migration Guide

<!-- section_id: "391ecce6-3183-4ecf-93ce-169fc279d3d9" -->
### If You Have This (Old/Wrong):

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

<!-- section_id: "c5bf71df-d722-4c2a-8c98-0d6457b39102" -->
### Change To This (New/Correct):

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "allow": [
      "Read(/**)",
      "Edit(**)",
      "Write(**)",
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(npx:*)"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm -rf :*)",
      "Bash(git push --force origin main)",
      "Bash(git push --force origin master)"
    ]
  }
}
```

<!-- section_id: "98bc58a5-3b5f-4153-b86f-f25c5426b1a0" -->
### Steps:

1. Update `.claude/settings.json` or `.claude/settings.local.json`
2. Validate JSON syntax: `cat .claude/settings.json | python3 -m json.tool`
3. Restart Claude Code
4. Verify by pressing Shift+Tab - you should see the bypass mode indicator

<!-- section_id: "525c1ce1-dede-4a2d-b613-6a75540f9d7d" -->
## Key Takeaways

1. **Use `defaultMode: "bypassPermissions"`** - This is the only reliable way to enable bypass mode and show the UI toggle

2. **Include comprehensive `allow` rules** - Don't rely on bypass mode alone; explicitly list allowed operations

3. **Add `deny` rules for safety** - Block dangerous operations even in bypass mode

4. **Test after changes** - Always restart Claude Code and verify the toggle appears

5. **Ignore old documentation** - Many guides suggest `disableBypassPermissionsMode: false` which doesn't work

<!-- section_id: "045fbbcb-6db7-4f8f-8cb1-a0c699c12081" -->
## Schema Reference

The actual Claude Code schema expects:

```typescript
interface Permissions {
  defaultMode?: "bypassPermissions" | "acceptEdits" | "default" | "plan";
  disableBypassPermissionsMode?: "disable";  // Only "disable" is valid!
  allow?: string[];
  deny?: string[];
  ask?: string[];
}
```

Note that `disableBypassPermissionsMode` is NOT a boolean - it only accepts the string `"disable"`.

<!-- section_id: "ad19cec6-3110-44c7-8263-61c2d2d36e86" -->
## Testing Checklist

After configuring bypass permissions, verify:

- [ ] Settings file has valid JSON syntax
- [ ] `defaultMode: "bypassPermissions"` is present
- [ ] Comprehensive `allow` rules are listed
- [ ] Safety `deny` rules are in place
- [ ] Claude Code has been restarted
- [ ] Shift+Tab shows bypass mode toggle
- [ ] Operations work without prompts
- [ ] Denied operations are still blocked

<!-- section_id: "4439fff0-106b-49cb-88f1-cc7f1fa2ad9f" -->
## Related Documentation

- [bypass-permissions-setup.md](./bypass-permissions-setup.md) - Complete setup guide (now corrected)
- [QUICK_START.md](./QUICK_START.md) - Quick reference (now corrected)
- [bash-wrapper-setup.md](./bash-wrapper-setup.md) - Alternative shell wrapper approach

---

**Version**: 2.0 (Corrected based on real-world testing)
**Date**: 2025-10-24
**Project**: I-eat-repo bypass permissions configuration
