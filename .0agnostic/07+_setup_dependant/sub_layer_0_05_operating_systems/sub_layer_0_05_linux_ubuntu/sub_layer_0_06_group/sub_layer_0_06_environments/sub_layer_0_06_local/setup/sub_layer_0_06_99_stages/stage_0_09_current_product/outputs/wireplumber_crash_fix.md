# WirePlumber Crash Fix

## Problem

WirePlumber service repeatedly failing on startup, causing:
- No audio hardware sinks available
- Only `auto_null` sink visible
- Audio completely non-functional

## Root Cause

A custom WirePlumber Lua script had a bug:

**File:** `~/.config/wireplumber/main.lua.d/51-easyeffects-volume.lua`

```lua
-- The problematic code:
table.insert(default_nodes_rules, rule)
-- ERROR: default_nodes_rules is nil (doesn't exist in current WirePlumber)
```

The script referenced `default_nodes_rules` which doesn't exist in the current WirePlumber version. This was likely created based on outdated documentation or a different WirePlumber version.

### Error Evidence

```
wireplumber[31457]: [string "51-easyeffects-volume.lua"]:13: bad argument #1 to 'insert' (table expected, got nil)
wireplumber[31457]: Lua runtime error
systemd[2662]: wireplumber.service: Main process exited, code=exited, status=70/SOFTWARE
wireplumber.service: Start request repeated too quickly.
wireplumber.service: Failed with result 'exit-code'.
```

## Solution

Disabled the problematic script:

```bash
mv ~/.config/wireplumber/main.lua.d/51-easyeffects-volume.lua \
   ~/.config/wireplumber/main.lua.d/51-easyeffects-volume.lua.disabled
```

Then restarted the PipeWire stack:

```bash
systemctl --user reset-failed wireplumber
systemctl --user restart pipewire pipewire-pulse wireplumber
```

## Verification

```bash
# Check WirePlumber is running
systemctl --user status wireplumber

# Check audio sinks are available
pactl list sinks short
# Should show hardware sinks, not just auto_null
```

## Notes

- The script was attempting to modify EasyEffects sink behavior
- This functionality is not needed - EasyEffects works fine without it
- Audio routing is handled through `pactl set-default-sink` commands instead

## Related Issues

- audio_quality_degraded (now using captured Dolby IR)
- gsd_daemon_failures (volume buttons)
