---
resource_id: "641c5dd0-ee26-48fb-9d99-937a0d9ce7b9"
resource_type: "document"
resource_name: "WHAT_ACTUALLY_WORKS"
---
# What Actually Works: Bypass Permissions Mode
*Lessons Learned from Real-World Testing*

<!-- section_id: "2915cecf-b62a-4692-9ec0-b9a7e990a608" -->
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

<!-- section_id: "d4dc312c-3622-485a-b88c-07f6a876a8da" -->
## The Problem with Old Documentation

<!-- section_id: "d952c115-9ab9-4117-a3a7-dbad4fe8213c" -->
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

<!-- section_id: "035f833e-1518-45c9-9807-2d98ff922688" -->
### The Truth About `disableBypassPermissionsMode`

According to the actual Claude Code schema:

| Setting | Value | Effect |
|---------|-------|--------|
| `disableBypassPermissionsMode` | `"disable"` | ✅ Valid - Prevents bypass mode from being activated |
| `disableBypassPermissionsMode` | `false` | ❌ Invalid - Schema validation fails |
| `disableBypassPermissionsMode` | Not set | ⚠️ Allows bypass but doesn't enable it or show toggle |

<!-- section_id: "6fbe4872-86aa-4870-b447-4c286767fcfb" -->
## ✅ What Actually Works

<!-- section_id: "14d084b2-7d90-4cfe-8f84-9643e9edafb4" -->
### The Magic Combination

To enable bypass permissions mode AND show the Shift+Tab toggle, you need:

1. **`defaultMode: "bypassPermissions"`** - This is the KEY setting
2. **Comprehensive `allow` rules** - List all operations you want to permit
3. **Strategic `deny` rules** - Block dangerous operations

<!-- section_id: "e512dddc-7171-4f71-935b-3a54a0dcf1f6" -->
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

<!-- section_id: "8f4aa554-70bf-40ed-b6e8-2d79fe1db68d" -->
## Real-World Tested Configurations

<!-- section_id: "e7bf9842-1cb7-488a-b4fb-f6a31d446ca8" -->
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

<!-- section_id: "036934e6-1110-432a-b0be-72a78d9b514c" -->
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

<!-- section_id: "87314471-ce0c-49a5-8aea-1da3ff4c15d2" -->
## The Shift+Tab Toggle Mystery Solved

<!-- section_id: "9acfa6aa-a226-4d09-ac09-2f33461f3cee" -->
### What Makes the Toggle Appear?

The Shift+Tab toggle indicator appears when:

1. ✅ `defaultMode: "bypassPermissions"` is set in settings
2. ✅ Claude Code is restarted after settings change
3. ✅ No enterprise policy is blocking bypass mode

<!-- section_id: "18dc0aa4-b976-4715-a88c-6e2d2a6e9f86" -->
### What DOESN'T Show the Toggle?

1. ❌ Only having extensive `allow` rules without `defaultMode`
2. ❌ Using `disableBypassPermissionsMode: false` (invalid)
3. ❌ Command-line `--dangerously-skip-permissions` flag (works but no persistent toggle)

<!-- section_id: "05d7eb2d-46a0-425a-9376-c6da0cd0de51" -->
## Comparison Table

| Approach | Shows Toggle? | Auto-Enables Bypass? | Valid Schema? |
|----------|---------------|----------------------|---------------|
| `defaultMode: "bypassPermissions"` | ✅ Yes | ✅ Yes | ✅ Yes |
| `disableBypassPermissionsMode: false` | ❌ No | ❌ No | ❌ No (invalid) |
| Extensive `allow` list only | ⚠️ Maybe | ⚠️ Partial | ✅ Yes |
| `--dangerously-skip-permissions` flag | ❌ No | ✅ Yes | ✅ Yes |
| Nothing (omit field) | ❌ No | ❌ No | ✅ Yes |

<!-- section_id: "09dc5943-de6a-4bb2-938b-d6d0b97b2c54" -->
## Migration Guide

<!-- section_id: "1e86286f-f2c2-4e78-96c2-7f14e4670c17" -->
### If You Have This (Old/Wrong):

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

<!-- section_id: "ccf8c17c-c42c-40cf-9d7d-a4588d5d54dd" -->
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

<!-- section_id: "b30a8921-8ff5-4b05-9340-291e7e37f35f" -->
### Steps:

1. Update `.claude/settings.json` or `.claude/settings.local.json`
2. Validate JSON syntax: `cat .claude/settings.json | python3 -m json.tool`
3. Restart Claude Code
4. Verify by pressing Shift+Tab - you should see the bypass mode indicator

<!-- section_id: "157e2a61-3d2b-4b96-96ae-5e433393de20" -->
## Key Takeaways

1. **Use `defaultMode: "bypassPermissions"`** - This is the only reliable way to enable bypass mode and show the UI toggle

2. **Include comprehensive `allow` rules** - Don't rely on bypass mode alone; explicitly list allowed operations

3. **Add `deny` rules for safety** - Block dangerous operations even in bypass mode

4. **Test after changes** - Always restart Claude Code and verify the toggle appears

5. **Ignore old documentation** - Many guides suggest `disableBypassPermissionsMode: false` which doesn't work

<!-- section_id: "e88c5459-627a-473e-bfc3-ae2ddd54eed5" -->
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

<!-- section_id: "9bf1a161-a08f-4a3c-afa4-1c62aad6980b" -->
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

<!-- section_id: "e5d6e21a-dc9a-42bf-8972-e5b7b7af01d8" -->
## Related Documentation

- [bypass-permissions-setup.md](./bypass-permissions-setup.md) - Complete setup guide (now corrected)
- [QUICK_START.md](./QUICK_START.md) - Quick reference (now corrected)
- [bash-wrapper-setup.md](./bash-wrapper-setup.md) - Alternative shell wrapper approach

---

**Version**: 2.0 (Corrected based on real-world testing)
**Date**: 2025-10-24
**Project**: I-eat-repo bypass permissions configuration
