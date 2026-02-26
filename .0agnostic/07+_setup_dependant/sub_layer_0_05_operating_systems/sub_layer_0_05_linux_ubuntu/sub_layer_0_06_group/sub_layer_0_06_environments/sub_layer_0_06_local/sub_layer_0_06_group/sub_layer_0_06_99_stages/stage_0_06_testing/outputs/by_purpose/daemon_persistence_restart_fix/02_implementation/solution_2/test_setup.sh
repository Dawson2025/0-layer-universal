#!/bin/bash
# Test Solution 2: Post-Login Hook
# This script creates a GNOME autostart entry that checks daemon health after login

set -e

TEST_NAME="Solution 2: Post-Login Hook (GNOME Autostart)"
RESULTS_FILE="$HOME/.local/var/test-sol2-results-$(date +%Y%m%d-%H%M%S).log"
mkdir -p "$HOME/.local/var"

log() {
  echo "[$(date '+%H:%M:%S')] $1" | tee -a "$RESULTS_FILE"
}

log "========================================"
log "$TEST_NAME"
log "========================================"
log "Timestamp: $(date)"
log ""

# Cleanup previous solutions if present
log "Cleaning up Solution 1 overrides if present..."
rm -rf ~/.config/systemd/user/gnome-session-binary.service.d 2>/dev/null || true
systemctl --user daemon-reload 2>/dev/null || true

# Create daemon health check script
log "Creating daemon health check script..."
mkdir -p ~/.local/bin
cat > ~/.local/bin/daemon-health-check.sh << 'SCRIPT_EOF'
#!/bin/bash
# Post-login daemon health check
# This runs after GNOME session is initialized

DISPLAY=:0
XAUTHORITY=/home/dawson/.Xauthority
export DISPLAY XAUTHORITY

# Wait 5 seconds for gnome-session to fully initialize
sleep 5

# Check and restart daemons if needed
pgrep -x gsd-media-keys > /dev/null 2>&1 || /usr/libexec/gsd-media-keys 2>/dev/null &
pgrep -x gsd-power > /dev/null 2>&1 || /usr/libexec/gsd-power 2>/dev/null &

# Log execution
echo "[$(date '+%H:%M:%S')] Daemon health check executed" >> ~/.local/var/daemon-health-check.log

exit 0
SCRIPT_EOF

chmod +x ~/.local/bin/daemon-health-check.sh
log "✓ Health check script created"

# Create GNOME autostart desktop file
log "Creating GNOME autostart entry..."
mkdir -p ~/.config/autostart
cat > ~/.config/autostart/daemon-health-check.desktop << 'DESKTOP_EOF'
[Desktop Entry]
Type=Application
Name=Daemon Health Check
Exec=/home/dawson/.local/bin/daemon-health-check.sh
OnlyShowIn=GNOME
NoDisplay=true
X-GNOME-Autostart-Phase=PostDisplayServer
X-GNOME-Autostart-Delay=0
DESKTOP_EOF

log "✓ Autostart entry created"

log ""
log "========================================"
log "Solution 2 setup COMPLETE"
log "========================================"
log ""
log "VALIDATION STEPS (perform after RESTART):"
log "1. System restart: sudo systemctl reboot"
log "2. After login, wait 15 seconds for autostart to run"
log "3. Run validation script: test-solution-2-validate.sh"
log ""
log "Daemon health check logs: ~/.local/var/daemon-health-check.log"
log "Results saved to: $RESULTS_FILE"
