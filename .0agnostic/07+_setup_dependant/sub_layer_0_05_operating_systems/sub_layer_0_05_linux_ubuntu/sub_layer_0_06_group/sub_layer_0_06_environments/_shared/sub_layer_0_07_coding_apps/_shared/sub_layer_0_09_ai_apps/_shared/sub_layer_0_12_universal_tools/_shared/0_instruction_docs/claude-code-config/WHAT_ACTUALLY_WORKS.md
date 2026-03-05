---
resource_id: "801fbf38-4cb8-4ce7-a39e-6fd48d7218cb"
resource_type: "document"
resource_name: "WHAT_ACTUALLY_WORKS"
---
# What Actually Works: Bypass Permissions Mode
*Lessons Learned from Real-World Testing*

<!-- section_id: "752927b3-e726-4b68-bc4f-adbf2e1abcc3" -->
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

<!-- section_id: "688829c9-f42b-4317-abc8-826697b26a7f" -->
## The Problem with Old Documentation

<!-- section_id: "1c49d565-d3a6-4c1d-8242-6983b01a6fd0" -->
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

<!-- section_id: "e3909ee7-5691-45e6-9d84-a66e84e58241" -->
### The Truth About `disableBypassPermissionsMode`

According to the actual Claude Code schema:

| Setting | Value | Effect |
|---------|-------|--------|
| `disableBypassPermissionsMode` | `"disable"` | ✅ Valid - Prevents bypass mode from being activated |
| `disableBypassPermissionsMode` | `false` | ❌ Invalid - Schema validation fails |
| `disableBypassPermissionsMode` | Not set | ⚠️ Allows bypass but doesn't enable it or show toggle |

<!-- section_id: "e018f9ec-b770-438a-a8c2-42c7538fd0dc" -->
## ✅ What Actually Works

<!-- section_id: "2dc5d705-4fc0-4d15-8658-54ad815b5b34" -->
### The Magic Combination

To enable bypass permissions mode AND show the Shift+Tab toggle, you need:

1. **`defaultMode: "bypassPermissions"`** - This is the KEY setting
2. **Comprehensive `allow` rules** - List all operations you want to permit
3. **Strategic `deny` rules** - Block dangerous operations

<!-- section_id: "da1dcf92-0e8b-4614-ae61-b9630f72b637" -->
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

<!-- section_id: "b3354be1-91ff-42f1-be53-30c9bd89791b" -->
## Real-World Tested Configurations

<!-- section_id: "0270505d-01fd-41c2-833c-974e69670963" -->
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

<!-- section_id: "ba26d321-467e-4084-bd37-0a3113ead622" -->
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

<!-- section_id: "26acb551-370e-42e6-82ae-1513c710112c" -->
## The Shift+Tab Toggle Mystery Solved

<!-- section_id: "7f4c0cbf-3f94-4ced-b5c7-a9f065bff6c5" -->
### What Makes the Toggle Appear?

The Shift+Tab toggle indicator appears when:

1. ✅ `defaultMode: "bypassPermissions"` is set in settings
2. ✅ Claude Code is restarted after settings change
3. ✅ No enterprise policy is blocking bypass mode

<!-- section_id: "c6d24d9d-df10-4b82-bb8f-15112d8d5712" -->
### What DOESN'T Show the Toggle?

1. ❌ Only having extensive `allow` rules without `defaultMode`
2. ❌ Using `disableBypassPermissionsMode: false` (invalid)
3. ❌ Command-line `--dangerously-skip-permissions` flag (works but no persistent toggle)

<!-- section_id: "108647b1-723e-4164-b8cc-770ff64d85c2" -->
## Comparison Table

| Approach | Shows Toggle? | Auto-Enables Bypass? | Valid Schema? |
|----------|---------------|----------------------|---------------|
| `defaultMode: "bypassPermissions"` | ✅ Yes | ✅ Yes | ✅ Yes |
| `disableBypassPermissionsMode: false` | ❌ No | ❌ No | ❌ No (invalid) |
| Extensive `allow` list only | ⚠️ Maybe | ⚠️ Partial | ✅ Yes |
| `--dangerously-skip-permissions` flag | ❌ No | ✅ Yes | ✅ Yes |
| Nothing (omit field) | ❌ No | ❌ No | ✅ Yes |

<!-- section_id: "9cf94172-1989-4fa3-8145-045d249f7297" -->
## Migration Guide

<!-- section_id: "6ebddffa-9a82-426a-b3af-873f0f99f577" -->
### If You Have This (Old/Wrong):

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

<!-- section_id: "315b1904-7940-40ca-8426-394212a52dee" -->
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

<!-- section_id: "1d71de84-0587-4d03-8f45-56b2685bee6e" -->
### Steps:

1. Update `.claude/settings.json` or `.claude/settings.local.json`
2. Validate JSON syntax: `cat .claude/settings.json | python3 -m json.tool`
3. Restart Claude Code
4. Verify by pressing Shift+Tab - you should see the bypass mode indicator

<!-- section_id: "5b149b17-ff81-4453-9946-bd54bb6a833d" -->
## Key Takeaways

1. **Use `defaultMode: "bypassPermissions"`** - This is the only reliable way to enable bypass mode and show the UI toggle

2. **Include comprehensive `allow` rules** - Don't rely on bypass mode alone; explicitly list allowed operations

3. **Add `deny` rules for safety** - Block dangerous operations even in bypass mode

4. **Test after changes** - Always restart Claude Code and verify the toggle appears

5. **Ignore old documentation** - Many guides suggest `disableBypassPermissionsMode: false` which doesn't work

<!-- section_id: "ae708140-ce35-4648-bf56-c7c08ff0bce0" -->
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

<!-- section_id: "077afac7-0c8e-4478-9307-c5b0d50c1755" -->
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

<!-- section_id: "0e722f23-b0e8-498f-9c4a-99a61118abad" -->
## Related Documentation

- [bypass-permissions-setup.md](./bypass-permissions-setup.md) - Complete setup guide (now corrected)
- [QUICK_START.md](./QUICK_START.md) - Quick reference (now corrected)
- [bash-wrapper-setup.md](./bash-wrapper-setup.md) - Alternative shell wrapper approach

---

**Version**: 2.0 (Corrected based on real-world testing)
**Date**: 2025-10-24
**Project**: I-eat-repo bypass permissions configuration
