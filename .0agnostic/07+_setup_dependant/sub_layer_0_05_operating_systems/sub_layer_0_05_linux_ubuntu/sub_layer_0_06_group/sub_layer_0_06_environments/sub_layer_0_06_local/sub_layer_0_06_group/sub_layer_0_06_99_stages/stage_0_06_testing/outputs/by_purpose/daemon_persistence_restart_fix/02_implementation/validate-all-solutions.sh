#!/bin/bash
# resource_id: "6f44118a-0e86-4caa-97ee-1c51c241511e"
# resource_type: "script"
# resource_name: "validate-all-solutions"
# Comprehensive validation script - run this AFTER restart to test all solutions
# Run once per solution (after setting up and restarting for each)

RESULTS_DIR="$HOME/.local/var"
mkdir -p "$RESULTS_DIR"
VALIDATION_LOG="$RESULTS_DIR/validation-$(date +%Y%m%d-%H%M%S).log"

log() {
  echo "[$(date '+%H:%M:%S')] $1" | tee -a "$VALIDATION_LOG"
}

log "========================================"
log "POST-RESTART VALIDATION"
log "========================================"
log "Timestamp: $(date)"
log "Time since last boot: $(uptime -p)"
log ""

# Test 1: Check if daemons are running
log "TEST 1: Daemon Status"
log "-----------------------"

GSD_MEDIA=$(pgrep -a gsd-media-keys)
GSD_POWER=$(pgrep -a gsd-power)

if [ -n "$GSD_MEDIA" ]; then
  log "✓ gsd-media-keys running: $GSD_MEDIA"
else
  log "✗ gsd-media-keys NOT running"
fi

if [ -n "$GSD_POWER" ]; then
  log "✓ gsd-power running: $GSD_POWER"
else
  log "✗ gsd-power NOT running"
fi

log ""
log "TEST 2: Volume Key Test"
log "-----------------------"

# Get current volume level
VOLUME_BEFORE=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\d+(?=%)')
log "Volume before: $VOLUME_BEFORE%"

# Simulate volume up key press
xdotool key XF86AudioRaiseVolume 2>/dev/null || log "⚠ xdotool not available, skipping key simulation"

sleep 1

VOLUME_AFTER=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\d+(?=%)')
log "Volume after: $VOLUME_AFTER%"

if [ "$VOLUME_AFTER" -gt "$VOLUME_BEFORE" ]; then
  log "✓ Volume key works (volume increased)"
else
  log "✗ Volume key does NOT work (volume unchanged)"
fi

log ""
log "TEST 3: System Services Status"
log "-----------------------"

FAILED_COUNT=$(systemctl --user --failed 2>/dev/null | grep -c "failed" || echo "0")
log "Failed user services: $FAILED_COUNT"

# Check specifically for gsd-* failures
if systemctl --user is-active org.gnome.SettingsDaemon.MediaKeys.service > /dev/null 2>&1; then
  log "✓ org.gnome.SettingsDaemon.MediaKeys.service is active"
else
  log "✗ org.gnome.SettingsDaemon.MediaKeys.service is NOT active"
fi

if systemctl --user is-active org.gnome.SettingsDaemon.Power.service > /dev/null 2>&1; then
  log "✓ org.gnome.SettingsDaemon.Power.service is active"
else
  log "✗ org.gnome.SettingsDaemon.Power.service is NOT active"
fi

log ""
log "TEST 4: Custom Keybinding Check"
log "-----------------------"

# Check if Control-Alt-S would work (verify dbus/session is healthy)
if [ -S /tmp/.X11-unix/X0 ] && pgrep -x gnome-shell > /dev/null; then
  log "✓ X11 and gnome-shell appear healthy"
else
  log "✗ X11 or gnome-shell may have issues"
fi

log ""
log "========================================"
log "VALIDATION COMPLETE"
log "========================================"
log ""
log "Summary:"
if [ -n "$GSD_MEDIA" ] && [ -n "$GSD_POWER" ]; then
  log "✓ OVERALL: Both daemons running - solution appears WORKING"
else
  log "✗ OVERALL: One or more daemons not running - solution did NOT work"
fi

log ""
log "Results saved to: $VALIDATION_LOG"
log "Full results: cat $VALIDATION_LOG"
