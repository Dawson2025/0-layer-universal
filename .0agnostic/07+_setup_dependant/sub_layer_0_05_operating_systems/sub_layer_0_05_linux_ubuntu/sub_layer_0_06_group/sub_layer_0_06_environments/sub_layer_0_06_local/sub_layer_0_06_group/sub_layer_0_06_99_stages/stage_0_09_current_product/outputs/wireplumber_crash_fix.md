---
resource_id: "197d24a1-7853-43de-b248-a6d4490c7873"
resource_type: "output"
resource_name: "wireplumber_crash_fix"
---
# WirePlumber Crash Fix

<!-- section_id: "01de2a20-f625-4e48-8b21-7fcad92fdbde" -->
## Problem

WirePlumber service repeatedly failing on startup, causing:
- No audio hardware sinks available
- Only `auto_null` sink visible
- Audio completely non-functional

<!-- section_id: "64185621-1bac-47d1-89e5-d24944713dfa" -->
## Root Cause

A custom WirePlumber Lua script had a bug:

**File:** `~/.config/wireplumber/main.lua.d/51-easyeffects-volume.lua`

```lua
-- The problematic code:
table.insert(default_nodes_rules, rule)
-- ERROR: default_nodes_rules is nil (doesn't exist in current WirePlumber)
```

The script referenced `default_nodes_rules` which doesn't exist in the current WirePlumber version. This was likely created based on outdated documentation or a different WirePlumber version.

<!-- section_id: "5092ae82-c29a-49e5-8f4d-fbc73fb6feac" -->
### Error Evidence

```
wireplumber[31457]: [string "51-easyeffects-volume.lua"]:13: bad argument #1 to 'insert' (table expected, got nil)
wireplumber[31457]: Lua runtime error
systemd[2662]: wireplumber.service: Main process exited, code=exited, status=70/SOFTWARE
wireplumber.service: Start request repeated too quickly.
wireplumber.service: Failed with result 'exit-code'.
```

<!-- section_id: "34161917-0c86-4eb0-8a9b-f3f9b9390134" -->
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

<!-- section_id: "007bbc9b-f4d7-45bf-b1af-8009b6c89ad6" -->
## Verification

```bash
# Check WirePlumber is running
systemctl --user status wireplumber

# Check audio sinks are available
pactl list sinks short
# Should show hardware sinks, not just auto_null
```

<!-- section_id: "e0fcfe1e-48e7-4a4a-bcdc-3361e64632db" -->
## Notes

- The script was attempting to modify EasyEffects sink behavior
- This functionality is not needed - EasyEffects works fine without it
- Audio routing is handled through `pactl set-default-sink` commands instead

<!-- section_id: "84e03d68-7b59-4ad2-ab34-ddeac50155d5" -->
## Related Issues

- audio_quality_degraded (now using captured Dolby IR)
- gsd_daemon_failures (volume buttons)
