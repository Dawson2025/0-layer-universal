---
resource_id: "61c961df-ffde-4db0-b953-87d9015920dc"
resource_type: "document"
resource_name: "QUICK_START"
---
# Claude Code Bypass Permissions - Quick Start Guide

<!-- section_id: "67b0ae74-6416-4e8b-ae4f-496d9858dc81" -->
## 5-Minute Setup

<!-- section_id: "e243b370-5a0d-4b10-a557-3b5fbff9f5a7" -->
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

<!-- section_id: "c766f4da-6970-4348-a06a-26034528cd1b" -->
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

<!-- section_id: "a5a2797e-e7e6-4c4a-9568-412e2c0123a1" -->
### One-Time Use (No Configuration)

```bash
claude --dangerously-skip-permissions
```

<!-- section_id: "d0da917e-6d8b-46a2-989a-a03cbfedfd55" -->
## Verification

In Claude Code, run:
```
/permissions
```

Look for: "Bypass permissions mode: enabled"

<!-- section_id: "bdbe510d-564a-45dd-832a-3143e1bc8fe5" -->
## Common Configurations

<!-- section_id: "26a92a9a-c623-450e-a6ef-1cb1a150126c" -->
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

<!-- section_id: "8ba87201-8949-4957-8a13-8005f3102c58" -->
### Full Documentation

See [bypass-permissions-setup.md](./bypass-permissions-setup.md) for complete details.

<!-- section_id: "a7f54b67-3b0f-4207-b468-fb8ec9b813bc" -->
## Need Help?

- **Security concerns?** Read [Security Best Practices](./bypass-permissions-setup.md#security-best-practices)
- **Not working?** See [Troubleshooting](./bypass-permissions-setup.md#troubleshooting)
- **Enterprise environment?** Check [Enterprise Policies](./bypass-permissions-setup.md#enterprise-policy-enforcement)
