---
resource_id: "bbe70587-359a-46c8-abea-42f202089046"
resource_type: "document"
resource_name: "WHAT_ACTUALLY_WORKS"
---
# What Actually Works: Bypass Permissions Mode
*Lessons Learned from Real-World Testing*

<!-- section_id: "64bb0800-058e-4720-9d58-3d7c55b88a8d" -->
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

<!-- section_id: "2cdbf30a-5485-4f34-927c-e3db04bbcfb9" -->
## The Problem with Old Documentation

<!-- section_id: "40edb052-5586-473b-b94a-e4ffa10007ff" -->
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

<!-- section_id: "a177e356-443c-4477-b848-d3a165170256" -->
### The Truth About `disableBypassPermissionsMode`

According to the actual Claude Code schema:

| Setting | Value | Effect |
|---------|-------|--------|
| `disableBypassPermissionsMode` | `"disable"` | ✅ Valid - Prevents bypass mode from being activated |
| `disableBypassPermissionsMode` | `false` | ❌ Invalid - Schema validation fails |
| `disableBypassPermissionsMode` | Not set | ⚠️ Allows bypass but doesn't enable it or show toggle |

<!-- section_id: "2a626775-355f-4e33-a943-006c160b36c6" -->
## ✅ What Actually Works

<!-- section_id: "dbf900c8-daec-40a7-8b38-d9025e9143a0" -->
### The Magic Combination

To enable bypass permissions mode AND show the Shift+Tab toggle, you need:

1. **`defaultMode: "bypassPermissions"`** - This is the KEY setting
2. **Comprehensive `allow` rules** - List all operations you want to permit
3. **Strategic `deny` rules** - Block dangerous operations

<!-- section_id: "2ff24bd0-3dbe-4b72-823b-8d9e16e4f87a" -->
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

<!-- section_id: "3ab15005-6c76-464c-9515-433594d92af2" -->
## Real-World Tested Configurations

<!-- section_id: "7f480b3c-2c08-463b-84c4-8de45ec183c6" -->
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

<!-- section_id: "d1098b61-09aa-4962-a4e8-ae0158ed920b" -->
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

<!-- section_id: "690e2bb0-3c71-4fbb-9e28-bd0535df0cfb" -->
## The Shift+Tab Toggle Mystery Solved

<!-- section_id: "152c9084-a855-4589-9302-b8cb38a87ab1" -->
### What Makes the Toggle Appear?

The Shift+Tab toggle indicator appears when:

1. ✅ `defaultMode: "bypassPermissions"` is set in settings
2. ✅ Claude Code is restarted after settings change
3. ✅ No enterprise policy is blocking bypass mode

<!-- section_id: "a1d25170-300f-4184-a51f-38cebb6cdf33" -->
### What DOESN'T Show the Toggle?

1. ❌ Only having extensive `allow` rules without `defaultMode`
2. ❌ Using `disableBypassPermissionsMode: false` (invalid)
3. ❌ Command-line `--dangerously-skip-permissions` flag (works but no persistent toggle)

<!-- section_id: "05aae96c-8cd9-4a27-bfc1-28d3890df991" -->
## Comparison Table

| Approach | Shows Toggle? | Auto-Enables Bypass? | Valid Schema? |
|----------|---------------|----------------------|---------------|
| `defaultMode: "bypassPermissions"` | ✅ Yes | ✅ Yes | ✅ Yes |
| `disableBypassPermissionsMode: false` | ❌ No | ❌ No | ❌ No (invalid) |
| Extensive `allow` list only | ⚠️ Maybe | ⚠️ Partial | ✅ Yes |
| `--dangerously-skip-permissions` flag | ❌ No | ✅ Yes | ✅ Yes |
| Nothing (omit field) | ❌ No | ❌ No | ✅ Yes |

<!-- section_id: "5b0f2e5d-16bb-4c48-8a87-e3965b5ac0fd" -->
## Migration Guide

<!-- section_id: "05cf7cba-2af3-4a02-a1cc-5337e79f61ad" -->
### If You Have This (Old/Wrong):

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

<!-- section_id: "1754523f-3b45-4c25-ae97-baa907bce80e" -->
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

<!-- section_id: "f8766c18-a973-40ab-b38e-3b48083e33e5" -->
### Steps:

1. Update `.claude/settings.json` or `.claude/settings.local.json`
2. Validate JSON syntax: `cat .claude/settings.json | python3 -m json.tool`
3. Restart Claude Code
4. Verify by pressing Shift+Tab - you should see the bypass mode indicator

<!-- section_id: "a4bfb3ba-b44b-471a-8fc0-41d04127921d" -->
## Key Takeaways

1. **Use `defaultMode: "bypassPermissions"`** - This is the only reliable way to enable bypass mode and show the UI toggle

2. **Include comprehensive `allow` rules** - Don't rely on bypass mode alone; explicitly list allowed operations

3. **Add `deny` rules for safety** - Block dangerous operations even in bypass mode

4. **Test after changes** - Always restart Claude Code and verify the toggle appears

5. **Ignore old documentation** - Many guides suggest `disableBypassPermissionsMode: false` which doesn't work

<!-- section_id: "6807d12e-1555-4fc0-864c-2f9f0a058437" -->
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

<!-- section_id: "1cf8bf06-1764-4e0c-8f87-5d767990dcbc" -->
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

<!-- section_id: "fdbe6eba-0793-402f-bc40-9d0fef736580" -->
## Related Documentation

- [bypass-permissions-setup.md](./bypass-permissions-setup.md) - Complete setup guide (now corrected)
- [QUICK_START.md](./QUICK_START.md) - Quick reference (now corrected)
- [bash-wrapper-setup.md](./bash-wrapper-setup.md) - Alternative shell wrapper approach

---

**Version**: 2.0 (Corrected based on real-world testing)
**Date**: 2025-10-24
**Project**: I-eat-repo bypass permissions configuration
