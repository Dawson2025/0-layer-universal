---
resource_id: "f29011da-1b6b-40c6-a232-63da6cfe1f08"
resource_type: "document"
resource_name: "QUICK_START"
---
# Claude Code Bypass Permissions - Quick Start Guide

<!-- section_id: "f7fd8206-d0be-4628-9d46-9a8a14bcd767" -->
## 5-Minute Setup

<!-- section_id: "49a4e1d7-4a0b-4239-9289-314dba70d2cc" -->
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

<!-- section_id: "039da0d8-6071-49f7-8286-83890319577a" -->
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

<!-- section_id: "db3d555c-1b50-4b33-8e92-29ef46d21439" -->
### One-Time Use (No Configuration)

```bash
claude --dangerously-skip-permissions
```

<!-- section_id: "b9fa6b06-fd85-47af-a2d2-415875256d81" -->
## Verification

In Claude Code, run:
```
/permissions
```

Look for: "Bypass permissions mode: enabled"

<!-- section_id: "0a9b3718-bf34-4bcb-b1a2-81793e58a763" -->
## Common Configurations

<!-- section_id: "00fd12ed-92fc-40fb-a944-3bc3ea5e05c6" -->
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

<!-- section_id: "a03713f5-d4e0-4b36-a919-5c82adbfae3f" -->
### Full Documentation

See [bypass-permissions-setup.md](./bypass-permissions-setup.md) for complete details.

<!-- section_id: "8d969e1a-4fe8-4987-876d-750fe3296017" -->
## Need Help?

- **Security concerns?** Read [Security Best Practices](./bypass-permissions-setup.md#security-best-practices)
- **Not working?** See [Troubleshooting](./bypass-permissions-setup.md#troubleshooting)
- **Enterprise environment?** Check [Enterprise Policies](./bypass-permissions-setup.md#enterprise-policy-enforcement)
