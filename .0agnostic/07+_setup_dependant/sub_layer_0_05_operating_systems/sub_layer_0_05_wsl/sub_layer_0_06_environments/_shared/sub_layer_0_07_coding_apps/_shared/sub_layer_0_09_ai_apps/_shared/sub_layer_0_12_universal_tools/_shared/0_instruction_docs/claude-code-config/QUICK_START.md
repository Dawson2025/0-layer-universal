---
resource_id: "d1256a6e-7bc9-4af8-9ed0-5c19e98b01b2"
resource_type: "document"
resource_name: "QUICK_START"
---
# Claude Code Bypass Permissions - Quick Start Guide

<!-- section_id: "5f3bde19-2279-4402-8905-6b5f4262bbab" -->
## 5-Minute Setup

<!-- section_id: "f8d8eb82-f1e9-4224-b80e-842dd4f0f4cb" -->
### For Personal Projects (Recommended)

1. **Create settings directory:**
   ```bash
   mkdir -p .claude
   ```

2. **Create settings file:**
   ```bash
   cat > .claude/settings.json << 'EOF'
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
   EOF
   ```

3. **Done!** Start Claude Code normally:
   ```bash
   claude
   ```

   **You should now see the Shift+Tab bypass mode toggle indicator.**

<!-- section_id: "53017909-0ef5-427a-9e91-91b320e8113b" -->
### For Shared Repositories (Local Override)

1. **Create local settings:**
   ```bash
   mkdir -p .claude
   cat > .claude/settings.local.json << 'EOF'
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
   EOF
   ```

2. **Add to .gitignore:**
   ```bash
   echo ".claude/settings.local.json" >> .gitignore
   ```

3. **Done!** Your team won't have bypass mode, but you will.

<!-- section_id: "401cb753-a4ec-48fb-b56c-01e7791c8eb9" -->
### One-Time Use (No Configuration)

```bash
claude --dangerously-skip-permissions
```

<!-- section_id: "c28093ed-f546-431e-919e-610357c95a30" -->
## Verification

In Claude Code, run:
```
/permissions
```

Look for: "Bypass permissions mode: enabled"

<!-- section_id: "873ec0ee-4da4-4ea4-a02e-a8ecaa3e8c2a" -->
## Common Configurations

<!-- section_id: "7a0198ae-5e82-4954-baa3-ea4f8cad4089" -->
### What Actually Works

**⚠️ IMPORTANT**: The `disableBypassPermissionsMode: false` approach shown in older documentation **does NOT work**. The correct configuration is:

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "allow": [
      "Read(/**)",
      "Edit(**)",
      "Write(**)",
      "Bash(git:*)",
      "Bash(npm:*)"
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

**Key Points:**
- Use `"defaultMode": "bypassPermissions"` to enable bypass mode and show the Shift+Tab toggle
- Include comprehensive `allow` rules for the operations you need
- Add `deny` rules for dangerous operations
- The `disableBypassPermissionsMode` field only accepts `"disable"` as a value (to disable bypass mode)

<!-- section_id: "79e28290-8c50-4f3d-8459-820116826c27" -->
### Full Documentation

See [bypass-permissions-setup.md](./bypass-permissions-setup.md) for complete details.

<!-- section_id: "bcb6b122-1840-4900-a2f0-ff4093db3820" -->
## Need Help?

- **Security concerns?** Read [Security Best Practices](./bypass-permissions-setup.md#security-best-practices)
- **Not working?** See [Troubleshooting](./bypass-permissions-setup.md#troubleshooting)
- **Enterprise environment?** Check [Enterprise Policies](./bypass-permissions-setup.md#enterprise-policy-enforcement)
