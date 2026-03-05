---
resource_id: "0f9ba716-3cc6-4ffa-bf8f-46b3ba3f266d"
resource_type: "document"
resource_name: "bypass-permissions-setup"
---
# Claude Code Bypass Permissions Setup Guide
*Universal Configuration for Trusted Development Environments*

<!-- section_id: "fde37948-5222-451c-94f5-025968732646" -->
## Overview

Bypass permissions mode allows Claude Code to operate without permission prompts, enabling autonomous development in trusted environments. This guide covers configuration, implementation, and security considerations.

<!-- section_id: "39f64956-6421-4abc-a3b8-9f729480156d" -->
## ⚠️ Security Warning

**Use bypass permissions mode ONLY in:**
- Personal development projects
- Trusted local environments
- Isolated development containers
- Educational/learning projects

**NEVER use bypass mode for:**
- Shared team repositories
- Client projects with sensitive data
- Production environments
- Codebases with proprietary information
- Systems with regulatory compliance requirements

<!-- section_id: "98bbf85d-aea7-4780-ae35-f1911a5af99a" -->
## Configuration Methods

<!-- section_id: "0fd5b3d6-d06c-48c8-a415-e15ec7256a4a" -->
### Method 1: Project-Level Configuration (Recommended)

This method enables bypass mode for a specific project while maintaining security for other projects.

#### Step 1: Create Project Settings Directory

```bash
mkdir -p .claude
```

#### Step 2: Create Settings File

Create `.claude/settings.json` in your project root:

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

**⚠️ IMPORTANT NOTE**: The `disableBypassPermissionsMode` field does NOT work as documented. The schema only accepts `"disable"` as a value, not `false`. The correct way to enable bypass permissions mode is using `defaultMode: "bypassPermissions"` as shown above.

#### Step 3: Add to Version Control (Optional)

If this is a personal project, you can commit this file:

```bash
git add .claude/settings.json
git commit -m "Enable Claude Code bypass permissions for development"
```

**Important**: Only commit this for personal projects. For shared repositories, use `.claude/settings.local.json` instead and add it to `.gitignore`.

#### Configuration Values

| Field | Value | Behavior |
|-------|-------|----------|
| `defaultMode` | `"bypassPermissions"` | **RECOMMENDED**: Enables bypass mode and shows Shift+Tab toggle |
| `defaultMode` | `"default"` | Normal permissions mode (prompts for approval) |
| `defaultMode` | `"acceptEdits"` | Auto-accept edit operations only |
| `defaultMode` | `"plan"` | Start in planning mode |
| `disableBypassPermissionsMode` | `"disable"` | Prevents bypass mode from being activated |
| `disableBypassPermissionsMode` | Not set | Allows bypass mode but doesn't auto-enable it |

**Note**: Despite old documentation suggesting `disableBypassPermissionsMode: false`, this is **invalid**. Use `defaultMode: "bypassPermissions"` instead.

<!-- section_id: "81ada79b-9855-4057-9d22-c0f6ff7aef4d" -->
### Method 2: Command-Line Flag

Enable bypass mode for a single session without modifying configuration files:

```bash
claude --dangerously-skip-permissions
```

**Use cases:**
- One-off autonomous tasks
- Testing without modifying config
- Temporary permission bypass

**Limitations:**
- Only affects current session
- Cannot be overridden by enterprise policies
- No persistent configuration

<!-- section_id: "8a394d38-2602-4ba5-bbd7-5b40e319045d" -->
### Method 3: User-Level Default

Set bypass mode as default for all your projects:

#### Step 1: Create User Settings Directory

```bash
mkdir -p ~/.claude
```

#### Step 2: Create User Settings File

Create `~/.claude/settings.json`:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

**Note**: Project-level settings can still override this.

<!-- section_id: "6a2d75eb-90ff-4908-9673-1d7a9f1298bc" -->
### Method 4: Local Development Override

For shared repositories where you want bypass mode locally but not for the team:

#### Step 1: Create Local Settings

Create `.claude/settings.local.json`:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

#### Step 2: Add to .gitignore

Ensure `.claude/settings.local.json` is in your `.gitignore`:

```bash
echo ".claude/settings.local.json" >> .gitignore
```

This allows you to work with bypass mode while team members maintain permission prompts.

<!-- section_id: "249f7bb9-26fc-4419-a1fb-8ac38feef93d" -->
## Settings Hierarchy

Claude Code reads settings in this precedence order (highest to lowest):

1. **Enterprise Managed Policies** (`managed-settings.json`)
   - Cannot be overridden
   - Deployed by IT/Security teams
   - Enforces organization-wide policies

2. **Command-Line Arguments** (`--dangerously-skip-permissions`)
   - Session-specific
   - Overrides all file-based settings except managed policies

3. **Project Local Settings** (`.claude/settings.local.json`)
   - Developer-specific overrides
   - Not version controlled
   - Highest precedence for file-based settings

4. **Project Settings** (`.claude/settings.json`)
   - Team-shared configuration
   - Version controlled
   - Project-specific defaults

5. **User Settings** (`~/.claude/settings.json`)
   - Personal defaults
   - Applies to all projects
   - Lowest precedence

<!-- section_id: "85401b8a-5408-4fbd-865e-045e174639ae" -->
### Example Hierarchy in Action

```
Enterprise Policy:     disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (enterprise policy wins)
```

```
User Settings:         disableBypassPermissionsMode: false
Project Settings:      disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (project settings win)
```

```
Project Settings:      disableBypassPermissionsMode: false
Local Settings:        disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (local settings win)
```

<!-- section_id: "41f7a361-a140-4c37-aa7a-a33ea18f74dc" -->
## Implementation Examples

<!-- section_id: "3b82f67d-d245-4795-bee1-43bc32f1eae4" -->
### Example 1: Personal Side Project (CORRECTED)

**Scenario**: Full control, rapid development, no sensitive data

```json
// .claude/settings.json (committed to git)
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
      "Bash(git push --force origin master)"
    ]
  }
}
```

**Workflow:**
```bash
# Start Claude Code normally - bypass mode is enabled
claude

# You'll see the Shift+Tab toggle indicator showing bypass mode is active
# AI can autonomously perform allowed operations without prompts
# Dangerous operations (in deny list) are still blocked
```

<!-- section_id: "8746ea93-efa9-46b1-9cac-03dcbcb98fa9" -->
### Example 2: Shared Repository with Local Override

**Scenario**: Team project, you want bypass locally, team wants prompts

```json
// .claude/settings.json (committed - team default)
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "description": "Team project - permissions required by default"
}
```

```json
// .claude/settings.local.json (not committed - your override)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  },
  "description": "Local override - bypass enabled for my development"
}
```

```bash
# Add to .gitignore
echo ".claude/settings.local.json" >> .gitignore
```

<!-- section_id: "22f6b7e7-a266-4755-bbc7-ae8ca95b1b96" -->
### Example 3: Hybrid Approach - Selective Bypass

**Scenario**: Want bypass for most operations, but protect sensitive files

```json
// .claude/settings.json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Read(.env)",
      "Read(.env.*)",
      "Edit(.env)",
      "Edit(.env.*)",
      "Read(config/secrets/**)",
      "Edit(config/secrets/**)",
      "Bash(rm -rf *)",
      "Bash(git push --force*)"
    ]
  },
  "description": "Bypass enabled but sensitive operations denied"
}
```

This configuration:
- Enables bypass mode for general operations
- Explicitly denies access to environment files
- Blocks destructive commands
- Provides a safety net for critical operations

<!-- section_id: "b1a4e367-fb74-4eab-925a-e12306003c7d" -->
### Example 4: Temporary Bypass for Specific Task

**Scenario**: Need bypass for one-time refactoring, normally use permissions

```bash
# One-time use without changing configuration
claude --dangerously-skip-permissions

# Run your task
# Bypass mode only active for this session

# Next time you run claude without the flag:
claude
# Normal permission prompts return
```

<!-- section_id: "e5f500d3-8dce-4797-b4d3-8f379f69f445" -->
## Verification

<!-- section_id: "e4a8d8e7-965c-4435-86ac-1e61888863d7" -->
### Check Current Settings

```bash
# View current permission configuration
claude
```

Then in Claude Code:
```
/permissions
```

This shows:
- Current bypass mode status
- Active allow/deny rules
- Settings hierarchy being applied

<!-- section_id: "b3642147-251d-47b3-a317-403664155ac7" -->
### Test Bypass Mode

Create a test file to verify bypass is working:

```bash
# Start Claude Code
claude

# Ask Claude to create a test file
> "Create a test file called test-bypass.txt with the content 'Bypass mode active'"
```

If bypass mode is enabled:
- No permission prompt appears
- File is created immediately
- Operation completes autonomously

If bypass mode is disabled:
- Permission prompt appears
- You must approve the file creation
- Operation waits for confirmation

<!-- section_id: "28904dc9-8703-4ef2-8cf8-1b6ec7a75784" -->
## Disabling Bypass Mode

<!-- section_id: "24518007-c7fc-42cc-8d96-8d4809a90fea" -->
### Temporary Disable (Current Session)

Cannot be done - bypass is session-wide if enabled. Restart Claude Code without the flag.

<!-- section_id: "c85ae04e-46ee-4f42-8124-6127ea9f9c5e" -->
### Permanent Disable for Project

```json
// .claude/settings.json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  }
}
```

<!-- section_id: "15cf63ca-67d2-4d20-b6ca-6c53d023a828" -->
### Remove All Bypass Configuration

```bash
# Remove project settings
rm .claude/settings.json
rm .claude/settings.local.json

# Remove user settings
rm ~/.claude/settings.json

# Claude Code will revert to default (prompts enabled)
```

<!-- section_id: "61f24b1e-b924-4a5e-80d9-58034cbdc054" -->
## Enterprise Policy Enforcement

<!-- section_id: "073b2086-1788-4f20-a999-7f18faf78fa8" -->
### Scenario: Organization Requires Permissions

If your organization deploys managed policies, bypass mode may be disabled regardless of your configuration.

**Managed Policy Example** (`managed-settings.json`):
```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "enforced": true,
  "description": "Corporate security policy - bypass mode prohibited"
}
```

**Result**: You cannot enable bypass mode, even with:
- Project settings
- User settings
- Command-line flags

**What to do:**
1. Contact your IT/Security team
2. Request exception for specific projects
3. Explain business justification
4. Follow your organization's security approval process

<!-- section_id: "501810eb-75b8-45f7-a1e9-ecce6a59e4ae" -->
## Troubleshooting

<!-- section_id: "c92c8308-fa15-46a9-97e1-deee2a4543ae" -->
### Shift+Tab Toggle Not Appearing

**Symptom**: Cannot see the bypass permissions mode toggle indicator in the UI

**Root Cause**: The Shift+Tab toggle only appears when `defaultMode: "bypassPermissions"` is set.

**Solution:**
1. ✅ Add `"defaultMode": "bypassPermissions"` to your settings file
2. ✅ Include comprehensive `allow` rules (see working example below)
3. ✅ Restart Claude Code

**Working Configuration:**
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
      "Bash(git push --force origin main)"
    ]
  }
}
```

**What DOESN'T Work:**
```json
{
  "permissions": {
    "disableBypassPermissionsMode": false  // ❌ INVALID - does not show toggle
  }
}
```

The `disableBypassPermissionsMode` field only accepts `"disable"` as a value (to prevent bypass mode). Setting it to `false` is invalid according to the schema.

<!-- section_id: "9ff320bc-846e-4940-8a63-c6c5fd537a75" -->
### Bypass Mode Not Working

**Symptom**: Still seeing permission prompts despite configuration

**Checklist:**
1. ✅ Verify you're using `"defaultMode": "bypassPermissions"` (not `disableBypassPermissionsMode: false`)
2. ✅ Include comprehensive `allow` rules in your configuration
3. ✅ Check for enterprise managed policies
4. ✅ Ensure JSON syntax is valid
5. ✅ Verify file is in correct location (`.claude/settings.json` or `.claude/settings.local.json`)
6. ✅ Restart Claude Code after changing settings
7. ✅ Check settings precedence - higher level may override

**Diagnostic:**
```bash
# Check if settings file is valid JSON
cat .claude/settings.json | python3 -m json.tool

# Review settings hierarchy
claude
# Then: /permissions
```

<!-- section_id: "be274462-394c-48d8-8441-6d1d05b43c3c" -->
### Bypass Mode Active When It Shouldn't Be

**Symptom**: No permission prompts when you expected them

**Checklist:**
1. ✅ Check for `--dangerously-skip-permissions` flag in launch command
2. ✅ Look for `.claude/settings.local.json` override
3. ✅ Review user-level settings (`~/.claude/settings.json`)
4. ✅ Verify project settings don't enable bypass

**Fix:**
```bash
# Find all settings files
find ~ -name "settings.json" -o -name "settings.local.json" 2>/dev/null

# Review each for bypass configuration
```

<!-- section_id: "528d5250-1ab2-482d-af7a-a5afd8bc0faa" -->
### Specific Operations Still Require Permissions

**Symptom**: Bypass mode enabled, but some operations still prompt

**Explanation**: Deny rules override bypass mode

**Example:**
```json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Bash(rm *)"
    ]
  }
}
```

Even with bypass enabled, `rm` commands will be denied.

**Solution**: Remove deny rules if you want full bypass, or keep them for safety.

<!-- section_id: "9e05ef7b-faf4-4014-a891-37d57790785f" -->
## Security Best Practices

<!-- section_id: "9f259245-b78e-4f83-a600-17f7d6643635" -->
### 1. Scope Bypass to Specific Projects

❌ **Don't do this:**
```json
// ~/.claude/settings.json (applies to ALL projects)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

✅ **Do this instead:**
```json
// .claude/settings.json (specific project only)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

<!-- section_id: "b075b054-0cce-4bc0-8ad1-23d237ce4c23" -->
### 2. Document Why Bypass is Enabled

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  },
  "description": "Personal learning project - bypass enabled for rapid experimentation",
  "project": "python-automation-tools",
  "owner": "personal",
  "risk_level": "low"
}
```

<!-- section_id: "71351a1d-a177-4d20-9599-9d55deb28445" -->
### 3. Use Deny Rules for Critical Operations

Even with bypass mode, protect destructive operations:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm *)",
      "Bash(git push --force*)",
      "Bash(DROP TABLE*)",
      "Edit(.git/config)",
      "Bash(curl * | bash)"
    ]
  }
}
```

<!-- section_id: "52de2430-6cf4-476f-84bc-5317878ca0d8" -->
### 4. Regular Security Reviews

Periodically review and audit your bypass configurations:

```bash
# Find all bypass configurations
find ~ -name "settings*.json" -exec grep -l "disableBypassPermissionsMode.*false" {} \;

# Review each one
# Remove bypass from projects that no longer need it
```

<!-- section_id: "1e695a56-0e4f-40a5-a2b9-0529a962b569" -->
### 5. Use Version Control Wisely

```gitignore
# .gitignore
.claude/settings.local.json   # Personal overrides
.claude/managed-settings.json # Enterprise policies
.env*                          # Secrets
```

```bash
# What TO commit
git add .claude/settings.json  # Only if personal project
```

<!-- section_id: "8098c55e-4a00-4287-a95d-0fc3db431fb2" -->
## Alternative: Fine-Grained Permissions

Instead of bypassing all permissions, consider allowing specific operations:

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Bash(npm *)",
      "Bash(git status)",
      "Bash(git diff)",
      "Edit(src/**)",
      "Edit(tests/**)",
      "Write(docs/**)"
    ]
  }
}
```

**Benefits:**
- No permission prompts for allowed operations
- Maintains security for non-allowed operations
- More granular control than bypass mode
- Better for shared repositories

**See**: [fine-grained-permissions.md](./fine-grained-permissions.md)

<!-- section_id: "4f5b530f-903d-4a36-8f21-5fddec09b8b3" -->
## Frequently Asked Questions

<!-- section_id: "17c9b24d-4412-4a69-9178-4ff896a4e4b9" -->
### Q: Is bypass mode safe for personal projects?

**A**: Yes, if:
- You fully control the repository
- No sensitive data is present
- Not connected to production systems
- You understand the implications

<!-- section_id: "6a6b94a3-7911-4e68-a6cb-684a98d7a81e" -->
### Q: Can I use bypass mode in a Docker container?

**A**: Yes, containers provide additional isolation:
```dockerfile
# Dockerfile
FROM python:3.11
WORKDIR /app
COPY .claude/settings.json .claude/
# Bypass mode contained within container
```

<!-- section_id: "8462dcc3-924d-416a-b8e6-7c19a5e22df1" -->
### Q: What happens if I forget bypass mode is enabled?

**A**: Claude Code will operate autonomously without prompts. You may experience:
- Unexpected file modifications
- Commands executed without confirmation
- Potential data loss if destructive operations occur

**Mitigation**: Use deny rules for critical operations.

<!-- section_id: "e551c4f3-cc9b-4ff1-a3ef-c5e07a21d1c7" -->
### Q: Can enterprise policies be bypassed?

**A**: No. Managed policies have highest precedence and cannot be overridden.

<!-- section_id: "a54f9c61-fa7d-40b3-9bf4-4bec1bca3f03" -->
### Q: Does bypass mode affect MCP servers?

**A**: Historically yes (Issue #5307), though this may be fixed in newer versions. Test your specific version.

<!-- section_id: "932b8c13-4d9b-4b40-8ddc-6c7daa51b003" -->
## Related Documentation

- [Fine-Grained Permissions](./fine-grained-permissions.md)
- [Enterprise Security Policies](./enterprise-policies.md)
- [Project Settings Setup](./project-settings.md)
- [Settings Hierarchy](./settings-hierarchy.md)

<!-- section_id: "118f3f2f-35bd-4f78-9116-c2d05b42af09" -->
## External References

- [Official Claude Code Settings Docs](https://docs.claude.com/en/docs/claude-code/settings)
- [IAM Documentation](https://docs.claude.com/en/docs/claude-code/iam)
- [Security Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

<!-- section_id: "500279bb-f6f6-4c42-b351-77008888d3ac" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides implementation patterns for any Claude Code project.*
