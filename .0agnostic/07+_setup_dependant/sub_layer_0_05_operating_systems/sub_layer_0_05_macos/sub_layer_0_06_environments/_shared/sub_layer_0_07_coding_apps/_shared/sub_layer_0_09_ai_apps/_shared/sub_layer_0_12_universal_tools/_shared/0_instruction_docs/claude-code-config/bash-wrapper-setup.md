---
resource_id: "b1a6953b-87cb-4f41-8d27-6984ad1fbe00"
resource_type: "document"
resource_name: "bash-wrapper-setup"
---
# Claude Code Bash Wrapper Setup Guide
*Advanced Configuration: Conditional Bypass Permissions via Shell Wrapper*

<!-- section_id: "c9a83301-f1ca-43ce-97b7-abaf0af06e44" -->
## Overview

This guide documents how to create a bash wrapper function that conditionally enables bypass permissions based on your current directory or environment variables. This approach provides more flexibility than configuration files alone.

<!-- section_id: "60dfd5a6-6de0-4857-9efa-74879a07055c" -->
## Why Use a Bash Wrapper?

<!-- section_id: "2b69c894-c481-449d-9f02-0e1c807f54be" -->
### Advantages

✅ **Context-Aware Bypass**
- Enable bypass only in specific directories
- Control via environment variables
- Different behavior per project

✅ **No Configuration File Changes**
- Works without modifying `.claude/settings.json`
- Doesn't affect version-controlled settings
- Easy to enable/disable globally

✅ **Granular Control**
- Per-directory automation
- Per-session control via environment variables
- Preserves help/version commands

<!-- section_id: "3bcb6192-6870-41bb-b8be-d63689089041" -->
### Disadvantages

❌ **Shell-Specific**
- Only works in bash/zsh
- Doesn't affect Claude Code launched from GUI
- Must configure each shell environment

❌ **Less Discoverable**
- Hidden in shell config files
- Team members won't automatically get it
- Harder to audit than configuration files

<!-- section_id: "1910fd8e-eafd-45a1-a191-63583c46b469" -->
## Implementation

<!-- section_id: "c991dcc0-39f4-4734-9fe7-486cc531001c" -->
### Method 1: Project Directory-Based Bypass

This wrapper enables bypass permissions automatically when you're in a specific project directory.

#### Step 1: Find Claude Binary Path

```bash
which claude
# Output example: /home/username/.nvm/versions/node/v22.20.0/bin/claude
```

Store this path - you'll need it for the wrapper.

#### Step 2: Add Wrapper to ~/.bashrc

Open your `~/.bashrc` (or `~/.zshrc` for zsh):

```bash
nano ~/.bashrc
```

Add this function at the end:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when in project directory
    if [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Important**: Replace:
- `/home/username/.nvm/versions/node/v22.20.0/bin/claude` with your actual path from step 1
- `/home/username/code/my-project` with your project path

#### Step 3: Reload Shell Configuration

```bash
source ~/.bashrc
```

#### Step 4: Verify Wrapper

```bash
# Check the wrapper function exists
typeset -f claude

# Test inside your project directory
cd /home/username/code/my-project
claude -p "echo 'testing bypass'"
# Should run without permission prompts

# Test outside your project directory
cd /tmp
claude -p "echo 'testing normal'"
# Should run with normal permission behavior
```

<!-- section_id: "8644d542-98a8-44ac-bef9-b677f0786729" -->
### Method 2: Environment Variable-Based Bypass

Enable bypass permissions on-demand with an environment variable.

```bash
# >>> CLAUDE_WRAPPER_ENV_VAR_START
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_ENV_VAR_END
```

**Usage:**

```bash
# Normal mode (with permissions)
claude

# Bypass mode (for this session)
CLAUDE_UNSAFE=1 claude

# Or set for entire session
export CLAUDE_UNSAFE=1
claude
# ... work without prompts ...
unset CLAUDE_UNSAFE  # Back to normal
```

<!-- section_id: "e3cac6a6-7a84-4375-93e4-cf9f6d24d329" -->
### Method 3: Combined Approach (Recommended)

Combine both methods for maximum flexibility:

```bash
# >>> CLAUDE_WRAPPER_COMBINED_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 OR in project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_COMBINED_END
```

**Behavior:**
- Inside `/home/username/code/my-project`: Bypass enabled automatically
- Outside that directory: Normal permissions
- Anywhere with `CLAUDE_UNSAFE=1`: Bypass enabled
- `--help` and `--version`: Always work normally

<!-- section_id: "45cb4353-5b70-4c13-8e0c-de4dbdff948c" -->
## Real-World Example

Here's the exact wrapper from the Lang-Trak project:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/dawson/.nvm/versions/node/v22.20.0/bin/claude"
if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 or when in the project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/dawson/code/lang-trak-in-progress"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Testing Results:**
```bash
# Inside project
$ cd /home/dawson/code/lang-trak-in-progress
$ claude -p "echo hello"
hello  # No permission prompt

# Outside project
$ cd /tmp
$ claude -p "echo hello"
# Permission prompt appears (normal behavior)

# Override from outside project
$ cd /tmp
$ CLAUDE_UNSAFE=1 claude -p "echo hello"
hello  # No permission prompt
```

<!-- section_id: "6fcaa7d2-0f39-409e-955b-d97cfb27c827" -->
## Advanced Configurations

<!-- section_id: "33890b2f-bd22-435e-bcae-1b9bba93381f" -->
### Multiple Project Directories

Enable bypass for multiple projects:

```bash
claude() {
  # ... help/version handling ...

  # List of trusted project directories
  local trusted_dirs=(
    "/home/username/code/personal-project"
    "/home/username/code/side-project"
    "/home/username/experiments"
  )

  # Check if current directory starts with any trusted path
  local bypass=0
  for dir in "${trusted_dirs[@]}"; do
    if [[ "$PWD" == "$dir"* ]]; then
      bypass=1
      break
    fi
  done

  # Enable bypass if in trusted directory or CLAUDE_UNSAFE=1
  if [ "$bypass" = "1" ] || [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "95268dee-7813-497f-a2dc-f2b22dc96a8a" -->
### Time-Based Bypass

Automatically disable bypass during certain hours (e.g., working hours for client projects):

```bash
claude() {
  # ... help/version handling ...

  # Get current hour (0-23)
  local hour=$(date +%H)

  # Disable bypass during working hours (9 AM - 5 PM)
  if [ "$hour" -ge 9 ] && [ "$hour" -lt 17 ]; then
    # Normal mode during work hours
    command "$_claude_real" "$@"
  else
    # Bypass enabled outside work hours
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/personal"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  fi
}
```

<!-- section_id: "bfec1881-0f37-46b8-b417-7b472666dfa5" -->
### Git Repository Detection

Enable bypass only in git repositories you own:

```bash
claude() {
  # ... help/version handling ...

  # Check if in a git repo
  if git rev-parse --git-dir > /dev/null 2>&1; then
    # Get git user email
    local git_email=$(git config user.email)

    # Enable bypass if it's your personal email
    if [[ "$git_email" == "personal@example.com" ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  else
    # Not in a git repo - normal mode
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "16f3bca4-e9c1-4e2a-961d-4fcf057bb116" -->
## Debugging

<!-- section_id: "7f6931b5-2d1a-454e-8bee-f7d8a505c2f2" -->
### Check if Wrapper is Active

```bash
# View the current wrapper function
typeset -f claude

# Check which claude command is being used
type claude
# Should output: claude is a function
```

<!-- section_id: "17d2dc30-be21-4590-8a0c-c555c7f6acad" -->
### Test Without Wrapper

To temporarily bypass the wrapper and use the real binary:

```bash
# Use full path
/home/username/.nvm/versions/node/v22.20.0/bin/claude

# Or use command builtin
command /path/to/real/claude
```

<!-- section_id: "a613adf0-bdea-420e-bc10-3a71d1838ecf" -->
### Enable Debug Output

Add debugging to your wrapper:

```bash
claude() {
  # Debug mode
  if [ "${CLAUDE_DEBUG:-0}" = "1" ]; then
    echo "[DEBUG] PWD: $PWD"
    echo "[DEBUG] CLAUDE_UNSAFE: ${CLAUDE_UNSAFE:-0}"
    echo "[DEBUG] Will use bypass: $([ condition ] && echo yes || echo no)"
  fi

  # ... rest of wrapper ...
}
```

Usage:
```bash
CLAUDE_DEBUG=1 claude -p "echo test"
```

<!-- section_id: "529709c6-a42a-46d2-a674-b73aeec00388" -->
## Removing the Wrapper

<!-- section_id: "c3654208-945d-422d-b7a3-1d5b31f86b8f" -->
### Temporary Removal (Current Session)

```bash
unset -f claude
```

<!-- section_id: "80b6b1bb-3adf-46a7-bf09-989a25d8da2d" -->
### Permanent Removal

1. Edit `~/.bashrc`:
   ```bash
   nano ~/.bashrc
   ```

2. Remove the wrapper block (between the comment markers)

3. Reload shell:
   ```bash
   source ~/.bashrc
   ```

4. Verify:
   ```bash
   type claude
   # Should output the path to the binary, not "claude is a function"
   ```

<!-- section_id: "49b0758d-7963-4676-b7ba-f89716f6e413" -->
## Security Considerations

<!-- section_id: "e8940f62-ed82-49f5-8e4b-0ee059d1c853" -->
### Risks

⚠️ **Directory-Based Bypass**
- Anyone with access to the directory gets bypass mode
- Symbolic links could potentially exploit path matching
- Subdirectories inherit bypass behavior

⚠️ **Environment Variable Bypass**
- Environment variables can be set by scripts
- Child processes inherit `CLAUDE_UNSAFE=1`
- Easy to forget it's enabled

⚠️ **Shell Configuration Files**
- `~/.bashrc` is executable code
- Errors can break your shell
- Hard for others to discover the bypass is active

<!-- section_id: "23c0ac41-ec7c-4d23-8d79-214d9583006a" -->
### Mitigations

✅ **Add Visual Indicators**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "⚠️  BYPASS MODE ACTIVE" >&2
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Log Bypass Usage**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "$(date): Bypass enabled in $PWD" >> ~/.claude/bypass.log
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Restrict by Ownership**

```bash
claude() {
  # Only enable bypass if you own the directory
  if [ -O "$PWD" ] && [[ "$PWD" == "/home/username/code"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "8cde5c8f-d01d-42fd-a828-6157c55e2d80" -->
## Integration with Configuration Files

The bash wrapper approach **works alongside** `.claude/settings.json` configurations:

<!-- section_id: "2c1b697a-80a8-491a-930e-6dedbfe25139" -->
### Precedence

1. **Bash Wrapper** (highest)
   - If wrapper adds `--dangerously-skip-permissions`, that takes effect

2. **Command-Line Flags**
   - Flags passed to the wrapper are forwarded

3. **Configuration Files**
   - `.claude/settings.json` and `.claude/settings.local.json`
   - Still respected when wrapper doesn't add bypass flag

<!-- section_id: "70c8df5a-83bf-4759-ba75-e4ca6c27ea77" -->
### Example: Hybrid Approach

```bash
# ~/.bashrc - Project directory gets wrapper bypass
claude() {
  if [[ "$PWD" == "/home/username/code/personal"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

```json
// /home/username/code/work-project/.claude/settings.local.json
// Work project uses fine-grained permissions
{
  "permissions": {
    "allow": [
      "Read(src/**)",
      "Edit(src/**)",
      "Bash(npm test)"
    ]
  }
}
```

**Result:**
- Personal projects: Full bypass via wrapper
- Work projects: Fine-grained permissions via config files
- Other directories: Default Claude Code behavior

<!-- section_id: "4d3c175a-68a4-430b-b202-e8d34b1812aa" -->
## Frequently Asked Questions

<!-- section_id: "0f6a8cce-41db-49c1-8a35-d090afd7b131" -->
### Q: Does this work with VS Code?

**A**: Only if you launch Claude Code from the terminal. If you launch VS Code from a GUI, it won't inherit your shell configuration.

**Workaround**: Set environment variables in VS Code settings:
```json
{
  "terminal.integrated.env.linux": {
    "CLAUDE_UNSAFE": "1"
  }
}
```

<!-- section_id: "6f3bb71f-d71e-4ffd-9640-6620688fea59" -->
### Q: Can I use this with zsh?

**A**: Yes, the syntax is compatible. Just add the wrapper to `~/.zshrc` instead of `~/.bashrc`.

<!-- section_id: "03d8efe7-f34a-4b05-a8d4-17a10b40d776" -->
### Q: What about fish shell?

**A**: Fish uses different syntax. Here's the equivalent:

```fish
# ~/.config/fish/functions/claude.fish
function claude
    set -l claude_real /home/username/.nvm/versions/node/v22.20.0/bin/claude

    # Check for help/version
    for arg in $argv
        switch $arg
            case --help -h --version -v
                command $claude_real $argv
                return
        end
    end

    # Enable bypass in project directory
    if string match -q "/home/username/code/my-project*" $PWD
        command $claude_real --dangerously-skip-permissions $argv
    else
        command $claude_real $argv
    end
end
```

<!-- section_id: "891ee0d4-0af5-4cdf-92bf-79bd62f859e0" -->
### Q: Can I check if bypass is active before running a command?

**A**: Yes, add a helper function:

```bash
claude-bypass-check() {
  if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/trusted"* ]]; then
    echo "✅ Bypass ACTIVE"
  else
    echo "❌ Bypass INACTIVE (normal permissions)"
  fi
}
```

Usage:
```bash
$ claude-bypass-check
✅ Bypass ACTIVE
```

<!-- section_id: "c91de4ae-5a37-40eb-b12e-28f7720d4bf2" -->
### Q: How do I share this with my team?

**A**: Document it in your project's README and provide a setup script:

```bash
#!/bin/bash
# scripts/setup-claude-wrapper.sh

CLAUDE_PATH=$(which claude)
PROJECT_PATH=$(pwd)

cat >> ~/.bashrc << EOF

# Auto-generated Claude wrapper for $(basename "$PROJECT_PATH")
_claude_real="$CLAUDE_PATH"
if [ -x "\$_claude_real" ]; then
  claude() {
    for arg in "\$@"; do
      case "\$arg" in
        --help|-h|--version|-v)
          command "\$_claude_real" "\$@"
          return \$?
          ;;
      esac
    done

    if [[ "\$PWD" == "$PROJECT_PATH"* ]]; then
      command "\$_claude_real" --dangerously-skip-permissions "\$@"
    else
      command "\$_claude_real" "\$@"
    fi
  }
fi
EOF

echo "✅ Claude wrapper added to ~/.bashrc"
echo "Run: source ~/.bashrc"
```

<!-- section_id: "7fa79b0c-7676-4ee5-b731-01a12faa0386" -->
## Related Documentation

- [Bypass Permissions Setup](./bypass-permissions-setup.md) - Configuration file approach
- [Fine-Grained Permissions](./fine-grained-permissions.md) - Alternative to bypass mode
- [Settings Hierarchy](./settings-hierarchy.md) - How settings interact

<!-- section_id: "bba35bc6-be39-4194-ba5d-86e61d2cc26e" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides advanced implementation patterns for Claude Code bypass permissions.*
